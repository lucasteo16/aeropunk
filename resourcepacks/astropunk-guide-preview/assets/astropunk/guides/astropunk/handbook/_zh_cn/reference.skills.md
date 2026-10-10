---
navigation:
  title: "战斗"
  position: 6
  icon: minecraft:iron_sword
---

# 战斗

## 可玩的职业

通过装备、职业书与技能树选择构筑，并没有永久锁定职业的选择界面。技能根节点仍可能互斥，更换装备不会返还已分配点数。

### 武技职业

<EmiSearch query="@archers" /> <EmiSearch query="@berserker_rpg" /> <EmiSearch query="@forcemaster_rpg" /> <EmiSearch query="@rogues" />

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

<EmiSearch query="@bards_rpg" /> <EmiSearch query="@elemental_wizards_rpg" /> <EmiSearch query="@paladins" /> <EmiSearch query="@witcher_rpg" /> <EmiSearch query="@wizards" />

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

## 装备与能力

让武器或法器、护甲加成和饰品属性与能力所用的属性相配。火焰法术强度不会增强冰霜法术。普通经验等级用于法术绑定，职业和武器技能点则用于发展各自的技能树。

- <ItemImage id="minecraft:iron_chestplate" /> [装备](reference.equipment.md) 武器、护甲、饰品与起步制作。
- <ItemImage id="minecraft:enchanted_book" /> [法术与能力](combat.abilities.md) 职业书准备、绑定消耗与施法要求。

***

## 起步步骤

<EmiSearch query="@spell_engine" />

<ItemGrid><ItemIcon id="spell_engine:spell_binding" /></ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

<Recipe id="spell_engine:spell_binding_table" />

1. 从上方选择玩法，制作对应的起步武器或法器。武器自带能力与职业书能力不同。
2. 制作法术绑定台，用普通书选择对应职业书，再根据界面显示的经验与青金石要求绑定能力。
3. 将职业书放入法术书栏，手持兼容装备。查看能力提示，确认弹药、符文或其他施法要求。
4. 按 <KeyBind id="key.puffish_skills.open" /> 发展相连节点。投入点数前查看互斥根节点，更换装备不会返还点数。

***

## 详细参考

- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [护甲与状态](equipment.display.md)
- [武器与闪避](combat.handling.md)
- [近战与弓弩](combat.martial.md)
- [法术与支援](combat.magic.md)
- [技能发展](combat.skills.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Additional Jewelry (RPG Series Plus)](images/catalog-rULzJh3O.png) [Additional Jewelry (RPG Series Plus)](equipment.accessories.md) | 为 More RPG Classes 的扩展职业增加首饰。 | <EmiSearch query="@additional_rpg_jewelry" /> |
| ![Archers (RPG Series)](images/catalog-QgooUXAJ.png) [Archers (RPG Series)](combat.martial.md) | 增加围绕弓箭与远程能力设计的弓箭手职业。 | <EmiSearch query="@archers" /> |
| ![Archers Expansion (RPG Series Plus)](images/catalog-1BHIIm4m.png) [Archers Expansion (RPG Series Plus)](combat.martial.md) | 增加弓箭手分支职业，提供冰冻、施加状态效果与爆炸箭能力。 | <EmiSearch query="@archers_expansion" /> |
| ![Armory (RPG Series)](images/catalog-PJvJUdGw.png) [Armory (RPG Series)](equipment.weapons-armor.md) | 增加面向不同职业的盔甲套装与套装加成。 | <EmiSearch query="@armory_rpgs" /> |
| ![Arsenal (RPG Series)](images/catalog-LiP9Q3KV.png) [Arsenal (RPG Series)](equipment.weapons-armor.md) | 增加通过战斗遭遇而非合成获取的传奇武器。 | <EmiSearch query="@arsenal" /> |
| ![Bard (RPG Series Plus)](images/catalog-kL7Bjgmw.png) [Bard (RPG Series Plus)](combat.magic.md) | 增加以歌曲与歌谣支援队友的吟游诗人职业。 | <EmiSearch query="@bards_rpg" /> |
| ![Berserker (RPG Series Plus)](images/catalog-8hqOZzxM.png) [Berserker (RPG Series Plus)](combat.martial.md) | 增加持斧狂战士，利用狂怒在低生命值时提高伤害。 | <EmiSearch query="@berserker_rpg" /> |
| ![Better Combat](images/catalog-5sy6g3kz.png) [Better Combat](combat.handling.md) | 通过武器攻击动画与更流畅的攻击机制改进近战。 | 无独立物品查询 |
| ![Combat Roll](images/catalog-wGKYL7st.png) [Combat Roll](combat.handling.md) | 增加闪避翻滚及相关属性与附魔。 | 无独立物品查询 |
| ![Critical Strike](images/catalog-ilvNBzFn.png) [Critical Strike](combat.handling.md) | 为近战与远程攻击增加概率触发的暴击。 | 无独立物品查询 |
| ![Curios API](images/catalog-vvuO3ImH.png) [Curios API](equipment.accessories.md) | 提供可扩展的饰品装备栏。 | 无独立物品查询 |
| ![Detail Armor Bar Reconstructed](images/catalog-Si9Uim4y.png) [Detail Armor Bar Reconstructed](equipment.display.md) | 在盔甲状态条中显示更多护甲信息。 | 无独立物品查询 |
| ![Elemental Wizards (RPG Series Plus)](images/catalog-PeZ4h4i0.png) [Elemental Wizards (RPG Series Plus)](combat.magic.md) | 为 Wizards 增加大地、水与风元素施法分支职业。 | <EmiSearch query="@elemental_wizards_rpg" /> |
| ![Forcemaster (RPG Series Plus)](images/catalog-K3yHebFL.png) [Forcemaster (RPG Series Plus)](combat.martial.md) | 增加使用拳套的武术职业，以奥术力量强化攻击。 | <EmiSearch query="@forcemaster_rpg" /> |
| ![Jewelry (RPG Series)](images/catalog-sNJAIjUm.png) [Jewelry (RPG Series)](equipment.accessories.md) | 增加可开采宝石与可制作首饰，用于提升战斗属性。 | <EmiSearch query="@jewelry" /> |
| ![More Relics (RPG Series Plus)](images/catalog-IZ3b4kEa.png) [More Relics (RPG Series Plus)](equipment.accessories.md) | 为 More RPG Classes 的扩展职业增加 Relics 饰品。 | <EmiSearch query="@more_relics" /> |
| ![More RPG Classes - Skill Tree (RPG Series Plus)](images/catalog-3OYmNUDq.png) [More RPG Classes - Skill Tree (RPG Series Plus)](combat.skills.md) | 为 More RPG Classes 的扩展职业增加职业技能树支持。 | 无独立物品查询 |
| ![Paladins & Priests (RPG Series)](images/catalog-FxXkHaLe.png) [Paladins & Priests (RPG Series)](combat.magic.md) | 增加专注防护与治疗的圣骑士及牧师职业。 | <EmiSearch query="@paladins" /> |
| ![Pufferfish's Skills](images/catalog-hqQqvaa4.png) [Pufferfish's Skills](combat.skills.md) | 提供可自定义的技能系统与技能树界面。 | 无独立物品查询 |
| ![Relics (RPG Series)](images/catalog-BDQucwF0.png) [Relics (RPG Series)](equipment.accessories.md) | 为 RPG Series 角色搭配增加强化战斗能力的饰品。 | <EmiSearch query="@relics_rpgs" /> |
| ![Rogues & Warriors (RPG Series)](images/catalog-3MKqoGuP.png) [Rogues & Warriors (RPG Series)](combat.martial.md) | 增加拥有不同近战能力的游荡者与战士职业。 | <EmiSearch query="@rogues" /> |
| ![Runes](images/catalog-lP9Yrr1E.png) [Runes](combat.magic.md) | 增加可制作的符文，作为施法消耗的弹药。 | <EmiSearch query="@runes" /> |
| ![Skill Tree (RPG Series)](images/catalog-PjDhruSC.png) [Skill Tree (RPG Series)](combat.skills.md) | 为 RPG Series 角色增加职业技能树。 | <EmiSearch query="@skill_tree_rpgs" /> |
| ![Status Effect Bars Reforged](images/catalog-TxIuhIFo.png) [Status Effect Bars Reforged](equipment.display.md) | 以可自定义进度条显示状态效果剩余时间。 | 无独立物品查询 |
| ![Stylish Effects](images/catalog-onDuQF5e.png) [Stylish Effects](equipment.display.md) | 将状态效果显示整理成紧凑且可调整的界面布局。 | 无独立物品查询 |
| ![Witcher (RPG Series Plus)](images/catalog-4eW1c7Gj.png) [Witcher (RPG Series Plus)](combat.magic.md) | 增加以猎杀怪物为主题的猎魔人职业与战斗能力。 | <EmiSearch query="@witcher_rpg" /> |
| ![Wizards (RPG Series)](images/catalog-NkGaQMDA.png) [Wizards (RPG Series)](combat.magic.md) | 增加使用奥术、火焰与冰霜法术的巫师战斗体系。 | <EmiSearch query="@wizards" /> |
