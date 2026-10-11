# Handbook quality revision 0.6.2-g

## Scope

Merged latest main f5c24f3 before repairs, preserving the guide edition. Reviewed every article changed by the first Cosmonautics handbook revision, with the dispositions recorded in cosmonautics-quality-review.md. Main and the heavy edition were not edited. No live installation or launcher record was changed.

## Repairs

The four new provider rows now use actual publisher logos instead of generic minecarts. Nine authentic assets cover provider icons, lunar terrain, Mars terrain, the orbital sky, the Hologram Table and gravity equipment. Image provenance and rights qualifications remain in handbook-visual-sources.json.

Moon, Mars and Deep Space now share Dimensions with the existing world catalog. The separate Space destinations article is retired. Cosmonautics and Expansion provider links lead to Dimensions. Orbital flight, life support and navigation remain consecutive substantial Transport articles.

Every root and child list has explicit semantic positions. Transport runs through land, sea, sky, space and teleportation. Food keeps cooking tools and hunger first. Building starts with palette and placement before specialized families. Combat keeps equipment and controls before class abilities and growth. Utilities and Maps precede exploration roots, and Credits remains the final root. Detailed ordering is in scripts/handbook_navigation.py.

The authoring standard was corrected to match the current roots, Credits placement, explicit sibling order and complete-publication policy. Paxi was reconciled after the main merge as a data-pack loader without an item query.

## Parent verification

The repository suite passed all 138 tests after generation. The released native NavigationTree accepted 111 pages in each locale, all sibling orders and eighteen roots, including deliberate ordering failures and stale destination resurrection controls.

The released syntax parser accepted all 222 localized pages. The native structural compiler reported zero failing pages and passed malformed-child and identifier controls. Its item normalization, absent fixture images, and skipped runtime Recipe and KeyBind compilation remain explicit boundaries.

Source validation checked 2,012 links. Native archive validation matched 579 resource files and all 297 selected main mod metadata files. The broader baseline assertion also checked resource-pack and shader metadata and the automatic world-border data pack against f5c24f3. Archive integrity, all nine new image bytes, destination-page retirement and generator idempotence passed. Whitespace checks passed.

Export is dist/astropunk-0.6.2-g-modrinth.mrpack. SHA256 is 9e9e0877bc0dbfe287423308ff65a9eccb5a883262150d880982d272ffd5fe73.

## Remaining boundaries

No game or server was launched. Native rendering, item references, recipe displays, current-binding labels and gameplay remain separate checks. The current official installation still contains 0.6.1-g and was not silently updated.

The Moon image is an identifiable video terrain crop, not a confirmed exact-release publisher capture. Expansion artwork and that crop lack independently established redistribution permission. Their provenance is retained for local review and must be resolved before public redistribution. Selected-release Mars data conflicts, missing rocket demonstration translations and Space Helmet acquisition limitations remain documented rather than concealed.
