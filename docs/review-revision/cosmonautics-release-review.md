# Cosmonautics handbook review

## Release

Astropunk Light Handbook 0.6.1-g remains on the test/guide branch for review. Main and the heavy edition were not merged or edited by this revision. No game, server or launcher was started, and no launcher records or existing installations were changed.

## Changes

The English and Simplified Chinese handbook now covers space destinations, orbital flight, surface entry, personal breathing equipment, sealed compartment oxygen, artificial gravity and planetary displays. Dimensions was updated for Cosmonautics and Expansion. Retired Northstar and deferred pages were removed from distributed resources, with historical evidence retained separately.

The independent artifact review corrected the unsupported rotational engine instruction, identified Lava as an available rocket fuel, documented return altitude and descent heating, and separated gravity from oxygen. Mechanical crafting stays in the recipe browser rather than using an unsupported native recipe display.

## Verification

The parent reran the repository suite with 122 passing tests. All 224 localized pages passed the released GuideME parser. Native navigation accepted 112 nodes per locale with eighteen ordered roots and passed its negative controls. Source validation checked 2,016 links.

Native export validation matched 572 resource files and confirmed 297 baseline mod metadata files unchanged, with no added mod metadata. The archive integrity check passed, and all 858 native override files matched the independent uncompressed game folder. The uncompressed export contains 1,157 files whose checksums are recorded in its ownership manifest.

The generated player pages contain no Work in progress, WIP, not installed, Northstar or equivalent checked Chinese placeholder wording. Detailed helper and structural compiler results and their boundaries are recorded in cosmonautics-integration-verification.json.

## Review artifacts

The native Modrinth archive is dist/astropunk-0.6.1-g-modrinth.mrpack. Its SHA256 checksum is f10cdbec88b1104043cd3f0674dac695635f4c42db8712b13c8a47f2c3d82590.

The launcher-independent folder is dist/astropunk-0.6.1-g-review-instance. It has not been registered in the official launcher.

## Remaining gameplay checks

Rendered layout, live recipe and item references, current-binding labels, transfer, destination approach, landing, passengers, inventory preservation, compartment breathing, gravity and saved ships require game testing. Static parser and packaging checks do not establish these behaviors.

Selected Expansion contains conflicting equal-priority Mars radius and texture records. Rocket Ponder explanatory translation keys are missing. Deep Air declares a different optional base dependency identifier. These findings are recorded in the evidence, not repaired by changing gameplay files.

No Space Helmet recipe was found across the selected mod archives and repository recipe overrides. The handbook documents a craftable Create breathing alternative rather than inventing an acquisition recipe. Dedicated station and docking mechanics were not established. Redistribution permission for bundled third-party artifacts is not established by this local review export.
