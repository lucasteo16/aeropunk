---
navigation:
  title: "Magic classes"
  position: 0
  parent: reference.skills.md
  icon: minecraft:enchanted_book
item_ids:
  - spell_engine:spell_binding
  - spell_engine:spell_book
  - spell_engine:spell_scroll
---

# Magic classes

## Spell binding

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

Read each spell tooltip for school, target, casting time, resource cost and cooldown. Keep any required runes or ammunition available. A spell assigned to a book can still be unavailable with an incompatible weapon.

Set spell-hotbar controls in Key Binds. The current first action is <KeyBind id="keybindings.spell_engine.spell_hotbar_1" />. The casting bar shows when a cast is still in progress.


***

## Arcane

<ItemGrid>
  <ItemIcon id="wizards:wand_arcane" />
</ItemGrid>

Arcane magic offers projectiles, beams, area attacks and self effects.

| Ability | Form |
| --- | --- |
| Arcane Missiles | Projectile |
| Arcane Explosion | Area |
| Arcane Beam | Beam |
| Arcane Barrage | Self effect |
| Blink | Self effect |
| Evocation | Self effect |

***

## Fire

<ItemGrid>
  <ItemIcon id="wizards:wand_fire" />
</ItemGrid>

Fire magic offers close areas, projectiles and falling attacks.

| Ability | Form |
| --- | --- |
| Fire Breath | Area |
| Flame Slash | Projectile |
| Meteor | Falling attack |
| Firestorm | Area |
| Wall of Flames | Persistent area |
| Fire Hydra | Self effect |

***

## Frost

<ItemGrid>
  <ItemIcon id="wizards:wand_frost" />
</ItemGrid>

Frost magic combines area attacks, protection and projectiles.

| Ability | Form |
| --- | --- |
| Frost Nova | Area |
| Frost Spikes | Persistent area |
| Frost Shield | Self effect |
| Ice Lance | Projectile |
| Blizzard | Falling attack |
| Frost Elemental | Self effect |

***

## Aqua

<ItemGrid>
  <ItemIcon id="elemental_wizards_rpg:wand_aqua" />
</ItemGrid>

Water magic combines damaging spells and support areas.

| Ability | Form |
| --- | --- |
| Bubble Beam | Area |
| Waterballs | Projectile |
| Springwater | Area |
| Hydro Beam | Beam |
| Healing Rain Cloud | Self effect |
| Tidal Wave | Self effect |

***

## Terra

<ItemGrid>
  <ItemIcon id="elemental_wizards_rpg:wand_terra" />
</ItemGrid>

Earth magic combines protection, aimed attacks and ground effects.

| Ability | Form |
| --- | --- |
| Stone Flesh | Area |
| Impale | Aimed target |
| Terra Circle | Aimed target |
| Shattering Stone | Projectile |
| Earthquake | Self effect |
| Earth Golem | Self effect |

***

## Wind

<ItemGrid>
  <ItemIcon id="elemental_wizards_rpg:wand_wind" />
</ItemGrid>

Air magic combines aimed attacks, persistent areas and self effects.

| Ability | Form |
| --- | --- |
| Aeroblast | Aimed target |
| Twister | Self effect |
| Updraft | Aimed target |
| Windfield | Aimed target |
| Tornado | Persistent area |
| Storm Draft | Projectile |

***

## Paladin

<ItemGrid>
  <ItemIcon id="paladins:iron_mace" />
</ItemGrid>

Healing-school and melee techniques combine support with close combat.

| Ability | Form |
| --- | --- |
| Flash Heal | Aimed target |
| Blessed Strikes | Prepared effect |
| Divine Protection | Self effect |
| Judgement | Falling attack |
| Battle Banner | Persistent area |
| Immolation | Area |

***

## Priest

<ItemGrid>
  <ItemIcon id="paladins:holy_wand" />
</ItemGrid>

Healing-school magic offers beams, healing areas and protection.

| Ability | Form |
| --- | --- |
| Holy Light | Beam |
| Circle of Healing | Area |
| Barrier | Self effect |
| Lightwell | Self effect |
| Levitate | Self effect |
| Penance | Projectile |

***

## Bard

<ItemGrid>
  <ItemIcon id="bards_rpg:wooden_lute" />
</ItemGrid>

Instrument-based abilities combine arcane attacks and support effects.

| Ability | Form |
| --- | --- |
| Magical Ballad | Projectile |
| Vicious Mockery | Aimed target |
| Warden's Paean | Aimed target |
| Encore | Area |
| Army's Paeon | Prepared effect |
| Crescendo | Projectile |

***

## Fencing

<ItemGrid>
  <ItemIcon id="witcher_rpg:steel_witcher_sword" />
</ItemGrid>

Witcher melee techniques supply attacks and self effects.

| Ability | Form |
| --- | --- |
| Fast Attack | Melee attack |
| Witcher Senses | Area |
| Strong Attack | Melee attack |
| Battle Trance | Self effect |
| Rend | Melee attack |
| Whirl | Area |

***

## Signs

<ItemGrid>
  <ItemIcon id="witcher_rpg:wolf_school_medallion" />
</ItemGrid>

Witcher signs have their own ability schools and control or protection effects.

| Ability | Form |
| --- | --- |
| Aard | Area |
| Igni | Area |
| Yrden | Persistent area |
| Axii | Aimed target |
| Quen | Self effect |
| Igni Firestream | Area |
| Aard Sweep | Area |
| Yrden Magic Trap | Self effect |
| Axii Puppet | Aimed target |
| Quen Active Shield | Self effect |

***

## Weapon spells & songs

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

## Build links

- [Weapons & armor](equipment.weapons-armor.md) Choose a weapon family and compare every supported variant.
- [Skill development](combat.skills.md) Spend class and weapon points on connected branches.
- [Combat controls](combat.handling.md) Learn attack patterns, spell controls and rolling.
