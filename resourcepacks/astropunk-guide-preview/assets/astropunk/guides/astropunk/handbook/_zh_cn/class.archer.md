---
navigation:
  title: "弓箭手"
  position: 4
  parent: combat.martial.md
  icon: archers:composite_longbow
item_ids:
  - archers:archer_armor_chest
  - archers:archer_armor_feet
  - archers:archer_armor_head
  - archers:archer_armor_legs
  - archers:composite_longbow
  - archers:diamond_spear
  - archers:flint_spear
  - archers:golden_spear
  - archers:heavy_crossbow
  - archers:iron_spear
  - archers:mechanic_shortbow
  - archers:netherite_heavy_crossbow
  - archers:netherite_longbow
  - archers:netherite_ranger_armor_chest
  - archers:netherite_ranger_armor_feet
  - archers:netherite_ranger_armor_head
  - archers:netherite_ranger_armor_legs
  - archers:netherite_rapid_crossbow
  - archers:netherite_shortbow
  - archers:netherite_spear
  - archers:ranger_armor_chest
  - archers:ranger_armor_feet
  - archers:ranger_armor_head
  - archers:ranger_armor_legs
  - archers:rapid_crossbow
  - archers:royal_longbow
---

# 弓箭手

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Archers+RPG+Archer+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Archers+RPG+%E5%BC%93%E7%AE%AD%E6%89%8B+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

弓箭手使用弓与弩远程作战，长矛提供近战选择，招式包含蓄势射击、范围攻击与伙伴效果。

![携带远程装备的弓箭手](images/visual-archer-equipment.png)

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

弓箭手招式可以配合任意手持的弓或弩，伤害来自远程武器与弹药，而不是另一项法术属性。长弓适合从容蓄力，短弓适合移动中快速出手，弩则有自己的装填节奏。弓箭手与游侠护甲提供远程加成，替换已有套装前先看清单件说明。一次成功的首战，是在骷髅或僵尸靠近之前将其击倒，用掉一个招式而箭矢还有余量。

下列阶段均为可选，说明手头需要什么、每一步解锁什么，不按游玩天数衡量。

| 阶段 | 就绪条件 | 建议行动或下一步选择 |
| --- | --- | --- |
| 前期：初次射击 | 一把弓或弩、一组箭或弩箭，以及补回失误消耗的食物。 | 材料齐备时先做复合长弓，否则用原版弓练习。弓箭手招式两者都能配合。 |
| 中期起步：弓术手册 | 周围有书架的法术绑定台、弓术手册，以及界面显示的学习费用。 | 绑定并装备手册，手中保持远程武器。村庄的箭术靶场是获取入门装备的地点之一。 |
| 中期：护甲 | 两件以上弓箭手或游侠护甲，可自行合成或购买，并有足够等级维修。 | 比较手中部件的悬停属性。游侠护甲的加成与你选定的武器分类相符时再更换。 |
| 后期：下界合金 | 下界合金锭、配方向导模板要求的锻造模板，以及待升级的游侠护甲部件。 | 优先升级你最常穿的位置。地牢战利品也会出现弓术装备，花材料前先看看捡到的弓。 |

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 强劲射击 | 预备效果 |
| 纠缠根须 | 持续范围 |
| 连箭射击 | 射箭 |
| 剑雨 | 落下攻击 |
| 魔法箭 | 投射物 |
| 灵魂狼群 | 自身效果 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择弓箭手法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="archers:composite_longbow" /><ItemIcon id="minecraft:bow" /><ItemIcon id="archers:iron_spear" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 弓箭手之路 | <ItemLink id="archers:composite_longbow" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 弓专精 | <ItemLink id="minecraft:bow" /> |
| 长矛专精 | <ItemLink id="archers:iron_spear" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@archers" />

长弓、短弓与弩在蓄力速度和射击伤害之间取舍。长矛提供近战选择，弓箭手与游侠护甲提供远程属性。

### 武器

| 分类 | 物品 | 定位 |
| --- | --- | --- |
| <ItemLink id="archers:flint_spear" /> | <ItemGrid><ItemIcon id="archers:flint_spear" /><ItemIcon id="archers:iron_spear" /><ItemIcon id="archers:golden_spear" /><ItemIcon id="archers:diamond_spear" /><ItemIcon id="archers:netherite_spear" /></ItemGrid> | 近战备选，怪物贴近时使用 |
| <ItemLink id="archers:composite_longbow" /> | <ItemGrid><ItemIcon id="archers:composite_longbow" /><ItemIcon id="archers:royal_longbow" /><ItemIcon id="archers:netherite_longbow" /></ItemGrid> | 远程，蓄力较久，适合稳定出手 |
| <ItemLink id="archers:mechanic_shortbow" /> | <ItemGrid><ItemIcon id="archers:mechanic_shortbow" /><ItemIcon id="archers:netherite_shortbow" /></ItemGrid> | 远程，蓄力较快，适合边移动边射 |
| <ItemLink id="archers:rapid_crossbow" /> | <ItemGrid><ItemIcon id="archers:rapid_crossbow" /><ItemIcon id="archers:heavy_crossbow" /><ItemIcon id="archers:netherite_rapid_crossbow" /><ItemIcon id="archers:netherite_heavy_crossbow" /></ItemGrid> | 远程，装填后由你决定发射时机 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="archers:archer_armor_chest" /> | <ItemGrid><ItemIcon id="archers:archer_armor_head" /><ItemIcon id="archers:archer_armor_chest" /><ItemIcon id="archers:archer_armor_legs" /><ItemIcon id="archers:archer_armor_feet" /></ItemGrid> |
| <ItemLink id="archers:ranger_armor_chest" /> | <ItemGrid><ItemIcon id="archers:ranger_armor_head" /><ItemIcon id="archers:ranger_armor_chest" /><ItemIcon id="archers:ranger_armor_legs" /><ItemIcon id="archers:ranger_armor_feet" /></ItemGrid> |
| <ItemLink id="archers:netherite_ranger_armor_chest" /> | <ItemGrid><ItemIcon id="archers:netherite_ranger_armor_head" /><ItemIcon id="archers:netherite_ranger_armor_chest" /><ItemIcon id="archers:netherite_ranger_armor_legs" /><ItemIcon id="archers:netherite_ranger_armor_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
