---
navigation:
  title: "Machine cooking"
  position: 0
  parent: reference.food.md
  icon: minecraft:smoker
---

# Machine cooking

## Slicing

<EmiSearch query="@farmersdelight" /> <EmiSearch query="@sliceanddice" />

<ItemGrid>
  <ItemIcon id="sliceanddice:slicer" />
  <ItemIcon id="farmersdelight:cutting_board" />
  <ItemIcon id="farmersdelight:flint_knife" />
</ItemGrid>

The <ItemLink id="sliceanddice:slicer" /> automates cutting rather than turning every ingredient directly into a finished meal. Choose the required ingredient and <ItemLink id="farmersdelight:flint_knife" />, then use native Ponder for assembly. <ItemLink id="farmersdelight:cutting_board" /> recipes distinguish whole ingredients from portions.

### Slicer craft

<Recipe id="sliceanddice:slicer" />

Connect ingredient delivery after crafting the machine and supplying its cutting tool.

***

## Drinks & farm fluids

<EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="farmersdelight:hot_cocoa" />
  <ItemIcon id="farmersdelight:apple_cider" />
  <ItemIcon id="sliceanddice:sprinkler" />
  <ItemIcon id="sliceanddice:fertilizer_bucket" />
</ItemGrid>

Slice & Dice supplies Create filling and emptying recipes for <ItemLink id="farmersdelight:hot_cocoa" /> and <ItemLink id="farmersdelight:apple_cider" />. Fluid handling is a different processing stage from making the drink ingredients. The <ItemLink id="sliceanddice:sprinkler" /> and <ItemLink id="sliceanddice:fertilizer_bucket" /> belong to crop production, not serving containers for meals.

***

## Kitchen integration

Create: Central Kitchen supplies cooking integration rather than another food menu. Inspect the target dish’s actual machine recipe before connecting ingredient delivery and output storage. A shared ingredient does not mean every pot recipe has a machine equivalent.

- [Cooking tools](food.utensils.md)
- [Crop production](food.growing.md)
- [Machines & storage](reference.machines-storage.md)

***

## Related mods

| Mod or content | Purpose | Status | Item search |
| --- | --- | --- | --- |
| ![Create Slice & Dice](images/slice-and-dice-icon.png) [Create Slice & Dice](food.machine-cooking.md) | Adds Create machinery for automated Farmer's Delight food preparation. | Baseline, installed | <EmiSearch query="@sliceanddice" /> |
| ![Create: Central Kitchen](images/create-central-kitchen-icon.png) [Create: Central Kitchen](food.machine-cooking.md) | Connects other cooking mods to Create machines for automated food processing. | Baseline, installed | No separate item search |
