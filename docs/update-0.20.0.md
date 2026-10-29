# Astropunk 0.20.0

## Release source

Lucas requested 0.20.0 as the actual release across the existing seven active edition branches. Development integrates the final shared update selections and configuration migrations; Main and the established downstream branches inherit them. Keep the existing edition suffixes and display name Astropunk. Hosting and Hosting Light clients are generated from their own branches using `just export-modrinth`, not an update companion branch or alternate exporter.

Minecraft remains 1.21.1. NeoForge is 21.1.265. No further version increment is needed within this update session.

## Shared changes

The release adopts the prepared global mod updates, Photon 1.4, and the refreshed existing configuration bundle. Six obsolete configuration paths migrate to the current Almanac, Let Me Despawn, Collective and Villager Names layouts; Navigator has a separate server configuration. Preserve authored resources, accepted difficulty replacement, exclusions, Better Days pacing and other deliberate settings. A minimal configuration-subset cleanup remains deferred.

The final native-default alignment uses Bits n Bobs flywheel bearing enabled and brass lamp disabled, Supplementaries naval-raid chance 0.4, and removes the retired plunderer-chance and Amendments warning keys. These choices match the verified uploaded-server preparation and last played client evidence.

EMI Recipe Sharing 1.0.4, WorldGen 1.4.5, Moderately Enough Effect Descriptions 8.1.0 and its client-only EMIffect 2.1.6 companion are shared features. Hosting retains its remaining edition-only information tools, server-only EasyAuth and saved server entry. Hosting Light retains the exact nine declared exclusions; these must not be reintroduced when shared metadata changes.

## Compatibility holds

- Beautify stays pinned to 1.9.0. Newer inspected releases requested Fabric's creative-tab identifier on NeoForge and prevented startup. Every Compat remains 2.11.56.
- GuideME stays pinned to 21.1.19 because the current handbook helper declares that exact dependency. Helper changes remain deferred.
- GrandTeleport stays at 1.0.0 because the attempted newer artifact had an invalid native version string.
- Distant Horizons stays at 3.3.3; no matching published replacement with the awaited Chunky fix was established during this update. Preserve disabled initial distant rendering and the shader-first workaround.
- Terralith stays at 2.6.2 rather than the updater's unintended downgrade. Forgematica uses the runnable 0.4.3 artifact, not its sources archive.

## Validation and deployment boundary

Lucas confirmed startup, world entry, backpack use and aqua-wand damage in the Beautify-pinned shared trial. He reports uploading the prepared matching server folders. These reports are not a dedicated-server startup result or a multiplayer connection test of the final client.

Source promotion and archive verification do not prove existing-world migration, every recipe, optional rendering or runtime compatibility. The final hosting clients require Lucas's connection test. Preserve existing installations, worlds, server credentials and previous deliveries. No live server or installed client is modified by source synchronization.
