# Hosting authentication research

## Selected implementation

Lucas approved replacing TrueUUID with EasyAuth for NeoForge. Hosting 0.15.2 selects EasyAuth 3.2.2 on the server only and removes TrueUUID from both sides. The earlier candidate review below is historical, not the current installation state.

Release source inspection confirms the adapter requires online mode enabled. Its login mixin lets detected premium names continue through vanilla account verification; it does not merely trust a public name lookup as proof of identity. Nonpremium names take the offline route. Premium automatic login bypasses the shared password. Global password mode with single-use disabled accepts the shared password without individual registration. Same-address session reuse is disabled in the shipped preset.

The released artifact targets Minecraft 1.21.1 and requires NeoForge 21.1.230 or newer. The pack's 21.1.259 meets that bound. Required library jars, including the permission bridge, are bundled. Publisher SHA-256: `04c9bc181d1a4a6672030fc5db592fc5ae92634d8ffe74e4ee8ebfe50c70113c`.

No real shared password or hash is distributed. Lucas must set it privately on the host with the documented administrator command and restart before admitting players. See `hosting.md` for the replacement server-property instructions and `reports/live-server-verification.json` for runtime evidence. Actual player login remains unverified.

Sources: https://github.com/Rico040/EasyAuthForNeoforge/releases/tag/3.2.2 and the same tag's ServerLoginPacketListenerImplMixin, AuthHelper, AuthCommand and main.conf template.

## Earlier candidate review

## Desired behavior

TrueUUID verifies premium account identities during login. Offline players need an additional server password or private access protection, because knowing a whitelisted offline name is not proof of ownership. Restrict additions to the hosted edition, preserving shared gameplay branches.

## Candidate: EasyLogin

Project: https://modrinth.com/mod/easylogin
Source: https://github.com/BigBangcraft-server/easyLogin

- Dedicated-server-only mod with a NeoForge 1.21.1 artifact. No additional client mod is required for password commands.
- Modrinth returned 5,733 project downloads at inspection. Its exact NeoForge 1.21.1 version 1.0.1 had 3,750 downloads; version identifier `tpr8fHX7`.
- GitHub also publishes a newer 1.0.2 NeoForge 1.21.1 artifact, while that version was not present in the filtered Modrinth results. Do not silently treat the two sources as identical releases.
- Inspected release 1.0.2 source: login state and stored accounts use the admitted player's identifier; password hashes use BCrypt with cost 12; unauthenticated players face movement, interaction and command restrictions.
- Every real player is put into the unauthenticated state on join. No direct TrueUUID integration or premium bypass was found in that join handler. Expect premium players to register and log in too unless a separately reviewed integration is added.
- Public searches found no documented TrueUUID combination test. Being downstream of TrueUUID's login-stage identity selection makes this a plausible candidate, not verified compatibility.
- Open upstream issues include a NeoForge 1.21.1 LuckPerms command-permission problem (issue 1), and an unused limbo-world option (issue 2). Avoid selecting extra features on assumption.

## Alternatives

EasyAuth is more widely used (225,085 project downloads returned), but its Modrinth release list returned no exact NeoForge 1.21.1 artifact. A separate NeoForge port exists at https://github.com/Rico040/EasyAuthForNeoforge. Its independent account-verification and identity features may overlap TrueUUID; compatibility and maintenance require separate evaluation. Do not install the Fabric build into this pack or import it merely because the name is established.

Simple Login offers automatic per-client secret-based login, but adds client state that must be preserved and must not be shared with friends. It is not the selected candidate for this bounded review. No release compatibility claim is made here.

## Recommendation and reversible test

Evaluate EasyLogin as an additional password layer in the hosting edition only. Keep it uninstalled until approved. Use a disposable offline-mode copy with TrueUUID, never the prepared world. Test premium registration, offline registration, wrong-password denial, reconnect authentication, pre-login movement and inventory restrictions, command access without administrator privileges and attempted reuse of an already registered offline name. Test custom mod interactions before calling the whole gameplay surface protected.

Registration is first-claim ownership. Enroll friends while the server is private and supervise first registration, otherwise an attacker may register a friend's offline name first. Use unique server passwords, not Microsoft or email passwords. Password hashes and account records become persistent private server data; keep them across upgrades and do not bundle them into releases. Server administrators and the provider control the running authentication code and may see submitted commands; hashing at rest does not establish transport secrecy or protect against an untrusted host.

Costs: no subscription required for these open-source mods, but account recovery, enrollment, updates and security testing become administrator responsibilities. A successful startup would not prove authentication protection.

Sources inspected: release-tagged EasyLogin 1.0.2 AuthManager, PasswordService and NeoForgeEventHandler; GitHub releases and issues; live Modrinth project and version metadata; TrueUUID 1.3.0 documentation. Download counts are a point-in-time adoption signal, not a security audit.
