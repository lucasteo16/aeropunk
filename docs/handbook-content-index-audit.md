# Astropunk handbook content index audit

## Findings

The handbook covers the selected content roster, but it does not yet provide a wiki-like inventory of the game. Its broad topic pages mostly identify mods rather than individual bosses, creatures, structures, equipment or recipes. Complete mod coverage must not be reported as complete gameplay coverage.

The first authoring priority is what exists in the game and where to find it. Example activities and builds follow that inventory. This report changes no handbook pages, layouts, schemas, pack selections or launcher state.

## Verified snapshot

| Measure | Verified result |
| --- | --- |
| Current branch | test/guide |
| Selected content entries reconciled with pack index | 292 |
| Selected mod metadata entries | 285 |
| Selected local handbook helper | 1 jar |
| Selected downloadable resource packs and shaders | 3 resource packs and 3 shaders |
| Separate unselected content | 20 heavy-edition entries and 8 deferred entries |
| Manifest articles | 84 |
| Articles marked drafted | 14 |
| Articles not drafted | 70 |
| Authored source entries | 15, comprising 14 articles and one area catalog |
| Generated Markdown pages | 95 in each locale |
| English pages with Work in progress marker | 70 |
| Selected downloadable artifacts resolved and checksummed | 291 |

Every selected content metadata path or local helper path appears in the manifest, and every baseline manifest path appears in the current index. English and Simplified Chinese filenames match. These checks establish selection and page presence, not entity coverage, translated meaning, source navigation reachability or working gameplay.

The manifest reports 318 indexed entries across its 320-entry combined roster. Its per-provider fields for written player mention, verified instructions, written English, written Simplified Chinese and checked links are all false. These fields are not a usable completion measurement: authored articles and visible publisher summaries exist despite the false fields. Keep article drafting, provider visibility, named content coverage, translation and gameplay verification as separate measures.

## Evidence and limits

The authoritative installed selection is index.toml plus the current packwiz metadata. The separately named Modrinth profile was not changed or used to override selections. Native packwiz cache index rows resolve the declared artifact digest to the cache SHA256 address. All 291 selected downloadable artifacts were checked against their declared digest before inspection. No artifacts were downloaded or installed.

The machine-readable companion contains the complete 320-entry selection roster, all 84 article mappings, exact selected artifact names and hashes for inspected content providers, 229 packaged worldgen structure definitions, placement references, raw entity resource evidence, 13 explicitly tagged bosses and nine prioritized gap groups. The 229 figure counts matching structure-definition files across the selected downloadable artifacts. It is not the number of structures that can actually generate. Incendium filters, disabled configuration, unused definitions, generation rules, built-in packs and vanilla content prevent that interpretation.

Structures, placement sets, template pools and structure templates are different counting units. A single placement grid can choose among many structures. Room templates are pieces, not separate dungeons. An entity translation can name a projectile, message or profession rather than a living creature. A spawn egg model can be unused. No total living-mob, cosmetic-variant, dungeon-layout or player-spell count is claimed.

No game was launched. Loaded registry state, pack precedence, natural spawning, summoning, drops, effective recipes, rendered pages, existing chunks and world configuration overrides remain unverified. No save-derived boss defeat state is inferred.

Concurrent handbook work changed the full pack index during this audit. The selected artifact paths and their complete index entries were rechecked at completion and remained unchanged. The manifest and authored source hashes remained unchanged. Companion source hashes record the inspected starting snapshot.

## Priority 0. Boss and encounter index

Existing reference: adventure.bosses.md, Challenging encounters. It is unwritten and contains four provider summaries. Dangerous is a balancing layer, not evidence of an additional boss collection. Illager Invasion and the creature-page providers require a separate encounter review.

Two selected releases expose concrete boss tags and matching kill-all-bosses advancement criteria. They provide the following starting catalog, not a whole-pack boss total.

