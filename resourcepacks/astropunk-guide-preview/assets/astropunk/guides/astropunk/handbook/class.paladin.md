---
navigation:
  title: "Paladin"
  position: 7
  parent: combat.magic.md
  icon: paladins:iron_mace
item_ids:
  - paladins:crusader_armor_chest
  - paladins:crusader_armor_feet
  - paladins:crusader_armor_head
  - paladins:crusader_armor_legs
  - paladins:diamond_claymore
  - paladins:diamond_great_hammer
  - paladins:diamond_kite_shield
  - paladins:diamond_mace
  - paladins:golden_claymore
  - paladins:golden_great_hammer
  - paladins:golden_kite_shield
  - paladins:golden_mace
  - paladins:iron_claymore
  - paladins:iron_great_hammer
  - paladins:iron_kite_shield
  - paladins:iron_mace
  - paladins:netherite_claymore
  - paladins:netherite_crusader_armor_chest
  - paladins:netherite_crusader_armor_feet
  - paladins:netherite_crusader_armor_head
  - paladins:netherite_crusader_armor_legs
  - paladins:netherite_great_hammer
  - paladins:netherite_kite_shield
  - paladins:netherite_mace
  - paladins:paladin_armor_chest
  - paladins:paladin_armor_feet
  - paladins:paladin_armor_head
  - paladins:paladin_armor_legs
  - paladins:stone_claymore
  - paladins:stone_great_hammer
  - paladins:wooden_great_hammer
---

# Paladin

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Paladins+and+Priests+Paladin+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Paladins+and+Priests+%E5%9C%A3%E9%AA%91%E5%A3%AB+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## Role & first weapon

Paladins combine close combat and healing-school support, using maces, hammers, claymores and shields.

![Holy protective effects](images/visual-holy-protection.png)

### What to look for

A Paladin works without a spell book at first. The Iron Mace is a normal melee weapon made from an iron ingot and a stick, and the official class description starts the journey with any melee weapon. The class spells arrive with the Paladin Libram, which the publisher says works best with heavy weapons such as hammers and claymores.

The Iron Mace carries no healing-power bonus, so a player who wants to heal keeps a Holy Wand or an Acolyte Wand for that job. The Acolyte Wand costs a stick and string, and the Holy Wand costs a gold ingot and an iron ingot, which makes the Acolyte Wand the cheapest way to try a healing cast. Check the healing line on the item tooltip before you commit.

Paladin Armor uses copper and iron, so the set is reachable early. The Crusader Armor is the later set and the Netherite Crusader Armor is its smithing upgrade. A shield in the off hand supports a defensive style, and the publisher lists that pairing explicitly.

Runes apply to the spells in the Libram, not to the mace swing. Keep the rune named by the spell you intend to cast and treat the melee weapon as a separate source of damage that needs no ammunition.

A successful first use looks like this. Hit a hostile with the Iron Mace and confirm normal melee damage, bind the Libram at a Spell Binding Table, equip it and hold the same mace, then cast Flash Heal on yourself or an ally and watch health return. If the heal fails while the mace still works, the miss is in the rune supply rather than in the weapon.

### Readiness

These checkpoints are optional. Nothing here is a requirement to play the class.

| Stage | Ready when | Next decision |
| --- | --- | --- |
| Early game | You have an iron ingot and a stick for the Iron Mace, and copper and iron for a Paladin Armor piece. | Fight with the mace. Add Paladin Armor pieces as materials arrive. |
| Early midgame | A Spell Binding Table with bookshelves is reachable and its cost is payable. | Bind the Paladin Libram. Keep a Holy or Acolyte Wand if you intend to heal. |
| Midgame | You can compare the mace, great hammer and claymore lines, and a shield is available. | Choose the weapon specialisation that matches your reach and speed, then decide whether the shield is worth the off hand. |
| Late game | You hold a netherite upgrade smithing template and netherite ingots. | Upgrade the Crusader Armor pieces one at a time and keep the healing focus you actually cast with. |

### Example starter outfit

