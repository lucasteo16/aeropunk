---
navigation:
  title: "Arcane Wizard"
  position: 0
  parent: combat.magic.md
  icon: wizards:wand_arcane
item_ids:
  - wizards:arcane_robe_chest
  - wizards:arcane_robe_feet
  - wizards:arcane_robe_head
  - wizards:arcane_robe_legs
  - wizards:netherite_arcane_robe_chest
  - wizards:netherite_arcane_robe_feet
  - wizards:netherite_arcane_robe_head
  - wizards:netherite_arcane_robe_legs
  - wizards:staff_arcane
  - wizards:staff_netherite_arcane
  - wizards:staff_wizard
  - wizards:wand_arcane
  - wizards:wand_netherite_arcane
  - wizards:wizard_robe_chest
  - wizards:wizard_robe_feet
  - wizards:wizard_robe_head
  - wizards:wizard_robe_legs
---

# Arcane Wizard

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Wizards+RPG+Arcane+Wizard+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Wizards+RPG+%E5%A5%A5%E7%A7%98%E6%B3%95%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## Role & first weapon

Arcane Wizards use arcane wands and staves for projectiles, beams, area attacks and self effects.

### Example starter outfit

An Arcane Wand with the four Wizard Robe pieces is one craftable starting outfit, not a required or universally best build. The model shows appearance and the held wand, not an equipped spell book.

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"wizards:wizard_robe_feet",count:1},{id:"wizards:wizard_robe_legs",count:1},{id:"wizards:wizard_robe_chest",count:1},{id:"wizards:wizard_robe_head",count:1}],HandItems:[{id:"wizards:wand_arcane",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid>

Ready for basic casting when you have the wand and the rune supply required by its spell. The wand recipe needs amethyst and gold. The general robes need wool and lapis lazuli. A class book is the next step, not a prerequisite for the wand's own basic spell.

These are optional readiness checkpoints, not a required order or a measure of days played.

| Stage | Next decision |
| --- | --- |
| Early game: first casts | Start with the Arcane Wand. Use the general robes if you can craft them. Check the spell tooltip for its rune cost. |
| Early midgame: book casting | Access a Spell Binding Table with bookshelves, meet the displayed learning costs, equip the Arcane book and hold compatible equipment. |
| Midgame: school investment | Compare Arcane robes and the Arcane Staff once ender pearls are available. Check school bonuses rather than replacing equipment by name alone. |
| Late game: netherite upgrade | Follow the selected smithing recipe once its template and materials are available. This is an equipment upgrade, not proof of boss readiness. |

### Starter equipment

<ItemGrid>
  <ItemIcon id="wizards:wand_arcane" />
</ItemGrid>

<ItemLink id="wizards:wand_arcane" />

<Recipe id="wizards:wand_arcane" />

### Book abilities

| Ability | Form |
| --- | --- |
| Arcane Missiles | Projectile |
| Arcane Explosion | Area |
| Arcane Beam | Beam |
| Arcane Barrage | Self effect |
| Blink | Self effect |
| Evocation | Self effect |

![Arcane casting with a staff](images/visual-arcane-casting.png)

***

## Class book
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

The Arcane book uses <ItemLink id="spell_engine:spell_book" /> with class-specific ability pools. Select the matching book at the Spell Binding Table.

- [Spell binding & casting](combat.abilities.md) Book creation, costs, equipment slots and casting controls.
- [Runes & weapon spells](combat.magic.md) Casting resources and equipment-provided spells.

***

## Class skills
<ItemGrid><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:staff_arcane" /></ItemGrid>

Open <KeyBind id="key.puffish_skills.open" /> to find these class and weapon paths.

| Path | Associated equipment |
| --- | --- |
| Path of Arcane | <ItemLink id="wizards:wand_arcane" /> |

### Weapon paths

| Path | Associated equipment |
| --- | --- |
| Arcane Staff Specialisation | <ItemLink id="wizards:staff_arcane" /> |

- [Skill development](combat.skills.md) Point budgets, connected nodes, incompatible roots and resetting. Changing equipment does not refund points.

***

## Weapons & armor

<EmiSearch query="@wizards" />

Arcane wands and staves supply this school's spell power. The general Wizard Staff supports arcane, fire and frost. Compare the school bonuses before choosing a focus.

### Weapons

| Family | Items | School bonuses |
| --- | --- | --- |
| <ItemLink id="wizards:wand_arcane" /> | <ItemGrid><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:wand_netherite_arcane" /></ItemGrid> | Arcane power |
| <ItemLink id="wizards:staff_wizard" /> | <ItemGrid><ItemIcon id="wizards:staff_wizard" /></ItemGrid> | Arcane, fire and frost power |
| <ItemLink id="wizards:staff_arcane" /> | <ItemGrid><ItemIcon id="wizards:staff_arcane" /><ItemIcon id="wizards:staff_netherite_arcane" /></ItemGrid> | Arcane power |

### Armor sets

| Set reference, chest piece | Pieces, head to feet |
| --- | --- |
| <ItemLink id="wizards:wizard_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:arcane_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:arcane_robe_head" /><ItemIcon id="wizards:arcane_robe_chest" /><ItemIcon id="wizards:arcane_robe_legs" /><ItemIcon id="wizards:arcane_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:netherite_arcane_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:netherite_arcane_robe_head" /><ItemIcon id="wizards:netherite_arcane_robe_chest" /><ItemIcon id="wizards:netherite_arcane_robe_legs" /><ItemIcon id="wizards:netherite_arcane_robe_feet" /></ItemGrid> |

***

## Shared equipment

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [Weapons & armor](equipment.weapons-armor.md)
- [Accessories](equipment.accessories.md)
- [Combat controls](combat.handling.md)
