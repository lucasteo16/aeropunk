---
navigation:
  title: "Space life support"
  position: 0
  parent: reference.vehicles.md
  icon: rocketnautics:space_helmet
item_ids:
  - rocketnautics:space_helmet
  - rocketnautics:jetpack
  - rocketnautics:copper_leg_thrusters
  - rocketnautics:copper_anchor_boots
  - cosmonauticsdeepair:gravity_generator
  - create_submarine:electrolyzer
  - create_submarine:oxygene_diffuser
---

# Space life support

## Breathing in space

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

The Space Helmet has no crafting recipe. A craftable breathing setup uses <ItemLink id="create:copper_diving_helmet" /> with a charged <ItemLink id="create:copper_backtank" /> in the head and chest slots. Charge the backtank before wearing it, using its Ponder instructions. A charged <ItemLink id="create:netherite_backtank" /> is another air source. The Jetpack supplies air from fuel instead of stored compressed air.

<Recipe id="create:crafting/appliances/copper_diving_helmet" />

<Recipe id="create:crafting/appliances/copper_backtank" />

<ItemGrid>
  <ItemIcon id="rocketnautics:space_helmet" />
  <ItemIcon id="rocketnautics:jetpack" />
</ItemGrid>

<ItemLink id="rocketnautics:space_helmet" />

A Space Helmet allows breathing in space when paired with a pressurized air source. The Cosmonautics Jetpack is a pressurized source as well as a powered flying chestplate. Wear the helmet in the head slot and the Jetpack in the chest slot. The Jetpack supplies pressurized air by slowly consuming its fuel. Its systems also need to be enabled for personal flight.

<Recipe id="rocketnautics:crafting/equipment/jetpack" />

The Jetpack holds Lava. Its tooltip describes refilling with a <ItemLink id="minecraft:lava_bucket" /> and filling beneath a <ItemLink id="create:spout" />. Use <KeyBind id="key.rocketnautics.toggle_jetpack" /> to toggle personal flight. The mod default is G. Disable flight when it is not needed to conserve fuel, without disabling the pressurized air supply.

<ItemLink id="rocketnautics:jetpack" />

***

## Sealed spacecraft rooms

<EmiSearch query="@cosmonauticsdeepair" /> <EmiSearch query="@create_submarine" />

<ItemGrid>
  <ItemIcon id="create_submarine:electrolyzer" />
  <ItemIcon id="create_submarine:oxygene_diffuser" />
  <ItemIcon id="cosmonauticsdeepair:gravity_generator" />
</ItemGrid>

<ItemLink id="create_submarine:electrolyzer" />

<Recipe id="create_submarine:electrolyzer" />

Use Deep Seas compartment tools to make an intact, sealed room inside a Sable ship. The Electrolyzer needs water and Forge Energy to make oxygen. Connect that oxygen supply to an Oxygen Diffuser inside the sealed room. The diffuser needs oxygen in its tank and a redstone signal. Deep Air restores breathing for entities in that sealed, unbreached, oxygenated compartment. It does not make oxygen or seal the hull.

<ItemLink id="create_submarine:oxygene_diffuser" />

<Recipe id="create_submarine:oxygen_diffuser" />

To restore gravity in that compartment, place a Gravity Generator within it, provide Forge Energy and give it a neighboring redstone signal. It is active when it is inside a Sable sublevel and both its signal and energy conditions are met. Oxygen supplies breathing. Gravity requires the separate active Gravity Generator, but does not require an oxygen supply.

<ItemLink id="cosmonauticsdeepair:gravity_generator" />

<Recipe id="cosmonauticsdeepair:gravity_generator" />


Deep Air reads sealed compartments and oxygen diffuser state from Deep Seas. Keep the compartment unbreached and the oxygen supply running. Ponder lessons for the Electrolyzer and Oxygen Diffuser show their power, oxygen and redstone requirements.

- [Orbital flight](space.vehicle-transfer.md) Build and fly the physical spacecraft.
- [Space destinations](space.destinations.md) Moon and Mars destination information.

***

## Personal movement

<ItemGrid>
  <ItemIcon id="rocketnautics:copper_leg_thrusters" />
  <ItemIcon id="rocketnautics:copper_anchor_boots" />
</ItemGrid>

<ItemLink id="rocketnautics:copper_leg_thrusters" /> use pressurized air for flight and inertial damping. Toggle damping with <KeyBind id="key.rocketnautics.toggle_dampeners" />. The mod default is Z.

<Recipe id="rocketnautics:crafting/equipment/copper_leg_thrusters" />

<ItemLink id="rocketnautics:copper_anchor_boots" /> help keep you grounded near a supporting floor. They do not create gravity throughout a room and do not ground an actively flying player.

<Recipe id="rocketnautics:crafting/equipment/copper_anchor_boots" />


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Cosmonautics: Deep Air](space.life-support.md) | Connects sealed Deep Seas compartments to space breathing and powered artificial gravity. | <EmiSearch query="@cosmonauticsdeepair" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
| ![Create Deep Seas](images/catalog-mva5q4qz.png) [Create Deep Seas](vehicles.water.md) | Adds marine vehicle components for Aeronautics boats and submarines. | <EmiSearch query="@create_submarine" /> |
