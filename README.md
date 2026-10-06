# Aeropunk

A lightweight Minecraft pack centered on Create Aeronautics and Streams Reflowing, with compatible performance improvements and client conveniences.

Current definition: Minecraft 1.21.1, NeoForge 21.1.255, pack version 0.1.0. All 292 mod selections, nine resource packs, and three shader packs are pinned. Packwiz pins hold exact artifacts, not major or minor version ranges. Lucas prefers updates within the same major version for ordinary mods and patch-only updates within the same major and minor version for sensitive core mods. Official pin documentation and the Modrinth updater source were checked: update metadata stores project and exact version identifiers, and its updater selects the latest matching release without a semantic-version range constraint. No global unpin, updater modification or substitute range syntax has been applied. Keep this policy preference separate from native packwiz capability; Minecraft mod versions are not guaranteed to follow semantic versioning.

## Requirements

Install Just, packwiz, Python 3.11 or newer, Docker Engine, and Docker Compose. Docker must be running and accessible to your user. No host Java installation or Python dependencies beyond the standard library are required.

Packwiz uses its default cache outside the repository. On this machine it is `/home/tsb/.cache/packwiz/cache`. Docker uses its normal image cache. Neither is relocated or deleted by the project commands.

## Commands

Run commands from the project directory:

```sh
cd ~/Projects/lucas/aeropunk
just --list
```

| Command | Behavior |
| --- | --- |
| `just export` | Native CurseForge server export to `dist/aeropunk-server.zip`. |
| `just export client` or `just export-client` | Native CurseForge client export to `dist/aeropunk-client.zip`. |
| `just test` | Export, start a disposable Docker server, confirm readiness, stop normally, and clean temporary files. |
| `just export-modrinth` | Native Modrinth export to `dist/aeropunk.mrpack`, with side information for the installer. |
| `just update` | Run `packwiz update --all`, respecting pins. |
| `just clean` | Remove recognized temporary test files and Python bytecode. Preserve exports, latest reports, sources, and caches. |

Because every mod is pinned, `just update` does not automatically move those mods to new versions. Changing a pinned selection is a separate, deliberate packwiz operation.

Just prevents Python bytecode generation for its commands. There is no separate list of verified mods and no repository-local collection of downloaded research copies.

## Exports

The shorthand passes explicit output paths directly to packwiz:

```text
dist/
  aeropunk-server.zip
  aeropunk-client.zip
  aeropunk.mrpack
```

The defaults overwrite those files. Pass an explicit output path to retain a versioned release, for example `just export server dist/Aeropunk-0.1.0-server.zip` or `just export-modrinth dist/Aeropunk-0.1.0.mrpack`. Existing older exports are preserved. `just clean` does not remove distributions.

Export recipes only create the destination directory and invoke packwiz directly. There is no staged copy, custom validation, archive rewrite or move. Packwiz owns archive contents and output behavior. CurseForge side selection uses its native `--side` flag; Modrinth embeds side information for compatible installers.

CurseForge exports legitimately retain Short Stacks as project 580100, file 6974172 in manifest download references. Neither installed export command offers an all-bundled flag. Native Modrinth export bundles that CurseForge-sourced artifact instead, leaving Modrinth download references and side information for the installer. Redistribution permissions remain the pack author's responsibility.

## Server test

```sh
just test
```

The test has bounded, visible phases for preparation, installation, startup, shutdown, and cleanup. It consumes a real native Modrinth archive and derives Minecraft and NeoForge versions from its index. The existing `mc-image-helper install-modrinth-modpack` inside the Docker image downloads files, applies server side selection, extracts overrides and installs the loader. It does not consume a live packwiz snapshot. The installer's optional default exclusion list is disabled, and no custom mod exclusions or dependency bypasses are applied.

The disposable server uses a digest-pinned Java 21 Docker image, a fresh runtime, no published ports, a four-gibibyte Java heap, a five-gibibyte memory limit, and four processors. The Minecraft end-user license agreement has already been accepted for this test server. Existing worlds are not used.

The test waits up to 600 seconds for the startup-complete message and help prompt, then immediately requests normal shutdown. Shutdown must finish within 60 seconds with exit status zero. There is no extra observation delay, forced chunk generation, saved-region inspection, or gameplay exercise.

A pass means the server started and stopped successfully. It does not establish client rendering compatibility, shader support, gameplay stability, or measured performance.

The latest evidence is always written to:

```text
reports/result.json
reports/server.log
```

These files are replaced on each test, including failures. Historical reports do not accumulate. Temporary runtime files are removed only after container and network cleanup is confirmed. If cleanup cannot be confirmed, the runtime remains for recovery and the failure is reported. `just clean` does not stop containers or prune Docker, and it preserves unknown build contents for manual review.

## Project files

| Location | Purpose |
| --- | --- |
| `pack.toml` | Pack name, version, and loader definition. |
| `index.toml` | Distribution index maintained by packwiz. |
| `mods` | Pinned provider metadata, download hashes, and side settings. |
| `config` | Deliberate shared game configuration. |
| `justfile` | Short command entry points. |
| `scripts` | Scoped cleanup and Docker startup coordination. |
| `.archive/unit-tests` | Reversibly archived original twelve-test suite and its review. |
| `dist` | Finished versioned exports. |
| `build` | Disposable work, empty after successful cleanup. |
| `reports` | Latest server result and log only. |

Generated exports, reports, and temporary files are excluded from Git. Operational files are also excluded from packwiz distributions. After changing shared configuration or documented side metadata, run `packwiz refresh` to update the index.

Git tracks the pack definition, not downloaded mod copies. Use a working branch for changes and merge accepted changes into `main`. A startup pass is not a substitute for later client and gameplay checks.

## Compatibility boundaries

Create, Create Aeronautics, Sable, and Streams Reflowing form the gameplay baseline. Sodium, Lithium, FerriteCore, ImmediatelyFast, and ModernFix provide the selected performance improvements. Client conveniences include Sodium Extra, Reese’s Sodium Options, Ok Zoomer, Dynamic FPS, and Quick Pack. Distant Horizons is client-only.

Entity Culling uses safe mode, disables client tick culling, and exempts Create contraption entities. Selected donor configuration files were subsequently copied and merged while preserving these settings; see the donor configuration transfer section. No dependency bypasses were included.

