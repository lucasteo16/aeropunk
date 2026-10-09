---
navigation:
  title: "附魔、修理与查看装备"
  position: 0
  parent: reference.machines-storage.md
  icon: minecraft:enchanting_table
---

# 附魔、修理与查看装备

## 经验与附魔

<EmiSearch query="@create_enchantment_industry" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create_enchantment_industry:mechanical_grindstone" />
  <ItemIcon id="create_enchantment_industry:grindstone_drain" />
  <ItemIcon id="create_enchantment_industry:blaze_enchanter" />
  <ItemIcon id="create_enchantment_industry:enchanting_template" />
  <ItemIcon id="create_enchantment_industry:blaze_composer" />
  <ItemIcon id="create_enchantment_industry:blaze_forger" />
  <ItemIcon id="create_enchantment_industry:printer" />
  <ItemIcon id="create_enchantment_industry:experience_hatch" />
  <ItemIcon id="create_enchantment_industry:experience_lantern" />
  <ItemIcon id="create_enchantment_industry:brass_bookshelf" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create_enchantment_industry:mechanical_grindstone" />, <ItemLink id="create_enchantment_industry:grindstone_drain" /> | Create: Enchantment Industry 通过砂轮排液器将经验物品转为液态经验。 |
| <ItemLink id="create_enchantment_industry:blaze_enchanter" />, <ItemLink id="create_enchantment_industry:enchanting_template" /> | 烈焰人附魔器使用液态经验与模板。 |
| <ItemLink id="create_enchantment_industry:blaze_composer" />, <ItemLink id="create_enchantment_industry:blaze_forger" />, <ItemLink id="create_enchantment_industry:printer" /> | 用于附魔加工与复制的合成器、锻造器和打印机系列。 |
| <ItemLink id="create_enchantment_industry:experience_hatch" />, <ItemLink id="create_enchantment_industry:experience_lantern" />, <ItemLink id="create_enchantment_industry:brass_bookshelf" /> | 经验取用、展示与书架组件。 |

***

## 铁砧与联动

<ItemGrid>
  <ItemIcon id="minecraft:anvil" />
  <ItemIcon id="minecraft:name_tag" />
  <ItemIcon id="create_enchantment_industry:infuser" />
  <ItemIcon id="create_enchantment_industry:affix_augmentor" />
  <ItemIcon id="create_enchantment_industry:gem_cutter" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="minecraft:anvil" />, <ItemLink id="minecraft:name_tag" /> | Easy Anvils 改善手动铁砧操作并提供命名牌编辑，不是动力机器。 |
| <ItemLink id="create_enchantment_industry:infuser" />, <ItemLink id="create_enchantment_industry:affix_augmentor" />, <ItemLink id="create_enchantment_industry:gem_cutter" /> | 可选联动组件。只有对应联动注册后才可使用，不应假定此整合包中一定存在这些物品或配方。 |

***

## 初次使用

先制作机械砂轮。其思索演示介绍置物排液器转换与经验输入。消耗液态经验前先查看烈焰人附魔器演示。超级附魔可能引发雷击，启用前请查看对应说明。

<Recipe id="create_enchantment_industry:crafting/mechanical_grindstone" />

## 相关物品

<ItemGrid>
  <ItemIcon id="create:item_drain" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create:item_drain" /> |

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create: Enchantment Industry](images/create-enchantment-industry-icon.png) [Create: Enchantment Industry](machines.enchanting.md) | 用机械动力机器自动处理经验与附魔。 | 已安装基准版 | <EmiSearch query="@create_enchantment_industry" /> |
| ![Easy Anvils](images/catalog-OZBR5JT5.png) [Easy Anvils](machines.enchanting.md) | 改进铁砧物品存放与费用，移除不断累积的维修惩罚。 | 已安装基准版 | 无独立物品查询 |
