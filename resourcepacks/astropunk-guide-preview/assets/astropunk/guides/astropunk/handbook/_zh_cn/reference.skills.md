---
navigation:
  title: "法术与技能"
  position: 7
  parent: quick-reference.md
  icon: minecraft:enchanted_book
---

# 法术与技能

## 可玩的职业

通过装备、职业书与技能树选择构筑，并没有永久锁定职业的选择界面。技能根节点仍可能互斥，更换装备不会返还已分配点数。

### 武技职业

| 职业 | 用途 | 入门武器或法器 |
| --- | --- | --- |
| 弓箭手 | 蓄力射击与范围箭雨。 | <ItemGrid><ItemIcon id="archers:composite_longbow" /></ItemGrid> <ItemLink id="archers:composite_longbow" /> |
| 神射手 | 快速远程攻击与限制敌人的射击。 | <ItemGrid><ItemIcon id="archers:rapid_crossbow" /></ItemGrid> <ItemLink id="archers:rapid_crossbow" /> |
| 冻原猎手 | 冰霜射击与冻结区域。 | <ItemGrid><ItemIcon id="archers:composite_longbow" /></ItemGrid> <ItemLink id="archers:composite_longbow" /> |
| 战争弓手 | 火焰箭与燃烧地面。 | <ItemGrid><ItemIcon id="archers:composite_longbow" /></ItemGrid> <ItemLink id="archers:composite_longbow" /> |
| 盗贼 | 近战攻击配合陷阱与机动。 | <ItemGrid><ItemIcon id="rogues:iron_dagger" /></ItemGrid> <ItemLink id="rogues:iron_dagger" /> |
| 战士 | 冲锋与防御型近战招式。 | <ItemGrid><ItemIcon id="rogues:iron_double_axe" /></ItemGrid> <ItemLink id="rogues:iron_double_axe" /> |
| 狂战士 | 怒气效果与强力近战打击。 | <ItemGrid><ItemIcon id="berserker_rpg:iron_berserker_axe" /></ItemGrid> <ItemLink id="berserker_rpg:iron_berserker_axe" /> |
| 气功师 | 以拳套施展奥术打击。 | <ItemGrid><ItemIcon id="forcemaster_rpg:iron_knuckle" /></ItemGrid> <ItemLink id="forcemaster_rpg:iron_knuckle" /> |

### 魔法与辅助职业

| 职业 | 用途 | 入门武器或法器 |
| --- | --- | --- |
| 奥术法师 | 奥术弹射物与光束。 | <ItemGrid><ItemIcon id="wizards:wand_arcane" /></ItemGrid> <ItemLink id="wizards:wand_arcane" /> |
| 火焰法师 | 火焰攻击与持续燃烧区域。 | <ItemGrid><ItemIcon id="wizards:wand_novice" /></ItemGrid> <ItemLink id="wizards:wand_novice" /> |
| 冰霜法师 | 冰霜攻击与防护效果。 | <ItemGrid><ItemIcon id="wizards:wand_frost" /></ItemGrid> <ItemLink id="wizards:wand_frost" /> |
| 水系法师 | 水系伤害与治疗区域。 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_kelp" /></ItemGrid> <ItemLink id="elemental_wizards_rpg:wand_kelp" /> |
| 地系法师 | 地系攻击与地面防护。 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_clay" /></ItemGrid> <ItemLink id="elemental_wizards_rpg:wand_clay" /> |
| 风系法师 | 风系攻击与龙卷风区域。 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_feather" /></ItemGrid> <ItemLink id="elemental_wizards_rpg:wand_feather" /> |
| 圣骑士 | 近战打击配合治疗与防护。 | <ItemGrid><ItemIcon id="paladins:iron_mace" /></ItemGrid> <ItemLink id="paladins:iron_mace" /> |
| 牧师 | 治疗光束与群体防护。 | <ItemGrid><ItemIcon id="paladins:acolyte_wand" /></ItemGrid> <ItemLink id="paladins:acolyte_wand" /> |
| 吟游诗人 | 乐器攻击与辅助乐曲。 | <ItemGrid><ItemIcon id="bards_rpg:wooden_lute" /></ItemGrid> <ItemLink id="bards_rpg:wooden_lute" /> |
| 猎魔人剑术 | 剑击与战斗招式。 | <ItemGrid><ItemIcon id="witcher_rpg:iron_witcher_sword" /></ItemGrid> <ItemLink id="witcher_rpg:iron_witcher_sword" /> |
| 猎魔人法印 | 以法印控制敌人与提供防护。 | <ItemGrid><ItemIcon id="witcher_rpg:iron_witcher_sword" /></ItemGrid> <ItemLink id="witcher_rpg:iron_witcher_sword" /> |

三个弓箭手扩展路线可先使用弓，再搭配专属护甲。猎魔人剑术与法印是同一职业的两条书籍路线，并非两个锁定的角色选择。

***

## 第一组招式

<ItemGrid>
  <ItemIcon id="spell_engine:spell_binding" />
  <ItemIcon id="minecraft:book" />
  <ItemIcon id="minecraft:lapis_lazuli" />
  <ItemIcon id="minecraft:bookshelf" />
  <ItemIcon id="spell_engine:spell_book" />
</ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

<Recipe id="spell_engine:spell_binding_table" />

1. 按职业表制作入门武器或法器。武器自带招式与职业法术书不同。
2. 将普通书放入法术绑定台，选择对应职业书，并支付界面显示的经验等级。猎魔人有独立的剑术书与法印书。
3. 将职业书放回绑定台，并放入青金石。选择招式，满足界面显示的等级要求、等级消耗、青金石消耗与书架能量。能量不足时，在附近放置有效书架。
4. 将书装备到法术书槽，并手持兼容武器或法器。查看法术快捷栏，以 <KeyBind id="keybindings.spell_engine.spell_hotbar_1" /> 使用第一个招式。准备所需箭矢或符文。
5. 按 <KeyBind id="key.puffish_skills.open" /> 打开技能树，将所得点数用于相连节点。分配前查看互斥根节点。职业点数与武器点数不同于绑定使用的普通经验等级。

