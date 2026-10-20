# Reviewer B, second verdict: still rejected

Parent read the actual returned fragment.json, not the narrative report. Resume the same session. Preserve original research and outputs, write revised results as revision2-fragment.json, revision2-evidence.json and revision2-notes.md within your directory. Limit this to eight minutes and the failures below, not another full scan.

The correction of Chipped paths and removal of renderer commentary are acknowledged and settled. Do not undo them. Recipe-resource evidence is useful but remains separate from real registry/runtime evidence.

Blocking presentation defect: you replaced mixed icon strips with tables of ItemLink TEXT only, which removes all visual identification from almost every section. ItemLink is a localized tooltip label, NOT a rendered item icon. The user explicitly requested visible icons for identifying tools and items. Use the accepted Combat comparison pattern: a compact native ItemGrid inside a table cell, adjacent ItemIcon children with no whitespace, and a visible name/role alongside. Each row is a coherent family or one real item. No tool-input-output strip.

Example shape, adapt only to verified identifiers:
| Dish | Identify it | Ingredients or use |
| --- | --- | --- |
| <ItemLink id="starcatcher_delight:hosomaki_common" /> | <ItemGrid><ItemIcon id="starcatcher_delight:hosomaki_common" /></ItemGrid> | Common fillet, kelp and rice |

Do not create a grid for each paragraph or a huge display before a repeated full table. Keep compact meaning, and match visuals in BOTH locales.

Specific factual and structural defects:
- Seafood: 'Three more dishes' table has two dishes plus raw fillet labeled 'Not a dish'. This directly repeats the user's criticism of mixing food/ingredients/none. Remove that row into an actual ingredient or cooking note with correct cooked output identifier, or retire it with reason. Keep sushi batch quantities and separate single-serving dishes, all columns consistent. Validate the universal all-tiers-same-ingredients assertion or limit it to checked recipes. Do not assert the next batch cannot start until output is taken without checking the pot's internal meal buffer.
- Seafood: first steps still use plain cutting board/knife words, not recognizable native identification. Add appropriate tool identification without recreating the mixed strip. 'Appear on the board' versus thrown outputs must match actual interaction.
- End: 'a dragon leaves one egg and one set of breath when it dies' is new unsupported misinformation. Remove it. Dragon breath collection during the encounter and egg acquisition are separate mechanics. Do not manufacture a universal death drop. 'Only egg dishes use the shell' also needs evidence or removal. Do not replace this with generic warning/filler.
- Portable: vanilla shulker crafting says one shell, but the vanilla recipe requires two shells. Correct both locales and use a supported native recipe if it helps. The tier upgrade paragraph is still long recipe narration; move actual layouts into native recipes where useful or concise comparisons, keep operation and meaningful differences.
- Portable: reinfshulker capacities were removed despite being core comparison information. Verify actual pack values or mark this as unresolved, rather than claiming the page complete with 'larger than copper'. Existing capacities are evidence to reconcile, not permission to guess. Do not keep inherited Easy Shulker Boxes or Shulker Drops Two claims unless checked. Drop the name-derived Chipped 'metal/mechanism themed' family claim and replace it with exact workstation function supported by recipes or documentation. Do not infer alchemy workstation outputs from its name.

Use docs/handbook-correction-gameplay-research.md for sources parent actually read. Avoid redoing prior scans. Return exact per-finding fixed/unresolved statuses. No source integration, generator/test edits, game launch, installs or commits. Parent will check visuals and facts again. No need to claim rendering was performed.
