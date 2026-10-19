---
navigation:
  title: "火焰法师"
  position: 1
  parent: combat.magic.md
  icon: wizards:wand_fire
item_ids:
  - wizards:fire_robe_chest
  - wizards:fire_robe_feet
  - wizards:fire_robe_head
  - wizards:fire_robe_legs
  - wizards:netherite_fire_robe_chest
  - wizards:netherite_fire_robe_feet
  - wizards:netherite_fire_robe_head
  - wizards:netherite_fire_robe_legs
  - wizards:staff_fire
  - wizards:staff_netherite_fire
  - wizards:wand_fire
  - wizards:wand_netherite_fire
  - wizards:wand_novice
---

# 火焰法师

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Wizards+RPG+Fire+Wizard+abilities+equipment+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Wizards+RPG+%E7%81%AB%E7%84%B0%E6%B3%95%E5%B8%88+%E6%8A%80%E8%83%BD+%E8%A3%85%E5%A4%87+%E6%95%99%E7%A8%8B+%E4%B8%AD%E6%96%87)

## 定位与入门武器

火焰法师使用火焰魔杖与法杖，招式包含近距范围攻击、投射物与下落攻击。

![火焰法术效果](images/visual-fire-magic.png)

### 入门配装示例

新手魔杖搭配四件通用巫师长袍，是一种入门配装示例，不是官方默认配置。模型展示外观与手持魔杖，不表示已装备法术书。

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Entity id="minecraft:armor_stand" x="0.5" y="0" z="0.5" rotationY="180" data='{NoGravity:1b,Invulnerable:1b,ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"wizards:wizard_robe_feet",count:1},{id:"wizards:wizard_robe_legs",count:1},{id:"wizards:wizard_robe_chest",count:1},{id:"wizards:wizard_robe_head",count:1}],HandItems:[{id:"wizards:wand_novice",count:1},{}]}' />
</GameScene>

<ItemGrid><ItemIcon id="wizards:wand_novice" /><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid>

### 值得关注的内容

火焰法术按火焰强度计算。新手魔杖只提供火焰强度，手持时不会增强奥术或冰霜法术。围绕法器绑定职业书之前，先读清它的学派词条。

通用巫师法杖同时提供奥术、火焰与冰霜强度，适合经常更换职业书的玩家。长期主修火焰时，火焰魔杖或火焰法杖更专注。手持法器自带武器法术，因此在拥有职业书之前就能造成伤害。

通用巫师长袍只需要羊毛与青金石，不必进入下界。火焰长袍每件都需要烈焰粉，所以这套装备要先去下界。下界合金火焰长袍是把对应的火焰长袍部件锻造升级，不是另外制作一件。

符文既是武器法术的弹药，也是已学法术的弹药。把准备施放的法术所指定的符文带在身上，可以散放在背包，也可以装进已装备的符文袋，并在提示中查看消耗。

一次成功的初次使用是这样的。手持新手魔杖，瞄准一个敌对生物，施放魔杖法术，符文数量按提示减少，目标受到火焰伤害。如果毫无反应，先核对符文类型与袋中内容，再考虑换掉魔杖。

### 准备阶段

以下检查点都是可选建议。每行给出一个可以满足的条件，而不是必须走完的章节。

| 阶段 | 就绪条件 | 下一步选择 |
| --- | --- | --- |
| 前期 | 能用煤炭与木棍做出新手魔杖，并持有其法术指定的符文。 | 先对单个目标施放一次。有羊毛与青金石时补上通用巫师长袍。 |
| 中期起步 | 拥有周围有书架的法术绑定台，并付得起界面显示的学习费用。 | 绑定火焰职业书，手持兼容法器时装备该职业书。 |
| 中期 | 能取得烈焰粉，来自下界或交易。 | 比较火焰长袍与火焰法杖。按学派加成判断每件装备，而不是只看名称。 |
| 后期 | 持有下界合金升级锻造模板与下界合金锭。 | 每次升级一件火焰长袍部件。这是装备步骤，不代表已经适合挑战首领。 |

