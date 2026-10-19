---
navigation:
  title: "技能成长"
  position: 8
  parent: reference.skills.md
  icon: minecraft:experience_bottle
---

# 技能成长

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Pufferfish+Skills+RPG+Series+Skill+Tree+class+weapon+points+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Pufferfish+Skills+RPG+Series+%E6%8A%80%E8%83%BD%E6%A0%91+%E8%81%8C%E4%B8%9A+%E6%AD%A6%E5%99%A8+%E6%8A%80%E8%83%BD%E7%82%B9+%E6%95%99%E7%A8%8B)

## 技能成长

![相互连接的职业技能路线](images/visual-class-skill-tree.png)

按 <KeyBind id="key.puffish_skills.open" /> 打开技能界面。Pufferfish’s Skills 提供界面与成长系统，Skill Tree 和 More RPG Classes Skill Tree 提供职业及武器分支。

击杀按自带定义获得技能树经验，并设有防刷限制与附近队友分享。投入点数前先看清相连节点的要求。职业点数、武器点数与普通经验等级是三种不同资源，只有前两种用于购买技能节点。

1. 先试用职业武器与招式，再打开职业技能分类阅读根节点，然后投入职业点。互斥根节点让你不能叠加所有职业路线。
2. 另行打开武器技能分类，把武器点投入实际使用武器对应的分支。职业选择与武器分支相互配合，但不是同一次购买。
3. 选好法术强化节点后，仍要装备对应书籍或武器并使用所指招式。被动节点则需满足其说明的触发条件。

奥术职业强化影响职业书法术，法杖分支发展的则是法杖本身。购买其中一项不会自动获得另一项，也不会绑定尚未学会的法术。

***

## 职业路线

<ItemGrid><ItemIcon id="archers:composite_longbow" /><ItemIcon id="rogues:iron_dagger" /><ItemIcon id="wizards:wand_arcane" /><ItemIcon id="wizards:wand_frost" /><ItemIcon id="paladins:iron_mace" /><ItemIcon id="bards_rpg:wooden_lute" /></ItemGrid>

| 玩法类型 | 职业路线 |
| --- | --- |
| 远程射击 | 弓箭手之路 [弓箭手](class.archer.md)、神射手 [神射手](class.deadeye.md)、冻原猎手 [冻原猎手](class.tundra-hunter.md)、战争弓手 [战争弓手](class.war-archer.md) |
| 近战 | 战士之路 [战士](class.warrior.md)、圣骑士之路 [圣骑士](class.paladin.md)、盗贼之路 [盗贼](class.rogue.md)、狂战士 [狂战士](class.berserker.md)、猎魔人剑术与法印 [猎魔人](class.witcher.md) |
| 奥术 | 奥秘之路 [奥术法师](class.arcane.md)、气功师 [气功师](class.forcemaster.md) |
| 元素法师 | 火焰之路 [火焰法师](class.fire.md)、冰霜之路 [冰霜法师](class.frost.md)、风 [风系法师](class.wind.md)、地 [地系法师](class.terra.md)、水 [水系法师](class.aqua.md) |
| 辅助与混合 | 光明之路 [牧师](class.priest.md)、吟游诗人 [吟游诗人](class.bard.md) |

***

## 武器成长
<ItemGrid><ItemIcon id="wizards:staff_arcane" /><ItemIcon id="wizards:staff_fire" /><ItemIcon id="wizards:staff_frost" /><ItemIcon id="paladins:holy_staff" /><ItemIcon id="elemental_wizards_rpg:staff_aqua" /><ItemIcon id="elemental_wizards_rpg:staff_terra" /></ItemGrid>

| 武器类型 | 武器与法器 |
| --- | --- |
| 法杖与法器 | <ItemLink id="wizards:staff_arcane" />, <ItemLink id="wizards:staff_fire" />, <ItemLink id="wizards:staff_frost" />, <ItemLink id="paladins:holy_staff" />, <ItemLink id="elemental_wizards_rpg:staff_aqua" />, <ItemLink id="elemental_wizards_rpg:staff_terra" />, <ItemLink id="elemental_wizards_rpg:staff_wind" /> |
| 弓与弩 | <ItemLink id="minecraft:bow" />, <ItemLink id="minecraft:crossbow" />, <ItemLink id="bards_rpg:harp_crossbow" /> |
| 剑与匕首 | <ItemLink id="minecraft:iron_sword" />, <ItemLink id="paladins:iron_claymore" />, <ItemLink id="rogues:iron_dagger" />, <ItemLink id="bards_rpg:iron_rapier" />, <ItemLink id="witcher_rpg:iron_witcher_sword" /> |
| 斧与锤 | <ItemLink id="minecraft:iron_axe" />, <ItemLink id="rogues:iron_double_axe" />, <ItemLink id="berserker_rpg:iron_berserker_axe" />, <ItemLink id="paladins:iron_great_hammer" />, <ItemLink id="paladins:iron_mace" /> |
| 乐器 | <ItemLink id="bards_rpg:wooden_lute" />, <ItemLink id="bards_rpg:golden_lyre" /> |
| 其他专精 | <ItemLink id="rogues:iron_glaive" />, <ItemLink id="rogues:iron_sickle" />, <ItemLink id="archers:iron_spear" />, <ItemLink id="forcemaster_rpg:iron_knuckle" /> |

每件武器在武器技能中都有对应的专精分支，强化分支则以被修改的招式命名。

***

## 重置与调整

<EmiSearch query="@skill_tree_rpgs" />

<ItemGrid><ItemIcon id="skill_tree_rpgs:orb_of_oblivion" /></ItemGrid>

<ItemLink id="skill_tree_rpgs:orb_of_oblivion" />

<Recipe id="skill_tree_rpgs:orb_of_oblivion" />

法术强化节点修改对应招式，不会凭空增加无关职业法术，因此先确认当前点数预算与互斥根节点。

- [武技](combat.martial.md) 查看远程射击、近战与职业招式。
- [法术与招式](combat.abilities.md) 查看法术绑定、卷轴与施法操作。
- [魔法与辅助](combat.magic.md) 查看武器法术、乐曲、符文与符文袋。
- [武器与护甲](equipment.weapons-armor.md) 选择武器类型，比较当前支持的各个变体。

***

## 配点目标与受阻节点

<ItemGrid><ItemIcon id="skill_tree_rpgs:orb_of_oblivion" /><ItemIcon id="spell_engine:spell_book" /></ItemGrid>

节点受阻可能是缺少连接、该分类点数不足、根节点互斥，或已达到投入上限。

想换路线时，先取得遗忘之球，阅读提示后再使用，然后重新打开技能树确认返还的点数。更换武器或装备另一本书不会重置技能树。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![More RPG Classes - Skill Tree (RPG Series Plus)](images/catalog-3oymnudq.png) [More RPG Classes - Skill Tree (RPG Series Plus)](combat.skills.md) | 为 More RPG Classes 的扩展职业增加职业技能树支持。 | 无独立物品查询 |
| ![Pufferfish's Skills](images/catalog-hqqqvaa4.png) [Pufferfish's Skills](combat.skills.md) | 提供可自定义的技能系统与技能树界面。 | 无独立物品查询 |
| ![Skill Tree (RPG Series)](images/catalog-pjdhrusc.png) [Skill Tree (RPG Series)](combat.skills.md) | 为 RPG Series 角色增加职业技能树。 | <EmiSearch query="@skill_tree_rpgs" /> |
