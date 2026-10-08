# Guide integration review

## Outcome

This review found a concrete loader declaration mismatch for Create Ballast and several gameplay boundaries that the handbook must not present as verified. The strongest version-matched reports concern Deep Seas sealing and rope energy transfer in 2.2.4, plus Tempad moving portals in 3.0.4. Other reports need endpoint matching or gameplay validation before they become pack defect claims.

No mod, configuration, installation, export or live instance changed. No Minecraft startup or gameplay test ran, and no commit was made. Space is deferred. The Northstar rendering override remains on hold and was not reopened.

## Baseline and evidence

The selected baseline is `4491dfe`, Astropunk Chunky Baseline `0.3.0-grouped.chunky.4`, Minecraft `1.21.1`, NeoForge `21.1.255`. Provider release metadata and publisher descriptions came from the existing guidance research cache. Selected released archives came from the native packwiz cache, read-only. Every inspected archive matched its packwiz-declared digest before inspection.

Evidence labels remain separate. Declared support means a publisher or archive declaration. Source-supported mechanism means implemented released code or packaged data, including static decompilation. Reported problem means an upstream report, not local reproduction. Locally verified is reserved for behavior actually exercised here; no gameplay integration earned that label. Unknown means applicability, operation or repair is not established.

The structured companion contains exact artifact filenames, hashes, internal class or data paths, quoted evidence, selected versions, report version qualifications, mitigation state and validation requirements. High severity identifies load, survival, travel or inventory stakes, not certainty that an untested combination fails.

## Priority version matrix

| System | Selected releases | Evidence boundary |
| --- | --- | --- |
| Physics | Sable 2.0.6, Aeronautics bundled 1.3.2, Create 6.0.10 | Separate ordinary Create contraptions from Sable moving sublevels. |
| Submarines | Deep Seas 2.2.4 | Released oxygen, pressure, ballast and survival recipe code inspected; sealing not played. |
| Cooking | Farmer's Delight 1.3.2, Central Kitchen 2.6.1, Slice & Dice 4.3.3, Integrated Farming 1.4.2, Dragons Plus 1.11.9 | Native integrations present; complete recipe coverage not claimed. |
| Teleportation | Waystones 21.1.46, Waystones Sable 1.0.7, Tempad 3.0.4 | Moving destination bridge differs from fixed saved coordinates. |
| Death recovery | Corpse 1.1.13, Corpse Curios bridge 4.0.1 | Deck motion and saved recovery coordinates remain separate. |
| Power and fuel | Electro Energetics 1.21.1-1.1.3, Liquid Fuel 2.1.1-1.21.1, AeroEngine filename 1.3.0 | AeroEngine internal mod version is 1.0.2. Electricity and fuel bridges are not interchangeable. |
| Portable storage | Backpacks 1.3.5, Easy Shulker Boxes 21.1.3, Reinforced Shulker Boxes 3.2.1+1.21.1, Sophisticated Inventory Interactions 0.1.9.160 | Menu interaction and storage preservation require separate validation. |
| Encounter rewards | Bosses'Rise 2.1.2, Cataclysm 3.33, Better Combat 2.4.0+1.21.1-neoforge, Spell Engine 1.10.7 | Check selected combat version in structured metadata; melee data does not prove class reward coverage. |

## Actionable findings
### GI-01 Create Ballast declares an incompatible loader ceiling

Severity is high. Evidence is source-supported mechanism.

`ballastmod-0.1.0.jar`, `META-INF/neoforge.mods.toml, dependencies.ballastmod, neoforge.versionRange` supports the recorded mechanism.[23] Local `pack.toml` selects `21.1.255`.

Mitigation: no repository mitigation found. No ballastmod dependency override was found in the repository search. A launcher-side override was not inspected.

Proposed action: Notify Lucas and request approval before any release replacement, removal or dependency override. Do not silently bypass the declared check.

Validation needed: An authorized fresh import must establish whether this declaration blocks loading, then exercise the selected counterweight if retained.

Guide boundary: Do not present this counterweight as an available working construction step before resolving the declared loader mismatch.[23]

