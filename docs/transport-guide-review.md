# Transport final review

The first export described below is historical and superseded by [screenshot correction round one](transport-feedback-1.md). The current exact source and resource closure is `transport-final-review.json`; the prior closure is preserved in `transport-feedback-prior-review.json`. Corrected and retired references have explicit dispositions in `transport-reference-corrections.json`.

Status: source-ready for Lucas's review, not merged. Development base: `543f6c0dbc599f4905e1366c78b7f02df0b4bce3`. The shared version remains `0.18.0-dev`. No launcher installation, world, runtime configuration, remote branch or accepted chapter was changed.

## Closed findings

| Topic | Review disposition |
| --- | --- |
| Transport | Reordered the landing choices to match all fourteen sidebar children: local travel, trains, water, vehicle construction and equipment, space, then teleportation. |
| Local transport | Retained the hypertube controls and exact references. Folded the bare branch subsection into its owning explanation. Added compact bilingual tutorial actions. |
| Train travel | Retained navigator, named stations and passenger-display operation. Replaced the oversized display strip with labeled compact form and configuration rows. |
| Railway building | Added station assembly, connected bogies and carriages, a manual route test, a seated conductor and actual schedule waiting conditions. Removed invented powered-bogie quotas, axle-load requirements and decorative bogie derailing claims. |
| Boats and submarines | Retained selected-release ballast vent behavior. Corrected oxygen budgeting against the selected diffuser tick method, rather than following its stale Ponder wording. Grouped hull, propulsion, pressure equipment and surface boats separately. |
| Vehicle assembly | Separated station-based trains from assembler-based Sable vehicles. Removed contradictory original-assembler retention instructions. Retained existing connection, winch and suspension coverage. |
| Controls | Retained desk, input modules, servos, sensors and receivers. Grouped catalogs by function and added a dedicated servo tutorial pair. |
| Engines | Retained propulsion families, fuels and turbine parts. Removed the invalid inference that different components' multipliers were directly comparable thrust ratings. |
| Airships | Retained buoyancy, burners, vents, levitite, trim and controls. Compacted equipment catalogs and folded camera bindings into the owning vehicle section without dropping any bindings. |
| Radar | Checked selected-release Ponder and tooltips for bearing, receiver, dish or plate, monitor, data links, network filters and fire control. Added a network-specific tutorial pair. |
| Mounted weapons | Distinguished big cannons from autocannons and cannon assembly from ship assembly. Corrected sliding-breech barrel-side loading, propellant placement and the cartridge's role. Removed the unsupported inference that the potato-cannon recoil setting proved no Big Cannons recoil. |
| Orbital flight | Removed the unverified gravity-feed fuel-tank placement rule. Added controlled descent and the actual arrival coordinate, transition height minus one thousand. Added a factual bilingual height schematic. |
| Space life support | Retained personal equipment and air supply. Corrected the repeated volume-based diffuser claim and linked the owning submarine explanation. |
| Space navigation | Removed the inverted low-gravity claim and the implication that every modeled body has a landable dimension. Corrected the atmospheric upper-bound interpretation after tracing its actual consumer. |
| Teleportation | Retained destination, scroll, shared endpoint, Tempad and Stargate instructions and native identities. Grouped existing inventories into compact functional families. |

## Release-specific evidence

The selected-artifact names and checksums, native recipe paths, exact source hashes, topic dispositions and every resource digest are bound in `transport-final-review.json`. Every baseline native item and recipe identity is retained per topic and locale. The inventory visual locations are aligned between languages; existing Chinese instructions were not mechanically translated from English.

### Oxygen

The checksum-matched selected artifact is `create_submarine-3.3.0.jar`. Its `OxygeneDiffuserBlockEntity.tick` checks redstone and available oxygen, obtains the containing Sable sublevel, claims the active submarine driver and, on the server every twenty ticks, drains a `FluidStack` of fifty units. That fixed drain contradicts the Ponder sentence about proportional volume consumption. The bytecode is retained under `build/transport-final/diffuser-bytecode.txt`.

### Atmosphere and transfer

