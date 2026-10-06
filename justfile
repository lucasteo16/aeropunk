set export
PYTHONDONTWRITEBYTECODE := "1"

# List available tasks.
default:
    @just --list

# Native CurseForge export. Specify client or server and an optional output path.
export side="server" output=("dist/aeropunk-" + side + ".zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side {{quote(side)}} --output {{quote(output)}}

# Native CurseForge client export.
export-client output="dist/aeropunk-client.zip":
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side client --output {{quote(output)}}

# Native Modrinth export with installer-managed side selection.
export-modrinth output="dist/aeropunk.mrpack":
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz modrinth export --output {{quote(output)}}

# Update external files, respecting packwiz pins.
update:
    packwiz update --all

# Export and boot a disposable Docker server, stopping immediately on readiness.
test:
    python scripts/test_server.py

# Remove scoped temporary test outputs, preserving distributions and caches.
clean:
    python scripts/tasks.py clean