### GI-02 Deep Seas ballast and oxygen instructions need released-code corrections

Severity is medium. Evidence is declared support, source-supported mechanism.

`create_submarine-2.2.4.jar`, `BallastVentBlockEntity.tickBallastTank` supports the recorded mechanism.[1] `create_submarine-2.2.4.jar`, `OxygeneDiffuserBlockEntity.tick` supports the recorded mechanism.[1] `create_submarine-2.2.4.jar`, `OxygeneDiffuserBlockEntity.tick, elected owner and gameTick modulo 20` supports the recorded mechanism.[1]

Mitigation: not mitigated in guidance. The startup preferences screen is suppressed by configureddefaults/config/create_submarine-common.toml. No hull-strength gameplay override was found.[40]

Proposed action: Document rotation, nonzero redstone and sea exposure for the vent. Document oxygen, redstone and an assembled Sable sublevel for the diffuser. Do not repeat the size-proportional consumption claim: the inspected active-owner drain is constant in this release.

Validation needed: Test vent fill and drain direction, redstone control, sea exposure, diffuser warmup, power loss and two different cabin sizes.

Guide boundary: Creative Oxygenator is a creative aid, not the survival oxygen supply. Survival recipes for the Electrolyzer, Oxygen Diffuser, ballast tank, vent and barometer are packaged. Pressure resistance is not average block strength.[1][40]

### GI-03 Deep Seas 2.2.4 has a version-matched sealing report

Severity is high. Evidence is reported problem, source-supported mechanism.

Create: Deep Seas version: 2.2.4 Report uses Sable 2.0.3, Aeronautics 1.3.0, Create 6.0.10 and NeoForge 21.1.233; pack uses Sable 2.0.6 and Aeronautics 1.3.2.[26] Hermetic (sealed): no Closed report, maintainer comment says fix without naming a released fix version.[26] `create_submarine-2.2.4.jar`, `SubmarinePressureSystem.getWeakestHullDepth` supports the recorded mechanism.[1]

Mitigation: unconfirmed for selected artifact. Selected 2.2.4 was published 2026-06-17. Report closed with a fix comment on 2026-09-25. Closure does not establish a fix in the selected artifact.[40]

Proposed action: Keep submarine survival guidance conditional until a simple enclosed cabin passes sealing and pressure checks. Seek approval for any version change only after matching a release to the reported fix.

Validation needed: Test a small vanilla-block sealed cabin with survival diffuser and creative control separately, add a door and Copycat blocks, inspect barometer response, then repeat after save and reload.

Guide boundary: The released pressure calculation traverses sealed compartment hull blocks, checks exposure and full collision shapes, and resolves Copycat material data. This is implemented logic, not confirmation that the report is fixed in the pack.[26][1][40]

### GI-04 Deep Seas 2.2.4 rope can retain unintended energy transfer

Severity is medium. Evidence is reported problem.

Hey there just noticed in the newest version: 2.2.4 that the rope also transfers energy between two rope attachments, wich should only happen if steel cable is used Exact Deep Seas version match; other selected endpoint versions not supplied.[27] after some investigation it happens because if only one side is borken of the rope the other one stays in the steel cable mode Reporter follow-up, not locally reproduced.[27]

Mitigation: unconfirmed for selected artifact. Maintainer says fix on 2026-09-25, after the selected artifact publication.[40]

Proposed action: Do not teach ordinary rope as an intentional electrical cable. Keep rope, steel-cable electrification and converter-based power transfer distinct.

Validation needed: Compare fresh rope against steel cable, then break and replace one endpoint while watching attached consumer energy.

Guide boundary: A report of energy transfer is not evidence that a rope is a supported cable for every electrical system.[27][40]

### GI-05 Deep Seas tall-machine placement has a storage duplication report

Severity is high. Evidence is reported problem, unknown.

You can do it with storage and dupe contents of it. Issue 77 supplies reproduction steps but no explicit mod version; applicability to selected 2.2.4 is unknown.[28]

