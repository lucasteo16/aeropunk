---
navigation:
  title: "Material processing"
  position: 6
  parent: reference.machines-storage.md
  icon: create:millstone
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# Material processing

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+mod+millstone+crushing+washing+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E7%A3%A8%E7%9F%B3+%E7%B2%89%E7%A2%8E%E8%BD%AE+%E6%B4%97%E6%B6%A4+%E6%95%99%E7%A8%8B)

## Start with the millstone

<EmiSearch query="@create" />

The <ItemLink id="create:millstone" /> takes items from above and returns products with an empty-hand right click. Use the waterwheel, vertical gearbox and upward shaft arrangement in [Rotational power](machines.rotation.md), then place the millstone directly above that shaft. Drop one wheat into its top. Turning gears and flour appearing in its output confirm the first job.

<Recipe id="create:crafting/kinetics/millstone" />

| Machine | View | Use |
| --- | --- | --- |
| <ItemLink id="create:millstone" /> | <ItemGrid><ItemIcon id="create:millstone" /></ItemGrid> | One item at a time, top input, empty-hand right click output |
| <ItemLink id="create:crushing_wheel" /> | <ItemGrid><ItemIcon id="create:crushing_wheel" /></ItemGrid> | Opposing rotating pair, top input |
| <ItemLink id="create:encased_fan" /> | <ItemGrid><ItemIcon id="create:encased_fan" /></ItemGrid> | Processes items in airflow on belts or depots |
| <ItemLink id="create:mechanical_press" /> | <ItemGrid><ItemIcon id="create:mechanical_press" /></ItemGrid> | Presses items on a depot, belt or basin |
| <ItemLink id="create:mechanical_mixer" /> | <ItemGrid><ItemIcon id="create:mechanical_mixer" /></ItemGrid> | Stirs items in a basin |

One <ItemLink id="minecraft:wheat" /> guarantees one <ItemLink id="create:wheat_flour" />. There is a separate twenty-five-percent chance for two extra flour, and another twenty-five-percent chance for one <ItemLink id="minecraft:wheat_seeds" />. A successful extra-flour roll therefore gives three flour in total.

<EmiSearch query="Wheat Flour" />

Select the matching result to see the complete input and probabilistic outputs.

***

## Crushing, washing and fan media

The Processing Items with Crushing Wheels lesson shows items inserted at the top between two wheels rotating into each other. Crushing <ItemLink id="minecraft:raw_iron" /> yields one <ItemLink id="create:crushed_raw_iron" /> and has a seventy-five-percent chance for <ItemLink id="create:experience_nugget" />. Washing that crushed iron yields nine <ItemLink id="minecraft:iron_nugget" /> and has a seventy-five-percent chance for <ItemLink id="minecraft:redstone" />.

| Fan medium | View | Operation |
| --- | --- | --- |
| Water | <ItemGrid><ItemIcon id="minecraft:water_bucket" /></ItemGrid> | Washes items |
| Lava | <ItemGrid><ItemIcon id="minecraft:lava_bucket" /></ItemGrid> | Blasts items, but destroys food in the airflow |
| Fire or campfire | <ItemGrid><ItemIcon id="minecraft:campfire" /></ItemGrid> | Smokes items |
| Soul fire or soul campfire | <ItemGrid><ItemIcon id="minecraft:soul_campfire" /></ItemGrid> | Haunts items |

Put the chosen medium in the airflow path, with items carried through it on a belt or depot. Air direction and range depend on rotation. Fan speed affects range, not processing speed. For food, use fire smoking rather than the lava blast.

***

## Press and mix in place

Place a <ItemLink id="create:depot" /> beneath the press for a single item, or use a <ItemLink id="create:basin" /> to press a filled two by two or three by three crafting recipe. Some basin recipes require a heated <ItemLink id="create:blaze_burner" />. A basin holds outputs if no valid output faucet is present. With one, output is directed below to the side.

| Station | View | Purpose |
| --- | --- | --- |
| Depot | <ItemGrid><ItemIcon id="create:depot" /></ItemGrid> | Holds an item stack beneath a press |
| Basin | <ItemGrid><ItemIcon id="create:basin" /></ItemGrid> | Holds item and fluid batches. Mixer or press works above it |
| Blaze Burner | <ItemGrid><ItemIcon id="create:blaze_burner" /></ItemGrid> | Supplies heat when a basin recipe requires it |

For mixing, place the mixer over the basin and mesh its upper cogwheel with a rotating drive. Check the mixer tooltip for its required speed. Check the basin output faucet or retained contents to confirm completion. Use the recipe browser for the exact mix or press recipe.

<ItemLink id="create:andesite_alloy" /> is a useful first crafting material before scaling the processing workshop.

- [Rotational power](machines.rotation.md) First drive layout and stress.
- [Item and fluid routing](machines.logistics.md) Belts and item transfer.
- [Cooking tools](food.utensils.md) Food-specific preparation.

***

## Useful processing recipes

<Recipe id="stam1ocreatetweaks:blasting/blue_dye" />

<EmiSearch query="Phantom Membrane" />

<EmiSearch query="Brown Mushroom Block" />

<EmiSearch query="Red Mushroom Block" />

| Process | Input | Output |
| --- | --- | --- |
| Haunting with soul-fire airflow | One <ItemLink id="minecraft:feather" /> | One <ItemLink id="minecraft:phantom_membrane" /> |
| Press and basin compacting | Four <ItemLink id="minecraft:brown_mushroom" /> | One <ItemLink id="minecraft:brown_mushroom_block" /> |
| Press and basin compacting | Four <ItemLink id="minecraft:red_mushroom" /> | One <ItemLink id="minecraft:red_mushroom_block" /> |
| Blasting | One <ItemLink id="minecraft:prismarine_shard" /> | One <ItemLink id="minecraft:blue_dye" /> |

The blue-dye recipe is displayed above. For haunting and compacting, open the shortcut recipes and select the corresponding output's processing recipe. Use soul-fire airflow for the membrane, and the powered press above a basin for the mushroom blocks.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Almost Unified](images/catalog-sdasaqez.png) [Almost Unified](machines.ore-processing.md) | Unifies only shared andesite alloy and zinc sheet recipe materials. | No separate item search |
| ![Create](images/create-icon.png) [Create](machines.ore-processing.md) | Adds rotational machines for processing, transport and automated construction. | <EmiSearch query="@create" /> |
| ![Create: Stam1o Tweaks](images/catalog-46rgf8h2.png) [Create: Stam1o Tweaks](machines.ore-processing.md) | Adjusts Create recipes and lets diving boots counter levitation. | No separate item search |
