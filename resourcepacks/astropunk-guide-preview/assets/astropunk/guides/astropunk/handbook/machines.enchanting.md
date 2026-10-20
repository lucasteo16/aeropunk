---
navigation:
  title: "Enchanting"
  position: 12
  parent: reference.machines-storage.md
  icon: minecraft:enchanting_table
---

# Enchanting

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Enchantment+Industry+experience+fluid+printer+blaze+enchanter+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E9%99%84%E9%AD%94%E5%B7%A5%E4%B8%9A+%E6%B6%B2%E4%BD%93%E7%BB%8F%E9%AA%8C+%E6%89%93%E5%8D%B0%E6%9C%BA+%E7%83%88%E7%84%B0%E9%99%84%E9%AD%94%E5%99%A8+%E6%95%99%E7%A8%8B)

## Turn experience into liquid

<EmiSearch query="@create_enchantment_industry" /> <EmiSearch query="@create" />

Craft two <ItemLink id="create_enchantment_industry:mechanical_grindstone" /> items. Right click a placed Item Drain with one to turn it into a <ItemLink id="create_enchantment_industry:grindstone_drain" />. Place the second Mechanical Grindstone on top, then connect the drain to a tank. Power the grindstone and insert experience items such as experience nuggets. The tank fills with Liquid Experience. Open the Ponder lesson Introduction to Mechanical Grindstone. This is not a general damaged-item experience source.

<Recipe id="create_enchantment_industry:crafting/mechanical_grindstone" />

| Part | View | Use |
| --- | --- | --- |
| Mechanical Grindstone | <ItemGrid><ItemIcon id="create_enchantment_industry:mechanical_grindstone" /></ItemGrid> | Grinds experience items into fluid. Also supports manual sanding |
| Grindstone Drain | <ItemGrid><ItemIcon id="create_enchantment_industry:grindstone_drain" /></ItemGrid> | Collects the grindstone's Liquid Experience output |
| Item Drain | <ItemGrid><ItemIcon id="create:item_drain" /></ItemGrid> | Drains fluid from fluid-bearing items |
| Experience Hatch | <ItemGrid><ItemIcon id="create_enchantment_industry:experience_hatch" /></ItemGrid> | Right click deposits player experience, shift right click withdraws. Panel sets amount |
| Experience Lantern | <ItemGrid><ItemIcon id="create_enchantment_industry:experience_lantern" /></ItemGrid> | Absorbs nearby experience orbs and player experience. Glow indicates stored amount |

***

## Enchant, forge and print

| Machine | View | First operation |
| --- | --- | --- |
| Blaze Enchanter | <ItemGrid><ItemIcon id="create_enchantment_industry:blaze_enchanter" /></ItemGrid> | Supply Liquid Experience and set the enchantment level. Hold the equipment type you want to use as the enchantment filter and right click the panel's filter slot to enter Template Enchanting Mode. Then insert a blank Enchanting Template. Only enchantments supported by that equipment type will be generated. Goggles show required inputs, cost, result or why it cannot start. |
| Blaze Forger | <ItemGrid><ItemIcon id="create_enchantment_industry:blaze_forger" /></ItemGrid> | Supply Liquid Experience and choose the side-panel mode. Merge compatible enchantments or templates, apply a template, or extract an enchantment into a blank template. Remove both outputs before another batch. |
| Printer | <ItemGrid><ItemIcon id="create_enchantment_industry:printer" /></ItemGrid> | Set a target item in its filter slot, then supply the matching fluid and materials for that print recipe. A concrete job is copying an enchanted book with its required Liquid Experience. |
| Enchanting Template | <ItemGrid><ItemIcon id="create_enchantment_industry:enchanting_template" /></ItemGrid> | Carries enchantments between supported operations |

The printer's filter selects what to print. The exact fluid and material are recipe-specific. The recipe browser gives that job's inputs. Forger mode changes through its side panel. Open these Ponder lessons: Introduction to Blaze Enchanter, Introduction to Blaze Forger and Introduction to Printer.

***

## Repair and manual tools

A spout supplied with Liquid Experience repairs passing gear that has Mending. Put the spout over a belt, fill it with the fluid, then send the item through. Reduced damage is the visible result.

| Tool | View | Use |
| --- | --- | --- |
| Spout | <ItemGrid><ItemIcon id="create:spout" /></ItemGrid> | Applies Liquid Experience to Mending gear on a belt |
| Belt | <ItemGrid><ItemIcon id="create:belt_connector" /></ItemGrid> | Carries gear through the spout |
| Anvil | <ItemGrid><ItemIcon id="minecraft:anvil" /></ItemGrid> | Manual repair and combination |
| Name Tag | <ItemGrid><ItemIcon id="minecraft:name_tag" /></ItemGrid> | Manual naming. Easy Anvils changes its interface |
| Enchanted Book | <ItemGrid><ItemIcon id="minecraft:enchanted_book" /></ItemGrid> | Manual enchantment source and printer job input |

- [Rotational power](machines.rotation.md) Drive the grindstone and belt.
- [Item and fluid routing](machines.logistics.md) Feed and collect machine inputs.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Enchantment Industry](images/create-enchantment-industry-icon.png) [Create: Enchantment Industry](machines.enchanting.md) | Automates experience handling and enchanting with Create machinery. | <EmiSearch query="@create_enchantment_industry" /> |
| ![Easy Anvils](images/catalog-ozbr5jt5.png) [Easy Anvils](machines.enchanting.md) | Improves anvil item storage and costs while removing escalating repair penalties. | No separate item search |
