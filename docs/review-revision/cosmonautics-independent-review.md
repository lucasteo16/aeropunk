# Cosmonautics independent artifact review

## Scope and result

Reviewed both locales of `cosmonautics-authored-pages.json`, its evidence record, the four checksum-selected archives and the cached decompiled classes. No game, server or desktop was launched. Only this report was written. Gameplay, live registries, native recipe rendering and safe landing remain untested.

The fragment correctly distinguishes Moon and Mars surface definitions from the unlinked gas giant and ice world. Its main concrete error is the instruction to operate the Rocket Thruster through Create rotation. The larger omissions are actual rocket fuel, the implemented return transition, personal maneuvering equipment and its controls. Expansion also contains a conflicting Mars definition that the evidence record does not discuss.

## Evidence locations

Archive root is `/home/tsb/.hermes/cache/scratch/cosmo-author`.

- Base archive is `create-cosmonatics.pw.toml.jar`, selected Cosmonautics 26.08.307.
- Expansion archive is `create-cosmonautics-expansion.pw.toml.jar`, selected Expansion 1.0.0.
- Deep Air archive is `cosmonautics-deep-air.pw.toml.jar`, selected Deep Air 1.0.2.
- Deep Seas archive is `create-deep-seas.pw.toml.jar`, selected Deep Seas 2.2.4.

Independently computed SHA-512 digests matched all four values in the fragment evidence record. Base class citations below are relative to `decompiled/selected/dev/devce/rocketnautics` beneath that archive root. Deep Air class citations are relative to `decompiled/deep-air/dev/compat/cosmonauticsdeepair`. Line numbers refer to these cached decompilations, not upstream source. Archive resource paths are exact.

## Required correction

### 1. Rocket Thruster rotation instruction is unsupported

Affected page is `space.vehicle-transfer` in both languages. Remove “Use the Create rotation setup shown by the item's Ponder lesson to operate the engine.”

The released Rocket Thruster is not a kinetic block entity. `content/blocks/RocketThrusterBlockEntity.java:65-68` extends `AbstractThrusterBlockEntity`, which extends `SmartBlockEntity` in `content/blocks/AbstractThrusterBlockEntity.java:32-36`. Fuel consumption drives activation in `RocketThrusterBlockEntity.java:146-201`. The defaults are active with full target throttle at lines 76 and 84. Thrust applies through the Sable physics callback at lines 267-268. `content/blocks/AbstractRocketThrusterBlock.java:58-59` has an empty neighbor-change handler.

The registered Ponder sequence, `ponder/RocketPonderScenes.java:28-51`, shows a thruster and tank, text overlays and a right-click prompt. It contains no rotation or rotational-speed setup. Do not add a redstone on and off instruction for this thruster either. Its programmable controls are `setActive`, `setThrottle` and `writeValue` at lines 354-380, which are different from mechanical rotation.

### 2. The Ponder lesson cannot replace all written fuel guidance

The scene emits the six strings named `rocketnautics.ponder.rocket_thruster.text_1` through `text_6` in `ponder/RocketPonderScenes.java:37-50`. None of those keys appears in any packaged language JSON in the selected base archive. The scene is registered correctly in `ponder/RocketPonderPlugin.java:23-24`, but registration does not prove that its explanations are readable. Keep the Ponder reference, but supply the essential fuel instruction directly and retain native lesson rendering as an unresolved check.

## Useful missing mechanics

### 3. Name Lava as the guaranteed rocket fuel

Affected page is `space.vehicle-transfer`. “Fluid tagged as rocket fuel” gives the player no starting fuel.

Base `data/rocketnautics/tags/fluid/rocket_fuel.json` explicitly includes `minecraft:lava`. Its optional entries reference `#c:gasoline`, `#c:diesel`, `#c:diesel_sulfur`, `#c:kerosene`, `#c:hydrogen`, `#c:lpg`, `#c:petroleum_gas`, `#c:napalm` and `#c:naphtha`. Optional tags do not establish that those fuels exist in this pack. Recommend a short Lava instruction and leave optional alternatives to the recipe browser.

`RocketThrusterBlockEntity.java:68` has a 1,000 millibucket internal tank. Lines 232-239 require the rocket-fuel tag for acceptance and draining. Lines 209-229 apply different consumption multipliers according to the accepted fluid identifier. This is separate from the Jetpack's Lava-only filling behavior. Do not describe the engine as accepting arbitrary liquids.