### 入门装备

<ItemGrid><ItemIcon id="wizards:wand_novice" /></ItemGrid>

<ItemLink id="wizards:wand_novice" />

<Recipe id="wizards:wand_novice" />

### 书中招式

| 能力 | 形式 |
| --- | --- |
| 火焰吐息 | 范围 |
| 烈焰斩击 | 投射物 |
| 陨石 | 下落攻击 |
| 火焰风暴 | 范围 |
| 火墙 | 持续范围 |
| 火焰九头蛇 | 自身效果 |

***

## 职业法术书
<ItemGrid><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

火焰法术书使用 <ItemLink id="spell_engine:spell_book" />，并带有对应的招式池。在法术绑定台选择职业书。

- [绑定与施法](combat.abilities.md) 职业书制作、费用、装备槽位与施法操作。
- [符文与武器法术](combat.magic.md) 施法资源与装备自带法术。

***

## 职业技能
<ItemGrid><ItemIcon id="wizards:wand_fire" /><ItemIcon id="wizards:staff_fire" /></ItemGrid>

按 <KeyBind id="key.puffish_skills.open" /> 查找下列职业路线与武器路线。

| 路线 | 相关装备 |
| --- | --- |
| 火焰之路 | <ItemLink id="wizards:wand_fire" /> |

### 武器路线

| 路线 | 相关装备 |
| --- | --- |
| 火焰法杖专精 | <ItemLink id="wizards:staff_fire" /> |

- [技能成长](combat.skills.md) 点数分类、相连节点、互斥路线与重置。更换装备不会返还点数。

***

## 武器与护甲

<EmiSearch query="@wizards" />

火焰魔杖与法杖提供本学派的法术强度。通用巫师法杖兼顾奥术、火焰与冰霜，选择法器前先比较学派加成。

### 武器

| 分类 | 物品 | 学派加成或定位 |
| --- | --- | --- |
| 火焰魔杖 | <ItemGrid><ItemIcon id="wizards:wand_novice" /><ItemIcon id="wizards:wand_fire" /><ItemIcon id="wizards:wand_netherite_fire" /></ItemGrid> | 火焰强度 |
| 通用法杖 | <ItemGrid><ItemIcon id="wizards:staff_wizard" /></ItemGrid> | 奥术、火焰与冰霜强度 |
| 火焰法杖 | <ItemGrid><ItemIcon id="wizards:staff_fire" /><ItemIcon id="wizards:staff_netherite_fire" /></ItemGrid> | 火焰强度 |

### 护甲套装

| 套装参考，以胸甲名称标识 | 部件，依次为头、胸、腿、足 |
| --- | --- |
| <ItemLink id="wizards:wizard_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:wizard_robe_head" /><ItemIcon id="wizards:wizard_robe_chest" /><ItemIcon id="wizards:wizard_robe_legs" /><ItemIcon id="wizards:wizard_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:fire_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:fire_robe_head" /><ItemIcon id="wizards:fire_robe_chest" /><ItemIcon id="wizards:fire_robe_legs" /><ItemIcon id="wizards:fire_robe_feet" /></ItemGrid> |
| <ItemLink id="wizards:netherite_fire_robe_chest" /> | <ItemGrid><ItemIcon id="wizards:netherite_fire_robe_head" /><ItemIcon id="wizards:netherite_fire_robe_chest" /><ItemIcon id="wizards:netherite_fire_robe_legs" /><ItemIcon id="wizards:netherite_fire_robe_feet" /></ItemGrid> |

***

## 通用装备

<ItemGrid><ItemIcon id="minecraft:iron_sword" /><ItemIcon id="minecraft:iron_chestplate" /><ItemIcon id="jewelry:copper_ring" /></ItemGrid>- [武器与护甲](equipment.weapons-armor.md)
- [饰品](equipment.accessories.md)
- [战斗操作](combat.handling.md)
