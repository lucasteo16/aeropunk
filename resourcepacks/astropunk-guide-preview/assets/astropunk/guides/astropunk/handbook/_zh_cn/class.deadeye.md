---
navigation:
  title: "神射手"
  position: 5
  parent: combat.martial.md
  icon: archers:rapid_crossbow
item_ids:
  - archers_expansion:bounty_hunter_chest
  - archers_expansion:bounty_hunter_feet
  - archers_expansion:bounty_hunter_head
  - archers_expansion:bounty_hunter_legs
  - archers_expansion:deadeye_chest
  - archers_expansion:deadeye_feet
  - archers_expansion:deadeye_head
  - archers_expansion:deadeye_legs
  - archers_expansion:netherite_deadeye_chest
  - archers_expansion:netherite_deadeye_feet
  - archers_expansion:netherite_deadeye_head
  - archers_expansion:netherite_deadeye_legs
---

# 神射手

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Archers+Expansion+Deadeye+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Archers+Expansion+%E7%A5%9E%E5%B0%84%E6%89%8B+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

神射手使用弩进行物理远程战斗，结合快射与控制。

![神射手战斗](images/visual-deadeye-combat.png)

### 入门配装示例

入门配装示例：职业入门武器搭配目录中的第一套护甲。这是一种可合成选择，并非官方或最优构筑。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"archers:archer_armor_feet",count:1},{id:"archers:archer_armor_legs",count:1},{id:"archers:archer_armor_chest",count:1},{id:"archers:archer_armor_head",count:1}],HandItems:[{id:"archers:rapid_crossbow",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="archers:rapid_crossbow" /><ItemIcon id="archers:archer_armor_feet" /><ItemIcon id="archers:archer_armor_legs" /><ItemIcon id="archers:archer_armor_chest" /><ItemIcon id="archers:archer_armor_head" /></ItemGrid>

### 入门装备

<ItemGrid><ItemIcon id="archers:rapid_crossbow" /></ItemGrid>

<ItemLink id="archers:rapid_crossbow" />

<Recipe id="archers:rapid_crossbow" />

### 准备阶段与首次战斗

神射手属于弓术体系中的弩类，发布说明把神射手招式描述为快速而刁钻的射击，以及附带负面效果的箭。弩装填一次后由你决定何时释放，因此职业书里的致残与毒气招式更贴合这种节奏。弓箭手与游侠护甲仍然提供远程加成，神射手套装另有自己的属性。一次成功的首战，是在两只怪物靠近之前各拦下一次，一只靠致残射击，一只靠普通弩伤。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次射击 | 一把弩、弩箭，以及通畅的射界。 | 材料允许时先做速射弩，否则用原版弩开始，先熟悉装填节奏。 |
| 中期起步：神射手职业书 | 周围有书架的法术绑定台、神射手职业书，以及学习费用。 | 绑定并装备职业书，手持弩。下矿前先确认每个招式的射程。 |
| 中期：护甲 | 可合成的神射手护甲，或扩展包中的赏金猎人护甲。 | 尽量凑齐一套，而不是把单件升级品混进普通护甲。比较提示中的属性。 |
| 后期：下界合金 | 下界合金材料、锻造模板，以及神射手或赏金猎人部件。 | 升级下界合金神射手套装，若已有基础套装，也可使用末地战利品中的军械库升级。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 快速射击 | 预备效果 |
| 弹跳箭 | 投射物 |
| 致残射击 | 投射物 |
| 窒息毒气 | 投射物 |
| 毒液桶 | 职业能力 |
| 分身 | 自身效果 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择神射手法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="archers:rapid_crossbow" /><ItemIcon id="minecraft:crossbow" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 神射手 | <ItemLink id="archers:rapid_crossbow" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 弩专精 | <ItemLink id="minecraft:crossbow" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@archers" />

长弓、短弓与弩在蓄力速度和射击伤害之间取舍。长矛提供近战选择，弓箭手与游侠护甲提供远程属性。

### 武器

| 分类 | 物品 | 定位 |
| --- | --- | --- |
| <ItemLink id="archers:rapid_crossbow" /> | <ItemGrid><ItemIcon id="archers:rapid_crossbow" /><ItemIcon id="archers:heavy_crossbow" /><ItemIcon id="archers:netherite_rapid_crossbow" /><ItemIcon id="archers:netherite_heavy_crossbow" /></ItemGrid> | 弩类，装填一发后由你决定发射时机 |

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
| <ItemLink id="archers_expansion:deadeye_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:deadeye_head" /><ItemIcon id="archers_expansion:deadeye_chest" /><ItemIcon id="archers_expansion:deadeye_legs" /><ItemIcon id="archers_expansion:deadeye_feet" /></ItemGrid> |
| <ItemLink id="archers_expansion:netherite_deadeye_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:netherite_deadeye_head" /><ItemIcon id="archers_expansion:netherite_deadeye_chest" /><ItemIcon id="archers_expansion:netherite_deadeye_legs" /><ItemIcon id="archers_expansion:netherite_deadeye_feet" /></ItemGrid> |
| <ItemLink id="archers_expansion:bounty_hunter_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:bounty_hunter_head" /><ItemIcon id="archers_expansion:bounty_hunter_chest" /><ItemIcon id="archers_expansion:bounty_hunter_legs" /><ItemIcon id="archers_expansion:bounty_hunter_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
