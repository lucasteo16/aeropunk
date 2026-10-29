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

The release includes the narrow `config/fml.toml` dependency exception for Scaling Difficulty 1.1.0 and Levelplate 1.0.0. The published Levelplate download version includes the Minecraft suffix, but its internal version does not; Scaling Difficulty incorrectly uses the suffixed value as its server-only minimum. The exception removes only that dependency constraint and leaves both original mod artifacts unchanged. A disposable dedicated server started, responded to a console command and shut down normally. Lucas also confirmed hosted-server startup and joining after applying the exception.

Levelplate size is now `-0.015`, with the remaining display and difficulty settings unchanged. The release stays at 0.20.0 for this update session.

Existing-world testing revealed a Create Encased tank-data migration failure: the older shared `createcasing:fluid_tank` block-entity identifier is replaced by per-variant identifiers. Lucas reported lost stored experience and restored tank operation by replacing the affected tank. Other older tanks need a migration check before assuming their contents survive. This is separate from the dependency exception.

The old generated More RPG Library configuration contained malformed earth-weakness and water-resistance tag references. Lucas regenerated its configuration folder and reported that things worked afterward. This generated folder is not bundled in the pack. More RPG Classes Skill Tree 1.3.1 does not recommend configuration regeneration; its renamed Berserker spell identifiers still matter for custom data packs.

The supplied hosted-server log also reports Streams Reflowing generation stalls, which remain unresolved. Successful startup and joining do not establish every recipe, optional rendering path or existing-world migration. Preserve existing installations, worlds, server credentials and previous deliveries. No live server or installed client is modified by source synchronization.