Mitigation: unconfirmed. Maintainer says fix on 2026-09-25 without identifying a released version. Do not claim selected 2.2.4 is affected or repaired solely from issue chronology.[40]

Proposed action: Flag the storage-loss and duplication checkpoint to Lucas. Avoid teaching occupied-block placement around the diffuser or electrolyzer as a useful construction technique.

Validation needed: In an authorized disposable world, use inexpensive marked contents, attempt machine placement under occupied upper space, wrench the neighboring block and count all resulting storage and contents.

Guide boundary: Treat this as a reported exploit candidate, not a reproduced pack defect or a reason to remove Deep Seas.[28][40]

### GI-06 Submarine electrical supply has a real converter bridge, not automatic cable compatibility

Severity is medium. Evidence is declared support, source-supported mechanism, unknown.

`create_submarine-2.2.4.jar`, `ElectrolyzerBlockEntity.energyStorage` supports the recorded mechanism.[1] `create_submarine-2.2.4.jar`, `ElectrolyzerBlockEntity.tick` supports the recorded mechanism.[1] `electroenergetics-1.21.1-1.1.3.jar`, `ConverterBlockEntity$ConverterEnergyStorage.class` supports the recorded mechanism.[9]

Mitigation: bridge selected, vehicle operation unverified. Electro Energetics includes a Forge Energy converter and assembly migration hooks. No additional electrical mod is justified merely to satisfy the FE consumer.[40]

Proposed action: Teach the realistic electrical circuit and converter as distinct from Forge Energy consumers. Do not imply direct wire interchangeability or that every machine works across a moving boundary.

Validation needed: Power an electrolyzer from a converter on land, assemble the same circuit onto a submarine, move, unload, reload and reconnect. Verify oxygen production and energy storage persistence under load.

Guide boundary: Selected Electro Energetics PantographBlockEntity performs Sable pose transformations. This supports a moving-contact mechanism, not blanket electricity compatibility. Issue 238 was corrected by the author as a voltmeter wired in series, and the reporter accepted the correction, so it is not evidence that all vehicle consumers fail.[1][9][30]

Additional supporting evidence.[40]

### GI-07 Liquid Fuel does not make every vehicle engine accept the same fuel

Severity is medium. Evidence is source-supported mechanism, unknown.

`createliquidfuel-2.1.1-1.21.1.jar`, `com/forsteri/createliquidfuel/mixin/MixinBlazeBurnerTileEntity.class` supports the recorded mechanism.[10] `AeroEngine-1.3.0.jar`, `EngineCombustorBlockEntity.getFuelConsumptionRate` supports the recorded mechanism.[21]

Mitigation: separate implementations already selected. AeroEngine published filename is AeroEngine-1.3.0.jar but its internal mod version is 1.0.2. Preserve both when reporting a defect.

Proposed action: Give burner fuel and AeroEngine aviation kerosene separate guide entries. Do not claim that Liquid Fuel supplies kerosene recipes or arbitrary engine interoperability.

Validation needed: Verify actual kerosene recipe in the selected item browser, combustion and start controls, afterburner consumption, refilling while moving, and fuel persistence after save and reload.

Guide boundary: Liquid Fuel targets Blaze Burners. A reference to fuel consumption in an engine is not evidence of accepting all liquid fuels.[10][21]

### GI-08 Kitchen integrations overlap in inputs but retain distinct automation roles

Severity is medium. Evidence is declared support, source-supported mechanism.

`create-central-kitchen-2.6.1.jar`, `CuttingBoardRecipeConverters.canSaw` supports the recorded mechanism.[2] `create-central-kitchen-2.6.1.jar`, `CuttingBoardRecipeConverters.SAWING and DEPLOYING` supports the recorded mechanism.[2] `sliceanddice-4.3.3-neoforge.jar`, `FarmersDelightCompat.shouldConvert` supports the recorded mechanism.[3]

Mitigation: native coverage selected. Farmer's Delight 1.3.2, Create 6.0.10 and Dragons Plus 1.11.9 meet Central Kitchen 2.6.1 declared minimums. Repository settings enable sawing, deploying and heated basin cooking.[41][42]