Avoid ScalableLux with Sable, Radium or Palladium with Create, and duplicate Embeddium and Sodium rendering backends. Additional threading and moving-structure rendering optimizations remain deferred.

Iris remains in the authored definition with its optional metadata. Complementary Reimagined r5.9.3, Complementary Unbound r5.9.3, and Photon v1.3b are bundled as client-only choices; no shader is enabled automatically. Client launch and shader compatibility remain unverified. Mouse Tweaks, AppleSkin, and EMI provide inventory, food-information, and recipe conveniences.

C2ME 0.4.0-alpha.0.122, Better Biome Reblend, Kerria, Structure Layout Optimizer, Model Gap Fix, and Neo Bee Fix are selected with their defaults. Resourceful Config is included as a required dependency. C2ME remains an alpha release and has not yet been tested with this selection. Other threading changes are deferred. Better Biome Reblend's universal archive contains a native NeoForge entry point without a Fabric dependency, despite the provider's shared Fabric dependency listing. Existing performance mods use their defaults except for the explicit Entity Culling configuration. Backports, space addons, and additional terrain generation are not part of this baseline.

## LifeOre base additions awaiting review

Selected LifeOre convenience additions include Sophisticated Inventory Interactions, Polymorph, three EMI information addons, Lighty, BetterF3, Toast Control, Trade Refresh, Steppy, Better Days and Villager Names. Cubes Without Borders 3.0.0 provides borderless fullscreen for Windows and other supported platforms. Performance selections include Clumps, Let Me Despawn, Ixeris, Observable, AttributeFix, BadOptimizations, AsyncParticles, AI Improvements and Cull Leaves. Cull Leaves had more Modrinth project downloads than Sodium Leaf Culling at selection time; only Cull Leaves is selected. Required libraries are pinned and inspected. Better Days bundles WhiteNoise.

Particular Reforged 1.5.5, the Not Enough Animations and Entity Model Features compatibility addon, Better Leaves, Simple Grass Flowers and Fancy Crops are selected. Particular uses LifeOre's configuration, retaining its effect toggles, with cave-dust spawn chance changed from 700 to 1400 and particle lifetime from 200 to 100. Cascades and waterfall spray remain enabled. Visual Effects Plus cave dust and underwater effects are disabled so Particular supplies those overlapping effects; its rain remains texture-only. BadOptimizations lightmap caching is disabled against the active Polytone lightmap. These settings were statically validated, not demonstrated in game.

Chloride and Open Parties and Claims are excluded. Fusion remains on hold. Extreme Sound Muffler 3.56 and Better ModList 1.1.22 are selected at LifeOre’s exact versions for an authorized trial. Their inspected Minecraft upper bounds exclude 1.21.1 despite provider labels and donor inclusion. Original requirements are preserved; no dependency bypass was applied. All additions remain untested; no exports were rebuilt.

## Combat additions awaiting review

Better Combat 2.4.0 and Combat Roll 2.0.6 are selected and pinned at native NeoForge 1.21.1 releases. Their required Player Animator library 2.0.4 is selected and inspected; Cloth Config is already present and Tiny Config is bundled with Better Combat. Critical Strike 1.0.4 and Team Capes 1.1.2 are also selected and pinned. Team Capes is provider-labelled Minecraft 1.21, but its native NeoForge archive accepts Minecraft 1.21 and later; this is an untested 1.21.1 trial. It uses vanilla team colors. Nine Fichte expansions are selected and pinned: Archers Expansion 2.1.1, Forcemaster 3.1.1, Elemental Wizards 3.1.1, Berserker 3.1.1, Witcher 3.1.4, Bard 1.1.1, Additional Jewelry 2.3.1, More Relics 1.3.1 and More RPG Classes Skill Tree 1.2.0 (beta). Required core selections include Archers 3.1.3, Wizards 3.1.3, Jewelry 2.5.1, Relics 1.4.0 and Skill Tree 1.6.1. Supporting libraries are pinned, including More RPG Library 2.7.2, Spell Engine 1.10.9, Spell Power 1.6.0, Armor Model API 1.1.0, Ranged Weapon API 3.0.0, Structure Pool API 1.2.1, Runes 1.3.2, Bundle API 1.1.0 and Pufferfish’s Skills 0.19.1. Archive inspection found dependencies omitted by automatic resolution, which were added explicitly. Pufferfish’s Skills is provider-labelled for 1.21.1 but its inspected Minecraft upper bound excludes 1.21.1; the original declaration is preserved for the trial, without a bypass. The complete original series is now selected: Rogues and Warriors 3.1.3, Paladins and Priests 3.1.3, Armory 1.5.2, Arsenal 1.5.0, Gazebos 2.2.0 and Village Taverns 1.3.0 have also been added and pinned. Attribute Icons 1.4 is included as a pinned client-only resource pack. Shield API 2.2.0 was added by provider dependency resolution and its native archive inspected. All eleven original series mods and its resource pack were reconciled against live provider identifiers and exact pinned versions. Separate exploration addons remain deferred. Druids and Tavern Brawl remain excluded. No exports or game tests ran for this batch.

## Food logistics additions awaiting testing

Short Stacks 1.2.2 and Spice of Life: Onion 1.5.6 are selected and pinned for both client and server. Onion requires CreativeCore 2.13.50, also selected on both sides and pinned. The published archives matched provider hashes and their native dependency declarations accept the selected Minecraft and NeoForge versions. Onion calculates dietary diversity from food properties; its default strength, regeneration and speed rewards remain pending the final balance review. Spoiled was removed at Lucas's request because its complexity was not worth the gameplay benefit. No competing nutrition system was added. No exports or game tests ran for this batch.

## Farming and food selections awaiting review

Farmer’s Delight 1.3.2, End’s Delight 2.6, Miner’s Delight 1.4.5, My Nether’s Delight 1.10.2, Smarter Farmers 2.2.4, RightClickHarvest 4.6.1, Universal Bone Meal 21.1.0 and Leaves Be Gone 21.1.1 are selected at exact donor versions and pinned. Lodestone 1.8.2 and JamLib 1.3.6 were added and their dependencies inspected. Miner’s Delight and Lodestone have Minecraft upper bounds excluding 1.21.1; My Nether’s Delight declares a Farmer’s Delight version inconsistent with its donor’s actual selection. These are authorized donor trials, with original requirements preserved for final testing. Create food and farming integrations remain deferred. No exports or game tests ran for this batch.

