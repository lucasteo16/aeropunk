---
navigation:
  title: "Spells & abilities"
  position: 0
  parent: reference.skills.md
  icon: minecraft:enchanted_book
---

# Spells & abilities

## First abilities

- Browse items: <EmiSearch query="@runes" /> <EmiSearch query="@spell_engine" />

<ItemGrid>
  <ItemIcon id="spell_engine:spell_binding" />
  <ItemIcon id="minecraft:book" />
  <ItemIcon id="minecraft:lapis_lazuli" />
  <ItemIcon id="minecraft:bookshelf" />
  <ItemIcon id="spell_engine:spell_book" />
</ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

1. Craft a starter weapon or focus from a class row. Its built-in ability is separate from a class book.
2. Put a normal book in the Spell Binding Table. Select the matching class book and pay the displayed experience levels. Witcher offers separate Fencing and Signs books.
3. Put the class book back in the table with lapis lazuli. Select an ability and meet its displayed level requirement, level cost, lapis cost and bookshelf power. Add valid nearby bookshelves when an offer lacks power.
4. Equip the book in its spell-book slot and hold a compatible weapon or focus. Check the spell hotbar and use <KeyBind id="keybindings.spell_engine.spell_hotbar_1" /> for its first action. Keep required ammunition or runes available.
5. Open <KeyBind id="key.puffish_skills.open" /> to spend earned points on connected nodes. Read incompatible roots before spending. Class and weapon points are separate from the ordinary experience levels used for binding.

The class books are configured versions of <ItemLink id="spell_engine:spell_book" />, not separate craftable item types. A weapon can grant an ability before you learn any book spells.

***

## Starter recipes

- Browse items: <EmiSearch query="@paladins" /> <EmiSearch query="@wizards" />

The Novice Wand is a low-cost Fire starting point, not an Arcane or Frost substitute. The Acolyte Wand starts healing with sticks and string.

<ItemGrid>
  <ItemIcon id="wizards:wand_novice" />
</ItemGrid>

<ItemLink id="wizards:wand_novice" />

<Recipe id="wizards:wand_novice" />

<ItemGrid>
  <ItemIcon id="paladins:acolyte_wand" />
</ItemGrid>

<ItemLink id="paladins:acolyte_wand" />

<Recipe id="paladins:acolyte_wand" />

***

## Gear & abilities

A spell uses its own school or combat attribute. Match Fire power to Fire spells and healing power to healing. A strong Fire wand does not raise Frost power. Melee and ranged techniques may use different attributes even within one class. Armor protects you, but its school bonuses determine which abilities it strengthens.

Read the ability tooltip before choosing accessories or skill nodes. Rage and Witcher sign intensity are their own build attributes. A relic trigger is not an extra freely castable class spell.

## Related pages

- [Martial abilities](combat.martial.md) Full ranged and melee ability lists.
- [Magic & support](combat.magic.md) Full spell lists and casting requirements.
- [Skill development](combat.skills.md) Class paths, weapon points and resets.
- [Combat controls](combat.handling.md) Attacks, spell actions and rolling.
- [Weapons & armor](equipment.weapons-armor.md) Starter recipes and equipment families.
- [Accessories](equipment.accessories.md) Jewelry, relics and their slots.
