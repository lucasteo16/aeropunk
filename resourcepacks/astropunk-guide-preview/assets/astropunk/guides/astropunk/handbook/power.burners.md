---
navigation:
  title: "Liquid fuels"
  position: 9
  parent: reference.machines-storage.md
  icon: minecraft:lava_bucket
---

# Liquid fuels

## Heat is its own resource

<EmiSearch query="@create" />

A <ItemLink id="create:blaze_burner" /> supplies heat to the block above it. It is not rotation and it is not electricity, so a machine can have full rotation and still do nothing because its burner is cold.

Start with an <ItemLink id="create:empty_blaze_burner" />. That is the crafted item, not a captured blaze.

<Recipe id="create:crafting/kinetics/empty_blaze_burner" />

<ItemGrid><ItemIcon id="create:empty_blaze_burner" /><ItemIcon id="create:blaze_burner" /><ItemIcon id="minecraft:blaze_rod" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| State | What you see |
| --- | --- |
| Empty burner | A cold cage, it supplies no heat |
| Fed burner | A blaze inside, ordinary heat, flames at the sides |
| Superheated burner | Taller flame, used by recipes that demand it |

To capture a blaze, place the empty burner and let a blaze walk into it. A burner with a blaze inside can be picked up with a wrench and moved without losing it.

***

## Feed it, or pipe it

<ItemGrid><ItemIcon id="create:blaze_burner" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| Route | What it gives |
| --- | --- |
| Burnable items dropped in | Ordinary heat for as long as the fuel lasts |
| A blaze cake | Superheated, for the recipes that name it |
| Liquid fuel through a pipe | Ordinary heat without restocking the burner by hand |
| Lava | Ordinary heat only, never superheat |

Create: Liquid Fuel is what makes the pipe route work. It does not add a new burner, it lets the existing one accept fluid from a tank, so a single tank can feed a row of burners through pipes and a pump.

The pump in this pack moves fluid 16 blocks to either side, and a tank holds 8 buckets per block. A bank of three burners under a basin is a small demand, so one tank is normally enough.

***

## Unified fuels does not mean any fuel

<EmiSearch query="@tfmg" />

Create: Unified Fuels connects supported consumers through shared fuel groups, and it generates compatibility data instead of adding machines. The selected release covers systems such as The Factory Must Grow, the Crafts and Additions burners, Liquid Fuel and the Stuff 'N Additions fueling tanks when those mods are present.

<ItemGrid><ItemIcon id="create:blaze_burner" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="tfmg:regular_engine" /></ItemGrid>

| Question | Where the answer is |
| --- | --- |
| Will this fluid burn here | The consumer's own entry, not the fluid's name |
| Will it superheat | Only fuels the burner lists as superheating |
| Is diesel accepted by a burner | Only if the burner's group includes it |

Refinery intermediates, process chemicals and steam are not automatically burnable. A shared fuel supply is a convenience for consumers that already accept the same group, not a universal adapter.

Test with one bucket before plumbing a line across a base. If the burner rejects it, the fluid is outside its group, and no amount of pipe will change that.

Heat and rotation meet at the same machine. [Rotational power](machines.rotation.md) covers the drive side, and [Industrial machinery](power.industry.md) covers the furnaces that use the most heat.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | Lets Create blaze burners consume pumped liquid fuel. | No separate item search |
| <ItemImage id="create:crushing_wheel" /> [Create: Unified Fuels](power.burners.md) | Connects supported Create fuel systems without adding a separate item catalog. | No separate item search |
