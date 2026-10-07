set export
PYTHONDONTWRITEBYTECODE := "1"
PACK_VERSION := `python -c 'import tomllib; print(tomllib.load(open("pack.toml", "rb"))["version"])'`

# List available tasks.
default:
    @just --list

# Native CurseForge server export.
export-server output=("dist/aeropunk-" + PACK_VERSION + "-server.zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side server --output {{quote(output)}}

# Native CurseForge client pack export.
export-curseforge output=("dist/aeropunk-" + PACK_VERSION + "-curseforge.zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side client --output {{quote(output)}}

# Native Modrinth export with installer-managed side selection.
export-modrinth output=("dist/aeropunk-" + PACK_VERSION + "-modrinth.mrpack"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz modrinth export --output {{quote(output)}}

# Update external files, respecting documented compatibility holds.
update:
    packwiz update --all

# Export and boot an isolated Docker server, reusing installed binaries by default.
test *args:
    python scripts/test_server.py {{args}}

# Remove temporary runs and Python bytecode; keep versioned exports, reports and installation.
clean:
    python scripts/tasks.py clean
