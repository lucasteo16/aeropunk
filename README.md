# Aeropunk

A medieval steampunk engineering and adventure pack built around Create Aeronautics, Streams Reflowing and the RPG Series combat system.

Current definition: pack version 0.2.1, Minecraft 1.21.1 and NeoForge 21.1.255. There are 293 mod selections, nine resource packs and three shader packs, each selecting an exact artifact. Only demonstrated compatibility exceptions are pinned against updates.

## Requirements

Install Just, packwiz, Python 3.11 or newer, Docker Engine and Docker Compose. Docker must be running and accessible to your user. The server test runner uses Linux host file locking; Windows client support is separate from the authoring host.

No host Java installation or third-party Python dependencies are required. Packwiz and Docker retain their normal caches. Project cleanup does not prune either cache.

## Commands

Run commands from the repository directory. `just --list` shows the available commands.

| Command | Behavior |
| --- | --- |
| `just export-server` | Export the server selection in CurseForge format. |
| `just export-curseforge` | Export the client selection in CurseForge format. |
| `just export-modrinth` | Export a Modrinth archive with client and server side information. |
| `just test` | Reuse installed binaries, create fresh test state, verify readiness, stop normally and clean temporary state. |
| `just test --fresh-install` | Run the server check with an entirely fresh temporary installation. |
| `just update` | Run `packwiz update --all`, respecting pins. |
| `just clean` | Remove recognized temporary runs and Python bytecode, preserving releases, latest reports and the reusable installation. |

Ordinary selections are unpinned so `just update` can offer newer releases for the selected Minecraft version and loader. Pin a mod only after a specific incompatibility has been demonstrated, and document the reason. Exact artifact selection still makes exports reproducible without an update hold. Packwiz does not restrict unpinned updates to patches or guarantee cross-mod compatibility; inspect changes and retest before distributing them.

The current compatibility holds are Spell Engine 1.10.7, because newer loot-function changes broke Witcher 3.1.4, and Xaero's Maps Multiplayer Plus 1.1.0, because 1.1.1 contains a malformed bundled Java module descriptor rejected by NeoForge. All other mods, resource packs and shader packs can receive updates. Prefer the newest mutually compatible combination, not the newest individual release of every mod.

## Versioned exports

All default outputs live directly in `dist`. There are no client or server output subfolders.

| Command | Default output for version 0.2.1 |
| --- | --- |
| `just export-server` | `dist/aeropunk-0.2.1-server.zip` |
| `just export-curseforge` | `dist/aeropunk-0.2.1-curseforge.zip` |
| `just export-modrinth` | `dist/aeropunk-0.2.1-modrinth.mrpack` |

The commands read the version from `pack.toml`; it is not duplicated in their definitions. Bumping it changes both the default filenames and the version inside newly exported archives. A bump does not export automatically: run the desired command afterward.

Each completed change batch increments the release version: major for breaking changes, minor for backward-compatible feature additions and medium-sized changes, and patch for bug fixes or configuration tweaks. Update this document, rebuild and verify the versioned exports, and record the batch in a meaningful local Git commit. Pushing remains a separate authorized action.

Exporting the same version again replaces only that version's corresponding file. Exporting a newer version preserves older versioned releases. Releases accumulate by version, while test reports retain only the latest run. `just clean` preserves every release in `dist`.

An optional output argument overrides the destination, for example `just export-modrinth dist/my-release.mrpack`. The recipes invoke packwiz directly, without rewriting archives or creating a second pack definition.

CurseForge exports bundle most selected mod files, but Short Stacks remains a manifest download reference. Modrinth exports reference most files by download address and hash, while bundling Short Stacks. Neither format contains a complete installed Minecraft server. A compatible launcher or server installer sets up the game and loader. Redistribution permissions remain the pack author's responsibility.

Version 0.2.1 replaces the original emblem with the approved simplified flying-castle icon. Mod selections and player preference defaults are unchanged.

## Player preference defaults

Configured Defaults 21.1.3 is client-only. Its `configureddefaults` folder mirrors the game directory. The pack supplies twenty-five preset files covering video, Distant Horizons, resource-pack order, sound, keybindings and map preferences. Ordinary files are copied only when absent; `options.txt` adds missing keys without replacing existing values. These preferences are not duplicated at their active destinations in the exported pack. Existing configuration files do not receive automatic per-setting migrations.

The initial baseline uses eight-chunk render and simulation distances, fast graphics, a sixty-frame limit and vertical synchronization. Shaders and Distant Horizons rendering are disabled, with Photon remembered as the shader selection. Shader refresh uses F12. Keybindings retain the current incomplete arrangement rather than attempting a new conflict-resolution scheme. Personal map data, generated server identity and personal chat mention entries are not imported from the client instance.

The released defaults handler passed isolated checks for fresh-file initialization, preservation of existing graphics, audio and keybindings, and repeated application without resetting those preferences. This does not replace a full Minecraft startup test. Shared server settings and existing compatibility fixes remain authoritative under `config`.

The donor audit retained all 271 eligible configuration paths, including Create settings. None of the three referenced donor archives contains separate hand-authored recipe scripts or recipe data packs. Create Plus bundles generated Supplementaries recipe caches; the running client already regenerates recipes for its installed content. Those caches and recipe-viewer favourites are not authoring inputs and are not copied.

