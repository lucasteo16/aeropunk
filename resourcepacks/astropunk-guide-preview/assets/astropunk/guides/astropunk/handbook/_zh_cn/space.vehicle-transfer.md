---
navigation:
  title: "轨道飞行"
  position: 10
  parent: reference.vehicles.md
  icon: rocketnautics:rocket_thruster
item_ids:
  - rocketnautics:rocket_thruster
---

# 轨道飞行

## 火箭推进

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="rocketnautics:rocket_thruster" />
  <ItemIcon id="create:mechanical_crafter" />
  <ItemIcon id="minecraft:lava_bucket" />
</ItemGrid>

| 装备 | 用途 |
| --- | --- |
| <ItemLink id="rocketnautics:rocket_thruster" /> | 为已组装的物理飞船提供液体燃料推力。 |
| <ItemLink id="create:mechanical_crafter" /> | 制作推进器。在配方浏览器中查看机械合成的排列。 |
| <ItemLink id="minecraft:lava_bucket" /> | 图示代表熔岩燃料。通过飞船的流体系统供给熔岩，不是将桶作为合成材料放入推进器。 |

推进器消耗火箭燃料，不使用旋转动力。熔岩是一种可用的入门燃料。推进器的 Ponder 演示展示推进器与储罐的布置。

***

## 离开主世界

用 Sable 组装物理飞船，安装推进器并保持燃料供应。飞船越过世界坐标 Y 20,000 后，会与附近乘客一起进入深空。此高度是世界坐标，不是距离发射台的高度。

深空是前往行星地表的轨道空间。仅凭天空画面变化，不能判断是否已进入其他维度。

***

## 进入地表维度

在深空中接近当前所环绕且有地表维度的行星。进入距其表面 20,000 格以内的范围后，飞船会转入该行星的维度，位于世界坐标 Y 19,000。主世界、月球与火星都使用这些边界。进入地表维度后，飞船仍在高空，不会自动着陆或自动驾驶。

请在世界坐标 Y 2,500 之前减慢下降速度。在 Y 1,000 至 Y 2,500 之间，以超过每秒 60 格的速度下降会使飞船发热。更强的热量可能伤害附近乘客。

***

## 相关页面

- [组装](vehicles.assembly.md)
- [维度](world.dimensions.md)
- [太空生命支持](space.life-support.md)
- [太空导航](space.navigation.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| ![Create Cosmonautics Expansion](images/cosmo-gd7m0igy-icon.png) [Create Cosmonautics Expansion](world.dimensions.md) | 新增火星地貌，包括平原、冻原与地下洞穴。 | <EmiSearch query="@rocketnautics_addon" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | 可交互移动方块结构框架。 | 无独立物品查询 |
