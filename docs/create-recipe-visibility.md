# Create recipe visibility

Development release: 0.16.3-dev.

Just Enough Items 19.64.0.455 is included on the client alongside EMI. It supplies the Create recipe plugin consumed by EMI, including mechanical crafting recipes for Crushing Wheels and Create Waystones Recipes. EMI remains the item browser. No server installation is required for this recipe-viewing change.

The selected publisher archive was verified against its SHA512 checksum. Its bundled MezzConfig 0.6.6 satisfies the declared range from 0.6.3 inclusive to 1.0.0 exclusive, so the redundant standalone dependency automatically added by packwiz was removed. The declared minimum NeoForge version is 21.1.238; this pack selects 21.1.259. The artifact is published for Minecraft 1.21.1 and NeoForge. Its native Minecraft dependency range is `[1.21, 1.21.1)`, also present in older upstream releases. No dependency declarations were modified or bypassed. Client startup and the actual recipe screens remain unverified.

## Separate player-map finding

In the inspected main, development and hosting definitions, Xaero's Minimap and World Map are client-only selections. Main and hosting ship `config/xaero/lib/common.cfg` with `everyone_tracks_everyone` disabled. The selected Minimap 26.6.0 contains the server-side SyncedPlayerTracker implementation that reads this option and sends tracked-player positions. The maps bundle XaeroLib 1.7.3.

For global player tracking, the server needs the matching Xaero's Minimap and its bundled library, with `everyone_tracks_everyone` enabled in the server's `config/xaero/lib/common.cfg`. Old instructions naming `xaerominimap-common.txt` are not the path used by this selected release. Multiplayer+ synchronizes map terrain and does not replace the Minimap's player-position broadcaster. Client radar and tracked-player display settings can still hide markers.

This finding is from authoring files, published project documentation and selected-artifact inspection, not the current remote server. No map settings, installed games or running servers were changed. No party or claims mod is required for the everyone-tracks-everyone mode.
