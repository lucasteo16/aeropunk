---
navigation:
  title: "操作船只与潜艇"
  position: 0
  parent: reference.vehicles.md
  icon: minecraft:oak_boat
---

# 操作船只与潜艇

## 船壳

![发布者铜潜艇](images/building-travel-submarine.png)

Deep Seas 铜制潜艇。

***

## 浮力与推进

<EmiSearch query="@create_submarine" />

<ItemGrid>
  <ItemIcon id="create_submarine:floater" />
  <ItemIcon id="create_submarine:ballast_tank" />
  <ItemIcon id="create_submarine:ballast_vent" />
  <ItemIcon id="create_submarine:water_thruster" />
  <ItemIcon id="create_submarine:submarine_propeller" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create_submarine:floater" /> |
| <ItemLink id="create_submarine:ballast_tank" /> |
| <ItemLink id="create_submarine:ballast_vent" /> |
| <ItemLink id="create_submarine:water_thruster" /> |
| <ItemLink id="create_submarine:submarine_propeller" /> |

浮筒用于水面船只。压载水箱与压载通风口控制水下浮力。通风口需要旋转动力、连接水箱的管道，以及至少一面接触海水。反转旋转方向可排水。水推进器需要水与旋转动力。潜艇螺旋桨用于水下，不能在空气中工作。

***

## 空气与压力

<ItemGrid>
  <ItemIcon id="create_submarine:electrolyzer" />
  <ItemIcon id="create_submarine:oxygene_diffuser" />
  <ItemIcon id="create_submarine:barometer" />
  <ItemIcon id="create_submarine:copper_pressurizer" />
  <ItemIcon id="create_submarine:iron_pressurizer" />
  <ItemIcon id="create_submarine:phycological_membrane" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create_submarine:electrolyzer" /> |
| <ItemLink id="create_submarine:oxygene_diffuser" /> |
| <ItemLink id="create_submarine:barometer" /> |
| <ItemLink id="create_submarine:copper_pressurizer" /> |
| <ItemLink id="create_submarine:iron_pressurizer" /> |
| <ItemLink id="create_submarine:phycological_membrane" /> |

电解器消耗水与 Forge Energy 生成氧气。氧气扩散器需要氧气与红石信号，用量随内部空间大小变化。压力表将压力与最薄弱船壳方块的承受能力比较。铜和铁耐压玻璃用于耐压窗。藻膜可以充气。

***

## 缆索与设备

<ItemGrid>
  <ItemIcon id="create_submarine:steel_cable" />
  <ItemIcon id="create_submarine:pulley" />
  <ItemIcon id="create_submarine:industrial_alarm" />
  <ItemIcon id="create_submarine:underwater_mine" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create_submarine:steel_cable" /> |
| <ItemLink id="create_submarine:pulley" /> |
| <ItemLink id="create_submarine:industrial_alarm" /> |
| <ItemLink id="create_submarine:underwater_mine" /> |

钢缆与相向的一对滑轮用于沿缆索运动的建筑。工业警报器与水下水雷为附加设备。创造供氧器属于创造模式设备。拦阻钩与减压舱的物品提示明确标注未完成，不应当作可用生存系统。入门时先阅读压载、电解器、扩散器与压力表思索演示，再下潜。维度单独说明目的地进入方式。

- [维度](world.dimensions.md)

***

## 制作

<Recipe id="create_submarine:ballast_tank" />

## 未完成设备

<ItemGrid>
  <ItemIcon id="create_submarine:arresting_hook" />
  <ItemIcon id="create_submarine:decompression_chamber" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create_submarine:arresting_hook" /> |
| <ItemLink id="create_submarine:decompression_chamber" /> |

这些设备的物品提示标明尚未完成，不能作为可用的生存系统。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Deep Seas](images/catalog-mva5q4qZ.png) [Create Deep Seas](vehicles.water.md) | 为 Aeronautics 船只与潜艇增加水上及水下航行部件。 | <EmiSearch query="@create_submarine" /> |