## Equipment and recovery selections awaiting review

Corpse 1.1.13, Corpse and Curios compatibility 4.0.1, Comforts 9.0.5, TorchMaster 21.1.9, Lootr 1.11.37.120 and Easy Anvils 21.1.0 are selected at exact donor versions. Curios 9.5.1 and BaguetteLib 2.0.7 were added as required dependencies and inspected. All entries are pinned. Sophisticated Backpacks and its Create integration remain excluded because their capacity and upgrades do not fit the intended survival balance. Vanilla Backpacks 1.3.5 and Easy Shulker Boxes 21.1.3 are selected and pinned. Vanilla Backpacks uses its native NeoForge archive; Fabric API is not required on NeoForge. Easy Shulker Boxes bundles its Item Interactions dependency. EnderPack remains excluded to avoid duplicate portable ender access. Shulker Drops Two 3.7 and Reinforced Shulker Boxes 3.2.1 are selected and pinned. Shulker Drops Two retains its default shell drop chance. Reinforced Shulker Boxes is a Fabric release selected for trial through the existing Connector and Forgified Fabric API; it bundles Reinforced Core. Its interaction with Easy Shulker Boxes is untested. Sophisticated Storage has not been approved or added. No exports or runtime tests were run for this batch.

## LifeOre building selections awaiting review

LifeOre's building and decoration batch is selected at exact donor versions, including Chipped, Chipped Express, six Macaw architectural mods, Handcrafted, Beautify ReFoxed, Immersive Paintings, Straw Statues, Armor Poser, Every Compat Wood Good and Stone Zone, Supplementaries, Amendments, Big Sign Writer, Mech Trowel, Forgematica and Freecam. Reconnectible Chains and Diagonal Fences were also selected. Required libraries are pinned; embedded helper libraries remain bundled. Shuffle and Brick & Mortar are excluded. Armor Poser replaces the uninstalled Armor Statues candidate; Another Furniture is not selected alongside this furniture batch.

Axiom 5.4.2 is included as the donor's client-only Fabric release through Connector and Forgified Fabric API. Packwiz could not resolve native Fabric API for NeoForge, and no duplicate Fabric API was added. Axiom's compatibility remains untested; creative-mode usage does not establish loader compatibility. No game tests or exports have run for this batch.

## Advancement additions awaiting review

Advancement Frames 2.3.1 and Advancement Plaques 1.6.8 are selected and pinned at native NeoForge 1.21.1 releases. Frames uses the existing Moonlight 3.7.1 library; Plaques adds Iceberg 1.3.2. Released mandatory dependency declarations were inspected. Frames displays earned advancements as world decorations; Plaques changes completion notifications. Reliable Advancements 6.3.0 remains the advancement-screen provider. Better Advancements is not installed because Reliable Advancements explicitly declares it incompatible and covers its features. Plaques retains the provider client-only classification, with multiplayer sound behavior still awaiting testing. No exports or game tests ran.

## Item interaction addition awaiting review

Interactic Renewed 0.2.2 is selected and pinned at its native NeoForge 1.21.1 release, with required owo-lib 0.12.15.5-beta.1. The selected NeoForge 21.1.255 meets its minimum 21.1.248 requirement. Both archives were inspected for dependencies. Interactic is included on client and server to retain item filters, pickup interactions and throwing rather than limiting it to client-only rendering. Feature defaults are unchanged. The library is a beta release; game behavior remains untested. No exports or game tests ran.

## Everyday conveniences awaiting review

Jade, Jade Addons, Controlling, Searchables, NetherPortalFix, Carry On, TrashSlot, Reliable Advancements, Reliable EMI, Progress Peek, Detail Armor Bar Reconstructed and Status Effect Bars Reforged are selected. Stylish Effects and its required Puzzles Lib dependency are included. ToolTipFix uses the exact donor Fabric release through the existing Connector stack; it has not been tested on this client. Reliable Advancements is client-only for screen improvements, not a source of custom advancement content. The obsolete Carry On Aeronautics compatibility addon is not included. Simple Voice Chat, Chat Heads, Ding, e4mc and Map Atlases are excluded. Donor configuration and advancement-content review remain deferred until mod selection is complete.

## Travel and shared maps awaiting review

Tempad 3.0.4 (beta) and Waystones 21.1.46 are both retained at Lucas's explicit approval, with their defaults. Tempad already provides fixed destinations through Timedoor Markers and stationary teleportation through a Workstation with a docked Tempad. Location cards can be shared. Create Waystones Recipes 3.0.1.b and Waystones Sable 1.0.7 are already selected and pinned on both client and server. Their inspected dependency ranges accept the selected Create, Waystones, Balm and Sable versions. Review these existing integrations in the Create category rather than adding duplicates. The Create Tempad retexture is excluded. These integrations have not been tested in game.

Xaero’s Minimap 26.6.0 and World Map 1.47.0 are client-only. Multiplayer Plus 1.1.1 is included on both sides for shared terrain. Its required settings library is also included on both sides. Xaero’s shared library is bundled in the map archives. Map sharing, stationary portals and travel balance have not been tested; final configuration review remains pending.

## Visual additions awaiting client review

The selected visual additions include Eating Animations, Not Enough Animations, Sounds, More Sounds, Particle Effects, Continuity, Polytone, Entity Model Features, Entity Texture Features, Explosive Enhancement, and the Fresh Animations base with Objects, Player, and Quivers extensions. Continuity requires client-only Connector and Forgified Fabric support. Eating Animations and GroovyModLoader are tagged for Minecraft 1.21 by the provider, but their inspected binaries declare a range including 1.21.1. They remain untested in this pack. Sounds uses its exact required long-term-support MRU dependency. Inventory Blur is excluded.

Sodium Dynamic Lights and Create Sable Dynamic Lights are client-only selections. The native FAST mode updates moving lighting every 250 milliseconds instead of every renderer update. Visual Effects+ 1.3.1 is included with custom clouds and light rays disabled, and rain set to texture-only effects. Other effects retain their defaults. The selected Polytone release stores these options in `polytone_options.json` at the game root. Resource packs must be enabled in the client, with Fresh Animations extensions above their base pack. No shader is selected automatically.

