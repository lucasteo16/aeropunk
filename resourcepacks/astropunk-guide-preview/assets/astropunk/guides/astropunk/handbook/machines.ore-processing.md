---
navigation:
  title: "Ore processing"
  position: 4
  parent: reference.machines-storage.md
  icon: create:millstone
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# Ore processing

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Almost+Unified+Ore+processing+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Almost+Unified+%E5%8A%A0%E5%B7%A5%E7%9F%BF%E7%9F%B3%E4%B8%8E%E5%8E%9F%E6%96%99+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## What the three stages give you

<EmiSearch query="@create" />

Raw ore smelts into one ingot. Crushing it first, then washing the crushed ore, returns the same ingot plus experience and a chance of a second material, so the extra machines pay for themselves on the ore you already mine.

Start with a <ItemLink id="create:millstone" />. It needs rotation but no water and no second wheel, which makes it the cheapest way to see the chain work.

<ItemGrid><ItemIcon id="create:millstone" /><ItemIcon id="create:crushing_wheel" /><ItemIcon id="create:encased_fan" /></ItemGrid>

| Machine | Rotation needed | What it does |
| --- | --- | --- |
| <ItemLink id="create:millstone" /> | Any speed, 4 stress units | Milling, one item at a time |
| <ItemLink id="create:crushing_wheel" /> | A pair of wheels, 8 stress units each | Crushing, bulk input |
| <ItemLink id="create:encased_fan" /> | Any speed, 2 stress units | Washing, smoking, blasting, haunting |

<Recipe id="create:crafting/kinetics/millstone" />

A millstone is also the grain machine. Feed it wheat and it returns flour, with seed as a second output.

<ItemGrid><ItemIcon id="minecraft:wheat" /><ItemIcon id="create:millstone" /><ItemIcon id="create:wheat_flour" /><ItemIcon id="minecraft:wheat_seeds" /></ItemGrid>

The result to look for is a machine that keeps turning while items pass through it. If it stalls, the network is overstressed, not the machine broken. [Rotational power](machines.rotation.md) owns the stress budget.

***

## Crush before you smelt

A <ItemLink id="create:crushing_wheel" /> pair sits opposite each other with a gap between them. Items dropped into the gap are crushed, and the wheels also damage anything that falls in.

<ItemGrid><ItemIcon id="minecraft:raw_iron" /><ItemIcon id="create:crushed_raw_iron" /><ItemIcon id="create:experience_nugget" /></ItemGrid>

| Input | Output | Extra |
| --- | --- | --- |
| One raw iron | One crushed iron ore | 75 percent chance of one experience nugget |

Every ore the pack adds has its own crushing entry, and the recipe browser shows the exact row for the ore in your hand. A millstone does the same kind of work for grain, turning wheat into flour.

The experience nugget is the reason to crush even when you do not need the dust. Nuggets thrown into a basin with a mechanical press become experience when you next touch them.

***

## Wash the crushed ore

Washing needs air that has passed through water. Put a water source directly in front of the fan face and the items beyond the water, and the fan pushes washed output toward the far side.

<ItemGrid><ItemIcon id="create:crushed_raw_iron" /><ItemIcon id="create:encased_fan" /><ItemIcon id="minecraft:water_bucket" /><ItemIcon id="minecraft:iron_nugget" /><ItemIcon id="minecraft:redstone" /></ItemGrid>

| Input | Output | Extra |
| --- | --- | --- |
| One crushed iron ore | Nine iron nuggets | 75 percent chance of one redstone |

Nine nuggets make one ingot, so washing does not add iron on its own. It adds redstone and it converts the ore into a form that stacks the same way ingots do. The pack sets fan processing at 150 game ticks, which is about seven and a half seconds at full fan speed.

Water is the medium, not an ingredient. The bucket icon stands for the water block, and the fan never drinks it.

***

## When two ores share a name

<EmiSearch query="@createdeco" />

Almost Unified in this pack unifies only the shared andesite alloy plate and zinc plate recipe tags, and it prefers the Create Deco output for them. Everything else keeps the item its own mod registered.

<ItemGrid><ItemIcon id="create:andesite_alloy" /></ItemGrid>

| Situation | What to do |
| --- | --- |
| A recipe names a plate | Read the accepted ingredient in the recipe browser, not the material name |
| You build an exact item filter | Match the item the recipe actually consumes |
| Loot or a boss drop looks equivalent | Treat it as a separate item |

A matching name does not make two items interchangeable in an exact item filter. Check the recipe before you build the filter, and check again after a pack update.

Next step is moving the crushed ore between these machines without carrying it. [Material routing](machines.logistics.md) covers belts, chutes and arms.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Almost Unified](images/catalog-sdasaqez.png) [Almost Unified](machines.ore-processing.md) | Unifies only shared andesite alloy and zinc sheet recipe materials. | No separate item search |
| ![Create](images/create-icon.png) [Create](machines.ore-processing.md) | Adds rotational machines for processing, transport and automated construction. | <EmiSearch query="@create" /> |
