# Cosmonautics content and visual quality review

## Result

Repaired the authoritative English and Simplified Chinese content, rather than accepting passing generated-page tests as a writing review. Dimensions now contains distinct Moon, Mars and Deep Space sections with authentic images and concise terrain inventories. Retired the authored Space destinations topic. All links in handbook-content.json now point to Dimensions instead of that retired page. Orbital flight, life support and navigation remain substantial Transport articles.

This worker did not change the generator, placements, navigation audits, coverage, versions, gameplay settings, final generated pages or exports. Other workers own those changes. No game or server was launched. No commit or push was made.

## Review basis

Read handbook-authoring-standard.md, the area catalog and reference catalog templates, and the polished Overworld, Nether, End, aviation engine, industrial power and fishing sections. Compared the authored sources changed by 6849f16 against its parent and the selected main baseline f5c24f3. Inspected the generated-page changes for catalog and retired-topic effects. Read cosmonautics-independent-review.md and cosmonautics-evidence.json, then checked selected archives and relevant cached decompiled implementation again.

Recomputed the selected metadata digests for Cosmonautics 26.08.307, Expansion 1.0.0, Deep Air 1.0.2, Deep Seas 2.2.4, Create and AeroEngine fuel compat 0.0.2. They matched. The Moon dimension references seven lunar biomes. Mars references three biomes. Both link to surface dimensions. Deep Space uses an empty flat generator with the vanilla void biome. Biome display labels in this review are readable names derived from those identifiers, since the inspected packaged English language files did not provide biome names.

## Article inventory

Every unique article changed by 6849f16 is listed below, including deleted and generated-only articles. Inherited engine and provider changes were also included.

| Article | Finding and disposition |
| --- | --- |
| world.dimensions | Replaced the duplicated generic space summary with Moon, Mars and Deep Space sections. Added seven lunar and three Mars biome entries and authentic terrain or sky images. Removed implementation discussion and the destination-page redirect. Kept Overworld, Nether and End catalogs intact. Access guidance links remain standalone. |
| space.destinations | Retired from the authoritative authored source. Terrain and destination scope moved into Dimensions. Flight boundaries and display controls have their existing substantial homes rather than duplicated explanations. All authored source links replaced. |
| space.vehicle-transfer | Rewrote dense engine and transfer prose into propulsion equipment, departure, surface entry and related-topic sections. Retained Lava, strict departure above world Y 20,000, inward planetary entry and world Y 19,000 return placement. Retained the descent hazard. Removed physical-handle and planetary-record terminology. Did not invent steering or safe landing. |
| space.life-support | Rebuilt into personal equipment, Jetpack fuel, oxygenated rooms, local gravity and personal movement. Added labeled native grids and comparison tables. Retained craftable Copper Diving Helmet and backtank entry, the uncraftable Space Helmet, fuel-backed air, separate gravity and breathing, optional leg thrusters and anchor boots. Added an authentic gravity-room gallery capture. |
| space.navigation | Added the official Hologram Table capture. Separated the display, Sputnik Probe and helmet display into sections. Removed duplicated planetary-record discussion and description-of-description prose. Retained the distinction between overview and automatic flight. |
| vehicles.engines | Reviewed the inherited fuel compatibility paragraph against the checksum-selected addon and existing binary evidence. Replaced ship-patch and refinery-balance commentary with an actual fuel visual, original fuel, TFMG kerosene support and standalone industrial and orbital links. Retained the actual fuel-acceptance boundary. |
| travel.destinations | Confirmed the distinction between moving player destinations, whole-ship relocation within one dimension and orbital travel. Added the substantial orbital-flight link without duplicating flight instructions. |
| food.fishing | Corrected the English and Chinese clam-chowder sentence together. Removed installed-mod and fallback-route commentary. Kept the heated cooking pot and serving bowl instruction, capture distinctions and existing item visuals. |
| power.industry | Reviewed the TFMG machinery and fuel context. Preserved its actual machine catalog and honest incomplete-help qualification. Added the missing separator before related topics. |
| performance.baseline | Reviewed the shared optimizer additions. Moved shared optimizer content before related topics and restored the separator, rather than leaving another content section after the closing links. No measured performance claims added. |
| reference.vehicles | Removed the standalone Space destinations entry from authored Transport content. Kept orbital flight, life support and navigation together. Directory ordering and sidebar presentation belong to the navigation worker. |
| reference.machines-storage | Generated-only query ordering change. The new ordering has the same exact producer query tokens. No authored mechanics repair required and no generated file edited. |
| reference.technical | Generated catalog retired-provider removals and optimizer relinking reviewed. Current provider destinations belong to maintained articles, not removed deferred pages. Generator and coverage work remain with their owner. |
| performance.deferred | Deleted deferred page reviewed. Useful optimizer descriptions are already in Performance. No retired placeholder reintroduced. |
| server.deferred-pack-loading | Deleted deferred Paxi page reviewed. No absent loader tutorial or placeholder added. |
| technical.space-bridge | Deleted Northstar compatibility page reviewed. No retired Northstar mechanic or misleading compatibility statement retained in the authored space articles. |

