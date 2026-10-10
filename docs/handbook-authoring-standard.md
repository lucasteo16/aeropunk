# Astropunk handbook authoring standard

This is the authoring contract for every handbook update. It belongs to repository documentation, not the distributed game resources. Read it before writing, translating or restructuring a page.

## Purpose and organization

The same handbook resources serve the light and heavy editions. Populate heavy-edition references even when authoring against the light pack, and label their scope with (heavy edition only), or （仅重型版）. Do not describe common content as baseline or installed, and do not claim edition-specific content is absent from whichever instance reads the guide. Keep truly deferred additions distinct from heavy-edition content. Optional-mod native item references must not cause missing-item errors in the light edition.

Combat may use three sidebar levels: the Combat root, a class grouping, and a focused class article. Keep the Combat overview concise and move class-specific equipment, abilities and starter recipes into those articles. Preserve native references and meaningful shared mechanics, without duplicating all class recipes on Weapons and armor. Keep all sidebar item identifiers globally unique.

Place Cooking tools first and Hunger and variety second within Food and farming. Keep help about the handbook and other documentation under Technical, not gameplay Utilities. Consolidate Moving destinations into Teleportation. Keep image-source qualifications and artwork provenance in authoring records rather than verbose player-facing captions.

Food articles teach the shared cutting-board, stove, pot and skillet interactions once in Cooking tools. Keep other food topics focused on ingredient sources, cuisine families and genuinely different mechanics. Leave amounts, substitutions, yields and ordinary cooking chains to native recipes and the recipe browser rather than repeating one instruction per dish. Preserve native item grids, useful recipe displays and unusual acquisition conditions. Give every food topic a distinct relevant sidebar icon instead of inheriting the same apple.

The handbook prioritizes a content index: answer what exists in the installed game before describing what players can do with it. A mod roster alone is not a complete content index. Catalog actual bosses, creatures, structures, dungeon variants, equipment, spells, foods, building families, vehicles and destination types. Mechanics and crafting tutorials are secondary. Reuse existing recipe tools and Ponder rather than duplicating their instruction. Do not organize the entire book around player intentions.

The home is Astropunk and explains the pack's identity, main activities and freely chosen ways to play. It is not a duplicate directory. Astropunk and the sixteen main sections are native first-level sidebar entries. Do not create Quick reference, another wrapper page or outer provider catalogs. Each topic contains the useful information from the former catalogs, explains available content and how to start, and then lists its relevant mods in a lower section with icons, translated purposes and installation status. Group mods that implement the same activity and explain the shared mechanic once. Introduce equipment, class choices, abilities and skill development together under Combat, keeping substantial equipment and ability references as subtopics. Keep utilities, appearance, audio and technical information as first-level sections with appropriate children. Use one category level before an article, give each article one primary home, and cross-link related uses without duplicate provider navigation.

The handbook is freely accessible. Do not add quests, completion rewards, progression locks or compulsory reading sequences. Actual mod gameplay requirements still apply and must be described accurately.

## Page types and section order

| Type | Required structure |
| --- | --- |
| Home | Astropunk title, pack identity, main activities and flexible starting points, not a copy of the reference directory |
| Area catalog | Title, available activities and starting guidance, visible topic links, then relevant mods with icons and installation status |
| Reference catalog | Title, second-level sections for actual entries such as Overworld, Nether and End; put short mod summaries and visuals in the catalog itself; link out only to substantial mechanics |
| Getting started | Inside its reference topic when short; name the first prerequisite, item, workstation or interface, then point to native recipes, Ponder or existing help; no exhaustive walkthrough |
| Controls article | Access instructions, current bindings, clearly labeled defaults, rebinding and conflict instructions |

The first-level heading supplies the toolbar title. The Astropunk homepage is the sole exception to sectioned article layout: put one clean authentic ship image directly beneath the title, followed by compact engaging prose, without secondary headings, a next-project section or a duplicated navigation list. A standalone image-credit link may lead to a short Credits child of Astropunk. Explain that sidebar topics are quick entry points, not quest progression. Target one screen at the review layout, preserve both languages and do not change global interface scaling to enlarge this page. All other article bodies must begin with a second-level heading, and every later section must remain beneath a second-level heading. Third-level headings may subdivide an article section.

Use the matching file in docs/handbook-templates as a starting point. Omit sections that add nothing; do not insert empty headings or generic introductory paragraphs to satisfy a template. A dimension catalog does not need a crafting recipe. A library reference does not need a demonstration.

## Visual and text conventions

