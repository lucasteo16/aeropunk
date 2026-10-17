# Astropunk

## Current hosting release

The current hosting client is `0.15.4-hosting`, based on shared Astropunk `0.15.4`. This release adds saved low-quality shader defaults only; the verified `0.15.3-hosting` live server remains unchanged and no server update is required. Every edition retains the display name `Astropunk`. Hosting authentication and the saved server listing stay on `admin/hosting`; private OpenCL generation is excluded.

## Deliverables

- `dist/astropunk-0.15.4-hosting-live-client.mrpack` is the client to share with friends. Fresh installations receive the saved Astropunk entry for `astropunk.sparked.network`, including its icon, and the saved low-quality settings for all three bundled shaders. Configured Defaults preserves existing player server lists and shader settings. Shaders remain disabled initially. EasyAuth is server-only; clients need neither EasyAuth nor TrueUUID.
- `dist/astropunk-0.15.3-hosting-live-server/` is the complete materialized server release, also provided as a matching ZIP archive. It contains no world, real shared password or account database.
- Native Modrinth, CurseForge client and server exports remain available through the ordinary Just commands. The prepared world is transferred separately.

## Apollo managed hosting

The provider owns Minecraft, NeoForge, Java, networking, memory and startup. Select Minecraft `1.21.1`, NeoForge `21.1.259` and Java 21 unless separately testing another compatible runtime.

Stop normally before replacing files. Upload `mods` and the complete `config` folder from the live server. Remove obsolete mod versions instead of merging duplicates. Upload the prepared `world` separately, with `world/level.dat` directly beneath the server root. Preserve existing host-owned authentication files and player data during updates.

Do not upload standalone `libraries`, launch scripts or Java argument files when Apollo supplies the installation. Top-level handbook `resourcepacks`, `configureddefaults`, launcher icons, manifests and upload instructions are not needed on the managed server. Keep the packaged GuideME and handbook helper mod selection unchanged.

For an unmanaged standalone installation, the release includes loader libraries and native launch scripts. Use `sh run.sh nogui` on Linux or the bundled Windows script, with a separately installed compatible Java runtime. This is an alternative to provider-owned startup, not an additional Apollo installation step.

Preserve provider-assigned network settings. EasyAuth requires `online-mode=true` and `enforce-secure-profile=false`. Whitelist policy and premium password bypass must match the administrator's intended admission rules; do not assume distributed defaults match later host edits.

## Authentication

EasyAuth for NeoForge `3.2.2` is selected. Distributed defaults retain premium automatic login, global-password login without individual registration, and disabled remembered sessions. Lucas has separately changed premium automatic login and session duration on the host; a release-label update must not overwrite host-owned choices.

Set the password privately with `auth setGlobalPassword YOUR_PRIVATE_PASSWORD`. Never use an account password. Changing the password does not itself require a restart; changes affecting command registration or server properties require one. Provider console history may retain the command.

Preserve `config/EasyAuth/technical.conf`, storage settings and the generated account database across updates. These are excluded from Git and exports. Never distribute a real password or hash.

The password controls group admission, not ownership of an offline name. Avoid impersonable offline administrators. If premium automatic login is enabled, verified premium players bypass the group password, so an enforced whitelist remains important for a friends-only server.

Before admitting players, test premium verification, intended password requirements, an offline friend, wrong-password rejection and reconnect behavior. When using a whitelist, also test an unlisted player. Startup does not prove authentication behavior.

## Rebuilding and retention

Run `just export-modrinth`, `just export-server` and `just test`. After matching server verification passes, `python scripts/export_live_server.py` materializes the complete release from checksum-verified installed mods, native overrides and loader libraries. It verifies the resulting archive and copies the native client to the live-client filename. It refuses to overwrite an existing same-version server folder or archive; inspect and remove those deliberately before rebuilding.

Normal native exports retain the newest two version groups. After all delivery variants pass verification, an explicitly requested latest-only cleanup uses `just retain-releases --keep 1 --apply`. Preserve reusable download caches. These local operations do not modify Apollo or installed clients.

## Verification limits

Native archive checks establish identity, selected downloads and authored overrides. Disposable startup and normal shutdown establish server lifecycle only. Player authentication, gameplay, rendering, provider deployment and backup restoration remain separate checks. The complete standalone archive can additionally be exercised without a network or installer to verify included runtime dependencies.