Proposed action: Retain distinct guide paths: Central Kitchen packages and arms into cooking tools plus knife-compatible sawing and tool-specific deploying; Slice & Dice provides slicer cutting and heated basin cooking; Integrated Farming provides harvesting, roosts, nets and moving-world farming hooks. Do not recommend removal as duplicate mods.

Validation needed: Compare manual and automated rice-panicle cutting including straw, an axe recipe, one pot meal with a bowl, milk or honey conversion, recipe reload and packaged orders. Check recipes contributed by every selected Delight addon before promising coverage.

Guide boundary: Conversions depend on recipe types, accepted tools, automation eligibility and settings. No exhaustive food coverage is verified. Legacy Central Kitchen sequenced sandwich, pie and fluid claims must not be copied into 2.6.1 guidance.[2][3][4]

Additional supporting evidence.[41][42]

### GI-09 Central Kitchen has new filter and feast-serving reports

Severity is medium. Evidence is reported problem, unknown.

Noticed in my game that the saw doesn't check for filters on recipes on the generated cutting board recipes. Open pull request 207, no release version supplied.[35] the mechanical arm does not replace the final portion with a new block when supplied or place the final portion into a storage medium targetted. Open issue 206, Minecraft 1.21.1 but no Central Kitchen release specified.[36]

Mitigation: not confirmed mitigated. Both were opened 2026-10-07, after the selected 2.6.1 publication. They are concrete new reports, not version-confirmed pack failures.[41]

Proposed action: Keep saw filter routing and unattended final-portion replacement out of guaranteed instructions until validated. Match any proposed fix to an approved published artifact, not an open pull request.

Validation needed: Test two competing cutting outputs with a configured saw filter. Serve an entire feast through an arm, confirm the final serving reaches storage and replacement occurs.

Guide boundary: Ponder instructions are helpful but can disagree with reported final-serving behavior.[35][36][41]

### GI-10 Moving farming has shipped hooks, but net collection still needs lifecycle validation

Severity is medium. Evidence is declared support, source-supported mechanism, reported problem.

`create-integrated-farming-1.4.2.jar`, `released integration classes` supports the recorded mechanism.[4] `create-integrated-farming-1.4.2.jar`, `released integration classes` supports the recorded mechanism.[4] `create-integrated-farming-1.4.2.jar`, `released integration classes` supports the recorded mechanism.[4]

Mitigation: publisher reports repair, pack not gameplay verified. Issue 62 was closed with New release should fix this issue. Selected 1.4.2 changelog also specifically fixes premature rice harvesting and water removal.[42]

Proposed action: Use native moving-farm support rather than proposing a missing integration addon. Keep net-to-auger storage transfer conditional until demonstrated.

Validation needed: Harvest mature and immature submerged rice on a moving structure, confirm water and seed retention, collect a coplanar net panel through an auger, then test full storage, unloaded vessel and reconnect.

Guide boundary: Hook presence and an upstream fix statement do not verify the assembled pack or every aquatic creature.[4][37][42]

### GI-11 Waystones tracks moving destinations, but unloaded-ship arrival has an open report

Severity is high. Evidence is declared support, source-supported mechanism, reported problem.

`waystonessable-1.0.7.jar`, `SableWaystoneEventHandler.onPrepareTeleport` supports the recorded mechanism.[5] `waystonessable-1.0.7.jar`, `SableWaystoneEventHandler.onTeleportEntityPost` supports the recorded mechanism.[5] the destination is outside the world bounds Issue 13 has multiplayer reports, no complete exact endpoint matrix in the issue body. Snapshot 1.0.8 attempts are not selected.[31]

Mitigation: partial declared mitigation. Waystones 21.1.46 and bridge 1.0.7 are selected on both sides. Older traversal and Twinbound issues have explicit intervening fix statements; the unloaded-destination report remains open.[43]

