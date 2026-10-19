# Recipe-browser hosting update

Release: 0.17.0-hosting. This is a targeted hosting update on the shared 0.16.4 baseline. Other branches remain unchanged.

## Selected additions

| Project | Selected release | Installation |
|---|---|---|
| WorldGen | 1.4.5 | Client and server |
| EMIffect | 2.1.6 | Client |
| Moderately Enough Effect Descriptions | 8.1.0 | Client and server |
| Just Enough Breeding | 3.3.1 | Client |
| Extra Mod Integrations | 1.0.3 | Client |
| EMI: Create Schematics | 1.1.0 | Client |
| EMI For Create Stock | 1.0.8, beta | Client |
| EMI Trades Reborn | Published 2.0.0, internal version 2.0.0+alpha.1 | Client |
| EMI Recipe Sharing | 1.0.4 | Client and server |

WorldGen was selected instead of EMI Ores. Just Enough Filters is excluded. EMI Loot, EMI Enchanting, Reliable EMI and Just Enough Items remain unchanged. Selected binaries were checked against publisher SHA512 values and their loader dependency declarations. Create Stock requires Create 6.0.9 or newer and conflicts with Create Factory Logistics, which is not selected. The pack retains Create 6.0.10 and EMI 1.1.24. Extra Mod Integrations supplies its component modules as bundled libraries.

## Cumulative server patch

The patch covers changes after 0.16.2, including both the earlier map update and this release:

- 0.16.3 added Just Enough Items 19.64.0.455 on clients for Create recipe visibility. It has no server payload.
- 0.16.4 added Xaero's Minimap 26.6.0 and World Map 1.47.0 to the server selection and enabled global player tracking.
- 0.17.0-hosting adds WorldGen 1.4.5, Moderately Enough Effect Descriptions 8.1.0 and EMI Recipe Sharing 1.0.4 to the server selection.

The unpacked patch contains five mod archives and the Xaero library configuration. It contains no worlds, player data, map caches, authentication files, launcher libraries or client-only addons. No existing server mod archive is upgraded or removed relative to 0.16.2. If matching files were installed manually, overwrite identical filenames and avoid keeping other versions of those same projects.

## Applying the patch

1. Stop the server and wait until it is offline.
2. Copy and paste the patch's five mod archives into the existing server mods folder. Merge folders, never replace or delete the whole folder.
3. For a server with custom Xaero library settings, change only `everyone_tracks_everyone` to `true` in `config/xaero/lib/common.cfg`. Otherwise copy the supplied file into that exact location. Preserve unrelated host settings.
4. Start the server, then connect using the 0.17.0-hosting client export.
5. If the map appears empty, use Xaero Map Selection to select or rebind the existing map. Do not delete map data.

The hosting client retains the saved astropunk.sparked.network listing, shader-disabled defaults and existing player-preference preservation. Preparing this update does not deploy to the host or modify played client installations. Archive and dependency checks do not establish in-game recipe visibility, trade completeness, Create stock behavior or successful hosted login.

## Deliveries and verification

- `dist/astropunk-0.17.0-hosting-modrinth.mrpack` is the standard hosting client.
- `dist/astropunk-0.17.0-hosting-light-modrinth.mrpack` is a Light hosting client built from an indexed snapshot of the same definition. It removes exactly the nine established environmental audio and entity-appearance selections recorded in `main-light`'s `docs/light-edition.json`. It preserves all other manifest entries and every override byte, including the saved server listing. The active Light branch itself is unchanged.
- `dist/astropunk-0.17.0-hosting-server-patch-from-0.16.2.zip` contains the six files listed above, with paths directly beneath the server root. The matching unpacked folder is available beside it.

The standard server definition reached readiness and stopped normally with exit status zero. The installed five patch binaries match their publisher checksums. The six newly selected client-only addons are omitted from the installed dedicated server. Both client archives passed integrity, identity, addition membership and shared-payload parity checks. No client was launched and the host remains unchanged.

Known nonfatal limitations from this startup:

- Moderately Enough Effect Descriptions loads ten effect-source recipes for installed boss mods that use the absent `jeed:effect_provider` serializer. Those source entries are discarded. Its translated descriptions remain packaged for EMIffect, but richer effect-source coverage is incomplete. Just Enough Effect Descriptions implements that serializer, but adding or substituting another effect viewer is outside this approved batch and has not been done.
- WorldGen builds its biome and loot-table data, but warns about unsupported placement combinations for some decorative stone features and unsupported loot entry types. This does not establish complete ore or loot coverage.
- EMI Recipe Sharing emits missing client-mixin-target warnings on the dedicated server, without preventing readiness or normal shutdown. Actual recipe sharing remains untested.
