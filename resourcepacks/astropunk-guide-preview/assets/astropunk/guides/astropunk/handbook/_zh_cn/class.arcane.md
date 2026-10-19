---
navigation:
  title: "奥秘法师"
  position: 0
  parent: combat.magic.md
  icon: wizards:wand_arcane
item_ids:
  - wizards:arcane_robe_chest
  - wizards:arcane_robe_feet
  - wizards:arcane_robe_head
  - wizards:arcane_robe_legs
  - wizards:netherite_arcane_robe_chest
  - wizards:netherite_arcane_robe_feet
  - wizards:netherite_arcane_robe_head
  - wizards:netherite_arcane_robe_legs
  - wizards:staff_arcane
  - wizards:staff_netherite_arcane
  - wizards:staff_wizard
  - wizards:wand_arcane
  - wizards:wand_netherite_arcane
  - wizards:wizard_robe_chest
  - wizards:wizard_robe_feet
  - wizards:wizard_robe_head
  - wizards:wizard_robe_legs
---

# 奥秘法师

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Wizards+RPG+Arcane+Wizard+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Wizards+RPG+%E5%A5%A5%E7%A7%98%E6%B3%95%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

奥秘法师使用奥术魔杖与法杖，招式包含投射物、光束、范围攻击与自身效果。

### 入门配装示例

奥术魔杖搭配四件巫师长袍，是一种可合成的入门配装，不是必选或普遍最优的构筑。模型展示外观与手持魔杖，不表示已装备法术书。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"wizards:wizard_robe_feet",count:1},{id:"wizards:wizard_robe_legs",count:1},{id:"wizards:wizard_robe_chest",count:1},{id:"wizards:wizard_robe_head",count:1}],HandItems:[{id:"wizards:wand_arcane",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid>

拥有魔杖并备好其法术所需的符文，即可尝试基础施法。魔杖配方需要紫水晶与金，通用巫师长袍需要羊毛与青金石。职业书是下一步，不是使用魔杖自带基础法术的前提。

以下是可选的准备阶段，不是必经顺序，也不按游玩天数划分。

| 阶段 | 下一步选择 |
| --- | --- |
| 前期：初次施法 | 先制作奥术魔杖，有材料时搭配通用巫师长袍，并查看法术提示中的符文消耗。 |
| 中期起步：职业书施法 | 使用周围有书架的法术绑定台，满足界面显示的学习费用，装备奥术职业书并手持兼容装备。 |
| 中期：专注学派 | 获得末影珍珠后，比较奥术长袍与奥术法杖。按学派属性选择，不要只按名称更换装备。 |
| 后期：下界合金升级 | 备齐模板与材料后查看对应锻造配方。这是装备升级，不代表已经适合挑战首领。 |

### 入门装备

<ItemGrid>
  <ItemIcon id="wizards:wand_arcane" />
</ItemGrid>

<ItemLink id="wizards:wand_arcane" />

<Recipe id="wizards:wand_arcane" />

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 奥秘飞弹 | 投射物 |
| 奥秘爆破 | 范围 |
| 奥秘射线 | 光束 |
| 奥秘弹幕 | 自身效果 |
| 闪现 | 自身效果 |
| 唤起 | 自身效果 |

![使用法杖施展奥术](images/visual-arcane-casting.png)

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

在法术绑定台选择奥秘法师法术书。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，包含对应的招式池。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:staff_arcane" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 奥秘之路 | <ItemLink id="wizards:wand_arcane" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 奥秘权杖专精 | <ItemLink id="wizards:staff_arcane" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@wizards" />

奥术魔杖与法杖提供对应的法术强度。通用巫师法杖兼顾奥术、火焰与冰霜，选择法器时先比较学派加成。

### 武器

| 分类 | 物品 | 学派加成 |
| --- | --- | --- |
| <ItemLink id="wizards:wand_arcane" /> | <ItemGrid><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:wand_netherite_arcane" /></ItemGrid> | 奥术强度 |
| <ItemLink id="wizards:staff_wizard" /> | <ItemGrid><ItemIcon id="wizards:staff_wizard" /></ItemGrid> | 奥术、火焰与冰霜强度 |
| <ItemLink id="wizards:staff_arcane" /> | <ItemGrid><ItemIcon id="wizards:staff_arcane" /><ItemIcon id="wizards:staff_netherite_arcane" /></ItemGrid> | 奥术强度 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="wizards:wizard_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:arcane_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:arcane_robe_head" /><ItemIcon id="wizards:arcane_robe_chest" /><ItemIcon id="wizards:arcane_robe_legs" /><ItemIcon id="wizards:arcane_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:netherite_arcane_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:netherite_arcane_robe_head" /><ItemIcon id="wizards:netherite_arcane_robe_chest" /><ItemIcon id="wizards:netherite_arcane_robe_legs" /><ItemIcon id="wizards:netherite_arcane_robe_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
