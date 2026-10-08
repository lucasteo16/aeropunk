Current package: optimizers.

# Astropunk grouped regression tests

Use three feature groups, not individual-mod brute force. All are based on stable main with Chunky, Astropunk branding and disabled Distant Horizons update checking. Rendering remains disabled. Main is unchanged; no merge is approved.

- grouped/chunky: trusted baseline candidate with Chunky and common fixes.
- grouped/northstar: baseline plus Northstar, original Aeronautics compatibility, the rendering bridge, Paxi recipe correction and AeroWarptics.
- grouped/optimizers: baseline plus Async Logger, Jasione and ServerCore.

The travel and optimizer branches are independent children of the Chunky baseline, not cumulative. Test the baseline first, then each feature group on Java 21 in fresh imports with identical memory, graphics settings and comparable separately created worlds. Keep Chunky tasks inactive unless testing pregeneration itself. Subdivide only the failing group. If both pass separately but the combined pack fails, investigate interactions between groups.

The old isolation branches and packages are retained as superseded diagnostic history. These grouped exports replace them for the next round. No launcher imports, game launches or performance measurements were performed. Native archive integrity and exact branch additions are verified. Configured Defaults preserves existing ordinary preferences; use fresh imports to receive the new updater default.