| Provider | Exact selected release | Tagged boss entries |
| --- | --- |
| Bosses'Rise | block_factorys_bosses-2.1.2-neo-1.21.1.jar | Ashlord, The Infernal Dragon, Skor, The Yeti, Sirok, The Sandworm, Helvar, the Underworld Knight, Nerakyss, The Kraken |
| L_Ender's Cataclysm | L_Ender's Cataclysm 1.21.1-3.33.jar | Ignis, Netherite Monstrosity, Ender Guardian, The Harbinger, The Leviathan, Ancient Remnant, Maledictus, Scylla |

Bosses'Rise has five tagged bosses: Ashlord, Skor, Sirok, Helvar and Nerakyss. L_Ender's Cataclysm has eight tagged bosses. The tag and advancement evidence establishes these exact named entries in the selected releases. It does not include every miniboss, older entity, pet, summon or vanilla encounter.

Bosses'Rise also packages Sandworm Nest, Dragon Tower, Underworld Arena, Yeti Hideout and Kraken Ship definitions. Cataclysm packages 15 definitions, including Burning Arena, Ruined Citadel, Soul Black Smith, Ancient Factory, Sunken City, Cursed Pyramid, Frosted Prison and Acropolis. These are identifier-derived labels; canonical player-facing structure names and boss-to-arena mappings need verification. Do not infer each boss's dimension, arena or summoning item solely from these names.

Next catalog work:

- Give each tagged boss one row with name, provider, dimension, biome or arena, encounter access, summoning or activation, repeat encounter rules, variants and reward sources.
- Audit Invoker in Illager Invasion and Wildfire in Friends and Foes as additional encounter candidates. Their named entity resources and released classes exist; their classification and access rules were not traced here.
- Add Cataclysm minibosses and ordinary enemies as separate entries rather than treating all spawn eggs or all entities in a boss-related class folder as major bosses.
- Include vanilla encounters separately and verify how installed mods alter them. Do not make the 13 tagged mod entries the whole-game checklist.
- Place an informational boss checklist in Quick reference, cross-linked to adventure.bosses.md and adventure.structures.md. It must remain freely accessible, with no quest gating or personalized defeat progress inferred from saves.

## Priority 0. Creature and variant index

Existing reference: adventure.creatures.md. It lists Creeper Overhaul, Enderman Overhaul, Friends and Foes, Spawn and Variants and Ventures, but contains no per-creature inventory. Bosses and furniture pages hide additional creature providers.

| Provider | Exact selected release | Readily verified scope |
| --- | --- |
| Creeper Overhaul | 4.0.6 | 16 creeper identifier constants in released ModEntities with matching English entity labels |
| Enderman Overhaul | 2.0.3 | 21 enderman identifier constants in released ModEntityTypes, including three pet types |
| Friends and Foes | 4.0.27 | 10 spawn egg model resources, four structure definitions; professions and player illusions also appear among raw entity labels |
| Spawn | 4.0.8 | 27 spawn egg model resources and eight structure definitions; multiple color, shape and pattern labels occur within creature families |
| Variants and Ventures | 1.0.28 | Four named entity labels and matching egg models: Gelid, Murk, Thicket and Verdant |
| Illager Invasion | 21.1.6 | 12 egg model resources and five structure definitions; an Illusioner egg exists although its label is not among the 11 namespaced English entity labels |
| Bosses'Rise | 2.1.2 | 14 egg model resources, including bosses and supporting enemies |
| L_Ender's Cataclysm | 3.33 | 40 egg model resources and 102 raw entity-prefixed translation keys, including effects, projectiles and messages |
| Supplementaries | Current exact filename and hash in companion | Named Plunderer and Red Merchant resources, plus Galleon and Road Sign structure definitions |

Creeper Overhaul contains a plains_creeper_spawn_egg model without a corresponding plains_creeper identifier in the inspected registration class. Counting its 17 egg models as 17 registered creeper variants would be wrong. Enderman Overhaul has 18 non-pet enderman identifiers and three pet identifiers; scarab, spirit and projectile types must remain separate. These are released identifier observations, not a verified natural-spawn census.

