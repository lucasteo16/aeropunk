---
navigation:
  title: "使用随机放置与蓝图工具"
  position: 0
  parent: reference.building.md
  icon: mechtrowel:mech_trowel
---

# 使用随机放置与蓝图工具

## 机械抹刀

<EmiSearch query="@mechtrowel" />

<ItemGrid>
  <ItemIcon id="mechtrowel:mech_trowel" />
  <ItemIcon id="mechtrowel:wand_template" />
  <ItemIcon id="mechtrowel:wand_capacity_template" />
  <ItemIcon id="mechtrowel:variant_conversion_template" />
  <ItemIcon id="mechtrowel:reach_upgrade_template" />
</ItemGrid>

<ItemLink id="mechtrowel:mech_trowel" /> 是实用建筑工具，并非另一种装饰方块。快速模式随机放置快捷栏中的方块。命名配色板可控制重复使用的材质组合，渐变模式则在不同配色段之间过渡。放置会消耗实际可用的建筑材料。

### 获取

<Recipe id="mechtrowel:mech_trowel" />

按配方所示对角线摆放一个 <ItemLink id="minecraft:iron_ingot" />、一个 <ItemLink id="minecraft:iron_block" /> 和一个 <ItemLink id="minecraft:stick" />，制作一把抹刀。

### 配色操作

| 操作 | 当前按键 |
| --- | --- |
| 配色管理器 | <KeyBind id="key.mechtrowel.open_palette" /> |
| 建筑模式 | <KeyBind id="key.mechtrowel.toggle_build_mode" /> |
| 轮盘菜单 | <KeyBind id="key.mechtrowel.open_radial_menu" /> |
| 替换模式 | <KeyBind id="key.mechtrowel.toggle_replace" /> |

快速放置前在快捷栏准备材质组合，也可打开配色管理器创建并选择命名配色板。批量操作前先预览目标。替换会改变已有方块，应先在可舍弃的小区域试用。

***

## 抹刀升级

<EmiSearch query="@chipped" />

| 升级物品 | 功能 |
| --- | --- |
| <ItemLink id="mechtrowel:wand_template" /> | 解锁魔杖模式，按当前配色板扩展方块。 |
| <ItemLink id="mechtrowel:wand_capacity_template" /> | 提高单次魔杖操作的方块上限。 |
| <ItemLink id="mechtrowel:variant_conversion_template" /> | 用已有基础方块转换为支持的 Chipped 或 Rechiseled 变体。此版本已安装 Chipped。 |
| <ItemLink id="mechtrowel:reach_upgrade_template" /> | 增加放置距离。 |

升级配方受服务器设置控制。模组自带默认设置要求先升级才能使用魔杖模式。Applied Energistics 2 与 Refined Storage 的整合模板需要相应仓储模组。

### 魔杖模板

<Recipe id="mechtrowel:wand_template" />

在锻造台的模板槽放入末影珍珠，以抹刀为基础物品，以 <ItemLink id="mechtrowel:wand_template" /> 为附加物品。配方返回升级后的抹刀。

### 容量、变体与距离

<Recipe id="mechtrowel:wand_capacity_template" />

<Recipe id="mechtrowel:variant_conversion_template" />

<Recipe id="mechtrowel:reach_upgrade_template" />

这些升级采用相同锻造槽位安排，换成对应升级物品。通过配方浏览器确认服务器是否开放各项配方。

***

## 随机筛选器

<EmiSearch query="@createshufflefilter" />

<ItemGrid>
  <ItemIcon id="mechtrowel:mech_trowel" />
  <ItemIcon id="createshufflefilter:shuffle_filter" />
  <ItemIcon id="createshufflefilter:weighted_shuffle_filter" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="mechtrowel:mech_trowel" /> |
| <ItemLink id="createshufflefilter:shuffle_filter" /> |
| <ItemLink id="createshufflefilter:weighted_shuffle_filter" /> |

Shuffle Filter 与 Weighted Shuffle Filter 分别提供随机与加权配色选择。工具设置决定材料组合，但仍需要可用材料。

***

## 蓝图

<EmiSearch query="@create_pattern_schematics" />

<ItemGrid>
  <ItemIcon id="create_pattern_schematics:empty_pattern_schematic" />
  <ItemIcon id="create_pattern_schematics:pattern_schematic_and_quill" />
  <ItemIcon id="create_pattern_schematics:pattern_schematic" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create_pattern_schematics:empty_pattern_schematic" /> |
| <ItemLink id="create_pattern_schematics:pattern_schematic_and_quill" /> |
| <ItemLink id="create_pattern_schematics:pattern_schematic" /> |

Pattern Schematics 提供空白样式、已记录样式和样式蓝图与笔。Forgematica 提供客户端蓝图投影与材料规划。显示蓝图不会直接放置完成的载具，也不会免除生存模式材料需求。

***

## 制作

<Recipe id="create_pattern_schematics:pattern_schematic" />

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Pattern Schematics](images/catalog-cpqKG67r.png) [Create: Pattern Schematics](building.placement.md) | 让机械动力蓝图建造重复铺设指定图案。 | <EmiSearch query="@create_pattern_schematics" /> |
| ![Create: Shuffle Filter](images/catalog-gv5RRavC.png) [Create: Shuffle Filter](building.placement.md) | 让机械动力机械手从指定材料组中随机选块放置。 | <EmiSearch query="@createshufflefilter" /> |
| ![Forgematica](images/catalog-dCKRaeBC.png) [Forgematica](building.placement.md) | 显示建筑蓝图，辅助方块摆放与施工。 | 无独立物品查询 |
| ![Mech Trowel](images/catalog-nqFNRALS.png) [Mech Trowel](building.placement.md) | 从自定义材料组随机放置方块，并支持建筑魔杖式摆放。 | <EmiSearch query="@mechtrowel" /> |