No server or client tests have been run after these visual additions. Existing distribution archives predate this batch; export them when the selection is finished.

## Structure and enemy additions awaiting review

Dangerous 1.5.2, Creeper Overhaul 4.0.6 and Enderman Overhaul 2.0.3 are selected and pinned. Eight YUNG structure overhauls are selected: Better Mineshafts 5.1.1, Better Dungeons 5.1.4, Better Desert Temples 4.1.5, Better Jungle Temples 3.1.2, Better Witch Huts 4.1.1, Better Ocean Monuments 4.1.2, Better Nether Fortresses 3.1.5 and Better Strongholds 5.1.3, all native NeoForge 1.21.1 releases. ChoiceTheorem’s Overhauled Village 3.6.3 and Tectonic 3.0.28 are also selected. Required GeckoLib 4.9.3, YUNG shared library 5.1.9, Lithostitched 1.8.0 and Apollib 1.2.0 are pinned. Binary inspection found Apollib missing from automatic dependency resolution, so it was added explicitly. Existing Resourceful Lib 3.0.12 and Resourceful Config 3.0.11 satisfy the overhaul requirements. Selected download hashes and native declarations were inspected.

YUNG Better End Island, Extras and Bridges are excluded. Ecologics and YUNG Cave Biomes remain on hold. Aquamirae is excluded. Champions Unofficial and Enemy Expansion are research-only candidates. Other boss and terrain proposals remain uninstalled unless separately selected. Dangerous retains its defaults; the proposed disabling of day-based health scaling is not yet applied. Tectonic terrain size and structure placement tuning remain pending. No exports or game tests ran for this batch.

## Exploration locator additions awaiting review

Nature’s Compass 3.4.0 and Explorer’s Compass 3.4.0 are selected at their publisher-labelled native NeoForge 1.21.1 releases, alongside Traveler’s Titles 5.1.3. All three are pinned and their published archives inspected. Both compass archives declare a Minecraft upper bound excluding 1.21.1 despite their filenames and provider support labels. Original declarations are preserved for testing, without bypasses. Traveler’s Titles uses the existing YUNG library. No exports or game tests ran.

Spoiled is excluded at Lucas’s request. Spice of Life: Onion is the selected dietary-diversity system; Short Stacks remains the food carrying-capacity constraint. Champions Unofficial and Enemy Expansion are dropped for now. Ecologics and YUNG Cave Biomes are excluded.

## Wildlife selections awaiting testing

Spawn 4.0.8, Friends and Foes 4.0.27 and Spawn Animations 1.11.6 are selected and pinned, with Spawn's required Teal Lib 1.3.teal. All are selected on both sides. Published archive hashes and native dependency declarations were inspected. Spawn Animations also lists Fabric and Quilt dependencies in universal provider metadata; its native NeoForge archive does not require either, so neither was added. Resourceful Lib already meets Friends and Foes' requirement. No exports or game tests ran.

Naturalist is deferred from the initial selection at Lucas's approval: retain Spawn for its stronger built-in cooking and existing-pack integrations. Naturalist is not installed. Spawn's checked archive names 27 creature types, including fictional creatures; 23 are animal types when excluding Flukeshroom, Stranded, Barbed and Firekeeper. Naturalist's checked 2.0.5 archive names 47 animal types, excluding three non-animal entities. Variants are not added to either count. Ants, anglerfish, clams, crabs and snails overlap conceptually; terrain and spawn-density tuning remain untested. Spawn includes its own hamster, distinct from the excluded Adorable Hamster Pets project. Adorable Hamster Pets is excluded. Ribbits and Critters and Companions remain optional and unselected. Spawn Animations Compats 18.0 is now approved, selected and pinned; see the latest integration batch below.

## Boss and expedition selections awaiting testing

Cataclysm 3.33, Bosses'Rise 2.1.2, Illager Invasion 21.1.6 and When Dungeons Arise 2.1.68 were approved and added through packwiz, with Cataclysm's required Lionfish library 3.1. All new entries are pinned; published archive hashes, native declarations and index entries were verified. Existing Curios, GeckoLib and Puzzles Lib meet the inspected requirements; Illager Invasion bundles Extensible Enums.

When Dungeons Arise's provider lists 1.21.1, but the actual archive declares a Minecraft upper bound excluding 1.21.1. Preserve this discrepancy for final testing. No requirement bypass was applied, and this is not a proven compatible selection.

Dungeon Difficulty is excluded at Lucas's request. Variants and Ventures 1.0.28 is now selected and pinned: it adds freezing zombies, poisonous jungle zombies, poison-arrow jungle skeletons and underwater skeletons. Its archive hash, native requirements and index entry were checked; existing Resourceful Lib meets its requirement. No exports or game tests ran. Existing Dangerous, Creeper Overhaul, Enderman Overhaul and the eight YUNG structure overhauls remain selected.

Cataclysm and Bosses'Rise provide Better Combat weapon definitions in the previously inspected releases. Their class balance, boss damage restrictions, reward integration and moving-vehicle interactions remain untested. Bosses'Rise's separate roll and structure protection settings remain pending review. No settings changed, exports rebuilt or game tests ran.

L_Ender's Cataclysm Delight 1.21.1-1.0.10b is approved, added and pinned. The selected archive has a configurable food-based stat progression system, including an enableStat switch; reward overlap with Onion, class progression and brewing needs final review. Defaults remain unchanged. Modrinth reported about 1.22 million project downloads and 39,874 selected-release downloads during this review. It was the only matching project returned by the provider search, not an established cross-platform popularity ranking. Other Cataclysm integration leads exist, including a separate Better Combat compatibility pack; do not assume it is needed because the selected Cataclysm already bundles weapon definitions. No exhaustive addon claim is established.

Create cooking integrations were selected in the later shared-donor batch below. Prefer donor integrations over adding Delightful Creators by default. Verified donor membership: Slice and Dice 4.3.3 in Create Ultimate, 4.2.4 in Create Plus and LifeOre; Central Kitchen 2.6.1 in Create Ultimate and 2.5.0 in LifeOre, absent from Create Plus. Terralith and Tectonic settings remain unchanged.

