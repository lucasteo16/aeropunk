# Astropunk editions

## Development branch

`dev` is the integration branch for future mod updates and pack changes. Keep `main` and `main-heavy` stable; promote reviewed and tested changes deliberately, with shared gameplay entering `main` before `main-heavy`. Run the existing `just update` command on `dev` for native global updates, preserving compatibility holds and the fixed Minecraft and NeoForge versions. Never deploy development updates to played instances or the retained server implicitly.

### 0.7.5-dev Deep Seas notification defaults

Moved the startup-screen suppression preset from create_submarine-common.toml to create_submarine-client.toml for Deep Seas 3.3.0. The client.disableStartupScreens setting remains true, suppressing welcome and update prompts on fresh installations without changing gameplay settings or existing player choices. Lucas reported that 0.7.4-dev seemed to work, with the Deep Seas prompt reappearing; exact test coverage was not specified. The corrected notification default still requires a fresh-client check.

### 0.7.4-dev missing dependencies

Added Struts 1.3.1 and Azimuth 1.4.10 on both sides through native packwiz. These satisfy the released dependency declarations for Bits 'n' Bobs 2.3.5 and More Girder 2.3.0; their Minecraft and NeoForge requirements match this development pack. GrandTeleport remains held at 1.0.0, and Spell Engine 1.10.9 and Xaero's Maps Multiplayer Plus 1.1.2 remain compatibility trials. Export verification does not establish successful game startup; Lucas's fresh-client test is pending.

### 0.7.3-dev GrandTeleport rollback

The global update changed GrandTeleport from 1.0.0 to 1.0.1. Lucas's client rejected 1.0.1 as an invalid mod file, so development restores the original both-side 1.0.0 selection and holds it pending a verified replacement. This rollback does not establish the exact cause of the invalid-file error. The separately reported missing Struts and Azimuth dependencies remain unresolved in this checkpoint; this export is not yet expected to pass startup. Spell Engine and Xaero's compatibility trials remain unchanged.

### 0.7.2-dev compatibility trial

Spell Engine is updated from 1.10.7 to 1.10.9 and Xaero's Maps Multiplayer Plus from 1.1.0 to 1.1.2 for Lucas's fresh-client test. Their development holds are removed; stable branches retain their previous selections and holds. Neither candidate is yet runtime-verified. Test startup and disposable single-player world entry first, watching for the former Witcher loot-function failure and Xaero's bundled Java module-descriptor failure. The retained server still runs the stable pack, so it is not a matching target for this development client's multiplayer test.

If the relevant failure recurs, revert only the implicated selection to its previous version and restore its compatibility hold. Commit 34ce59f and the retained 0.7.1-dev export preserve the pre-trial baseline. Do not revert unrelated development updates or modify played instances implicitly.

### 0.7.1-dev update checkpoint

NeoForge is updated from 21.1.255 to 21.1.259 without changing Minecraft 1.21.1. The previous global update changed 65 mods and Better Leaves, including an unintended Terralith downgrade. Terralith's NeoForge 2.6.2 selection is now restored through native packwiz. Its older multi-loader release includes Fabric, which packwiz prefers during its loader-list comparison; this was not a compatibility-driven downgrade. Review this selection after future global updates.

Spell Engine and Xaero's Maps Multiplayer+ remained held at this checkpoint. Reinforced Shulker Boxes and ToolTipFix publish Fabric releases, excluded by the NeoForge updater filter despite Connector support. GroovyModLoader's selected release is tagged Minecraft 1.21 rather than 1.21.1. Their existing selections remain unchanged; updater lookup failures do not establish runtime incompatibility. Updated selections are experimental, not gameplay-certified.

## Shader selection in 0.6.7

Fresh installations select Complementary Reimagined r5.9.3 while leaving shaders disabled. Configured Defaults preserves existing player settings. No rendering mods or server deployment were changed.

## Multiplayer compatibility in 0.6.6

Better Advancements 0.4.3.21 replaces Reliable Advancements as a client-only advancement screen improvement. The unused editor settings and saved layout are archived outside the distributed pack. Existing Minecraft and content-mod advancements are unchanged; no custom advancements were authored.

Sinytra Connector and Forgified Fabric support are included on both clients and servers so NeoForge can load the selected Fabric gameplay content, including Reinforced Shulker Boxes. The previous server skipped that archive despite having it installed. Client reconnection and reinforced storage gameplay still require player verification after deployment. Use a fresh 0.6.6 client import because Reliable Advancements must no longer be loaded.

