# Astropunk handbook authoring standard

This is the authoring contract for every handbook update. It belongs to repository documentation, not the distributed game resources. Read it before writing, translating or restructuring a page.

## Purpose and organization

The handbook is a reference to Astropunk's installed mods, worlds, items and mechanics. Catalogs answer what is available. Mechanics articles explain how a particular system works. Do not organize the entire book around player intentions.

The home is Astropunk. It contains compact catalog entry points and links to Controls, Items and recipes, and Dimensions. Use no more than two category levels before an article. Give each topic one primary home and use cross-links for related areas. Include supporting libraries in the same consistent reference structure, without presenting them as gameplay features.

The handbook is freely accessible. Do not add quests, completion rewards, progression locks or compulsory reading sequences. Actual mod gameplay requirements still apply and must be described accurately.

## Page types and section order

| Type | Required structure |
| --- | --- |
| Home | Astropunk title, one-sentence scope, essential help links, compact area catalog |
| Area catalog | Title, topic contents, installed mod table, clearly separated uninstalled content when relevant |
| Reference catalog | Title, comparable entries, one-sentence descriptions, links to detailed articles; availability or access fields only when useful |
| Mechanics article | Title, optional one-sentence purpose, item visuals and labels, recipe or visual explanation, short operational guidance, related topics and mods |
| Controls article | Access instructions, current bindings, clearly labeled defaults, rebinding and conflict instructions |

Use the matching file in docs/handbook-templates as a starting point. Omit sections that add nothing; do not insert empty headings or generic introductory paragraphs to satisfy a template. A dimension catalog does not need a crafting recipe. A library reference does not need a demonstration.

## Visual and text conventions

Lead with actual item models, native recipe displays, verified comparisons or authentic game captures. Text explains the visual rather than replacing it. Generated art may decorate a background or theme, but never explains a machine, recipe or gameplay procedure.

Use native item slots for item names and hover tooltips. Label unfamiliar icons visibly when identifying them is necessary to understand the page; a hover name is a supplement, not the only instruction. Keep input, tool or processing medium, and output distinct. A water-bucket icon used to represent water must not imply that the recipe consumes a bucket.

Use native recipes only for types the selected renderer supports. For unsupported processing types, show verified item visuals and concise output data. State quantities and chances exactly. Record the source artifact and recipe identifier in authoring evidence, not as an intrusive player-facing disclaimer. Never substitute an illustrative scene for a working arrangement without identifying what it depicts.

Keep an introduction to one sentence when possible. Prefer short labels, comparison tables and brief instructions. Explain one mechanic per section. Add numbered steps only when order matters. Avoid dense prose, repeated warnings, large icon-title-description stacks and unqualified claims that all machines or containers behave identically.

Reuse Create Ponder for supported assembly and operation. Identify the relevant item and its help entry rather than rebuilding an existing demonstration. Write bespoke explanation when existing help does not cover the mechanic or interaction.

## Language and tone

Write for the player as a maintained handbook. Do not mention review, samples, prototypes, future interface plans or the author's implementation process. Use noun-driven titles such as Ore processing and Cooking tools. Do not use Draft for review or temporary status prose.

An unwritten article retains a short Work in progress (WIP) marker. Installed, heavy-edition-only and deferred content must remain distinct. Do not remove a genuine uncertainty by turning it into a confident claim. Keep material safety or compatibility limitations where they affect the player.

Apply Lucas's writing conventions: no em dashes or en dashes, no decorative symbols or symbol operators, no abbreviations in authored prose, and no bold labels followed by colons. Preserve official mod names, identifiers, commands and native markup exactly when they are needed. Avoid backticks around search examples because this GuideME release renders inline code in italics.

Maintain English and Simplified Chinese only. Use identical filenames, links, section meaning, item associations and visual identifiers across languages. Translate prose naturally rather than copying English word order. Preserve official mod names and exact query tokens. Label English publisher summaries accurately until they have been translated; an untranslated summary is not completed Chinese coverage.

## Navigation and interaction

Every catalog title and detailed entry that promises a destination must have a real handbook link. Link mod entries to their primary topic. Place related topic links near the relevant explanation or in one short closing line. Use the toolbar for history navigation; do not stack Back to category and Back to activities links.

Item associations belong in item_ids frontmatter and must have one unambiguous primary article. Native ItemLink follows those associations to handbook pages. It does not open the external recipe browser. Native ItemGrid provides tooltips, not automatic external actions. Do not describe an icon as clickable unless its action has been verified.

Use exact registered KeyBind identifiers for current controls. Label default keys separately from current assignments. The item browser has its own settings; do not imply all its controls are configured in Minecraft's Key Binds screen. Check the selected instance before assigning a new shortcut, and do not overwrite unrelated controls.

## Native component conventions

| Component | Intended use | Boundary |
| --- | --- | --- |
| ItemGrid with ItemIcon children | Item models and hover names | Does not automatically open recipes or another page |
| ItemLink | Localized item label with tooltip and associated handbook destination | A self-reference or unassociated item may be a tooltip label rather than a link |
| Recipe | Exact registered recipe display | Requires a supported renderer and a loaded game recipe manager |
| KeyBind | Current configured key label | Requires the exact registered action identifier |
| Markdown link | Handbook navigation | The target must exist in both languages |
| Row and Column | Small visual comparisons | Check narrow widths; do not assume responsive cards or wrapping |

Do not use decorative ItemImage for instructional item names. Do not invent component attributes or imply a component supplies an integration it does not have.

## Source ownership

Authored mechanics and controls live in docs/handbook-content.json. Publisher summaries and source links live in docs/handbook-project-descriptions.json. The generator owns navigation, catalogs, coverage and final resource page files. Templates are starting material for the authoring sources, not files to copy into a running resource pack unchanged.

Generated pages live in the handbook resource pack. Do not edit those pages by hand and then run the generator over them. Add new topics to the generator's inventory and navigation definitions, keep locale parity, and regenerate before testing.

Documentation and templates remain under docs. The existing docs exclusion in .packwizignore keeps them out of the pack index and native exports. Helper source remains under scripts, also excluded. Neither documentation exclusion nor syntax success replaces archive verification.

## Iterative workflow

1. Read this standard and the latest player review.
2. Edit the authoritative content, catalog definitions or translations.
3. Run the generator and source checks.
4. Run the selected-release parser check after markup changes.
5. Review the changed page in the dedicated linked instance.
6. Record what was actually verified and commit the completed logical change.

Use the currently linked light authoring instance, not a new import for each writing update. F3 and T reloads resources before the helper's initial launch. After one restart with the installed helper, native watched sources should update ordinary page edits automatically. Helper code changes need another restart; changes to resource registration or other resource-pack assets can still require a resource reload.

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
