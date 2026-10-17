# Aeronautics orientation trial

Development release: 0.12.0-dev.

## Approved additions

- Aeronautics Camera Sync 1.4.0, Modrinth project ZGxtWu73 and version UbgVQ0qd.
- Aeronautics Player Tilt 0.2.3, CurseForge project 1681706 and file 9138420.
- Both are selected on client and server and remain unpinned. Existing mod metadata is byte-identical to the previous development checkpoint.
- Preserve the earlier adaptive Distant Horizons transfer setting. No played client, retained server, world, stable branch or remote branch was updated.

## Cosmonautics assessment

Selected Cosmonautics: cosmonautics-26.08.307.jar. Selected Sable: 2.0.6. Minecraft: 1.21.1. NeoForge: 21.1.259.

Publisher-checksum-verified released archives declare compatible loader and dependency ranges. Player Tilt requires Camera Sync 1.4.0 or newer; both require Sable 1.1.1 or newer. The selected versions satisfy those declarations. This is not full gameplay clearance.

No Cosmonautics, gravity or dimension-specific report was found when checking the 34 returned Camera Sync issue entries. This does not establish that no defect exists, and Player Tilt's complete issue history was not available in this check.

Player Tilt advertises world-relative and sublevel-relative falling. Cosmonautics independently contains entity, living-entity and physics integration plus dimension transfer. Their combined behavior in low gravity, orbit and ship transfers remains untested. Camera and body alignment are distinct from physically correct planetary gravity.

## Verification

- Native Modrinth client export and native CurseForge server export completed.
- Both archives passed ZIP integrity checks.
- Camera Sync is retained for both sides in the Modrinth manifest.
- Player Tilt is bundled in the client archive and referenced by exact project and file in the native CurseForge server manifest. The native smoke installer materialized it successfully.
- Installed Camera Sync, Player Tilt and Cosmonautics binaries matched their authoritative metadata checksums.
- Disposable server smoke test reached readiness with all three mods in the loaded inventory, shut down normally with exit code zero, and removed temporary test resources.
- Evidence: reports/result.json and reports/server.log. The run contains nonfatal error-level messages elsewhere in the pack; successful startup is not an error-free-pack claim. No error-level line named either new addon's identifier.
- Existing mod metadata remained byte-identical; exactly the two approved mods were added. Pack index hash and Git whitespace checks passed.

## Manual acceptance before stable promotion

1. Walk, jump, crouch, climb and sleep on a banked Sable ship. Check third-person model and hitbox alignment.
2. Test projectile aiming, dropped items, buckets and representative Create tools with both mods on client and server.
3. Compare world-relative and sublevel-relative falling on a planetary surface and in orbit. Check for unintended gravity or fall-damage behavior.
4. Transfer a crewed Cosmonautics ship between dimensions and verify camera, body pose and collision recovery. Step off and reboard to check that tilt clears correctly.
5. Use the native camera and body toggles or item blacklist for isolation. Restore only these two additions if the combined trial introduces a blocking regression.

## Sources

- https://modrinth.com/mod/aero_cam_sync
- https://www.curseforge.com/minecraft/mc-mods/aeronautics-player-tilt
- https://github.com/playsi/Aeronautics-Camera-Sync/issues
- https://github.com/playsi/Aeronautics-Camera-Sync/blob/master/docs/compatibility.md
