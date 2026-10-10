"""Copy a cache-only client instance and register a fresh official launcher installation."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import tempfile
import tomllib
import uuid

import export_instance as instance


def ensure_closed(proc=Path("/proc")):
    """Fail closed on unreadable process state; never disclose command arguments."""
    if not proc.is_dir():
        raise RuntimeError("Linux process inspection is unavailable; registration refused")
    for process in proc.iterdir():
        if not process.name.isdigit():
            continue
        try:
            comm = (process / "comm").read_text().strip()
            if comm == "minecraft-launc" or comm.startswith("minecraft-laun"):
                raise RuntimeError("Official Minecraft launcher is running; close it before export")
            if comm in ("java", "javaw"):
                arguments = (process / "cmdline").read_bytes().lower()
                indicators = (b"net.minecraft.", b"net.neoforged.", b"neoforgeclient",
                              b"neoforgeserver", b"cpw.mods.bootstraplauncher.bootstraplauncher",
                              b"cpw.mods.modlauncher.launcher")
                if any(indicator in arguments for indicator in indicators):
                    raise RuntimeError("Minecraft or NeoForge is running; close it before export")
        except FileNotFoundError:
            # A process may exit during inspection.
            continue
        except OSError as exc:
            raise RuntimeError("Cannot inspect Linux process state; registration refused") from exc


def saved_profile(template, requirements):
    """Only safe built-in icon names and custom type may come from a template."""
    instance.template_layout(template, requirements)
    metadata = json.loads(instance.regular(template / "template.json").read_bytes())
    if set(metadata) - {"game_version", "loader", "loader_version", "launcher_profile"}:
        raise ValueError("Template contains unsupported fields")
    profile = metadata.get("launcher_profile")
    if not isinstance(profile, dict) or set(profile) - {"icon", "type"}:
        raise ValueError("Template launcher_profile must contain only icon and type")
    if profile.get("type", "custom") != "custom":
        raise ValueError("Template launcher profile type must be custom")
    icon = profile.get("icon")
    if icon is not None and (not isinstance(icon, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,63}", icon)):
        raise ValueError("Template icon must be a safe built-in launcher icon name")
    return {"icon": icon} if icon is not None else {}


def export(output=None, *, source=instance.SOURCE, cache=instance.CACHE, template=None):
    home = Path.home()
    pack = tomllib.loads(instance.regular(Path(source) / "pack.toml").read_text())
    version = pack["version"]
    instance.safe_relative(version)
    runtime_id = "neoforge-" + pack["versions"]["neoforge"]
    instance.safe_relative(runtime_id)
    runtime_path = home / ".minecraft/versions" / runtime_id / f"{runtime_id}.json"
    try:
        runtime = json.loads(instance.regular(runtime_path).read_bytes())
    except FileNotFoundError as exc:
        raise ValueError(f"Missing installed loader runtime manifest: {runtime_path}") from exc
    if not isinstance(runtime, dict):
        raise ValueError("Installed runtime manifest must be an object")
    if runtime.get("id") != runtime_id or runtime.get("inheritsFrom") != pack["versions"]["minecraft"]:
        raise ValueError("Installed runtime identifier or Minecraft inheritance does not match source pack")
    default_template = home / "Projects/lucas/instance-templates" / f"official-neoforge-{pack['versions']['minecraft']}"
    template = instance.checked_path(template) if template else default_template if (default_template / "template.json").exists() else None
    requirements = {"minecraft": pack["versions"]["minecraft"], "loader": "neoforge", "loader_version": pack["versions"]["neoforge"]}
    template_fields = saved_profile(template, requirements) if template else {}
    timestamp = datetime.now(timezone.utc)
    stamp = timestamp.strftime("%Y%m%dT%H%M%S%fZ")
    identifier = uuid.uuid4().hex
    output = instance.checked_path(output or home / "Projects/lucas/instance-runs" / f"astropunk-{version}-{stamp}-{identifier[:8]}")
    profiles_path = instance.regular(home / ".minecraft/launcher_profiles.json")
    ensure_closed()
    original_bytes = profiles_path.read_bytes()
    original = json.loads(original_bytes)
    if not isinstance(original, dict) or not isinstance(original.get("profiles"), dict):
        raise ValueError("Launcher profiles must contain a profiles mapping")
    manifest = instance.export(output, source=source, cache=cache, template=template)
    try:
        iso = timestamp.isoformat(timespec="milliseconds").replace("+00:00", "Z")
        profile = {"name": f"Astropunk Guide Test {version} {stamp} {identifier[:8]}",
                   "type": "custom", "gameDir": str(output / "game"), "lastVersionId": runtime_id,
                   "created": iso, "lastUsed": iso, "javaArgs": "-Xmx6G"}
        profile.update(template_fields)
        updated = json.loads(original_bytes)
        if identifier in updated["profiles"]:
            raise RuntimeError("New launcher profile identifier already exists")
        updated["profiles"][identifier] = profile
        backups = instance.checked_path(home / "Projects/lucas/instance-templates" / f"official-neoforge-{pack['versions']['minecraft']}" / "backups")
        backups.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(backups, 0o700)
        backup = backups / f"launcher_profiles-{stamp}-{identifier}.json"
        with backup.open("xb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(original_bytes)
            stream.flush()
            os.fsync(stream.fileno())
        fd, temporary = tempfile.mkstemp(prefix=".official-profile-", dir=profiles_path.parent)
        try:
            with os.fdopen(fd, "w") as stream:
                json.dump(updated, stream, indent=2)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            ensure_closed()
            if instance.regular(profiles_path).read_bytes() != original_bytes:
                raise RuntimeError("Launcher profiles changed concurrently; registration refused")
            os.replace(temporary, profiles_path)
            readback = json.loads(instance.regular(profiles_path).read_bytes())
            if readback != updated or readback["profiles"].get(identifier) != profile:
                raise RuntimeError("Launcher profile readback verification failed")
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        manifest["official_launcher"] = {"profile_id": identifier, "profiles_path": str(profiles_path)}
        (output / "instance-export.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        return manifest
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as exc:
        raise RuntimeError(f"Official registration failed: {exc}. Prepared game folder preserved at {output / 'game'}; do not repeat into the same destination.") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", default="", help="Empty means a unique instance-runs destination")
    parser.add_argument("--template", default="", help="Optional durable official template directory")
    parser.add_argument("--source", type=Path, default=instance.SOURCE)
    parser.add_argument("--cache", type=Path, default=instance.CACHE)
    args = parser.parse_args()
    try:
        manifest = export(args.output, source=args.source, cache=args.cache, template=args.template)
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as exc:
        parser.exit(1, f"Official instance export failed: {exc}\n")
    print(f"Registered {manifest['official_launcher']['profile_id']} for {manifest['pack_version']}")


if __name__ == "__main__":
    main()
