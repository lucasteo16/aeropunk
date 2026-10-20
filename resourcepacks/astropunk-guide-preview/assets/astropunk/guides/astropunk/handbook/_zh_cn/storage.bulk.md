---
navigation:
  title: "储存工厂的大批原料"
  position: 2
  parent: reference.machines-storage.md
  icon: create:item_vault
---

# 储存工厂的大批原料

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+mod+item+vault+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E7%89%A9%E5%93%81%E4%BB%93%E5%BA%93+%E6%95%99%E7%A8%8B)

## 仓库容量

<EmiSearch query="@create" />

<ItemLink id="create:item_vault" /> 是批量工厂存储。相连的仓库方块组成一个库存，本整合包给每个方块 20 堆容量。

<Recipe id="create:crafting/kinetics/item_vault" />

仓库的横截面是正方形，最宽三块，长度最多是宽度的三倍。容量按实际成形的方块数量计算。

| 仓库形状 | 方块数 | 容量 |
| --- | --- | --- |
| 一乘一乘一 | 1 | 20 堆 |
| 二乘二横截面，长六块 | 24 | 480 堆 |
| 三乘三横截面，长九块 | 81 | 1620 堆 |

仓库没有箱子界面。物品不能手动放入或取出，所有物品都通过某一面的物品传输部件进出。

***

## 第一个仓库

1. 放下箱子，在它正上方放一个朝下、向箱子供料的漏斗。
2. 在漏斗正上方放一块仓库，再在仓库正上方放另一个朝下的漏斗。
3. 将少量物品放入上方漏斗。它会向仓库送入物品，下方漏斗则将物品抽入箱子。
4. 打开箱子确认物品到达。需要保留仓库里的物品而不是持续转运时，用红石锁住下方漏斗。

成功的表现是物品经下方漏斗进入箱子。仓库本身没有可打开的库存窗口。

| 部件 | 外观 | 作用 |
| --- | --- | --- |
| <ItemLink id="create:item_vault" /> | <ItemGrid><ItemIcon id="create:item_vault" /></ItemGrid> | 批量物品存储 |
| <ItemLink id="minecraft:hopper" /> | <ItemGrid><ItemIcon id="minecraft:hopper" /></ItemGrid> | 从上方输入或从下方抽取，出口指向接收容器 |
| <ItemLink id="minecraft:chest" /> | <ItemGrid><ItemIcon id="minecraft:chest" /></ItemGrid> | 接收抽出的物品 |
| <ItemLink id="create:brass_funnel" /> | <ItemGrid><ItemIcon id="create:brass_funnel" /></ItemGrid> | 在某一面过滤输入或抽取 |
| <ItemLink id="create:chute" /> | <ItemGrid><ItemIcon id="create:chute" /></ItemGrid> | 竖直传送物品 |

扩建与自动化布局可查看物品仓库的思索课程 Dimensions of an Item Vault 和 Storing Items in Vaults。

***

## 已安装的其他存储家族

<EmiSearch query="@create_connected" /> <EmiSearch query="@create_vibrant_vaults" />

| 存储方块 | 外观 | 作用 |
| --- | --- | --- |
| <ItemLink id="create_connected:item_silo" /> | <ItemGrid><ItemIcon id="create_connected:item_silo" /></ItemGrid> | 竖直批量物品存储 |
| <ItemLink id="create_vibrant_vaults:shipping_container" /> | <ItemGrid><ItemIcon id="create_vibrant_vaults:shipping_container" /><ItemIcon id="create_vibrant_vaults:vertical_shipping_container" /></ItemGrid> | 集装箱风格的仓库变体 |
| <ItemLink id="create_vibrant_vaults:basic_shipping_container" /> | <ItemGrid><ItemIcon id="create_vibrant_vaults:basic_shipping_container" /><ItemIcon id="create_vibrant_vaults:vertical_basic_shipping_container" /></ItemGrid> | 基础集装箱变体 |
| <ItemLink id="create_vibrant_vaults:vertical_item_vault" /> | <ItemGrid><ItemIcon id="create_vibrant_vaults:vertical_item_vault" /></ItemGrid> | 窄房间用的高仓库 |

颜色与集装箱外观只改变造型，不改变每块的容量规则。流体分支与物品存储分开，不会增加物品容量。

| 流体存储 | 外观 | 作用 |
| --- | --- | --- |
| <ItemLink id="create_connected:fluid_vessel" /> | <ItemGrid><ItemIcon id="create_connected:fluid_vessel" /></ItemGrid> | 流体罐，不是物品仓库 |

***

## 狭小空间的访问

| 接口 | 外观 | 作用与限制 |
| --- | --- | --- |
| <ItemLink id="create_connected:inventory_access_port" /> | <ItemGrid><ItemIcon id="create_connected:inventory_access_port" /></ItemGrid> | 扩展单个库存的访问面，不增加空间，不能串联，可被红石禁用 |
| <ItemLink id="create_connected:inventory_bridge" /> | <ItemGrid><ItemIcon id="create_connected:inventory_bridge" /></ItemGrid> | 只把两个库存暴露给接在桥本身的部件，不能串联，可被红石禁用 |
| <ItemLink id="create:stock_link" /> | <ItemGrid><ItemIcon id="create:stock_link" /></ItemGrid> | 接入库存网络，由打包机提供库存 |

桥的过滤槽决定放入的物品进哪个库存，两个过滤都不匹配的物品无法放入，抽取时同样遵守过滤。埋在墙里的单个仓库只需要一个可达面时，访问端口更简单。

库存链接属于物流网络：接入网络的打包机把它的库存提供给网络。它不是装满一个仓库的必需步骤。

- [物品与流体输送](machines.logistics.md) 传送带、机械臂、打包机与库存网络。
- [存储处理](storage.handling.md) 共用的物品移动与过滤。
- [便携存储](storage.portable.md) 随身携带的背包与潜影盒。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Vibrant Vaults](images/catalog-hddn8ksr.png) [Create: Vibrant Vaults](storage.bulk.md) | 增加机械动力物品仓库的颜色与材料变体。 | <EmiSearch query="@create_vibrant_vaults" /> |
