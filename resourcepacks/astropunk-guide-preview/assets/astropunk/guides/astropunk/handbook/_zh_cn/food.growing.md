---
navigation:
  title: "种植与收获食材"
  position: 2
  parent: reference.food.md
  icon: minecraft:wheat
---

# 种植与收获食材

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Farmer%27s%20Delight%20crops%20rice%20tomato%20rope%20farming%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20%E5%86%9C%E5%A4%AB%E4%B9%90%E4%BA%8B%20%E4%BD%9C%E7%89%A9%20%E7%A8%BB%E7%B1%B3%20%E7%95%AA%E8%8C%84%20%E7%BB%B3%E5%AD%90%20%E7%A7%8D%E6%A4%8D%20%E6%95%99%E7%A8%8B)

## 野生作物

<EmiSearch query="@farmersdelight" />

![一园烹饪食材](images/visual-garden-crops.png)


| 作物丛 | 辨认 | 空手打掉 | 用剪刀 |
| --- | --- | --- | --- |
| <ItemLink id="farmersdelight:wild_cabbages" /> | <ItemGrid><ItemIcon id="farmersdelight:wild_cabbages" /></ItemGrid> | 卷心菜种子，偶尔还有卷心菜 | 整丛取下，搬到别处种植 |
| <ItemLink id="farmersdelight:wild_tomatoes" /> | <ItemGrid><ItemIcon id="farmersdelight:wild_tomatoes" /></ItemGrid> | 番茄种子，偶尔还有番茄 | 整丛取下，搬到别处种植 |
| <ItemLink id="farmersdelight:wild_onions" /> | <ItemGrid><ItemIcon id="farmersdelight:wild_onions" /></ItemGrid> | 一个洋葱 | 整丛取下，搬到别处种植 |
| <ItemLink id="farmersdelight:wild_rice" /> | <ItemGrid><ItemIcon id="farmersdelight:wild_rice" /></ItemGrid> | 稻米 | 整丛取下，搬到别处种植 |

作物丛是一次性发现。用剪刀把整丛取下就能搬家，但搬走之后它不会自己再长回来，想要更多就继续找新的丛，或者用打下来的种子自己种。

***

## 种下第一份作物

<ItemGrid><ItemIcon id="farmersdelight:cabbage_seeds" /><ItemIcon id="farmersdelight:tomato_seeds" /><ItemIcon id="farmersdelight:onion" /><ItemIcon id="farmersdelight:rice" /></ItemGrid>

卷心菜是最简单的第一份作物。把 <ItemLink id="farmersdelight:cabbage_seeds" /> 种在水边耕地上，等菜球成形。成熟的菜球是汤和卷的绿叶材料，一颗还能在切菜板上切出两张叶片。

番茄种在耕地上即可，<ItemLink id="farmersdelight:rope" /> 是可选的支架，只让藤长得更高，没有绳子也能结果。洋葱直接把鳞茎种下去。

稻米和这三种旱地作物不同。把 <ItemLink id="farmersdelight:rice" /> 种进一格深的水源水里，水下面放泥土。它会长成两格高的植株。收获得到 <ItemLink id="farmersdelight:rice_panicle" />，而下一茬仍然用稻米播种，不是用稻穗。

每种作物的成功标志不同。卷心菜和洋葱看菜球或鳞茎是否饱满，番茄看藤上是否挂着成熟的果实，稻米看稻穗是否到了可以收割的状态。

***

## 收割与处理稻米

| 结果 | 怎么得到 | 用途 |
| --- | --- | --- |
| <ItemGrid><ItemIcon id="farmersdelight:rice_panicle" /></ItemGrid> | 收割成熟的稻株 | 未经处理的收获物 |
| <ItemGrid><ItemIcon id="farmersdelight:rice" /></ItemGrid> | 合成稻穗 | 锅与碗装料理用的米，也可以留作下一茬种子 |
| <ItemGrid><ItemIcon id="farmersdelight:straw" /></ItemGrid> | 用刀在切菜板上切稻穗 | 绳子、帆布与合成材料 |

合成稻穗只出米。用刀在 <ItemLink id="farmersdelight:cutting_board" /> 上切稻穗会同时出米和稻草，所以等你要用绳子做番茄支架时，走切菜板这条路更划算。

***

## 肥沃土壤与蘑菇

<ItemGrid><ItemIcon id="farmersdelight:organic_compost" /><ItemIcon id="farmersdelight:rich_soil" /></ItemGrid>

