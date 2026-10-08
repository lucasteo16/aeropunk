---
navigation:
  title: "Ore processing"
  parent: category-automation.md
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# Ore processing

<ItemGrid>
  <ItemIcon id="create:millstone" />
  <ItemIcon id="create:crushing_wheel" />
  <ItemIcon id="create:encased_fan" />
</ItemGrid>

| Machine | Processing |
| --- | --- |
| <ItemLink id="create:millstone" /> | Milling |
| <ItemLink id="create:crushing_wheel" /> | Crushing |
| <ItemLink id="create:encased_fan" /> | Washing with water |

Use Ponder for the machine arrangement and power supply.

## Millstone

<Recipe id="create:crafting/kinetics/millstone" />

## Wheat milling

<ItemGrid>
  <ItemIcon id="minecraft:wheat" />
  <ItemIcon id="create:millstone" />
  <ItemIcon id="create:wheat_flour" />
  <ItemIcon id="minecraft:wheat_seeds" />
</ItemGrid>

| Input | Output |
| --- | --- |
| One wheat | One wheat flour |
| Bonus, 25 percent chance | Two more wheat flour |
| Bonus, 25 percent chance | One wheat seed |

## Iron crushing

<ItemGrid>
  <ItemIcon id="minecraft:raw_iron" />
  <ItemIcon id="create:crushing_wheel" />
  <ItemIcon id="create:crushed_raw_iron" />
  <ItemIcon id="create:experience_nugget" />
</ItemGrid>

| Input | Output |
| --- | --- |
| One raw iron | One crushed raw iron |
| Bonus, 75 percent chance | One experience nugget |

## Iron washing

<ItemGrid>
  <ItemIcon id="create:crushed_raw_iron" />
  <ItemIcon id="create:encased_fan" />
  <ItemIcon id="minecraft:water_bucket" />
  <ItemIcon id="minecraft:iron_nugget" />
  <ItemIcon id="minecraft:redstone" />
</ItemGrid>

| Input | Output |
| --- | --- |
| One crushed raw iron | Nine iron nuggets |
| Bonus, 75 percent chance | One redstone |

Water is the fan's processing medium, not a consumed bucket. [Material routing](machines.logistics.md) covers moving ingredients and collecting outputs.

## Related mods

| Mod or content | Publisher description |
| --- | --- |
| Create | Aesthetic Technology that empowers the Player |
