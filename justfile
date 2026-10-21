set export
PYTHONDONTWRITEBYTECODE := "1"
PACK_VERSION := `python -c 'import tomllib; print(tomllib.load(open("pack.toml", "rb"))["version"])'`

# List available tasks.
default:
    @just --list

# On-demand native CurseForge server export, not a managed-host installation.
export-server output=("dist/astropunk-" + PACK_VERSION + "-server.zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side server --output {{quote(output)}}
    python scripts/retain_releases.py --after-export {{quote(output)}} --apply

# On-demand native CurseForge client export; not part of routine releases.
export-curseforge output=("dist/astropunk-" + PACK_VERSION + "-curseforge.zip"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz curseforge export --side client --output {{quote(output)}}
    python scripts/retain_releases.py --after-export {{quote(output)}} --apply

# Requested edition only: native Modrinth export with installer-managed sides.
export-modrinth output=("dist/astropunk-" + PACK_VERSION + "-modrinth.mrpack"):
    mkdir -p "$(dirname {{quote(output)}})"
    packwiz modrinth export --output {{quote(output)}}
    python scripts/retain_releases.py --after-export {{quote(output)}} --apply


# On-demand cache-only client folder and a new official launcher installation.
export-instance output="" template="":
    python scripts/export_official_instance.py {{quote(output)}} --template {{quote(template)}}

# Update external files, respecting documented compatibility holds.
update:
    packwiz update --all

# Explicitly requested test only: export and boot an isolated Docker server.
test *args:
    python scripts/test_server.py {{args}}

# Remove temporary runs and Python bytecode; keep versioned exports, reports and installation.
clean:
    python scripts/tasks.py clean

# Preview release retention; add --apply to remove superseded distributions.
retain-releases *args:
    python scripts/retain_releases.py {{args}}
