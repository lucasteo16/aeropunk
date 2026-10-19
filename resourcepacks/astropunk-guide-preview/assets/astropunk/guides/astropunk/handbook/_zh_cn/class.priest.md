---
navigation:
  title: "牧师"
  position: 6
  parent: combat.magic.md
  icon: paladins:holy_wand
item_ids:
  - paladins:acolyte_wand
  - paladins:diamond_holy_staff
  - paladins:diamond_holy_wand
  - paladins:holy_staff
  - paladins:holy_wand
  - paladins:netherite_holy_staff
  - paladins:netherite_holy_wand
  - paladins:netherite_prior_robe_chest
  - paladins:netherite_prior_robe_feet
  - paladins:netherite_prior_robe_head
  - paladins:netherite_prior_robe_legs
  - paladins:priest_robe_chest
  - paladins:priest_robe_feet
  - paladins:priest_robe_head
  - paladins:priest_robe_legs
  - paladins:prior_robe_chest
  - paladins:prior_robe_feet
  - paladins:prior_robe_head
  - paladins:prior_robe_legs
---

# 牧师

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Paladins+and+Priests+Priest+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Paladins+and+Priests+%E7%89%A7%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

牧师使用圣光魔杖与法杖，招式包含治疗、光束与保护。

![神圣施法效果](images/visual-holy-casting.png)

### 入门配装示例

侍僧魔杖搭配四件牧师长袍，是一种入门配装示例，不是官方默认配置。模型展示外观与手持魔杖，不表示已装备法术书。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"paladins:priest_robe_feet",count:1},{id:"paladins:priest_robe_legs",count:1},{id:"paladins:priest_robe_chest",count:1},{id:"paladins:priest_robe_head",count:1}],HandItems:[{id:"paladins:acolyte_wand",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="paladins:acolyte_wand" /><ItemIcon id="paladins:priest_robe_head" /><ItemIcon id="paladins:priest_robe_chest" /><ItemIcon id="paladins:priest_robe_legs" /><ItemIcon id="paladins:priest_robe_feet" /></ItemGrid>

### 值得关注的内容

治疗法术按治疗强度计算。侍僧魔杖提供治疗强度，配方只要木棍与线，因此第一次治疗不必等金锭。圣光魔杖与圣光法杖是同一条线上更晚的步骤，发行方也为牧师职业书推荐圣光法杖与魔杖。

牧师长袍用锁链与羊毛，成本低且在早期就能做。司铎长袍每件需要金锭与恶魂之泪，因此要等一次下界行程。下界合金司铎长袍是它的锻造升级。发行方说明圣光装备同时提升法术伤害与治疗，因此要看完整提示，而不只是一行。

牧师辅助别人，所以真正有用的问题是身边站着谁。治疗之环与光泉是范围与自身效果，团战比单挑更能发挥这个职业。苦修与圣光是针对单个目标的直接选项。

符文在这里比近战职业更重要，因为几乎每个动作都要消耗弹药。把每条法术指定的符文带在身上，为应急治疗留一组，进入战斗前检查符文袋，而不是打起来才看。

一次成功的初次使用是这样的。手持侍僧魔杖，对受伤的盟友施放快速治疗，看生命值上升、符文减少。然后在战斗前对自己施放屏障并确认保护出现。如果治疗成功而屏障失败，就比较两条法术各自指定的符文。

### 准备阶段

下面的提示是可选的。一个阶段只要还有用，就可以一直停留。

| 阶段 | 就绪条件 | 下一步选择 |
| --- | --- | --- |
| 前期 | 有木棍、线，以及魔杖法术指定的符文。 | 做出侍僧魔杖，治疗一位盟友并施放一次保护法术。 |
| 中期起步 | 能走到周围有书架的法术绑定台，并付得起费用。 | 绑定牧师职业书，手持兼容法器时装备它。 |
| 中期 | 能取得锁链、羊毛、金锭与恶魂之泪。 | 比较牧师长袍与司铎长袍，并判断圣光魔杖或圣光法杖更贴合你的施法距离。 |
| 后期 | 持有下界合金升级锻造模板与下界合金锭。 | 每次升级一件司铎长袍部件，并为治疗与保护都留足符文。 |

### 入门装备

<ItemGrid><ItemIcon id="paladins:acolyte_wand" /></ItemGrid>

<ItemLink id="paladins:acolyte_wand" />

<Recipe id="paladins:acolyte_wand" />

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 圣光 | 光束 |
| 治疗之环 | 范围 |
| 屏障 | 自身效果 |
| 光泉 | 自身效果 |
| 漂浮 | 自身效果 |
| 苦修 | 投射物 |

侍僧魔杖是圣光魔杖之前成本更低的治疗入门。

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

牧师法术书使用 <ItemLink id="spell_engine:spell_book" />，并带有对应的招式池。在法术绑定台选择职业书。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="paladins:holy_wand" /><ItemIcon id="paladins:holy_staff" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 圣光之路 | <ItemLink id="paladins:holy_wand" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 圣光法杖专精 | <ItemLink id="paladins:holy_staff" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@paladins" />

钉锤、巨锤、巨剑与盾牌支持近战。圣光魔杖与法杖支持治疗法术。护甲同时提供防护与职业属性。

### 武器

| 分类 | 物品 | 学派加成或定位 |
| --- | --- | --- |
| 圣光魔杖 | <ItemGrid><ItemIcon id="paladins:acolyte_wand" /><ItemIcon id="paladins:holy_wand" /><ItemIcon id="paladins:diamond_holy_wand" /><ItemIcon id="paladins:netherite_holy_wand" /></ItemGrid> | 治疗强度 |
| 圣光法杖 | <ItemGrid><ItemIcon id="paladins:holy_staff" /><ItemIcon id="paladins:diamond_holy_staff" /><ItemIcon id="paladins:netherite_holy_staff" /></ItemGrid> | 治疗强度 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="paladins:priest_robe_chest" /> | <ItemGrid><ItemIcon id="paladins:priest_robe_head" /><ItemIcon id="paladins:priest_robe_chest" /><ItemIcon id="paladins:priest_robe_legs" /><ItemIcon id="paladins:priest_robe_feet" /></ItemGrid> |
| <ItemLink id="paladins:prior_robe_chest" /> | <ItemGrid><ItemIcon id="paladins:prior_robe_head" /><ItemIcon id="paladins:prior_robe_chest" /><ItemIcon id="paladins:prior_robe_legs" /><ItemIcon id="paladins:prior_robe_feet" /></ItemGrid> |
| <ItemLink id="paladins:netherite_prior_robe_chest" /> | <ItemGrid><ItemIcon id="paladins:netherite_prior_robe_head" /><ItemIcon id="paladins:netherite_prior_robe_chest" /><ItemIcon id="paladins:netherite_prior_robe_legs" /><ItemIcon id="paladins:netherite_prior_robe_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