Proposed action: Distinguish fixed-site and moving-ship Waystones. Warn that returning to an unloaded vessel is not yet verified. Do not install the snapshot, force-load all ships or use destructive player-data repair instructions without approval.

Validation needed: Test land to loaded moving vessel, vessel to land, ship to ship, unloaded destination, save and reload, assembly and disassembly discovery state, warp plates and ordinary non-operator multiplayer users.

Guide boundary: Create Waystones Recipes changes crafting, not moving coordinates. The bridge is meaningful, not a redundant themed recipe addon.[5][31][32]

Additional supporting evidence.[33][43]

### GI-12 Tempad 3.0.4 fixed saved locations do not follow a moving vessel

Severity is high. Evidence is source-supported mechanism, reported problem.

`tempad-1.21.1-3.0.4-all.jar`, `CreateLocationPacket.type$lambda$4` supports the recorded mechanism.[6] Currently, when on a Create Aeronautics contraption the portal drifts away when moving. Open feature request 190 explicitly names Tempad 3.0.4, Minecraft 1.21.1 and NeoForge.[34]

Mitigation: no selected moving-portal bridge established. Fixed saved location captures player position and dimension. Tempad also has separate marker and player-broadcaster handlers, so not every destination type should be described as fixed.

Proposed action: Teach saved locations as stationary endpoints, not a return-to-current-ship function. Prefer a validated Waystones moving destination for that role. Label player broadcast and marker behavior separately.

Validation needed: Record a location on land and on a ship, move the ship, open and enter portals; separately test broadcaster, marker and workstation behavior while moving and after reload.

Guide boundary: Do not describe Tempad as only portable or fuel-powered. Selected release includes workstation and metronome blocks, and chronon generation is a distinct system from Forge Energy.[6][34]

### GI-13 Corpse deck following does not make the saved death location a live recovery target

Severity is high. Evidence is source-supported mechanism, unknown.

`corpse-neoforge-1.21.1-1.1.13.jar`, `Death.fromPlayer` supports the recorded mechanism.[7] `corpse-neoforge-1.21.1-1.1.13.jar`, `Death.fromPlayer` supports the recorded mechanism.[7] `corpse-neoforge-1.21.1-1.1.13.jar`, `CorpseEntity.createFromDeath` supports the recorded mechanism.[7]

Mitigation: Curios recovery bridge selected, moving-deck recovery unverified. Corpse x Curios API Compat 4.0.1 addresses accessory inventory, not demonstrated live corpse coordinates. Prior Corpse conclusions were static-code findings, not gameplay verification.

Proposed action: Keep corpse physical attachment and saved death-history coordinates separate. Do not promise history teleportation or compass guidance returns to the corpse on the current deck. Do not replace Corpse merely because a ragdoll addon exists.

Validation needed: Die on a moving deck and while seated, move the vessel away, find and open the physical corpse, compare death history and recovery compass, unload and reload, reconnect and recover all Curios and backpack contents.

Guide boundary: Generic Sable entity tracking supports a possible movement mechanism. It does not prove the corpse is attached at creation or that its inventory survives every vessel lifecycle.[7][8]

### GI-14 Vehicle storage and portable backpack menus have separate preservation paths

Severity is high. Evidence is source-supported mechanism, declared support, unknown.

`sable-neoforge-1.21.1-2.0.6.jar`, `released Create capability integration class` supports the recorded mechanism.[8] `1.3.5-backpacks_mod-1.21-1.21.1.jar`, `data/backpacks/function/bp/control/tp.mcfunction` supports the recorded mechanism.[11] `1.3.5-backpacks_mod-1.21-1.21.1.jar`, `data/backpacks/function/bp/container/save/main.mcfunction` supports the recorded mechanism.[11]

Mitigation: mechanisms present, no full preservation verification. Backpacks 1.3.5 changelog fixes contents sometimes not being saved. This does not certify moving-deck menus. Sophisticated Inventory Interactions is a screen utility, not an installed Sophisticated backpack progression.[44]

Proposed action: Keep placed ship inventories, carried backpack menu entities and carried shulker interactions separate. Do not promise all reinforced shulkers or every vehicle inventory support direct item access. Test backpacks in survival, not creative.