Spawn supplies named fish and coastal creatures such as Tuna, Herring, Seahorse, Clam, Coastal Crab, Spider Crab, Seal and Sea Cow. Its packaged English descriptions include habitat, capture, taming and utility information. Those descriptions are useful exact-release source material, but their habitat text does not replace inspecting spawn rules. Clam base, color and pattern labels must not be multiplied into an assumed supported variant total.

Each creature row needs disposition, dimension, biome or structure and spawn conditions, taming, breeding, drops, food or utility links, plus explicit distinction between a separate entity type and a cosmetic variant. Include vanilla mobs and changes from installed combat or difficulty systems without presenting changed behavior as a new species.

## Priority 0. Structures and dungeon variants

Existing references: adventure.structures.md, adventure.settlements.md and world.dimensions.md. The first two are unwritten. The dimension page summarizes terrain providers but does not inventory their structures. The structures page maps nine mods only, omitting providers filed under bosses, creatures, furniture and magic.

| Selected provider | Packaged structure definitions | Packaged placement sets | Important distinction |
| --- | --- | --- | --- |
| Bosses'Rise | 5 | 5 | Packaged definitions only; effective generation not verified |
| ChoiceTheorem's Overhauled Village | 78 | 0 | 66 village definitions across three sizes, plus 12 outposts; configuration narrows this |
| Friends&Foes (Forge/NeoForge) | 4 | 4 | Packaged definitions only; effective generation not verified |
| Illager Invasion | 5 | 5 | Packaged definitions only; effective generation not verified |
| Incendium Legacy | 9 | 3 | Selected Biomes Only filter targets these resources; do not advertise as available |
| L_Ender's Cataclysm | 15 | 11 | Packaged definitions only; effective generation not verified |
| Nullscape | 2 | 3 | Rift and Dragon Skeleton; three sets do not mean three new definitions |
| Spawn | 8 | 8 | Packaged definitions only; effective generation not verified |
| Supplementaries | 2 | 2 | Galleon and Road Sign currently mapped to furniture |
| Terralith | 28 | 7 | Includes mage towers, villages, underground sites and rubble, not only biomes |
| When Dungeons Arise | 40 | 2 | 40 definitions share two placement sets; not 40 independent grids |
| Witcher (RPG Series Plus) | 8 | 1 | Eight ruins, hideout and grave definitions currently mapped to magic roles |
| YUNG's Better Desert Temples | 1 | 1 | Packaged definitions only; effective generation not verified |
| YUNG's Better Dungeons | 5 | 5 | Small Nether Dungeon disabled in repository configuration |
| YUNG's Better Jungle Temples | 1 | 1 | Packaged definitions only; effective generation not verified |
| YUNG's Better Mineshafts | 13 | 1 | 13 material or biome variants share one placement set |
| YUNG's Better Nether Fortresses | 1 | 1 | Packaged definitions only; effective generation not verified |
| YUNG's Better Ocean Monuments | 1 | 1 | Packaged definitions only; effective generation not verified |
| YUNG's Better Strongholds | 1 | 1 | Packaged definitions only; effective generation not verified |
| YUNG's Better Witch Huts | 2 | 2 | Packaged definitions only; effective generation not verified |

Concrete variant groups:

- YUNG's Better Dungeons defines Skeleton Dungeon, Zombie Dungeon, Spider Dungeon, Small Dungeon and Small Nether Dungeon. Only the last has an explicit disabled switch in the inspected repository configuration. Do not describe all five as enabled encounters.
- YUNG's Better Mineshafts defines acacia, desert, dripstone, ice, jungle, lush, mesa, mushroom, oak, overgrown, red desert, spruce and snowy spruce variants. The exact identifiers and biome selectors are in the companion.
- YUNG's Better Witch Huts defines Witch Hut and Witch Circle. The latter is easy to miss when summarizing only the mod title.
- When Dungeons Arise defines 40 structures, including airships, ships, mines, temples, towers and settlements. The companion preserves every identifier, biome selector, structure definition and placement reference. They are not 40 dungeon-room variants.
- ChoiceTheorem's Overhauled Village defines 22 village families in each of small, medium and large sizes, plus 12 outpost definitions. Repository configuration enables 21 named village families and all three sizes, excludes the underground family from its named list, and disables its outposts. That produces 63 configured family-and-size combinations, not a proven count of generated villages.
- Gazebos packages 17 structure templates and Village Taverns packages five. Neither contributes a standalone worldgen structure definition in this scan. These are village additions, not 22 independent destination structures.
- Spawn defines Ant Mount, Cold Island, Dodo Island, Octopolis, Sandy Island, Tide Pool, Tropical Island and Volcanic Island identifiers. Friends and Foes defines Citadel, Iceologer Cabin, Illusioner Shack and Illusioner Training Grounds.
- Illager Invasion defines Firecaller Hut, Illager Fort, Illusioner Tower, Labyrinth and Sorcerer Hut. Distinguish its Illager Fort from the different When Dungeons Arise identifier.

