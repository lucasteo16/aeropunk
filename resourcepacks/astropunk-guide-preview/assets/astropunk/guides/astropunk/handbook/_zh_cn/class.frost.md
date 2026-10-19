---
navigation:
  title: "冰霜法师"
  position: 2
  parent: combat.magic.md
  icon: wizards:wand_frost
item_ids:
  - wizards:frost_robe_chest
  - wizards:frost_robe_feet
  - wizards:frost_robe_head
  - wizards:frost_robe_legs
  - wizards:netherite_frost_robe_chest
  - wizards:netherite_frost_robe_feet
  - wizards:netherite_frost_robe_head
  - wizards:netherite_frost_robe_legs
  - wizards:staff_frost
  - wizards:staff_netherite_frost
  - wizards:wand_frost
  - wizards:wand_netherite_frost
---

# 冰霜法师

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Wizards+RPG+Frost+Wizard+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Wizards+RPG+%E5%86%B0%E9%9C%9C%E6%B3%95%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

冰霜法师使用冰霜魔杖与法杖，招式包含范围攻击、保护与投射物。

![冰霜法术效果](images/visual-frost-magic.png)

### 值得关注的内容

冰霜法术按冰霜强度计算。冰霜魔杖只提供冰霜强度，通用巫师法杖同时提供奥术、火焰与冰霜强度，因此魔杖更适合专修。绑定职业书之前，先读清学派词条。

冰霜魔杖的配方需要铁锭与雪球，是本模组里成本较低的学派法器之一。冰霜法杖还需要海晶砂粒，因此要等一次海洋行程。法杖自带的武器法术强于魔杖，消耗写在提示里。

通用巫师长袍用羊毛与青金石就能覆盖任何学派。冰霜长袍每件需要海晶碎片，与法杖一样要等海洋行程。下界合金冰霜长袍是把对应的冰霜长袍部件锻造升级。

霜盾在职业书中是自身效果，因此冰霜构筑可以守住位置，让范围法术持续落下。把法术指定的符文带在身上，放在背包或已装备的符文袋中，并留出一次护盾的用量与一次攻击的用量。

一次成功的初次使用是这样的。手持冰霜魔杖，把两三个敌对生物聚到面前，施放魔杖法术，符文减少，范围内的目标都有反应。如果只有一个目标有反应，说明这是瞄准型法术而不是范围法术，提示里会写明。

### 准备阶段

下面顺序是可选的。每行描述一个条件，不是必须完成的章节。

| 阶段 | 就绪条件 | 下一步选择 |
| --- | --- | --- |
| 前期 | 有铁锭、雪球，以及魔杖法术指定的符文。 | 做出冰霜魔杖，对一个敌对生物施放一次。 |
| 中期起步 | 能使用周围有书架的法术绑定台，并付得起显示的费用。 | 绑定冰霜职业书，手持兼容法器时装备它。 |
| 中期 | 一次海洋行程带回了海晶碎片与海晶砂粒。 | 比较冰霜长袍与冰霜法杖。如果专精部件的学派加成帮不到你的法术，就继续用通用长袍。 |
| 后期 | 持有下界合金升级锻造模板与下界合金锭。 | 每次升级一件冰霜长袍部件，再把结果与被替换的部件比较。 |

### 入门配装示例

入门配装示例：职业入门武器搭配目录中的第一套护甲。这是一种可合成选择，并非官方或最优构筑。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"wizards:wizard_robe_feet",count:1},{id:"wizards:wizard_robe_legs",count:1},{id:"wizards:wizard_robe_chest",count:1},{id:"wizards:wizard_robe_head",count:1}],HandItems:[{id:"wizards:wand_frost",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="wizards:wand_frost" /><ItemIcon id="wizards:wizard_robe_feet" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_head" /></ItemGrid>

### 入门装备

<ItemGrid><ItemIcon id="wizards:wand_frost" /></ItemGrid>

<ItemLink id="wizards:wand_frost" />

<Recipe id="wizards:wand_frost" />

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 冰霜新星 | 范围 |
| 冰霜尖刺 | 持续范围 |
| 霜盾 | 自身效果 |
| 冰枪 | 投射物 |
| 暴风雪 | 下落攻击 |
| 冰霜元素 | 自身效果 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

冰霜法术书使用 <ItemLink id="spell_engine:spell_book" />，并带有对应的招式池。在法术绑定台选择职业书。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="wizards:wand_frost" /><ItemIcon id="wizards:staff_frost" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 冰霜之路 | <ItemLink id="wizards:wand_frost" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 冰霜法杖专精 | <ItemLink id="wizards:staff_frost" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@wizards" />

冰霜魔杖与法杖提供本学派的法术强度。通用巫师法杖兼顾奥术、火焰与冰霜，选择法器前先比较学派加成。

### 武器

| 分类 | 物品 | 学派加成或定位 |
| --- | --- | --- |
| 冰霜魔杖 | <ItemGrid><ItemIcon id="wizards:wand_frost" /><ItemIcon id="wizards:wand_netherite_frost" /></ItemGrid> | 冰霜强度 |
| 通用法杖 | <ItemGrid><ItemIcon id="wizards:staff_wizard" /></ItemGrid> | 奥术、火焰与冰霜强度 |
| 冰霜法杖 | <ItemGrid><ItemIcon id="wizards:staff_frost" /><ItemIcon id="wizards:staff_netherite_frost" /></ItemGrid> | 冰霜强度 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="wizards:wizard_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:frost_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:frost_robe_head" /><ItemIcon id="wizards:frost_robe_chest" /><ItemIcon id="wizards:frost_robe_legs" /><ItemIcon id="wizards:frost_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:netherite_frost_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:netherite_frost_robe_head" /><ItemIcon id="wizards:netherite_frost_robe_chest" /><ItemIcon id="wizards:netherite_frost_robe_legs" /><ItemIcon id="wizards:netherite_frost_robe_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