## Provider metadata and queries

Reviewed all four newly added provider descriptions, bilingual purposes and item queries. Exact selected-release publisher descriptions and identifiers remain in handbook-project-descriptions.json. Do not replace them with newer website marketing, which can describe different functionality.

Expansion's bilingual purpose now describes Mars terrain, plains, frostlands and caves instead of the implementation term planetary record. Cosmonautics and Deep Air purposes remain concise and consistent with selected artifacts. AeroEngine fuel compat has no independent item catalog, so its two producer queries remain intentional.

| Provider metadata key | Query |
| --- | --- |
| mods/create-cosmonatics.pw.toml | @rocketnautics |
| mods/create-cosmonautics-expansion.pw.toml | @rocketnautics_addon |
| mods/cosmonautics-deep-air.pw.toml | @cosmonauticsdeepair |
| mods/aeroengine-fuel-compat.pw.toml | @aeroengineering and @tfmg |

The misspelled create-cosmonatics metadata filename is exact and must not be normalized. The Oxygen Diffuser item is create_submarine:oxygene_diffuser. Its recipe is create_submarine:oxygen_diffuser. Both remain exact.

## Authentic assets and generator handoff

Downloaded the actual four publisher icons from the official Modrinth project API. All four decode and visibly contain project artwork, not minecart placeholders. Converted them to 96-pixel PNG images, giving compact 24-pixel provider images under GuideME's ordinary scaling. Sidebar ItemImage identifiers are a separate global uniqueness concern and must not be used instead of these publisher logos.

The generator's existing provider icon convention is a handbook-visual-sources.json entry keyed by the exact metadata path. Read its resource field when rendering a provider roster row. Do not add a parallel mapping or use a fallback item icon when this entry exists.

| Metadata key | Resource |
| --- | --- |
| mods/create-cosmonatics.pw.toml | images/cosmo-micg1ith-icon.png |
| mods/create-cosmonautics-expansion.pw.toml | images/cosmo-gd7m0igy-icon.png |
| mods/cosmonautics-deep-air.pw.toml | images/cosmo-rzqxjxfo-icon.png |
| mods/aeroengine-fuel-compat.pw.toml | images/cosmo-rnuszf19-icon.png |

Added four clean official gallery captures for Mars terrain, the cosmic sky, Hologram Table and gravity equipment. Inspected images directly. Images have no blocking marketing captions, interface overlays or watermarks. Gallery captions and shader qualifications stay in provenance, not production copy. The Hologram Table image contains its actual in-world visualization, not a synthesized diagram. The gravity capture illustrates equipment appearance, not a tested construction recipe.

