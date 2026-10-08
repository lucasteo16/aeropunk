# Astropunk sandbox guide: categories and presentation

## Decision

The guide is a map of available activities, not a progression system. Every category is visible from the start. Players choose an interest and receive enough information to try it, with links to existing help. Crafting costs and ordinary survival requirements remain gameplay rules, but the guide adds no locks, mandatory prerequisites, item submissions or rewards.

This document revises the presentation and category proposal in [the complete selected-mod inventory](player-guidance-plan.md). That inventory remains the coverage reference. Its technical appendix is an authoring audit, not the proposed player-facing menu.

Research only: no presentation mod has been installed, no pack settings changed, and no Minecraft tests performed.

## Proposed category map

Categories describe functions. A mod may appear under several activities without being counted as several installed mods. Categories can contain smaller pages when the activity has distinct systems.

| Main category | Smaller pages | Examples from the selected inventory and scope |
| --- | --- | --- |
| Finding things and getting help | Item searches, recipes and uses, block inspection, controls, existing demonstrations | EMI, its integrations, Jade, Controlling and Create Ponder |
| Teleportation and destinations | Placed destinations, portable travel, moving destinations, whole-vehicle dimension transfer | Waystones, Tempad and Waystones: Sable belong in the baseline overview. Whole-vehicle transfer through AeroWarptics and space integrations belongs in clearly marked deferred pages. Do not confuse teleporting a person to a moving destination with transferring the vehicle itself. |
| Vehicles and transport | Flying ships, propulsion, balancing and controls, boats and submarines, trains and stations, hypertubes, lifts and escalators | Aeronautics, Aeroworks, AeroEngine, Deep Seas, Steam 'n' Rails, Railways Navigator, Hypertubes and Escalated. A passenger route explains using transport without requiring machinery expertise. |
| Mechanical automation | Rotational power, processing, belts and logistics, filtering and storage interfaces, farms, enchanting, trading | Create and its functional addons. Each page starts from a useful operation rather than a prescribed machine tier. |
| Electricity and industry | Generation, wiring and distribution, storage and consumers, oil and fuel, powered transport | Electro Energetics, TFMG Community Edition and Liquid Fuel. Explain their systems separately before claiming interchangeable cables, energy or moving-vehicle behavior. |
| Food, farming and hunger | Hunger and saturation, dietary variety, utensils, staple recipes, Nether food, End food, underground food, boss-related ingredients, automated cooking | Farmer's Delight and its installed food addons, AppleSkin, Spice of Life Onion, Short Stacks, Central Kitchen, Slice & Dice and Integrated Farming. Teach what cooking changes, not just a catalogue of meals. |
| Storage and inventory | Backpacks, shulker boxes, bulk storage, sorting and transfer, portable access, expedition packing | Backpacks!, Reinforced Shulker Boxes, Easy Shulker Boxes, Sophisticated Inventory Interactions and Create storage. Explain capacities and controls from the selected releases. |
| Building and decoration | Material palettes, furniture, factory decoration, copycat blocks, displays, paintings and signs, schematic placement | Chipped, Handcrafted, Macaw's collection, Create decoration addons, Copycats, Immersive Paintings, Mech Trowel and Forgematica. Palette and randomized placement tools need separate pages from the decorative block catalogues. |
| Handy interactions | Carrying blocks, harvesting, sleeping, chains, anvils, recipe conflicts, item handling and disposal | Carry On, RightClickHarvest, Comforts, Reconnectible Chains, Easy Anvils, Polymorph, Mouse Tweaks and TrashSlot. Use short illustrated tips rather than long chapters. |
| Combat and character builds | Weapon handling, dodging, martial roles, magic and support, spells and runes, jewelry and relics, skill trees | Better Combat, Combat Roll and the installed role-playing systems. Link skill choices and equipment acquisition without forcing a class or completion order. |
| Adventures, structures and bosses | Villages and taverns, dungeons, overhauled vanilla structures, creature variety, boss encounters, shared loot and death recovery | YUNG's structures, When Dungeons Arise, Cataclysm, Bosses'Rise, Lootr and Corpse. A boss page can explain location, preparation and available help without requiring other guide pages first. |
| Landscapes and dimensions | Overworld landscapes and rivers, Nether, End, finding biomes and structures | Terralith, Tectonic, Streams Reflowing, Nullscape, the selected Incendium modifier and compass tools. Use actual configured dimension content, not an upstream roadmap. |
| Space, deferred | Destinations, ascent and landing, vehicle transfer, rockets where actually supplied, environmental survival | Pre-plan Northstar and its related branch additions. Clearly mark them absent from the current Chunky baseline. Do not invent a separate rocket construction system merely because the category is space. |
| Visuals and sound | Mod visuals and animations, weather and particles, resource packs, shaders, distant terrain, audio and sound controls | Keep appearance mods, resource packs and shader packs as separate subcategories. Include Distant Horizons as a player choice, not a universal enabled setting. |
| Performance and optimization | Client rendering, memory, simulation, chunk generation, optional diagnostic trials | Explain relevant player choices. Keep the extra optimizer branch deferred. Do not make players read implementation details to play. |
| Server utilities and diagnostics | Chunk pregeneration, profiling, lag investigation, administrator tools and permissions | Chunky, spark and Observable. Keep operator-only commands separate from normal player features. |
| Libraries and compatibility | Dependency catalogue, bridges and technical troubleshooting | Collapse this reference section by default. It is not an activity category and does not absorb animations, player tools or useful commands. |

