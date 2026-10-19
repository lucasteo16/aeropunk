---
navigation:
  title: "战争弓手"
  position: 6
  parent: combat.martial.md
  icon: archers_expansion:war_archer_chest
item_ids:
  - archers_expansion:netherite_war_archer_chest
  - archers_expansion:netherite_war_archer_feet
  - archers_expansion:netherite_war_archer_head
  - archers_expansion:netherite_war_archer_legs
  - archers_expansion:sentinel_archer_chest
  - archers_expansion:sentinel_archer_feet
  - archers_expansion:sentinel_archer_head
  - archers_expansion:sentinel_archer_legs
  - archers_expansion:war_archer_chest
  - archers_expansion:war_archer_feet
  - archers_expansion:war_archer_head
  - archers_expansion:war_archer_legs
---

# 战争弓手

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Archers+Expansion+War+Archer+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Archers+Expansion+%E6%88%98%E4%BA%89%E5%BC%93%E6%89%8B+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

战争弓手将弓箭攻击与火焰远程招式、燃烧区域结合。

![战争弓箭手战斗](images/visual-war-archer-combat.png)

### 入门配装示例

入门配装示例：职业入门武器搭配目录中的第一套护甲。这是一种可合成选择，并非官方或最优构筑。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"archers:archer_armor_feet",count:1},{id:"archers:archer_armor_legs",count:1},{id:"archers:archer_armor_chest",count:1},{id:"archers:archer_armor_head",count:1}],HandItems:[{id:"archers:composite_longbow",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="archers:composite_longbow" /><ItemIcon id="archers:archer_armor_feet" /><ItemIcon id="archers:archer_armor_legs" /><ItemIcon id="archers:archer_armor_chest" /><ItemIcon id="archers:archer_armor_head" /></ItemGrid>

### 入门装备

<ItemGrid><ItemIcon id="archers:composite_longbow" /></ItemGrid>

<ItemLink id="archers:composite_longbow" />

<Recipe id="archers:composite_longbow" />

### 准备阶段与首次战斗

战争弓手把冰霜减速换成燃烧区域与爆发伤害，发布说明把战争弓手套装称为更安全的厚甲远程选择。火焰与爆炸招式奖励命中聚集的敌人，因此能打到怪群的武器比单体弓更有价值。哨兵射手是备选护甲家族。一次成功的首战，是用一片燃烧区域加后续箭矢清掉一群怪物，没有怪物留在近身距离。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次燃烧射击 | 一把弓或弩、弹药，以及一个会在地面留下火焰的招式。 | 先做复合长弓，把招式打向怪物正在走进的地面，而不是直接打向怪物。 |
| 中期起步：职业书 | 法术绑定台、战争弓手职业书，以及学习费用。 | 绑定职业书，并留一个能定住目标的射击，接上随后的范围招式。 |
| 中期：护甲 | 战争弓手护甲，或作为备选家族的哨兵射手护甲。 | 选择你能凑齐的一套。发布说明称战争弓手护甲更厚重，可对比其防护属性。 |
| 后期：下界合金 | 下界合金材料，以及战争弓手或哨兵射手部件。 | 先把下界合金战争弓手套装升级完成，再考虑第二个家族。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 双重射击 | 射箭 |
| 灼热箭 | 预备效果 |
| 近距射击 | 投射物 |
| 钉住 | 投射物 |
| 焦土 | 持续范围 |
| 爆炸桶 | 自身效果 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择战争弓手法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="archers_expansion:war_archer_chest" /><ItemIcon id="minecraft:bow" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 战争弓手 | <ItemLink id="archers_expansion:war_archer_chest" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 弓专精 | <ItemLink id="minecraft:bow" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@archers" />

长弓、短弓与弩在蓄力速度和射击伤害之间取舍。长矛提供近战选择，弓箭手与游侠护甲提供远程属性。

### 武器

| 分类 | 物品 | 定位 |
| --- | --- | --- |
| <ItemLink id="archers:composite_longbow" /> | <ItemGrid><ItemIcon id="archers:composite_longbow" /><ItemIcon id="archers:royal_longbow" /><ItemIcon id="archers:netherite_longbow" /></ItemGrid> | 远程，蓄力较久，适合范围射击 |
| <ItemLink id="archers:mechanic_shortbow" /> | <ItemGrid><ItemIcon id="archers:mechanic_shortbow" /><ItemIcon id="archers:netherite_shortbow" /></ItemGrid> | 远程，蓄力较快，适合移动中爆发 |
| <ItemLink id="archers:rapid_crossbow" /> | <ItemGrid><ItemIcon id="archers:rapid_crossbow" /><ItemIcon id="archers:heavy_crossbow" /><ItemIcon id="archers:netherite_rapid_crossbow" /><ItemIcon id="archers:netherite_heavy_crossbow" /></ItemGrid> | 远程，装填后留下燃烧区域 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="archers:archer_armor_chest" /> | <ItemGrid><ItemIcon id="archers:archer_armor_head" /><ItemIcon id="archers:archer_armor_chest" /><ItemIcon id="archers:archer_armor_legs" /><ItemIcon id="archers:archer_armor_feet" /></ItemGrid> |
| <ItemLink id="archers:ranger_armor_chest" /> | <ItemGrid><ItemIcon id="archers:ranger_armor_head" /><ItemIcon id="archers:ranger_armor_chest" /><ItemIcon id="archers:ranger_armor_legs" /><ItemIcon id="archers:ranger_armor_feet" /></ItemGrid> |
| <ItemLink id="archers:netherite_ranger_armor_chest" /> | <ItemGrid><ItemIcon id="archers:netherite_ranger_armor_head" /><ItemIcon id="archers:netherite_ranger_armor_chest" /><ItemIcon id="archers:netherite_ranger_armor_legs" /><ItemIcon id="archers:netherite_ranger_armor_feet" /></ItemGrid> |

***

## 弓箭手扩展

<EmiSearch query="@archers_expansion" />

神射手、冻原猎手与战争弓手装备分别支持物理、冰霜及火焰远程构筑。赏金猎人、极地追猎者与哨卫弓手提供其他护甲套装。

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="archers_expansion:war_archer_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:war_archer_head" /><ItemIcon id="archers_expansion:war_archer_chest" /><ItemIcon id="archers_expansion:war_archer_legs" /><ItemIcon id="archers_expansion:war_archer_feet" /></ItemGrid> |
| <ItemLink id="archers_expansion:netherite_war_archer_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:netherite_war_archer_head" /><ItemIcon id="archers_expansion:netherite_war_archer_chest" /><ItemIcon id="archers_expansion:netherite_war_archer_legs" /><ItemIcon id="archers_expansion:netherite_war_archer_feet" /></ItemGrid> |
| <ItemLink id="archers_expansion:sentinel_archer_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:sentinel_archer_head" /><ItemIcon id="archers_expansion:sentinel_archer_chest" /><ItemIcon id="archers_expansion:sentinel_archer_legs" /><ItemIcon id="archers_expansion:sentinel_archer_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