## Terrain and dimension selections awaiting testing

Lucas approved Terralith with unchanged Tectonic for the Overworld, Incendium with Incendium Biomes Only for the Nether, and Nullscape for the End. Aether and its addons are deferred from the initial pack because their separate progression does not fit the selected class system. Oh The Biomes We've Gone is not selected.

Added and pinned Terralith 2.6.2, Incendium 5.4.4, Incendium Biomes Only 3.1.0 and Nullscape 1.2.14 through packwiz. Published archive hashes, native declarations, pins and refreshed index entries were verified. Existing Lithostitched 1.8.0 satisfies Terralith's minimum 1.7.7. Incendium's internal metadata still reports 5.4.3 despite publisher release 5.4.4; that satisfies Biomes Only's declared minimum 5.4.3. Biomes Only's provider side is unknown and packwiz selected both sides; its root data-pack metadata uses an older format. Keep these discrepancies for final validation rather than assuming behavior from successful packaging. The addon is intended to disable Incendium structures, custom items, mobs and bosses while retaining terrain and biomes; that behavior has not yet been tested in game. Tectonic settings remain unchanged. No exports or game tests ran.

## Latest integration approvals awaiting testing

GrandTeleport NeoForge neoforge-1.0.1 and Spawn Animations Compats 18.0 are approved, added and pinned, alongside Cataclysm Delight above. GrandTeleport's native declarations accept Minecraft 1.21.1 and require NeoForge 21.1.234 or newer, satisfied by the selected loader. This is an unofficial native port of Grand Teleport. Packwiz marked it for both sides because it did not recognize the provider's client-required and server-optional environment label; dedicated-server behavior and Tempad transitions remain untested. Spawn Animations Compats adds optional entity tags for existing Creeper Overhaul, Enderman Overhaul, Variants and Ventures and Cataclysm entities, without requiring those other mods to be installed. All three published archive hashes, pins and refreshed index entries were checked. No exports or game tests ran.

Onion clarification: the default window holds 32 food consumptions, not 32 unique foods. Duplicate items count only once at their strongest current contribution, so repeated eating displaces other food types without reducing the repeated food's normal hunger restoration. The 1.21 source exposes window size, recency decay toggle, minimum foods for benefits, food diversity overrides, reward thresholds and optional detriments. Default detriments are empty. Lucas subsequently approved a 16-event history trial. Shared config/solonion.json now sets trackCount to 16 and explicitly retains trackedFoodDiversityDecay as true. The configuration was indexed and its hash verified; no runtime test ran. All other Onion settings remain at their defaults pending final review. Dangerous also retains defaults pending review; calendar-based health growth is a concern to assess, not an approved adjustment. Boss restrictions refers to encounter damage rules, range limits and arena protection, not a separate mod. Prioritize When Dungeons Arise large-structure frequency in final placement review. Sparse Structures is a possible existing tool, but is not approved or installed; targeted native structure-set overrides may suffice. All remaining configuration and placement work is deferred until Create selection is finished.

## Create shared-donor additions awaiting testing

Lucas authorized including commonly shared Create additions, followed by a quick review of single-donor choices. Shared means present in at least two of Create Ultimate 2.0.3, Create Plus 6.0.0-alpha-f and LifeOre Season 2 0.1.1. The deduplicated current research review covers 93 Create and closely related donor projects, including computer and Sable bridges. It records 26 already selected entries after this batch, 24 recommended single-donor additions, 10 optional entries, 26 further-review entries, five excluded or recommended skips and two held space entries. Single-donor recommendations are not approval and remain uninstalled. Existing exclusions remain unchanged.

Added and pinned 22 shared addons: Slice and Dice 4.3.3, Dragons Plus 1.11.9, Enchantment Industry 2.5.4, Framed 1.8.2, Steam and Rails 0.3.0-beta.2, Big Cannons 5.11.7, Deco 2.1.3, Encased 1.9.0-ht3, Railway Navigator beta 0.9.1, Stuff and Additions 2.1.4.b, Bells and Whistles 0.4.7, Bits and Bobs 0.0.44, Central Kitchen 2.6.1, Copycats Plus 3.0.9, Design and Decor 2.2b, Escalated 1.3.2, Hypertubes 0.6.0, Integrated Farming 1.4.2, Pattern Schematics 2.0.10, Prismatic Shine 1.2.2, Shuffle Filter 2.1.1 and Vibrant Vaults 0.3.2. Prefer the newest selected donor release, retaining the current Create, Aeronautics and Sable core. Automatic dependencies Ritchie's Projectile Library 2.1.2 and DragonLib beta 3.0.28 were also pinned and inspected. Existing Architectury satisfies DragonLib; Kotlin for Forge satisfies Slice and Dice. Atmosphere and Sable Companion are bundled in Slice and Dice; Flywheel and Ponder are bundled in Create. Nested archive declarations were inspected rather than adding duplicate libraries.

All requested archives matched published hashes, native dependency declarations were inspected, and every selected mod's pin and metadata index hash was verified. Integrated Farming 1.4.2 declares optional Supplementaries integration requiring 3.9.9 or newer, but existing Supplementaries is 3.6.7. Preserve this conflict for explicit final resolution without silently updating unrelated donor selections. Big Cannons declares NeoForge 21.1.228 as a bare version; preserve it and assess actual loader behavior in final testing. Steam and Rails, Railway Navigator and DragonLib are beta releases. No exports or game tests ran.

## Approved LifeOre Create additions and integration update

Lucas approved the seven recommended LifeOre-only additions, Stam1o Tweaks, LazyTick and CreateBetterFps for trial, and The Factory Must Grow. Added exact donor releases: Additional Logistics 1.4.5, Liquid Fuel 2.1.1, More Girder 2.1.2, Oxidized 0.1.3, Blocks and Bogies 1.0.7, Trading Floor 3.0.16, Entity Model Features compatibility for Create 1.2.2, Stam1o Tweaks 1.0.8, LazyTick 2.4.9 and CreateBetterFps 1.1.4. The Factory Must Grow Community Edition 1.3.1 is the selected Create Ultimate donor variant; the original competing version was not added. Its bundled fixes make several separate patch addons redundant or incompatible, so none were added.

