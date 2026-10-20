# Refurbishment correction contract

This contract reopens the Food and farming, Machines and storage, and Transport batch after player review rejected the previous export. It supplements the authoring standard and playbook. Where older procedural shortcuts disagree, this contract wins. The accepted rebuilt Combat chapter is the presentation reference, not the previously refurbished food pages.

## Player questions

An activity page must answer both what exists and what to do with it. Naming one item or answering one question is not sufficient.

- What is available here, and why would I choose it?
- Where do I begin, and which concrete item, resource, workstation or access do I need?
- How do I place, equip, connect or operate it, using actual interactions?
- What result shows that the first use succeeded?
- What can I make or do next, and why is that worthwhile?
- Which optional improvement fits my current access and resources?
- Which mod-specific restriction explains a failed attempt, when genuinely useful?

Integrate these answers beside the appropriate items. Do not impose the same seven headings everywhere, manufacture failure tables or create a separate tutorial tree. A catalog remains browsable and complete, but no longer leads with a dump of everything. Start with a small useful action and expand into meaningful alternatives. Optional Early game, Midgame and Late game guidance describes concrete readiness, not elapsed days or compulsory quests.

## Canonical style

Read these accepted bodies in docs/handbook-content.json before writing: reference.skills, combat.abilities, combat.magic, class.arcane and equipment.weapons-armor. Read both locales. Identify how they combine first actions, meaningful catalogs and shared mechanics. Do not imitate their subject-specific class headings on food pages.

Keep short noun titles, concise sentences, compact comparisons, prominent standalone topic links and clear separators. Remove generic gamer advice and repeated explanations. No implementation commentary or descriptions such as remaining items, shown items, catalog completeness or this chapter's leftovers in player text. No dense paragraph blocks. Reduce scrolling without deleting mechanics.

Apply the authoring standard's language conventions in both languages. No em or en dashes, semicolons, symbol operators, abbreviations or bold labels followed by colons in authored prose. Keep exact official names, identifiers, links, markup and literal commands intact. Chinese must read naturally and preserve equivalent meaning.

## Tutorial actions

Every substantive revised page and each revised activity landing page must have exactly one compact YouTube search action immediately below its page title, before the first section. Both English and 中文 choices appear in both locales with the shared play icon. Build contextual query URLs from the actual topic. Preserve the headings-first authoring contract and let the generator hoist the row. Do not silently omit the row because the old source lacked it. Verify generated resources and the delivered archive, not just authored strings.

## Visual semantics

- Item icons identify items. Put the specific tool beside its name when the reader must recognize it, including knife, pickaxe, axe, shovel and shears in the cutting-board comparison.
- Never use a mixed strip of workstation, fuel, tool, ingredients and outputs as a relationship diagram, procedure or recipe. A caption does not repair that representation.
- Native GameScene illustrates actual placement and orientation. Cooking pot over a lit stove, heat below a skillet, and an output collector's location should be shown spatially when explained. Read docs/guideme-scene-authoring-notes.md and verify selected-release markup and state properties. Scenes must identify the parts and the relationship, not display unrelated blocks on a plinth.
- Native recipes show transformations only when the exact loaded recipe exists and the renderer supports its type. Unsupported processing uses a verified concise explanation and deliberately labeled item visuals, not a red error or a fake crafting recipe.
- Authentic screenshots show appearance or an interface. Do not substitute a generic screenshot for a missing placement explanation.
- Every meaningful section needs an explanatory visual. A text-only table does not satisfy this rule. Do not add a random grid to satisfy a validator. Delete filler rather than decorating it.
- Tables compare genuinely parallel alternatives. Avoid wide prose-heavy rows and one-column tables. Catalog rows must have precise, consistent membership. Separate tools, raw ingredients, intermediates and finished foods. Do not preserve arbitrary mixed leftovers by appending them to the nearest grid.
- Preserve meaningful item and ability coverage, but move references into their correct owning sections with a recorded disposition. Preservation never requires retaining a broken identifier or redundant icon occurrence.

