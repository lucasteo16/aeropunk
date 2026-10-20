---
navigation:
  title: "储存工厂的大批原料"
  position: 2
  parent: reference.machines-storage.md
  icon: create:item_vault
---

# 储存工厂的大批原料

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Vibrant+Vaults+Bulk+storage+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Vibrant+Vaults+%E5%82%A8%E5%AD%98%E5%B7%A5%E5%8E%82%E7%9A%84%E5%A4%A7%E6%89%B9%E5%8E%9F%E6%96%99+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 储物仓容量是方块数乘二十

<EmiSearch query="@create_connected" /> <EmiSearch query="@create" />

<ItemLink id="create:item_vault" /> 以相连方块的形式储存物品。本包把储物仓设为每格 20 组，因此容量取决于形状里的方块数，而不是你看到的那一面。

<Recipe id="create:crafting/kinetics/item_vault" />

<ItemGrid><ItemIcon id="create:item_vault" /><ItemIcon id="create_connected:item_silo" /><ItemIcon id="create_connected:inventory_access_port" /></ItemGrid>

| 形状 | 方块数 | 可存组数 |
| --- | --- | --- |
| 单格储物仓 | 1 | 20 |
| 两格储物仓 | 2 | 40 |
| 三乘三一面 | 9 | 180 |

储物仓只通过自己的面和贴着面的漏斗或滑槽连接。它不是箱子，没有可以整理的可视格界面。要用库存链接或显示链接去读它。

***

## 适合墙面的形状

<EmiSearch query="@create_vibrant_vaults" />

<ItemGrid><ItemIcon id="create_vibrant_vaults:shipping_container" /><ItemIcon id="create_vibrant_vaults:vertical_item_vault" /><ItemIcon id="create_vibrant_vaults:vertical_shipping_container" /><ItemIcon id="create_connected:fluid_vessel" /><ItemIcon id="create_vibrant_vaults:basic_shipping_container" /><ItemIcon id="create_vibrant_vaults:vertical_basic_shipping_container" /></ItemGrid>

| 方块 | 用途 |
| --- | --- |
| <ItemLink id="create_connected:item_silo" /> | 用于高层空间的竖向储物仓 |
| <ItemLink id="create_vibrant_vaults:shipping_container" /> | 看着像集装箱堆场的宽储存 |
| <ItemLink id="create_vibrant_vaults:vertical_item_vault" /> | 窄房间用的高储存 |
| <ItemLink id="create_vibrant_vaults:vertical_shipping_container" /> | 竖向集装箱变体 |
| <ItemLink id="create_connected:fluid_vessel" /> | 横向流体罐 |

Vibrant Vaults 为每个家族加入彩色与染色版本。颜色是标签，不改变容量，同样形状的红色储物仓与蓝色储物仓存的一样多。

流体容器是横向储罐，可以改成锅炉但效率较低。它的窗口形状可用扳手切换，在把它埋进墙里之前值得先调好。

***

## 够到看不见的那一面

<ItemGrid><ItemIcon id="create_connected:inventory_access_port" /><ItemIcon id="create_connected:inventory_bridge" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:stock_link" /></ItemGrid>

| 部件 | 效果 |
| --- | --- |
| <ItemLink id="create_connected:inventory_access_port" /> | 在狭窄位置给容器增加一个可用面 |
| <ItemLink id="create_connected:inventory_bridge" /> | 把两个容器作为一个连接暴露，过滤器仍然有效 |
| <ItemLink id="create:brass_funnel" /> | 从指定面取出过滤后的物品 |
| <ItemLink id="create:stock_link" /> | 让储物仓对库存网络可见 |

改变布局的是桥接器。通过它抽取物品时过滤器有效，因此一整面储物仓可以只露出一个整齐的出口，而不会把里面的东西全部漏出去。

这两个部件都不增加容量。装了三个接入口的储物仓，装的还是原来那么多。

***

## 放下第一只储物仓

<ItemGrid><ItemIcon id="create:item_vault" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:stock_link" /></ItemGrid>

1. 做一只 <ItemLink id="create:item_vault" />，贴放在它服务的房间墙边。
2. 在传送带够得到的那一面装漏斗或滑槽。
3. 贴着第一格再加一格，确认两格被读作同一处储存。
4. 若要让工厂仪表统计内容，装上库存链接。

要看到的结果是储存靠增加方块而增长，而不是靠增加箱子。下一步是不用玩家也能喂满它。[物料输送](machines.logistics.md)说明传送带、机械臂与包裹。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Vibrant Vaults](images/catalog-hddn8ksr.png) [Create: Vibrant Vaults](storage.bulk.md) | 增加机械动力物品仓库的颜色与材料变体。 | <EmiSearch query="@create_vibrant_vaults" /> |
