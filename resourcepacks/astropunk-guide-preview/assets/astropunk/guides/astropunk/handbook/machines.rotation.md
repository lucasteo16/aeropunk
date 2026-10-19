---
navigation:
  title: "Rotational power"
  position: 3
  parent: reference.machines-storage.md
  icon: create:cogwheel
---

# Rotational power

## Stress before speed

<EmiSearch query="@create" />

Every rotating network has a capacity from its generators and an impact from its machines. While impact stays under capacity the whole network turns. The moment impact exceeds capacity the network stops and nothing on it works.

This pack keeps the stress mechanic on, so the first question at any machine is not how fast it should spin but whether the network can carry it.

<ItemGrid><ItemIcon id="create:water_wheel" /><ItemIcon id="create:large_water_wheel" /><ItemIcon id="create:windmill_bearing" /><ItemIcon id="create:steam_engine" /></ItemGrid>

| Source | Capacity | Note |
| --- | --- | --- |
| <ItemLink id="create:water_wheel" /> | 32 stress units | Cheapest steady source |
| <ItemLink id="create:large_water_wheel" /> | 128 stress units | Four times the wheel, same footprint height |
| <ItemLink id="create:windmill_bearing" /> | 512 stress units | Needs a sail assembly above it |
| <ItemLink id="create:steam_engine" /> | 1024 stress units | Needs a boiler and water supply |

The pack leaves the global speed limit at 256 revolutions per minute. Impact grows with speed, and the configuration states that a machine's cost doubles for every speed increase it receives, so gearing a line faster buys throughput at the price of capacity.

***

## Turning and reversing

<EmiSearch query="@create_connected" />

A <ItemLink id="create:shaft" /> passes rotation straight through. A <ItemLink id="create:cogwheel" /> changes the axis by a quarter turn. A <ItemLink id="create:gearbox" /> splits one input into four directions.

<ItemGrid><ItemIcon id="create:shaft" /><ItemIcon id="create:cogwheel" /><ItemIcon id="create:large_cogwheel" /><ItemIcon id="create:gearbox" /><ItemIcon id="create:wrench" /></ItemGrid>

| Part | What changes |
| --- | --- |
| <ItemLink id="create:shaft" /> | Nothing, same axis and speed |
| <ItemLink id="create:cogwheel" /> with a second cogwheel | Direction of the second axis reverses |
| <ItemLink id="create:large_cogwheel" /> meshed with a small one | Speed changes by the size ratio, direction reverses |
| <ItemLink id="create:gearbox" /> | Four faces, opposite faces turn the same way |

Create: Connected fills the gaps in that set. Each part answers a different routing problem.

| Part | Difference |
| --- | --- |
| <ItemLink id="create_connected:cross_connector" /> | Relays rotation in two directions without them meeting |
| <ItemLink id="create_connected:parallel_gearbox" /> | All four faces turn the same way |
| <ItemLink id="create_connected:six_way_gearbox" /> | Shafts on all six sides, top and bottom at half speed |
| <ItemLink id="create_connected:brass_gearbox" /> | Each face configured independently with a wrench |
| <ItemLink id="create_connected:encased_chain_cogwheel" /> | A chain drive that also takes a cogwheel |
| <ItemLink id="create_connected:crank_wheel" /> | A hand crank with a cogwheel for tight gear ratios |
| <ItemLink id="create_connected:kinetic_bridge" /> | Passes capacity between two networks without joining them |

Rotation direction is not cosmetic. Two networks only merge when they meet turning the same way. If a join reverses, the connecting part breaks, so check direction with the wrench before you power a new branch.

A windmill needs at least eight sails to assemble. Each additional eight sails above that adds one revolution per minute, so a modest sail disc is the normal build rather than a huge one.

***

<Recipe id="create:crafting/kinetics/wrench" />
## Controls that keep a line safe

<ItemGrid><ItemIcon id="create:clutch" /><ItemIcon id="create:gearshift" /><ItemIcon id="create_connected:shear_pin" /><ItemIcon id="create_connected:overstress_clutch" /><ItemIcon id="create_connected:brake" /><ItemIcon id="create_connected:centrifugal_clutch" /><ItemIcon id="create_connected:freewheel_clutch" /><ItemIcon id="create_connected:inverted_clutch" /><ItemIcon id="create_connected:inverted_gearshift" /></ItemGrid>

| Part | Use |
| --- | --- |
| <ItemLink id="create:clutch" /> | Redstone cuts the branch without stopping the source |
| <ItemLink id="create:gearshift" /> | Redstone reverses the branch |
| <ItemLink id="create_connected:shear_pin" /> | Single use connector that breaks instead of stalling the whole network |
| <ItemLink id="create_connected:overstress_clutch" /> | Uncoupled after a delay when the network is overstressed, reset with a wrench |
| <ItemLink id="create_connected:brake" /> | Stops the network by overstressing it on purpose |

A clutch belongs on any branch you want to switch off while the source keeps running. A shear pin belongs on a branch you would rather lose than stall.

***

## First drive line

Two <ItemLink id="create:andesite_alloy" /> make eight <ItemLink id="create:shaft" />. That ratio is why short shaft runs are cheap and long ones are not.

<Recipe id="create:crafting/kinetics/shaft" />

<Recipe id="create:crafting/kinetics/water_wheel" />

1. Place the <ItemLink id="create:water_wheel" /> against flowing water so its paddles are pushed.
2. Run a shaft from the wheel to the machine you want to drive.
3. Fit a <ItemLink id="create:stressometer" /> on the line and read capacity against impact.
4. Watch the machine turn for a full cycle before adding a second one.

The expected result is a machine that runs without stopping and a stressometer that does not sit above capacity. The next useful step is a reserve so a short interruption does not stop production. [Stored rotation](power.stored-rotation.md) covers batteries and springs.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Connected](images/create-connected-icon.png) [Create: Connected](machines.rotation.md) | Adds Create transmission components and flexible storage arrangements. | <EmiSearch query="@create_connected" /> |