The selected artifact is `cosmonautics-26.08.307.jar`, not an assumed newer release. `StandardUniverseProvider` assigns an empty Overworld atmosphere below the bound 5000, low-density and drowning flags below the bound 21000, and transition height 20000. `GlobalSpacePhysicsHandler.getFlags` calls `atmosphere.tailMap(integerHeight).firstEntry()`. Therefore the Overworld band starts above 5000, not above 21000. Moon and deep-space breathing need their own equipment; the selected map is not a realistic universal atmospheric model. `SpaceTransitionHandler` uses `transitionHeight - 1000` for surface arrival, producing 19000. The selected planet acceleration values are 11.0 and 2.0. Relevant disassembly is retained in `build/transport-final/space-bytecode.txt`, `global-space-bytecode.txt` and `atmosphere-bytecode.txt`.

The height schematic is original deterministic artwork showing those data, not a screenshot or a claim of a working spacecraft. It uses no third-party game image. It was visually inspected for legibility, then corrected to show the actual breathing boundary.

### Publisher and gameplay sources actually read

- Blocks & Bogies publisher source: https://github.com/WeidosOddities/Blocks-And-Bogies
- Deep Seas publisher release history: https://github.com/MaxCreateMC/Create-Deep-Seas/releases
- Big Cannons mount and loading references: https://mc-wiki.net/create-big-cannons/cannon-mount/ and https://mc-wiki.net/create-big-cannons/cannon-loading-guide/
- Publisher descriptions: https://modrinth.com/mod/create-radars, https://modrinth.com/mod/create-propulsion, https://modrinth.com/mod/aeroengine and https://modrinth.com/mod/create-deep-seas
- The selected Create, Big Cannons, Radar, Aeroworks and Deep Seas language and Ponder resources were extracted for targeted operation checks under `build/transport-final`.
- Partial transcript actually read: EtcProductions, “I Made A WORKING SUBMARINE in Minecraft (Create: Aeronautics)”, https://www.youtube.com/watch?v=5RnzghFDqww through https://youtubetotranscript.com/transcript?v=5RnzghFDqww. Only the opening excerpt was available. Its older generator setup and repeated volume-budget wording are not authoritative for the selected release. No whole-video viewing or complete transcript review is claimed.
- Earlier accepted version and system evidence remains in `docs/review-revision/cosmonautics-evidence.json` and `cosmonautics-quality-review.md`; selected-release checks above take precedence where versions or interpretations differ.

## Verification boundaries

All thirty pages pass the released GuideME syntax parser. The structural compiler also passes all thirty with its documented vanilla registry substitutions, recipe and key-binding skips and query normalization. This is not a real mod-registry or rendered client check. All twenty-four native recipe identifiers resolve to checksum-selected resources, including the nested Aeronautics, Offroad and Simulated artifacts; their serializers are supported vanilla crafting or furnace types. Every referenced local image fully decodes. Source and generated-page audits both exclude tutorial icons when checking section visuals. Native navigation was exercised in both languages with the selected NavigationTree bytecode and the existing negative controls.

Historical Food and Machines preservation checks were updated to reconstruct their exact prior revision, not to exempt arbitrary Transport changes. Exact Transport source and resource digests remain enforced, with negative controls for later owned and unrelated edits. The full source suite was not requested and was not run.

In-game layout, tooltips, query activation, registry resolution and actual vehicle operation remain player-testing checks. No game was launched. No commit, merge or push was performed.

## Bounded method review

The main avoidable cost was assuming equivalent catalog placement across languages before compacting the grids. Counts exposed the mismatch. The correction aligned only visual catalogs by section while preserving authored prose and complete topic-level identities. One consolidated pass then handled long strips, missing tutorial rows, references and factual corrections across all fifteen topics. The second factual review caught the atmosphere-map interpretation before export. Future passes should inspect the consuming lookup before turning a named configuration bound into a player threshold. No measured speed improvement is claimed because the earlier half-way timestamp was not recorded. Scope was kept to fifteen topic pairs; no additional research project or whole-guide rewrite was opened.
