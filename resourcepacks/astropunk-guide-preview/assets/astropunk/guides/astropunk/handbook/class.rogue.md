---
navigation:
  title: "Rogue"
  position: 2
  parent: combat.martial.md
  icon: rogues:iron_dagger
item_ids:
  - rogues:assassin_armor_chest
  - rogues:assassin_armor_feet
  - rogues:assassin_armor_head
  - rogues:assassin_armor_legs
  - rogues:diamond_dagger
  - rogues:diamond_sickle
  - rogues:flint_dagger
  - rogues:golden_dagger
  - rogues:golden_sickle
  - rogues:iron_dagger
  - rogues:iron_sickle
  - rogues:netherite_assassin_armor_chest
  - rogues:netherite_assassin_armor_feet
  - rogues:netherite_assassin_armor_head
  - rogues:netherite_assassin_armor_legs
  - rogues:netherite_dagger
  - rogues:netherite_sickle
  - rogues:rogue_armor_chest
  - rogues:rogue_armor_feet
  - rogues:rogue_armor_head
  - rogues:rogue_armor_legs
---

# Rogue

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Rogues+and+Warriors+Rogue+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Rogues+and+Warriors+%E7%9B%97%E8%B4%BC+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## Role & first weapon

Rogues use daggers and sickles, combining close attacks with prepared melee effects, traps and mobility.

![Rogue and Warrior equipment](images/visual-martial-equipment.png)

### Starter equipment

<ItemGrid><ItemIcon id="rogues:iron_dagger" /></ItemGrid>

<ItemLink id="rogues:iron_dagger" />

<Recipe id="rogues:iron_dagger" />

### Example starter outfit

An iron dagger with the four Rogue armor pieces is one craftable starting outfit, not the official default or a required build. The model shows appearance and the held weapon only.

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"rogues:rogue_armor_feet",count:1},{id:"rogues:rogue_armor_legs",count:1},{id:"rogues:rogue_armor_chest",count:1},{id:"rogues:rogue_armor_head",count:1}],HandItems:[{id:"rogues:iron_dagger",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="rogues:rogue_armor_head" /><ItemIcon id="rogues:rogue_armor_chest" /><ItemIcon id="rogues:rogue_armor_legs" /><ItemIcon id="rogues:rogue_armor_feet" /></ItemGrid>

### Readiness & first fight

The Rogue book is built around evading attacks and tricking opponents, and its publisher recommends dual wielded quick weapons, which means a dagger or a sickle in each hand. Damage per swing is lower than a heavy weapon, so the class wins by attacking between enemy swings and by setting a prepared effect before the fight starts. Rogue armor supports that rhythm and assassin armor is the next family in the same list. A good first fight is one mob killed in a short exchange after a shock powder or a trap, with your health nearly untouched.

The stages below are optional. They describe what you need on hand and what each step unlocks, not how long you have played.

| Stage | Ready when | Suggested action or next decision |
| --- | --- | --- |
| Early game: first daggers | Two quick weapons, ideally a dagger beside a sickle, and food. | Craft the iron dagger and pair it with any second quick weapon. Confirm both hands hold a weapon before you rely on the off hand. |
| Early midgame: rogue manual | A Spell Binding Table with bookshelves, the Rogue Manual, and its learning cost. | Bind the manual and equip it. Set one prepared effect before you enter a fight rather than casting mid swing. |
| Midgame: armor | Rogue armor pieces, or assassin pieces as the stronger family. | Complete one set. Compare attack speed and damage on the weapon before swapping a set for a single piece. |
| Late game: netherite | Netherite materials, the template, and an assassin armor piece. | Upgrade the assassin set and keep a trap or an escape ability bound for group fights. |

### Book abilities

| Ability | Form |
| --- | --- |
| Slice & Dice | Prepared effect |
| Shock Powder | Area |
| Shadowstep | Aimed target |
| Vanish | Self effect |
| Bear Trap | Persistent area |
| Mutilate | Melee attack |

***

## Class book
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

The Rogue book uses <ItemLink id="spell_engine:spell_book" /> with class-specific ability pools. Select the matching book at the Spell Binding Table.

- [Spell binding & casting](combat.abilities.md) Book creation, costs, equipment slots and casting controls.
- [Runes & weapon spells](combat.magic.md) Casting resources and equipment-provided spells.

***

## Class skills
<ItemGrid><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="rogues:iron_sickle" /></ItemGrid>

Open <KeyBind id="key.puffish_skills.open" /> to find these class and weapon paths.

| Path | Associated equipment |
| --- | --- |
| Path of the Rogue | <ItemLink id="rogues:iron_dagger" /> |

### Weapon paths

| Path | Associated equipment |
| --- | --- |
| Dagger Specialisation | <ItemLink id="rogues:iron_dagger" /> |
| Sickle Specialisation | <ItemLink id="rogues:iron_sickle" /> |

- [Skill development](combat.skills.md) Point budgets, connected nodes, incompatible roots and resetting. Changing equipment does not refund points.

***

## Weapons & armor

<EmiSearch query="@rogues" />

Daggers and sickles are the Rogue weapon families listed here. Compare damage, attack speed and weapon abilities.

- [Warrior](class.warrior.md)

### Weapons

| Family | Items | Role |
| --- | --- | --- |
| <ItemLink id="rogues:flint_dagger" /> | <ItemGrid><ItemIcon id="rogues:flint_dagger" /><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="rogues:golden_dagger" /><ItemIcon id="rogues:diamond_dagger" /><ItemIcon id="rogues:netherite_dagger" /></ItemGrid> | Quick weapon, pairs with a second quick weapon |
| <ItemLink id="rogues:iron_sickle" /> | <ItemGrid><ItemIcon id="rogues:iron_sickle" /><ItemIcon id="rogues:golden_sickle" /><ItemIcon id="rogues:diamond_sickle" /><ItemIcon id="rogues:netherite_sickle" /></ItemGrid> | Quick weapon, pairs with a second quick weapon |

### Armor sets

| Set reference, chest piece | Pieces, head to feet |
| --- | --- |
| <ItemLink id="rogues:rogue_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:rogue_armor_head" /><ItemIcon id="rogues:rogue_armor_chest" /><ItemIcon id="rogues:rogue_armor_legs" /><ItemIcon id="rogues:rogue_armor_feet" /></ItemGrid> |
| <ItemLink id="rogues:assassin_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:assassin_armor_head" /><ItemIcon id="rogues:assassin_armor_chest" /><ItemIcon id="rogues:assassin_armor_legs" /><ItemIcon id="rogues:assassin_armor_feet" /></ItemGrid> |
| <ItemLink id="rogues:netherite_assassin_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:netherite_assassin_armor_head" /><ItemIcon id="rogues:netherite_assassin_armor_chest" /><ItemIcon id="rogues:netherite_assassin_armor_legs" /><ItemIcon id="rogues:netherite_assassin_armor_feet" /></ItemGrid> |

***

## Shared equipment

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [Weapons & armor](equipment.weapons-armor.md)
- [Accessories](equipment.accessories.md)
- [Combat controls](combat.handling.md)
