# Astropunk player guidance proposal

## Recommendation

Create a discovery handbook organized around what a player wants to do. Start with a Markdown handbook that can be read on a phone or desktop. Use the existing EMI item browser, Create Ponder, mod documentation and existing information screens rather than adding a quest system or a new handbook dependency now.

The handbook should answer four questions quickly: what this mod adds, why a player might care, what to inspect first, and where to learn more. Give substantial gameplay systems short introductions. Put everyday controls in convenience tips, terrain and encounters in discovery pages, and libraries and optimizers in a technical appendix. Players should not have to study every library to understand the pack.

This document is a proposal and initial guide shortlist. No handbook has been installed in the game. No rewards, content locks, mandatory quests, new recipes or progression dependencies are proposed. Optional natural milestones can recognize a first flight, a shared railway, a varied meal or an expedition without awarding items or requiring completion before another activity.

## Source and coverage

The baseline is the selected metadata in `build/isolation-authoring`, matching the `grouped/chunky` source tree at `add68e3338132fd05d1be87764c0a9b1ed23340f`. The pack version is `0.3.0-grouped.chunky.4`, for Minecraft `1.21.1` and NeoForge `21.1.255`. All selected metadata bytes in the three requested content folders were compared with that source tree and matched.

| Inventory treatment | Baseline mods | Intended handbook treatment |
| --- | --- | --- |
| Full short introduction | 103 | Purpose, suggested first step, search, existing help and related systems |
| Convenience tip | 80 | One visible action or setting, plus a caution where useful |
| World discovery | 26 | What changes in the world and how to recognize it, without inventing crafting progression |
| Technical only | 88 | Background role, troubleshooting relevance and source |
| Total selected mods | 297 | Every metadata entry appears in one baseline inventory row |
| Resource packs | 10 | Appearance notes, separate from mod totals |
| Shader packs | 3 | Appearance and performance-choice notes, separate from mod totals |

The inventory has 310 baseline rows across those three content types. The deferred branches add five Northstar-related mods and three optimizer mods, listed separately below. They are not part of the 297-mod baseline.

Purpose summaries are conservative paraphrases of publisher project summaries. Public Modrinth project and selected-version metadata were retrieved for all 296 Modrinth-backed baseline mods, all 13 visual packs and all seven Modrinth-backed branch additions. Short Stacks and AeroWarptics use CurseForge project pages because their selected metadata names CurseForge projects. Each row links its publisher project and selected release. A linked release records selection, not a successful gameplay test.

Current project summaries may describe newer releases. Exact selected-release mechanics, configured behavior, survival availability and moving-build compatibility need separate checks before turning a suggested first step into authoritative instructions. Broad or vague summaries remain broad here rather than gaining imagined mechanics.

## Handbook shape

The landing page should offer goals such as flying a machine, supplying a factory, taking an expedition, choosing a combat role, cooking for friends and furnishing a home. Each route should remain a menu of possibilities rather than a checklist. An engineer can build transport while passengers concentrate on exploration or combat.

Keep a short start page that explains EMI, recipe viewing, mod-name searches, Ponder and the relevant control menus. Follow it with brief illustrated cards for gameplay systems and links between related cards. Give terrain and creature pages recognizable examples only after checking selected-release content. Keep the comprehensive inventory searchable, but do not put all 297 entries on the opening page.

### Finding items among thousands of entries

Use the mod-name filter in EMI rather than guessing item names. Suggested searches include `@create`, `@aeronautics`, `@farmers` and `@waystones`. These are initial search candidates, not verified exact filters for every selected addon. EMI's indexed mod display name can differ from the metadata title. A partial name can match several addons, which is useful for browsing an ecosystem but insufficient for identifying one project.

For the eventual maintained guide, record a tested search string and one verified example item identifier per gameplay entry. Open its recipe and uses views, inspect ingredient requirements, and read tooltips before building. A terrain mod, library or optimizer may have no useful item results. An empty search is not evidence that the mod is absent.

