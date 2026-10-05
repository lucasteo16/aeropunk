# Aeropunk

A lightweight Minecraft pack centered on Create Aeronautics and Streams Reflowing, with compatible performance improvements and client conveniences.

Current definition: Minecraft 1.21.1, NeoForge 21.1.255, pack version 0.1.0. All 17 mod selections are pinned.

## Requirements

Install Just, packwiz, Python 3.11 or newer, Docker Engine, and Docker Compose. Docker must be running and accessible to your user. No host Java installation or Python dependencies beyond the standard library are required.

Packwiz uses its default cache outside the repository. On this machine it is `/home/tsb/.cache/packwiz/cache`. Docker uses its normal image cache. Neither is relocated or deleted by the project commands.

## Commands

Run commands from the project directory:

```sh
cd ~/Projects/lucas/aeropunk
just --list
```

| Command | Behavior |
| --- | --- |
| `just export` | Export and validate the server distribution. |
| `just export-client` | Export the client definition. This does not launch the client. |
| `just test` | Export, start a disposable Docker server, confirm readiness, stop normally, and clean temporary files. |
| `just unit` | Run fast automation tests using disposable fixtures. |
| `just update` | Run `packwiz update --all`, respecting pins. |
| `just clean` | Remove recognized temporary test files and Python bytecode. Preserve exports, latest reports, sources, and caches. |

Because every mod is pinned, `just update` does not automatically move those mods to new versions. Changing a pinned selection is a separate, deliberate packwiz operation.

Just prevents Python bytecode generation for its commands. There is no separate list of verified mods and no repository-local collection of downloaded research copies.

## Exports

Packwiz generates the filenames using the pack name and version. Server and client archives are separated because their native filenames are identical:

```text
dist/
  server/
    Aeropunk-0.1.0.zip
  client/
    Aeropunk-0.1.0.zip
```

Exporting the same version replaces its existing archive. Bumping the pack version creates a different filename, so older versioned exports remain until deliberately removed. `just clean` does not remove distributions.

The wrapper runs the native CurseForge-format export without overriding its filename, validates the generated archive, and moves it into the appropriate distribution directory. A failed export preserves the previous distribution. Packwiz decides which mods belong on each side; the server tester does not maintain its own mod classification or remove specific mods.

The current Modrinth-sourced server mods are bundled in the archive. Unresolved CurseForge manifest references are rejected rather than silently testing an incomplete distribution.

## Server test

```sh
just test
```

The test has bounded, visible phases for preparation, installation, startup, shutdown, and cleanup. It consumes the actual server export and derives Minecraft and NeoForge versions from its manifest.

The disposable server uses a digest-pinned Java 21 Docker image, a fresh runtime, no published ports, a four-gibibyte Java heap, a five-gibibyte memory limit, and four processors. The Minecraft end-user license agreement has already been accepted for this test server. Existing worlds are not used.

The test waits up to 600 seconds for the startup-complete message and help prompt, then immediately requests normal shutdown. Shutdown must finish within 60 seconds with exit status zero. There is no extra observation delay, forced chunk generation, saved-region inspection, or gameplay exercise.

A pass means the server started and stopped successfully. It does not establish client rendering compatibility, shader support, gameplay stability, or measured performance.

The latest evidence is always written to:

```text
reports/result.json
reports/server.log
```

These files are replaced on each test, including failures. Historical reports do not accumulate. Temporary runtime files are removed only after container and network cleanup is confirmed. If cleanup cannot be confirmed, the runtime remains for recovery and the failure is reported. `just clean` does not stop containers or prune Docker, and it preserves unknown build contents for manual review.

## Project files

| Location | Purpose |
| --- | --- |
| `pack.toml` | Pack name, version, and loader definition. |
| `index.toml` | Distribution index maintained by packwiz. |
| `mods` | Pinned provider metadata, download hashes, and side settings. |
| `config` | Deliberate shared game configuration. |
| `justfile` | Short command entry points. |
| `scripts` | Minimal export and Docker test coordination. |
| `tests` | Automation regression and cleanup-safety tests. |
| `dist` | Finished versioned exports. |
| `build` | Disposable work, empty after successful cleanup. |
| `reports` | Latest server result and log only. |

Generated exports, reports, and temporary files are excluded from Git. Operational files are also excluded from packwiz distributions. After changing shared configuration or documented side metadata, run `packwiz refresh` to update the index.

Git tracks the pack definition, not downloaded mod copies. Use a working branch for changes and merge accepted changes into `main`. A startup pass is not a substitute for later client and gameplay checks.

## Compatibility boundaries

Create, Create Aeronautics, Sable, and Streams Reflowing form the gameplay baseline. Sodium, Lithium, FerriteCore, ImmediatelyFast, and ModernFix provide the selected performance improvements. Client conveniences include Sodium Extra, Reese’s Sodium Options, Ok Zoomer, Dynamic FPS, and Quick Pack. Distant Horizons is client-only.

Entity Culling uses safe mode, disables client tick culling, and exempts Create contraption entities. Donor configuration bundles, risky threading changes, and dependency bypasses are not included.

Avoid ScalableLux with Sable, Radium or Palladium with Create, and duplicate Embeddium and Sodium rendering backends. Additional threading and moving-structure rendering optimizations remain deferred.

Iris remains in the authored definition with its optional metadata. Client launch and shader compatibility are unverified; no shader pack is bundled. Backports, space addons, and resource-pack additions are not part of this baseline.

## Verified baseline

The latest completed verification exercised command listing, both exports, update with pins retained, all 12 automation tests, a real server startup and normal shutdown, and cleanup. Both exports excluded operational files. The final inventory showed an empty build directory, only the latest two report files, no remaining test containers or networks, and no recreated research cache, archive, old documentation directory, or Python bytecode directories.

Client gameplay remains untested. Verification results describe this baseline, not a guarantee for future changes; rerun `just test` after server-relevant changes.