The official Cosmonautics gallery and description had no usable Moon landscape image. Targeted searching found the identifiable Create: Cosmonautics, moon sneakpeek video by the web channel. Its thumbnail contains real lunar terrain but also interface and a foreground machine. The guide uses only a clean 500 by 300 terrain crop. No pixels were generated or retouched. The relationship of that channel to the Modrinth publisher and the precise release depicted are not independently established, so the record calls it an identified video thumbnail crop, not a confirmed official gallery capture. It is an appearance illustration, not mechanics evidence.

All nine added assets have lowercase resource paths, original and resource SHA-256 hashes, dimensions, source and project URLs, author or project identity, license metadata and rights qualifications. Original downloads remain in scratch. Images were proportionally reduced or, for the Moon, cropped. No tutorial imagery, artificial screenshots or user-supplied images were needed.

## Released mechanics and unresolved risks

The independent report's important distinctions remain in the revised copy.

- Rocket Thruster consumes supported fluid, including Lava, rather than Create rotation. Mechanical crafting belongs in the recipe browser because the selected GuideME mapping does not support that recipe type. Its Ponder scene is registered, but its six explanation keys are absent from the selected packaged language files. Written essential fuel guidance therefore remains necessary.
- SpaceTransitionHandler checks logical ship height strictly above the dimension threshold and a valid physics handle. Its return target is the dimension threshold minus 1,000. DeepSpaceInstance checks the distance to the current linked orbital body's surface. The code establishes those conditions, not a tested flight route.
- GlobalSpacePhysicsHandler heats descending ships between world Y 1,000 and 2,500 above 60 blocks per second. Stronger intensity damages nearby entities. No heat shield or safe touchdown method was established.
- Space Helmet is registered, but the prior whole-selected-inventory search found no survival recipe or override for it. The source does not invent one. Create's backtank tag and shaped helmet and backtank recipes were rechecked. The prior selected Create breathing inspection supports the inherited helmet route. Actual breathing remains a runtime check.
- Deep Air room breathing checks sealed, uncompromised, oxygenated compartments and ship breach status. Local gravity checks a separate active generator. Generator power and signal requirements were rechecked. Gravity does not require a diffuser in the same room and does not alter ship orbital gravity.
- The current official Deep Air description additionally warns that at least one room on the ship needs air because of Deep Seas compartment cleanup. Added this conservative practical instruction to both locales without claiming an oxygen prerequisite in every gravity room. The selected cleanup behavior was not independently decompiled in this review. This is publisher-reported guidance, not a reproduced failure.
- Expansion packages two equal-priority Mars records with conflicting radius and texture. The linked dimension can survive merging, but effective orbital geometry depends on input order. Do not convert a surface definition into a tested approach or accessibility guarantee.
- Deep Air's optional dependency identifier mismatch remains a runtime compatibility question, not proof that its breathing handler fails.

Expansion artwork is listed under All Rights Reserved. The Moon video image also lacks established redistribution permission. Project license metadata is not independent artwork permission, even for other gallery images. All assets record this honestly. Distribution permission requires a separate decision before release. No rights were fabricated and no download was treated as permission.

## Verification

Ran the six new source-quality tests in tests/test_cosmonautics_source_quality.py. All passed. The tests cover destination retirement, absence of authored stale links, sectioned bilingual structure, exact native-reference and visual parity, standalone topic links, forbidden production wording and punctuation, key mechanics, survival acquisition boundaries, publisher icon selection, provenance hashes, lowercase resource paths and PNG integrity with decompressed pixel data.

Resolved all ten authored space Recipe identifiers against the selected cached archives. They exist. The unsupported mechanical crafting Recipe component remains absent. Rechecked Moon and Mars biome membership against the actual dimension biome sources.

ImageMagick decoded all nine resulting images successfully. Direct visual inspection covered official Mars terrain, cosmic sky, Hologram Table, gravity room, the Moon source and its crop, and a contact sheet of the four publisher icons.

Final generation, final-resource parser and compiler checks, archive verification and rendered narrow-layout inspection are intentionally left to the parent. Source tests do not establish native live item registries, working recipes, tooltips, safe landing, breathable rooms, passenger or inventory preservation, save and reload, or compatibility in an actual game.