Incendium Legacy packages nine structure definitions, but the selected Incendium Biomes Only artifact contains a built-in pack filter targeting Incendium structures, placement sets, template pools, encounter functions and related resources. The current dimension article already describes their removal. Keep these nine as filtered source evidence, not advertised encounters. Runtime activation and precedence of that built-in filter were not inspected.

The structure index must include provider and identifier, dimension, biome tags resolved to player-facing names, height or depth, entrance or access, encounters, loot sources, placement and configuration status, and family variants. Room pools and templates belong beneath their parent structure. No count of all possible procedurally assembled layouts is available. Include vanilla structures and verify which are replaced, supplemented or disabled.

## Priority 1. Equipment, spells and character systems

Existing references: equipment.weapons-armor.md, equipment.accessories.md, combat.martial.md and combat.magic.md are unwritten. combat.skills.md is authored but describes interfaces rather than individual nodes or abilities.

Installed equipment providers include Armory, Arsenal, Jewelry, Additional Jewelry, Relics and More Relics, plus class and boss providers. Curios supplies equipment slots. Equipment display mods change presentation rather than establish another equipment roster.

Installed martial and magic providers include Archers, Archers Expansion, Rogues and Warriors, Berserker, Forcemaster, Wizards, Paladins and Priests, Elemental Wizards, Bard, Witcher and Runes. Skill Tree, More RPG Classes Skill Tree and Pufferfish's Skills require independent node catalogs and point-system descriptions. Spell Engine and Spell Power supply supporting systems.

The exact artifacts expose spell-definition files: Archers 6, Wizards 25, Paladins and Priests 15, Rogues and Warriors 12, Elemental Wizards 39, Bard 24, Berserker 7, Forcemaster 9 and Witcher 84. Additional selected artifacts also contain spell files, including equipment triggers, library definitions and hundreds of skill-tree entries. These are scoped packaged-file counts, not counts of selectable player spells. Every observed source path and provider count is preserved in the companion.

Equipment rows need item name and identifier, mod, slot, role or school, tier or set, attributes, effects and crafting or loot acquisition. Spell and skill rows need name and identifier, school, active or passive classification, granting item or node, learning source, costs, cooldown, targeting and effects. Class and boss reward integration must be verified rather than assumed.

## Priority 2. Building, vehicles and food

| Inventory | Current references | Installed provider scope and missing content |
| --- | --- | --- |
| Building materials and shapes | building.palette.md, building.factory.md, building.copycats.md, building.architecture.md | Chipped, Chipped Express, Every Compat, Stone Zone, Create decoration addons, Copycats+, Macaw architecture and Diagonal Fences. Copycats article is orientation only; no shape or material family catalog. |
| Furniture, displays and tools | building.furniture.md, building.displays.md, building.placement.md, building.safety.md | Handcrafted, Supplementaries, Amendments, Beautify, Decorative Food, Interiors, display tools, schematic tools and lighting tools. Inventory block families, tool modes and source workstations separately. |
| Vehicle components | vehicles.assembly.md, vehicles.airships.md, vehicles.engines.md, vehicles.controls.md, vehicles.radar.md, vehicles.weapons.md, vehicles.water.md | Aeronautics, Ballast, Aeroengine, Propulsion Simulated, Aeroworks, Tweaked Controllers, Radars, Big Cannons and Deep Seas. All seven topics are unwritten. Start with real components, fuels, controls and assembly requirements rather than invented vehicle entity classes. |
| Rail and local transport | transport.passenger.md, transport.railway-builder.md, transport.local.md | Railways Navigator, Blocks and Bogies, Steam and Rails, Escalated and Hypertube. List track, bogie, station, passenger and local transit systems before sample networks. |
| Ingredients and dishes | food.utensils.md, food.nether.md, food.end.md, food.underground.md, food.encounters.md, food.machine-cooking.md | Farmer's Delight, My Nether's Delight, End's Delight, Miner's Delight, Cataclysm Delight, Central Kitchen and Slice and Dice. Only utensils is authored among these; it does not list all meals. |
| Gathering, catches and food rules | food.growing.md, food.fishing.md, food.hunger.md | Farming tools and Create Integrated Farming, plus Spawn wildlife and fish. Fishing has no mapped providers. Hunger article names AppleSkin, Short Stacks and Spice of Life Onion without cataloging meal values or dietary rules. |

