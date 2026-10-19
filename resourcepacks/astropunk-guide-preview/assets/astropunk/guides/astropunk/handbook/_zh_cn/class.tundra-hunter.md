---
navigation:
  title: "冻原猎手"
  position: 7
  parent: combat.martial.md
  icon: archers_expansion:tundra_hunter_chest
item_ids:
  - archers_expansion:netherite_tundra_hunter_chest
  - archers_expansion:netherite_tundra_hunter_feet
  - archers_expansion:netherite_tundra_hunter_head
  - archers_expansion:netherite_tundra_hunter_legs
  - archers_expansion:polar_stalker_chest
  - archers_expansion:polar_stalker_feet
  - archers_expansion:polar_stalker_head
  - archers_expansion:polar_stalker_legs
  - archers_expansion:tundra_hunter_chest
  - archers_expansion:tundra_hunter_feet
  - archers_expansion:tundra_hunter_head
  - archers_expansion:tundra_hunter_legs
---

# 冻原猎手

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Archers+Expansion+Tundra+Hunter+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Archers+Expansion+%E5%86%BB%E5%8E%9F%E7%8C%8E%E6%89%8B+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

冻原猎手将弓箭攻击与冰冻射击、持续冰霜区域结合。

![苔原猎人战斗](images/visual-tundra-hunter-combat.png)

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

冻原猎手的职业书以冻结射击与冰霜区域为主，弓只是投放寒冷的手段，而不是整个构筑。长弓能让范围招式落在怪群站位上，短弓让你在施法之间保持移动。冻原猎人与极地追猎者护甲提供冰霜与远程属性。一次成功的首战，是把一只怪物留在冰霜区域内，让它在减速中被打完。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次冰霜射击 | 一把弓、箭矢，以及一个附带寒冷效果的招式。 | 先用复合长弓，招式投向怪群而不是单个目标，减速才值得消耗。 |
| 中期起步：职业书 | 法术绑定台、冻原猎手职业书，以及学习费用。 | 绑定职业书并与弓一同装备。为走出冰霜区域的怪物留一手近战。 |
| 中期：护甲 | 冻原猎手护甲，或作为备选家族的极地追猎者护甲。 | 选定一个家族并凑齐。两者都是远程套装，比较提示属性而不是只看名称。 |
| 后期：下界合金 | 下界合金材料，以及对应的冻原猎手或极地追猎者部件。 | 经常挨打就先升级胸甲，否则升级你最依赖的那条加成所在的位置。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 冰冻射击 | 预备效果 |
| 冰霜契约 | 范围 |
| 极地齐射 | 投射物 |
| 魔法水晶箭 | 投射物 |
| 北极熊守卫 | 自身效果 |
| 冰霜连射 | 持续范围 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择冻原猎手法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="archers_expansion:tundra_hunter_chest" /><ItemIcon id="minecraft:bow" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 冻原猎手 | <ItemLink id="archers_expansion:tundra_hunter_chest" /> |

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
| <ItemLink id="archers:composite_longbow" /> | <ItemGrid><ItemIcon id="archers:composite_longbow" /><ItemIcon id="archers:royal_longbow" /><ItemIcon id="archers:netherite_longbow" /></ItemGrid> | 远程，蓄力较久，适合向怪群投放范围 |
| <ItemLink id="archers:mechanic_shortbow" /> | <ItemGrid><ItemIcon id="archers:mechanic_shortbow" /><ItemIcon id="archers:netherite_shortbow" /></ItemGrid> | 远程，蓄力较快，适合在施法之间移动 |
| <ItemLink id="archers:rapid_crossbow" /> | <ItemGrid><ItemIcon id="archers:rapid_crossbow" /><ItemIcon id="archers:heavy_crossbow" /><ItemIcon id="archers:netherite_rapid_crossbow" /><ItemIcon id="archers:netherite_heavy_crossbow" /></ItemGrid> | 远程，装填后把冰霜区域留在原地 |

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
| <ItemLink id="archers_expansion:tundra_hunter_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:tundra_hunter_head" /><ItemIcon id="archers_expansion:tundra_hunter_chest" /><ItemIcon id="archers_expansion:tundra_hunter_legs" /><ItemIcon id="archers_expansion:tundra_hunter_feet" /></ItemGrid> |
| <ItemLink id="archers_expansion:netherite_tundra_hunter_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:netherite_tundra_hunter_head" /><ItemIcon id="archers_expansion:netherite_tundra_hunter_chest" /><ItemIcon id="archers_expansion:netherite_tundra_hunter_legs" /><ItemIcon id="archers_expansion:netherite_tundra_hunter_feet" /></ItemGrid> |
| <ItemLink id="archers_expansion:polar_stalker_chest" /> | <ItemGrid><ItemIcon id="archers_expansion:polar_stalker_head" /><ItemIcon id="archers_expansion:polar_stalker_chest" /><ItemIcon id="archers_expansion:polar_stalker_legs" /><ItemIcon id="archers_expansion:polar_stalker_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
