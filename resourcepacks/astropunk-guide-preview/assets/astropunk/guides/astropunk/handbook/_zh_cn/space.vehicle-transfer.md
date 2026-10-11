---
navigation:
  title: "轨道飞行"
  position: 0
  parent: reference.vehicles.md
  icon: rocketnautics:rocket_thruster
item_ids:
  - rocketnautics:rocket_thruster
---

# 轨道飞行

## 火箭推进器

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="rocketnautics:rocket_thruster" />
</ItemGrid>

<ItemLink id="rocketnautics:rocket_thruster" />

使用 <ItemLink id="create:mechanical_crafter" />制作液体燃料火箭推进器。在配方浏览器中查看机械合成配方。推进器的 Ponder 演示展示推进器与储罐的布置。

***

## 轨道飞行

建造一艘能由 Sable 组装为移动子空间的物理飞船，然后安装火箭推进器并为其供油。通过流体系统供应熔岩，<ItemLink id="minecraft:lava_bucket" /> 表示所需流体，而不是会被消耗的合成材料。推进器只接受火箭燃料标签中的流体，不接受任意液体。它在组装后的物理飞船上产生推力，需保持燃料供应。旋转动力不会直接驱动此推进器。

主世界进入太空的边界是飞船世界坐标 Y 超过 20,000。这不是从发射台向上计算的距离。已组装且准备好物理模拟的飞船越过此边界时，飞船及其附近乘客会被转移到深空。这是进入轨道的飞行转换，不是火箭推进器直接将玩家送到月球。月球与火星是行星系统中的独立连接维度。

不要仅凭天空画面变化就判断飞船已进入其他维度。

- [太空目的地](space.destinations.md) 可登陆世界与行星数据。
- [太空生命支持](space.life-support.md) 完好飞船舱室中的呼吸与重力。
- [太空导航](space.navigation.md) 使用行星总览，不要将其误认为自动驾驶。

***

## 进入地表维度

在深空中，靠近当前所环绕且连接到地表维度的行星，越过转换边界后，飞船会进入该行星的地表维度。主世界、月球与火星的边界距行星表面 20,000 格。返回时飞船位于世界坐标 Y 19,000，而不是地面。这是维度转换，不是落地或自动着陆。

请在世界坐标 Y 2,500 之前减慢下降速度。飞船在 Y 1,000 至 Y 2,500 之间以超过每秒 60 格的速度下降时会发热，更强的热量可能伤害附近乘客。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics Expansion](space.navigation.md) | 新增可登陆的火星维度、地貌与行星数据。 | <EmiSearch query="@rocketnautics_addon" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | 可交互移动方块结构框架。 | 无独立物品查询 |
