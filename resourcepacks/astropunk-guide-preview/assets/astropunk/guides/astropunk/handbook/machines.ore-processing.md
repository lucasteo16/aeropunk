---
navigation:
  title: "Ore processing"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# Ore processing

## Processing machines

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

***

## Millstone

<Recipe id="create:crafting/kinetics/millstone" />

***

## Wheat milling

<ItemGrid>
  <ItemIcon id="minecraft:wheat" />
  <ItemIcon id="create:millstone" />
  <ItemIcon id="create:wheat_flour" />
  <ItemIcon id="minecraft:wheat_seeds" />
</ItemGrid>

| Shown items |
| --- |
| <ItemLink id="minecraft:wheat" /> |
| <ItemLink id="create:millstone" /> |
| <ItemLink id="create:wheat_flour" /> |
| <ItemLink id="minecraft:wheat_seeds" /> |

| Input | Output |
| --- | --- |
| One wheat | One wheat flour |
| Bonus, 25 percent chance | Two more wheat flour |
| Bonus, 25 percent chance | One wheat seed |

***

## Iron crushing

<ItemGrid>
  <ItemIcon id="minecraft:raw_iron" />
  <ItemIcon id="create:crushing_wheel" />
  <ItemIcon id="create:crushed_raw_iron" />
  <ItemIcon id="create:experience_nugget" />
</ItemGrid>

| Shown items |
| --- |
| <ItemLink id="minecraft:raw_iron" /> |
| <ItemLink id="create:crushing_wheel" /> |
| <ItemLink id="create:crushed_raw_iron" /> |
| <ItemLink id="create:experience_nugget" /> |

| Input | Output |
| --- | --- |
| One raw iron | One crushed raw iron |
| Bonus, 75 percent chance | One experience nugget |

***

## Iron washing

<ItemGrid>
  <ItemIcon id="create:crushed_raw_iron" />
  <ItemIcon id="create:encased_fan" />
  <ItemIcon id="minecraft:water_bucket" />
  <ItemIcon id="minecraft:iron_nugget" />
  <ItemIcon id="minecraft:redstone" />
</ItemGrid>

| Shown items |
| --- |
| <ItemLink id="create:crushed_raw_iron" /> |
| <ItemLink id="create:encased_fan" /> |
| <ItemLink id="minecraft:water_bucket" /> |
| <ItemLink id="minecraft:iron_nugget" /> |
| <ItemLink id="minecraft:redstone" /> |

| Input | Output |
| --- | --- |
| One crushed raw iron | Nine iron nuggets |
| Bonus, 75 percent chance | One redstone |

Water is the fan's processing medium, not a consumed bucket. Material routing covers moving ingredients and collecting outputs.

- [Material routing](machines.logistics.md)
