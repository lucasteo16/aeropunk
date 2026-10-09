# Astropunk handbook authoring standard

This is the authoring contract for every handbook update. It belongs to repository documentation, not the distributed game resources. Read it before writing, translating or restructuring a page.

## Purpose and organization

The handbook prioritizes a content index: answer what exists in the installed game before describing what players can do with it. A mod roster alone is not a complete content index. Catalog actual bosses, creatures, structures, dungeon variants, equipment, spells, foods, building families, vehicles and destination types. Mechanics and crafting tutorials are secondary. Reuse existing recipe tools and Ponder rather than duplicating their instruction. Do not organize the entire book around player intentions.

The home is Astropunk. Quick reference comes first for important cross-cutting information such as Controls, Item recipe, Dimensions, Maps, Character skills, and Food and hunger. Mod catalogs follows for installed feature areas. Use matching icon-and-label table rows for both sections, rather than an arbitrary strip of three links above the catalogs. The left navigation mirrors this structure with Quick reference and Mod catalogs as ordered roots. Reference topics have one primary parent; mod catalogs cross-link those same pages rather than duplicating them. Use no more than two category levels before an article. Give each topic one primary home and use cross-links for related areas. Include supporting libraries in the same consistent reference structure, without presenting them as gameplay features.

The handbook is freely accessible. Do not add quests, completion rewards, progression locks or compulsory reading sequences. Actual mod gameplay requirements still apply and must be described accurately.

## Page types and section order

| Type | Required structure |
| --- | --- |
| Home | Astropunk title, Quick reference section first, separator, then Mod catalogs; matched two-column navigation tables with decorative inline icons |
| Area catalog | Title, area-specific mod heading such as Automation Mods, functional subgroups with icon, linked name and concise purpose, then Mechanics links; uninstalled content separated when relevant |
| Reference catalog | Title, second-level sections for actual entries such as Overworld, Nether and End; put short mod summaries and visuals in the catalog itself; link out only to substantial mechanics |
| Getting started | Inside its reference topic when short; name the first prerequisite, item, workstation or interface, then point to native recipes, Ponder or existing help; no exhaustive walkthrough |
| Controls article | Access instructions, current bindings, clearly labeled defaults, rebinding and conflict instructions |

The first-level heading supplies the toolbar title. No prose, image, table, status marker or navigation may sit directly below it. The body must begin with a second-level heading, and every later section must remain beneath a second-level heading. Third-level headings may subdivide a section.

Use the matching file in docs/handbook-templates as a starting point. Omit sections that add nothing; do not insert empty headings or generic introductory paragraphs to satisfy a template. A dimension catalog does not need a crafting recipe. A library reference does not need a demonstration.

## Visual and text conventions

Lead with actual item models, native recipe displays, verified comparisons or authentic game captures. Publisher icons and screenshots are allowed. Download them into the guide source images folder, convert to supported image formats, record source URLs, publisher identity, checksum and license metadata in docs/handbook-visual-sources.json, and use a short subject caption. Do not add publisher screenshot boilerplate to player-facing captions; retain attribution and provenance in repository notes, and never imply they show this instance. Prefer clean terrain and interface screenshots over marketing banners and do not substitute decorative item icons for missing landscape images. GuideME scales ordinary images to one quarter of their pixel dimensions, so 96-pixel publisher icons produce compact 24-pixel guide images. Verify dimensions and do not invent sizing attributes. Text explains the visual rather than replacing it. Generated art may decorate a background or theme, but never explains a machine, recipe or gameplay procedure.

Use native item slots for actual item instruction, with item names and hover tooltips. For topics and catalog navigation, use decorative ItemImage beside the linked label instead: it has fixed icon dimensions and no item tooltip. Do not invent a hide-tooltip attribute on ItemGrid. ItemGrid expands to the available width, which can force a nearby label onto a new line; avoid it for inline navigation. Label unfamiliar icons visibly when identifying them is necessary to understand the page; a hover name is a supplement, not the only instruction. Keep input, tool or processing medium, and output distinct. A water-bucket icon used to represent water must not imply that the recipe consumes a bucket.

Use native recipes only for types the selected renderer supports. For unsupported processing types, show verified item visuals and concise output data. State quantities and chances exactly. Record the source artifact and recipe identifier in authoring evidence, not as an intrusive player-facing disclaimer. Never substitute an illustrative scene for a working arrangement without identifying what it depicts.

