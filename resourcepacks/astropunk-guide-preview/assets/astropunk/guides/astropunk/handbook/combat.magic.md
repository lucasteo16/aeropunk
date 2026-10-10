---
navigation:
  title: "Magic & support classes"
  position: 0
  parent: reference.skills.md
  icon: minecraft:blaze_rod
item_ids:
  - spell_engine:spell_binding
  - spell_engine:spell_book
  - spell_engine:spell_scroll
---

# Magic & support classes

## Magic & support classes

Choose a class for its role, starter recipe, books, full ability list, skills and equipment.

- [Arcane Wizard](class.arcane.md)
- [Fire Wizard](class.fire.md)
- [Frost Wizard](class.frost.md)
- [Aqua Wizard](class.aqua.md)
- [Terra Wizard](class.terra.md)
- [Wind Wizard](class.wind.md)
- [Paladin](class.paladin.md)
- [Priest](class.priest.md)
- [Bard](class.bard.md)
- [Witcher](class.witcher.md)

***

## Spell binding

<EmiSearch query="@spell_engine" />

<ItemGrid>
  <ItemIcon id="spell_engine:spell_binding" />
  <ItemIcon id="minecraft:book" />
  <ItemIcon id="minecraft:lapis_lazuli" />
  <ItemIcon id="minecraft:bookshelf" />
  <ItemIcon id="spell_engine:spell_book" />
  <ItemIcon id="spell_engine:spell_scroll" />
</ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

<Recipe id="spell_engine:spell_binding_table" />

1. Put a normal book in the table and select a class spell book. Book creation spends experience levels.
2. Put that spell book in the table and choose abilities from its pool. Meet the displayed level requirement, level cost, lapis cost and bookshelf power requirement. Tier conflicts or a slot limit can block a choice.
3. Equip the configured book in its supported spell-book slot and hold a compatible weapon or focus. The held item filters the spells you can use.

Books carry learned abilities. A skill-tree point improves a build but is not a substitute for spell binding. Scroll application is a separate table mode with its own requirements. The class books are configured versions of <ItemLink id="spell_engine:spell_book" />, not separately registered item identifiers.

***

## Casting requirements

<EmiSearch query="@runes" />

Read each spell tooltip for school, target, casting time, resource cost and cooldown. Keep any required runes or ammunition available. A spell assigned to a book can still be unavailable with an incompatible weapon.

Set spell-hotbar controls in Key Binds. The current first action is <KeyBind id="keybindings.spell_engine.spell_hotbar_1" />. The casting bar shows when a cast is still in progress.

***

## Weapon spells & songs

<EmiSearch query="@bards_rpg" /> <EmiSearch query="@elemental_wizards_rpg" /> <EmiSearch query="@paladins" /> <EmiSearch query="@wizards" />

<ItemGrid>
  <ItemIcon id="wizards:staff_arcane" />
  <ItemIcon id="elemental_wizards_rpg:staff_aqua" />
  <ItemIcon id="paladins:holy_staff" />
  <ItemIcon id="bards_rpg:wooden_lute" />
  <ItemIcon id="bards_rpg:diamond_lyre" />
</ItemGrid>

Wands, staves and instruments can carry active weapon spells without learning them from a class book. Arcane, fire, frost, water, earth and air focuses have school-specific attacks. Holy focuses support healing spells. Named Bard instruments carry different songs. Inspect the held item tooltip for its full set and casting conditions. These families are separate from the complete class-book lists above.

***

## Runes & pouches

<ItemGrid>
  <ItemIcon id="runes:crafting_altar" />
  <ItemIcon id="runes:small_rune_pouch" />
  <ItemIcon id="runes:medium_rune_pouch" />
  <ItemIcon id="runes:large_rune_pouch" />
  <ItemIcon id="runes:arcane_stone" />
  <ItemIcon id="runes:fire_stone" />
  <ItemIcon id="runes:frost_stone" />
  <ItemIcon id="runes:healing_stone" />
  <ItemIcon id="runes:lightning_stone" />
  <ItemIcon id="runes:soul_stone" />
</ItemGrid>

| Item | Role |
| --- | --- |
| <ItemLink id="runes:crafting_altar" /> | Rune crafting workstation |
| <ItemLink id="runes:small_rune_pouch" /> | Equipped rune storage |
| <ItemLink id="runes:medium_rune_pouch" /> | Equipped rune storage |
| <ItemLink id="runes:large_rune_pouch" /> | Equipped rune storage |
| <ItemLink id="runes:arcane_stone" /> | Casting resource |
| <ItemLink id="runes:fire_stone" /> | Casting resource |
| <ItemLink id="runes:frost_stone" /> | Casting resource |
| <ItemLink id="runes:healing_stone" /> | Casting resource |
| <ItemLink id="runes:lightning_stone" /> | Casting resource |
| <ItemLink id="runes:soul_stone" /> | Casting resource |

Runes are consumed only where the spell requires them. The equipped pouch supplies stored runes. The Rune Crafting Altar offers a separate rune-crafting interface. Bundle API is present, enabling the pouch recipes in this selection.

<Recipe id="runes:pouch/small_rune_pouch" />


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Bard (RPG Series Plus)](images/catalog-kL7Bjgmw.png) [Bard (RPG Series Plus)](combat.magic.md) | Adds a bard class that supports allies through songs and ballads. | <EmiSearch query="@bards_rpg" /> |
| ![Elemental Wizards (RPG Series Plus)](images/catalog-PeZ4h4i0.png) [Elemental Wizards (RPG Series Plus)](combat.magic.md) | Expands Wizards with earth, water and wind spellcasting subclasses. | <EmiSearch query="@elemental_wizards_rpg" /> |
| ![Paladins & Priests (RPG Series)](images/catalog-FxXkHaLe.png) [Paladins & Priests (RPG Series)](combat.magic.md) | Adds paladin and priest classes focused on protection and healing. | <EmiSearch query="@paladins" /> |
| ![Runes](images/catalog-lP9Yrr1E.png) [Runes](combat.magic.md) | Adds craftable runes consumed as ammunition for spells. | <EmiSearch query="@runes" /> |
| ![Witcher (RPG Series Plus)](images/catalog-4eW1c7Gj.png) [Witcher (RPG Series Plus)](combat.magic.md) | Adds a monster-hunting witcher class and associated combat abilities. | <EmiSearch query="@witcher_rpg" /> |
| ![Wizards (RPG Series)](images/catalog-NkGaQMDA.png) [Wizards (RPG Series)](combat.magic.md) | Adds wizard combat using arcane, fire and frost spells. | <EmiSearch query="@wizards" /> |