职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，不是独立的合成物品。尚未学习书中法术时，武器也可能已提供自带招式。

***

## 入门配方

新手魔杖是低成本火系起点，不能代替奥术或冰霜法器。侍僧魔杖以木棍与线开始治疗路线。

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

## 装备与招式

每个招式使用自己的学派或战斗属性。火系法术搭配火焰强度，治疗搭配治疗强度。强力火系魔杖不会增加冰霜强度。同一职业的近战与远程招式也可能使用不同属性。护甲提供防护，但其学派加成决定它能强化哪些招式。

选择饰品或技能节点前先阅读招式提示。怒气与猎魔人法印强度是各自独立的构筑属性。遗物触发效果不是可以任意释放的额外职业法术。

## 相关页面

- [武技](combat.martial.md) 完整远程与近战招式表。
- [魔法与辅助](combat.magic.md) 完整法术表与施法要求。
- [技能成长](combat.skills.md) 职业路线、武器点数与重置。
- [战斗操作](combat.handling.md) 攻击、施法与翻滚。
- [武器与护甲](equipment.weapons-armor.md) 入门配方与装备类型。
- [饰品](equipment.accessories.md) 珠宝、遗物与适用槽位。


***

## 相关模组

| 模组或内容 | 状态 | 英文官方简介 |
| --- | --- | --- |
| ![Archers (RPG Series)](images/catalog-QgooUXAJ.png) [Archers (RPG Series)](combat.martial.md) | 已安装基准版 | 🏹 Draw, Release, Conquer - Master the art of Archery! |
| ![Archers Expansion (RPG Series Plus)](images/catalog-1BHIIm4m.png) [Archers Expansion (RPG Series Plus)](combat.martial.md) | 已安装基准版 | Extends the Archers-Mod (RPG Series)  with new content. Spell Engine Add-On |
| ![Bard (RPG Series Plus)](images/catalog-kL7Bjgmw.png) [Bard (RPG Series Plus)](combat.magic.md) | 已安装基准版 | Motivate and strengthen the party with awesome song's and ballads! Spell Engine Add-On |
| ![Berserker (RPG Series Plus)](images/catalog-8hqOZzxM.png) [Berserker (RPG Series Plus)](combat.martial.md) | 已安装基准版 | Enter a wild, relentless battle trance as a Berserker! Spell Engine Add-On |
| ![Better Combat](images/catalog-5sy6g3kz.png) [Better Combat](combat.handling.md) | 已安装基准版 | ⚔️ Easy, spectacular and fun melee combat system from Minecraft Dungeons. |
| ![Combat Roll](images/catalog-wGKYL7st.png) [Combat Roll](combat.handling.md) | 已安装基准版 | 🧶 Adds combat roll ability, with related attributes and enchantments. |
| ![Critical Strike](images/catalog-ilvNBzFn.png) [Critical Strike](combat.handling.md) | 已安装基准版 | 🍀 Chance based critical hits for melee and ranged attacks! |
| ![Elemental Wizards (RPG Series Plus)](images/catalog-PeZ4h4i0.png) [Elemental Wizards (RPG Series Plus)](combat.magic.md) | 已安装基准版 | Master the elements to overcome your foes! Spell Engine Add-On |
| ![Forcemaster (RPG Series Plus)](images/catalog-K3yHebFL.png) [Forcemaster (RPG Series Plus)](combat.martial.md) | 已安装基准版 | Grab a Knuckle, master the force and martial art. Spell Engine Add-On |
| ![More RPG Classes - Skill Tree (RPG Series Plus)](images/catalog-3OYmNUDq.png) [More RPG Classes - Skill Tree (RPG Series Plus)](combat.skills.md) | 已安装基准版 | RPG Series Skill Tree Add-On for the More RPG Classes! |
| ![Paladins & Priests (RPG Series)](images/catalog-FxXkHaLe.png) [Paladins & Priests (RPG Series)](combat.magic.md) | 已安装基准版 | ✨ Protect and heal your friends as a Paladin or a Priest |
| ![Pufferfish's Skills](images/catalog-hqQqvaa4.png) [Pufferfish's Skills](combat.skills.md) | 已安装基准版 | Adds a fully configurable skill system to the game. |
| ![Rogues & Warriors (RPG Series)](images/catalog-3MKqoGuP.png) [Rogues & Warriors (RPG Series)](combat.martial.md) | 已安装基准版 | 🗡️ Silent Blades, Mighty Blows - Dominate with martial skills! |
| ![Runes](images/catalog-lP9Yrr1E.png) [Runes](combat.magic.md) | 已安装基准版 | 🪨 Craft runes to serve as ammo for spells |
| ![Skill Tree (RPG Series)](images/catalog-PjDhruSC.png) [Skill Tree (RPG Series)](combat.skills.md) | 已安装基准版 | ⭐️ Choose your path - Skills that shape your class |
| ![Witcher (RPG Series Plus)](images/catalog-4eW1c7Gj.png) [Witcher (RPG Series Plus)](combat.magic.md) | 已安装基准版 | Slay monsters like a Witcher! Spell Engine Add-On |
| ![Wizards (RPG Series)](images/catalog-NkGaQMDA.png) [Wizards (RPG Series)](combat.magic.md) | 已安装基准版 | 🧙🏻‍♂️ Destroy your enemies with Arcane, Fire and Frost magic |
