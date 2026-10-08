# Astropunk grouped regression tests

## Chunky baseline revision 2

This branch removes AFK Cinematics and Steppy. Dynamic FPS now uses its released defaults: unfocused rendering at 1 frame per second, invisible rendering at 0, and idle rendering at 10. Idle detection remains the native five-minute, on-battery default. The old active configuration override is removed, so existing player settings are not replaced.

Added Sound Physics Remastered 1.5.1, Presence Footsteps (NeoForge) 1.12.0 beta 1, Presence Footsteps x Sable 1.0, Cool Rain Reforged 1.0.2, and Sable: Cool Rain 1.0.1. These audio additions are client-only. Presence Footsteps uses the NeoForge fork because the other port's selected artifact declares a malformed Minecraft dependency range. Beta status is retained as a manual-test checkpoint.

The other grouped branches still use revision 1 of the baseline. They have not been rebased or rebuilt, so these new audio additions must not be mistaken for shared settings in the original three-package comparison. Main remains unchanged. Archive verification does not establish sound behavior, performance or gameplay compatibility.

Use three feature groups, not individual-mod brute force. All are based on stable main with Chunky, Astropunk branding and disabled Distant Horizons update checking. Rendering remains disabled. Main is unchanged; no merge is approved.

- grouped/chunky: trusted baseline candidate with Chunky and common fixes.
- grouped/northstar: baseline plus Northstar, original Aeronautics compatibility, the rendering bridge, Paxi recipe correction and AeroWarptics.
- grouped/optimizers: baseline plus Async Logger, Jasione and ServerCore.

The travel and optimizer branches are independent children of the Chunky baseline, not cumulative. Test the baseline first, then each feature group on Java 21 in fresh imports with identical memory, graphics settings and comparable separately created worlds. Keep Chunky tasks inactive unless testing pregeneration itself. Subdivide only the failing group. If both pass separately but the combined pack fails, investigate interactions between groups.

The old isolation branches and packages are retained as superseded diagnostic history. These grouped exports replace them for the next round. No launcher imports, game launches or performance measurements were performed. Native archive integrity and exact branch additions are verified. Configured Defaults preserves existing ordinary preferences; use fresh imports to receive the new updater default.
