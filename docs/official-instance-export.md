# Official launcher instance exports

`just export-instance` now copies a fresh uncompressed client game folder and creates a new installation in the official Minecraft launcher. It does not start the launcher or Minecraft. Open the launcher and choose the new installation yourself after the command finishes.

## Prerequisites

- Close the official launcher and every Minecraft or NeoForge Java process for the entire export. The command checks Linux process state before copying and immediately before registration. It refuses unreadable process state and never prints process arguments or account tokens.
- Install the source pack's NeoForge runtime into the official launcher once. For the current source requirements, this is NeoForge 21.1.255 for Minecraft 1.21.1. The installed manifest must be `~/.minecraft/versions/neoforge-21.1.255/neoforge-21.1.255.json`, declare that runtime identifier, and inherit Minecraft 1.21.1. A changed loader version requires its own installation.
- The launcher must already have a valid `~/.minecraft/launcher_profiles.json` containing a profiles mapping.
- Populate the normal packwiz cache before exporting. Each export verifies and copies cached mod files and indexed pack files. It does not download mods, install NeoForge again, or compress an archive. Missing or corrupt cached files fail without a network fallback.

## Commands and destinations

Run `just export-instance` for a unique destination beneath `~/Projects/lucas/instance-runs`. Its folder name starts with `astropunk-`, followed by the exact source pack version, a universal coordinated time timestamp, and a short random suffix. Repeated exports never overwrite earlier runs or reuse their launcher installation.

Provide an unused explicit destination with `just export-instance '/absolute/path/to/new-instance'`. The pure exporter's existing path, checksum, overlap and existing-output validation still applies. The launcher uses the absolute `game` directory inside that destination.

Provide an explicit template directory as the second argument, such as `just export-instance '' '/absolute/path/to/template'`. An omitted or empty template argument uses the durable default template when its metadata exists. For Minecraft 1.21.1 that directory is `~/Projects/lucas/instance-templates/official-neoforge-1.21.1`. If the default metadata is absent, export proceeds without template directories or a saved icon. An explicitly supplied template must exist and validate.

## Durable template

The template is optional. Its `template.json` declares matching `game_version`, `loader` and `loader_version` fields, plus a `launcher_profile` object. Only `icon` and `type` are allowed inside that object. An icon must be a safe built-in launcher icon name, such as `Grass` or `Furnace`. Custom image data and path-based icons are not accepted. The type, if present, must be `custom`.

The template also contains a `game` directory with empty directory layout only. Regular files, special files and symbolic links are forbidden. The wrapper uses the existing pure exporter's template validation and directory copying. It never copies personal options, saves or account data from a template.

Do not put old creation times, last-used times, identifiers, game directories, Java arguments or Java paths in the template. Unsupported fields are rejected. Every new profile receives a new identifier and current timestamps, the source pack's native NeoForge runtime identifier, and its own absolute game directory. The wrapper does not copy the live vanilla Template installation or modify it. It leaves Java arguments, memory settings and Java selection unspecified for the new profile, so normal launcher defaults apply. Existing installations keep their settings.

## Registration safety and recovery

The wrapper captures the exact launcher profile bytes before exporting. Before registration, it saves those bytes beneath the durable default template's `backups` directory, outside `.minecraft`. Backup files permit only their owner to read and write them; the backups directory permits only its owner to access it. The wrapper uses this default backup location even when another template is selected.

Registration adds one new profile named `Astropunk Guide Test`, followed by the exact source pack version and a unique timestamp and suffix. Every existing profile, unrelated top-level field and selected profile remains unchanged. JSON formatting may change, but existing field values do not.

Before replacing the profile file, the wrapper checks again that the launcher and game remain closed and that the original bytes have not changed. It refuses concurrent edits instead of overwriting them. Replacement uses a temporary file in the same directory and an atomic rename. Keep the launcher closed throughout: byte comparison and rename are separate operating-system operations, not a lock respected by other programs.

After replacement, the wrapper reads back the complete document and verifies the new profile and all preserved fields. Only then does it record `official_launcher.profile_id` and `official_launcher.profiles_path` in the export's own `instance-export.json`.

If registration fails after copying, the command reports failure and the prepared game folder's location. It never deletes that output. Inspect the launcher profiles and the saved backup before recovery, especially after a readback failure, which may mean registration already happened. Do not retry into the same destination, because existing-output protection will refuse it. A new export creates another independent folder and installation. Restore a backup only deliberately, with the launcher closed, after accounting for any later legitimate profile changes.

## Scope and verification

`scripts/export_instance.py` remains the pure cache-only exporter, without launcher registration. Archive export recipes are unchanged.

The automated tests use tiny private source, cache, runtime and launcher fixtures. They verify unique and explicit destinations, preserved profiles and settings, backup bytes and permissions, template validation, process refusal, concurrent-edit refusal, readback checking and preservation of prepared output after registration failure. These tests do not launch Minecraft or establish gameplay compatibility.
