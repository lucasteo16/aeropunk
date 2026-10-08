# Astropunk grouped regression tests

## Chunky baseline revision 2

This branch removes AFK Cinematics and Steppy. Dynamic FPS now uses its released defaults: unfocused rendering at 1 frame per second, invisible rendering at 0, and idle rendering at 10. Idle detection remains the native five-minute, on-battery default. The old active configuration override is removed, so existing player settings are not replaced.

Added Sound Physics Remastered 1.5.1, Presence Footsteps (NeoForge) 1.12.0 beta 1, Presence Footsteps x Sable 1.0, Cool Rain Reforged 1.0.2, and Sable: Cool Rain 1.0.1. These audio additions are client-only. Presence Footsteps uses the NeoForge fork because the other port's selected artifact declares a malformed Minecraft dependency range. Beta status is retained as a manual-test checkpoint.

The revision 2 grouped test set shares this Chunky baseline across all three packages. The Northstar and optimizer branches independently inherit it, never each other's additions. Test Chunky first, optimizers second, and Northstar last. Main remains unchanged. Archive verification does not establish sound behavior, performance or gameplay compatibility. The Northstar rendering override investigation remains on hold.

For the intermittent loading crash, distinguish a fresh instance creating its first world, another newly created world in that same instance, and reopening an existing save. Record which case succeeds or fails and retain its matching crash report. A successful retry does not establish that the failure is fixed. This round deliberately retains Chunky, Distant Horizons and Progress Peek without crash-specific changes.

Use three feature groups, not individual-mod brute force. All are based on stable main with Chunky, Astropunk branding and disabled Distant Horizons update checking. The initial rendering preference is disabled, not a restriction on player choices. The unchanged Northstar bridge can override that preference during play. Main is unchanged; no merge is approved.

- grouped/chunky: trusted baseline candidate with Chunky and common fixes.
- grouped/northstar: baseline plus Northstar, original Aeronautics compatibility, the rendering bridge, Paxi recipe correction and AeroWarptics.
- grouped/optimizers: baseline plus Async Logger, Jasione and ServerCore.

The travel and optimizer branches are independent children of the Chunky baseline, not cumulative. Test the baseline first, then each feature group on Java 21 in fresh imports with identical memory, graphics settings and comparable separately created worlds. Keep Chunky tasks inactive unless testing pregeneration itself. Subdivide only the failing group. If both pass separately but the combined pack fails, investigate interactions between groups.

The old isolation branches and packages are retained as superseded diagnostic history. These grouped exports replace them for the next round. No launcher imports, game launches or performance measurements were performed. Native archive integrity and exact branch additions are verified. Configured Defaults preserves existing ordinary preferences; use fresh imports to receive the new updater default.
