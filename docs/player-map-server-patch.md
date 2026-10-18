# Player map server patch

Development release: 0.16.4-dev.

Xaero's Minimap 26.6.0 and World Map 1.47.0 now target both client and server. Their selected publisher artifacts are unchanged, and both contain XaeroLib 1.7.3. Global player tracking is enabled through `config/xaero/lib/common.cfg`. Other values in that file remain unchanged.

The drag-and-drop patch contains only the two selected mod archives and that configuration file. It contains no world, player data, map cache, authentication settings, launcher libraries or unrelated settings. Just Enough Items is a separate client-only change and is not included in this server patch.

## Installation

1. Stop the server and wait until it is offline.
2. Extract the patch archive locally. Copy and paste the contents of its `mods` folder into the existing server `mods` folder. Merge folders; do not replace or delete either directory.
3. Copy the patch's `config/xaero/lib/common.cfg` into the matching server path, overwriting only that file. If the host has custom Xaero library permission settings, preserve them and change only `everyone_tracks_everyone` to `true` instead.
4. Restart the server and reconnect. Clients with the same selected map versions do not need different map binaries. Check distant online players in the same dimension, with tracked-player display enabled.

There are no obsolete mod filenames in the authored baseline because these two map mods were previously excluded from server exports. If they were installed manually, retain only one version of each map mod and use the filenames supplied by this patch. Preserve Multiplayer+, worlds and all existing map data.

World Map's server identification can select a different map entry. If the displayed map looks empty after reconnecting, select or rebind the existing map through Map Selection; do not delete map data.

Publisher checksums, the complete patch archive membership, configuration parity and export inclusion are checked during preparation. Server startup, actual player markers and world identification remain to be tested on the hosted server. No live host or installed client is modified by preparing this patch.