Building rows need material, shape, color or finish, crafting workstation, modes and relevant compatibility. Vehicle rows need component, vehicle family, assembly conditions, fuel or power, controls, passengers, storage and evidence for moving-structure support. Food rows need ingredient source, recipe type, heat, container, hunger, saturation, dietary contribution, stack limit and supported machine processing. Shared ingredients do not prove identical food properties or integration.

Northstar and space transfer bridges are deferred selections. Heavy-only visuals are not baseline gameplay. Neither group belongs in the installed-content catalog, though separate labeled references remain useful.

## Priority 3. Machines, resources and storage

The existing ore-processing article verifies a few Create examples, not the full machine or resource catalog. Rotation, logistics, renewable resources, enchanting, trading, electricity, industry, burners and stored rotation remain unwritten. Installed providers include Create and its mapped addons, Electro Energetics, TFMG Community Edition and Springs. Inventory machine inputs, outputs, processing types, power, resource acquisition and native Ponder help before writing sample factory projects.

Portable storage is authored only as an orientation page. Backpacks, reinforced shulker boxes and workshop vaults need separate capacities, upgrades, recipes and access conditions. Native recipe-browser lookup and Ponder are supporting references, not substitutes for a named content index.

## Inventory contract and completion criteria

Every content row should carry the same minimum fields:

- English and Simplified Chinese names, exact identifier, provider and selected release.
- Installed, heavy-only, deferred, disabled or filtered availability, with the evidence source.
- Dimension, biome, structure or other spawn location as appropriate.
- Access, acquisition, activation or summoning requirements.
- Variants with their counting unit, distinguishing entity types, cosmetic appearances, structure families, size variants and room pieces.
- Primary handbook reference and substantial mechanics links.
- Evidence and verification state for each material claim; unknown values remain unknown.

The companion uses null for unresolved names, dimensions, access and variants instead of filling them from plausible names. Its structure inventory contains exact biome selectors and raw definitions that can support later verification. Its raw labels and egg models are evidence queues, not ready-made player catalog entries.

A domain is complete only after its selected providers and their exact-release named content have been reconciled, relevant configuration and data-pack overrides applied, every entry placed once in the primary catalog, and both locales checked. Provider coverage and article drafting must remain separate from this denominator. No domain-wide completion percentage can be justified from the current evidence.

## Source references

- docs/handbook-authoring-standard.md, authoring and source ownership rules.
- docs/handbook-draft-manifest.json, 84 topic mappings and 320 combined roster entries.
- docs/handbook-content.json, authored bilingual source entries.
- index.toml and selected mods, resourcepacks and shaderpacks metadata, authoritative current selection.
- Generated handbook sources under resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook, observed page contents and locale filenames.
- config/ctov-common.toml and config/betterdungeons-neoforge-1_21.toml, configured exclusions.
- Exact released artifact paths, filenames, declared hashes and packaged source paths recorded in docs/handbook-content-index-audit.json.

Repository research provides background on creature and integration choices, but historical candidate or installation reports were not used to replace current selections or invent a completed entity list.
