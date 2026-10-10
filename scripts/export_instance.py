"""Materialize a client game folder from verified pack files and native cache only."""
import argparse
import ctypes
import errno
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile
import tomllib

SOURCE = Path(__file__).absolute().parents[1]
CACHE = Path.home() / ".cache/packwiz/cache"


def safe_relative(value):
    if (not isinstance(value, str) or not value or value.startswith("/")
            or "\\" in value or ":" in value or any(ord(c) < 32 for c in value)
            or any(part in ("", ".", "..") for part in value.split("/"))):
        raise ValueError(f"Unsafe relative path: {value!r}")
    return PurePosixPath(value)


def checked_path(value):
    """Check every component before resolving, including dangling symlinks."""
    path = Path(os.path.abspath(value))
    for component in (*reversed(path.parents), path):
        if component.is_symlink():
            raise ValueError(f"Symlink forbidden: {component}")
    return path


def regular(path):
    checked_path(path)
    if not stat.S_ISREG(path.stat().st_mode):
        raise ValueError(f"Expected a regular file: {path}")
    return path


def checksum(path, algorithm):
    try:
        hasher = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"Unsupported checksum algorithm: {algorithm}") from exc
    with regular(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def verify(path, algorithm, expected):
    if checksum(path, algorithm) != expected:
        raise ValueError(f"File checksum mismatch ({algorithm}): {path}")


def overlaps(first, second):
    return first == second or first in second.parents or second in first.parents


def claim(relative, files, directories):
    if relative in files or relative in directories or any(p in files for p in relative.parents):
        raise ValueError(f"Destination collision: {relative}")
    files.add(relative)
    directories.update(relative.parents)


def cache_lookup(cache, artifacts):
    if not artifacts:
        return {}
    try:
        index = json.loads(regular(cache / "index.json").read_text())
    except FileNotFoundError as exc:
        raise ValueError(f"Missing cached artifact index: {cache / 'index.json'}; no network fallback") from exc
    hashes = index.get("Hashes")
    if index.get("Version") != 2 or not isinstance(hashes, dict):
        raise ValueError("Expected native packwiz cache Version 2 Hashes mapping")
    canonical = hashes.get("sha256")
    if not isinstance(canonical, list) or any(not isinstance(v, list) or len(v) != len(canonical) for v in hashes.values()):
        raise ValueError("Invalid native cache parallel hash arrays")
    result = {}
    for metadata, relative in artifacts:
        download = metadata["download"]
        algorithm, declared = download["hash-format"], download["hash"]
        values = hashes.get(algorithm, [])
        matches = [i for i, value in enumerate(values) if value == declared]
        if not matches:
            raise ValueError(f"Missing cached artifact: {relative} ({algorithm}: {declared}); no network fallback")
        names = {canonical[i] for i in matches}
        if len(names) != 1:
            raise ValueError(f"Ambiguous cache mapping: {relative}")
        name = names.pop()
        if not isinstance(name, str) or not re.fullmatch(r"[0-9a-f]{64}", name):
            raise ValueError(f"Unsafe canonical cache checksum: {name!r}")
        path = checked_path(cache / name[:2] / name[2:])
        if not path.exists():
            raise ValueError(f"Missing cached artifact: {relative} at {path}; no network fallback")
        verify(path, algorithm, declared)
        verify(path, "sha256", name)
        result[relative] = (path, algorithm, declared)
    return result


def template_layout(template, requirements):
    metadata = json.loads(regular(template / "template.json").read_text())
    expected = {"game_version": requirements["minecraft"], "loader": requirements["loader"],
                "loader_version": requirements["loader_version"]}
    if any(metadata.get(key) != value for key, value in expected.items()):
        raise ValueError(f"Template requirements do not match pack: expected {expected}")
    game = checked_path(template / "game")
    if not game.is_dir():
        raise ValueError("Template must contain a game directory")
    directories = []
    for root, children, files in os.walk(game, followlinks=False):
        for name in children + files:
            path = checked_path(Path(root) / name)
            if not path.is_dir():
                raise ValueError(f"Template game must contain no regular files or special files: {path}")
            directories.append(safe_relative(path.relative_to(game).as_posix()))
    return directories


def publish(stage, output):
    """Linux atomic publication without replacing a concurrently created output."""
    library = ctypes.CDLL(None, use_errno=True)
    rename = getattr(library, "renameat2", None)
    if rename is None:
        raise RuntimeError("Atomic no-replace directory publication requires renameat2")
    rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    rename.restype = ctypes.c_int
    if rename(-100, os.fsencode(stage), -100, os.fsencode(output), 1) != 0:
        code = ctypes.get_errno()
        if code == errno.EEXIST:
            raise ValueError(f"Output already exists: {output}")
        raise OSError(code, os.strerror(code), str(output))


def export(output: Path, *, source: Path = SOURCE, cache: Path = CACHE, template=None):
    source, cache, output = (checked_path(path) for path in (source, cache, output))
    template = checked_path(template) if template else None
    # dist is the dedicated generated-output subtree, never an indexed input.
    in_dist = source / "dist" in output.parents
    if (overlaps(output, source) and not in_dist) or overlaps(output, cache):
        raise ValueError("Source or cache and output overlap")
    if template and overlaps(output, template):
        raise ValueError("Template and output overlap")
    if output.exists():
        raise ValueError(f"Output already exists: {output}")
    pack = tomllib.loads(regular(source / "pack.toml").read_text())
    index_path = source / safe_relative(pack["index"]["file"])
    verify(index_path, pack["index"]["hash-format"], pack["index"]["hash"])
    index = tomllib.loads(index_path.read_text())
    versions = pack["versions"]
    loaders = [key for key in versions if key in ("neoforge", "forge", "fabric", "quilt")]
    if loaders != ["neoforge"]:
        raise ValueError("Pack must declare exactly the neoforge loader")
    requirements = {"minecraft": versions["minecraft"], "loader": "neoforge", "loader_version": versions["neoforge"]}
    layout = template_layout(template, requirements) if template else []
    plan, artifacts = {}, []
    destinations, directories, indexed = set(), set(layout), set()
    excluded = 0
    # Validate destinations before any writes, then verify every index entry.
    entries = []
    for entry in index.get("files", []):
        relative = safe_relative(entry["file"])
        if relative in indexed:
            raise ValueError(f"Duplicate indexed file: {relative}")
        indexed.add(relative)
        path = source / relative
        if overlaps(path, output) or source / "dist" in path.parents:
            raise ValueError(f"Indexed source and output overlap: {relative}")
        if entry.get("metafile", False):
            if not str(relative).endswith(".pw.toml"):
                raise ValueError(f"Expected indexed .pw.toml metafile: {relative}")
            verify(path, entry.get("hash-format", index["hash-format"]), entry["hash"])
            metadata = tomllib.loads(path.read_text())
            target = relative.parent / safe_relative(metadata["filename"])
            side = metadata.get("side", "both")
            if side not in ("server", "client", "both"):
                raise ValueError(f"Invalid artifact side: {side}")
            if side == "server":
                excluded += 1
                entries.append((path, entry))
                continue
            claim(target, destinations, directories)
            artifacts.append((metadata, target))
        else:
            claim(relative, destinations, directories)
            plan[relative] = (path, entry.get("hash-format", index["hash-format"]), entry["hash"])
        entries.append((path, entry))
    for path, entry in entries:
        verify(path, entry.get("hash-format", index["hash-format"]), entry["hash"])
    ordinary_count = len(plan)
    plan.update(cache_lookup(cache, artifacts))
    output.parent.mkdir(parents=True, exist_ok=True)
    checked_path(output.parent)
    stage = Path(tempfile.mkdtemp(prefix=".instance-export-", dir=output.parent))
    try:
        game = stage / "game"
        game.mkdir()
        for relative in sorted(layout):
            (game / relative).mkdir(parents=True, exist_ok=True)
        owned = {}
        for relative, (path, algorithm, expected) in sorted(plan.items()):
            target = game / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            regular(path)
            shutil.copyfile(path, target)
            verify(target, algorithm, expected)
            owned["game/" + str(relative)] = checksum(target, "sha256")
        manifest = {"format_version": 1, "pack_name": pack.get("name"), "pack_version": pack["version"],
                    "requirements": requirements, "files": owned,
                    "counts": {"files": len(owned), "ordinary_files": ordinary_count,
                               "cached_artifacts": len(artifacts), "server_excluded": excluded,
                               "indexed_files": len(entries), "template_directories": len(layout)}}
        (stage / "instance-export.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        publish(stage, output)
        return manifest
    finally:
        # Only this invocation's newly created staging directory is disposable.
        if stage.exists():
            shutil.rmtree(stage)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--template", default="", help="Empty durable template directory; empty string means absent")
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--cache", type=Path, default=CACHE)
    args = parser.parse_args()
    try:
        manifest = export(args.output, source=args.source, cache=args.cache, template=args.template)
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as exc:
        parser.exit(1, f"Instance export failed: {exc}\n")
    print(f"Created {args.output} with {manifest['counts']['files']} independently copied game files")


if __name__ == "__main__":
    main()