Supplementaries was explicitly updated from 3.6.7 to 3.9.9 to meet Integrated Farming's optional integration requirement. Its native minimum NeoForge 21.1.247 is met by 21.1.255, Moonlight's minimum 3.6.4 is met by 3.7.1, and its Sodium incompatibility range below 0.8.12-beta.1 does not include selected Sodium 0.8.13. Published hashes and native dependencies were inspected; every mod pin and refreshed index hash was verified. All selected artifacts remain exactly pinned pending the version-policy discussion. No game tests or exports ran.

Numismatics is explicitly excluded. Molten Vents 2.1.1 was subsequently approved and added at LifeOre's exact release for renewable decorative Create stones. Its archive hash, native declaration, pin and index hash were verified. Its legacy Create minimum is written as v0.5.1c; preserve that declaration for final loader validation rather than assume its ordering against Create 6.0.10. No exports or game tests ran. Other single-donor choices remain unchanged and held for Lucas's remaining instructions. Stam1o Tweaks is added without assuming it affects only recipes. Optimization behavior remains untested despite donor usage.

## Approved vehicle and physics additions awaiting testing

Added nine exact donor selections at Lucas's approval. Create Ultimate 2.0.3 supplies Aeroworks 1.5.0, AeroEngine 1.3.0, Propulsion Simulated 1.1.5, Deep Seas 2.2.4, Tweaked Controllers 1.2.7 and Springs 1.2.1. Create Plus 6.0.0-alpha-f supplies Ballast 0.1.0, Aeronautics Encased Fluid Pipes 1.0.7 and Sable Physics Compat 1.3.0. No existing mod definitions changed. Published archive hashes, native declarations, exact provider identities, pin states and index hashes were verified. The definition now contains 282 mod selections. No exports or game tests ran.

Ballast 0.1.0 declares a NeoForge upper bound excluding the selected 21.1.255. It remains an approved exact-donor trial, with the original requirement preserved and no bypass. AeroEngine is published as 1.3.0 but internally reports 1.0.2. Its narrow Create requirement accepts selected 6.0.10; its Sable range accepts selected 2.0.6. Aeronautics bundles Simulated 1.3.2, satisfying the inspected consumers, and Deep Seas bundles Sable Companion 1.5.0. Existing Create bundles Ponder. Deep Seas 2.2.4 actually contains the Abyss dimension definition and registers its Abyss component, contrary to the earlier claim that it was future content. Surface naval content is marked coming soon in its native description. Preserve the correction and review actual dimension behavior in final testing.

ComputerCraft and its Sable bridge are excluded for now because Lucas does not currently want programming-oriented automation. Pipes and Physics and Sable Ragdolls are also excluded for now at his explicit decision. Sable Beyond 0.4.1 was subsequently approved and added at Create Plus's exact alpha release, with defaults unchanged. Radars 0.4.9.4 was conditionally approved if cannons were selected: the existing Big Cannons 5.11.7 satisfies its inspected minimum 5.11.2, so Create Ultimate's exact Radars release was added. Both archives matched published hashes, native requirements were inspected, saved provider identities and index hashes were verified, and no pre-existing mod definitions changed. There are now 284 mod selections. No exports or game tests ran. Physics Compat supplies physical-property tags for supported modded blocks rather than universal coverage or functional compatibility for every machine.

Electricity review remains research only. The selected Factory Must Grow Community Edition 1.3.1 already includes electricity generators, large rotor and stator generation, motors, accumulators, cables, transformers and electrical utilities alongside fuel engines, metallurgy, chemical processing and industrial decoration. Its tagged 1.3.1 CableConnectorBlockEntity source supports external standard Forge Energy through connector input mode, translating the input to configurable network voltage. The old Converter block has been removed in Community Edition; do not recommend old Converter fixes. Crafts and Additions 1.7.1 and New Age 1.2.0 donor archives declare native dependencies fitting current Create and NeoForge. Both expose standard electrical capabilities, but actual cross-mod transfer and moving-ship operation are untested. Prefer Crafts and Additions for a smaller rotation and electricity bridge if another system is desired; New Age adds a larger generator, heat, solar and nuclear progression. Neither has been approved or added.

## Decorative and client animation additions awaiting testing

TW’s Decorative Food 1.21.1-2.0.1-neoforge and Items Displayed 2.0.10 are selected on both sides. Fancy World Animations 1.2.31 is native NeoForge and client-only. AFK Cinematics 1.21.1 and Ripple 1.2.1 are Fabric client-only selections for trial through the existing Connector and Forgified Fabric support; no duplicate Fabric library was added. All five selected archives matched published hashes and their dependency declarations were inspected. Saved exact versions, sides, pins and refreshed index hashes were verified. No pre-existing mod metadata changed. No exports or client or server tests ran.

Decorative Food supplies models for selected foods rather than universal models for every modded meal. Items Displayed contains optional integrations for Create, Spawn, Friends and Foes and Supplementaries. Fancy World Animations and moving-structure rendering require client review. The cinematic camera mod may look less smooth with Dynamic FPS idle throttling; existing performance settings are unchanged. Ripple modifies particle behavior, so compatibility with AsyncParticles remains a specific client test rather than a guarantee from general Sodium and Iris support.

Electro Energetics 1.21.1-1.1.3 was approved and added through packwiz for both client and server. Its archive matched the published hash, native requirements accept selected Create 6.0.10 and NeoForge 21.1.255, and bundled Sable Companion 1.6.0 was inspected. The exact version, pin, side and refreshed index hash were verified; no existing mod metadata changed. Defaults are unchanged. It supplies voltage and current simulation and electrified trains alongside The Factory Must Grow’s separate electrical network. Standard energy conversion and moving-ship circuits remain untested. No exports or game tests ran.

## Donor configuration transfer awaiting testing

All three donor archives were inspected: Create Ultimate 2.0.3 has no bundled configuration, Create Plus 6.0.0 Alpha f has 272 configuration files, and LifeOre Season 2 0.1.1 has 319. Their union contains 515 distinct paths. Imported settings cover 271 paths: 268 new files, one merge and two existing files preserved unchanged. Sources comprise 59 Create Plus files and 212 LifeOre files. The other 244 paths belong to absent consumers, personal state, backups, documentation, machine fingerprints or loader window settings and were not imported. Game-root recipe favourites were also omitted.