Keep an introduction to one sentence when possible. Prefer short labels, comparison tables and brief instructions. Explain one mechanic per section. Add numbered steps only when order matters. Avoid dense prose, repeated warnings, large icon-title-description stacks and unqualified claims that all machines or containers behave identically.

Reuse Create Ponder for supported assembly and operation. Identify the relevant item and its help entry rather than rebuilding an existing demonstration. Write bespoke explanation when existing help does not cover the mechanic or interaction.

## Shared topic structure

Use one topic tree and two complementary page types: Reference and Getting started. The reference page is the landing page and inventories what exists, variants, locations and access. Put a short Getting started section beneath that same topic when useful. It should establish the first meaningful entry into the mod, not teach every machine or recipe. A substantial introduction may become a linked companion article beneath the same topic, never a separate tutorial tree. Do not create an empty Getting started section or a mandatory pair of pages for every topic.

Top-level reference entries are Controls, Item recipe, Bosses, Creatures, Structures and dungeons, Dimensions, Equipment, Spells and skills, Food and farming, Building, Vehicles and travel, Machines and storage, and Maps. Six grouped directories organize existing topic pages. A directory lists real destinations and honest completion markers, not duplicated article prose.

## Catalog completeness

Boss and creature entries need a name, introducing mod, dimension, encounter or spawn location, and any access or summoning requirement. Structures and dungeons need the actual structure family and variant list, source mod, dimension and relevant biome or placement restrictions. Separate structure definitions, templates and assembled dungeon variants: their file counts are not interchangeable. Record exact selected-version evidence before claiming a complete total. Do not infer personal defeat progress from handbook presence or introduce quests.

Catalog items by useful families and variant names, not just by mod slogans. Use authentic publisher galleries where they help identify a place or feature, with clear captions and provenance. A screenshot does not establish that every feature shown ships in the selected release. Keep snapshots and illustrated catalogs legible instead of creating a wall of adjacent tables.

## Spacing

The selected engine has fixed heading margins, but native Row and Column containers expose a gap attribute for spacing their child blocks. Markdown thematic breaks provide readable separators. Use a single thematic break between major homepage sections and between each major reference section, including Controls, so tables and following headings do not run together. Extra blank source lines generally collapse and are not a reliable spacer. Do not add empty headings or invented margin attributes. Recheck the rendered result before applying extra separators throughout the book.

## Language and tone

Write for the player as a maintained handbook. Do not mention review, samples, prototypes, future interface plans or the author's implementation process. Use short noun-driven titles such as Controls, Structures, Ore processing and Cooking tools. Use an ampersand in compact navigation labels and headings when it shortens a useful paired name, such as Spells & skills and Machines & storage. Avoid long sidebar labels that wrap; keep the taxonomy identity separate from its shorter display label. Give every sidebar topic a meaningful native navigation icon, including all Quick reference entries. Do not use Draft for review or temporary status prose.

An unwritten article retains a short Work in progress (WIP) marker. Installed, heavy-edition-only and deferred content must remain distinct. Do not remove a genuine uncertainty by turning it into a confident claim. Keep material safety or compatibility limitations where they affect the player.

Apply Lucas's writing conventions: no em dashes or en dashes, no decorative symbols or symbol operators, no abbreviations in authored prose, and no bold labels followed by colons. Preserve official mod names, identifiers, commands and native markup exactly when they are needed. Avoid backticks around search examples because this GuideME release renders inline code in italics.

Maintain English and Simplified Chinese only. Use identical filenames, links, section meaning, item associations and visual identifiers across languages. Translate prose naturally rather than copying English word order. Preserve official mod names and exact query tokens. Label English publisher summaries accurately until they have been translated; an untranslated summary is not completed Chinese coverage.

## Navigation and interaction

Do not create one-line redirect pages or duplicate top-level navigation entries. Ore processing has one primary page under Machines and storage in Quick reference, cross-linked from Automation and industry. Consolidate short landscape and river summaries under the appropriate dimension section instead of requiring another page click. A separate page must offer substantial information beyond the catalog row.

