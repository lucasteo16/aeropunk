---
navigation:
  title: "土系法师"
  position: 4
  parent: combat.magic.md
  icon: elemental_wizards_rpg:wand_terra
item_ids:
  - elemental_wizards_rpg:dripstone_chest
  - elemental_wizards_rpg:dripstone_feet
  - elemental_wizards_rpg:dripstone_head
  - elemental_wizards_rpg:dripstone_legs
  - elemental_wizards_rpg:mountain_robe_chest
  - elemental_wizards_rpg:mountain_robe_feet
  - elemental_wizards_rpg:mountain_robe_head
  - elemental_wizards_rpg:mountain_robe_legs
  - elemental_wizards_rpg:netherite_dripstone_chest
  - elemental_wizards_rpg:netherite_dripstone_feet
  - elemental_wizards_rpg:netherite_dripstone_head
  - elemental_wizards_rpg:netherite_dripstone_legs
  - elemental_wizards_rpg:staff_netherite_terra
  - elemental_wizards_rpg:staff_terra
  - elemental_wizards_rpg:wand_clay
  - elemental_wizards_rpg:wand_netherite_terra
  - elemental_wizards_rpg:wand_terra
---

# 土系法师

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Elemental+Wizards+RPG+Terra+Wizard+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Elemental+Wizards+RPG+%E5%9C%9F%E7%B3%BB%E6%B3%95%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

土系法师使用土魔杖与法杖，招式包含保护、瞄准攻击与地面效果。

![元素法师长袍](images/visual-elemental-robes.png)

### 值得关注的内容

土系法术按土强度计算。黏土魔杖提供土强度，配方只要黏土球与木棍，因此第一件法器不需要先挖矿。绑定职业书之前，先读清学派词条。

职业书里的土系招式分成保护与瞄准两类。石肤与土魔像是防御选项，穿刺与土之环需要目标。两类都会用到的构筑，符文要备足两种用途。

土魔杖与土法杖是专精升级，法杖还要用到粗铁。元素法杖同时提供风、土与水强度，但需要下界之星，因此属于后期目标。

滴水石长袍用尖滴水石与羊毛支撑本学派，胸甲额外需要滴水石块。山岳长袍是更晚的升级，配方使用史诗护甲升级与监守者升级水晶。元素长袍覆盖三种元素学派。

一次成功的初次使用是这样的。手持黏土魔杖，对一个瞄准目标施放并确认命中，然后在战斗开始前施放石肤，确认保护已经生效。如果护甲数值没有变化，说明法术没有施放，符文也就没有消耗。

### 准备阶段

下面的提示是可选的。每个阶段描述你已经具备的能力，而不是游玩了多久。

| 阶段 | 就绪条件 | 下一步选择 |
| --- | --- | --- |
| 前期 | 有黏土、木棍，以及魔杖法术指定的符文。 | 做出黏土魔杖并施放一次。羊毛有余时补上元素长袍部件。 |
| 中期起步 | 能走到周围有书架的法术绑定台，并付得起费用。 | 绑定土系职业书，手持兼容法器时装备它。 |
| 中期 | 能取得尖滴水石，并能比较土魔杖与土法杖。 | 按每件装备的学派加成，在滴水石长袍路线与通用长袍之间选择。 |
| 后期 | 能获得一次史诗护甲升级或下界之星。 | 把山岳长袍与元素法杖当作两个独立目标，并且每次只升级一件。 |

### 入门配装示例

入门配装示例：职业入门武器搭配目录中的第一套护甲。这是一种可合成选择，并非官方或最优构筑。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"elemental_wizards_rpg:elemental_feet",count:1},{id:"elemental_wizards_rpg:elemental_legs",count:1},{id:"elemental_wizards_rpg:elemental_chest",count:1},{id:"elemental_wizards_rpg:elemental_head",count:1}],HandItems:[{id:"elemental_wizards_rpg:wand_clay",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_clay" /><ItemIcon id="elemental_wizards_rpg:elemental_feet" /><ItemIcon id="elemental_wizards_rpg:elemental_legs" /><ItemIcon id="elemental_wizards_rpg:elemental_chest" /><ItemIcon id="elemental_wizards_rpg:elemental_head" /></ItemGrid>

### 入门装备

<ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_clay" /></ItemGrid>

<ItemLink id="elemental_wizards_rpg:wand_clay" />

<Recipe id="elemental_wizards_rpg:wand_clay" />

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 石肤 | 范围 |
| 穿刺 | 瞄准目标 |
| 土之环 | 瞄准目标 |
| 碎石 | 投射物 |
| 地震 | 自身效果 |
| 土魔像 | 自身效果 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

土系法术书使用 <ItemLink id="spell_engine:spell_book" />，并带有对应的招式池。在法术绑定台选择职业书。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_terra" /><ItemIcon id="elemental_wizards_rpg:staff_terra" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 大地之路 | <ItemLink id="elemental_wizards_rpg:wand_terra" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 强化石矛 | <ItemLink id="elemental_wizards_rpg:staff_terra" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@elemental_wizards_rpg" />

土系法器提供对应的法术强度。列表中的共享元素法杖兼顾风、土与水。选择前把它们的完整属性与专精法器比较。

### 武器

| 分类 | 物品 | 学派加成或定位 |
| --- | --- | --- |
| 土魔杖 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:wand_clay" /><ItemIcon id="elemental_wizards_rpg:wand_terra" /><ItemIcon id="elemental_wizards_rpg:wand_netherite_terra" /></ItemGrid> | 土强度 |
| 元素法杖 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:staff_elemental" /></ItemGrid> | 风、土与水强度 |
| 土法杖 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:staff_terra" /><ItemIcon id="elemental_wizards_rpg:staff_netherite_terra" /></ItemGrid> | 土强度 |
| 独特法杖 | <ItemGrid><ItemIcon id="elemental_wizards_rpg:unique_staff_1" /></ItemGrid> | 土、水与风强度 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="elemental_wizards_rpg:elemental_chest" /> | <ItemGrid><ItemIcon id="elemental_wizards_rpg:elemental_head" /><ItemIcon id="elemental_wizards_rpg:elemental_chest" /><ItemIcon id="elemental_wizards_rpg:elemental_legs" /><ItemIcon id="elemental_wizards_rpg:elemental_feet" /></ItemGrid> |
| <ItemLink id="elemental_wizards_rpg:dripstone_chest" /> | <ItemGrid><ItemIcon id="elemental_wizards_rpg:dripstone_head" /><ItemIcon id="elemental_wizards_rpg:dripstone_chest" /><ItemIcon id="elemental_wizards_rpg:dripstone_legs" /><ItemIcon id="elemental_wizards_rpg:dripstone_feet" /></ItemGrid> |
| <ItemLink id="elemental_wizards_rpg:netherite_dripstone_chest" /> | <ItemGrid><ItemIcon id="elemental_wizards_rpg:netherite_dripstone_head" /><ItemIcon id="elemental_wizards_rpg:netherite_dripstone_chest" /><ItemIcon id="elemental_wizards_rpg:netherite_dripstone_legs" /><ItemIcon id="elemental_wizards_rpg:netherite_dripstone_feet" /></ItemGrid> |
| <ItemLink id="elemental_wizards_rpg:mountain_robe_chest" /> | <ItemGrid><ItemIcon id="elemental_wizards_rpg:mountain_robe_head" /><ItemIcon id="elemental_wizards_rpg:mountain_robe_chest" /><ItemIcon id="elemental_wizards_rpg:mountain_robe_legs" /><ItemIcon id="elemental_wizards_rpg:mountain_robe_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