Conflicts prefer the exact selected artifact's donor, then LifeOre and Create Plus, with existing Aeropunk values taking precedence. Sodium uses the newer Create Plus schema. Fifty files had differing donor contents; source and key-level resolutions are recorded outside the distributed pack at `/home/tsb/Hermes/research/aeropunk/donor-config-transfer-audit.json`. Existing Entity Culling safety, Particular density and lifetime, BadOptimizations lightmap behavior, Polytone effects, Sodium Dynamic Lights mode and Onion history settings were preserved. The donor Windows schematic path was cleared and chunk processor counts remain automatic. Iris has no automatically selected or enabled shader.

Dynamic FPS now targets thirty frames per second when unfocused, invisible or abandoned. Its hovered target remains sixty and unlimited targets remain unlimited. This limits Dynamic FPS throttling, not the computer's actual rendering performance. Other settings use the selected release's defaults. NeoForge 1.21.1 loads server configurations from the normal configuration folder by default, so donor server-file locations were retained. Per-world overrides remain a separate consideration.

Better ModList’s native mod_menu configuration and Reliable EMI’s supported legacy EMI++ settings were identified through archive inspection and copied too. Unsupported legacy formats and stack groups for excluded mods were left out.

Applicable structured configuration syntax, all transferred file hashes and every refreshed index entry were verified. Five existing deliberate files were unchanged byte-for-byte, and mod, resource-pack and shader-pack index hashes did not change. Older donor schemas still require actual game validation. No exports or game tests ran. Historical selection notes above describe earlier checkpoints; the transfer and latest selections take precedence over their earlier statements that configuration review was deferred. Food rewards, boss behavior, Dangerous calendar scaling, structure density and electricity overlap still need balance review.

## Latest utility additions and test checkpoint

Create Connected 1.3.3 and Interiors 0.6.1 were approved and added at Create Ultimate's exact releases. Connected supplies Create machinery conveniences; Interiors supplies usable seating and furnishing blocks. Both are selected on client and server. Published archive hashes, native dependencies, saved provider identities, pin states and refreshed index hashes were verified. Connected bundles Sable Companion 1.6.0. No pre-existing mod definitions changed and no new shared settings were introduced. The current definition has 292 mod selections.

The preceding startup-only test of the 290-selection definition failed during export preparation after about 92 seconds. Short Stacks is the sole CurseForge-sourced mod, and its manifest reference was rejected by the existing fully-materialized-export check. Minecraft never launched, so no mod-loading, world, gameplay or balance result was obtained. Disposable preparation files were cleaned up. This is a packaging limitation, not evidence of a Short Stacks runtime defect. The report remains at reports/result.json. No test was rerun after these two additions because the packaging limitation remains unresolved.

Preserve the approved settings and donor baseline for initial testing. Food-reward overlap, duplicate dodge mechanics, Dangerous calendar scaling, structure density and electrical integration are playtest checkpoints, not mandatory changes before launch. Propose balance adjustments from actual behavior or a demonstrated conflict rather than tuning speculatively.

## Witcher compatibility correction

Spell Engine was downgraded from 1.10.9 to 1.10.7 while keeping Witcher 3.1.4. Published archives were checksum-verified. Witcher calls the loot configuration method with a supplier parameter; Spell Engine 1.10.8 and 1.10.9 changed that parameter to a list. Version 1.10.7 supplies the exact required signature. Native bounds and binary references from twenty-two selected combat ecosystem artifacts were inspected without finding a newly missing Spell Engine member when moving from 1.10.9 to 1.10.7. Only Spell Engine metadata changed; its exact selection, pin and refreshed index hash were verified. The subsequent native archive installation and disposable server startup test passed with this pairing. Minecraft reached readiness, accepted normal shutdown and exited with status zero; temporary files, containers and networks were cleaned. This verifies server startup, not client rendering or gameplay balance.

Version selection prioritizes the newest mutually compatible combination, not the newest individual release of every mod. Runtime verification is recorded in the latest reports.

## Previously verified baseline

The latest completed verification exercised command listing, both exports, update with pins retained, all 12 automation tests, a real server startup and normal shutdown, and cleanup. Both exports excluded operational files. The final inventory showed an empty build directory, only the latest two report files, no remaining test containers or networks, and no recreated research cache, archive, old documentation directory, or Python bytecode directories.

Client gameplay remains untested. Verification results describe this baseline, not a guarantee for future changes; rerun `just test` after server-relevant changes.

## Native export and headless test checkpoint

The export shorthand now invokes packwiz directly. Real CurseForge client and server exports completed at `dist/aeropunk-client.zip` and `dist/aeropunk-server.zip`. Each legitimately retains Short Stacks as a manifest reference. A real native Modrinth export completed at `dist/aeropunk.mrpack`, bundling `overrides/mods/shortstacks-1.2.2.jar`. All three archives passed read-only integrity checks. No archive processing or custom validation is part of the export recipes.

The Docker installer consumed a separate native Modrinth export for the disposable test. An initial installation attempt failed during secure-connection negotiation. Using the installer's documented `FETCH_USE_HTTP2` setting with value `false` allowed downloads and loader installation to complete. This is a transport setting, not a dependency or mod compatibility bypass.

The one actual Minecraft headless startup failed before readiness. NeoForge 21.1.255 on Java 21 discovered Short Stacks, then rejected Xaero's Maps Multiplayer Plus 1.1.1 because its bundled `META-INF/jarjar/zstd-jni-1.5.7-20.jar` exposes the invalid package `META-INF.versions.22.com.github.luben.zstd`. The server exited with status one. Normal shutdown on readiness was therefore not reached and cannot be claimed as verified. No mods, dependencies or balance settings were changed in response. Other previously recorded version-range concerns were not reached by this startup and remain unresolved.

The latest failure evidence is in `reports/result.json` and `reports/server.log`. Containers and the Compose network were removed, and the disposable build directory is empty. Scoped cleanup also completed without touching exports or caches. The twelve original unit tests were reversibly moved unchanged to `.archive/unit-tests`, with individual purposes and verdicts in its `REVIEW.md`; the unit recipe was removed. Useful lifecycle and filesystem checks remain in the runtime code. Two small read-only research probes exercised archive-installer configuration and failure-phase classification without launching another game.

