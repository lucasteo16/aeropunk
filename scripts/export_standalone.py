"""Bundle a client mrpack using native packwiz exports and its existing cache."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import tempfile
import zipfile


def export(output: Path) -> None:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    # Native exporters select artifacts, resolve providers and reuse packwiz's cache.
    with tempfile.TemporaryDirectory(prefix="astropunk-standalone-") as directory:
        directory = Path(directory)
        native = directory / "native.mrpack"
        materialized = directory / "client.zip"
        subprocess.run(["packwiz", "modrinth", "export", "--output", str(native)], check=True)
        subprocess.run(["packwiz", "curseforge", "export", "--side", "client", "--output", str(materialized)], check=True)
        with zipfile.ZipFile(native) as source, zipfile.ZipFile(materialized) as client:
            manifest = json.loads(source.read("modrinth.index.json"))
            bundled = []
            skipped = []
            stage = directory / "standalone.mrpack"
            names = set()
            with zipfile.ZipFile(stage, "w", zipfile.ZIP_DEFLATED) as target:
                for entry in source.infolist():
                    if entry.filename == "modrinth.index.json":
                        continue
                    target.writestr(entry, source.read(entry))
                    names.add(entry.filename)
                for entry in manifest["files"]:
                    path = entry["path"]
                    if entry.get("env", {}).get("client") == "unsupported":
                        skipped.append(path)
                        continue
                    parsed = PurePosixPath(path)
                    if parsed.is_absolute() or ".." in parsed.parts or "\\" in path or ":" in path:
                        raise ValueError(f"Unsafe artifact path: {path}")
                    # CurseForge's native client export embeds the Modrinth download entries.
                    candidate = "overrides/" + path
                    if candidate not in client.namelist():
                        raise RuntimeError(f"Native client export did not materialize {path}")
                    content = client.read(candidate)
                    for algorithm in ("sha1", "sha512"):
                        if hashlib.new(algorithm, content).hexdigest() != entry["hashes"][algorithm]:
                            raise ValueError(f"Artifact checksum mismatch: {path}")
                    destination = "client-overrides/" + path
                    if destination in names or candidate in names:
                        raise ValueError(f"Duplicate artifact: {path}")
                    target.writestr(destination, content)
                    names.add(destination)
                    bundled.append(path)
                manifest["files"] = []
                target.writestr("modrinth.index.json", json.dumps(manifest, indent=2) + "\n")
            with zipfile.ZipFile(stage) as verify:
                if verify.testzip() is not None:
                    raise ValueError("Archive integrity failure")
                if json.loads(verify.read("modrinth.index.json"))["files"]:
                    raise ValueError("Standalone pack still has download entries")
            stage.replace(output)
            print(f"Created {output}")
            print(f"Bundled {len(bundled)} manifest artifacts; excluded {len(skipped)} server-only entries.")
            print("Native bundled overrides preserved. No mod download entries remain.")
            print("Minecraft, loader, Java and authentication remain launcher-managed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    export(parser.parse_args().output)
