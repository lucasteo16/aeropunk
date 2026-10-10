---
navigation:
  title: "Placement tools"
  position: 0
  parent: reference.building.md
  icon: mechtrowel:mech_trowel
---

# Placement tools

## Mechanical Trowel

<EmiSearch query="@mechtrowel" />

<ItemGrid>
  <ItemIcon id="mechtrowel:mech_trowel" />
  <ItemIcon id="mechtrowel:wand_template" />
  <ItemIcon id="mechtrowel:wand_capacity_template" />
  <ItemIcon id="mechtrowel:variant_conversion_template" />
  <ItemIcon id="mechtrowel:reach_upgrade_template" />
</ItemGrid>

The <ItemLink id="mechtrowel:mech_trowel" /> is a functional building tool, not another decorative block. Quick mode randomly places blocks from your hotbar. Named palettes let you control a repeated material mix, and gradient mode transitions between palette sections. Placement consumes available building materials.

### Acquisition

<Recipe id="mechtrowel:mech_trowel" />

Craft one trowel with one <ItemLink id="minecraft:iron_ingot" />, one <ItemLink id="minecraft:iron_block" /> and one <ItemLink id="minecraft:stick" /> arranged along the diagonal shown in the recipe.

### Palette controls

<EmiSearch query="@create" />

| Action | Your key |
| --- | --- |
| Palette manager | <KeyBind id="key.mechtrowel.open_palette" /> |
| Building mode | <KeyBind id="key.mechtrowel.toggle_build_mode" /> |
| Radial menu | <KeyBind id="key.mechtrowel.open_radial_menu" /> |
| Replacement mode | <KeyBind id="key.mechtrowel.toggle_replace" /> |

Prepare a hotbar mix for quick placement, or open the palette manager to create and select a named palette. Preview the target before using a bulk operation. Replacement changes existing blocks, so test it on a small disposable section first.

***

## Trowel upgrades

<EmiSearch query="@chipped" />

| Upgrade item | Function |
| --- | --- |
| <ItemLink id="mechtrowel:wand_template" /> | Unlocks wand mode, which extends blocks using the current palette. |
| <ItemLink id="mechtrowel:wand_capacity_template" /> | Raises the wand operation's block limit. |
| <ItemLink id="mechtrowel:variant_conversion_template" /> | Converts available base blocks to supported Chipped or Rechiseled variants. Chipped is installed here. |
| <ItemLink id="mechtrowel:reach_upgrade_template" /> | Extends placement reach. |

Upgrade recipes are controlled by server settings. The shipped default requires the wand upgrade for wand mode. Applied Energistics 2 and Refined Storage integration templates require their corresponding storage mods.

### Wand template

<Recipe id="mechtrowel:wand_template" />

Use the smithing table with an ender pearl in the template slot, your trowel as the base and <ItemLink id="mechtrowel:wand_template" /> as the addition. The recipe returns the upgraded trowel.

### Other upgrades

<Recipe id="mechtrowel:wand_capacity_template" />

<Recipe id="mechtrowel:variant_conversion_template" />

<Recipe id="mechtrowel:reach_upgrade_template" />

These upgrades use the same smithing slot arrangement with their matching upgrade item. Check the recipe browser for whether a server enables each recipe.

***

## Shuffle filters

<EmiSearch query="@createshufflefilter" />

<ItemGrid>
  <ItemIcon id="mechtrowel:mech_trowel" />
  <ItemIcon id="createshufflefilter:shuffle_filter" />
  <ItemIcon id="createshufflefilter:weighted_shuffle_filter" />
</ItemGrid>

| Shown items |
| --- |
| <ItemLink id="mechtrowel:mech_trowel" /> |
| <ItemLink id="createshufflefilter:shuffle_filter" /> |
| <ItemLink id="createshufflefilter:weighted_shuffle_filter" /> |

Shuffle Filter and Weighted Shuffle Filter supply random and weighted palette selection. Their settings choose the palette. Available materials still matter.

***

## Schematics

<EmiSearch query="@create_pattern_schematics" />

<ItemGrid>
  <ItemIcon id="create_pattern_schematics:empty_pattern_schematic" />
  <ItemIcon id="create_pattern_schematics:pattern_schematic_and_quill" />
  <ItemIcon id="create_pattern_schematics:pattern_schematic" />
</ItemGrid>

| Shown items |
| --- |
| <ItemLink id="create_pattern_schematics:empty_pattern_schematic" /> |
| <ItemLink id="create_pattern_schematics:pattern_schematic_and_quill" /> |
| <ItemLink id="create_pattern_schematics:pattern_schematic" /> |

Pattern Schematics supplies empty patterns, captured patterns and the quill capture item. Forgematica supplies a client schematic overlay and material planning. A displayed schematic does not place a finished vehicle or bypass survival ingredients.

***

## Crafting

<Recipe id="create_pattern_schematics:pattern_schematic" />

## Related topics

- [Browse recipe](help.search.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Pattern Schematics](images/catalog-cpqkg67r.png) [Create: Pattern Schematics](building.placement.md) | Repeats schematic patterns when building with Create schematics. | <EmiSearch query="@create_pattern_schematics" /> |
| ![Create: Shuffle Filter](images/catalog-gv5rravc.png) [Create: Shuffle Filter](building.placement.md) | Lets Create deployers place randomized blocks from a selected palette. | <EmiSearch query="@createshufflefilter" /> |
| ![Forgematica](images/catalog-dckraebc.png) [Forgematica](building.placement.md) | Displays building schematics to guide block placement and construction. | No separate item search |
| ![Mech Trowel](images/catalog-nqfnrals.png) [Mech Trowel](building.placement.md) | Places randomized blocks from custom palettes and supports building-wand placement. | <EmiSearch query="@mechtrowel" /> |