Classify inventory entries by their actual function, not merely by their relationship to a mechanic. Recipe-browser addons, villager naming, trade-screen shortcuts and manual anvil conveniences belong with player utilities. A mechanics page may cross-reference them without turning them into Automation Mods. Supporting libraries belong under Technical reference.

Every catalog title and detailed entry that promises a destination must have a real handbook link. Link mod entries to their primary topic. Place related topic links near the relevant explanation or in one short closing line. Use the toolbar for history navigation; do not stack Back to category and Back to activities links.

Item associations belong in item_ids frontmatter and must have one unambiguous primary article. Native ItemLink follows those associations to handbook pages. It does not open the external recipe browser. Native ItemGrid provides tooltips, not automatic external actions. Do not describe an icon as clickable unless its action has been verified.

Use exact registered KeyBind identifiers for current controls. Label default keys separately from current assignments. The item browser has its own settings; do not imply all its controls are configured in Minecraft's Key Binds screen. Check the selected instance before assigning a new shortcut, and do not overwrite unrelated controls.

## Native component conventions

| Component | Intended use | Boundary |
| --- | --- | --- |
| ItemGrid with ItemIcon children | Actual item instruction and hover names | Expands to available width; not a compact decorative navigation icon |
| ItemImage | Decorative inline topic icon | No item tooltip; pair it with a visible linked topic label |
| ItemLink | Localized item label with tooltip and associated handbook destination | A self-reference or unassociated item may be a tooltip label rather than a link |
| Recipe | Exact registered recipe display | Requires a supported renderer and a loaded game recipe manager |
| KeyBind | Current configured key label | Requires the exact registered action identifier |
| Markdown link | Handbook navigation | The target must exist in both languages |
| Row and Column | Small visual comparisons | Check narrow widths; do not assume responsive cards or wrapping |

Use decorative ItemImage only where the item represents a topic or category and the visible label supplies its meaning. Do not use it for instructional item names. Do not invent component attributes or imply a component supplies an integration it does not have.

## Source ownership

Authored mechanics and controls live in docs/handbook-content.json. Publisher summaries and source links live in docs/handbook-project-descriptions.json. The generator owns navigation, catalogs, coverage and final resource page files. Templates are starting material for the authoring sources, not files to copy into a running resource pack unchanged.

Generated pages live in the handbook resource pack. Do not edit those pages by hand and then run the generator over them. Add new topics to the generator's inventory and navigation definitions, keep locale parity, and regenerate before testing.

Documentation and templates remain under docs. The existing docs exclusion in .packwizignore keeps them out of the pack index and native exports. Helper source remains under scripts, also excluded. Neither documentation exclusion nor syntax success replaces archive verification.

## Iterative workflow

1. Read this standard and the latest player review.
2. Edit the authoritative content, catalog definitions or translations. Tune three representative pages and their templates before rolling a new layout across all authored articles. Structural repairs such as consistent heading placement and corrected membership may affect linked pages, but do not expand their prose prematurely.
3. Run the generator and source checks.
4. Run the selected-release parser check after markup changes.
5. Review the changed page in the dedicated instance with native live preview enabled.
6. Record what was actually verified and commit the completed logical change.

Use the dedicated light authoring instance, not a new import for each writing update. It contains a normal resource-pack copy. GuideME's official live-preview Java arguments point directly to the generated repository Markdown folder. After launch with those arguments and the guide resource pack enabled, native watched sources should update ordinary page edits automatically. Do not use a symbolic resource-pack link: Minecraft rejects it by default. Helper code changes need another restart; changes to resource registration or other resource-pack assets can still require a resource reload.

## Verification checklist

- Titles, section order and navigation match the appropriate page type.
- The first useful information is a visual, catalog entry or control rather than authoring commentary.
- Item identifiers, recipe identifiers, quantities and chances match the selected artifacts.
- Expected links exist; expected interactions are actually implemented.
- Both locales have matching pages and meaning. Untranslated text remains explicitly tracked.
- Installed, optional-edition and deferred content are labeled accurately.
- Source checks pass for links, reachability, coverage and forbidden temporary wording.
- The released parser accepts markup and rejects its malformed negative control.
- Native exports exclude docs and scripts and preserve game resource bytes.
- Rendered layout, hover behavior and live refreshing are reported separately from source and packaging checks.
