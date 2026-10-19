---
navigation:
  title: "使用武器与闪避"
  position: 0
  parent: reference.skills.md
  icon: minecraft:feather
---

# 使用武器与闪避

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Better+Combat+Combat+Roll+weapon+attacks+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Better+Combat+Combat+Roll+%E6%AD%A6%E5%99%A8%E6%94%BB%E5%87%BB+%E7%BF%BB%E6%BB%9A+%E6%95%99%E7%A8%8B)

## 攻击与武器类型

![使用职业装备进行近战](images/visual-melee-combat.png)

## 一览武器系列

| 系列 | 示例 | 差异 |
| --- | --- | --- |
| 剑或斧 | <ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_axe" /><ItemIcon id="rogues:iron_dagger" /></ItemGrid> | 单手快速攻击，距离较短。 |
| 巨剑或巨锤 | <ItemGrid><ItemIcon id="paladins:iron_claymore" /><ItemIcon id="paladins:iron_great_hammer" /></ItemGrid> | 挥动更慢，需要双手持握。 |
| 弓 | <ItemGrid><ItemIcon id="minecraft:bow" /><ItemIcon id="archers:composite_longbow" /></ItemGrid> | 拉弓后释放，拉满时伤害更高。 |
| 弩 | <ItemGrid><ItemIcon id="minecraft:crossbow" /></ItemGrid> | 先装填，再在合适的时机发射。 |
| 法杖或魔杖 | <ItemGrid><ItemIcon id="wizards:staff_arcane" /><ItemIcon id="wizards:wand_arcane" /></ItemGrid> | 施放武器法术，而不是挥击。 |

***

Better Combat 为支持的武器提供攻击模式与动画。比较攻击距离、攻速、伤害及双手要求，弓弩还各有蓄力或装填方式。

用 <KeyBind id="key.attack" /> 攻击，用 <KeyBind id="key.use" /> 使用物品。

***

## 翻滚与施法

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="wizards:staff_arcane" /><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

按 <KeyBind id="keybinds.combat_roll.roll" /> 翻滚。Combat Roll 提供闪避动作，并按当前移动方向翻滚。翻滚有短暂冷却，界面会显示剩余时间，同时消耗饥饿度，连续翻滚会更快需要进食。使用物品、跳跃或游泳时无法翻滚。

本整合默认关闭翻滚期间的无敌帧，因此请把翻滚当作重新走位，而不是必定躲开攻击。Critical Strike 提供近战暴击属性，武器动画或翻滚本身都不保证无敌。

法术招式使用 Spell Engine 快捷栏。若招式没有绑定按键，可在按键设置中分配。配方浏览器使用独立设置，按键重复时可能需要同时检查两处界面。

- [法术与招式](combat.abilities.md) 查看职业书绑定与法术快捷栏要求。
- [完整操作](help.controls.md)
- [技能成长](combat.skills.md) 在相连分支中分配职业与武器技能点。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Better Combat](images/catalog-5sy6g3kz.png) [Better Combat](combat.handling.md) | 通过武器攻击动画与更流畅的攻击机制改进近战。 | 无独立物品查询 |
| ![Combat Roll](images/catalog-wgkyl7st.png) [Combat Roll](combat.handling.md) | 增加闪避翻滚及相关属性与附魔。 | 无独立物品查询 |
| ![Critical Strike](images/catalog-ilvnbzfn.png) [Critical Strike](combat.handling.md) | 为近战与远程攻击增加概率触发的暴击。 | 无独立物品查询 |