合成 <ItemLink id="farmersdelight:organic_compost" />，放下肥堆并等待。附近的水，以及相邻的肥堆、肥沃土壤、菌丝、<ItemLink id="minecraft:podzol" />或蘑菇都会加快分解，最后变成 <ItemLink id="farmersdelight:rich_soil" />。

用锄头把肥沃土壤变成肥沃耕地，适合播种作物。本整合包把肥沃土壤提供骨粉催熟效果的几率设为百分之二十。

在暗处把蘑菇种在肥沃土壤上，会长成一小丛蘑菇。打掉整丛可以拿到每一朵，用剪刀则能整丛搬走。

***

## 田间辅助

<EmiSearch query="@create_integrated_farming" />

| 辅助或机器 | 辨认 | 操作 |
| --- | --- | --- |
| <ItemLink id="minecraft:bone_meal" /> | <ItemGrid><ItemIcon id="minecraft:bone_meal" /></ItemGrid> | 配合 Universal Bone Meal 可让甘蔗与仙人掌生长，原版骨粉对它们无效 |
| <ItemLink id="create_integrated_farming:vacuum_harvester" /> | <ItemGrid><ItemIcon id="create_integrated_farming:vacuum_harvester" /></ItemGrid> | 由旋转动力充能，收获物存在机器内部，除传动轴一侧外任意面都能取出 |

RightClickHarvest 让你右键一次就完成收割与补种。本整合包把它配置成不需要锄头，空手也可以。

Smarter Farmers 让村民补种对应作物的种子，包括模组作物。

真空收割机只把收获存在自己内部，不会继续往外推送，指望它自动输出的产线不会工作。

***

## 作物分组

<EmiSearch query="@minersdelight" /> <EmiSearch query="@mynethersdelight" />

| 分组 | 物品 | 作用 |
| --- | --- | --- |
| 农田作物 | <ItemGrid><ItemIcon id="farmersdelight:cabbage" /><ItemIcon id="farmersdelight:tomato" /><ItemIcon id="farmersdelight:onion" /><ItemIcon id="farmersdelight:rice" /></ItemGrid> | 本页种植的四种作物，尚未处理。 |
| 种子与种苗 | <ItemGrid><ItemIcon id="farmersdelight:cabbage_seeds" /><ItemIcon id="farmersdelight:tomato_seeds" /><ItemIcon id="farmersdelight:rice_panicle" /></ItemGrid> | 用来开始下一茬的材料。洋葱直接用上面的鳞茎种植，稻米用米播种。 |
| 收获产物 | <ItemGrid><ItemIcon id="farmersdelight:cabbage_leaf" /><ItemIcon id="farmersdelight:straw" /><ItemIcon id="farmersdelight:rice" /></ItemGrid> | 切菜板与收割的产物，用来做绳子、烹饪与合成。 |
| 原版菜园作物 | <ItemGrid><ItemIcon id="minecraft:wheat" /><ItemIcon id="minecraft:carrot" /><ItemIcon id="minecraft:potato" /><ItemIcon id="minecraft:beetroot" /></ItemGrid> | 厨房同样会用的普通耕地作物。 |
| 地区作物 | <ItemGrid><ItemIcon id="minersdelight:cave_carrot" /><ItemIcon id="mynethersdelight:bullet_pepper" /></ItemGrid> | 在其他地区种植与采集，归[地下食物](food.underground.md)与[下界食物](food.nether.md)。 |

- [机器厨房](food.machine-cooking.md) 自动切片与生产肥料。
- [烹饪工具与料理](food.utensils.md) 把收获做成料理。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Integrated Farming](images/catalog-9k1pasfr.png) [Create: Integrated Farming](food.growing.md) | 为机械动力增加自动收割、渔网与家禽产物自动收集。 | <EmiSearch query="@create_integrated_farming" /> |
| ![Leaves Be Gone](images/catalog-avq17pqv.png) [Leaves Be Gone](food.growing.md) | 让树木被砍后失去支撑的树叶快速凋落。 | 无独立物品查询 |
| ![RightClickHarvest](images/catalog-cnejf5xm.png) [RightClickHarvest](food.growing.md) | 右键即可收获成熟作物，无需手动破坏再补种。 | 无独立物品查询 |
| ![Smarter Farmers (farmers replant)](images/catalog-bh6zomvp.png) [Smarter Farmers (farmers replant)](food.growing.md) | 让农民村民正确补种作物，也支持部分模组种子。 | 无独立物品查询 |
| ![Universal Bone Meal](images/catalog-66viit1y.png) [Universal Bone Meal](food.growing.md) | 让骨粉可用于原本不接受骨粉的植物。 | 无独立物品查询 |
