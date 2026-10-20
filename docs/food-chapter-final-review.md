# Food and farming final review

## Accepted scope

Lucas accepted the eight unmentioned Food articles and requested a final review and correction of Underground foods, Nether foods and Encounter foods before merging Food into development. This change contains eleven topics in English and Simplified Chinese. The eight accepted article bodies are retained byte-for-byte; their hashes are recorded in food-chapter-final-review.json.

## Named corrections

Underground foods now distinguish ingredients, cooked portions, handheld foods, plated meals, pasta, cup families and bars. The old mixed Dishes and materials strips are removed. Recipe ingredients, copper-pot container and output handling, rice-independent cave crop acquisition, Gossypium propagation and string use, raw-loot conditions and baked tentacles were reviewed against selected resources. Generic pantry/tool references retired from input strips are not claimed to be preserved elsewhere; no Miner's Delight food variant was removed.

Nether foods retain the accepted body and change the visual column label to View and 外观. The previously reviewed pepper-harvesting, knife-cut sausage, raw-to-roast preparation, knife-then-bowl serving and pickaxe-cracked strider egg instructions remain intact.

Encounter foods now distinguish raw drops, board portions, cooked cuts, finished meals and specialty ingredients. Raw and cooked deepling meat no longer share a grid. Grilled lionfish remains a pot dish, not a generic raw-to-cooked icon sequence. Boss and sea foods use compact named family rows, and pet food has a labeled native item display and a specific tamed-wolf interaction. The stat paragraph no longer claims every food gives a bonus or asks the player to infer repeatability from eating once: the selected default configuration enables food-stat tooltips and repeatable accumulation. Death persistence is deliberately not claimed.

The selected literal recipe identifiers and ordinary crafting/smelting serializers were checked separately from syntax parsing. Source recipes and registration names are not inferred from translated labels. Gameplay and video access limitations remain in the preserved correction research; no new video playback is claimed in this final pass.

## Final verification

All ten focused Food checks pass. They cover accepted-body preservation, Food-only source and generated-page scope, retired-habitat removal and book-led fishing lookup, View labels, tutorial actions under the title, exact bilingual native-reference and link parity, canonical compact item grids, section visual presence and the corrected critical recipe and interaction references. Negative controls reject later edits to named Food pages, accepted Food pages, unrelated Transport content and resurrection of the retired topic.

The selected GuideME 21.1.19 parser passes all twenty-two generated localized chapter pages. The native table-layout probe passes those pages with 476 grids and 922 slots. The probe normalizes item identities to vanilla stone, skips Recipe and KeyBind dispatch, uses a null image loader and omits two GameScene blocks. It establishes table/component structure, not actual pack registry resolution or in-game rendering. Actual image resources were checked independently; null-loader image warnings are expected fixture output.

Literal mod recipe paths, local handbook links and image paths have no missing references in the chapter. Model-asset discovery has no gaps, but is not a runtime registry dump. Native navigation ordering and its negative controls pass for 130 nodes and eighteen roots in both languages.

One historical metadata-preservation assertion still fails: its stored snapshot predates JEI and the two Sophisticated Backpacks files and still expects the already-retired vanilla-backpacks file. All 318 current mod metadata files and their bytes match the declared development base exactly. The unrelated snapshot assertion was not weakened to hide this pre-existing discrepancy.

The broader handbook source selection contains forty-nine tests. Its actual development-base worktree has nine failures. After the Food change and targeted repair, eight of those same failures remain and there are no new source-test failures or errors. They concern older inventory, rocket-fuel, acquisition-text, image and historical preservation expectations. They were not silently skipped or reported as green. The obsolete habitat references in historical tests now restore only an exact hash-verified approved source snapshot and its matching historical ownership scope; the live Food contract independently checks the current chapter and retirement.

## Integration and boundaries

The independent final review found one additional factual error: veggieball pasta accepts vegan patty through the baked-cave-carrot ingredient tag. Both the paragraph and table now state the alternative in both languages. The selected cooking recipe and tag values were read directly, and the focused regression rejects the old exclusion.

Only Food source, its generated resources, necessary fishing-habitat retirement and incoming links, navigation/coverage synchronization, focused tests and this evidence are included. Machines, storage, Transport, accepted Combat, model settings, game installations and worlds are unchanged. The target is local dev, not a stable branch, and no push is authorized.

No Minecraft launch, scene execution, hover review or full-pack runtime verification was performed. Lucas's acceptance of the unmentioned Food pages is not replaced with another whole-chapter redesign or an additional mandatory gameplay approval cycle.
