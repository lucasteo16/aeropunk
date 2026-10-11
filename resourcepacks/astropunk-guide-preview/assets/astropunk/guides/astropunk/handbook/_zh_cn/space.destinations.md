---
navigation:
  title: "太空目的地"
  position: 0
  parent: reference.vehicles.md
  icon: rocketnautics:lunar_rock
---

# 太空目的地

## 可登陆目的地

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

Cosmonautics将主世界连接到可登陆的月球维度。Create Cosmonautics Expansion新增可登陆的火星维度。基础版本也定义了气态巨行星与冰世界这两个天体，但其行星数据没有连接到可游玩的地表维度。在天空或行星展示中看到某颗行星，并不能证明存在可登陆的世界。

| 目的地 | 已包含地貌 |
| --- | --- |
| 月球 | 月球高地、月海与岩石峡谷 |
| 火星 | 平原、冻原与地下洞穴 |

月球与火星既有维度定义，也有行星数据。深空是物理飞船使用的中转维度，不是另一个行星地表。

- [维度](world.dimensions.md) 查看整合包中的可登陆维度与地貌。
- [轨道飞行](space.vehicle-transfer.md) 建造并驾驶物理飞船。

***

## 前往目的地

建造一艘能由 Sable 组装为移动子空间的物理飞船。安装液体燃料 <ItemLink id="rocketnautics:rocket_thruster" />，并查看其内置 Ponder 演示，了解推进器的安装与操作。维度转换检查的是飞船的世界坐标 Y。主世界的行星数据将转换高度设为 20,000，这是坐标值，不是相对于发射台的高度。已组装且拥有有效物理句柄的飞船越过此边界时，转换系统会将飞船及附近乘客带入深空。目的地行星数据将月球与火星维度连接到轨道宇宙中。

<ItemLink id="rocketnautics:hologram_block" /> 用于展示天体系统，不能选择目的地或自动驾驶着陆。

- [轨道飞行](space.vehicle-transfer.md) 火箭建造，以及主世界至深空的转换。
- [太空导航](space.navigation.md) 查看行星展示，并了解它与飞行控制的区别。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics Expansion](space.navigation.md) | 新增可登陆的火星维度、地貌与行星数据。 | <EmiSearch query="@rocketnautics_addon" /> |
