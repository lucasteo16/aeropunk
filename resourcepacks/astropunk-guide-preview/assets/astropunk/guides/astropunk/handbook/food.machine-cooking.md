---
navigation:
  title: "Machine cooking"
  position: 9
  parent: reference.food.md
  icon: minecraft:smoker
---

# Machine cooking

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Create%20Slice%20and%20Dice%20slicer%20sprinkler%20Central%20Kitchen%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Create%20Slice%20and%20Dice%20%E5%88%87%E7%89%87%E6%9C%BA%20%E6%B4%92%E6%B0%B4%E5%99%A8%20%E4%B8%AD%E5%A4%AE%E5%8E%A8%E6%88%BF%20%E6%95%99%E7%A8%8B)

## First slice

<EmiSearch query="@create" /> <EmiSearch query="@sliceanddice" />

![Mechanical preparation beside a heated cooking pot](images/visual-automatic-cooking.png)


<Recipe id="sliceanddice:slicer" />

The <ItemLink id="sliceanddice:slicer" /> runs cutting board recipes. Its own Ponder entry is Cutting with the slicer, opened from the Slicer item, and that scene shows the supported arrangement. A knife or an axe loads by right clicking the machine, and this pack allows both as cutting tools.

1. Place the slicer facing its target. Above a belt or depot it cuts one item at a time, and above a basin it works on the items inside the basin.
2. Right click it with the knife or axe you want it to use.
3. Drive it from a shaft. When it turns the wrong way, use a <ItemLink id="create:gearshift" /> to reverse the drive, which switches the output direction by redstone signal.
4. Feed one cabbage and collect the leaves from the output side.

Funnels or chutes move items in and out, which is what turns a single machine into a line. Success is the board result: one cabbage becomes two leaves.

The tools wear out. This pack turns on tool durability use, so keep a spare knife or a repair plan before you build a long line.

Pot recipes are a different case. Slice and Dice converts them into heated mixing recipes, which is a mixer over a heated basin, not the slicer cooking whole meals. The basin cooking setting in this pack is HEATED, so a blaze burner under the basin is the heat condition.

***

## Sprinklers

<ItemGrid><ItemIcon id="sliceanddice:sprinkler" /></ItemGrid>

A sprinkler sprays whatever fluid it is given, and the fluid decides the effect. It is supplied through a pipe, placed below one, and needs no rotation.

| Fluid | What it does |
| --- | --- |
| Water | Wets the ground under it, which keeps farmland hydrated |
| <ItemGrid><ItemIcon id="sliceanddice:fertilizer_bucket" /></ItemGrid> <ItemLink id="sliceanddice:fertilizer_bucket" /> | Applies a bone meal effect to crops |
| Potion | Applies that potion effect to entities in range |
| Lava | Damages entities in range |

This pack sets the sprinkler tank to 300 millibuckets, with a draw of 100 millibuckets per use, and a horizontal range of five blocks.

Liquid Fertilizer is made in a mixer from compost. Build the fertilizer supply before you place a sprinkler over a field, because water hydrates the field but does not apply the fertilizer bone meal effect.

***

## Central Kitchen

<EmiSearch query="@farmersdelight" />

Central Kitchen connects Create logistics to Farmer's Delight stations and ships its own Ponder lessons. Open the Cutting board, Cooking pot and Heat source entries, which are the supported targets for these setups.

| Machine | Identify it | What it does here |
| --- | --- | --- |
| <ItemLink id="create:mechanical_arm" /> | <ItemGrid><ItemIcon id="create:mechanical_arm" /></ItemGrid> | Puts the raw ingredient onto a cutting board, and loads a cooking pot |
| <ItemLink id="create:deployer" /> | <ItemGrid><ItemIcon id="create:deployer" /></ItemGrid> | Holds a knife in Use Mode and cuts the ingredient on the board |
| <ItemLink id="create:mechanical_saw" /> | <ItemGrid><ItemIcon id="create:mechanical_saw" /></ItemGrid> | Cuts converted board recipes without a knife item |
| <ItemLink id="create:andesite_funnel" /> | <ItemGrid><ItemIcon id="create:andesite_funnel" /></ItemGrid> | Takes cooked food out of the pot |
| <ItemLink id="create:blaze_burner" /> | <ItemGrid><ItemIcon id="create:blaze_burner" /></ItemGrid> | Supplies heat under a pot or skillet |

This pack enables both board conversions, to sawing and to deploying, so the saw and Deployer routes are both available.

- [Crop production](food.growing.md) The crops these machines process.
- [Cooking tools](food.utensils.md) The stations being automated.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Slice & Dice](images/slice-and-dice-icon.png) [Create Slice & Dice](food.machine-cooking.md) | Adds Create machinery for automated Farmer's Delight food preparation. | <EmiSearch query="@sliceanddice" /> |
| ![Create: Central Kitchen](images/create-central-kitchen-icon.png) [Create: Central Kitchen](food.machine-cooking.md) | Connects other cooking mods to Create machines for automated food processing. | No separate item search |