Lead with actual item models, native recipe displays, verified comparisons or authentic game captures. Publisher icons and screenshots are allowed. Download them into the guide source images folder, convert to supported image formats, record source URLs, publisher identity, checksum and license metadata in docs/handbook-visual-sources.json, and use a short subject caption. Do not add publisher screenshot boilerplate to player-facing captions; retain attribution and provenance in repository notes, and never imply they show this instance. Prefer clean terrain and interface screenshots over marketing banners and do not substitute decorative item icons for missing landscape images. GuideME scales ordinary images to one quarter of their pixel dimensions, so 96-pixel publisher icons produce compact 24-pixel guide images. Verify dimensions and do not invent sizing attributes. Text explains the visual rather than replacing it. Generated art may decorate a background or theme, but never explains a machine, recipe or gameplay procedure.

Use native item slots for actual item instruction, with item names and hover tooltips. For topics and catalog navigation, use decorative ItemImage beside the linked label instead: it has fixed icon dimensions and no item tooltip. Do not invent a hide-tooltip attribute on ItemGrid. ItemGrid expands to the available width, which can force a nearby label onto a new line. Avoid it for inline navigation, and do not mix links or table separators into its child content. A Markdown parser accepting a compact table cell does not prove that its native component tree is valid. Label unfamiliar icons visibly when identifying them is necessary to understand the page; a hover name is a supplement, not the only instruction. Keep input, tool or processing medium, and output distinct. A water-bucket icon used to represent water must not imply that the recipe consumes a bucket.

Use native recipes only for types the selected renderer supports. For unsupported processing types, show verified item visuals and concise output data. State quantities and chances exactly. Record the source artifact and recipe identifier in authoring evidence, not as an intrusive player-facing disclaimer. Never substitute an illustrative scene for a working arrangement without identifying what it depicts.

Keep an introduction to one sentence when possible. Prefer short labels, comparison tables and brief instructions. Explain one mechanic per section. Add numbered steps only when order matters. Avoid dense prose, repeated warnings, large icon-title-description stacks and unqualified claims that all machines or containers behave identically.

Reuse Create Ponder for supported assembly and operation. Identify the relevant item and its help entry rather than rebuilding an existing demonstration. Write bespoke explanation when existing help does not cover the mechanic or interaction.

Use native GameScene when an equipped model or spatial arrangement adds useful information. Read docs/guideme-scene-authoring-notes.md before authoring scenes. In the selected release, imported structures omit entities, so an equipped armor stand requires the native Entity element and verified equipment data. Preserve native item references beside model displays. Verify scene compilation, selected registries and actual rendering separately, and do not present a scene as proof of functioning machinery.

## Shared topic structure

Use one topic tree and two complementary page types: Reference and Getting started. The reference page is the landing page and inventories what exists, variants, locations and access. Put a short Getting started section beneath that same topic when useful. It should establish the first meaningful entry into the mod, not teach every machine or recipe. Show playable class choices and their roles directly on Spells & skills, with starting equipment, suitable native crafting recipes, spell binding and equipment relationships. Do not bury class choices or first steps in provider rosters. A substantial introduction may become a linked companion article beneath the same topic, never a separate tutorial tree. Do not create an empty Getting started section or a mandatory pair of pages for every topic.

The exact native root order is Astropunk, Controls, Browse recipe, Bosses, Creatures, Structures, Dimensions, Combat, Food & farming, Building, Transport, Machines & storage, Maps, Utilities, Appearance, Audio and Technical. Astropunk and all sixteen sections omit the parent field. Set Astropunk position to negative one hundred and section positions to zero through fifteen. Directory children use their actual section filename as parent. Equipment, abilities and detailed combat articles remain direct Combat children. Audio contains the complete rain, footsteps, effects, acoustics and volume reference with one related-mods footer, not a single-link Sound directory. Archive obsolete Quick reference and standalone Sound pages outside the source tree rather than creating redirects. Count native roots, reference directories and authored articles separately. Validate reachability from all native sidebar roots, without copying the directory into Astropunk. Grouped directories organize substantial topic pages. A directory lists real destinations and honest completion markers, not duplicated article prose.

## Catalog completeness

Boss and creature entries need a name, introducing mod, dimension, encounter or spawn location, and any access or summoning requirement. Structures and dungeons need the actual structure family and variant list, source mod, dimension and relevant biome or placement restrictions. Separate structure definitions, templates and assembled dungeon variants: their file counts are not interchangeable. Record exact selected-version evidence before claiming a complete total. Do not infer personal defeat progress from handbook presence or introduce quests.

Catalog items by useful families and variant names, not just by mod slogans. Search official galleries and main-description images first. If no suitable image exists there, make a targeted online search, including relevant third-party wiki pages. Use only identifiable, clean images without watermarks, blocking text or poor fidelity, and preserve source and rights provenance. Third-party prose is not evidence of mechanics in the selected release. A screenshot does not establish that every feature shown ships in the selected release. Keep snapshots and illustrated catalogs legible instead of creating a wall of adjacent tables.

## Spacing

