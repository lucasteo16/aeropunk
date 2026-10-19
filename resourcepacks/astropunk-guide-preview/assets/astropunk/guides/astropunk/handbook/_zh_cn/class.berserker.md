---
navigation:
  title: "狂战士"
  position: 1
  parent: combat.martial.md
  icon: berserker_rpg:iron_berserker_axe
item_ids:
  - berserker_rpg:diamond_berserker_axe
  - berserker_rpg:flint_berserker_axe
  - berserker_rpg:golden_berserker_axe
  - berserker_rpg:iron_berserker_axe
  - berserker_rpg:netherite_berserker_axe
  - berserker_rpg:netherite_northling_chest
  - berserker_rpg:netherite_northling_feet
  - berserker_rpg:netherite_northling_head
  - berserker_rpg:netherite_northling_legs
  - berserker_rpg:northling_chest
  - berserker_rpg:northling_feet
  - berserker_rpg:northling_head
  - berserker_rpg:northling_legs
  - berserker_rpg:stone_berserker_axe
  - berserker_rpg:unique_berserker_axe_1
  - berserker_rpg:unique_berserker_axe_2
  - berserker_rpg:unique_sword_1
  - berserker_rpg:warlord_chest
  - berserker_rpg:warlord_feet
  - berserker_rpg:warlord_head
  - berserker_rpg:warlord_legs
  - berserker_rpg:wildling_chest
  - berserker_rpg:wildling_feet
  - berserker_rpg:wildling_head
  - berserker_rpg:wildling_legs
---

# 狂战士

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Berserker+RPG+Berserker+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Berserker+RPG+%E7%8B%82%E6%88%98%E5%A3%AB+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

狂战士使用狂战斧，结合近战攻击与怒气招式。

![狂战士护甲](images/visual-berserker-armor.png)

### 入门配装示例

入门配装示例：职业入门武器搭配目录中的第一套护甲。这是一种可合成选择，并非官方或最优构筑。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"berserker_rpg:wildling_feet",count:1},{id:"berserker_rpg:wildling_legs",count:1},{id:"berserker_rpg:wildling_chest",count:1},{id:"berserker_rpg:wildling_head",count:1}],HandItems:[{id:"berserker_rpg:iron_berserker_axe",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="berserker_rpg:iron_berserker_axe" /><ItemIcon id="berserker_rpg:wildling_feet" /><ItemIcon id="berserker_rpg:wildling_legs" /><ItemIcon id="berserker_rpg:wildling_chest" /><ItemIcon id="berserker_rpg:wildling_head" /></ItemGrid>

### 入门装备

<ItemGrid><ItemIcon id="berserker_rpg:iron_berserker_axe" /></ItemGrid>

<ItemLink id="berserker_rpg:iron_berserker_axe" />

<Recipe id="berserker_rpg:iron_berserker_axe" />

### 准备阶段与首次战斗

狂战士是以怒气属性为核心的物理近战职业，发布说明写明生命越低，造成的伤害越高。因此斧类武器与一套退出战斗的计划，比完美套装更重要。荒原与北地护甲提供怒气加成，督军护甲是第四个家族。一次成功的首战，是你在带伤但仍有掌控的情况下解决一只怪物，并留有脱离接触的招式。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次用斧 | 一把狂战士斧、食物，以及一处能安全测试怒气加成的场地。 | 合成铁狂战士斧。先一次只打一只怪物，摸清自己能花掉多少生命。 |
| 中期起步：职业书 | 法术绑定台、狂战士职业书，以及学习费用。 | 绑定职业书，并保留一个防御或治疗手段，因为这个职业奖励低生命。 |
| 中期：护甲 | 荒原或北地护甲。 | 先凑齐一个家族。替换部件前先读提示里的怒气属性。 |
| 后期：下界合金 | 下界合金材料与对应的北地部件，或箱中战利品里的独特斧。 | 升级北地护甲，并把捡到的独特斧与自己合成的比较后再更换。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 狂野之怒 | 预备效果 |
| 血腥打击 | 范围 |
| 拖拽 | 范围 |
| 鲜血清算 | 自身效果 |
| 暴怒 | 自身效果 |
| 北地断头斩 | 瞄准目标 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择狂战士法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="berserker_rpg:iron_berserker_axe" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 狂战士 | <ItemLink id="berserker_rpg:iron_berserker_axe" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 狂战斧专精 | <ItemLink id="berserker_rpg:iron_berserker_axe" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@berserker_rpg" />

狂战斧将近战攻击与怒气招式结合，护甲与独特武器提供不同属性。

### 武器

| 分类 | 物品 | 定位 |
| --- | --- | --- |
| <ItemLink id="berserker_rpg:stone_berserker_axe" /> | <ItemGrid><ItemIcon id="berserker_rpg:stone_berserker_axe" /><ItemIcon id="berserker_rpg:iron_berserker_axe" /><ItemIcon id="berserker_rpg:golden_berserker_axe" /><ItemIcon id="berserker_rpg:diamond_berserker_axe" /><ItemIcon id="berserker_rpg:netherite_berserker_axe" /><ItemIcon id="berserker_rpg:unique_berserker_axe_1" /><ItemIcon id="berserker_rpg:unique_berserker_axe_2" /></ItemGrid> | 怒气修正 |
| <ItemLink id="berserker_rpg:flint_berserker_axe" /> | <ItemGrid><ItemIcon id="berserker_rpg:flint_berserker_axe" /></ItemGrid> | 入门斧，用于凑齐上一行的材料 |
| <ItemLink id="berserker_rpg:unique_sword_1" /> | <ItemGrid><ItemIcon id="berserker_rpg:unique_sword_1" /></ItemGrid> | 怒气修正，只能通过战利品获得 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="berserker_rpg:wildling_chest" /> | <ItemGrid><ItemIcon id="berserker_rpg:wildling_head" /><ItemIcon id="berserker_rpg:wildling_chest" /><ItemIcon id="berserker_rpg:wildling_legs" /><ItemIcon id="berserker_rpg:wildling_feet" /></ItemGrid> |
| <ItemLink id="berserker_rpg:northling_chest" /> | <ItemGrid><ItemIcon id="berserker_rpg:northling_head" /><ItemIcon id="berserker_rpg:northling_chest" /><ItemIcon id="berserker_rpg:northling_legs" /><ItemIcon id="berserker_rpg:northling_feet" /></ItemGrid> |
| <ItemLink id="berserker_rpg:netherite_northling_chest" /> | <ItemGrid><ItemIcon id="berserker_rpg:netherite_northling_head" /><ItemIcon id="berserker_rpg:netherite_northling_chest" /><ItemIcon id="berserker_rpg:netherite_northling_legs" /><ItemIcon id="berserker_rpg:netherite_northling_feet" /></ItemGrid> |
| <ItemLink id="berserker_rpg:warlord_chest" /> | <ItemGrid><ItemIcon id="berserker_rpg:warlord_head" /><ItemIcon id="berserker_rpg:warlord_chest" /><ItemIcon id="berserker_rpg:warlord_legs" /><ItemIcon id="berserker_rpg:warlord_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
