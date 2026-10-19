---
navigation:
  title: "Fire Wizard"
  position: 1
  parent: combat.magic.md
  icon: wizards:wand_fire
item_ids:
  - wizards:fire_robe_chest
  - wizards:fire_robe_feet
  - wizards:fire_robe_head
  - wizards:fire_robe_legs
  - wizards:netherite_fire_robe_chest
  - wizards:netherite_fire_robe_feet
  - wizards:netherite_fire_robe_head
  - wizards:netherite_fire_robe_legs
  - wizards:staff_fire
  - wizards:staff_netherite_fire
  - wizards:wand_fire
  - wizards:wand_netherite_fire
  - wizards:wand_novice
---

# Fire Wizard

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Wizards+RPG+Fire+Wizard+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Wizards+RPG+%E7%81%AB%E7%84%B0%E6%B3%95%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## Role & first weapon

Fire Wizards use fire wands and staves for close area attacks, projectiles and falling attacks.

![Fire spell effects](images/visual-fire-magic.png)

### Example starter outfit

The Novice Wand with the four general Wizard Robe pieces is an example starter outfit, not the official default. The model shows appearance and the held wand, not an equipped spell book.

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"wizards:wizard_robe_feet",count:1},{id:"wizards:wizard_robe_legs",count:1},{id:"wizards:wizard_robe_chest",count:1},{id:"wizards:wizard_robe_head",count:1}],HandItems:[{id:"wizards:wand_novice",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="wizards:wand_novice" /><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid>

### What to look for

Fire spells scale with Fire power. The Novice Wand names Fire power only, so it adds nothing to an Arcane or Frost spell while it is held. Read the school line on a focus before you bind a book around it.

A general Wizard Staff names Arcane, Fire and Frost power together, which suits a player who keeps several books. A fire wand or fire staff is the focused choice for a player who casts Fire most of the time. The held focus also carries its own weapon spell, so you can deal damage before any book exists.

The general Wizard Robe needs wool and lapis lazuli and no Nether trip. Each Fire Robe piece needs blaze powder, so that set follows a Nether visit. A Netherite Fire Robe piece is a smithing upgrade of the matching Fire Robe piece, not a separate craft.

Runes are ammunition for weapon spells and for learned spells. Carry the rune named by the spell you intend to cast, loose in the inventory or inside an equipped pouch, and read the cost in its tooltip.

A successful first use looks like this. Hold the Novice Wand, aim at one hostile, cast the wand spell and watch the rune count fall by the stated cost while the target takes fire damage. If nothing happens, check the rune type and the pouch contents before you replace the wand.

### Readiness

These checkpoints are optional suggestions. Each row names a condition you can meet, not a chapter you have to finish.

| Stage | Ready when | Next decision |
| --- | --- | --- |
| Early game | You can craft the Novice Wand from coal and a stick, and you hold the rune its spell names. | Cast once at a single target. Add the general Wizard Robe when wool and lapis lazuli are available. |
| Early midgame | You have a Spell Binding Table with bookshelves and can pay the displayed learning cost. | Bind the Fire book and equip it while a compatible focus is held. |
| Midgame | Blaze powder is available, from the Nether or from trading. | Compare the Fire Robe with the Fire Staff. Judge each piece by its school bonus rather than by its name. |
| Late game | You hold a netherite upgrade smithing template and netherite ingots. | Upgrade one Fire Robe piece at a time. This is an equipment step, not a measure of boss readiness. |

### Starter equipment

<ItemGrid><ItemIcon id="wizards:wand_novice" /></ItemGrid>

<ItemLink id="wizards:wand_novice" />

<Recipe id="wizards:wand_novice" />

### Book abilities

| Ability | Form |
| --- | --- |
| Fire Breath | Area |
| Flame Slash | Projectile |
| Meteor | Falling attack |
| Firestorm | Area |
| Wall of Flames | Persistent area |
| Fire Hydra | Self effect |

***

## Class book
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

The Fire book uses <ItemLink id="spell_engine:spell_book" /> with class-specific ability pools. Select the matching book at the Spell Binding Table.

- [Spell binding & casting](combat.abilities.md) Book creation, costs, equipment slots and casting controls.
- [Runes & weapon spells](combat.magic.md) Casting resources and equipment-provided spells.

***

## Class skills
<ItemGrid><ItemIcon id="wizards:wand_fire" /><ItemIcon id="wizards:staff_fire" /></ItemGrid>

Open <KeyBind id="key.puffish_skills.open" /> to find these class and weapon paths.

| Path | Associated equipment |
| --- | --- |
| Path of Fire | <ItemLink id="wizards:wand_fire" /> |

### Weapon paths

| Path | Associated equipment |
| --- | --- |
| Fire Staff Specialisation | <ItemLink id="wizards:staff_fire" /> |

- [Skill development](combat.skills.md) Point budgets, connected nodes, incompatible roots and resetting. Changing equipment does not refund points.

***

## Weapons & armor

<EmiSearch query="@wizards" />

Fire wands and staves supply this school's spell power. The general Wizard Staff supports arcane, fire and frost. Compare the school bonuses before choosing a focus.

### Weapons

| Family | Items | School bonuses or Role |
| --- | --- | --- |
| Fire wands | <ItemGrid><ItemIcon id="wizards:wand_novice" /><ItemIcon id="wizards:wand_fire" /><ItemIcon id="wizards:wand_netherite_fire" /></ItemGrid> | Fire power |
| General staff | <ItemGrid><ItemIcon id="wizards:staff_wizard" /></ItemGrid> | Arcane, Fire and Frost power |
| Fire staves | <ItemGrid><ItemIcon id="wizards:staff_fire" /><ItemIcon id="wizards:staff_netherite_fire" /></ItemGrid> | Fire power |

### Armor sets

| Set reference, chest piece | Pieces, head to feet |
| --- | --- |
| <ItemLink id="wizards:wizard_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:fire_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:fire_robe_head" /><ItemIcon id="wizards:fire_robe_chest" /><ItemIcon id="wizards:fire_robe_legs" /><ItemIcon id="wizards:fire_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:netherite_fire_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:netherite_fire_robe_head" /><ItemIcon id="wizards:netherite_fire_robe_chest" /><ItemIcon id="wizards:netherite_fire_robe_legs" /><ItemIcon id="wizards:netherite_fire_robe_feet" /></ItemGrid> |

***

## Shared equipment

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [Weapons & armor](equipment.weapons-armor.md)
- [Accessories](equipment.accessories.md)
- [Combat controls](combat.handling.md)
