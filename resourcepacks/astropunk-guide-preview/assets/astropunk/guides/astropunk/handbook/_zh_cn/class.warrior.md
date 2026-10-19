---
navigation:
  title: "战士"
  position: 0
  parent: combat.martial.md
  icon: rogues:iron_double_axe
item_ids:
  - rogues:berserker_armor_chest
  - rogues:berserker_armor_feet
  - rogues:berserker_armor_head
  - rogues:berserker_armor_legs
  - rogues:diamond_double_axe
  - rogues:diamond_glaive
  - rogues:golden_double_axe
  - rogues:golden_glaive
  - rogues:iron_double_axe
  - rogues:iron_glaive
  - rogues:netherite_berserker_armor_chest
  - rogues:netherite_berserker_armor_feet
  - rogues:netherite_berserker_armor_head
  - rogues:netherite_berserker_armor_legs
  - rogues:netherite_double_axe
  - rogues:netherite_glaive
  - rogues:stone_double_axe
  - rogues:warrior_armor_chest
  - rogues:warrior_armor_feet
  - rogues:warrior_armor_head
  - rogues:warrior_armor_legs
---

# 战士

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Rogues+and+Warriors+Warrior+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Rogues+and+Warriors+%E6%88%98%E5%A3%AB+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

战士使用双刃斧与战刃，招式包含投掷、冲锋与自身防御效果。

![盗贼与战士装备](images/visual-martial-equipment.png)

### 入门配装示例

入门配装示例：职业入门武器搭配目录中的第一套护甲。这是一种可合成选择，并非官方或最优构筑。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"rogues:warrior_armor_feet",count:1},{id:"rogues:warrior_armor_legs",count:1},{id:"rogues:warrior_armor_chest",count:1},{id:"rogues:warrior_armor_head",count:1}],HandItems:[{id:"rogues:iron_double_axe",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="rogues:iron_double_axe" /><ItemIcon id="rogues:warrior_armor_feet" /><ItemIcon id="rogues:warrior_armor_legs" /><ItemIcon id="rogues:warrior_armor_chest" /><ItemIcon id="rogues:warrior_armor_head" /></ItemGrid>

### 入门装备

<ItemGrid><ItemIcon id="rogues:iron_double_axe" /></ItemGrid>

<ItemLink id="rogues:iron_double_axe" />

<Recipe id="rogues:iron_double_axe" />

### 准备阶段与首次战斗

战士使用重型慢速武器，发布说明为战士法典列出双刃斧与长柄刀。每次挥击都需要你先站定，因此选准时机、用冲锋或战吼拉近距离，才是这个职业的收益所在。战士护甲是入门套装，狂战士护甲是同一列表中的更重家族。一次成功的首战，是冲进两只怪物中间接一个范围招式，结束时你仍然站立而怪群已被削薄。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次重武器 | 一把双刃斧或长柄刀、食物，以及足够的挥击空间。 | 先合成铁双刃斧。先在单只怪物身上练习挥击节奏，再打群战。 |
| 中期起步：战士法典 | 法术绑定台、战士法典，以及学习费用。 | 绑定法典，并留一个投掷或冲锋招式，应对怪物后撤的瞬间。 |
| 中期：护甲 | 战士护甲，或狂战士护甲。 | 先凑齐战士套装。把狂战士护甲当作另一个选择，而不是免费升级。 |
| 后期：下界合金 | 下界合金材料，以及狂战士护甲部件。 | 只有在打算长期近战时才升级狂战士套装，否则把材料用在武器路线上。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 碎裂投掷 | 投射物 |
| 撒网 | 投射物 |
| 冲锋 | 自身效果 |
| 挫志怒吼 | 范围 |
| 背水一战 | 自身效果 |
| 致死打击 | 近战攻击 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择战士法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="rogues:iron_double_axe" /><ItemIcon id="rogues:iron_glaive" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 战士之路 | <ItemLink id="rogues:iron_double_axe" /> |

- [盗贼](class.rogue.md)

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 双刃斧专精 | <ItemLink id="rogues:iron_double_axe" /> |
| 长柄刀专精 | <ItemLink id="rogues:iron_glaive" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@rogues" />

本页列出战士使用的双刃斧与战刃。选择时比较伤害、攻速与武器招式。

### 武器

| 分类 | 物品 | 定位 |
| --- | --- | --- |
| <ItemLink id="rogues:stone_double_axe" /> | <ItemGrid><ItemIcon id="rogues:stone_double_axe" /><ItemIcon id="rogues:iron_double_axe" /><ItemIcon id="rogues:golden_double_axe" /><ItemIcon id="rogues:diamond_double_axe" /><ItemIcon id="rogues:netherite_double_axe" /></ItemGrid> | 重型慢速武器，双刃大幅挥击 |
| <ItemLink id="rogues:iron_glaive" /> | <ItemGrid><ItemIcon id="rogues:iron_glaive" /><ItemIcon id="rogues:golden_glaive" /><ItemIcon id="rogues:diamond_glaive" /><ItemIcon id="rogues:netherite_glaive" /></ItemGrid> | 重型慢速武器，长柄大幅挥击 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="rogues:warrior_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:warrior_armor_head" /><ItemIcon id="rogues:warrior_armor_chest" /><ItemIcon id="rogues:warrior_armor_legs" /><ItemIcon id="rogues:warrior_armor_feet" /></ItemGrid> |
| <ItemLink id="rogues:berserker_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:berserker_armor_head" /><ItemIcon id="rogues:berserker_armor_chest" /><ItemIcon id="rogues:berserker_armor_legs" /><ItemIcon id="rogues:berserker_armor_feet" /></ItemGrid> |
| <ItemLink id="rogues:netherite_berserker_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:netherite_berserker_armor_head" /><ItemIcon id="rogues:netherite_berserker_armor_chest" /><ItemIcon id="rogues:netherite_berserker_armor_legs" /><ItemIcon id="rogues:netherite_berserker_armor_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