## Fishing scope

The Starcatcher book owns fish location lookup, biome conditions and live catch information. Explain how to obtain and use the book, then how to choose equipment, fish and use the catch. Remove the handbook's Terralith marker tables, custom-biome inference and duplicated fish-location database. Update the landing-page descriptions and links too. A page left without substantial content must be merged or retired coherently, not turned into a one-line redirect. Preserve distinct rod-catch, natural-spawn and food-processing mechanics where relevant.

## Runtime correctness

The screenshots demonstrate missing recipes starcatcher_delight:hosomaki_common and ends_delight:chorus_fruit_milk_tea, and missing dotted Chipped backpack upgrades. These are unresolved defects, regardless of earlier passing checks.

A translation key, model, blockstate or class constant is a discovery hint, not proof of a registered item. The previous check_item_existence.py is not a registry acceptance gate. Recover actual registration identifiers, conditional integration requirements and supported recipe types from the exact selected release. A disabled integration may leave assets behind. Never change a slash to a dot by inferring from a translation key. Validate against real registry evidence when available and record any runtime uncertainty honestly.

Scan every native recipe and optional integration in the whole batch for the same defect class. Verify recipe resource paths, recipe type support and pack overrides. Do not restore an invalid recipe solely to make an old preservation test pass. Record the corrected, relocated or retired reference with its evidence and adapt only the stale expectation, not the quality requirement.

## Research

Read official and maintained gameplay guidance, plus relevant videos or available transcripts. Record exact source URLs, version boundaries and access limits. Use selected-artifact data or targeted code only for unresolved facts. A search result is not a read video. A partial transcript is partial evidence. Existing evidence may be reused after checking relevance, but it cannot justify unrelated assertions.

## Reviewer and writer workflow

The reviewer is the parent Codex session. Writers use deepseek/deepseek-v4.1-flash-1017 through OpenRouter for this correction, explicitly overriding the earlier Codex-only writer rule. Do not change global provider settings or credentials. At most two writers run concurrently.

First repair representative pages: cooking tools and its landing page, seafood and End food recipe failures, and portable storage. Writers return disjoint topic-keyed fragments and evidence, never editing the shared source, generator, tests or pack resources. The parent alone integrates and packages.

The parent reviews the actual complete fragment for player questions, visual semantics, scrolling cost, native references, bilingual parity and source grounding. Reject with exact findings and resume the same writer with the rejected passage and acceptance example. Keep a reusable rejection record so the same pattern is not debated repeatedly. No concurrent writer and parent edits to the same fragment. Preserve returned originals and use separately named reviewed versions.

After regional repairs, repeat the same review, delegate, revision and verification cycle across every topic and landing page in this batch. Review changed hunks and discovered cross-page effects rather than reopening accepted unrelated Combat work. No fixed pass count substitutes for acceptance. Stop a failing execution route after one failed attempt and report a genuine blocker rather than silently switching models or bypassing permissions.

## Acceptance and handoff

- Each page satisfies its applicable player questions and the Combat presentation standard.
- Tutorial actions survive generation and archive creation in both locales.
- No relational item strips, mixed leftover catalogs, filler or prose-only tables used as visual substitutes.
- Appropriate verified scenes and supported native recipes are present.
- Fishing directs biome lookup to the book without duplicating the biome database.
- Exact item and recipe registration evidence replaces asset-based guesses. No known red errors remain.
- Focused source, parser, component, scene and packaging checks are recorded separately from real rendered acceptance. A probe that replaces registry entries or strips scenes cannot prove those features work.
- The parent reads the final archive back and confirms it matches the integrated source after the final correction.
- Do not launch a game, alter a played instance, install anything, promote stable branches, commit or push without the applicable approval. The old review archive is rejected, not a valid completion artifact.
- Do not declare flawless while rendered defects or requested review work remain unresolved. Name the remaining boundary plainly.