Validation needed: Use counted distinct items in chest, backpack and reinforced shulker. Open each while moving, transfer items, assemble and disassemble, save and reload, reconnect, die, recover, and use two players concurrently. Compare counts before and after every transition.

Guide boundary: Backpacks uses command-controlled menu entities and item saving. This is a concrete interaction surface to validate, not evidence of actual item loss in the pack.[8][11][39]

Additional supporting evidence.[17][25][44]

### GI-15 Boss weapons have melee integration, not proven class-reward progression

Severity is medium. Evidence is source-supported mechanism, unknown.

`block_factorys_bosses-2.1.2-neo-1.21.1.jar`, `data/block_factorys_bosses/weapon_attributes/knight_sword.json` supports the recorded mechanism.[13] `L_Ender's Cataclysm 1.21.1-3.33.jar`, `data/cataclysm/weapon_attributes/coral_spear.json` supports the recorded mechanism.[14] `L_Ender's Cataclysm 1.21.1-3.33.jar`, `data/cataclysm/curios/slots/hands.json` supports the recorded mechanism.[14]

Mitigation: duplicate roll already disabled in repository. Combat Roll remains selected. The boss client roll indicator is still enabled independently and is not permission to change it.

Proposed action: Describe boss equipment as encounter rewards with some native Better Combat data and Cataclysm Curios slots. Do not claim spell-school bonuses, spell binding or equivalent rewards for every class. Propose a targeted reward mapping only after a concrete missing school, tag or slot is demonstrated.

Validation needed: Check melee animations and special attacks on representative boss weapons, spell binding and school attributes for caster rewards, archer ammunition and weapon roles, effective accessory slots and non-stacking limits, then assess fights with several class builds.

Guide boundary: No evidence establishes a generally out-of-place boss addition or justifies removal. Fighting a boss using class abilities and integrating its loot into class progression are separate claims.[13][14]

## Restrictions and non-findings

Deep Seas rejects a specifically declared old Sodium artifact token, `mc1.21.1-0.6.13-neoforge`, while this pack selects `sodium-neoforge-0.8.13+mc1.21.1.jar`. That is not a declaration that all Sodium releases are incompatible. Publisher descriptions that say any Sodium version must not override the released metadata. Iris and Veil lighting remain a separate appearance check; this review does not propose renderer replacements.[1]

The Deep Seas archive registers Abyss content and packages `data/create_abyss/dimension/abyss.json`. Do not call it wholly future content from the current publisher description. Registration and packaged terrain do not prove successful access or safe vessel transfer. Space remains deferred.[1]

No addition was established as generally out of place or wholly redundant. The Ballast counterweight and Deep Seas water ballast are different mechanics. The cooking addons share ingredients but expose different machines and transport paths. Sable Physics Compat supplies block physics properties, not proof of working machines, inventory transfer or teleportation. Sophisticated Inventory Interactions is a screen utility, not Sophisticated Backpacks.

No missing integration addon is recommended from absence of tests. The confirmed gaps are guidance boundaries: fixed Tempad endpoints, unverified Corpse recovery coordinates, incomplete class reward mapping and untested vehicle inventory lifecycles. Any pack change requires Lucas's approval.

## Additional inspected evidence

The bounded reward survey also inspected released Bosses'Rise, Better Combat and Spell Engine artifacts.[13][15][16]

The storage survey inspected Reinforced Shulker Boxes and the block-property survey inspected Sable Physics Compat.[18][12]

Create and Dragons Plus artifacts establish the selected native integration providers, not full recipe coverage.[19][20]

Aeroworks and the bundled Aeronautics artifact were inspected without promoting their presence into general fuel or inventory compatibility.[22][24]

The Electro Energetics issue about nonworking vehicle devices was closed after the author identified a voltmeter wired in series and the reporter accepted the wiring correction.[38]

The Deep Seas common oxygen-tag proposal is unmerged and targets development source. The selected diffuser accepts its own registered oxygen fluid, so guidance must not promise arbitrary oxygen interchangeability.[29][1]