The selected engine has fixed heading margins, but native Row and Column containers expose a gap attribute for spacing their child blocks. Markdown thematic breaks provide readable separators. Use a single thematic break between major homepage sections and between each major reference section, including Controls, so tables and following headings do not run together. Extra blank source lines generally collapse and are not a reliable spacer. Do not add empty headings or invented margin attributes. Recheck the rendered result before applying extra separators throughout the book.

## Language and tone

Write for the player as a maintained handbook. Do not mention review, samples, prototypes, future interface plans or the author's implementation process. Use short noun-driven titles such as Controls, Structures, Ore processing and Cooking tools. Use an ampersand in compact navigation labels and headings when it shortens a useful paired name, such as Spells & skills and Machines & storage. Avoid long sidebar labels that wrap; keep the taxonomy identity separate from its shorter display label. Give every sidebar topic a meaningful native navigation icon, including every first-level section. Do not use Draft for review or temporary status prose.

An unwritten article retains a short Work in progress (WIP) marker. Installed, heavy-edition-only and deferred content must remain distinct. Do not remove a genuine uncertainty by turning it into a confident claim. Keep material safety or compatibility limitations where they affect the player.

Apply Lucas's writing conventions: no em dashes or en dashes, no decorative symbols or symbol operators, no abbreviations in authored prose, and no bold labels followed by colons. Preserve official mod names, identifiers, commands and native markup exactly when they are needed. Avoid backticks around search examples because this GuideME release renders inline code in italics.

Maintain English and Simplified Chinese only. Use identical filenames, links, section meaning, item associations and visual identifiers across languages. Translate prose naturally rather than copying English word order. Preserve official mod names and exact query tokens. Label English publisher summaries accurately until they have been translated; an untranslated summary is not completed Chinese coverage.

## Navigation and interaction

Do not create one-line redirect pages or duplicate top-level navigation entries. Ore processing has one primary page under the first-level Machines and storage section, without a second Automation catalog. Consolidate short landscape and river summaries under the appropriate dimension section instead of requiring another page click. A separate page must offer substantial information beyond the catalog row.

Classify inventory entries by their actual function, not merely by their relationship to a mechanic. Recipe-browser addons, villager naming, trade-screen shortcuts and manual anvil conveniences belong with player utilities. A mechanics page may cross-reference them without turning them into Automation Mods. Supporting libraries belong under Technical reference. Classify ambient rain and footsteps as audio, not technical support, and verify every technical entry by actual function.

Every catalog title and detailed entry that promises a destination must have a real handbook link. Link mod entries to their primary topic. Put topic entry points in standalone bullet lists or clear navigation tables above or below the explanation, never hide multiple destination links inside paragraphs. Use the toolbar for history navigation, do not stack Back to category and Back to activities links.

Use informational sentences instead of comma-separated name dumps. Describe a family's purpose, how to acquire it and what a player can do with it. A partial grid must not imply complete equipment coverage. Give each boss its own identifying section, appearance image where available, location and verified access requirement. Bosses owns boss encounters, Creatures links to that page rather than duplicating them. Actual named items used for summoning, crafting, equipment or instruction need native item visuals and localized tooltip references beside their explanation. Resource models and translations alone do not prove that an item is registered in the running game.

Do not use English or Chinese semicolons in player prose. Preserve them only inside literal code or a required token. Omit ordinary Minecraft movement controls. Distinguish normal resource reloading, GuideME's contextual item binding and the custom whole-handbook helper, never claim that watching, shortcuts or an inventory button work without runtime evidence. Structure image fallbacks may use a publisher title image, but label its subject without pretending it is an individual structure screenshot. All mod roster rows need publisher icons where supplied, or a meaningful topic icon when no publisher artwork is available.

Item associations belong in item_ids frontmatter and must have one unambiguous primary article. Native ItemLink follows those associations to handbook pages. It does not open the external recipe browser. Native ItemGrid provides tooltips, not automatic external actions. Do not describe an icon as clickable unless its action has been verified.

Use native Color with the six-digit pink color #F28CBD around literal commands and manually typed search queries. Where the verified recipe-browser integration exists, use its actual registered query component for clickable searches. Preserve query tokens and check namespace matching against the selected browser. Include the appropriate query near each mod explanation and in its provider row. A genuine mod-section query is an unlabeled line directly beneath its heading, with no bullet and no Browse items prefix. Controls and Browse recipe teach search syntax instead, label example queries in their instructional context and do not inject mod filters above their headings or images. Mods without an independent item catalog need a truthful non-item designation or a related producer query, not a misleading addon slug. Component-bearing vanilla outputs may require localized name searches instead. Never imply plain colored text executes an action.

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
- The released parser accepts markup and rejects its malformed negative control. Actual native component compiler probes reject invalid child trees and accept the repaired structures, including item grids in their real Markdown context.
- Native exports exclude docs and scripts and preserve game resource bytes.
- Rendered layout, hover behavior and live refreshing are reported separately from source and packaging checks.
