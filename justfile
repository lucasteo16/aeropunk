set export
PYTHONDONTWRITEBYTECODE := "1"
PACK_VERSION := `python -c 'import tomllib; print(tomllib.load(open("pack.toml", "rb"))["version"])'`

# List available tasks.
default:
    @just --list

# Native CurseForge server export.
export-server output=("dist/astropunk-" + PACK_VERSION + "-server.zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side server --output {{quote(output)}}

# Native CurseForge client pack export.
export-curseforge output=("dist/astropunk-" + PACK_VERSION + "-curseforge.zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side client --output {{quote(output)}}

# Native Modrinth export with installer-managed side selection.
export-modrinth output=("dist/astropunk-" + PACK_VERSION + "-modrinth.mrpack"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz modrinth export --output {{quote(output)}}

# Self-contained client pack, with all client artifacts bundled.
export-standalone output=("dist/astropunk-" + PACK_VERSION + "-standalone.mrpack"):
    python scripts/export_standalone.py {{quote(output)}}

# Cache-only uncompressed client folder and a new official launcher installation.
export-instance output="" template="":
    python scripts/export_official_instance.py {{quote(output)}} --template {{quote(template)}}

# Update external files, respecting documented compatibility holds.
update:
    packwiz update --all

# Export and boot an isolated Docker server, reusing installed binaries by default.
test *args:
    python scripts/test_server.py {{args}}

# Remove temporary runs and Python bytecode; keep versioned exports, reports and installation.
clean:
    python scripts/tasks.py clean