### 4. Return from Deep Space has a released automatic boundary

Affected pages are `space.vehicle-transfer` and `space.destinations`. They explain departure but omit the implemented surface return. This is useful artifact-backed content even without a tested landing procedure.

`content/orbit/DeepSpaceInstance.java:213-235` identifies the current orbital planet, requires its linked dimension and permission to return, then compares distance from its surface against the transfer height. The distance calculation supports cube and sphere shapes. Crossing inward triggers `SpaceTransitionHandler.exitDeepSpace`, not a Hologram Table selection.

`content/physics/SpaceTransitionHandler.java:149-157` places the returning instance at the linked dimension's transfer height minus 1,000. Moon, Overworld and Expansion Mars records all specify 20,000, so the stated return height is Y 19,000. Lines 161-177 transfer players and ships. Explain that this is atmospheric or surface-dimension entry, not touchdown or autopilot. No exact interplanetary steering procedure or safe landing sequence was established by this review.

Departure requires the ship's logical Y to be strictly greater than 20,000, not merely equal to it, in `SpaceTransitionHandler.java:113-116`. The English “crossing” wording is suitable. Adjust the Chinese “达到 20,000” wording to make the strict boundary clear.

### 5. Add the landing hazard, without inventing a heat shield

`content/physics/GlobalSpacePhysicsHandler.java:136-159` registers ship physics and calls the reentry-heat routine. Lines 344-361 apply heat effects between Y 1,000 and Y 2,500 when downward ship speed exceeds 60 blocks per second. Higher intensity damages nearby living entities. This routine has no atmosphere or dimension restriction in its own body.

A brief warning to slow descent before that band is useful. Do not promise that a named hull material or unverified shield prevents the damage. Also do not use `applyFallingHeatDamage` at lines 418-430 as proof of an active player heat mechanic. Its helper body exists, but the inspected living-entity tick handler at lines 365-371 is empty.

### 6. Personal equipment coverage omits the movement and grounding pieces

Affected page is `space.life-support`. It shows only the helmet and Jetpack while discussing a personal space setup.

`registry/RocketItems.java:61-64` registers the Jetpack, `rocketnautics:copper_leg_thrusters`, `rocketnautics:copper_anchor_boots` and Space Helmet. Add the leg thrusters and anchor boots as optional movement equipment, not a compulsory complete suit.

- `content/items/LegThrustersItem.java:145-177` requires air unless the player has infinite materials and consumes air during flight or damping. Lines 181-206 implement inertial damping and grant creative-style flight through an attribute. The archive includes `data/rocketnautics/recipe/crafting/equipment/copper_leg_thrusters.json`.
- `content/items/AnchorBootsItem.java:45-55` adds downward motion. Lines 74-94 restrict it to a nearby supporting block and exclude actively flying players. Describe this as grounding near a floor, not gravity everywhere. The archive includes `data/rocketnautics/recipe/crafting/equipment/copper_anchor_boots.json`.

### 7. Use the actual current-binding identifiers and explain the Jetpack control

`RocketNauticsClient.java:162-164` defines three actions with released defaults G, Z and Y respectively.

- `key.rocketnautics.toggle_jetpack` toggles the worn Jetpack.
- `key.rocketnautics.toggle_dampeners` toggles damping when leg thrusters are worn, confirmed in `client/RocketNauticsClientEvents.java:134-140`.
- `key.rocketnautics.toggle_alignment` toggles the Space Helmet display in Deep Space, confirmed in `client/HelmetHudHandler.java:101-122`.

Show native KeyBind components rather than only “check Key Binds”. Label defaults separately. Do not imply that the alignment action steers the ship. Its lock branch at `HelmetHudHandler.java:135-137` is empty.

`content/items/JetpackItem.java:129-155` applies thrust while jumping and follows the player's look direction, with greater thrust and consumption while sprinting. Its implementation drains flight fuel before testing whether thrust is requested at lines 132-148. An enabled Jetpack can therefore drain fuel while not actively thrusting. Disabling it when personal flight is not needed is useful fuel advice. This does not disable its air-source interface, which has no active-system check at lines 289-322.

### 8. Backtanks and helmet acquisition need explicit coverage

