---
navigation:
  title: "附魔、修理与查看装备"
  position: 12
  parent: reference.machines-storage.md
  icon: minecraft:enchanting_table
---

# 附魔、修理与查看装备

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Enchantment+Industry+Easy+Anvils+Enchanting+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Enchantment+Industry+Easy+Anvils+%E9%99%84%E9%AD%94%E3%80%81%E4%BF%AE%E7%90%86%E4%B8%8E%E6%9F%A5%E7%9C%8B%E8%A3%85%E5%A4%87+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 把经验变成液体

<EmiSearch query="@create" />

Create: Enchantment Industry 把经验存成流体，这正是附魔能自动化的关键。转换发生在放在 <ItemLink id="create:item_drain" /> 上方的 <ItemLink id="create_enchantment_industry:mechanical_grindstone" />。

<EmiSearch query="@create_enchantment_industry" />

<ItemGrid><ItemIcon id="create_enchantment_industry:mechanical_grindstone" /><ItemIcon id="create_enchantment_industry:grindstone_drain" /><ItemIcon id="create:item_drain" /><ItemIcon id="create_enchantment_industry:experience_hatch" /><ItemIcon id="create_enchantment_industry:experience_lantern" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="create_enchantment_industry:mechanical_grindstone" /> | 磨制物品，也能打磨，并释放经验 |
| <ItemLink id="create_enchantment_industry:grindstone_drain" /> | 收集这些释放物的排液变体 |
| <ItemLink id="create:item_drain" /> | 把释放的经验收集为流体 |
| <ItemLink id="create_enchantment_industry:experience_hatch" /> | 让你把自己的经验存入储罐或取回 |
| <ItemLink id="create_enchantment_industry:experience_lantern" /> | 吸收附近经验，装在移动结构上也能工作 |

<Recipe id="create_enchantment_industry:crafting/mechanical_grindstone" />

第一步是在排除口上方磨掉一件附魔或受损物品，看储罐被填满。如果什么也没有，要么磨石没在转，要么排液口没有可推入的储罐。

***

## 附魔、锻造与复制

<ItemGrid><ItemIcon id="create_enchantment_industry:blaze_enchanter" /><ItemIcon id="create_enchantment_industry:blaze_forger" /><ItemIcon id="create_enchantment_industry:printer" /><ItemIcon id="create_enchantment_industry:enchanting_template" /></ItemGrid>

| 机器 | 发行方描述 |
| --- | --- |
| <ItemLink id="create_enchantment_industry:blaze_enchanter" /> | 由烈焰人充当智能附魔台 |
| <ItemLink id="create_enchantment_industry:blaze_forger" /> | 由烈焰人充当智能铁砧，用于修理与合并 |
| <ItemLink id="create_enchantment_industry:printer" /> | 复制成书、附魔书、命名牌与列车时刻表 |

改变基地运作方式的是打印机。一本好附魔书可以用液体经验换成一整叠副本，一次幸运的收获就能装备整个工坊。

自动化之前先读方块自带的帮助条目。附魔台与锻造台都要放入装备与液体经验，槽位细节具体，截图很快就会过时。

***

## 在线上修理

带经验修补的物品可以用装满液体经验的注液器修理，因此一条传送带经过就能修复装备。

<ItemGrid><ItemIcon id="create:spout" /><ItemIcon id="create:belt_connector" /><ItemIcon id="minecraft:enchanted_book" /></ItemGrid>

| 布置 | 结果 |
| --- | --- |
| 传送带上方的注液器，储罐装液体经验 | 经过的经验修补物品减少损伤 |
| 储罐旁的存取口 | 存入或取回自己的等级 |
| 发射器击杀与粉碎轮击杀 | 本模组下会掉落经验颗粒 |

当你带着不想替换的装备时，修理线就值得建。主工坊旁一条短带、一个注液器、一只储罐，能省掉大部分跑铁砧的路。铁砧与命名牌仍然是手动工具，Easy Anvils 改的是它们的界面，并没有把它们变成动力机器。

<ItemGrid><ItemIcon id="minecraft:anvil" /><ItemIcon id="minecraft:name_tag" /></ItemGrid>

***

## 本包没有的内容

本包没有安装 Apothic Enchanting 与 Apotheosis，因此这两个模组带来的联动方块不在这里的目录中。

| 联动方块 | 需要 |
| --- | --- |
| 黄铜书架、注入器 | Apothic Enchanting |
| 烈焰作曲器、词缀增幅器、宝石切割器 | Apotheosis |

按磨石、附魔台、锻造台、打印机与经验储存来规划。存在的机器就是这些。

下一步是给磨石供能。[旋转动力](machines.rotation.md)说明传动线。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Enchantment Industry](images/create-enchantment-industry-icon.png) [Create: Enchantment Industry](machines.enchanting.md) | 用机械动力机器自动处理经验与附魔。 | <EmiSearch query="@create_enchantment_industry" /> |
| ![Easy Anvils](images/catalog-ozbr5jt5.png) [Easy Anvils](machines.enchanting.md) | 改进铁砧物品存放与费用，移除不断累积的维修惩罚。 | 无独立物品查询 |
