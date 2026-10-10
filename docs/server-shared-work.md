# Server shared work

Distant Horizons 3.3.3 is included on both client and server. The exact artifact is unchanged. Server generation and transfer of simplified terrain let compatible clients reuse the server's terrain data instead of relying only on terrain captured while exploring. Rendering still runs on each client. This shifts generation and storage work to the server and adds bandwidth and server resource costs; it does not make distant rendering free.

Players retain their own rendering choice. The client initialization preset remains unchanged, including the default disabled renderer. No played installation or hosted server was updated.

Use matching server and client releases. Keep generation and network requests enabled where server terrain sharing is wanted. Existing preset values permit generation, real-time updates and synchronization. Dedicated servers without that client preset use the mod's own defaults. Server tuning and pregeneration need separate deployment decisions; no background pregeneration was started.

## Client-only selection review

Reviewed all 70 client-classified mod selections in lightweight main using publisher environment metadata, plus the 11 heavy-only visual additions. Provider compatibility labels establish possible installation sides, not shared computation. Raw project data is retained in the ignored reports folder.

Distant Horizons is the confirmed shared-terrain case and is now included in server exports. The selected archive declares both sides and the publisher documents server terrain delivery.

Xaero's maps already have Xaero's Maps Multiplayer Plus in the pack on both sides. That synchronization is distinct from Distant Horizons terrain sharing. Installing the base map mods on the server does not establish offloaded map rendering.

Async Logger is a possible separate server optimization, not shared client work. Its publisher environment labels disagree across providers; the selected binary contains early loader services. Keep its current side until dedicated-server behavior for this artifact is verified. Its logging optimization would act independently on each process, not transfer client logging to the server.

Other client renderers, shaders, culling, particles, audio, menus and libraries needed only by client consumers remain client-only. A library being server-capable is not a reason to add it to a server that has no server consumer. Existing server-capable general optimizers retain their current sides.

## Verification limits

Native client and server packaging can verify inclusion, unchanged artifact hashes and preserved preferences. This maintenance does not authorize starting a game, hosting a test server or modifying a running installation. Server startup, actual network transfer and performance remain unverified.

Source: https://gitlab.com/distant-horizons-team/distant-horizons/-/wikis/1-user-guide/1-frequently-asked-questions/5-server-owners/Server-Owners