## Coverage limits

GitHub searches and repository issue retrieval covered the named combinations, not every issue or selected mod. The first 100 issues and pull requests from each named repository were inspected for relevant leads, with exact selected issue discussions fetched separately. Closed reports and current development branches were not treated as proof of released fixes. Older unrelated Corpse vehicle reports and electrical wiring mistakes were not promoted into incompatibility claims.

Direct page extraction hit rate limits on two requests. GitHub API retrieval supplied those discussions. The bytecode inspection utility was unavailable, so existing CFR and an existing Java runtime supplied static decompilation. Neither Minecraft nor released mod code executed.

## Sources

[1] https://cdn.modrinth.com/data/mva5q4qZ/versions/UcXaPVeD/create_submarine-2.2.4.jar (create_submarine-2.2.4.jar)
[2] https://cdn.modrinth.com/data/btq68HMO/versions/FaEwZ1Pr/create-central-kitchen-2.6.1.jar (create-central-kitchen-2.6.1.jar)
[3] https://cdn.modrinth.com/data/GmjmRQ0A/versions/N67LJgrN/sliceanddice-4.3.3-neoforge.jar (sliceanddice-4.3.3-neoforge.jar)
[4] https://cdn.modrinth.com/data/9k1pAsfR/versions/90PTskVE/create-integrated-farming-1.4.2.jar (create-integrated-farming-1.4.2.jar)
[5] https://cdn.modrinth.com/data/BxhPGfcK/versions/Wot8Pf4C/waystonessable-1.0.7.jar (waystonessable-1.0.7.jar)
[6] https://cdn.modrinth.com/data/gKNwt7xu/versions/T26aJH7E/tempad-1.21.1-3.0.4-all.jar (tempad-1.21.1-3.0.4-all.jar)
[7] https://cdn.modrinth.com/data/WrpuIfhw/versions/Zwf8nv8y/corpse-neoforge-1.21.1-1.1.13.jar (corpse-neoforge-1.21.1-1.1.13.jar)
[8] https://cdn.modrinth.com/data/T9PomCSv/versions/fg9dTRz9/sable-neoforge-1.21.1-2.0.6.jar (sable-neoforge-1.21.1-2.0.6.jar)
[9] https://cdn.modrinth.com/data/qYJdIoAx/versions/KWxEmmON/electroenergetics-1.21.1-1.1.3.jar (electroenergetics-1.21.1-1.1.3.jar)
[10] https://cdn.modrinth.com/data/sH9tXU9f/versions/7oNrI3y9/createliquidfuel-2.1.1-1.21.1.jar (createliquidfuel-2.1.1-1.21.1.jar)
[11] https://cdn.modrinth.com/data/MGcd6kTf/versions/uJz7ESID/1.3.5-backpacks_mod-1.21-1.21.1.jar (1.3.5-backpacks_mod-1.21-1.21.1.jar)
[12] https://cdn.modrinth.com/data/sZbcIrJb/versions/Ucq7afTi/sablephysicscompat-1.3.0.jar (sablephysicscompat-1.3.0.jar)
[13] https://cdn.modrinth.com/data/q2bV1Tm1/versions/lE9PF6Wp/block_factorys_bosses-2.1.2-neo-1.21.1.jar (block_factorys_bosses-2.1.2-neo-1.21.1.jar)
[14] https://cdn.modrinth.com/data/46KJle7n/versions/PsPYpoCC/L_Ender%27s%20Cataclysm%201.21.1-3.33.jar (L_Ender's Cataclysm 1.21.1-3.33.jar)
[15] https://cdn.modrinth.com/data/5sy6g3kz/versions/VhIOvcXP/bettercombat-neoforge-2.4.0%2B1.21.1.jar (bettercombat-neoforge-2.4.0+1.21.1.jar)
[16] https://cdn.modrinth.com/data/XvoWJaA2/versions/wKITXgNx/spell_engine-neoforge-1.10.7%2B1.21.1.jar (spell_engine-neoforge-1.10.7+1.21.1.jar)
[17] https://cdn.modrinth.com/data/gA5euN8S/versions/OBp8ltOS/EasyShulkerBoxes-v21.1.3-1.21.1-NeoForge.jar (EasyShulkerBoxes-v21.1.3-1.21.1-NeoForge.jar)
[18] https://cdn.modrinth.com/data/xlOwuSdN/versions/PZOyr6QP/reinforced-shulker-boxes-3.2.1%2B1.21.1.jar (reinforced-shulker-boxes-3.2.1+1.21.1.jar)
[19] https://cdn.modrinth.com/data/LNytGWDc/versions/UjX6dr61/create-1.21.1-6.0.10.jar (create-1.21.1-6.0.10.jar)
[20] https://cdn.modrinth.com/data/dzb1a5WV/versions/b0u9vk8C/CreateDragonsPlus-1.11.9.jar (CreateDragonsPlus-1.11.9.jar)
[21] https://cdn.modrinth.com/data/CRh10iJF/versions/eqi1VZul/AeroEngine-1.3.0.jar (AeroEngine-1.3.0.jar)
[22] https://cdn.modrinth.com/data/P26k79kP/versions/6kk7ruR3/aeroworks-1.5.0.jar (aeroworks-1.5.0.jar)
[23] https://cdn.modrinth.com/data/5ypXYrfG/versions/uJwkM1Xh/ballastmod-0.1.0.jar (ballastmod-0.1.0.jar)
[24] https://cdn.modrinth.com/data/oWaK0Q19/versions/44pLdPGg/create-aeronautics-bundled-1.21.1-1.3.2.jar (create-aeronautics-bundled-1.21.1-1.3.2.jar)
[25] https://cdn.modrinth.com/data/orgY0JIo/versions/wiUUWZ2E/sophisticatedinventoryinteractions-1.21.1-0.1.9.160.jar (sophisticatedinventoryinteractions-1.21.1-0.1.9.160.jar)
[26] https://github.com/MaxCreateMC/Create-Deep-Seas/issues/73 (deep seal)
[27] https://github.com/MaxCreateMC/Create-Deep-Seas/issues/74 (deep rope)
[28] https://github.com/MaxCreateMC/Create-Deep-Seas/issues/77 (deep dupe)
[29] https://github.com/MaxCreateMC/Create-Deep-Seas/pull/85 (deep oxygen)
[30] https://github.com/MaxCreateMC/Create-Deep-Seas/issues/81 (deep power)
[31] https://github.com/SShakusora/WaystonesSable/issues/13 (waystone unloaded)
[32] https://github.com/SShakusora/WaystonesSable/issues/6 (waystone hang)
[33] https://github.com/SShakusora/WaystonesSable/issues/11 (waystone twinbound)
[34] https://github.com/terrarium-earth/Tempad/issues/190 (tempad sable)
[35] https://github.com/DragonsPlusMinecraft/CreateCentralKitchen/pull/207 (kitchen filter)
[36] https://github.com/DragonsPlusMinecraft/CreateCentralKitchen/issues/206 (kitchen portion)
[37] https://github.com/DragonsPlusMinecraft/CreateIntegratedFarming/issues/62 (farming net)
[38] https://github.com/george8188625/Create-Electro-Energetics/issues/238 (electric wiring)
[39] https://github.com/Eclipse-Studios/backpacks/wiki/%E2%9A%A0%EF%B8%8F-Compatibility (backpack creative)
[40] https://api.modrinth.com/v2/version/UcXaPVeD (Selected release metadata for create-deep-seas)
[41] https://api.modrinth.com/v2/version/FaEwZ1Pr (Selected release metadata for create-central-kitchen)
[42] https://api.modrinth.com/v2/version/90PTskVE (Selected release metadata for create-integrated-farming)
[43] https://api.modrinth.com/v2/version/Wot8Pf4C (Selected release metadata for waystones-sable)
[44] https://api.modrinth.com/v2/version/uJz7ESID (Selected release metadata for vanilla-backpacks)
