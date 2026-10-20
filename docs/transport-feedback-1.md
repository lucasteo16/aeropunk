# Transport screenshot corrections, round one

The first export is superseded by the feedback-one export. Its exact manifest remains in `transport-feedback-prior-review.json`; its archive is preserved. Changes are confined to ten Transport topic pairs, their generated pages, the two localized chart assets, asset provenance and focused regression and review evidence. Version remains `0.18.0-dev`. No installation, commit, merge or push was performed.

## Screenshot dispositions

| Report | Cause | Correction |
| --- | --- | --- |
| Image one | Authored item reference used the wrong namespace for Rudder. | Use `create_high_seas:rudder`, registered by the High Seas code bundled in the selected Deep Seas artifact. This was a documentation defect, not a player setup error. |
| Images two and six | Width-filling ItemGrid blocks were placed inside table cells. The structural compiler accepted the tree but did not prove visible column layout. | Removed that table pattern throughout Transport. Kept the same actual item families as bounded, labeled icon rows outside tables. |
| Image three | Obsidian was an unrelated visual placeholder for a comparison of non-portal travel systems. | Removed it and used the actual Waystone, Sharestone, Warp Plate and Tempad equipment. No portal mechanic was removed. |
| Create waystone recipe omission | The page omitted the main rewritten Create recipes and showed only a recoloring recipe. | Added exact ingredient layouts for Warp Stone and ordinary Waystone, including empty positions, output counts and the Mechanical Crafter requirement. The recipe definitions are copied into `transport-waystone-recipes.json` from the checksum-selected recipe addon. |
| Image four | Fluid Hose had a stale resource model but no corresponding available item registration. | Removed its icon, broken item link and invented component requirement, retaining fuel-supply instructions. |
| Image five | One combined bilingual chart crowded its labels, with lines crossing the text baseline. | Separate English and Chinese images. The drawing positions each rule sixteen source pixels below the actual text bounding box. Both images were opened and visually checked. |
| Image seven | Levitite Blend is a registered fluid, not an item, and was passed to an item-link component. The section also displayed unrelated propellers. | Use the registered bucket only for native item visuals and name the fluid as fluid in curing instructions. Show Levitite and its fluid bucket in that section; move propeller models to Trim and thrust. |

## Breathing behavior

The selected artifact is `cosmonautics-26.08.307.jar`. `GlobalSpacePhysicsHandler` is an event-bus subscriber for `rocketnautics`. Its `onLivingBreathe` method is subscribed at highest priority. Where the atmosphere flags include `DROWNING`, it sets the living breathing event to false, except for invulnerable players. Creative-mode testing therefore does not establish that survival players can breathe there.

The Space Helmet extends Create's `DivingHelmetItem`. Cosmonautics integrates with Create backtank air through `BacktankUtilMixin`; this is a breathing and equipment system, not an independent cabin-atmosphere simulation. Deep Seas and Deep Air provide the separate oxygenated-compartment integration documented on the same page. No new in-game suffocation experiment was performed.

Evidence is retained under `build/transport-final/feedback`: `breathing.txt`, `breathing-event-registration.txt`, `high-seas-registry.txt`, `aero-fluids.txt`, `rocket-items.txt` and the pre-correction source snapshot. The prior oxygen and height disassembly is unchanged.

## Recipe presentation

The selected Create Waystones Recipes release is `create_waystones_recipes-3.0.1.b.jar`. Its two definitions use the `create:mechanical_crafting` serializer. Create's `MechanicalCraftingRecipe` extends `ShapedRecipe`, but returns its own mechanical-crafting recipe type. The selected GuideME `RecipeTypeMapping.tryCreate` dispatches by recipe type, not superclass alone. Its standard crafting renderer therefore cannot be assumed to display these recipes through the ordinary Recipe tag.

Instead, the guide shows the exact recipe positions with fixed-size native ItemImage cells and output references. Unlike the rejected catalog grids, each cell contains at most one fixed-size item image. The source distinguishes ingredient placement from the crafters' output-arrow directions. The ordinary Waystone recipe produces two Waystones. The Warp Stone recipe produces one Warp Stone. Emerald-tag slots are illustrated by emeralds and identified as tag alternatives. The item-browser action remains available for the live recipe view and variants.

A regression compares every displayed position, including every empty cell, and each output count against the copied selected recipe definitions in both languages.

## Preservation and verification

The reference-correction record gives an explicit disposition for each retired or corrected identifier. Preservation gates now apply those exact per-topic dispositions rather than requiring broken references to remain forever. No arbitrary missing identity is exempted. Prior source and resource evidence is preserved separately.

The selected engine parser and structural compiler pass all thirty localized pages. Image decoding, references, source scope, per-topic bilingual native identity parity and authored and generated section visuals pass. Focused Transport, feedback, Food preservation, Machines preservation and query presentation checks pass. The full repository suite and a game launch were not run. The corrected resource pack must still be inspected in the game to confirm the final layout; a structural pass is not rendered verification.

## Method correction

The initial export was overconfident about source readiness because normalized registry substitutions cannot detect missing mod items, and a structural compiler cannot detect an overflowing table. The correction pass begins with the actual screenshot errors, traces the exact selected registrations, and rejects the failed layout pattern across the chapter. Future reports must keep those evidence boundaries explicit. Language assets are now separated before rendering, and chart spacing is checked using actual ink bounds instead of baseline assumptions.
