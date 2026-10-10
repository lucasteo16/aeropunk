# Self-contained client export

Run `just export-standalone` from an edition's authoring workspace. The default destination is `dist/astropunk-<version>-standalone.mrpack`. Pass a destination as the first argument to write elsewhere. Existing export-modrinth, export-curseforge and export-server recipes remain unchanged.

The extra exporter invokes native packwiz Modrinth export and native CurseForge client export, both using the ordinary packwiz cache. It verifies the selected client files against the native manifest hashes, embeds them under client-overrides, and leaves the required Modrinth metadata with an empty download list. Native bundled overrides are retained. Server-only manifest entries, including spark, are excluded. An unresolved file or checksum mismatch fails the build rather than silently producing a partially self-contained archive. Temporary native exports are removed after completion.

Import the resulting mrpack normally. It requires no downloads for the bundled mods, resource packs or shader packs. Minecraft, NeoForge, Java, account authentication and any runtime downloads initiated by a mod remain separate launcher or runtime concerns. This is not a complete offline Minecraft installation. Launcher import and game startup have not been tested as part of packaging verification.

The self-contained archive is larger than the conventional export. Keep the conventional export for normal distribution and retain the self-contained variant for faster repeated fresh-instance testing. Bundling does not grant redistribution rights: review every project's license and permissions before sharing or publicly hosting the archive. Do not assume that availability through a manifest permits redistributing the binaries.

This build-tool addition does not change the gameplay pack version or any selected mod. Main owns the common command, and main-heavy inherits it.