Use Create Ponder only for items that expose a Ponder prompt. Hold the bound forward key, normally `W`, over a supported item. Do not promise Ponder scenes for every Create addon, cannon, controller or aircraft block. The [official Create documentation](https://github.com/Creators-of-Create/Create/wiki/Internal---Ponder-UI) describes this interaction; scenes are assigned to particular items.

### Reuse existing help

| Existing source | Recommended use | Limitation |
| --- | --- | --- |
| Create Ponder | Mechanical relationships and supported block demonstrations | Check scene availability for each selected addon |
| Farmer's Delight advancements and [Getting Started guide](https://github.com/vectorwing/FarmersDelight/wiki/Getting-Started) | Cooking introduction without a new quest layer | Treat advancements as optional reference, not required progression |
| Spice of Life Onion Food Book | Dietary history, diversity and configured benefits | Current project documentation describes a book-screen shortcut that is unbound by default; check selected-release controls and pack settings before promising an inventory-free shortcut |
| Combat-mod tooltips, skill screens and upstream documentation | Explain roles, equipment and abilities | Wizards spell books are gameplay equipment, not automatically documentation handbooks |
| EMI and Jade | Recipes, uses, loot information and inspection of the world | Integration coverage varies by system; they do not explain every mechanic |
| Mod-provided books found in the selected releases | Link the verified book or screen instead of duplicating a whole manual | No other documentation book has been confirmed by this metadata-only audit |

The [Spice of Life Onion project documentation](https://modrinth.com/project/eHGYGKJz) describes the Food Book and its optional shortcut. These are upstream descriptions, not a check of the selected artifact or the pack's bindings.

## Goal-based routes and first guide shortlist

These are proposed reading routes, not implemented progression and not verified construction instructions. Their first actions usually start with search, inspection or documentation rather than prescribing an unverified recipe. Every gameplay inventory row is a candidate for its own short card; the following routes identify the first cards to write.

| Goal | First cards to write | Suggested first action | Links to adjacent goals |
| --- | --- | --- | --- |
| Make a useful mechanical workshop | Create, Create: Connected, Create: Additional Logistics | Search the Create catalogue, inspect a basic power component and use its Ponder scene where present | Food processing, storage and transport |
| Fly a first vehicle | Create Aeronautics, Create: Aeroworks, AeroEngine | Browse Aeronautics parts and its selected-release documentation; identify the documented assembly and control method before choosing a first design | Ballast, propulsion and expedition supplies |
| Balance and control a vehicle | Create: Ballast, Create: Tweaked Controllers, Create Propulsion: Simulated, Create: Radars | Inspect the layerable ballast block, controller descriptions and supported propulsion examples; do not assume every control or radar works on every vessel | Flight, navigation and cannons |
| Travel on water | Create Deep Seas | Browse its boat and submarine parts and check selected-release operating requirements | Expedition planning and moving-build controls |
| Move around a shared base | Steam 'n' Rails Neoforge, Create Railways Navigator, Create: Hypertubes, Create: Escalated | Inspect transport parts and available navigation interfaces before designing a route | Factory logistics and decorative stations |
| Add large mounted weapons | Create Big Cannons | Read its assembly and ammunition documentation and use available Ponder scenes before selecting a design | Combat and vehicle testing |
| Supply an industrial workshop | Create: Electro Energetics, Create: TFMG Community Edition, Create: Liquid Fuel, Create: Springs | Compare each system's documented inputs and outputs; check exact recipes before assuming electricity, fuel or moving-vessel integration is interchangeable | Aircraft engines and automation |
| Automate materials and enchanting | Create: Molten Vents, Create: Enchantment Industry, Create: Vibrant Vaults | Browse the renewable-material, enchanting and storage catalogues and inspect an achievable recipe | Workshop expansion and equipment |
| Feed an expedition | Farmer's Delight, Spice of Life Onion, Short Stacks, Backpacks! | Browse food recipes and the Food Book; inspect actual food stack sizes and backpack costs before packing | Exploration and combat readiness |
| Automate a kitchen | Create: Central Kitchen, Create Slice & Dice, Create: Integrated Farming | Compare a selected dish's manual recipe with the automated processing options actually displayed | Material logistics and farming |
| Cook regional ingredients | My Nether's Delight, End's Delight, Miner's Delight, L_Ender's Cataclysm Delight | Browse one addon's dishes, inspect ingredient sources and check its installed integrations | Regional exploration and dungeon loot |
| Pick a martial role | Better Combat, Combat Roll, Archers, Rogues & Warriors, Berserker, Forcemaster | Read role equipment and ability tooltips; inspect the combat and roll bindings rather than prescribing a key | Equipment, skills and encounter selection |
| Pick a magic or support role | Wizards, Elemental Wizards, Paladins & Priests, Bard, Witcher | Compare the upstream role descriptions and selected abilities; use a verified spell-binding guide where applicable | Runes, jewelry and party composition |
| Shape a character build | Skill Tree, More RPG Classes - Skill Tree, Armory, Arsenal, Jewelry, Relics, their selected expansions | Inspect the skill screen and acquisition information in EMI or upstream documentation | Combat roles and loot discovery |
| Plan an expedition | Xaero's Minimap, Xaero's World Map, Nature's Compass, Explorer's Compass, Comforts | Find the map bindings, mark a destination and inspect a compass recipe and portable-sleep option | Terrain discovery and transport |
| Share adventure loot and recover safely | Lootr, Corpse, Corpse x Curios API Compat | Learn chest ownership and the recovery interface before a difficult encounter | Equipment and multiplayer travel |
| Find a shared destination | Waystones, Tempad, Create Waystones Recipes | Read their destination and cost rules and inspect the actual pack recipes | Moving-build compatibility and transport balance |
| Discover landscapes | Terralith, Tectonic, Streams Reflowing, Nullscape, Incendium and Incendium Biomes Only | Read the terrain overview and explore; explain that the selected Incendium modifier removes its structures, creatures, bosses and items | Navigation and regional food |
| Find settlements and dungeons | ChoiceTheorem's Overhauled Village, Village Taverns, Gazebos, When Dungeons Arise, YUNG's structure collection | Recognize structure types while exploring; check survival navigation tools before promising a specific location | Combat roles and shared loot |
| Find challenging encounters | Bosses'Rise, L_Ender's Cataclysm, Illager Invasion, creature-variant collections | Read encounter warnings and equipment options; distinguish ordinary creature variety from boss difficulty | Food, recovery and party roles |
| Build a factory that looks intentional | Create Deco, Create: Design n' Decor, Create: Interiors, Create: Copycats+, Create: Framed | Search each decorative catalogue separately and compare material variants before designing a palette | Train stations and homes |
| Furnish homes and communal spaces | Chipped, Chipped Express, Handcrafted, Beautify: ReFoxed, Macaw's collection, Supplementaries, Amendments | Browse one material or furniture family and inspect recipes and interactions | Decorative food, paintings and displays |
| Place large builds efficiently | Mech Trowel, Forgematica, Create: Pattern Schematics, Create: Shuffle Filter | Inspect building controls and supported modes; compare palette placement with repeating schematics | Copycats and decorative catalogues |
| Reduce everyday friction | EMI, Reliable EMI, Jade, Controlling, Mouse Tweaks, Sophisticated Inventory Interactions, Polymorph | Learn mod-name searches and control search, then test sorting and recipe-choice controls with ordinary items | Every other route |

### Boundaries that the handbook must explain

Flight should be the pack's main engineering invitation, not a promise that every addon is compatible with every moving block structure. Separate assembling a vehicle, controlling it, carrying passengers, powering machines aboard it and changing dimensions. The baseline has Aeronautics-related content but no selected Northstar space-exploration project. Do not advertise planetary travel in the baseline guide.

Explain mechanics that change player expectations before adding advanced tutorials: food stack limits, dietary variety, role equipment, loot ownership, death recovery and transport costs. Do not invent exact food benefits, cooldowns, skill allocations, damage values or crafting chains from project summaries. Treat difficulty settings and transport shortcuts as playtest questions rather than applying balance changes here.

Building pages should separate decorative block catalogues, furniture interactions, placement helpers, schematics and camera tools. World-discovery pages should explain what to notice without requiring players to find every structure. Creature variants, boss encounters, terrain changes and visual spawning animations are different kinds of content.

## Delivery options

| Option | Contribution | Cost and limitation | Decision now |
| --- | --- | --- | --- |
| Markdown handbook | Searchable goal routes, source links, screenshots and a complete reference outside the game | No new game dependency; players leave the game to read it, and no automatic recipe rendering is promised | Recommended first edition |
| Existing screens and books | Immediate contextual help where a selected mod already provides it | Coverage is uneven; verify each selected-release book, screen and control | Reuse and link them |
| Patchouli handbook | A possible in-game categorized book with authored entries and recipe pages | Patchouli is not selected in the baseline; adding it requires separate approval, version checks, distribution work and usability testing | Compare later, do not install now |

The [official Patchouli getting-started documentation](https://vazkiimods.github.io/Patchouli/docs/patchouli-basics/getting-started/) describes modpack-authored external books, categories and entries. If eventually selected, avoid advancement-gated chapters and reward pages. Evaluate direct screen access and whether players must carry a book, because an inventory item should not become the price of understanding the pack. A Markdown handbook and a future in-game book should be generated from the same maintained entries rather than written as two diverging manuals.

## Maintained single-source entries

Use one entry keyed by the selected provider project identifier. Keep the authoritative mod selection in pack metadata, not a second manually maintained selection list. Join the entry to the branch's actual project and version selections when rendering a guide.

| Field | Content and maintenance rule |
| --- | --- |
| Category | One primary player goal and one treatment: full short introduction, convenience tip, world discovery or technical only |
| Purpose | A small publisher-grounded explanation, with source and a clear distinction between advertised and tested behavior |
| First step | One practical discovery action checked against the selected release; mark unverified candidates until inspected |
| Search | Tested EMI mod-name search, optional example item identifier, or an explicit note that item search does not apply |
| Existing guides | Verified Ponder scene, book, information screen, advancement reference or upstream guide; record absent or unknown help rather than inventing a book |
| Related mods | Provider identifiers for complementary selected systems, with a short reason; distinguish recipe integration from moving-build compatibility |
| Branch availability | Read from the actual branch metadata and render only available content; show deferred features separately |
| Version | Selected provider version identifier and artifact filename, pack version and source commit |
| Evidence and review | Source retrieval record, selected-release inspection status, settings dependencies and last reviewed version |

For example, a Create Aeronautics entry would use the moving-build goal, its publisher summary, a proposed first action of inspecting documented assembly controls, a candidate `@aeronautics` search, an unverified existing-guide field, and related Create, Aeroworks and Ballast identifiers. Its availability comes from branch selections; its exact release comes from metadata. No imaginary starter recipe belongs in that entry.

When selection changes, regenerate category totals and identity coverage, then flag entries whose selected versions changed. Check example items, controls, recipes, Ponder scenes and guide access in the eventual approved test environment. Keep absent branches out of baseline routes. A publication check should require every selected project to appear once in the appropriate inventory and every implemented instruction to have evidence for its selected release.

## Complete baseline mod inventory

Each selected mod appears once in the following inventory. Earlier route names are reading suggestions, not additional inventory entries. Project names preserve official titles. The release column links the selected publisher artifact; the metadata column provides the exact local identity for programmatic reconciliation. A folder separator appears only inside literal paths and links.


### Fly, drive and control moving builds

Full short introduction candidates: 9. Start with the documented assembly and control workflow, then compare addon parts. Test moving-build interactions separately.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [AeroEngine](https://modrinth.com/project/CRh10iJF) | Modular aircraft engines and an on-screen pilot display for flight control and navigation. | [1.3.0](https://modrinth.com/project/CRh10iJF/version/eqi1VZul) | `mods/aeroengine.pw.toml` |
| [Create Aeronautics](https://modrinth.com/project/oWaK0Q19) | Build anything from airships to planes and cars. | [1.3.2+mc1.21.1](https://modrinth.com/project/oWaK0Q19/version/44pLdPGg) | `mods/create-aeronautics.pw.toml` |
| [Create Aeronautics: Encased Fluid Pipes](https://modrinth.com/project/DdAlVT8M) | Encase Create Fluid Pipes with the Create Aeronautics Hot Air Envelope. | [1.0.7](https://modrinth.com/project/DdAlVT8M/version/pKFEfjEB) | `mods/create-aeronautics-encased-fluid-pipes.pw.toml` |
| [Create Deep Seas](https://modrinth.com/project/mva5q4qZ) | Submarine and boat in Create Aeronautics. | [2.2.4](https://modrinth.com/project/mva5q4qZ/version/UcXaPVeD) | `mods/create-deep-seas.pw.toml` |
| [Create Propulsion: Simulated](https://modrinth.com/project/ApkoHNO9) | Port of Create: Propulsion mod to NeoForge 1.21.1 with support of Sable and Create: Aeronautics. | [1.1.5](https://modrinth.com/project/ApkoHNO9/version/H13U56dc) | `mods/create-propulsion-simulated.pw.toml` |
| [Create: Aeroworks](https://modrinth.com/project/P26k79kP) | A collection of addons for Create Aeronautics with blocks such as the gyroscope, joystick, and more. | [1.5.0+mc1.21.1](https://modrinth.com/project/P26k79kP/version/6kk7ruR3) | `mods/create-aeroworks.pw.toml` |
| [Create: Ballast](https://modrinth.com/project/5ypXYrfG) | Adds a new layerable block that has more mass with each added layer. Useful for balancing your aeronautics builds. | [0.1.0](https://modrinth.com/project/5ypXYrfG/version/uJwkM1Xh) | `mods/create-ballast.pw.toml` |
| [Create: Radars](https://modrinth.com/project/BLu2Yqfq) | Adding Radars (and more) to Create. | [0.4.9.4-1.21.1](https://modrinth.com/project/BLu2Yqfq/version/AntNFNAx) | `mods/create-radars.pw.toml` |
| [Create: Tweaked Controllers](https://modrinth.com/project/H6bJ8Ju4) | An addon for the Create Minecraft mod that adds a way of controlling contraptions using an advanced controller. | [1.21.1-1.2.7](https://modrinth.com/project/H6bJ8Ju4/version/csCe2v7f) | `mods/create-tweaked-controllers.pw.toml` |

### Power machines and automate materials

Full short introduction candidates: 14. Start with item searches and recipe inspection. Use Ponder where supported; keep electricity and industrial systems distinct until their interfaces are verified.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Create](https://modrinth.com/project/LNytGWDc) | Mechanical automation and moving contraptions built from cooperating components. | [6.0.10+mc1.21.1](https://modrinth.com/project/LNytGWDc/version/UjX6dr61) | `mods/create.pw.toml` |
| [Create Stuff 'N Additions](https://modrinth.com/project/aq9qUUQG) | Additional Create technology. The summary does not specify the individual tools. | [2.1.4.b](https://modrinth.com/project/aq9qUUQG/version/gMWQ1LX9) | `mods/create-stuff-additions.pw.toml` |
| [Create: Additional Logistics](https://modrinth.com/project/CZaz7aje) | Adds a few new logistics-oriented blocks to Create, and tweaks a few behaviors. | [1.4.5](https://modrinth.com/project/CZaz7aje/version/soesZiME) | `mods/create-additional-logistics.pw.toml` |
| [Create: Connected](https://modrinth.com/project/Vg5TIO6d) | Additional convenience blocks for Create, with configurable feature availability. | [1.3.3-mc1.21.1](https://modrinth.com/project/Vg5TIO6d/version/Xe7EqzfQ) | `mods/create-connected.pw.toml` |
| [Create: Dragons Plus](https://modrinth.com/project/dzb1a5WV) | Player conveniences and development utilities for Create addons. Separate visible features from background support during handbook authoring. | [1.11.9](https://modrinth.com/project/dzb1a5WV/version/b0u9vk8C) | `mods/create-dragons-plus.pw.toml` |
| [Create: Electro Energetics](https://modrinth.com/project/qYJdIoAx) | Electricity generation, transmission and use for Create, including electric trains. | [1.21.1-1.1.3](https://modrinth.com/project/qYJdIoAx/version/KWxEmmON) | `mods/create-electro-energetics.pw.toml` |
| [Create: Enchantment Industry](https://modrinth.com/project/JWGBpFUP) | Automatic Enchanting, with Create. | [2.5.4](https://modrinth.com/project/JWGBpFUP/version/WJ2VPWAG) | `mods/create-enchantment-industry.pw.toml` |
| [Create: Integrated Farming](https://modrinth.com/project/9k1pAsfR) | Integrated farming automation for Create. | [1.4.2](https://modrinth.com/project/9k1pAsfR/version/90PTskVE) | `mods/create-integrated-farming.pw.toml` |
| [Create: Liquid Fuel](https://modrinth.com/project/sH9tXU9f) | Pump in liquid fuel to blaze burners. | [2.1.1-1.21.1](https://modrinth.com/project/sH9tXU9f/version/7oNrI3y9) | `mods/create-liquid-fuel.pw.toml` |
| [Create: Molten Vents](https://modrinth.com/project/uuVy6k1s) | Adds a renewable source of the orestones found in the Create mod, and by extension, many resources. | [2.1.1](https://modrinth.com/project/uuVy6k1s/version/By33YVeb) | `mods/create-molten-vents.pw.toml` |
| [Create: Springs](https://modrinth.com/project/wDCqub60) | Store rotational force using springs. | [1.2.1-neoforge](https://modrinth.com/project/wDCqub60/version/3tMl04vO) | `mods/create-springs.pw.toml` |
| [Create: TFMG Community Edition](https://modrinth.com/project/hC1xYvnS) | A community fork of Create: TFMG focused on bug fixes. Detailed industrial mechanics need selected-release documentation. | [1.3.1](https://modrinth.com/project/hC1xYvnS/version/LNfoHEO4) | `mods/tfmg-community-edition.pw.toml` |
| [Create: Trading floor](https://modrinth.com/project/WROfLLvn) | Automate trading with villagers using create. | [3.0.16](https://modrinth.com/project/WROfLLvn/version/K3nIvcWT) | `mods/create-trading-floor.pw.toml` |
| [Create: Vibrant Vaults](https://modrinth.com/project/hddN8ksR) | A Create mod addon that adds more item vaults. | [0.3.2](https://modrinth.com/project/hddN8ksR/version/t17qYXjn) | `mods/create-vibrant-vaults.pw.toml` |

### Build transport networks

Full short introduction candidates: 8. Start with transport parts, route displays or destination rules. Large cannons get an assembly introduction rather than a generic train tutorial.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Create Big Cannons](https://modrinth.com/project/GWp4jCJj) | A Minecraft mod for building large cannons with the Create mod. | [5.11.7](https://modrinth.com/project/GWp4jCJj/version/bOiDu0LS) | `mods/create-big-cannons.pw.toml` |
| [Create Railways Navigator](https://modrinth.com/project/Dq3STxps) | Train-route navigation, improved display boards and additional schedule entries. | [1.21.1-beta-0.9.1-C6](https://modrinth.com/project/Dq3STxps/version/hjpv7klQ) | `mods/create-railways-navigator.pw.toml` |
| [Create: Blocks & Bogies](https://modrinth.com/project/j4ARnQwY) | Larger train bogies, including variants with valve gear. | [1.0.7-1.21.1](https://modrinth.com/project/j4ARnQwY/version/rUu97B0K) | `mods/blocks-bogies.pw.toml` |
| [Create: Escalated](https://modrinth.com/project/LyOBYG8Q) | A mod to add functional, aesthetic, and rotation-powered escalators to Create. | [1.3.2](https://modrinth.com/project/LyOBYG8Q/version/vJ49zRJl) | `mods/escalated.pw.toml` |
| [Create: Hypertubes](https://modrinth.com/project/ATDdrG1y) | Tube-based player transport. | [0.6.0](https://modrinth.com/project/ATDdrG1y/version/qYjOyvgW) | `mods/hypertube.pw.toml` |
| [Steam 'n' Rails Neoforge](https://modrinth.com/project/L3Jv0QZI) | An unofficial Steam 'n' Rails port for Minecraft 1.21.1. Selected-release train features need documentation review. | [0.3.0-beta.2+neoforge-mc1.21.1](https://modrinth.com/project/L3Jv0QZI/version/czVeSmZo) | `mods/create-steam-n-rails-1.21.1.pw.toml` |
| [Tempad](https://modrinth.com/project/gKNwt7xu) | Portable portal travel. Exact destination, cost and moving-build behavior need selected-release checks. | [3.0.4](https://modrinth.com/project/gKNwt7xu/version/T26aJH7E) | `mods/tempad.pw.toml` |
| [Waystones](https://modrinth.com/project/LOpKHB2A) | Teleport from waystone to waystone or craft magical scrolls to warp. | [21.1.46+neoforge-1.21.1](https://modrinth.com/project/LOpKHB2A/version/6Z6MQ6os) | `mods/waystones.pw.toml` |

### Build factories, homes and scenery

Full short introduction candidates: 39. Start by browsing a small palette or interaction, then distinguish decoration from placement, schematic and camera tools.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Amendments](https://modrinth.com/project/6iTJugQR) | Changes and additions to vanilla block interactions. | [1.21-2.0.15-neoforge](https://modrinth.com/project/6iTJugQR/version/8xf6Wpxs) | `mods/amendments.pw.toml` |
| [Armor Poser](https://modrinth.com/project/PFwYNrHb) | An armor-stand pose and property editor. | [6.2.3](https://modrinth.com/project/PFwYNrHb/version/a0U02pcz) | `mods/armor-poser.pw.toml` |
| [Beautify: ReFoxed](https://modrinth.com/project/ZQCyyWBM) | Vanilla-styled decorative additions. | [1.9.0](https://modrinth.com/project/ZQCyyWBM/version/fkkocn59) | `mods/beautify-refoxed.pw.toml` |
| [Big Sign Writer](https://modrinth.com/project/UCpxwAAu) | Easily write large, multi-line characters and symbols on signs. | [2.2.0+1.21.1-neoforge](https://modrinth.com/project/UCpxwAAu/version/tDRzCOIC) | `mods/bigsignwriter.pw.toml` |
| [Chipped](https://modrinth.com/project/BAscRYKm) | Decorative block variants. The short project summary does not explain individual workstations. | [4.0.2](https://modrinth.com/project/BAscRYKm/version/eqVowbGc) | `mods/chipped.pw.toml` |
| [Chipped Express](https://modrinth.com/project/dQIcJONI) | Stonecutter access to Chipped recipes. | [1.3.2-21](https://modrinth.com/project/dQIcJONI/version/NPqP9QZO) | `mods/chipped-express.pw.toml` |
| [Create Deco](https://modrinth.com/project/sMvUb4Rb) | Industrial decoration themed around the aesthetics of the Create mod. | [2.1.3](https://modrinth.com/project/sMvUb4Rb/version/qrcMVoBD) | `mods/create-deco.pw.toml` |
| [Create Encased](https://modrinth.com/project/hSSqdyU1) | Allow to use all casing on shafts and cogwheels and pipes. | [1.21.1-1.9.0-ht3](https://modrinth.com/project/hSSqdyU1/version/t6MATlU9) | `mods/create-encased.pw.toml` |
| [Create: Bells & Whistles](https://modrinth.com/project/gJ5afkVv) | Decorative additions for Create builds. | [v0.4.7-1.21.1](https://modrinth.com/project/gJ5afkVv/version/w0mifib8) | `mods/bellsandwhistles.pw.toml` |
| [Create: Bits 'n' Bobs](https://modrinth.com/project/T8bvmqVZ) | Decorative and mechanical Create additions. | [0.0.44](https://modrinth.com/project/T8bvmqVZ/version/XKDQlGJW) | `mods/create-bits-n-bobs.pw.toml` |
| [Create: Copycats+](https://modrinth.com/project/UT2M39wf) | Additional copycat building blocks. Check selected recipes and tooltips for supported shapes. | [3.0.9+mc.1.21.1-neoforge](https://modrinth.com/project/UT2M39wf/version/bPYeUWZx) | `mods/copycats.pw.toml` |
| [Create: Design n' Decor](https://modrinth.com/project/x49wilh8) | Decorative blocks for Create factories. | [2.2b](https://modrinth.com/project/x49wilh8/version/uQsIRky8) | `mods/create-design-n-decor.pw.toml` |
| [Create: Framed](https://modrinth.com/project/15fFZ3f4) | Additional framed-glass variants. | [1.8.2+1.21.1](https://modrinth.com/project/15fFZ3f4/version/yioQUGiO) | `mods/create-framed.pw.toml` |
| [Create: Interiors](https://modrinth.com/project/r4Knci2k) | Additional furniture for Create. | [0.6.1](https://modrinth.com/project/r4Knci2k/version/gBrfZy6S) | `mods/interiors.pw.toml` |
| [Create: More Girder](https://modrinth.com/project/sPg2LVAd) | Eight additional girder variants. | [2.1.2](https://modrinth.com/project/sPg2LVAd/version/LG0UGk5r) | `mods/create-more-girder.pw.toml` |
| [Create: Oxidized](https://modrinth.com/project/X9kjRZeX) | Oxidizing recipes for copper blocks. | [0.1.3](https://modrinth.com/project/X9kjRZeX/version/z8PFRVBs) | `mods/create_oxidized.pw.toml` |
| [Create: Pattern Schematics](https://modrinth.com/project/cpqKG67r) | Build with repeating schematics. | [2.0.10](https://modrinth.com/project/cpqKG67r/version/VSJhIkG2) | `mods/create-pattern-schematics.pw.toml` |
| [Create: Prismatic Shine](https://modrinth.com/project/udEtt0b2) | Glass and illuminated Create casings. | [1.2.2](https://modrinth.com/project/udEtt0b2/version/gKqw2akx) | `mods/create-prismatic-shine.pw.toml` |
| [Create: Shuffle Filter](https://modrinth.com/project/gv5RRavC) | Random block placement through a filter used in moving Create deployers. | [2.1.1](https://modrinth.com/project/gv5RRavC/version/5DJFXpjO) | `mods/create-shuffle-filter.pw.toml` |
| [Diagonal Fences](https://modrinth.com/project/IKARgflD) | Diagonal connections for fences. | [v21.1.1-1.21.1-NeoForge](https://modrinth.com/project/IKARgflD/version/bgR1e0O5) | `mods/diagonal-fences.pw.toml` |
| [Every Compat (Stone Zone)](https://modrinth.com/project/uYwn8IP5) | Stone-type compatibility across supported building mods. | [1.21-2.11.16-neoforge](https://modrinth.com/project/uYwn8IP5/version/5yz4JuMs) | `mods/stone-zone.pw.toml` |
| [Every Compat (Wood Good)](https://modrinth.com/project/eiktJyw1) | Wood-type compatibility across supported building mods. Listed upstream integrations are not all selected in this pack. | [1.21-2.11.46](https://modrinth.com/project/eiktJyw1/version/nyFPhGH6) | `mods/every-compat.pw.toml` |
| [Forgematica](https://modrinth.com/project/dCKRaeBC) | A client-side schematic tool, ported from Litematica. | [0.4.2+mc1.21.1](https://modrinth.com/project/dCKRaeBC/version/71jxaAwz) | `mods/forgematica.pw.toml` |
| [Freecam](https://modrinth.com/project/XeEZ3fK2) | Configurable detached-camera viewing. | [1.3.0+mc1.21.1](https://modrinth.com/project/XeEZ3fK2/version/ROfcbxxe) | `mods/freecam.pw.toml` |
| [Handcrafted](https://modrinth.com/project/pJmCFF0p) | Home decoration. The short project summary does not describe individual furniture functions. | [4.0.3](https://modrinth.com/project/pJmCFF0p/version/JfqnpP2Z) | `mods/handcrafted.pw.toml` |
| [Immersive Paintings](https://modrinth.com/project/6txNkua3) | Importable paintings that can be pixelated and displayed, including on servers. | [0.7.8+1.21.1](https://modrinth.com/project/6txNkua3/version/DeOfrXC3) | `mods/immersive-paintings.pw.toml` |
| [Items Displayed [NeoForge]](https://modrinth.com/project/PuR4vDBo) | Display items in the world instead of leaving them in containers. | [2.0.10](https://modrinth.com/project/PuR4vDBo/version/8ZZWElcA) | `mods/items-displayed-forge.pw.toml` |
| [Macaw's Bridges](https://modrinth.com/project/GURcjz8O) | A simple mod that adds a lot of bridges. | [3.1.2](https://modrinth.com/project/GURcjz8O/version/aQ7rY7ng) | `mods/macaws-bridges.pw.toml` |
| [Macaw's Doors](https://modrinth.com/project/kNxa8z3e) | Additional vanilla-style and themed door designs. | [1.1.5](https://modrinth.com/project/kNxa8z3e/version/u7BRX44F) | `mods/macaws-doors.pw.toml` |
| [Macaw's Fences and Walls](https://modrinth.com/project/GmwLse2I) | Adds new vanilla styled fences, walls and gates. | [1.2.1](https://modrinth.com/project/GmwLse2I/version/jVdb0r4W) | `mods/macaws-fences-and-walls.pw.toml` |
| [Macaw's Roofs](https://modrinth.com/project/B8jaH3P1) | Dedicated roof building pieces. | [2.3.2](https://modrinth.com/project/B8jaH3P1/version/jiXRXiSt) | `mods/macaws-roofs.pw.toml` |
| [Macaw's Stairs](https://modrinth.com/project/iP3wH1ha) | Adds new Vanilla styled Stairs, Handrails for Stairs and Balconies. | [1.0.2](https://modrinth.com/project/iP3wH1ha/version/4t8L0dGP) | `mods/macaws-stairs.pw.toml` |
| [Macaw's Windows](https://modrinth.com/project/C7I0BCni) | Windows, glass designs, blinds, shutters and curtains. | [2.4.2](https://modrinth.com/project/C7I0BCni/version/rQUE4LCz) | `mods/macaws-windows.pw.toml` |
| [Mech Trowel](https://modrinth.com/project/nqFNRALS) | Palette-based random block placement and building-wand functionality, including Create and Copycats support. | [1.3.2.1](https://modrinth.com/project/nqFNRALS/version/nCXGFcYp) | `mods/mech-trowel.pw.toml` |
| [Reconnectible Chains](https://modrinth.com/project/5pzBXDS3) | Decorative chains connecting fences and walls. | [2.2.5-1.21.1-neoforge](https://modrinth.com/project/5pzBXDS3/version/kxlFAdAZ) | `mods/reconnectible-chains.pw.toml` |
| [Straw Statues](https://modrinth.com/project/2fltysAl) | Player-shaped decorative statues. | [v21.1.0-1.21.1-NeoForge](https://modrinth.com/project/2fltysAl/version/C7j9WWVp) | `mods/straw-statues.pw.toml` |
| [Supplementaries](https://modrinth.com/project/fFEIiSDQ) | Decorative and functional vanilla-style additions, including jars, signposts, faucets, planters and lights. | [1.21.1-3.9.9](https://modrinth.com/project/fFEIiSDQ/version/WrZWfRjP) | `mods/supplementaries.pw.toml` |
| [TorchMaster](https://modrinth.com/project/Tl8ESrhX) | Control Mob Spawning with simple to use Blocks like the Mega Torch or the Dread Lamp. | [21.1.9-release](https://modrinth.com/project/Tl8ESrhX/version/PhWXajPC) | `mods/torchmaster.pw.toml` |
| [TW‘s  Decorative Food](https://modrinth.com/project/656seq5J) | Placeable food for decoration. | [1.21.1-2.0.1-neoforge](https://modrinth.com/project/656seq5J/version/WktBUUVN) | `mods/decorative-food.pw.toml` |

### Choose combat roles and equipment

Full short introduction candidates: 24. Start with equipment and ability tooltips, the appropriate skill screen and selected-release acquisition information.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Additional Jewelry (RPG Series Plus)](https://modrinth.com/project/rULzJh3O) | Additional jewelry for More RPG Classes. | [2.3.1+1.21.1-neoforge](https://modrinth.com/project/rULzJh3O/version/FtXm9snY) | `mods/additional-rpg-jewelry.pw.toml` |
| [Archers (RPG Series)](https://modrinth.com/project/QgooUXAJ) | Archery-focused combat content. | [3.1.3+1.21.1-neoforge](https://modrinth.com/project/QgooUXAJ/version/7oSRQwU0) | `mods/archers.pw.toml` |
| [Archers Expansion (RPG Series Plus)](https://modrinth.com/project/1BHIIm4m) | Additional content for Archers, built on Spell Engine. | [2.1.1+1.21.1-neoforge](https://modrinth.com/project/1BHIIm4m/version/nOK3xplJ) | `mods/archers-expansion.pw.toml` |
| [Armory (RPG Series)](https://modrinth.com/project/PJvJUdGw) | Armor sets with individual designs and set bonuses. | [1.5.2+1.21.1-neoforge](https://modrinth.com/project/PJvJUdGw/version/51cccxUm) | `mods/armory-rpg-series.pw.toml` |
| [Arsenal (RPG Series)](https://modrinth.com/project/LiP9Q3KV) | Legendary weapons described as rewards to conquer rather than craft. | [1.5.0+1.21.1-neoforge](https://modrinth.com/project/LiP9Q3KV/version/rYyhslig) | `mods/arsenal-rpg-series.pw.toml` |
| [Bard (RPG Series Plus)](https://modrinth.com/project/kL7Bjgmw) | Party-support songs and ballads, built on Spell Engine. | [1.1.1-1.21.1-neoforge](https://modrinth.com/project/kL7Bjgmw/version/K2t0CqfR) | `mods/bard-more-rpg-classes.pw.toml` |
| [Berserker (RPG Series Plus)](https://modrinth.com/project/8hqOZzxM) | Berserker combat content built on Spell Engine. | [3.1.1+1.21.1-neoforge](https://modrinth.com/project/8hqOZzxM/version/Z169ob2G) | `mods/berserker-rpg-class.pw.toml` |
| [Better Combat](https://modrinth.com/project/5sy6g3kz) | Melee combat inspired by Minecraft Dungeons. | [2.4.0+1.21.1-neoforge](https://modrinth.com/project/5sy6g3kz/version/VhIOvcXP) | `mods/better-combat.pw.toml` |
| [Combat Roll](https://modrinth.com/project/wGKYL7st) | A combat roll ability with related attributes and enchantments. | [2.0.6+1.21.1-neoforge](https://modrinth.com/project/wGKYL7st/version/FT7t1n1a) | `mods/combat-roll.pw.toml` |
| [Critical Strike](https://modrinth.com/project/ilvNBzFn) | Chance-based critical hits for melee and ranged attacks. | [1.0.4+1.21.1-neoforge](https://modrinth.com/project/ilvNBzFn/version/2LZ76MSH) | `mods/critical-strike.pw.toml` |
| [Dangerous - Just A Difficulty Mod](https://modrinth.com/project/nsri5wVW) | Difficulty balancing intended for packs with powerful player abilities or extra health. | [1.5.2](https://modrinth.com/project/nsri5wVW/version/ItIXjtt2) | `mods/dangerous.pw.toml` |
| [Elemental Wizards (RPG Series Plus)](https://modrinth.com/project/PeZ4h4i0) | Elemental magic combat content built on Spell Engine. | [3.1.1+1.21.1-neoforge](https://modrinth.com/project/PeZ4h4i0/version/lZy9JjDR) | `mods/elemental-wizards-rpg.pw.toml` |
| [Forcemaster (RPG Series Plus)](https://modrinth.com/project/K3yHebFL) | Knuckle weapons and martial combat content built on Spell Engine. | [3.1.1+1.21.1-neoforge](https://modrinth.com/project/K3yHebFL/version/2yMJPJK9) | `mods/forcemaster-rpg-class.pw.toml` |
| [Jewelry (RPG Series)](https://modrinth.com/project/sNJAIjUm) | Gems found underground and crafted into jewelry. | [2.5.1+1.21.1-neoforge](https://modrinth.com/project/sNJAIjUm/version/iLTExB6G) | `mods/jewelry.pw.toml` |
| [More Relics (RPG Series Plus)](https://modrinth.com/project/IZ3b4kEa) | Additional relics for the More RPG Classes series. | [1.3.1+1.21.1-neoforge](https://modrinth.com/project/IZ3b4kEa/version/eYDetZyP) | `mods/more-relics-rpg.pw.toml` |
| [More RPG Classes - Skill Tree (RPG Series Plus)](https://modrinth.com/project/3OYmNUDq) | Skill-tree additions for the More RPG Classes series. | [1.2.0+1.21.1-neoforge](https://modrinth.com/project/3OYmNUDq/version/zW9lGhaT) | `mods/more-rpg-classes-skill-tree.pw.toml` |
| [Paladins & Priests (RPG Series)](https://modrinth.com/project/FxXkHaLe) | Protective and healing combat roles. | [3.1.3+1.21.1-neoforge](https://modrinth.com/project/FxXkHaLe/version/7oCw7txX) | `mods/paladins-and-priests.pw.toml` |
| [Pufferfish's Skills](https://modrinth.com/project/hqQqvaa4) | A configurable skill system. The summary does not establish which pack-specific skills are enabled. | [0.19.1](https://modrinth.com/project/hqQqvaa4/version/uqAz8XFU) | `mods/skills.pw.toml` |
| [Relics (RPG Series)](https://modrinth.com/project/BDQucwF0) | Equipment trinkets for combat builds. | [1.4.0+1.21.1-neoforge](https://modrinth.com/project/BDQucwF0/version/O6zfkTwx) | `mods/relics-rpg.pw.toml` |
| [Rogues & Warriors (RPG Series)](https://modrinth.com/project/3MKqoGuP) | Rogue and warrior martial combat content. | [3.1.3+1.21.1-neoforge](https://modrinth.com/project/3MKqoGuP/version/WxwS7HDW) | `mods/rogues-and-warriors.pw.toml` |
| [Runes](https://modrinth.com/project/lP9Yrr1E) | Craftable ammunition for spells. | [1.3.2+1.21.1-neoforge](https://modrinth.com/project/lP9Yrr1E/version/Br4oP4M6) | `mods/runes.pw.toml` |
| [Skill Tree (RPG Series)](https://modrinth.com/project/PjDhruSC) | Skills for shaping a combat class. | [1.6.1+1.21.1-neoforge](https://modrinth.com/project/PjDhruSC/version/Vr94BeiF) | `mods/skill-tree.pw.toml` |
| [Witcher (RPG Series Plus)](https://modrinth.com/project/4eW1c7Gj) | Witcher-themed monster-fighting content built on Spell Engine. | [3.1.4+1.21.1-neoforge](https://modrinth.com/project/4eW1c7Gj/version/QF76fKlN) | `mods/witcher-rpg-class.pw.toml` |
| [Wizards (RPG Series)](https://modrinth.com/project/NkGaQMDA) | Arcane, fire and frost magic combat content. | [3.1.3+1.21.1-neoforge](https://modrinth.com/project/NkGaQMDA/version/lxbf57N2) | `mods/wizards.pw.toml` |

### Grow food, cook and supply expeditions

Full short introduction candidates: 9. Start with a dish recipe, ingredient source and the current dietary information. Automation is an optional next route.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Create Slice & Dice](https://modrinth.com/project/GmjmRQ0A) | Create-based automation support for Farmer's Delight. | [4.3.3](https://modrinth.com/project/GmjmRQ0A/version/N67LJgrN) | `mods/slice-and-dice.pw.toml` |
| [Create: Central Kitchen](https://modrinth.com/project/btq68HMO) | Create-based automation for food processing from supported cooking mods. | [2.6.1](https://modrinth.com/project/btq68HMO/version/FaEwZ1Pr) | `mods/create-central-kitchen.pw.toml` |
| [End's Delight](https://modrinth.com/project/yHN0njMr) | End's Delight is an addon mod for Farmer's Delight based around adding culinary content to the end. | [2.6+neoforge.1.21.1](https://modrinth.com/project/yHN0njMr/version/La8SvoPm) | `mods/ends-delight.pw.toml` |
| [Farmer's Delight](https://modrinth.com/project/R2OftAxM) | Farming and cooking expansion. | [1.21.1-1.3.2](https://modrinth.com/project/R2OftAxM/version/GbNuOZ4S) | `mods/farmers-delight.pw.toml` |
| [L_Ender 's Cataclysm Delight](https://modrinth.com/project/a48R8AGk) | Additional dishes connecting L_Ender's Cataclysm with Farmer's Delight. | [1.21.1-1.0.10b](https://modrinth.com/project/a48R8AGk/version/cl5zVy2S) | `mods/l_enders-cataclysm-delight.pw.toml` |
| [Miner's Delight](https://modrinth.com/project/qMxbM4BQ) | Farmer's Delight add-on for miners. | [1.4.5](https://modrinth.com/project/qMxbM4BQ/version/YUHbwbgQ) | `mods/miners-delight.pw.toml` |
| [My Nether's Delight](https://modrinth.com/project/O53VhQoZ) | New Nether addon for Farmer's Delight. | [1.10.2](https://modrinth.com/project/O53VhQoZ/version/qBUSJw5Z) | `mods/my-nethers-delight.pw.toml` |
| [Short Stacks](https://www.curseforge.com/minecraft/mc-mods/short-stacks) | Reduces food stack sizes according to how filling each food is, including modded food. | [shortstacks-1.2.2.jar](https://www.curseforge.com/minecraft/mc-mods/short-stacks/files/6974172) | `mods/short-stacks.pw.toml` |
| [Spice of Life Onion](https://modrinth.com/project/eHGYGKJz) | Encourages dietary variety. The project's Food Book describes food history, diversity and configured benefits. | [1.5.6](https://modrinth.com/project/eHGYGKJz/version/4YRKCovn) | `mods/spice-of-life-onion.pw.toml` |

### Find landscapes, settlements and encounters

World discovery candidates: 26. Explain what players can recognize while exploring. Terrain, structures, ordinary creatures and bosses deserve different descriptions.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Bosses'Rise](https://modrinth.com/project/q2bV1Tm1) | Souls-like boss encounters. | [2.1.2](https://modrinth.com/project/q2bV1Tm1/version/lE9PF6Wp) | `mods/bossesrise.pw.toml` |
| [ChoiceTheorem's Overhauled Village](https://modrinth.com/project/fgmhI8kH) | Changed and additional villages and pillager outposts. | [3.6.3](https://modrinth.com/project/fgmhI8kH/version/ztzRUnQ7) | `mods/ct-overhaul-village.pw.toml` |
| [Creeper Overhaul](https://modrinth.com/project/MI1LWe93) | A mod which overhauls the vanilla creepers. | [4.0.6](https://modrinth.com/project/MI1LWe93/version/HNrAYCLH) | `mods/creeper-overhaul.pw.toml` |
| [Enderman Overhaul](https://modrinth.com/project/Lq6ojcWv) | Enderman Overhaul adds over 20 new enderman variants, each with their own sounds, models, and animations. | [2.0.3](https://modrinth.com/project/Lq6ojcWv/version/TH9YXp9r) | `mods/enderman-overhaul.pw.toml` |
| [Friends&Foes (Forge/NeoForge)](https://modrinth.com/project/BOCJKD49) | Outvoted and forgotten mob-vote creatures with expanded vanilla-like features. | [neoforge-4.0.27+mc1.21.1](https://modrinth.com/project/BOCJKD49/version/zeGwtTNo) | `mods/friends-and-foes-forge.pw.toml` |
| [Gazebos (RPG Series)](https://modrinth.com/project/XIpMGI6r) | Village structures containing small spell libraries. | [2.2.0+1.21.1-neoforge](https://modrinth.com/project/XIpMGI6r/version/ktRCCPX3) | `mods/gazebos.pw.toml` |
| [Illager Invasion](https://modrinth.com/project/jSV9w0J5) | Additional illager enemies, ported from Illager Expansion. | [v21.1.6-1.21.1-NeoForge](https://modrinth.com/project/jSV9w0J5/version/9bEpNrvK) | `mods/illager-invasion.pw.toml` |
| [Incendium Biomes Only](https://modrinth.com/project/gmUU3UdW) | Removes Incendium structures, items, creatures and bosses, retaining its terrain and biomes. | [v3.1.0-neoforge-1.21](https://modrinth.com/project/gmUU3UdW/version/ZQz8SbYS) | `mods/ibo.pw.toml` |
| [Incendium Legacy](https://modrinth.com/project/ZVzW5oNS) | Nether terrain and biome overhaul with upstream structure, equipment and creature content. The selected Incendium Biomes Only modifier removes those content groups. | [5.4.4](https://modrinth.com/project/ZVzW5oNS/version/7mVvV9Th) | `mods/incendium.pw.toml` |
| [L_Ender's Cataclysm](https://modrinth.com/project/46KJle7n) | Difficult dungeons, challenging bosses and powerful equipment. | [3.33](https://modrinth.com/project/46KJle7n/version/PsPYpoCC) | `mods/l_enders-cataclysm.pw.toml` |
| [Nullscape](https://modrinth.com/project/LPjGiSO4) | Changed End terrain with additional biomes. | [1.2.14](https://modrinth.com/project/LPjGiSO4/version/3fv8O3xX) | `mods/nullscape.pw.toml` |
| [Spawn](https://modrinth.com/project/rex9wwpz) | Wilderness content including animals, biomes, ambience and other features. | [4.0.8](https://modrinth.com/project/rex9wwpz/version/OgmUYgeL) | `mods/spawn-mod.pw.toml` |
| [Streams Reflowing](https://modrinth.com/project/oLS8HdJ1) | Flowing streams in world generation. | [2.14.4](https://modrinth.com/project/oLS8HdJ1/version/3NL8BzMK) | `mods/streams-reflowing.pw.toml` |
| [Tectonic](https://modrinth.com/project/lWDHr9jE) | Expanded terrain shapes and height variation. | [3.0.28-neoforge-21.1](https://modrinth.com/project/lWDHr9jE/version/n4iyW7aB) | `mods/tectonic.pw.toml` |
| [Terralith](https://modrinth.com/project/8oi3bsk5) | Additional biomes and structures built from vanilla blocks. | [2.6.2](https://modrinth.com/project/8oi3bsk5/version/IY93YaEe) | `mods/terralith.pw.toml` |
| [Variants&Ventures](https://modrinth.com/project/lNDRiXkY) | Additional creature variants. | [neoforge-1.0.28+mc1.21.1](https://modrinth.com/project/lNDRiXkY/version/FIBENnpb) | `mods/variants-and-ventures.pw.toml` |
| [Village Taverns (RPG Series)](https://modrinth.com/project/bj4a8NjJ) | Tavern structures in villages. | [1.3.0+1.21.1-neoforge](https://modrinth.com/project/bj4a8NjJ/version/qhOcjQ6u) | `mods/village-taverns.pw.toml` |
| [When Dungeons Arise](https://modrinth.com/project/8DfbfASn) | Additional dungeons and structures, often with hostile encounters. | [2.1.68](https://modrinth.com/project/8DfbfASn/version/XIRJSFQ0) | `mods/when-dungeons-arise.pw.toml` |
| [YUNG's Better Desert Temples](https://modrinth.com/project/XNlO7sBv) | A complete redesign of Minecraft's desert temples. | [1.21.1-NeoForge-4.1.5](https://modrinth.com/project/XNlO7sBv/version/GQ9iNWkI) | `mods/yungs-better-desert-temples.pw.toml` |
| [YUNG's Better Dungeons](https://modrinth.com/project/o1C1Dkj5) | A complete redesign of Minecraft's dungeons. | [1.21.1-NeoForge-5.1.4](https://modrinth.com/project/o1C1Dkj5/version/D6aZn0Em) | `mods/yungs-better-dungeons.pw.toml` |
| [YUNG's Better Jungle Temples](https://modrinth.com/project/z9Ve58Ih) | A complete redesign of Minecraft's jungle temples. | [1.21.1-NeoForge-3.1.2](https://modrinth.com/project/z9Ve58Ih/version/P00i2hJn) | `mods/yungs-better-jungle-temples.pw.toml` |
| [YUNG's Better Mineshafts](https://modrinth.com/project/HjmxVlSr) | A long-awaited and much-needed abandoned mineshaft overhaul. | [1.21.1-NeoForge-5.1.1](https://modrinth.com/project/HjmxVlSr/version/Go3nbneL) | `mods/yungs-better-mineshafts.pw.toml` |
| [YUNG's Better Nether Fortresses](https://modrinth.com/project/Z2mXHnxP) | A complete redesign of Minecraft's Nether fortresses. | [1.21.1-NeoForge-3.1.5](https://modrinth.com/project/Z2mXHnxP/version/iopJiJQp) | `mods/yungs-better-nether-fortresses.pw.toml` |
| [YUNG's Better Ocean Monuments](https://modrinth.com/project/3dT9sgt4) | A complete redesign of Minecraft's ocean monuments. | [1.21.1-NeoForge-4.1.2](https://modrinth.com/project/3dT9sgt4/version/yFjEcj2g) | `mods/yungs-better-ocean-monuments.pw.toml` |
| [YUNG's Better Strongholds](https://modrinth.com/project/kidLKymU) | A complete redesign of Minecraft's strongholds. | [1.21.1-NeoForge-5.1.3](https://modrinth.com/project/kidLKymU/version/8U0dIfSM) | `mods/yungs-better-strongholds.pw.toml` |
| [YUNG's Better Witch Huts](https://modrinth.com/project/t5FRdP87) | Adds overhauled witch huts to swamps. | [1.21.1-NeoForge-4.1.1](https://modrinth.com/project/t5FRdP87/version/AvedwcIe) | `mods/yungs-better-witch-huts.pw.toml` |

### Navigate, carry supplies and recover

Convenience tip candidates: 16. Give a short action or control tip, along with destination, ownership, capacity or recovery limits that require release-specific verification.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Backpacks!](https://modrinth.com/project/MGcd6kTf) | Dyeable and upgradeable backpacks. | [1.3.5](https://modrinth.com/project/MGcd6kTf/version/uJz7ESID) | `mods/vanilla-backpacks.pw.toml` |
| [Carry On](https://modrinth.com/project/joEfVgkn) | Carry On allows you to pick up Tile Entities and Mobs and carry them around. | [2.2.6](https://modrinth.com/project/joEfVgkn/version/PV8oLZ1q) | `mods/carry-on.pw.toml` |
| [Comforts](https://modrinth.com/project/SaCpeal4) | Portable sleeping bags and hammocks without changing the player's spawn point. | [9.0.5+1.21.1](https://modrinth.com/project/SaCpeal4/version/3kpPjcTc) | `mods/comforts.pw.toml` |
| [Corpse](https://modrinth.com/project/WrpuIfhw) | Death recovery through a corpse system. The summary's promise does not establish lossless recovery in every situation. | [neoforge-1.21.1-1.1.13](https://modrinth.com/project/WrpuIfhw/version/Zwf8nv8y) | `mods/corpse.pw.toml` |
| [Corpse x Curios API Compat](https://modrinth.com/project/pJGcKPh1) | Directly equips recovered Curios items into accessory slots. | [4.0.1](https://modrinth.com/project/pJGcKPh1/version/Ix4uAd2i) | `mods/corpse-x-curios-api-compat.pw.toml` |
| [Easy Anvils](https://modrinth.com/project/OZBR5JT5) | Stored anvil items, changed costs and repair-penalty improvements. | [v21.1.0-1.21.1-NeoForge](https://modrinth.com/project/OZBR5JT5/version/fSQSKhdF) | `mods/easy-anvils.pw.toml` |
| [Easy Shulker Boxes](https://modrinth.com/project/gA5euN8S) | Browse, insert and extract shulker-box contents from the inventory. | [v21.1.3-1.21.1-NeoForge](https://modrinth.com/project/gA5euN8S/version/OBp8ltOS) | `mods/easy-shulker-boxes.pw.toml` |
| [Explorer's Compass](https://modrinth.com/project/RV1qfVQ8) | Allows you to locate structures anywhere in the world. | [1.21.1-3.4.0-neoforge](https://modrinth.com/project/RV1qfVQ8/version/hIJ2Ev1Q) | `mods/explorers-compass.pw.toml` |
| [Lootr](https://modrinth.com/project/EltpO5cN) | Separate loot inventories for individual players in supported loot chests. | [1.21.1-1.11.37.120](https://modrinth.com/project/EltpO5cN/version/C2tLycH2) | `mods/lootr.pw.toml` |
| [Nature's Compass](https://modrinth.com/project/fPetb5Kh) | Allows you to locate biomes anywhere in the world. | [1.21.1-3.4.0-neoforge](https://modrinth.com/project/fPetb5Kh/version/nFniEtJV) | `mods/natures-compass.pw.toml` |
| [NetherPortalFix](https://modrinth.com/project/nPZr02ET) | Ensures correct destinations when traveling back and forth through Nether Portals in Multiplayer. | [21.1.1+neoforge-1.21.1](https://modrinth.com/project/nPZr02ET/version/O09BGtgh) | `mods/netherportalfix.pw.toml` |
| [Reinforced Shulker Boxes](https://modrinth.com/project/xlOwuSdN) | Adds reinforced shulker boxes. | [3.2.1+1.21.1](https://modrinth.com/project/xlOwuSdN/version/PZOyr6QP) | `mods/reinforced-shulker-boxes.pw.toml` |
| [Shulker Drops Two](https://modrinth.com/project/UjXIyw47) | Configurable additional shulker-shell drops. The pack's exact drop settings are not established here. | [1.21.1-3.7-fabric+forge+neo](https://modrinth.com/project/UjXIyw47/version/eFIjYo5d) | `mods/shulker-drops-two.pw.toml` |
| [Xaero's Maps: Multiplayer+](https://modrinth.com/project/stTaMuWa) | Multiplayer map features, including explored-world synchronization. | [1.1.0+1.21.1-neoforge](https://modrinth.com/project/stTaMuWa/version/b7pFomcM) | `mods/xaeros-maps-multiplayer-plus.pw.toml` |
| [Xaero's Minimap](https://modrinth.com/project/1bokaNcj) | A nearby terrain and entity map with player-created waypoints. | [neoforge-1.21.1-26.6.0](https://modrinth.com/project/1bokaNcj/version/irjR7dHk) | `mods/xaeros-minimap.pw.toml` |
| [Xaero's World Map](https://modrinth.com/project/NcUtCpym) | A full-screen map of explored terrain. | [neoforge-1.21.1-1.47.0](https://modrinth.com/project/NcUtCpym/version/SnQ4SoDe) | `mods/xaeros-world-map.pw.toml` |

### Find recipes and simplify everyday play

Convenience tip candidates: 38. Give one useful search, control or interface tip. Display improvements do not establish custom progression content.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Advancement Plaques](https://modrinth.com/project/9NM0dXub) | Replacement advancement notifications. | [1.6.8](https://modrinth.com/project/9NM0dXub/version/OWylG33I) | `mods/advancement-plaques.pw.toml` |
| [AppleSkin](https://modrinth.com/project/EsAfCjCV) | Food and hunger information in the on-screen display. | [3.0.9+mc1.21](https://modrinth.com/project/EsAfCjCV/version/uAKA6Laj) | `mods/appleskin.pw.toml` |
| [Better Days](https://modrinth.com/project/tPLE214j) | Configurable day length and sleep-time acceleration. | [1.21.1-3.3.6.3-NEOFORGE](https://modrinth.com/project/tPLE214j/version/Ho93yCC3) | `mods/betterdays.pw.toml` |
| [Better ModList](https://modrinth.com/project/sbpqhzIG) | Mod-list display improvements, including library filtering and function badges. | [1.1.22](https://modrinth.com/project/sbpqhzIG/version/XlCN7NWa) | `mods/better-modlist.pw.toml` |
| [BetterF3](https://modrinth.com/project/8shC1gFX) | A configurable, more readable debug display. | [11.0.3](https://modrinth.com/project/8shC1gFX/version/maXNB1dn) | `mods/betterf3.pw.toml` |
| [Controlling](https://modrinth.com/project/xv94TkTM) | Adds a search bar to the Key-Bindings menu. | [19.0.5](https://modrinth.com/project/xv94TkTM/version/FaNppCJJ) | `mods/controlling.pw.toml` |
| [Create Waystones Recipes](https://modrinth.com/project/wQpKGqNJ) | Changes Waystones recipes to use Create ingredients. | [3.0.1.b](https://modrinth.com/project/wQpKGqNJ/version/KZ8x4j1W) | `mods/create-waystones-recipes.pw.toml` |
| [Create: Stam1o Tweaks](https://modrinth.com/project/46RgF8H2) | Pack-specific tweaks to Create and Minecraft. Review the selected release before writing a mechanics guide. | [1.0.8+1.21.1-neo](https://modrinth.com/project/46RgF8H2/version/QxBHdxaK) | `mods/create-stam1o-tweaks.pw.toml` |
| [Curios API](https://modrinth.com/project/vvuO3ImH) | Accessory equipment slots and supporting interfaces. Individual accessories determine the gameplay effects. | [9.5.1+1.21.1](https://modrinth.com/project/vvuO3ImH/version/yohfFbgD) | `mods/curios.pw.toml` |
| [Detail Armor Bar Reconstructed](https://modrinth.com/project/Si9Uim4y) | Additional armor information in the armor display. | [5.0.2](https://modrinth.com/project/Si9Uim4y/version/qePsyQOP) | `mods/detail-armor-bar-reconstructed.pw.toml` |
| [EMI](https://modrinth.com/project/fRiHVvU7) | Searchable item and recipe browsing. | [1.1.24+1.21.1+neoforge](https://modrinth.com/project/fRiHVvU7/version/5sIPA1To) | `mods/emi.pw.toml` |
| [EMI Enchanting](https://modrinth.com/project/wbWoo11W) | Enchantment information in EMI, including eligible items and exclusions. | [0.1.2+1.21+neoforge](https://modrinth.com/project/wbWoo11W/version/ZyJ6TKvh) | `mods/emi-enchanting.pw.toml` |
| [EMI Loot](https://modrinth.com/project/qbbO7Jns) | Chest, block and creature loot information in EMI. | [0.7.9+1.21+neoforge](https://modrinth.com/project/qbbO7Jns/version/QXkODMCT) | `mods/emi-loot.pw.toml` |
| [EMI professions (EMIP)](https://modrinth.com/project/LGVihYcz) | Profession workstation information in EMI. | [1.0.3](https://modrinth.com/project/LGVihYcz/version/wGOa5uxT) | `mods/emi-professions-(emip).pw.toml` |
| [Extreme sound muffler](https://modrinth.com/project/5IIKsxiL) | Extreme sound muffler is a client side mod that allows you to muffle sounds selectively. | [3.56-1.21.1](https://modrinth.com/project/5IIKsxiL/version/m5je0Rop) | `mods/extreme_sound_muffler.pw.toml` |
| [Interactic Renewed](https://modrinth.com/project/BM12h14f) | A maintained Interactic fork. The summary does not specify its interactions. | [0.2.2+1.21.1](https://modrinth.com/project/BM12h14f/version/W05MzXWJ) | `mods/interactic-renewed.pw.toml` |
| [Jade Addons (Neo/Forge)](https://modrinth.com/project/xuDOzCLy) | Additional mod support for Jade. | [6.1.2+neoforge](https://modrinth.com/project/xuDOzCLy/version/O3F6Dkle) | `mods/jade-addons-forge.pw.toml` |
| [Jade 🔍](https://modrinth.com/project/nvQzSEkH) | Information about the block or entity you are looking at. | [15.10.6+neoforge](https://modrinth.com/project/nvQzSEkH/version/eYz2YBGT) | `mods/jade.pw.toml` |
| [Leaves Be Gone](https://modrinth.com/project/AVq17PqV) | Faster leaf decay after cutting trees. | [v21.1.1-1.21.1-NeoForge](https://modrinth.com/project/AVq17PqV/version/kAbmpvF3) | `mods/leaves-be-gone.pw.toml` |
| [Lighty](https://modrinth.com/project/yjvKidNM) | The Light Overlay Mod with a twist. | [3.0.0-beta.8+1.21.1](https://modrinth.com/project/yjvKidNM/version/Ua5CgydL) | `mods/lighty.pw.toml` |
| [Mouse Tweaks](https://modrinth.com/project/aC3cM3Vq) | Additional mouse controls for inventory management. | [1.21-2.26.1-neoforge](https://modrinth.com/project/aC3cM3Vq/version/9I21YYxf) | `mods/mouse-tweaks.pw.toml` |
| [Ok Zoomer - It's Zoom!](https://modrinth.com/project/aXf2OSFU) | Configurable zoom controls. | [10.0.0-beta.13+neo](https://modrinth.com/project/aXf2OSFU/version/AkPuuAgJ) | `mods/ok-zoomer.pw.toml` |
| [Polymorph](https://modrinth.com/project/tagwiZkJ) | Choose a crafting result when multiple recipes conflict. | [1.1.0+1.21.1](https://modrinth.com/project/tagwiZkJ/version/VEburL70) | `mods/polymorph.pw.toml` |
| [Progress Peek](https://modrinth.com/project/1A2XNzUB) | Display game loading progress on the taskbar. | [1.1.0+1.21.1-neoforge](https://modrinth.com/project/1A2XNzUB/version/Oa4LONcz) | `mods/progresspeek.pw.toml` |
| [Reliable Advancements](https://modrinth.com/project/xVwaUG1g) | An improved advancement screen and in-game advancement editing. It does not itself prove that the pack has custom progression content. | [6.3.0+1.21.1-neoforge](https://modrinth.com/project/xVwaUG1g/version/yE5ZGOzA) | `mods/reliable-advancements.pw.toml` |
| [Reliable EMI (REMI)](https://modrinth.com/project/N9WucjHL) | Configurable additions to EMI. | [4.7.9-1.21.1-neoforge](https://modrinth.com/project/N9WucjHL/version/iOekvzRL) | `mods/reliable-emi.pw.toml` |
| [RightClickHarvest](https://modrinth.com/project/Cnejf5xM) | Allows you to harvest crops with right click. | [4.6.1+1.21.1](https://modrinth.com/project/Cnejf5xM/version/djt0zS53) | `mods/rightclickharvest.pw.toml` |
| [Smarter Farmers (farmers replant)](https://modrinth.com/project/Bh6ZOMvp) | Allows villagers to replant the correct seed and allows them to use modded ones. | [1.21-2.2.4](https://modrinth.com/project/Bh6ZOMvp/version/odppGdXf) | `mods/smarter-farmers-farmers-replant.pw.toml` |
| [Sophisticated Inventory Interactions](https://modrinth.com/project/orgY0JIo) | Container search, sorting and transfer controls, including player-inventory sorting. | [1.21.1-0.1.9.160](https://modrinth.com/project/orgY0JIo/version/wiUUWZ2E) | `mods/sophisticated-inventory-interactions.pw.toml` |
| [Status Effect Bars Reforged](https://modrinth.com/project/TxIuhIFo) | Remaining-duration bars for active status effects. | [1.0.2](https://modrinth.com/project/TxIuhIFo/version/PPVE16f7) | `mods/status-effect-bars-reforged.pw.toml` |
| [Stylish Effects](https://modrinth.com/project/onDuQF5e) | More compact status-effect display across menus. | [v21.1.3-1.21.1-NeoForge](https://modrinth.com/project/onDuQF5e/version/MT3yeDds) | `mods/stylish-effects.pw.toml` |
| [Toast Control](https://modrinth.com/project/CnOG2wlS) | Control over on-screen notification popups. | [1.21.1-9.0.1](https://modrinth.com/project/CnOG2wlS/version/jXHDAUrd) | `mods/toast-control.pw.toml` |
| [ToolTipFix](https://modrinth.com/project/2RKFTmiB) | Prevents tooltips from extending off the screen. | [1.1.1-1.20](https://modrinth.com/project/2RKFTmiB/version/B2L4LeMV) | `mods/tooltipfix.pw.toml` |
| [Trade Refresh](https://modrinth.com/project/OlAQOlqx) | A trade-refresh control in the trading interface. | [3.0.4](https://modrinth.com/project/OlAQOlqx/version/okw4BAHD) | `mods/trade-refresh.pw.toml` |
| [TrashSlot](https://modrinth.com/project/vRYk0bv7) | A movable inventory trash slot. Check its current binding before discarding items. | [21.1.11+neoforge-1.21.1](https://modrinth.com/project/vRYk0bv7/version/HY8Ybozd) | `mods/trashslot.pw.toml` |
| [Traveler's Titles](https://modrinth.com/project/JtifUr64) | Biome and dimension entry titles. | [1.21.1-NeoForge-5.1.3](https://modrinth.com/project/JtifUr64/version/2y01mBUy) | `mods/travelers-titles.pw.toml` |
| [Universal Bone Meal](https://modrinth.com/project/66VIiT1y) | Expanded bone-meal support for plants. | [v21.1.0-1.21.1-NeoForge](https://modrinth.com/project/66VIiT1y/version/5g9aZDW0) | `mods/universal-bone-meal.pw.toml` |
| [Villager Names](https://modrinth.com/project/gqRXDo8B) | Default or custom names for villagers. | [1.21.1-8.5-fabric+forge+neo](https://modrinth.com/project/gqRXDo8B/version/2PLlKTES) | `mods/villager-names-serilum.pw.toml` |

### Adjust visuals, sound and accessibility

Convenience tip candidates: 26. Explain the visible effect and where to find its settings. Keep player preference and performance testing separate.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [[EMF] Entity Model Features](https://modrinth.com/project/4I1XuqiY) | Resource-pack support for OptiFine-format custom entity models. | [3.3.11-neoforge-1.21](https://modrinth.com/project/4I1XuqiY/version/bRlX1x4e) | `mods/entity-model-features.pw.toml` |
| [[ETF] Entity Texture Features](https://modrinth.com/project/BVzZfTc1) | Resource-pack support for emissive, randomized and custom entity textures. | [7.2.5-neoforge-1.21](https://modrinth.com/project/BVzZfTc1/version/CfQJbv1u) | `mods/entitytexturefeatures.pw.toml` |
| [Better Biome Reblend](https://modrinth.com/project/Xh8hkQmD) | Improved biome-color blending. | [1.5.2](https://modrinth.com/project/Xh8hkQmD/version/HZlLCOct) | `mods/bbrb.pw.toml` |
| [Continuity](https://modrinth.com/project/1IjD5062) | A Minecraft mod that allows for efficient connected textures. | [3.0.0+1.21.neoforge](https://modrinth.com/project/1IjD5062/version/eXGUs5sy) | `mods/continuity.pw.toml` |
| [Cool Rain Reforged](https://modrinth.com/project/IgftU6Mn) | Creates ambient sounds for certain blocks during rain. | [1.0.2](https://modrinth.com/project/IgftU6Mn/version/SwSSfJQQ) | `mods/cool-rain-reforged.pw.toml` |
| [Cubes Without Borders](https://modrinth.com/project/ETlrkaYF) | Allows you to play Minecraft in a borderless fullscreen window. | [3.0.0+1.21](https://modrinth.com/project/ETlrkaYF/version/epixUL1j) | `mods/cubes-without-borders.pw.toml` |
| [Distant Horizons](https://modrinth.com/project/uCdwusMi) | Distant terrain rendering. Visual quality, resource costs and moving-build visibility need separate testing. | [3.3.3-1.21.1](https://modrinth.com/project/uCdwusMi/version/9w34y8ai) | `mods/distanthorizons.pw.toml` |
| [Eating Animations](https://modrinth.com/project/X8CISwXp) | A Forge port of the Eating Animation mod. | [6.0.1](https://modrinth.com/project/X8CISwXp/version/D7saUVV5) | `mods/eating-animations.pw.toml` |
| [Explosive Enhancement: Reforged](https://modrinth.com/project/r0camchr) | Changed explosion visuals. | [1.2.0](https://modrinth.com/project/r0camchr/version/GYn7YRXz) | `mods/explosive-enhancement-forge.pw.toml` |
| [Fancy World Animations [FWA]](https://modrinth.com/project/IAzUFvS6) | Animations for interactive blocks and hanging lanterns. | [1.2.31](https://modrinth.com/project/IAzUFvS6/version/79A6vRlK) | `mods/fwa.pw.toml` |
| [GrandTeleport NeoForge](https://modrinth.com/project/PsllFHj8) | A cinematic zoom-out teleportation animation. | [1.0.0](https://modrinth.com/project/PsllFHj8/version/SRYiyHAS) | `mods/grandteleport-neoforge.pw.toml` |
| [Iris Shaders](https://modrinth.com/project/YL57xq9U) | Shader-pack loading support. | [1.8.14-beta.1+1.21.1-neoforge](https://modrinth.com/project/YL57xq9U/version/KduFYu4t) | `mods/iris.pw.toml` |
| [More Sounds](https://modrinth.com/project/8jvcOd6S) | Additional sounds and mod compatibility for Sounds. | [1.21.x-0.3.0-neoforge](https://modrinth.com/project/8jvcOd6S/version/s0FVNDXY) | `mods/more-sounds.pw.toml` |
| [Not Enough Animations](https://modrinth.com/project/MPCX6s5C) | First-person-style player animations shown in third person. | [1.12.6](https://modrinth.com/project/MPCX6s5C/version/VCuMsK45) | `mods/not-enough-animations.pw.toml` |
| [Particle Effects](https://modrinth.com/project/PLAGcSFJ) | Individual particle textures for vanilla status effects. | [1.6.0+1.21.1+neoforge](https://modrinth.com/project/PLAGcSFJ/version/HVllSdtX) | `mods/particle-effects.pw.toml` |
| [Particular ✨ Reforged](https://modrinth.com/project/pYFUU6cq) | Ambient visual effects. | [1.5.5](https://modrinth.com/project/pYFUU6cq/version/gxO1XUMR) | `mods/particular-reforged.pw.toml` |
| [Polytone](https://modrinth.com/project/3qAYkBMB) | Resource-pack control of colors and block sounds. | [1.21-4.5.3](https://modrinth.com/project/3qAYkBMB/version/ROLbT0WQ) | `mods/polytone.pw.toml` |
| [Presence Footsteps (NeoForge)](https://modrinth.com/project/JIEwmDVI) | Presence Footsteps sound support ported to NeoForge. The summary does not specify each sound interaction. | [1.21.1-1.12.0-beta.1](https://modrinth.com/project/JIEwmDVI/version/f3SxKzof) | `mods/pf-neoforge.pw.toml` |
| [Reese's Sodium Options](https://modrinth.com/project/Bh37bMuy) | Alternative Options Menu for Sodium. | [mc1.21.1-2.2.4+neoforge](https://modrinth.com/project/Bh37bMuy/version/XjF2IkL8) | `mods/reeses-sodium-options.pw.toml` |
| [Ripple](https://modrinth.com/project/5hOgUfig) | Particles that react to entities. | [1.2.1](https://modrinth.com/project/5hOgUfig/version/VqmLKAjX) | `mods/ripple.pw.toml` |
| [Sodium Dynamic Lights](https://modrinth.com/project/PxQSWIcD) | Multiloader port of LambDynLights that adds Sodium options integration. | [neoforge-1.21.1-1.0.10](https://modrinth.com/project/PxQSWIcD/version/XI0WLXdn) | `mods/sodium-dynamic-lights.pw.toml` |
| [Sodium Extra](https://modrinth.com/project/PtjYWJkn) | A Sodium addon that adds features that shouldn't be in Sodium. | [mc1.21.1-0.9.4+neoforge](https://modrinth.com/project/PtjYWJkn/version/ufpcXU9c) | `mods/sodium-extra.pw.toml` |
| [Sound Physics Remastered](https://modrinth.com/project/qyVF9oeo) | Sound attenuation, reverberation and absorption through blocks. | [neoforge-1.21.1-1.5.1](https://modrinth.com/project/qyVF9oeo/version/Dd2tmpsk) | `mods/sound-physics-remastered.pw.toml` |
| [Sounds](https://modrinth.com/project/ZouiUX7t) | Additional sound effects for interfaces, items, blocks and other interactions. | [2.4.22+lts+1.21.1-neoforge](https://modrinth.com/project/ZouiUX7t/version/kti7i9SG) | `mods/sound.pw.toml` |
| [Spawn Animations](https://modrinth.com/project/zrzYrlm0) | Hostile mobs dig out of the ground or poof into existence when they spawn. | [1.11.6+mod](https://modrinth.com/project/zrzYrlm0/version/xFTfXEwk) | `mods/spawn-animations.pw.toml` |
| [Team Capes](https://modrinth.com/project/Sw4LxdbE) | Team-colored capes for players who are in teams. | [1.1.2+1.21-neoforge](https://modrinth.com/project/Sw4LxdbE/version/kmuG9MOR) | `mods/team-capes.pw.toml` |

## Technical-only appendix

These 88 selected mods support other systems, supply compatibility or improve operation. Keep them out of normal onboarding. This treatment does not imply they are optional or safe to remove. Some expose visible controls or statistics, but their independent contribution is primarily supporting infrastructure. Sable is the moving-block framework, not a second vehicle crafting route. Chunky is administrative pregeneration, not a player quest.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [AI Improvements: Performance Tuning](https://modrinth.com/project/DSVgwcji) | Creature-behavior optimization, including optional behavior disabling. | [0.5.3](https://modrinth.com/project/DSVgwcji/version/dGNP90t0) | `mods/ai-improvements.pw.toml` |
| [Almanac](https://modrinth.com/project/Gi02250Z) | Shared cross-loader code for the author's mods. | [1.5.2](https://modrinth.com/project/Gi02250Z/version/cHGan9fQ) | `mods/almanac.pw.toml` |
| [Apollib](https://modrinth.com/project/VDI2Ytax) | Shared configuration and registration utilities. | [1.2.0-neoforge-21.1](https://modrinth.com/project/VDI2Ytax/version/zMAIdVwq) | `mods/apollib.pw.toml` |
| [Architectury API](https://modrinth.com/project/lhGA9TYQ) | Shared development interface for mods targeting multiple loaders. | [13.0.11+neoforge](https://modrinth.com/project/lhGA9TYQ/version/1IiqEQGl) | `mods/architectury-api.pw.toml` |
| [Armor Model API](https://modrinth.com/project/onz2NN2n) | Support for rendering Bedrock and GeckoLib armor models through vanilla armor rendering. | [1.1.0+1.21.1-neoforge](https://modrinth.com/project/onz2NN2n/version/QRkmKYGJ) | `mods/armor-model-api.pw.toml` |
| [AsyncParticles](https://modrinth.com/project/c3onkd5k) | Particle simulation and rendering optimization. | [21.1.4.5](https://modrinth.com/project/c3onkd5k/version/8S3JSSbl) | `mods/asyncparticles.pw.toml` |
| [Athena](https://modrinth.com/project/b1ZV3DIJ) | Shared support for connected block textures. | [4.0.6](https://modrinth.com/project/b1ZV3DIJ/version/dJgL278E) | `mods/athena-ctm.pw.toml` |
| [AttributeFix](https://modrinth.com/project/lOOpEntO) | Removes limits in the attribute system that can affect modded statistics. | [21.1.3](https://modrinth.com/project/lOOpEntO/version/TyNITLDY) | `mods/attributefix.pw.toml` |
| [BadOptimizations](https://modrinth.com/project/g96Z4WVZ) | Optimization mod that focuses on things other than rendering. | [2.4.1](https://modrinth.com/project/g96Z4WVZ/version/S2qthD5S) | `mods/badoptimizations.pw.toml` |
| [BaguetteLib](https://modrinth.com/project/OfKzpbRU) | Shared support for death handling and inventory tracking. | [2.0.7](https://modrinth.com/project/OfKzpbRU/version/5RiJQA1Z) | `mods/baguettelib.pw.toml` |
| [Balm](https://modrinth.com/project/MBAkmtvl) | Shared support for mods targeting multiple loaders. | [21.0.66+neoforge-1.21.1](https://modrinth.com/project/MBAkmtvl/version/CquiaiDj) | `mods/balm.pw.toml` |
| [Bookshelf](https://modrinth.com/project/uy4Cnpcm) | Shared library for other mods. | [21.1.81](https://modrinth.com/project/uy4Cnpcm/version/1sdJl7J1) | `mods/bookshelf-lib.pw.toml` |
| [Bundle API](https://modrinth.com/project/n8QN6Z1a) | Shared support for larger bundles restricted by item tags. | [1.1.0-neoforge](https://modrinth.com/project/n8QN6Z1a/version/w5F5wdko) | `mods/bundle-api.pw.toml` |
| [Chunky](https://modrinth.com/project/fALzjamp) | Administrator-controlled chunk pregeneration. Players do not need a crafting guide for it. | [1.4.23](https://modrinth.com/project/fALzjamp/version/LuFhm4eU) | `mods/chunky.pw.toml` |
| [Cloth Config API](https://modrinth.com/project/9s6osm5g) | Shared configuration library for mods. | [15.0.140+neoforge](https://modrinth.com/project/9s6osm5g/version/izKINKFg) | `mods/cloth-config.pw.toml` |
| [Clumps](https://modrinth.com/project/Wnxd13zP) | Combines experience orbs to reduce processing work. | [19.0.0.1](https://modrinth.com/project/Wnxd13zP/version/jo7lDoK4) | `mods/clumps.pw.toml` |
| [Collective](https://modrinth.com/project/e0M1UDsY) | Shared code for Serilum's mods. | [1.21.1-8.42-fabric+forge+neo](https://modrinth.com/project/e0M1UDsY/version/ZHBXubZ4) | `mods/collective.pw.toml` |
| [Concurrent Chunk Management Engine (NeoForge)](https://modrinth.com/project/COlSi5iR) | Chunk-processing optimization. | [0.4.0-alpha.0.122+1.21.1](https://modrinth.com/project/COlSi5iR/version/yxOYFgnK) | `mods/c2me-neoforge.pw.toml` |
| [Configured Defaults](https://modrinth.com/project/SISoSFPP) | Supplies initial configuration files when they are absent. | [v21.1.3-1.21.1-NeoForge](https://modrinth.com/project/SISoSFPP/version/HJxTPhTM) | `mods/configured-defaults.pw.toml` |
| [Create Sable Dynamic Lights](https://modrinth.com/project/eIsyUZG3) | A bridge between Sodium Dynamic Lights and the Create mod as well as the Sable mod used for mods like Create: Aeronautics. | [2.3.1-sodium-sable](https://modrinth.com/project/eIsyUZG3/version/sKw2ERw2) | `mods/create-sable-dynamic-lights.pw.toml` |
| [Create: LazyTick](https://modrinth.com/project/Z0d7hFh4) | Optimization for large numbers of Create machines. | [1.21.1-2.4.9-6.0.x](https://modrinth.com/project/Z0d7hFh4/version/Dx5cIwDo) | `mods/createlazytick.pw.toml` |
| [CreateBetterFps](https://modrinth.com/project/lMYIHZNH) | Create rendering optimization intended for shader use. No performance gain has been measured for this pack. | [1.1.4](https://modrinth.com/project/lMYIHZNH/version/QWqEdWHy) | `mods/createbetterfps.pw.toml` |
| [CreativeCore](https://modrinth.com/project/OsZiaDHq) | Supporting core library. | [2.13.50](https://modrinth.com/project/OsZiaDHq/version/v1GIKf4i) | `mods/creativecore.pw.toml` |
| [Cull Leaves](https://modrinth.com/project/GNxdLCoP) | Hides unnecessary leaf geometry to reduce rendering work. | [4.1.1+1.21.1-neoforge](https://modrinth.com/project/GNxdLCoP/version/V7PU4g8I) | `mods/cull-leaves.pw.toml` |
| [DragonLib](https://modrinth.com/project/sbIsGaOV) | Shared code used by the author's mods. | [1.21.1-beta-3.0.28](https://modrinth.com/project/sbIsGaOV/version/x376YU9w) | `mods/dragonlib.pw.toml` |
| [Dynamic FPS](https://modrinth.com/project/LQ3K71Q1) | Reduce resource usage while Minecraft is in the background, idle, or on battery. | [3.11.4](https://modrinth.com/project/LQ3K71Q1/version/T238FZpQ) | `mods/dynamic-fps.pw.toml` |
| [EMF Compat: Core](https://modrinth.com/project/hbGct5uU) | Shared framework for the EMF Compat family. | [2.0.0](https://modrinth.com/project/hbGct5uU/version/31At82lp) | `mods/emf-compat-core.pw.toml` |
| [EMF Compat: Create](https://modrinth.com/project/J9McOdzy) | Makes Create animations work correctly with animated EMF player models. | [2.0.0](https://modrinth.com/project/J9McOdzy/version/FYa3pSLC) | `mods/create-emf-compat-skyhook.pw.toml` |
| [EMF Compat: Not Enough Animations](https://modrinth.com/project/IGCrWfL7) | Makes Not Enough Animations work correctly with animated EMF player models. | [1.2.0](https://modrinth.com/project/IGCrWfL7/version/2PAaJs7w) | `mods/not-enough-animations-emf-compat.pw.toml` |
| [Entity Culling](https://modrinth.com/project/NNAgCjsB) | Hides entities and block entities that are not visible. | [1.11.2](https://modrinth.com/project/NNAgCjsB/version/8w8FfUPs) | `mods/entityculling.pw.toml` |
| [FerriteCore](https://modrinth.com/project/uXXizFIs) | Memory usage optimizations. | [7.0.3-neoforge](https://modrinth.com/project/uXXizFIs/version/x7kQWVju) | `mods/ferrite-core.pw.toml` |
| [Flerovium](https://modrinth.com/project/4Rh1Mobu) | Rendering optimization. This inventory does not verify the advertised performance gains. | [1.0.18](https://modrinth.com/project/4Rh1Mobu/version/ROADZx1W) | `mods/flerovium.pw.toml` |
| [Forgified Fabric API](https://modrinth.com/project/Aqlf1Shp) | Fabric API functionality implemented on NeoForge. | [0.116.15+2.3.5+1.21.1](https://modrinth.com/project/Aqlf1Shp/version/V9WdDUTx) | `mods/forgified-fabric-api.pw.toml` |
| [Fzzy Config](https://modrinth.com/project/hYykXjDp) | Configuration support with settings screens, validation and synchronization. | [0.7.7+1.21+neoforge](https://modrinth.com/project/hYykXjDp/version/uG7oHgw6) | `mods/fzzy-config.pw.toml` |
| [Geckolib](https://modrinth.com/project/8BmcQJ2H) | Animation library for entities, blocks, items and armor. | [4.9.3](https://modrinth.com/project/8BmcQJ2H/version/Grwn5rUB) | `mods/geckolib.pw.toml` |
| [GroovyModLoader (GML)](https://modrinth.com/project/zg2tT2Vu) | Groovy language support for NeoForge mods. | [6.0.2](https://modrinth.com/project/zg2tT2Vu/version/IDRMIIb4) | `mods/gml.pw.toml` |
| [Hide Experimental Warning](https://modrinth.com/project/Rm4OOdHd) | Hides the Experimental Settings Warning when trying to create or load a modded world. | [1.21.1-1.3-fabric+forge+neo](https://modrinth.com/project/Rm4OOdHd/version/tJbfSalt) | `mods/hide-experimental-warning.pw.toml` |
| [Iceberg](https://modrinth.com/project/5faXoLqX) | Shared events, helpers and utilities for other mods. | [1.3.2](https://modrinth.com/project/5faXoLqX/version/IMssx9du) | `mods/iceberg.pw.toml` |
| [ImmediatelyFast](https://modrinth.com/project/5ZwdcRci) | Speed up immediate mode rendering in Minecraft. | [1.6.14+1.21.1-neoforge](https://modrinth.com/project/5ZwdcRci/version/OUpXxw4n) | `mods/immediatelyfast.pw.toml` |
| [Ixeris](https://modrinth.com/project/p8RJPJIC) | Buffered raw input and threaded event polling. | [4.5.2+1.21.1-neoforge](https://modrinth.com/project/p8RJPJIC/version/hZ6rxco6) | `mods/ixeris.pw.toml` |
| [JamLib](https://modrinth.com/project/IYY9Siz8) | Shared cross-platform code for JamCoreModding's mods. | [1.3.6+1.21.1](https://modrinth.com/project/IYY9Siz8/version/n6UM6TcS) | `mods/jamlib.pw.toml` |
| [Kerria](https://modrinth.com/project/f0ruQTF7) | Faster texture animation. | [1.3.2+1.21.1-neoforge](https://modrinth.com/project/f0ruQTF7/version/MsiyjxjP) | `mods/kerria-opt.pw.toml` |
| [Kotlin for Forge](https://modrinth.com/project/ordsPcFz) | Kotlin language support and development utilities. | [5.12.0](https://modrinth.com/project/ordsPcFz/version/uhJhCT7X) | `mods/kotlin-for-forge.pw.toml` |
| [Let Me Despawn](https://modrinth.com/project/vE2FN5qn) | Modified creature despawn rules intended to reduce unnecessary persistent creatures. | [1.5.0](https://modrinth.com/project/vE2FN5qn/version/fgcMDg9B) | `mods/lmd.pw.toml` |
| [Lionfish-API](https://modrinth.com/project/FoVacERa) | Lightweight animation support. | [3.1](https://modrinth.com/project/FoVacERa/version/fTRMVgyZ) | `mods/lionfish-api.pw.toml` |
| [Lithium](https://modrinth.com/project/gvQqBUqZ) | Game-logic optimization for single-player and multiplayer. | [mc1.21.1-0.15.4-neoforge](https://modrinth.com/project/gvQqBUqZ/version/DDUrRVCA) | `mods/lithium.pw.toml` |
| [Lithostitched](https://modrinth.com/project/XaDC71GB) | Shared world-generation configuration and compatibility support. | [1.8.0-neoforge-21.1](https://modrinth.com/project/XaDC71GB/version/sPmtDq1X) | `mods/lithostitched.pw.toml` |
| [Lodestone](https://modrinth.com/project/bN3xUWdo) | Shared code for Lodestar team projects. | [1.8.2](https://modrinth.com/project/bN3xUWdo/version/CohX6yP1) | `mods/lodestonelib.pw.toml` |
| [MaFgLib](https://modrinth.com/project/SKI34J7B) | Shared support for the Forge and NeoForge ports of masa's mods. | [0.4.3+mc1.21.1](https://modrinth.com/project/SKI34J7B/version/CgDQ0u0Q) | `mods/mafglib.pw.toml` |
| [MidnightLib](https://modrinth.com/project/codAaoxh) | Shared configuration support. | [1.9.3+1.21.1-neoforge](https://modrinth.com/project/codAaoxh/version/6Gv5jvTB) | `mods/midnightlib.pw.toml` |
| [Model Gap Fix](https://modrinth.com/project/QdG47OkI) | Fixes gaps in Block Models and Item Models. | [1.21-1.10](https://modrinth.com/project/QdG47OkI/version/X2U8ceG9) | `mods/modelfix.pw.toml` |
| [ModernFix](https://modrinth.com/project/nmDcB62a) | Performance, memory and bug-fix improvements. | [5.27.24+mc1.21.1](https://modrinth.com/project/nmDcB62a/version/5HLHxQ2F) | `mods/modernfix.pw.toml` |
| [Moonlight Lib](https://modrinth.com/project/twkfQtEc) | Shared registration, data-pack, villager activity and map-marker utilities. | [1.21.1-3.7.1](https://modrinth.com/project/twkfQtEc/version/YfHkk7hg) | `mods/moonlight.pw.toml` |
| [More Culling](https://modrinth.com/project/51shyZVL) | Rendering visibility optimizations. | [1.0.8](https://modrinth.com/project/51shyZVL/version/tFPgktUw) | `mods/moreculling.pw.toml` |
| [More RPG Library](https://modrinth.com/project/Wkc3lwHo) | Shared support for the More RPG Classes and More RPG Content series. | [2.7.2+1.21.1-neoforge](https://modrinth.com/project/Wkc3lwHo/version/aYw4LYyV) | `mods/more-rpg-library.pw.toml` |
| [MRU](https://modrinth.com/project/SNVQ2c0g) | Shared support for Cassian and IMB11's mods. | [1.0.19+LTS+1.21.1-neoforge](https://modrinth.com/project/SNVQ2c0g/version/qYqVf5jP) | `mods/mru.pw.toml` |
| [Neo Bee Fix](https://modrinth.com/project/DzSY371i) | Bee fixes. The short summary does not specify the individual defects. | [2.0.1](https://modrinth.com/project/DzSY371i/version/MUOGH4UT) | `mods/neo-bee-fix.pw.toml` |
| [Observable](https://modrinth.com/project/VYRu7qmG) | See what's lagging your server. | [5.4.4+neoforge](https://modrinth.com/project/VYRu7qmG/version/f8lSH3bs) | `mods/observable.pw.toml` |
| [oωo (owo-lib)](https://modrinth.com/project/ccKDOlHs) | General development, settings-screen and configuration library for Fabric and Quilt mods. | [0.12.15.5-beta.1+1.21](https://modrinth.com/project/ccKDOlHs/version/NMCHU6DZ) | `mods/owo-lib.pw.toml` |
| [Placebo](https://modrinth.com/project/tCkE8p2N) | Shared support for the author's mods, without independent gameplay content. | [1.21.1-9.9.2](https://modrinth.com/project/tCkE8p2N/version/1Ypo4tf4) | `mods/placebo.pw.toml` |
| [playerAnimator](https://modrinth.com/project/gedNE4y2) | Shared player animation support. | [2.0.4+1.21.1-forge](https://modrinth.com/project/gedNE4y2/version/HJZB6bmA) | `mods/playeranimator.pw.toml` |
| [Presence Footsteps x Sable (Aeronautics Compat)](https://modrinth.com/project/ZAhKrMSS) | Presence Footsteps compatibility for Sable and Create Aeronautics. | [1.0](https://modrinth.com/project/ZAhKrMSS/version/Mnm18kQK) | `mods/presence-footsteps-x-sable.pw.toml` |
| [Prickle](https://modrinth.com/project/aaRl8GiW) | Shared configuration-file support. | [21.1.11](https://modrinth.com/project/aaRl8GiW/version/EE1FHDyD) | `mods/prickle.pw.toml` |
| [Puzzles Lib](https://modrinth.com/project/QAGBst4M) | Supporting library. The project summary does not describe its functionality. | [21.1.62](https://modrinth.com/project/QAGBst4M/version/1TmfTuyw) | `mods/puzzles-lib.pw.toml` |
| [quick pack](https://modrinth.com/project/pSISfJ4O) | Optimize datapack and resourcepack zip file loading times. | [neoforge-1.5.1+1.21.1](https://modrinth.com/project/pSISfJ4O/version/yXZgoajP) | `mods/quick-pack.pw.toml` |
| [Ranged Weapon API](https://modrinth.com/project/AqaIIO6D) | Shared support for custom bows and crossbows. | [3.0.0+1.21.1-neoforge](https://modrinth.com/project/AqaIIO6D/version/WxNYN3Zh) | `mods/ranged-weapon-api.pw.toml` |
| [Resourceful Config](https://modrinth.com/project/M1953qlQ) | Shared cross-platform configuration support. | [3.0.11](https://modrinth.com/project/M1953qlQ/version/lSbyRD6v) | `mods/resourceful-config.pw.toml` |
| [Resourceful Lib](https://modrinth.com/project/G1hIVOrD) | Supporting library. The project summary provides no further detail. | [3.0.12](https://modrinth.com/project/G1hIVOrD/version/x99nCLTm) | `mods/resourceful-lib.pw.toml` |
| [Ritchie's Projectile Library](https://modrinth.com/project/B3pb093D) | Shared projectile support. | [2.1.2](https://modrinth.com/project/B3pb093D/version/hZ6B2Z0x) | `mods/rpl.pw.toml` |
| [Sable](https://modrinth.com/project/T9PomCSv) | A library mod for interactive moving block structures, or "sub-levels". | [2.0.6+mc1.21.1](https://modrinth.com/project/T9PomCSv/version/fg9dTRz9) | `mods/sable.pw.toml` |
| [Sable Beyond](https://modrinth.com/project/PrW3B4fH) | Sable Beyond expands the Sable mod with additional features, quality-of-life improvements, and compatibility support. It is designed to add ideas that are not part of the main mod while keeping the gameplay experience consistent with Sable. | [neoforge1.21.1+v0.4.1](https://modrinth.com/project/PrW3B4fH/version/JRq5Yypd) | `mods/sable_beyond.pw.toml` |
| [Sable: Cool Rain](https://modrinth.com/project/nUwwB5kx) | Compatibility addon that makes Cool Rain Reforged rain sounds work with Sable structures, Create copycats and other modded blocks. | [1.0.1+1.21.1+neoforge](https://modrinth.com/project/nUwwB5kx/version/3KLMffqk) | `mods/sable-cool-rain.pw.toml` |
| [Sable: Physics Compat](https://modrinth.com/project/sZbcIrJb) | Sable and Aeronautics compatibility tags for selected modded blocks. | [1.3.0](https://modrinth.com/project/sZbcIrJb/version/Ucq7afTi) | `mods/sablecompat.pw.toml` |
| [Searchables](https://modrinth.com/project/fuuu3xnx) | Shared search, filtering and completion support. | [1.0.2](https://modrinth.com/project/fuuu3xnx/version/iEE85X0w) | `mods/searchables.pw.toml` |
| [Shield API](https://modrinth.com/project/y9clIFY4) | Shared support for shields with custom models. | [2.2.0-neoforge](https://modrinth.com/project/y9clIFY4/version/fgK2cNYi) | `mods/shield-api.pw.toml` |
| [Sinytra Connector](https://modrinth.com/project/u58R1TMW) | Allows supported Fabric mods to run on NeoForge. | [2.0.0-beta.17+1.21.1](https://modrinth.com/project/u58R1TMW/version/IITF0PRC) | `mods/connector.pw.toml` |
| [Sodium](https://modrinth.com/project/AANobbMI) | Replacement rendering engine intended to improve frame rate and reduce stutter. | [mc1.21.1-0.8.13-neoforge](https://modrinth.com/project/AANobbMI/version/uMOpc5uV) | `mods/sodium.pw.toml` |
| [Sophisticated Core](https://modrinth.com/project/nmoqTijg) | Shared support for Sophisticated mods. | [1.21.1-1.5.5.2363](https://modrinth.com/project/nmoqTijg/version/nSoNwJfm) | `mods/sophisticated-core.pw.toml` |
| [spark](https://modrinth.com/project/l6YH9Als) | Performance profiling for clients and servers. | [1.10.124-neoforge-1.21.1](https://modrinth.com/project/l6YH9Als/version/v5qtqRQi) | `mods/spark.pw.toml` |
| [Spawn Animations Compats](https://modrinth.com/project/ofDka6PS) | Additional mod compatibility for Spawn Animations. | [18.0+mod](https://modrinth.com/project/ofDka6PS/version/AyNBs0vr) | `mods/spawn-animations-compats.pw.toml` |
| [Spell Engine](https://modrinth.com/project/XvoWJaA2) | Data-driven magic framework used by content addons. | [1.10.7+1.21.1-neoforge](https://modrinth.com/project/XvoWJaA2/version/wKITXgNx) | `mods/spell-engine.pw.toml` |
| [Spell Power Attributes](https://modrinth.com/project/8ooWzSQP) | Spell-related attributes, effects and enchantment support. | [1.6.0+1.21.1-neoforge](https://modrinth.com/project/8ooWzSQP/version/RFCD8Aio) | `mods/spell-power.pw.toml` |
| [Structure Layout Optimizer](https://modrinth.com/project/ayPU0OHc) | Optimization for structure layout and piece generation. | [1.0.12+1.21.1-neoforge](https://modrinth.com/project/ayPU0OHc/version/eTz03Gfd) | `mods/structure-layout-optimizer.pw.toml` |
| [Structure Pool API](https://modrinth.com/project/LrYZi08Q) | Shared support for adding structures to structure pools. | [1.2.1+1.21.1-neoforge](https://modrinth.com/project/LrYZi08Q/version/kdWVYKdx) | `mods/structure-pool-api.pw.toml` |
| [Teal Lib](https://modrinth.com/project/rLJ1qF79) | Supporting library. The summary does not specify its individual utilities. | [1.3.teal](https://modrinth.com/project/rLJ1qF79/version/lZTBRemW) | `mods/teallib.pw.toml` |
| [Waystones: Sable (Create Aeronautics Addon)](https://modrinth.com/project/BxhPGfcK) | Waystones compatibility for Sable moving structures, including teleportation, validation, distance and synchronization fixes. | [1.0.7](https://modrinth.com/project/BxhPGfcK/version/Wot8Pf4C) | `mods/waystones-sable.pw.toml` |
| [YetAnotherConfigLib (YACL)](https://modrinth.com/project/1eAoo2KR) | Shared configuration library. | [3.8.2+1.21.1-neoforge](https://modrinth.com/project/1eAoo2KR/version/7TVdVtxF) | `mods/yacl.pw.toml` |
| [YUNG's API](https://modrinth.com/project/Ua7DFN59) | Shared support for YUNG's mods. | [1.21.1-NeoForge-5.1.9](https://modrinth.com/project/Ua7DFN59/version/2prKITKh) | `mods/yungs-api.pw.toml` |

## Resource packs and shader packs

These are selected visual content, counted separately from mods. Mandala is already added and enabled in the supplied context; this proposal does not change its ordering or settings. Selection alone does not establish that a shader is active. Resource-pack ordering, animation support, shader appearance and performance remain outside this planning task.

### Resource packs

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [(Bee's) Fancy Crops](https://modrinth.com/project/UGEVQ6t9) | Decorative crop appearance with advertised mod support. | [1.3](https://modrinth.com/project/UGEVQ6t9/version/ZJEBZjg6) | `resourcepacks/fancy-crops.pw.toml` |
| [Attribute Icons (RPG Series)](https://modrinth.com/project/73QpzsIN) | Icons in attribute names. | [1.4](https://modrinth.com/project/73QpzsIN/version/it8xKo5G) | `resourcepacks/attribute-icons-rpg-series.pw.toml` |
| [Fresh Animations](https://modrinth.com/project/50dA9Sha) | Animated creatures with changed movement and expressions. | [1.10.4](https://modrinth.com/project/50dA9Sha/version/xN57JJts) | `resourcepacks/fresh-animations.pw.toml` |
| [Fresh Animations: Objects](https://modrinth.com/project/23O9JVMV) | Animations for non-creature entities in Fresh Animations' style. | [2.1.2](https://modrinth.com/project/23O9JVMV/version/AIGgXNdl) | `resourcepacks/fresh-animations-objects.pw.toml` |
| [Fresh Animations: Player Extension](https://modrinth.com/project/TAIMVZCL) | Player animations in Fresh Animations' style. | [1.1.0](https://modrinth.com/project/TAIMVZCL/version/Wj7NeGjP) | `resourcepacks/fa-player-extension.pw.toml` |
| [Fresh Animations: Quivers](https://modrinth.com/project/T4pK4GiQ) | Skeleton quivers compatible with Fresh Animations. | [2.2.0](https://modrinth.com/project/T4pK4GiQ/version/RLEhLx95) | `resourcepacks/fresh-animations-quivers.pw.toml` |
| [Mandala's GUI - Dark mode](https://modrinth.com/project/h6zxsNVF) | A dark interface theme without changes to item or block textures. | [2.1](https://modrinth.com/project/h6zxsNVF/version/Z2ajDlEE) | `resourcepacks/mandalas-gui-dark-mode.pw.toml` |
| [Motschen's Better Leaves](https://modrinth.com/project/uvpymuxq) | Changed leaf appearance. | [9.5](https://modrinth.com/project/uvpymuxq/version/XWtayRKd) | `resourcepacks/better-leaves.pw.toml` |
| [Simple Grass Flowers](https://modrinth.com/project/ti9KkMHm) | Decorative flowers, clovers and rocks on selected ground textures. | [1.9.6](https://modrinth.com/project/ti9KkMHm/version/BFqp4P2V) | `resourcepacks/simple-grass-flowers.pw.toml` |
| [Visual Effects+](https://modrinth.com/project/ZyZknBVG) | Biome-dependent colored fog, particles and weather visuals. | [1.3.1](https://modrinth.com/project/ZyZknBVG/version/MgC4Oa2v) | `resourcepacks/visual-effects-plus.pw.toml` |

### Shader packs

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Complementary Shaders - Reimagined](https://modrinth.com/project/HVnmMxH1) | Minecraft-oriented shader visuals. | [r5.9.3](https://modrinth.com/project/HVnmMxH1/version/Bqen1mJX) | `shaderpacks/complementary-reimagined.pw.toml` |
| [Complementary Shaders - Unbound](https://modrinth.com/project/R6NEzAwj) | A more transformed shader visual style. | [r5.9.3](https://modrinth.com/project/R6NEzAwj/version/B1kyfoUZ) | `shaderpacks/complementary-unbound.pw.toml` |
| [Photon Shaders](https://modrinth.com/project/lLqFfGNs) | Gameplay-focused shaders with a semi-realistic style. | [v1.3b](https://modrinth.com/project/lLqFfGNs/version/gUv7fBPN) | `shaderpacks/photon-shader.pw.toml` |

## Deferred branch inventories

These inventories were read from Git trees without switching, changing or merging branches. They show additional selected projects relative to the Chunky baseline, not content installed in the baseline. They do not establish that the branches are interchangeable or runtime-compatible.

### Northstar group

Source branch `grouped/northstar` at `bb7575a079fafec9899e97bd26d981526a35f386`. The five additional projects are a future space and vehicle-transfer route. Write a separate introduction only when this branch is chosen and its survival acquisition and transfer ownership have been verified. The compatibility project summary explicitly says its Dimensional Drive has no crafting recipe; do not present it as an ordinary survival milestone. Overlapping transfer claims are not proof that both mechanisms should operate together.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Create: AeroWarptics](https://www.curseforge.com/minecraft/mc-mods/create-aerowarptics) | Airship relocation through a rotationally powered Rift Drive, according to the CurseForge project page. | [aerowarptics-1.3.0.jar](https://www.curseforge.com/minecraft/mc-mods/create-aerowarptics/files/8787426) | `mods/create-aerowarptics.pw.toml` |
| [Create: Northstar - Redux](https://modrinth.com/project/UZiq3QVW) | Space-exploration content for Create. | [0.6.6+1.21.1](https://modrinth.com/project/UZiq3QVW/version/2xMVbJcV) | `mods/northstar-redux.pw.toml` |
| [Create: Northstar-Aeronautics Compatibility](https://modrinth.com/project/Mit4b2tJ) | A Dimensional Drive that selects a Northstar planet and transfers a physics contraption with its player. The current project summary says no crafting recipe is provided. | [3.0.0](https://modrinth.com/project/Mit4b2tJ/version/Y91G3nhq) | `mods/create-northstar-aeronautics-compatibility.pw.toml` |
| [Northstar Sable Iris Horizons Bridge](https://modrinth.com/project/MSoLk54A) | Northstar sky and distant-terrain rendering compatibility, plus advertised Sable transfers between planets and orbit. | [0.6.4+1.21.1](https://modrinth.com/project/MSoLk54A/version/kaxeIMPF) | `mods/northstar-sable-iris-horizons-bridge.pw.toml` |
| [Paxi](https://modrinth.com/project/CU0PAyzb) | Automatic loading of data packs and resource packs. | [1.21.1-NeoForge-5.1.3](https://modrinth.com/project/CU0PAyzb/version/CLZfFbCx) | `mods/paxi.pw.toml` |

Compared with the current Chunky tree, this branch also lacks `mods/hide-experimental-warning.pw.toml` and `resourcepacks/mandalas-gui-dark-mode.pw.toml`. These absences must remain visible in branch availability; the branches are not simply the entire current baseline plus these additions.

### Optimizer group

Source branch `grouped/optimizers` at `ba3fe12fa90d474cb1308f0a6030d759455ea99d`. The three additional projects are technical-only candidates. They do not introduce a player progression route. No performance or stability claim is established by their selection.

| Selected project and source | Purpose | Selected release | Metadata |
| --- | --- | --- | --- |
| [Async Logger](https://modrinth.com/project/zvNzKfGF) | Asynchronous logging and message filtering. | [2.2.2+1.21.1-neoforge](https://modrinth.com/project/zvNzKfGF/version/yj7KaIVy) | `mods/asynclogger.pw.toml` |
| [Jasione](https://modrinth.com/project/qlDkBPij) | Reduces memory allocation from enumeration value-array cloning through bytecode analysis. | [1.0.9+1.21.1-neoforge](https://modrinth.com/project/qlDkBPij/version/GsGw7K8F) | `mods/jasione.pw.toml` |
| [ServerCore](https://modrinth.com/project/4WWQxlQP) | Server optimization. | [1.5.19+1.21.1](https://modrinth.com/project/4WWQxlQP/version/6N9hXiRa) | `mods/servercore.pw.toml` |

Compared with the current Chunky tree, this branch also lacks `mods/hide-experimental-warning.pw.toml` and `resourcepacks/mandalas-gui-dark-mode.pw.toml`. These absences must remain visible in branch availability; the branches are not simply the entire current baseline plus these additions.

## Verification and limitations

A programmatic inventory check parsed every selected metadata file, assigned one primary category per baseline mod, reconciled the generated baseline inventory paths with the source set, and rejected duplicates or omissions. It confirmed 297 unique baseline mod paths, 10 unique resource-pack paths and 3 unique shader-pack paths. All 310 baseline paths appear exactly once in inventory rows. The deferred extras are five Northstar paths and three optimizer paths, with no baseline paths counted as additions.

All Modrinth batch requests succeeded, yielding 316 distinct project records and 316 selected-version records across baseline content and deferred additions. The remaining two projects were grounded in their CurseForge pages. Baseline metadata was byte-identical to the declared Chunky source tree. Counts here refer to selected pack metadata, not the number of runtime-loaded components or nested libraries.

This task did not inspect mod archives, inspect every configuration value, run Minecraft, test recipes, test controls, verify addon Ponder coverage, validate visual-pack compatibility or implement any guidance in the game. Exact operating instructions and balance statements still need selected-release evidence. Existing books beyond the explicitly documented sources remain unconfirmed. Current Modrinth summaries describe project intent and can differ from the selected artifact.

No pack definitions, settings, branches or commits were changed. The deliverable is this proposal and categorized inventory, not a published in-game handbook.