An example starter outfit: the class starter weapon with the first armor set in its catalog. It is one craftable option, not the official or best build.

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"paladins:paladin_armor_feet",count:1},{id:"paladins:paladin_armor_legs",count:1},{id:"paladins:paladin_armor_chest",count:1},{id:"paladins:paladin_armor_head",count:1}],HandItems:[{id:"paladins:iron_mace",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="paladins:iron_mace" /><ItemIcon id="paladins:paladin_armor_feet" /><ItemIcon id="paladins:paladin_armor_legs" /><ItemIcon id="paladins:paladin_armor_chest" /><ItemIcon id="paladins:paladin_armor_head" /></ItemGrid>

### Starter equipment

<ItemGrid><ItemIcon id="paladins:iron_mace" /></ItemGrid>

<ItemLink id="paladins:iron_mace" />

<Recipe id="paladins:iron_mace" />

### Book abilities

| Ability | Form |
| --- | --- |
| Flash Heal | Aimed target |
| Blessed Strikes | Prepared effect |
| Divine Protection | Self effect |
| Judgement | Falling attack |
| Battle Banner | Persistent area |
| Immolation | Area |

***

## Class book
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

The Paladin book uses <ItemLink id="spell_engine:spell_book" /> with class-specific ability pools. Select the matching book at the Spell Binding Table.

- [Spell binding & casting](combat.abilities.md) Book creation, costs, equipment slots and casting controls.
- [Runes & weapon spells](combat.magic.md) Casting resources and equipment-provided spells.

***

## Class skills
<ItemGrid><ItemIcon id="paladins:iron_mace" /><ItemIcon id="paladins:iron_claymore" /><ItemIcon id="paladins:iron_great_hammer" /></ItemGrid>

Open <KeyBind id="key.puffish_skills.open" /> to find these class and weapon paths.

| Path | Associated equipment |
| --- | --- |
| Path of the Paladin | <ItemLink id="paladins:iron_mace" /> |

### Weapon paths

| Path | Associated equipment |
| --- | --- |
| Claymore Specialisation | <ItemLink id="paladins:iron_claymore" /> |
| Hammer Specialisation | <ItemLink id="paladins:iron_great_hammer" /> |
| Mace Specialisation | <ItemLink id="paladins:iron_mace" /> |

- [Skill development](combat.skills.md) Point budgets, connected nodes, incompatible roots and resetting. Changing equipment does not refund points.

***

## Weapons & armor

<EmiSearch query="@paladins" />

Maces, hammers, claymores and shields support close combat. Holy wands and staves support healing spells. Armor combines protection with class attributes.

### Weapons

| Family | Items | School bonuses or Role |
| --- | --- | --- |
| Claymores | <ItemGrid><ItemIcon id="paladins:stone_claymore" /><ItemIcon id="paladins:iron_claymore" /><ItemIcon id="paladins:golden_claymore" /><ItemIcon id="paladins:diamond_claymore" /><ItemIcon id="paladins:netherite_claymore" /></ItemGrid> | Melee, heavy swing |
| Great hammers | <ItemGrid><ItemIcon id="paladins:wooden_great_hammer" /><ItemIcon id="paladins:stone_great_hammer" /><ItemIcon id="paladins:iron_great_hammer" /><ItemIcon id="paladins:golden_great_hammer" /><ItemIcon id="paladins:diamond_great_hammer" /><ItemIcon id="paladins:netherite_great_hammer" /></ItemGrid> | Melee, heavy swing |
| Maces | <ItemGrid><ItemIcon id="paladins:iron_mace" /><ItemIcon id="paladins:golden_mace" /><ItemIcon id="paladins:diamond_mace" /><ItemIcon id="paladins:netherite_mace" /></ItemGrid> | Melee, class starter |
| Kite shields | <ItemGrid><ItemIcon id="paladins:iron_kite_shield" /><ItemIcon id="paladins:diamond_kite_shield" /><ItemIcon id="paladins:netherite_kite_shield" /></ItemGrid> | Armor toughness and Maximum health |
| Golden kite shield | <ItemGrid><ItemIcon id="paladins:golden_kite_shield" /></ItemGrid> | Equipment-specific effect |

### Armor sets

| Set reference, chest piece | Pieces, head to feet |
| --- | --- |
| <ItemLink id="paladins:paladin_armor_chest" /> | <ItemGrid><ItemIcon id="paladins:paladin_armor_head" /><ItemIcon id="paladins:paladin_armor_chest" /><ItemIcon id="paladins:paladin_armor_legs" /><ItemIcon id="paladins:paladin_armor_feet" /></ItemGrid> |
| <ItemLink id="paladins:crusader_armor_chest" /> | <ItemGrid><ItemIcon id="paladins:crusader_armor_head" /><ItemIcon id="paladins:crusader_armor_chest" /><ItemIcon id="paladins:crusader_armor_legs" /><ItemIcon id="paladins:crusader_armor_feet" /></ItemGrid> |
| <ItemLink id="paladins:netherite_crusader_armor_chest" /> | <ItemGrid><ItemIcon id="paladins:netherite_crusader_armor_head" /><ItemIcon id="paladins:netherite_crusader_armor_chest" /><ItemIcon id="paladins:netherite_crusader_armor_legs" /><ItemIcon id="paladins:netherite_crusader_armor_feet" /></ItemGrid> |

***

## Healing focus

The Iron Mace starts Paladin melee but has no healing-power bonus. For a healing-focused build, start with the Acolyte Wand and compare healing power rather than attack damage.

<ItemGrid><ItemIcon id="paladins:acolyte_wand" /></ItemGrid>

<ItemLink id="paladins:acolyte_wand" />

<Recipe id="paladins:acolyte_wand" />

***

## Shared equipment

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [Weapons & armor](equipment.weapons-armor.md)
- [Accessories](equipment.accessories.md)
- [Combat controls](combat.handling.md)
