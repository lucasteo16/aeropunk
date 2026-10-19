---
navigation:
  title: "法术与招式"
  position: 7
  parent: reference.skills.md
  icon: minecraft:enchanted_book
item_ids:
  - spell_engine:spell_binding
  - spell_engine:spell_book
  - spell_engine:spell_scroll
---

# 法术与招式

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Spell+Engine+RPG+Series+spell+binding+table+spell+book+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Spell+Engine+RPG+Series+%E6%B3%95%E6%9C%AF%E7%BB%91%E5%AE%9A%E5%8F%B0+%E8%81%8C%E4%B8%9A%E4%B9%A6+%E7%BB%91%E5%AE%9A+%E6%95%99%E7%A8%8B)

## 准备职业书

![法术书与法术绑定台](images/visual-spell-binding.png)

<EmiSearch query="@spell_engine" />

<ItemGrid><ItemIcon id="spell_engine:spell_binding" /></ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

<Recipe id="spell_engine:spell_binding_table" />

武器自带招式与职业书教授的招式是两回事。

1. 将普通 <ItemLink id="minecraft:book" /> 放入绑定台，选择对应职业书并支付显示的经验等级。猎魔人有独立的剑术书与法印书。
2. 将职业书放回绑定台并放入 <ItemLink id="minecraft:lapis_lazuli" />，选择满足等级、青金石消耗与书架能量的招式。能量不足时在附近添加有效的 <ItemLink id="minecraft:bookshelf" />，并留意同阶冲突与书籍槽位上限。
3. 将配置好的书放入法术书槽，并手持兼容武器或法器。手持物品会筛选可用法术。

职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，并非独立的合成物品。<ItemLink id="spell_engine:spell_scroll" /> 只携带一个法术，使用前先看下一节。

***

## 使用法术卷轴

<ItemGrid><ItemIcon id="spell_engine:spell_scroll" /><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

卷轴可让你使用战利品中的单个法术，或把它加入兼容书籍，但它不能通用于所有职业。

- 想单独试用时，把卷轴放入支持的法术书槽暂时代替职业书，再手持兼容武器。独立卷轴槽只有启用后才能使用，并非所有饰品槽都接受卷轴。
- 想保存在书中，把接收法术的职业书放入绑定台的书籍槽，用卷轴代替青金石放入材料槽。选择显示的法术，并确认书籍池接受该法术后再应用。
- 若没有可用选项，先确认该法术属于这本书的法术池，再检查已学招式、同阶冲突与剩余容量。书籍不兼容时，积攒更多普通经验也不能解决。

应用所选法术会消耗卷轴，并扣除界面显示的普通经验等级。这种转移不需要青金石。以绑定台当前显示为准，不要假设卷轴绑定与青金石学习消耗相同。

***

## 释放招式

<ItemGrid><ItemIcon id="spell_engine:spell_book" /><ItemIcon id="minecraft:book" /></ItemGrid>

查看提示中的学派、目标、施法时间、材料消耗与冷却，并备好所需弹药或符文。已学法术仍可能因武器不兼容而无法使用，施法条显示施法是否仍在进行。

第一个招式在按键设置中配置，当前为 <KeyBind id="keybindings.spell_engine.spell_hotbar_1" />，显示未绑定时可在那里修改。

- [魔法与辅助](combat.magic.md) 武器法术、乐曲、符文种类与符文袋制作。
- [战斗操作](combat.handling.md) 攻击、翻滚与按键冲突。

***

## 装备与技能点

<ItemGrid><ItemIcon id="spell_engine:spell_book" /><ItemIcon id="skill_tree_rpgs:orb_of_oblivion" /></ItemGrid>

让装备契合招式使用的属性。火焰强度增强火系法术，不增强冰霜法术，治疗则使用治疗强度。同一职业的近战与远程招式也可能使用不同属性。护甲防护与学派加成作用不同，遗物触发效果也不是可任意释放的职业法术。

绑定消耗普通经验等级。职业点数与武器点数用于各自相连的技能树，不能代替绑定，更换装备也不会返还点数。

- [技能成长](combat.skills.md) 按 <KeyBind id="key.puffish_skills.open" /> 打开界面，查看互斥根节点与重置。
- [武器与护甲](equipment.weapons-armor.md) 职业装备与通用具名套装。
- [饰品](equipment.accessories.md) 珠宝、遗物与适用槽位。

***

## 入门法器

新手魔杖是低成本火系起点，不能代替奥术或冰霜法器。侍僧魔杖以木棍与线开始治疗路线。其他入门装备与完整招式目录见各职业文章。

<ItemGrid><ItemIcon id="wizards:wand_novice" /></ItemGrid>

<ItemLink id="wizards:wand_novice" />

<Recipe id="wizards:wand_novice" />

<ItemGrid><ItemIcon id="paladins:acolyte_wand" /></ItemGrid>

<ItemLink id="paladins:acolyte_wand" />

<Recipe id="paladins:acolyte_wand" />

- [武技职业](combat.martial.md) 远程与近战职业文章。
- [法术与支援职业](combat.magic.md) 魔法与辅助职业文章。

***

## 招式无效时

<ItemGrid><ItemIcon id="spell_engine:spell_book" /><ItemIcon id="runes:arcane_stone" /></ItemGrid>

| 现象 | 优先检查 |
| --- | --- |
| 法术没有出现在快捷栏 | 是否装备了配置好的书，书中是否已有该法术，手持武器是否允许使用？ |
| 招式出现却不能释放 | 先检查符文或弹药、冷却、有效目标与距离，再看当前按键。 |
| 开始施法却没有命中 | 蓄力或引导时间、目标条件与视线。 |
| 伤害或治疗效果偏低 | 核对该招式的属性，再比较手持武器与护甲。护甲值更高不代表法术强度更高。 |

每次只调整一项，再安全试放。能看到预期招式，并产生说明中的攻击、治疗或防护效果，才算配置成功。
