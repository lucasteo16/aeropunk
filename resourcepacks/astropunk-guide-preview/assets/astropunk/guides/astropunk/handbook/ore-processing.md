---
navigation:
  title: Process ores
  icon: create:crushing_wheel
  parent: index.md
item_ids:
  - create:crushing_wheel
  - create:crushed_raw_iron
---

# Process ores

Turn raw materials into useful outputs with Create machines. Choose a process by its recipe, not by assuming a larger machine always gives more metal.

<Row>
  <ItemImage id="minecraft:raw_iron" />
  <ItemImage id="create:crushing_wheel" />
  <ItemImage id="create:crushed_raw_iron" />
  <ItemImage id="create:encased_fan" />
</Row>

## Try raw iron

Crushing raw iron produces crushed raw iron, with a chance of an experience nugget. Washing the crushed material produces iron nuggets, with a chance of redstone.

Search `@create` in the item browser, then look for Crushing Wheel and Encased Fan. Check their recipes and existing Ponder demonstrations before building.

## Inspect recipes

The following display tests an ordinary crafting recipe. Item tooltips and links use the real game items.

<RecipeFor id="minecraft:iron_ingot" fallbackText="This recipe display is unavailable." />

Create processing recipes use custom types. The following displays are capability checks, not a promise that the default renderer supports them. If either is unavailable, inspect the same ingredients in the item browser.

<Recipe id="create:crushing/raw_iron" fallbackText="Crushing recipe needs a custom renderer. Inspect raw iron in the item browser." />

<Recipe id="create:splashing/crushed_raw_iron" fallbackText="Washing recipe needs a custom renderer. Inspect crushed raw iron in the item browser." />

## Inspect machine shapes

This interactive scene demonstrates real block models and annotations. It is not an assembled or powered processing machine.

<GameScene zoom="3" interactive={true}>
  <Block id="create:crushing_wheel" x="0" />
  <Block id="create:encased_fan" x="2" />
  <BlockAnnotation x="0">Crushing Wheel. Use its Ponder demonstration for the actual arrangement.</BlockAnnotation>
  <BlockAnnotation x="2">Encased Fan. Its processing setup depends on what you want to do.</BlockAnnotation>
</GameScene>

## Continue exploring

Input delivery and output collection belong to Storage and logistics. Related guides are not written yet.

[Back to activities](index.md)

This first preview tests writing, layout, item rendering, recipe support and scenes. Direct item-browser buttons, direct Ponder buttons and the spatial homepage are not implemented yet.
