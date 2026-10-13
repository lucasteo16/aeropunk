# Fishing handbook testing

## Review package

Current review version `0.11.0-g` on `test/guide`, based on development commit `43ffb9f`. The visual follow-up adds gameplay images and focused creature catalogs. Its current checklist and verification are in [Handbook visual review](handbook-visual-review.md). The latest local development changes were merged into the retained guide branch before authoring. The remote does not have a development branch. No guide changes have been merged back into development, pushed or deployed to a played instance.

Import `dist/astropunk-0.11.0-g-modrinth.mrpack` into a fresh testing instance. The older guide instance does not establish that the newly added fish, recipes and item references are loaded. Use a disposable world, and do not overwrite a played world or its installation.

## Initial fishing update

The new English and Simplified Chinese articles are Fishing habitats and Seafood under Food and farming, and Aquatic wildlife under Creatures. Fishing habitats and Seafood follow Fishing consecutively in the sidebar. Cooking tools and Hunger and variety retain their first and second positions.

Fishing now introduces Starcatcher equipment, attachments, bait, its minigame and the Hybrid Aquatic bridge. Seafood contains the existing Spawn food and capture material alongside Starcatcher's Delight, Hybrid Delights and Ocean's Delight. Hunger and variety now explains Short Stacks with verified nutrition-based examples and the original item-limit boundary.

Existing related pages cover aquatic terrain, Tidal Towns, fishing boats, selective materials, unified fuels, shader bridges, ship inspection and the replacement advancement screen. Strut Your Stuff is correctly classified as a supporting library rather than a standalone item catalog. Unrelated authored articles remain unchanged. Coverage and provider records were reconciled with the development selection, and new publisher icons have provenance records.

## Initial 0.10.2-g automated verification

Verification ran after the content edits and native export.

- Five fishing source-quality tests passed, including preservation of unrelated authored articles and matching native references and links across both languages.
- The released GuideME 21.1.19 parser accepted all 228 pages, with zero parse failures, and rejected its malformed-tag negative control.
- Released navigation bytecode accepted both language trees, each with 114 nodes and eighteen ordered roots. Semantic-order and stale-resource negative controls passed.
- The native structural compiler accepted all 228 pages, with zero failing pages. Its item identifiers are normalized at the vanilla registry boundary. It does not verify the modded item registry, recipe loading, key bindings, image rendering or actual game interaction.
- Thirty-six referenced items from the new fishing and seafood mods have matching item-model resources in the exact selected archives. This is resource evidence, not a live-registry test.
- Native archive verification compared all 601 handbook resource files byte-for-byte, retained all 313 development mod metadata files unchanged, checked the loader and pack versions, and confirmed documentation and scripts are excluded.
- The archive validator initially expected GuideME to be a guide-only addition. Development already contained it. That stale expectation was corrected, and the failed archive check was rerun successfully. Player content did not need another editing cycle.
- The whitespace check passed.

No Minecraft client or server was launched for this authoring update. Rendering and gameplay remain pending Lucas's test.

## Player acceptance checklist

- Open the handbook and inspect Food and farming. Confirm Fishing, Fishing habitats and Seafood are consecutive, with no duplicate roots or unrelated page movement.
- Switch between English and Simplified Chinese. Check the new pages, tables, publisher icons, item tooltips and recipe searches at the normal interface width.
- Open Creatures, then Aquatic wildlife. Check that the species tables remain readable and the fishing, seafood and boat links work.
- Craft the Starcatcher rod and guide. Check attachment changes through a Tackle Box, the displayed minigame binding, and ordinary water fishing.
- Check a cold, warm, cherry and cave habitat in a disposable world. Confirm readable habitat labels and species conditions in Starcatcher's own guide. A biome match alone is not a guaranteed catch.
- Inspect seafood recipes for the three new cooking addons and the retained Spawn ingredients. Check that the shown items exist and that the intended recipes load.
- Compare food stacks with their hunger restoration values. Confirm that Short Stacks never increases an item's original smaller stack limit.
- Inspect Tidal Towns in newly generated Deep Ocean terrain, separately from reading its catalog.
- Check Better Advancements, Jade on a Sable ship, shared material outputs and fuel acceptance where those features are being tested.
- Test shaders disabled first, then deliberately enable Reimagined and inspect Create machines and ship effects. The Veil bridge is an alpha release.

Merge the guide changes into development only after Lucas approves the rendered handbook and the relevant gameplay tests.
