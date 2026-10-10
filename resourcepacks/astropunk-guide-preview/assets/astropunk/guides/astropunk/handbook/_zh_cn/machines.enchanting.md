---
navigation:
  title: "附魔、修理与查看装备"
  position: 0
  parent: reference.machines-storage.md
  icon: minecraft:enchanting_table
---

# 附魔、修理与查看装备

## 经验与附魔

<EmiSearch query="@create_enchantment_industry" />

<ItemGrid>
  <ItemIcon id="create_enchantment_industry:mechanical_grindstone" />
  <ItemIcon id="create_enchantment_industry:grindstone_drain" />
  <ItemIcon id="create_enchantment_industry:blaze_enchanter" />
  <ItemIcon id="create_enchantment_industry:enchanting_template" />
  <ItemIcon id="create_enchantment_industry:blaze_forger" />
  <ItemIcon id="create_enchantment_industry:printer" />
  <ItemIcon id="create_enchantment_industry:experience_hatch" />
  <ItemIcon id="create_enchantment_industry:experience_lantern" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create_enchantment_industry:mechanical_grindstone" />, <ItemLink id="create_enchantment_industry:grindstone_drain" /> | 将机械砂轮装在分液池上，把经验物品转换为液态经验。 |
| <ItemLink id="create_enchantment_industry:blaze_enchanter" />, <ItemLink id="create_enchantment_industry:enchanting_template" /> | 烈焰人附魔器使用液态经验与附魔模板处理装备。 |
| <ItemLink id="create_enchantment_industry:blaze_forger" />, <ItemLink id="create_enchantment_industry:printer" /> | 烈焰人锻造器负责锻造处理，打印机复制支持的书籍与其他可打印物品。 |
| <ItemLink id="create_enchantment_industry:experience_hatch" />, <ItemLink id="create_enchantment_industry:experience_lantern" /> | 经验舱口用于取用经验，经验灯笼用于显示经验。 |

***

## 铁砧

<ItemGrid>
  <ItemIcon id="minecraft:anvil" />
  <ItemIcon id="minecraft:name_tag" />
</ItemGrid>

Easy Anvils 改善 <ItemLink id="minecraft:anvil" /> 的手动操作与 <ItemLink id="minecraft:name_tag" /> 的编辑功能，它们不是动力工厂机器。

***

## 联动范围

黄铜书架与灌注器需要 Apothic Enchanting，烈焰人合成器、词缀强化器与宝石切割器需要 Apotheosis。轻型版与重型版都未包含这两个前置模组，因此这些联动机器不属于两版的附魔目录。

***

## 初次使用

先制作机械砂轮，查看思索演示中的分液池转换与经验输入。消耗液态经验前，先查看烈焰人附魔器的演示。超级附魔可能引发雷击，启用前应先阅读对应说明。

<Recipe id="create_enchantment_industry:crafting/mechanical_grindstone" />

## 相关物品

<EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:item_drain" />
</ItemGrid>

<ItemLink id="create:item_drain" />

## 相关主题

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Enchantment Industry](images/create-enchantment-industry-icon.png) [Create: Enchantment Industry](machines.enchanting.md) | 用机械动力机器自动处理经验与附魔。 | <EmiSearch query="@create_enchantment_industry" /> |
| ![Easy Anvils](images/catalog-ozbr5jt5.png) [Easy Anvils](machines.enchanting.md) | 改进铁砧物品存放与费用，移除不断累积的维修惩罚。 | 无独立物品查询 |
