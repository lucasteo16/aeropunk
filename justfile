set export
PYTHONDONTWRITEBYTECODE := "1"

# List available tasks.
default:
    @just --list

# Export and validate the current fully materialized server distribution.
export:
    python scripts/tasks.py export

# Export the current client definition; packaging is not launch tested.
export-client:
    python scripts/tasks.py export-client

# Update all external files; pinned mods are respected (this all-pinned pack may have no updates).
update:
    packwiz update --all

# Boot and normally stop a disposable Docker server.
test:
    python scripts/test_server.py

# Run fast unit tests with disposable fixtures and mocked exports.
unit:
    python -m unittest discover -s tests -v

# Delete scoped generated test outputs and Python bytecode, preserving caches.
clean:
    python scripts/tasks.py clean
