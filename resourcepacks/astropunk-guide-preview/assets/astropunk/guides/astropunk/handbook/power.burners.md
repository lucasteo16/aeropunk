---
navigation:
  title: "Liquid fuels"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
---

# Liquid fuels

## Burners & fluid supply

- Browse items: <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:blaze_burner" />
  <ItemIcon id="create:fluid_tank" />
  <ItemIcon id="create:fluid_pipe" />
  <ItemIcon id="create:mechanical_pump" />
  <ItemIcon id="minecraft:lava_bucket" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create:blaze_burner" /> | Create Blaze Burner supplies heat. Create: Liquid Fuel extends this existing burner rather than adding a separate machine. |
| <ItemLink id="create:fluid_tank" />, <ItemLink id="create:fluid_pipe" />, <ItemLink id="create:mechanical_pump" /> | Tank, pipe and pump components provide fluid supply. |
| <ItemLink id="minecraft:lava_bucket" /> | The released liquid-fuel definition accepts lava for ordinary heat, not superheating. The bucket icon represents the fluid. |

***

## Getting started

### Empty burner

<Recipe id="create:crafting/kinetics/empty_blaze_burner" />

Craft <ItemLink id="create:empty_blaze_burner" /> first. It is not a captured <ItemLink id="create:blaze_burner" /> yet. Capture a blaze using the empty burner before supplying fuel.

Start with a captured Blaze Burner and inspect the lava supply route. Do not assume diesel, gasoline or every oil is accepted: the selected Liquid Fuel artifact defines lava plus named compatibility fluids from other mods. Confirm the actual fluid in the item browser before plumbing a fuel line. Burner arrangement and heat states are covered by Create Ponder.

## Related topics

- [Browse recipe](help.search.md)


***

## Related mods

| Mod or content | Purpose | Status | Item search |
| --- | --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | Lets Create blaze burners consume pumped liquid fuel. | Baseline, installed | No separate item search |
