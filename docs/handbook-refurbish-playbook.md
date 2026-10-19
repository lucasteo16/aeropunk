# Handbook refurbishment playbook

This distils the requirements and the writing style agreed for the Astropunk handbook into one working document. `docs/handbook-authoring-standard.md` remains the structural contract. This playbook is the quality bar and the process for a chapter refurbishment batch.

## What a refurbished chapter must do

A reader opens a page to answer one of these questions. Every page must answer at least one of them without leaving the page.

1. What is this thing and why would I want it.
2. What do I need before I can start.
3. What exactly do I do, step by step, with the real items and the real interface.
4. How do I know it worked.
5. What do I do next, and when is that worth doing.
6. What commonly blocks people, and what is the mod specific cause.

A page that only names things, or only restates general Minecraft knowledge, is unfinished.

## Style rules, non negotiable

- No em dash, en dash, equals sign, forward slash as a separator, arrow or symbol operator in player prose.
- No abbreviations. Write the whole word.
- No bold label followed by a colon. Write a sentence instead.
- No semicolons or full width Chinese semicolons in player prose.
- Short declarative sentences. One idea per sentence. Prefer verbs to nominalisations.
- Production language only. No draft, review, sample, prototype or implementation notes in player pages.
- Keep official mod names, item identifiers, commands and query tokens exactly as they ship.
- Follow the established page voice already used in the refurbished Combat section.
- Titles are short nouns or short noun pairs, for example Cooking tools, Rotational power, Portable storage.

## Content rules

- Research before writing. Read official documentation and maintained guides first, then credible gameplay videos and their transcripts where available. Record what was read. Never claim a video was watched when only a transcript or search snippet was read.
When direct YouTube access is blocked from this network, read transcripts through a server side transcript frontend and expect only the opening minutes. Verify every video claim against the selected jar first: a video about a similarly named mod will describe blocks that this pack does not ship. Record which videos were read, which were only found, and why the rest were not used, the same way docs/handbook-refurbish-video-evidence.json does.
- Reconcile every mechanic against the selected Minecraft version and the selected mod versions in `mods/*.pw.toml`. Targeted code or data inspection is allowed only to resolve a specific unresolved mechanic.
- Keep facts that only this pack can teach. Delete advice any Minecraft player already has, such as which mouse button attacks, or that gear can be enchanted.
- No filler sections. If a section would be generic troubleshooting, generic readiness advice or a restatement of a table, delete it rather than decorate it.
- Optional guidance may use readiness stages, naming what you must already have or be able to do. Never use days played, invented tiers or compulsory quest chains.
- Distinguish required mechanics from recommended builds. Never call an example the official or best build.
- One mechanic owns its instructions. Other pages link to it instead of repeating it.

## Visual rules

- No section may be text only. Every section carries something visual that earns its place.
- Item icons identify actual items, with tooltips, inside a grid. They are not relationship maps, procedures or action sequences.
- Recipes explain crafting and processing. Native scenes explain placement, builds and spatial relationships. Screenshots show appearance or interface.
- Tables are for parallel comparison: family, item group, difference. A table of one column repeated is a list, not a table.
- Compact tables beat tall stacks of heading, caption and grid. Group by family and exact role, never invent a role.
- Equipped armor stand scenes illustrate example builds in class style pages, at zoom 4, with the companion item grid beside them.
- Choose visuals by the explanatory job, not to hit a count. Do not add a scene where a table answers the question.

## Per page completion bar

A page is done when all of these hold.

- It states its purpose in the first lines.
- It answers at least one of the six questions above, ideally several.
- It carries a visual in every section.
- It contains no generic advice and no duplicated instruction.
- Every native reference resolves in the selected pack.
- Both languages read naturally and say the same thing.
- No style violation remains.

## Batch workflow

1. Pick the chapter and list its pages from the generated navigation, not from memory.
2. Freeze the baseline of the chapter pages before editing, as the Combat review did, so later comparison is honest.
3. Split the chapter into two disjoint worker batches at most. Workers write topic keyed fragments only. They never edit `docs/handbook-content.json`, the generator, tests or generated pages.
4. Workers research first and record sources, transcript limits and version boundaries in an evidence file beside the fragment.
5. The parent integrates, normalises grids, regenerates, then runs the gates below.
6. Review the changed chapter once, then re review only changed sections. Do not reopen settled pages.
7. Package and hand over a comparison resource pack for the maintainer to inspect in game.

## Gates

- `python scripts/build-handbook-draft.py`
- `python -m unittest discover -s tests -p test_handbook_visual_pass.py`
- `python -m unittest discover -s tests -p test_handbook_navigation.py`
- `python -m unittest discover -s tests -p test_handbook_review_layout.py`
- selected GuideME parser over the generated pages
- structural compiler over the generated pages, scenes stripped
- scene attribute probe where scenes were added
- no text only section check over the chapter in both languages
- archive parity check when a comparison pack is built

## Evidence to keep

Per batch, keep the frozen baseline, worker fragments, merged evidence JSON, parser and compiler logs, the text only report, and the final archive hash. Evidence lives under `build/<batch-name>/`.

## Chapter priority thinking

Rank a chapter by how much a new player needs it, multiplied by how bad its current pages are. The worst pages are the ones with a lot of text, few visuals and no scenes. A chapter that is already short and honest is lower priority even if it is small.
