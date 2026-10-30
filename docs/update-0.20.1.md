# Astropunk 0.20.1

Minecraft 1.21.1 and NeoForge 21.1.265 are unchanged. All seven supported editions retain the display name Astropunk and their established version suffixes.

## Deep Seas custom bugfix

Replace the published Deep Seas 3.4.5 selection with `mods/create_submarine-3.4.6-astropunk.1.jar`. This is the full upstream 3.4.6 source at main commit `020c4fc6612051a76220ab003e2b41ae965a1edb`, with one local pressure-scan merge correction. The artifact retains upstream internal version 3.4.6; the filename identifies our custom revision rather than implying it is an official published binary.

The correction restores `level.getMaxBuildHeight()` as the pressure column's upper scan boundary, preserving the dimension-specific bounds and the merged nonblocking chunk lookup. The upstream merge had restored a reference to the removed `MAX_WATER_SCAN` constant and could not compile. All upstream shader corrections, translations and nonblocking chunk lookups remain included.

The full 3.4.6 update also includes Vortex rendering features and gameplay changes. This is not represented as a shader-only backport. Upstream shader integration now sets hull-depth readiness per active program and binds the hull texture immediately before the relevant draw pass.

The tested binary is tracked directly as a game override, replacing the provider metafile so installations cannot fetch a second, unpatched Deep Seas jar. Other publisher selections remain unchanged. It is intentionally not an automatic Modrinth update selection. Reassess and retire the custom artifact when a compatible published upstream replacement is accepted.

## Vortex defaults

Lucas's complete tested `create_submarine-vortex.toml` is copied unchanged into `configureddefaults/config/`. Its master switch is off for every edition, including Light, while retaining his reduced-cost settings for players who opt in. The upstream consumer registers this exact filename as client configuration. Existing player files are preserved by Configured Defaults, so updating an existing installation does not force its current Vortex settings off.

Lucas reports an approximately 30 frames-per-second cost on his device with Vortex enabled. This is user-provided evidence, not an independent benchmark or a universal performance estimate. Iris shader packs disable supported Vortex rendering paths, but the explicit master-off default also covers players without shaders.

## Validation and boundaries

The patched main source compiled and its archive integrity and installed checksum were verified. Lucas reports the patched official-launcher instance works. The prior release-commit trial also showed the fog obstruction resolved, with normal world saves and shutdown. This does not establish exhaustive boat, submarine, pressure, multiplayer or saved-world migration compatibility. Remaining Veil, graphics initialization and recipe-browser log errors have not been represented as fixed.

This batch synchronizes local source editions only. No live server or played instance is updated, no unrequested distribution is exported, and nothing is pushed.

## Rebuilding

See `scripts/deep-seas/README.md` for the exact upstream source, tracked patch and build procedure. The upstream license remains All Rights Reserved; this local integration does not grant permission to publish the modified artifact publicly.
