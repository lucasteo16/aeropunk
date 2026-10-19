---
navigation:
  title: "Enchanting"
  position: 12
  parent: reference.machines-storage.md
  icon: minecraft:enchanting_table
---

# Enchanting

## Turn experience into a liquid

<EmiSearch query="@create" />

Create: Enchantment Industry stores experience as a fluid, which is the piece that makes enchanting automatable. The conversion happens at a <ItemLink id="create_enchantment_industry:mechanical_grindstone" /> placed over an <ItemLink id="create:item_drain" />.

<EmiSearch query="@create_enchantment_industry" />

<ItemGrid><ItemIcon id="create_enchantment_industry:mechanical_grindstone" /><ItemIcon id="create_enchantment_industry:grindstone_drain" /><ItemIcon id="create:item_drain" /><ItemIcon id="create_enchantment_industry:experience_hatch" /><ItemIcon id="create_enchantment_industry:experience_lantern" /></ItemGrid>

| Part | Job |
| --- | --- |
| <ItemLink id="create_enchantment_industry:mechanical_grindstone" /> | Grinds items and also sands them, and releases experience |
| <ItemLink id="create_enchantment_industry:grindstone_drain" /> | The drain variant that collects that release |
| <ItemLink id="create:item_drain" /> | Collects the released experience as fluid |
| <ItemLink id="create_enchantment_industry:experience_hatch" /> | Lets you put your own experience into a tank or take it back |
| <ItemLink id="create_enchantment_industry:experience_lantern" /> | Absorbs experience nearby and works while mounted on a contraption |

<Recipe id="create_enchantment_industry:crafting/mechanical_grindstone" />

The first action is to grind one enchanted or damaged item over the drain and watch the tank fill. If nothing appears, the grindstone is not turning, or the drain has no fluid tank to push into.

***

## Enchant, forge and copy

<ItemGrid><ItemIcon id="create_enchantment_industry:blaze_enchanter" /><ItemIcon id="create_enchantment_industry:blaze_forger" /><ItemIcon id="create_enchantment_industry:printer" /><ItemIcon id="create_enchantment_industry:enchanting_template" /></ItemGrid>

| Machine | Publisher description |
| --- | --- |
| <ItemLink id="create_enchantment_industry:blaze_enchanter" /> | A blaze acting as a smart enchanting table |
| <ItemLink id="create_enchantment_industry:blaze_forger" /> | A blaze acting as a smart anvil for repairing and combining |
| <ItemLink id="create_enchantment_industry:printer" /> | Copies written books, enchanted books, name tags and train schedules |

The printer is the machine that changes how a base operates. One good enchanted book becomes a stack of copies for the price of liquid experience, so a single lucky find can equip a whole workshop.

Read the block's own help entry before automating it. The enchanter and forger both take equipment and liquid experience, and the exact slots are specific enough that a screenshot would age badly.

***

## Repair on the line

An item with Mending can be repaired by a spout filled with liquid experience, which means a belt can repair gear as it passes.

<ItemGrid><ItemIcon id="create:spout" /><ItemIcon id="create:belt_connector" /><ItemIcon id="minecraft:enchanted_book" /></ItemGrid>

| Setup | Result |
| --- | --- |
| Spout over a belt, liquid experience in the tank | Passing Mending items lose damage |
| Experience hatch at a tank | You deposit or withdraw your own levels |
| Deployer kills and crushing wheel kills | Drop experience nuggets in this mod |

The repair route is worth building once you carry gear you would rather not replace. A short belt with a spout and a tank beside your main workshop removes most trips to an anvil. The anvil and the name tag still do manual work, since Easy Anvils changes their interface rather than making them powered machines.

<ItemGrid><ItemIcon id="minecraft:anvil" /><ItemIcon id="minecraft:name_tag" /></ItemGrid>

***

## What this pack leaves out

This pack does not install Apothic Enchanting or Apotheosis, so the integration blocks those mods add are not part of the catalog here.

| Integration block | Needs |
| --- | --- |
| Brass Bookshelf, Infuser | Apothic Enchanting |
| Blaze Composer, Affix Augmentor, Gem Cutter | Apotheosis |

Plan around the grindstone, enchanter, forger, printer and experience storage. Those are the machines that exist.

Next step is power for the grindstone. [Rotational power](machines.rotation.md) covers the drive line.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Enchantment Industry](images/create-enchantment-industry-icon.png) [Create: Enchantment Industry](machines.enchanting.md) | Automates experience handling and enchanting with Create machinery. | <EmiSearch query="@create_enchantment_industry" /> |
| ![Easy Anvils](images/catalog-ozbr5jt5.png) [Easy Anvils](machines.enchanting.md) | Improves anvil item storage and costs while removing escalating repair penalties. | No separate item search |
