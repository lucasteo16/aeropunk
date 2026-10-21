# Astropunk hosting

## Clients

Regular hosting and Hosting Light are the primary client editions. Their sources are the normal Git branches `admin/hosting` and `admin/hosting-light`. Both inherit accepted shared fixes; Hosting Light inherits hosting and removes only the nine entries in its tracked `docs/light-edition.json`. Private OpenCL generation is excluded from both.

Read `pack.toml` for the checked-out source version and loader requirements. Source versions and already-built archives are separate: synchronizing source does not rebuild an export or change a running installation.

From the requested hosting checkout, run `just export-modrinth`. Share the resulting `dist/astropunk-<version>-modrinth.mrpack` directly. Do not create a renamed live-client duplicate. Hosting Light needs no ignored snapshot or separate exporter.

Fresh installations receive the saved Astropunk entry for `astropunk.sparked.network`, its icon and the balanced client defaults. Configured Defaults preserves existing server lists and ordinary player preferences. Shaders remain disabled initially. EasyAuth is server-only; clients need neither EasyAuth nor TrueUUID. Just Enough Breeding 3.3.1 is shared client-and-server content: Lucas confirmed that server installation restores multiplayer breeding information.

## On-demand server preparation

Server exports, managed-host uploads and tests run only when requested. `just export-server` remains the native CurseForge server distribution command. Its manifest may contain download references, so the archive is not necessarily a complete upload folder. Resolve its manifest downloads with a compatible installer before claiming it is materialized.

The existing optional `just test` workflow uses native Modrinth export and the standard `mc-image-helper install-modrinth-modpack` installer in a disposable Docker test. It retains the reusable installation under `build/server-installation`. It is not part of client export or source synchronization. Do not run it merely to obtain a client pack.

The complete standalone-server bundle builder is retired. A previous local test report is not an input to normal native exports. Existing server deliveries and runtime installations are preserved, not silently rebuilt or deleted.

## Apollo managed hosting

The provider owns Minecraft, NeoForge, Java, networking, memory and startup. Use the Minecraft and NeoForge versions in the hosting branch's `pack.toml`; the current Minecraft 1.21.1 baseline uses Java 21 unless separately testing another compatible runtime.

Stop normally before replacing runtime files. Upload the selected server-supported mod binaries and authoritative server configuration from an explicitly prepared managed-host delivery. Remove exact obsolete mod versions rather than keeping duplicates. Merge the supplied files into existing folders; do not replace whole configuration or mod directories. Preserve host-owned authentication files, unrelated settings and player data.

Do not upload loader libraries, launch scripts or Java argument files when Apollo supplies the installation. Top-level handbook resource packs, player default templates, launcher icons, pack manifests and local reports are not managed-server runtime inputs. Keep server datapacks and resource integrations loaded from the configuration folder. Keep the packaged GuideME and handbook helper mod selection unchanged unless separately reviewed.

Upload a prepared world only when requested, separately from pack updates, with `world/level.dat` directly beneath the server root. Never replace an existing played world as part of an ordinary pack update.

Preserve provider-assigned networking. EasyAuth requires `online-mode=true` and `enforce-secure-profile=false`. Whitelist policy and premium password bypass must match the administrator's intended admission rules; do not assume distributed defaults match later host edits.

## Authentication

EasyAuth for NeoForge 3.2.2 is selected. Distributed defaults retain premium automatic login, global-password login without individual registration, and disabled remembered sessions. Lucas has separately changed premium automatic login and session duration on the host; release maintenance must not overwrite those choices.

Set the group password privately with `auth setGlobalPassword YOUR_PRIVATE_PASSWORD`. Never use an account password. Changing the password does not itself require a restart; changes affecting command registration or server properties require one. Provider console history may retain the command.

Preserve `config/EasyAuth/technical.conf`, storage settings and the generated account database. These are deliberately excluded from Git and exports. Never distribute a real password or hash.

The password controls group admission, not ownership of an offline name. Avoid impersonable offline administrators. With premium automatic login enabled, verified premium players bypass the group password; enforce a suitable admission policy for a friends-only server.

## Verification and retention

Native archive checks establish pack identity, selected downloads and authored overrides. Disposable startup and shutdown establish server lifecycle only. Player authentication, recipe visibility, gameplay, provider deployment and backup restoration are separate checks. A previous successful startup does not prove a newly selected delivery works.

Native exports retain the newest two completed release versions. Cleanup is separate from source maintenance and preserves protected deliveries, worlds and shared download caches. No command in this document authorizes changing Apollo, an installed client or a played world automatically.
