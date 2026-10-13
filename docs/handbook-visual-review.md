# Handbook visual and creature review

## Image feedback revision

Lucas reviewed the official-launcher `0.11.1-g` installation and approved the visual result and merge into `dev`. This approval covers handbook presentation, not comprehensive gameplay, multiplayer or public artwork redistribution rights. Stable branches and played installations remain outside this merge request.

The current package is `dist/astropunk-0.11.1-g-modrinth.mrpack`. This revision adds twenty authentic image assets across nineteen topics without changing gameplay prose, native references, recipes or navigation. The original review record below describes `0.11.0-g` and remains historical.

Review Teleportation's Tempad section, Orbital flight, Mounted weapons, Radar, Enchanting, Materials and fuels, Liquid fuel, Rotational power, Martial classes, Aquatic wildlife, Block and mob information, Carry On and all seven Appearance subpages. Orbital flight shows a community Cosmonautics spacecraft above Earth, cropped to remove interface overlays. Materials and fuels uses Lucas's supplied desert oil-extraction screenshot. Liquid fuel has both its publisher burner illustration and Create tanks beside a Nether portal. Martial classes and Aquatic wildlife reuse existing family images.

The exact inserted image blocks and pre-feedback article hashes are in `handbook-image-feedback.json`. Source URLs, creator names, crop coordinates and output hashes are in `handbook-visual-sources.json`. The supplied Reddit post URL and creator were not provided, so its rights are explicitly unknown rather than attributed to an invented source. Newly sourced illustrations remain subject to public redistribution rights review.

Verification results for this revision are recorded separately in `handbook-image-feedback-verification.json`. Test image sizing, caption spacing, Earth visibility and readability of the Jade and radar displays in both languages. Existing launcher installations are not updated by building this package. Approval is still required before merging into development.

## Review package

Version `0.11.0-g` on `test/guide`, based on development commit `43ffb9f`. The new package is `dist/astropunk-0.11.0-g-modrinth.mrpack`. The earlier fishing package is retained. No changes have been committed, pushed, merged back into development or applied to a played installation during this visual pass.

## Scope

Reviewed the original 114 generated topics, including 111 authoritative authored topics and three generated directories. Added 67 authentic images, selected after inspecting publisher main descriptions and galleries. Fifty-five come from galleries and twelve from main-description embeds. Logos, badges, sponsorship banners and unrelated artwork were not used as gameplay illustrations. One Illager Invasion banner was cropped to its three creature designs, retaining only original image pixels and recording the crop.

The final handbook has 131 topics in each language. Of 113 non-root subpages, 82 have at least one subject image, or 72.6 percent. This count excludes small provider icons and provider-art fallback logos. Top-level directories were not given decorative filler images. Technical and administrative references, some compact utility pages and some machinery pages remain text-led. Dungeon guards and Cataclysm creatures retain their qualified catalogs without a fabricated appearance image.

The visual pass changes 63 existing authored topics and adds seventeen creature topics. The exact scope and unchanged pre-pass source are recorded in handbook-visual-pass.json and handbook-before-visual-pass.json. Native item references, recipes, bindings and search components on existing non-split pages are unchanged. Fishing steps, casting steps and console instructions now have shorter text blocks. Navigation outside Creatures is unchanged from the fishing package.

## Fishing and food

Fishing now shows an actual reeling scene, Tackle Boxes and living catches in aquariums. Fishing habitats shows the species Guide and its conditions. Seafood shows the three cooking addons' ingredients and dishes beside their respective sections. Cooking tools, farming, hunger, Nether food, underground food, End food and machine cooking have relevant kitchen, garden, feast or processing imagery. Native item grids and recipe searches remain available for actual interaction.

## Creatures

Creatures is now a short directory. Its direct children are Wildlife, Friends and foes, Aquatic wildlife, Creeper variants, Enderman variants, Hostile variants, Dungeon guards, Cataclysm creatures, Illagers and Summons. Existing encounter rows and qualifications were moved rather than discarded. Boss encounters remain under Bosses.

Aquatic wildlife is another concise directory. Its eight family pages contain all 120 ordinary biome-spawn species from the selected Hybrid Aquatic artifact:

| Family | Species rows |
| --- | --- |
| Freshwater fish | 17 |
| Marine fish and rays | 26 |
| Deepwater fish | 18 |
| Sharks | 13 |
| Jellyfish | 14 |
| Squid and octopuses | 6 |
| Seafloor wildlife | 22 |
| Aquatic mammals | 4 |

No family table exceeds thirty species. Each aquatic family has a relevant image, including habitat illustrations where the scene explains the place better than an isolated item icon. Snailfish was corrected from the former seafloor-invertebrate grouping into Deepwater fish. The publisher's duplicate Chinese Lionfish and Snailfish labels are disambiguated with their English names. Catch rules, natural-spawn resources and game content are unchanged.

## Broader visual improvements

Class articles show school-specific casting, armor or equipment. Related combat and skill pages show actual class systems rather than a generic logo. Building articles show materials, copycat shapes, bridges, train fittings, palette controls and displays. Storage and logistics show backpacks, vaults, inventory cleanup and package handling. Transport shows airships, engines, cockpits, trains and local tubes. Existing useful screenshots elsewhere were retained.

## Verification

All checks ran after generation and native export:

- Ten source-quality tests passed, covering authoring scope, untouched source, native interaction preservation, bilingual image and link parity, creature-row preservation, short family tables, image provenance, PNG checksums and decompressed pixel integrity.
- The released GuideME 21.1.19 parser accepted all 262 language pages with zero parse failures. Its malformed-tag negative control was rejected.
- Released navigation bytecode accepted 131 nodes in each language with eighteen ordered roots, correct sibling order, permitted depth and the existing stale-resource negative controls.
- The native structural compiler accepted all 262 pages with zero failing pages. It preserves a normalized vanilla item-registry boundary, and does not establish real mod registry, recipe, binding, image rendering or interaction behavior.
- Native archive verification compared all 702 handbook resource files byte-for-byte. All 313 development mod metadata files remain unchanged. Pack version, loader version and documentation exclusions passed.
- The whitespace check passed.

The raw summaries are in handbook-visual-verification.json. Measured image coverage is in handbook-visual-coverage.json. Original image URLs, publisher identities, project license metadata, crop coordinates, dimensions and hashes are in handbook-visual-sources.json. Project license metadata does not independently establish artwork redistribution permission. These images are prepared for local review, with publication rights still requiring review.

No Minecraft client or server was launched. A valid image and a passing compiler do not prove that the image is sized or rendered well in the game.

## Player review

1. Open Fishing and check the three subject images, their spacing and the shortened first steps.
2. Check Fishing habitats, Seafood, Cooking tools and Hunger and variety. Images should help identify the activity without pushing item references or recipes out of reach.
3. Open Creatures and confirm that its overview is short. Expand Aquatic wildlife and review Freshwater fish, Marine fish, Deepwater fish and one other family. Check both language versions and the Chinese Lionfish and Snailfish labels.
4. Check representative class, building, storage and vehicle pages. Arcane Wizard, Berserker, Copycat shapes, Bulk storage and Engines are useful samples.
5. At the normal interface width, check that images fit, captions remain short, narrow interface screenshots stay readable, native item tooltips still work and recipe searches still open.
6. If using an existing authoring instance with the new assets installed, perform a normal resource reload before judging newly added PNG images or the changed sidebar. Watched Markdown alone does not establish that new resource images have loaded.

Use a disposable world. Do not overwrite played worlds. Merge back into development only after Lucas approves the visual result and relevant game behavior.
