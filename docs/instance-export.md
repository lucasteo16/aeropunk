# Uncompressed instance export

`just export-instance` produces a copyable client game folder using only indexed pack files and the existing native packwiz cache. It does not download anything, refresh the index, compress files, register a launcher instance, or modify a live instance.

Minecraft, NeoForge, Java, authentication, and their supporting libraries remain launcher managed. This is not a complete offline Minecraft installation. The current pack requires Minecraft 1.21.1 and NeoForge 21.1.255, read directly from `pack.toml` rather than inferred from a launcher installation.

## Commands

Run from the pack directory with Python 3.11 or newer on Linux. Atomic publication requires the Linux `renameat2` operation.

```sh
just export-instance
just export-instance /path/to/new-export
just export-instance /path/to/new-export /path/to/durable-template
python scripts/export_instance.py /path/to/new-export --template ""
```

The default destination is `dist/astropunk-` followed by the exact pack version and `-instance`. The optional second recipe argument is a template directory. An empty template string means no template, so the exporter starts with an empty game directory.

The script also accepts `--source` and `--cache` for isolated testing or an explicit alternate source. The normal cache is `~/.cache/packwiz/cache`. No alternate cache is searched automatically.

## Output

The export contains `game/` and `instance-export.json`.

The game directory contains independent normal file copies. Indexed ordinary files retain their paths and bytes, including the custom handbook helper, configurations, menu images, and handbook resource pack. Cached artifacts replace indexed metadata files at the metadata parent directory followed by the declared `filename`. Metadata files themselves are not copied. Server-only artifacts are excluded after their indexed metadata checksums are verified.

The manifest records the pack name and exact version, Minecraft and loader requirements, every owned game file relative to the export root and its SHA256 checksum, and counts for indexed files, ordinary files, cached artifacts, server exclusions, template directories, and exported files. The manifest does not list itself because a file cannot contain its own checksum. Empty directories are not owned files.

Create or select a launcher instance with the recorded Minecraft and loader requirements before copying the exported game contents into its game directory. Launcher registration and deployment are separate operations. The exporter does not perform them.

## Cache and integrity

The exporter reads `pack.toml`, verifies its declared index checksum, and reads the authoritative index. It verifies every indexed file, including server-only metadata. It never refreshes or rewrites either source document.

For each client artifact, its declared download checksum is looked up in native cache `index.json`. The required structure has `Version` set to 2 and `Hashes` mapping each algorithm to parallel arrays. The matching array position identifies the canonical SHA256 value. Cached bytes live beneath the cache directory, with the first two checksum characters as the directory name and the remaining characters as the filename.

Both the declared metadata checksum and the canonical SHA256 checksum are checked against the cached bytes. Copied files are checked again before publication. Missing cache mappings or bytes fail with the artifact path and a clear error. There is no network fallback.

## Empty template contract

An optional durable template directory must contain `template.json` and `game/`. The document must contain these exact string fields matching the authoritative pack requirements:

```json
{
  "game_version": "1.21.1",
  "loader": "neoforge",
  "loader_version": "21.1.255"
}
```

The template game tree may contain directories only. Regular files, symbolic links, and special files are rejected. Only its empty directory layout is copied before indexed files are materialized. The template metadata stays outside the export. The exporter does not create or update a template snapshot.

## Safety and failure handling

Unsafe relative paths, symbolic links in input or output path components, duplicate destinations, file and directory collisions, overlapping source or template destinations, and existing outputs are rejected. Existing empty output directories are also rejected.

The source `dist` subtree is reserved for generated output so the default recipe can write beneath the repository without overlapping indexed inputs. Indexed files beneath that subtree are rejected. Other destinations within the source tree are rejected, as are destinations that contain the source, template, or cache.

Publication uses a newly created staging directory in the destination parent, followed by an atomic rename that cannot replace an existing destination. A failed run removes only its own staging directory. It never deletes an existing source or output. Copies do not share file identities with the cache, source, or template and use neither hard links nor symbolic links.

## Focused tests

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p test_export_instance.py -v
```

The tests use tiny indexed fixtures and a private native cache. They cover cache materialization, checksum failures, exclusions, unchanged ordinary files, independent file identities, path protections, collisions, empty template validation, command line handling, and staging cleanup. They do not export the actual pack or touch live instances.