The retained local server reached healthy startup with Reinforced Core and Reinforced Shulker Boxes loaded. Connector also exposes a Moonlight compatibility warning and a Tectonic Fabric overlay metadata error about its configuration resource condition. These are nonfatal startup findings, not verified terrain compatibility; no terrain settings or gameplay content were changed to suppress them.

## Grand Teleport server inclusion in 0.6.5

Grand Teleport 1.0.0 is included on both clients and servers because its NeoForge port requires matching teleport network channels. The client artifact is unchanged from 0.6.4. Dedicated-server startup and a player reconnection are separate validation steps.

## Interactic networking in 0.6.4

Main selects Interactic Renewed 0.2.3 for both clients and servers. The released archive moves filter-mode response registration into shared initialization, addressing the missing channel in 0.2.2. Lucas's subsequent connection screenshot no longer listed the Interactic mismatch; Grand Teleport still blocked that attempt.

## Typing sounds in 0.6.3

Fresh installations disable chat and inventory typing sounds from Sounds. Other sound effects remain unchanged. Configured Defaults preserves existing player settings, so existing installations need these two effects disabled manually in the Sounds settings.

The default main branch is the lean gameplay baseline. The main-heavy branch independently inherits main and adds the optional client visual stack. Apply shared gameplay, fixes and updates to main first, then merge main into main-heavy. Do not merge heavy-only visuals back into main. Both have separate Git workspaces and use native packwiz and Just exports.

The split follows Lucas’s disabled screenshot selections. Heavy adds Fancy Crops, all four Fresh Animations packs, Simple Grass Flowers, Visual Effects+, Create Sable Dynamic Lights, Eating Animations, Not Enough Animations and its Entity Model Features compatibility addon, Explosive Enhancement, Fancy World Animations, Particle Effects, Particular Reforged, Ripple, Sodium Dynamic Lights and Team Capes. Heavy also initializes Interactic fancy item rendering as enabled; lean initializes it as disabled. Interactic gameplay settings and artifact remain identical. Configured Defaults preserves existing ordinary configuration files, so use fresh imports to compare the presets.

Spawn Animations and Spawn Animations Compats are excluded from both editions. Spark is server-only in both, which excludes client profiling and profiling local single-player through a bundled spark installation. Rendering optimizations and gameplay animation libraries are retained. Better Leaves, shaders, Distant Horizons, audio additions, Mandala’s dark interface and Hide Experimental Warning are retained; they were not part of this screenshot-defined removal batch. Shader and Distant Horizons rendering preferences remain initially disabled, not restrictions on player choices.

Cosmonautics, Deep Air and Cosmonautics Expansion are promoted in 0.6.0 as optional space activities, not mandatory progression. Northstar's superseded trial is retired with its history preserved. Retired optimizer and isolation branches have been removed after promotion or supersession. Packaging checks do not establish runtime compatibility or measured frame rates. Lucas reported a large improvement after disabling the screenshot group; no individual cost is established.

The optimizer trial was manually tested by Lucas and promoted to both editions. Shared additions are Async Logger, Jasione and ServerCore. The retired Northstar trial had unresolved rendering issues; its unique selections were Northstar Redux, the Northstar-Aeronautics compatibility addon, the Sable Iris Horizons bridge and Paxi.

## Ship teleportation additions in 0.5.0

Main includes Create: AeroWarptics 1.3.0 for same-dimension relocation of assembled Aeronautics ships and AeroEngine fuel compat 0.0.2 for accepting shared fuel tags, including TFMG Community Edition kerosene. The fuel addon accepts the broader common fuel tag, not only kerosene, and does not rebalance each fuel's energy value.

Lucas authorized inclusion before functional travel and fuel testing. The fresh official launcher instance reached world entry, saved and shut down normally. Its latest and debug logs contained no fatal markers or error-level messages naming these additions. Nonfatal recipe, model, Sable property, item-browser and Distant Horizons with Chunky integration errors remain separate unresolved findings. Actual teleportation, passenger and inventory preservation, and fuel consumption are unverified.

The original isolated proposal and packaging evidence are retained in docs/ship-teleportation-proposal.md and docs/ship-teleportation-verification.json as historical records. No live installation is updated and no push is performed.
