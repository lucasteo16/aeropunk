# Astropunk

## Client distribution 0.15.3-hosting

The pack display name is always `Astropunk`. Branch names, version identifiers and artifact filenames distinguish editions, never the pack name.

`dist/astropunk-0.15.3-hosting-live-client.mrpack` adds the saved `Astropunk` multiplayer entry for `astropunk.sparked.network`, including its saved icon, through `configureddefaults/servers.dat`. Configured Defaults supplies this file only when a client has no server list, preserving existing player lists. This client-only packaging update leaves the existing 0.15.2-hosting server artifacts and installed clients untouched; it does not change gameplay or require a server update.

## Existing server distribution 0.15.2-hosting

This administrator edition branches from stable Astropunk 0.15.1 on `admin/hosting`. Shared gameplay remains upstream on `main`. Do not merge hosting policy into main. This edition does not contain the private world-generation OpenCL module.

## Distributions

- `dist/astropunk-0.15.2-hosting-live-server/` is the fully materialized server folder. Upload its contents directly into the provider's server root. All selected server mod binaries, configurations and installed Minecraft and NeoForge libraries are present. No pack installer is needed on the host.
- `dist/astropunk-0.15.2-hosting-live-server.zip` contains exactly that folder's contents at archive root. Extract locally before transfer, or use the provider's extraction button if available. The world is intentionally absent.
- `dist/astropunk-0.15.2-hosting-live-client.mrpack` is the matching client pack, importable through Modrinth or Prism. It uses the launcher's ordinary dependency downloads. Neither EasyAuth nor TrueUUID is required on the client: EasyAuth is server-only, and TrueUUID has been removed from this edition.
- The native `just export-server` and `just export-modrinth` commands remain unchanged. Their ordinary outputs are build inputs, not the drag-and-drop live server. The live folder was materialized from the verified server installation and native server overrides, with every selected server mod checked against authoritative pack metadata.
- Minecraft 1.21.1, NeoForge 21.1.259, Java 21.
- EasyAuth for NeoForge 3.2.2, exact Minecraft 1.21.1 artifact from Rico040's GitHub release, verified against its published SHA-256 digest. Its loader requirement is NeoForge 21.1.230 or newer; the pack uses 21.1.259. Required library dependencies are bundled in the released mod.

## Provider setup

1. Stop the provider's server and select Java 21. Upload the live server folder's contents into the server root, so `mods`, `config`, `libraries` and `run.sh` are directly there. Do not upload the outer folder as an extra nesting level. Do not run an installer or a vanilla server against this pack.
2. Configure the panel to launch `sh run.sh nogui`, or use `java @user_jvm_args.txt @libraries/net/neoforged/neoforge/21.1.259/unix_args.txt nogui` from the server root. The included memory file uses a 1 gigabyte initial heap and 4 gigabyte maximum heap, matching the disposable test. Adjust it to the provider's allocation, leaving memory for Java overhead. If the panel supplies its own memory flags, omit `@user_jvm_args.txt` and let the panel own them. A panel that only permits `java -jar server.jar` needs provider support for a NeoForge argument-file launch; do not rename a library jar to fake that entry point.
3. Accept the Minecraft EULA through the panel. Set `level-name=world`, `online-mode=true`, `enforce-secure-profile=false`, `white-list=true`, `enforce-whitelist=true`, `enable-rcon=false`, `enable-query=false`, `view-distance=8` and `simulation-distance=6` in the provider's server properties. Use the provider-assigned port and leave `server-ip` empty unless the provider requires otherwise. Set `motd=Astropunk Live | 0.15.2` if desired. These host-owned settings are not shipped as shared client overrides. Do not retain the former TrueUUID instruction to disable online mode.
4. Start with access restricted. In the private provider console, run `auth setGlobalPassword YOUR_PRIVATE_PASSWORD false`, replacing the placeholder yourself. Do not use your Microsoft or email password. Restart afterward so the command registration and shared-password mode agree. The real password and its hash are deliberately absent from the release. The provider console and its history may retain the command, so treat them as sensitive.
5. The shipped `config/EasyAuth/main.conf` enables premium automatic login, enables global password login, disables individual registration, and disables same-address session reuse. Premium players use normal Minecraft account verification and skip the shared password. Offline players enter `login YOUR_PRIVATE_PASSWORD` as an in-game command, with the usual leading command slash. Nobody needs to register. Do not open access until the real shared password has been set.
6. Restore or create the whitelist using each player's admitted identity. Premium players keep their official account identifier. Offline players need their name-derived offline identifier; a panel account-name lookup may not create the correct entry. Test premium login, offline correct-password and wrong-password cases, and unlisted-player rejection. Do not grant administrator privileges to bypass a login failure. Do not mark a premium account name as offline merely to fix an invalid-session error.
7. Upload the prepared world as a separate later step, with the server stopped. Map `initial-save/world` directly to the provider's `world`, avoiding `world/world`. Do not merge an accidentally generated temporary world into the prepared world. The source world, manual server and original archive remain unchanged.

## Identity policy and limitations

This EasyAuth adapter needs online mode enabled. It checks whether a name belongs to a premium account; premium names continue through vanilla Minecraft session verification, rather than receiving an official identifier merely from a name lookup. Names without premium accounts take its offline path and need the shared password. Offline launchers using an existing premium account name can receive invalid-session errors; use a distinct offline name rather than weakening premium-name protection.

The shared password is a group entry gate, not individual identity proof. Anyone who knows it may impersonate another offline name. Premium players are protected by Minecraft account verification, but this policy intentionally lets verified premium players bypass the group password. The whitelist therefore remains important. Rotate the shared password if it leaks. Do not distribute the server's generated authentication files or database with later releases.

Preserve the generated EasyAuth account database and `config/EasyAuth/technical.conf` on the host across upgrades. The technical file contains the password hash. Never overwrite host-owned authentication state with release defaults. No existing hosted player data has been migrated or reset by this change.

## Verification scope

Packaging checks EasyAuth server inclusion, client exclusion, TrueUUID removal, baseline mod preservation and loader requirements. The disposable project test checks installed server readiness and normal shutdown. The separate live-folder test runs the extracted upload archive directly, without an installer or network access, with a fresh disposable world and online mode enabled. Neither startup test proves player authentication. Actual premium verification requires internet access on the host. Player login, wrong-password rejection, offline access, whitelist behavior and provider startup selection remain deployment checks.

Source: https://github.com/Rico040/EasyAuthForNeoforge/releases/tag/3.2.2 and its release-tagged login mixin, AuthHelper, configuration templates and administrator command implementation.