The selected Create archive `create.pw.toml.jar` contains `data/create/tags/item/pressurized_air_sources.json`, listing `create:copper_backtank` and `create:netherite_backtank`. The base archive adds the Jetpack to that same tag. `content/items/SpaceHelmetItem.java:22-25` inherits Create's `DivingHelmetItem`. `mixin/BacktankUtilMixin.java:32-61` preserves original handling for non-`IBacktank` items while adapting the Jetpack interface.

This evidence supports documenting ordinary Create backtanks as air-source alternatives rather than presenting the Jetpack as the only personal breathing setup. Exact inherited breathing behavior should be checked against Create's released class before expanding that instruction into an exhaustive compatibility claim.

No recipe JSON anywhere in the selected base archive references `rocketnautics:space_helmet`. The item is registered, but this fragment does not establish survival acquisition. Do not invent a crafting recipe. Record the acquisition gap and inspect other selected recipe providers or existing pack overrides before presenting helmet crafting as a completed starting instruction.

## Destination and life-support qualifications

### 9. Expansion has two competing Mars records

The evidence record cites only `data/rocketnautics_addon/universe_planets/mars_planet.json`. Expansion also packages `data/rocketnautics_addon/universe_planets/mars.json`. Both have name `mars` and priority 1,000. The first has radius 1,590,000 and linked dimension `rocketnautics_addon:mars`. The second has radius 0.1 and no dimension data.

`content/orbit/universe/UniverseLoader.java:74-89` merges equal-priority records by name. `content/orbit/universe/builder/PlanetDefinitionBuilder.java:127-132` preserves whichever conflicting value is already present and fills missing fields from the next record. The link can survive either order, but the Mars radius and texture depend on the order of the two equal-priority inputs. This is not proof that Mars is inaccessible. It is a concrete reason not to claim that the effective Mars orbital geometry and approach have been verified merely because a linked record exists. Add both records and the merge behavior to the evidence and retain the landing qualification.

### 10. Deep Air gravity does not require oxygen

The fragment largely gets compartment breathing right. `util/LifeSupportStatus.java:78-88` tracks breathing and gravity separately. The gravity result requires a sealed, uncompromised compartment, an active generator and no ship breach. It does not require an Oxygen Diffuser. Avoid wording that makes oxygen a gravity prerequisite.

`util/GravityGeneratorBlockEntity.java:65-96` requires a Sable sublevel, an enabled generator, a neighboring signal and sufficient energy. Consumption increases with room volume, using five energy units plus the ceiling of half the internal block count per tick. The status caches refresh after 40 ticks in `LifeSupportStatus.java:91-97`, so changes can be delayed. `mixin/EntitySubmarineGravityMixin.java:42-57` returns gravity 0.06 when the generator condition holds. It does not promise normal vanilla gravity or alter the ship's orbital gravity.

The Deep Air breathing handler actually restores the event in `event/CosmonauticsDeepAirEvents.java:25-44`. The known optional dependency identifier discrepancy remains in `META-INF/neoforge.mods.toml`, but is not evidence that this handler is disabled. Avoid inventing a failure from that metadata alone.

## Native references and limits

All seven recipe identifiers listed in `cosmonautics-evidence.json` correspond to actual selected archive recipe files. The diffuser spelling difference is intentional. `create_submarine:oxygen_diffuser` is the recipe identifier, while its output is `create_submarine:oxygene_diffuser`. Do not normalize either identifier.

Base equipment registration is evidenced in `registry/RocketItems.java:61-64`. Base block items have registration evidence in `registry/RocketBlocks.java`. Deep Air registration is in `init/ModRegistries.java`. Recipe resource presence and cached registration code are static checks, not a running registry or a successful native Recipe component render.

The bare Magnetic Stabilizer item reference in `space.life-support` needs a purpose. It is a gravity-generator recipe ingredient. Its own behavior is angular ship damping when powered, not gravity generation, in `content/blocks/MagneticStabilizerBlockEntity.java:48-63`. Either explain that distinction briefly or remove the unexplained standalone reference.

The report does not validate every recipe ingredient's live registration, loaded recipe availability, compartment assembly, interplanetary piloting, passengers, saved ships or export behavior. An attempted independent Create bytecode inspection was blocked because `javap` is unavailable. No tool installation or launch was performed.