Fishing remains a possible page, not a promised dedicated system. The selected inventory does not identify a dedicated fishing overhaul. Vanilla fishing and actual recipe or loot integrations can receive a small page after checking selected content. Do not add a fishing mod simply to fill a category.

## Page pattern

Each activity page should fit on a screen before optional details expand:

1. An image, item icon or small scene showing the activity.
2. One sentence explaining what the player can do.
3. A short choice between relevant installed systems, with their differences.
4. A first useful action, with ordinary materials or operating requirements where verified.
5. An item-browser query, example item and recipe or uses reference.
6. A link to existing Ponder scenes, information screens or upstream help.
7. Related activity links and a brief warning only when the activity needs one.

For cooking, separate pages should cover how hunger differs from dietary variety, cooking utensils, regional ingredients and automated meals. Explain the actual pack settings before stating bonuses. For electricity, show a small generation and consumption example rather than beginning with every available component. For transport, offer both a passenger explanation and a builder explanation.

Suggested search candidates include `@create`, `@waystones`, `@tempad` and `@farmers`. These are authoring candidates, not verified exact filters for every installed display name. The finished guide must record tested queries, because a broad mod-name fragment can match several addons. Guide text should also teach ordinary item-name searches and recipe and uses navigation.

## Presentation research

### GuideME, recommended first candidate

GuideME supports scrolling Markdown pages, full-text search, cross-links, inline recipes and interactive annotated three-dimensional scenes. Complete guides can be supplied through a resource pack rather than requiring a custom Java content mod.[1][2][6]

Its documented navigation supports nested topics and item icons. Pages can declare item identifiers so holding its guide key over a matching tooltip opens the relevant page. This makes it possible to connect the item browser to an explanation, but the actual interaction with our selected EMI screens still needs testing.[7][9]

The default guide key is G. Our existing keybindings already use G for other functions, so it is not an approved binding for this pack. A future trial must choose an unclaimed binding or avoid adding another shortcut.[7]

The client command opens a guide without carrying an item. The separate server command requires operator permissions because it can target other players. These are distinct access paths, not a reason to grant operators to ordinary players.[8]

The changelog documents a full-width layout option in its Minecraft 1.21.1 history. This addresses the small-book complaint more directly than merely changing a book texture. Actual comfort at our screen scale remains a presentation test.[15]

Proposed access is a persistent Help or Activities button in a suitable inventory or pause screen, plus optional contextual tooltip access. The documentation establishes the command and contextual shortcut, not a ready-made pack-wide persistent button. That button is a small integration task, and its placement must be checked against existing screen modifications. Do not build a replacement handbook renderer just to add a button.

Use still images and simple scenes first. Complex scenes of moving vehicles or active machines are not proven to render or simulate accurately inside the guide. Existing Ponder demonstrations remain the preferred source for dynamic mechanical teaching when available.

### Patchouli, viable but less suited to the requested layout

Patchouli has data-driven books, category entries and visual page types. Its book definition allows hiding the advancement progress bar. Our guide would omit advancement-based content locks rather than making information conditional on progress.[3]

Yes, Patchouli can be accessible from the inventory without carrying its book. The inspected Minecraft 1.21 source branch creates an inventory button for a configured registered book without checking the player inventory for that item. It replaces an existing image button in that screen rather than adding an arbitrary free-standing dashboard button.[10]

That source inspection is not an execution test of the proposed release. Screen replacement interactions with our pack need checking. More importantly, an inventory button fixes access, not the compact page-based layout Lucas dislikes. Patchouli remains a fallback for conventional recipe and multiblock pages, not the leading presentation choice.

### Modonomicon, visual overview alternative

Modonomicon offers a two-dimensional node map, data-driven documentation, images, recipes and multiblocks. This could present activities as a visual map with independent clickable topics.[4]

Its condition and unlock system is a capability, not a requirement for our design. We would use independent visible entries and avoid connecting them as mandatory progression. The map is appealing for exploration, but detailed content still opens documentation pages. It is not automatically a larger, more comfortable reference interface than GuideME.

### Guide by deaddiesel, multimedia candidate with more moving parts

The publisher advertises Markdown, themes, search, multiblock projection, images, animation and video playback. The current CurseForge listing names a Minecraft 1.21.1 NeoForge release, Guide NeoForge 1.5.1.[11]

Its guide command is advertised as item-free. Its ordinary keyboard shortcuts are inventory-aware, so a shortcut alone does not satisfy the no-carried-book requirement. The publisher describes optional recipe-viewer integration with JEI; that is not evidence of matching EMI integration.[11]