Authoritative references checked for this change:

- https://packwiz.infra.link/tutorials/hosting/curseforge/
- https://packwiz.infra.link/tutorials/hosting/modrinth/
- https://docker-minecraft-server.readthedocs.io/en/latest/types-and-platforms/mod-platforms/modrinth-modpacks/

Installed packwiz export help offers output and CurseForge side flags, but no all-bundled option. The existing Docker helper supports a local Modrinth archive and NeoForge installation. The installed helper's help also documents the transport setting used above.

## Multiplayer map downgrade and next startup blocker

At Lucas's approval, packwiz replaced Xaero's Maps Multiplayer Plus 1.1.1 with the matching native NeoForge Minecraft 1.21.1 release 1.1.0, Modrinth version `b7pFomcM`. The existing both-side selection and exact pin were retained. A before-and-after hash comparison of 577 selection and configuration files found only this mod's metadata changed, with no added files or unrelated configuration changes. Packwiz refreshed the index, whose metadata and pack hashes were verified. All three distribution archives were regenerated and checked for the downgraded artifact.

The defect is corroborated by https://github.com/luben/zstd-jni/issues/422, reporting malformed module exports starting in compression-library 1.5.7-18. The selected 1.1.1 bundled library 1.5.7-20 failed an isolated Java 21 module-validation check; the 1.1.0 bundled library 1.5.7-9 passed it. This establishes avoidance of that defect, not overall gameplay compatibility.

A real disposable server startup after the downgrade passed the previous nested-library failure and proceeded further, but still failed before readiness. The fatal pre-loading error now identifies GrandTeleport NeoForge's selected `GrandTeleport-NeoForge-1.21.1-neoforge-1.0.1.jar` as invalid, specifically `Illegal version number specified neoforge-1.0.1`. Downloaded bytes match the recorded publisher checksum and the published native metadata contains that exact version string. No further mod changes were applied. Axiom and Reinforced Shulker Boxes also generated Fabric-loading warnings on this server; Connector is currently client-only, so these are separate side and compatibility-layer review items, not the identified fatal cause.

The tester correctly reports failure even though the server process returned zero, because the readiness condition was never reached. Normal shutdown on readiness remains unverified. Latest reports retain this attempt, and disposable containers, networks and installation files were removed. Build is empty. Future packwiz updates need deliberate pin handling, compatibility review and repeat testing rather than a calendar-based assurance of success.

## GrandTeleport downgrade and subsequent registration failure

At Lucas's request to fix the next blocker, the native NeoForge GrandTeleport selection was downgraded through packwiz to 1.0.0, version `SRYiyHAS`, retaining both-side metadata and the exact pin. The published 1.0.0 archive declares a valid `1.0.0` version, Minecraft 1.21.1 and NeoForge 21.1.234 or newer. Upstream issue https://github.com/f65q4fffs/GrandTeleport-NeoForge/issues/4 reports the exact invalid `neoforge-1.0.1` version failure in 1.0.1. Issue 8 separately reports client-class loading on a dedicated server; it is not the same failure and remains a dedicated-server compatibility concern rather than proof the downgrade fully resolves that mod's behavior.

A fresh exported-archive server test no longer encounters the GrandTeleport invalid-version error and proceeds to registration. Startup still fails before readiness. The first fatal registration trace identifies Advancement Frames 2.3.1: its advancement-frame block initialization loads client-only `ModelResourceLocation` on the dedicated server. Later registration failures include unbound entries in other mods and must be traced as possible cascades rather than assumed independent defects. No further versions, sides or balance settings were changed.

All three distribution archives were regenerated and their contents verified for GrandTeleport 1.0.0. Compared with the saved pre-downgrade inventory, only the Xaero multiplayer mod and GrandTeleport metadata changed; unrelated selections and shared settings are unchanged. Latest reports record this failed startup. Containers, networks and disposable build files were removed.

## Verified side correction and retained server-required content

Lucas authorized correcting genuinely client-only mods in the authoritative packwiz definition without further approval. Installed command help exposes no per-mod side setter, so the documented `side` field was used and packwiz refreshed the index. GrandTeleport 1.0.0 is now client-only, consistent with its server-optional role and the approved client animation use. Actual native server export omits it, client export retains it, and Modrinth export declares its server environment unsupported. All three distributions were regenerated.

Advancement Frames was deliberately not reclassified: Modrinth declares it required on both sides, and it adds physical frame blocks. A client-only declaration would remove required multiplayer content rather than fix its server bug. Upstream https://github.com/MehVahdJukaar/AdvancementFrames/issues/31 reports the exact client-only ModelResourceLocation failure on Minecraft 1.21.1 NeoForge. Published matching releases 2.3.1, 2.3.0, 2.2.10 and 2.2.9 all contain that client-model reference in the block's Type class; this inspection does not establish an earlier version as a tested remedy.

A fresh startup test confirms GrandTeleport is absent from the server installation but Advancement Frames still fails during registration with the same client-model error. This remains a failed startup, not a normal-shutdown pass. Containers, networks and disposable files were cleaned up. Resolving this remaining blocker requires a verified corrected artifact or explicit approval to exclude Advancement Frames on both sides, not an unsupported client-only relabel.

## Advancement Frames excluded with approval

Lucas approved excluding Advancement Frames because it is decorative. Its original selection is preserved at `.archive/excluded-mods/advancement-frames.pw.toml`; `packwiz remove advancement-frames --yes` removed it from the active definition and index. All three native distributions were regenerated and verified to omit it and its archived metadata.

The first test's outer command deadline interrupted observation, so its exact container diagnostics were recovered and its resources cleaned up. A second complete startup-only test reproduced a new failure: Witcher Class Mod 3.1.4 calls `LootHelper.configure`, but the selected Spell Engine 1.10.9 does not provide the expected method signature. Datapack loading aborts with `NoSuchMethodError` before readiness. No safe-mode bypass or unrelated mod changes were applied. The server process exits with code zero, but the readiness check correctly reports failure. Latest evidence is in `reports/result.json` and `reports/server.log`; disposable containers, networks and build files were verified removed.