## Server test

`just test` exports a fresh native Modrinth archive into a unique temporary directory under `build`. The Docker image's existing `mc-image-helper install-modrinth-modpack` installs it and applies its server side declarations. Its optional default exclusion list is disabled. There are no custom mod exclusions or dependency bypasses.

The reusable installation is at `build/server-installation`. Minecraft, NeoForge, libraries, selected mods, native installer manifests and native caches remain between runs. Referenced existing files are checked against the current exported hashes before reuse. Mismatching files are removed so the native installer can fetch the correct artifact. The installer reconciles removed selections, extracts current overrides and skips reinstalling an unchanged loader.

Each run gets fresh world, configuration, default configuration, logs, crash reports and generated-data directories. Separate bind mounts keep them in the temporary run directory rather than the reusable installation. Existing worlds are never used. A file lock prevents concurrent reuse; retained containers using the installation must be cleaned up before another run can use it.

The test uses a digest-pinned Java 21 image, four processors, a four-gibibyte Java heap and a five-gibibyte container memory limit. It publishes no ports. The Minecraft end-user license agreement has been accepted for this test server. These are testing limits, not production deployment settings.

Progress is reported in preparation, installation, startup, shutdown and cleanup phases. Minecraft must emit its startup-complete message and help prompt within the default 600-second readiness deadline. The runner immediately sends the stop command, requires confirmation and allows 60 seconds for a normal exit with status zero. Individual commands have separate limits.

There is no observation delay, simulated player, forced exploration, explicit save test or additional terrain-generation command. Minecraft performs normal fresh-world initialization. A pass verifies installation, readiness and normal shutdown, not client rendering, gameplay, sustained performance or world-migration safety. Installation time and startup time are reported separately.

## Reports and cleanup

Every test replaces the latest evidence:

| File | Contents |
| --- | --- |
| `reports/result.json` | Status, loader versions, archive fingerprint, installation mode, phase timings and failure phase. |
| `reports/server.log` | Full captured server output. |
| `reports/startup-diagnostics.log` | Terrain-stall thread dumps if emitted, otherwise an empty file. |

The runner captures final logs, removes its containers and network and checks that none remain. Only after confirmation does it remove the temporary world, generated settings, remote-console settings and run directory. Installed binaries and native caches remain.

If Docker cleanup cannot be confirmed, temporary files remain for recovery and the failure is reported. `just clean` refuses to remove a recognized run still associated with containers or networks. It never stops containers or prunes Docker.

## Repository layout

| Location | Purpose |
| --- | --- |
| `pack.toml` | Pack version, game version, loader version and index reference. |
| `index.toml` | Distribution index maintained by packwiz. |
| `mods`, `resourcepacks`, `shaderpacks` | Selected artifacts, provider metadata, pins and side declarations. |
| `config` and `polytone_options.json` | Shared game settings. |
| `configureddefaults` | Initial client preferences that preserve existing player choices. |
| `justfile` | Active command entry points. |
| `scripts` | Active test lifecycle and scoped cleanup code. |
| `dist` | Versioned release archives, all in one folder. |
| `build` | Reusable installation and lock, plus temporary runs removed after cleanup. |
| `reports` | Latest test evidence. |

Git tracks authoring sources, not binaries, worlds, exports or reports. `.packwizignore` independently excludes operational files, secrets, local installations and generated outputs from distributions. After changing shared game settings or side declarations, run `packwiz refresh`.

Obsolete export layouts, unversioned duplicates and inactive archived test code are no longer kept in the repository. Earlier material was moved outside it for reversibility. The current versioned release history remains in `dist`.

## Compatibility and remaining checks

The selected server mod set passed readiness and normal shutdown checks before spark was added. spark 1.10.124 is included by default on clients and servers; its addition has packaging validation only, pending the next runtime test. Spell Engine 1.10.7 is retained for Witcher 3.1.4 compatibility. Xaero's Maps Multiplayer Plus is pinned to 1.1.0. GrandTeleport 1.0.0 is client-only. Advancement Frames is excluded because its selected release loaded a client-only class on a dedicated server; it was not relabelled as client-only content.

Client crash corrections retain Entity Model Features 3.3.11 and update its Not Enough Animations compatibility addon to 1.2.0, Create compatibility addon to 2.0.0 and shared compatibility core to 2.0.0. AsyncParticles is updated to 21.1.4.5. Exact released class-member checks resolve the animation references against the selected game and libraries; the newer particle mixin removes the offending light-color shadow method. Lodestone's delayed particle buffer is disabled using the particle author's documented compatibility workaround. Lucas's supplied recordings establish a running client and integrated server for the corrected 0.1.3 installation. They do not establish that every rendering warning is resolved. Reinforced Shulker Boxes' early rendering initialization and older Sodium settings integrations remain client playtest concerns.

Version 0.2.0 adds client preference initialization and integrates Lucas's selected settings without upgrading the existing mods. A full client launch of the 0.2 series, shaders, moving-structure interactions, multiplayer behavior and gameplay balance remain separate playtest work. No shader is enabled automatically. Preserve approved donor settings until observed behavior justifies a specific adjustment.

The latest saved result documents the definition it tested. Rerun `just test` after server-relevant changes. A release archive is an installation definition, not proof of a running production server.