The media system includes native video libraries and caching. Those are extra packaging and platform concerns compared with static images and built-in scenes. This is a candidate if embedded videos become important, not the first choice for a lightweight guide. Project descriptions and version references are not fully consistent, so exact released features require inspection before selection.[11]

### Quest framework and external site

Feed The Beast Quests is explicitly a team-based questing system. It may be possible to use its presentation without a mandatory progression chain, but its completion-oriented model is a poorer default for this brief. It should not be installed merely to obtain a visual menu.[5]

An external searchable website is useful for phones, large images and reading outside the game. Its weakness is context switching and weaker live item and recipe integration. Keep content portable enough to publish there later, but prioritize in-game help. A custom full-screen Java interface offers complete layout freedom at a much higher maintenance cost. Reserve that for a demonstrated limitation after trying an existing presentation engine.

## Release and adoption snapshot

The public Modrinth records were checked for both Minecraft 1.21.1 and NeoForge. Downloads are provider-specific adoption signals, not performance or reliability guarantees. No artifact has been installed or compatibility-tested for this research.

| Candidate | Matching published release | Modrinth project downloads | Matching release downloads | Recommendation |
| --- | --- | --- | --- | --- |
| GuideME | 21.1.19 | 3,165,534 | 41,378 | First presentation candidate.[12][16] |
| Patchouli | 1.21.1-93-neoforge | 35,649,609 | 704,846 | Established book fallback.[13][17] |
| Modonomicon | 1.21.1-1.120.7 | 1,332,268 | 13,873 | Alternative if a visual activity map is preferred.[14][18] |
| Guide | Guide NeoForge 1.5.1 | Not supplied by this comparison | Not supplied by this comparison | CurseForge lists 48,124 project downloads. Do not combine platform totals.[11] |

Provider records list no required external projects for these three matching Modrinth releases. That is provider metadata, not a binary dependency audit. Modonomicon lists an optional additional project. The actual archives and their side requirements must be inspected before installation.[16][17][18]

## Advancements

Add a modest set of optional recognition advancements after the guide structure is settled. They should recognize natural accomplishments and point back to relevant help, not serve as the table of contents.

Useful candidate achievements include preparing a regional meal, taking a train journey, assembling or flying a vehicle, visiting a dungeon and defeating a boss. These are design examples, not implemented triggers. Vanilla criteria can cover some item, location and entity events, but reliable recognition of driving, flying or machine operation may require mod-specific events or a small integration. Do not replace meaningful accomplishments with craft-every-block tasks merely because item criteria are easier.

Every guide category remains accessible regardless of advancements. Use no reward items, recipes, currency or content unlocks. Avoid drawing parent-child relationships that suggest a required order. Ordinary recipes and survival requirements still apply independently of the guide.

Audit the actual advancements already supplied by selected mods before adding duplicates. Advancement Plaques concerns presentation, Reliable Advancements concerns reliability, and Straw Statues is a decorative display system; none establishes that this pack already contains the desired custom achievement content. Keep discovery information available before the player completes an activity.

## Proposed next step

The next implementation milestone, only after separate approval, is a small GuideME presentation trial containing teleportation, cooking and one vehicle page. Provide access without a carried item and keep all pages visible. Include an illustrated comparison, tested item-browser queries and links to existing help.

Validate navigation comfort, text size, search, access without operator permissions, keybinding conflicts, actual EMI tooltip behavior and resource reloads. This is a guide-interface trial, not a vehicle-transfer or gameplay certification. If the presentation is comfortable, expand by function using the existing complete inventory as the coverage check.

Do not build all 297 pages before the presentation is accepted. Most dependencies need no player page. The player-facing guide should explain useful actions; the installation inventory remains a separate searchable reference.

## Sources

[1] https://github.com/AppliedEnergistics/GuideME
[2] https://guideme.appliedenergistics.org
[3] https://vazkiimods.github.io/Patchouli/docs/reference/book-json
[4] https://modrinth.com/mod/modonomicon
[5] https://docs.feed-the-beast.com/mod-docs/mods/suite/Quests
[6] https://guideme.appliedenergistics.org/data-driven-guides
[7] https://guideme.appliedenergistics.org/open-guide-hotkey
[8] https://guideme.appliedenergistics.org/commands
[9] https://guideme.appliedenergistics.org/authoring
[10] https://github.com/VazkiiMods/Patchouli/blob/1.21.x/Xplat/src/main/java/vazkii/patchouli/mixin/client/MixinInventoryScreen.java
[11] https://www.curseforge.com/minecraft/mc-mods/guide
[12] https://api.modrinth.com/v2/project/guideme
[13] https://api.modrinth.com/v2/project/patchouli
[14] https://api.modrinth.com/v2/project/modonomicon
[15] https://guideme.appliedenergistics.org/changelog
[16] https://api.modrinth.com/v2/version/hFpGwC6q
[17] https://api.modrinth.com/v2/version/BIogJv2D
[18] https://api.modrinth.com/v2/version/fbS7CiY6
