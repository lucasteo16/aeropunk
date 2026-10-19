---
navigation:
  title: "盗贼"
  position: 2
  parent: combat.martial.md
  icon: rogues:iron_dagger
item_ids:
  - rogues:assassin_armor_chest
  - rogues:assassin_armor_feet
  - rogues:assassin_armor_head
  - rogues:assassin_armor_legs
  - rogues:diamond_dagger
  - rogues:diamond_sickle
  - rogues:flint_dagger
  - rogues:golden_dagger
  - rogues:golden_sickle
  - rogues:iron_dagger
  - rogues:iron_sickle
  - rogues:netherite_assassin_armor_chest
  - rogues:netherite_assassin_armor_feet
  - rogues:netherite_assassin_armor_head
  - rogues:netherite_assassin_armor_legs
  - rogues:netherite_dagger
  - rogues:netherite_sickle
  - rogues:rogue_armor_chest
  - rogues:rogue_armor_feet
  - rogues:rogue_armor_head
  - rogues:rogue_armor_legs
---

# 盗贼

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Rogues+and+Warriors+Rogue+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Rogues+and+Warriors+%E7%9B%97%E8%B4%BC+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

盗贼使用匕首与镰刀，结合近战攻击、蓄势效果、陷阱与机动能力。

![盗贼与战士装备](images/visual-martial-equipment.png)

### 入门装备

<ItemGrid><ItemIcon id="rogues:iron_dagger" /></ItemGrid>

<ItemLink id="rogues:iron_dagger" />

<Recipe id="rogues:iron_dagger" />

### 入门配装示例

铁匕首搭配四件盗贼护甲，是一种可合成的入门配装，不是官方默认，也不是必选构筑。模型只展示外观与手持武器。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"rogues:rogue_armor_feet",count:1},{id:"rogues:rogue_armor_legs",count:1},{id:"rogues:rogue_armor_chest",count:1},{id:"rogues:rogue_armor_head",count:1}],HandItems:[{id:"rogues:iron_dagger",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="rogues:rogue_armor_head" /><ItemIcon id="rogues:rogue_armor_chest" /><ItemIcon id="rogues:rogue_armor_legs" /><ItemIcon id="rogues:rogue_armor_feet" /></ItemGrid>

### 准备阶段与首次战斗

盗贼职业书围绕闪避与戏弄对手，发布说明建议双持快速武器，也就是一手匕首或一手镰刀。单次挥击伤害低于重型武器，因此职业强度来自在敌人挥击之间出刀，以及在开战前布好预备效果。盗贼护甲贴合这种节奏，刺客护甲是同一列表中的下一套。一次成功的首战，是用震撼粉或陷阱之后的一段短促交手解决一只怪物，而生命几乎未损。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次双持 | 两把快速武器，最好一把匕首配一把镰刀，以及食物。 | 合成铁匕首，再配任意第二把快速武器。确认两只手都握有武器，再依赖副手。 |
| 中期起步：盗贼手册 | 周围有书架的法术绑定台、盗贼手册，以及学习费用。 | 绑定并装备手册。进战前先设好一个预备效果，而不是挥击到一半再施法。 |
| 中期：护甲 | 盗贼护甲，或更强的刺客护甲。 | 先凑齐一套。更换套装前，先比较武器的攻击速度与伤害。 |
| 后期：下界合金 | 下界合金材料、锻造模板，以及刺客护甲部件。 | 升级刺客套装，并为群战保留一个陷阱或脱身招式。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 切割 | 预备效果 |
| 眩晕粉 | 范围 |
| 暗影步 | 瞄准目标 |
| 消失 | 自身效果 |
| 捕熊夹 | 持续范围 |
| 残害 | 近战攻击 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择盗贼法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="rogues:iron_sickle" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 盗贼之路 | <ItemLink id="rogues:iron_dagger" /> |

- [战士](class.warrior.md)

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 匕首专精 | <ItemLink id="rogues:iron_dagger" /> |
| 镰刀专精 | <ItemLink id="rogues:iron_sickle" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@rogues" />

本页列出盗贼使用的匕首与镰刀。选择时比较伤害、攻速与武器招式。

### 武器

| 分类 | 物品 | 定位 |
| --- | --- | --- |
| <ItemLink id="rogues:flint_dagger" /> | <ItemGrid><ItemIcon id="rogues:flint_dagger" /><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="rogues:golden_dagger" /><ItemIcon id="rogues:diamond_dagger" /><ItemIcon id="rogues:netherite_dagger" /></ItemGrid> | 快速武器，适合与另一把快速武器搭配 |
| <ItemLink id="rogues:iron_sickle" /> | <ItemGrid><ItemIcon id="rogues:iron_sickle" /><ItemIcon id="rogues:golden_sickle" /><ItemIcon id="rogues:diamond_sickle" /><ItemIcon id="rogues:netherite_sickle" /></ItemGrid> | 快速武器，适合与另一把快速武器搭配 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="rogues:rogue_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:rogue_armor_head" /><ItemIcon id="rogues:rogue_armor_chest" /><ItemIcon id="rogues:rogue_armor_legs" /><ItemIcon id="rogues:rogue_armor_feet" /></ItemGrid> |
| <ItemLink id="rogues:assassin_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:assassin_armor_head" /><ItemIcon id="rogues:assassin_armor_chest" /><ItemIcon id="rogues:assassin_armor_legs" /><ItemIcon id="rogues:assassin_armor_feet" /></ItemGrid> |
| <ItemLink id="rogues:netherite_assassin_armor_chest" /> | <ItemGrid><ItemIcon id="rogues:netherite_assassin_armor_head" /><ItemIcon id="rogues:netherite_assassin_armor_chest" /><ItemIcon id="rogues:netherite_assassin_armor_legs" /><ItemIcon id="rogues:netherite_assassin_armor_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
