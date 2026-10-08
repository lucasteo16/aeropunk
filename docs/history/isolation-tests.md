Historical reference from the retired combined experiment. This does not describe the current edition or testing plan.

# Astropunk feature isolation trials

## Current grouped test round

The current bundle is `dist/astropunk-grouped-tests-2.zip`. It contains `0.3.0-grouped.chunky.2`, `0.3.0-grouped.optimizers.2` and `0.3.0-grouped.northstar.2`. Test Chunky first, optimizers second and Northstar last. Both feature branches independently inherit Chunky baseline commit `18228de4b230ed48fffd0f52182abae26b3eb15d`, not each other's additions. Branch ancestry, all shared mod metadata, shared exported download entries and shared override bytes were verified.

The common baseline removes AFK Cinematics and Steppy, restores native Dynamic FPS defaults, and adds Sound Physics Remastered, Presence Footsteps with Sable compatibility, and Cool Rain Reforged with Sable compatibility. All five audio additions are client-only. Each group has native Modrinth, CurseForge client and server exports. The bundle manifest records all nine verified exports and their checksums. Superseded revision 1 grouped packages and bundle were moved to `dist/.archive/grouped-round-1`, not deleted. Live launcher instances remain untouched.

No crash-specific mod removals or version changes were made. Chunky, Distant Horizons and Progress Peek remain selected. Northstar retains AeroWarptics, original Aeronautics compatibility, the rendering bridge and Paxi recipe correction. Optimizers retains Async Logger, Jasione and ServerCore. The Northstar bridge override issue is on hold. Distant Horizons starts with a disabled rendering preference, but players may enable it; the unchanged Northstar bridge can override that choice at runtime.

For the intermittent loading crash, compare first world creation in a fresh instance, another new world in the same instance, and reopening an existing save. Record the case and matching crash report. A successful retry does not prove a fix. No client or server runtime was launched during this rebuild. Main and the mixed experimental mod selections are unchanged. No push was performed.

## Historical individual trials

The eight-package plan below is superseded and retained as historical diagnostic documentation. Its statements describe that earlier round, not the current grouped packages.

Eight independent client packages were created from stable main 0.2.7. All use the same control, with Astropunk branding, the current icon and Distant Horizons update checking disabled. The renderer remains disabled. No existing baseline mod selections or preference presets were otherwise changed.

| Trial | Git branch | Addition to control |
| --- | --- | --- |
| Control | `isolation/control` | None |
| Async Logger | `isolation/async-logger` | Async Logger 2.2.2, client only |
| Chunky | `isolation/chunky` | Chunky 1.4.23 |
| Jasione | `isolation/jasione` | Jasione 1.0.9 |
| ServerCore | `isolation/servercore` | ServerCore 1.5.19 |
| AeroWarptics | `isolation/aerowarptics` | AeroWarptics 1.3.0 |
| Northstar | `isolation/northstar` | Northstar 0.6.6, original Aeronautics compatibility and Paxi recipe correction |
| Northstar with bridge | `isolation/northstar-bridge` | Same Northstar package with bridge 0.6.4 and its structure transfer disabled |

The bridge trial differs from the Northstar trial only by the bridge selection and its configuration. Optimizers are not combined with each other or with either travel trial. The earlier mixed experimental branch is preserved, not approved for merging. Main remains unchanged.

## Manual comparison

Extract the package bundle, then import each Modrinth pack as a fresh instance. Do not update existing instances or move worlds between trials with different content.

Use Java 21, the same memory allocation, shader choice, render distance and simulation distance for every trial. Use the same world seed and comparable route in separately created worlds. Allow initial generation to settle before comparing ordinary movement. Record whether degradation affects frame rate, frame-time stutter, chunk loading or server tick behavior.

Start with the control, then the four individual optimizer trials and AeroWarptics. Compare Northstar against the control in the Overworld first. Compare the bridge trial directly with the Northstar trial. Test planetary generation separately from ordinary Overworld play. Keep Chunky tasks inactive for the installation-only comparison.

Passing individual trials does not prove their eventual combination performs well. Combine only after the separate results identify acceptable components. Do not merge any experimental feature into main without approval.

## Distant Horizons quick check

The original template, exported mixed package and inspected current instance all select `DISABLED` for `client.advanced.debugging.rendererMode`. The similarly named `enableRendering` entry is only for debug wireframes. The template has debug keybindings disabled, silent updates disabled and no second active Distant Horizons configuration distributed alongside it.

The new control changes only `client.advanced.autoUpdater.enableAutoUpdater` to false. This common change is inherited by every trial. Configured Defaults initializes missing ordinary configuration files but preserves existing ones. Thus an existing instance can retain an enabled renderer or update checker despite an updated template. These packages are intended for fresh imports.

No restart reproduction was run. The observed files do not establish why rendering appeared to enable itself. For a manual check, inspect the renderer switch after first launch, quit normally, restart the same fresh instance and inspect it again. Distinguish actual distant terrain rendering from generation activity or generated database files.

## Verification and limits

Native packwiz and Just created all eight client exports. Archive integrity, exact expected additions, unchanged baseline manifest entries, unchanged baseline override bytes, disabled rendering and disabled update checking were verified. AeroWarptics is bundled in game overrides rather than appearing as a Modrinth download reference.

No client or server runtime was launched for these isolation releases. Packaging verification is not a performance result. Live launcher instances and worlds were not modified. No branch was pushed.

The export manifest in the bundle records branch commits, package paths and SHA256 checksums. Package version identifiers use `0.3.0-isolation.<trial>.1`.