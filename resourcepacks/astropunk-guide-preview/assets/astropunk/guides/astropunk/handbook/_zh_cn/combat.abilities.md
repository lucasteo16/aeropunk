---
navigation:
  title: "法术与招式"
  position: 0
  parent: reference.skills.md
  icon: minecraft:enchanted_book
---

# 法术与招式

## 第一组招式

<EmiSearch query="@spell_engine" />

<ItemGrid>
  <ItemIcon id="spell_engine:spell_binding" />
  <ItemIcon id="minecraft:book" />
  <ItemIcon id="minecraft:lapis_lazuli" />
  <ItemIcon id="minecraft:bookshelf" />
  <ItemIcon id="spell_engine:spell_book" />
</ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

1. 按职业表制作入门武器或法器。武器自带招式与职业法术书不同。
2. 将普通书放入法术绑定台，选择对应职业书，并支付界面显示的经验等级。猎魔人有独立的剑术书与法印书。
3. 将职业书放回绑定台，并放入青金石。选择招式，满足界面显示的等级要求、等级消耗、青金石消耗与书架能量。能量不足时，在附近放置有效书架。
4. 将书装备到法术书槽，并手持兼容武器或法器。查看法术快捷栏，以 <KeyBind id="keybindings.spell_engine.spell_hotbar_1" /> 使用第一个招式。准备所需箭矢或符文。
5. 按 <KeyBind id="key.puffish_skills.open" /> 打开技能树，将所得点数用于相连节点。分配前查看互斥根节点。职业点数与武器点数不同于绑定使用的普通经验等级。

职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，不是独立的合成物品。尚未学习书中法术时，武器也可能已提供自带招式。

***

## 入门配方

<EmiSearch query="@paladins" /> <EmiSearch query="@wizards" />

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
