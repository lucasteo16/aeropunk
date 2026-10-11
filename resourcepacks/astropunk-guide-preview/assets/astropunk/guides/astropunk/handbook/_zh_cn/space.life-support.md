---
navigation:
  title: "太空生命支持"
  position: 11
  parent: reference.vehicles.md
  icon: rocketnautics:space_helmet
item_ids:
  - rocketnautics:space_helmet
  - rocketnautics:jetpack
  - rocketnautics:copper_leg_thrusters
  - rocketnautics:copper_anchor_boots
  - cosmonauticsdeepair:gravity_generator
  - create_submarine:electrolyzer
  - create_submarine:oxygene_diffuser
---

# 太空生命支持

## 个人呼吸装备

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:copper_diving_helmet" />
  <ItemIcon id="create:copper_backtank" />
  <ItemIcon id="create:netherite_backtank" />
  <ItemIcon id="rocketnautics:space_helmet" />
  <ItemIcon id="rocketnautics:jetpack" />
</ItemGrid>

| 装备 | 用途 |
| --- | --- |
| <ItemLink id="create:copper_diving_helmet" /> | 可合成的呼吸头盔，需搭配加压气源，穿在头部装备栏。 |
| <ItemLink id="create:copper_backtank" />, <ItemLink id="create:netherite_backtank" /> | 储存呼吸用的空气。充气后穿在胸部装备栏，充气方法见背罐的 Ponder 演示。 |
| <ItemLink id="rocketnautics:space_helmet" /> | 带轨道显示的呼吸头盔，没有合成配方。 |
| <ItemLink id="rocketnautics:jetpack" /> | 消耗燃料的飞行胸甲，也提供加压空气。 |

入门可使用铜潜水头盔与已充气的铜背罐。有燃料的喷气背包是另一种气源，不必用它替换背罐。

<Recipe id="create:crafting/appliances/copper_diving_helmet" />

<Recipe id="create:crafting/appliances/copper_backtank" />

***

## 喷气背包燃料与飞行

<ItemGrid>
  <ItemIcon id="rocketnautics:jetpack" />
  <ItemIcon id="minecraft:lava_bucket" />
  <ItemIcon id="create:spout" />
</ItemGrid>

用 <ItemLink id="minecraft:lava_bucket" /> 或 <ItemLink id="create:spout" /> 补充熔岩。使用 <KeyBind id="key.rocketnautics.toggle_jetpack" /> 切换飞行，默认按键为 G。不需要飞行时关闭该功能可节省燃料。喷气背包的供气仍会消耗燃料，不受飞行开关控制。

<Recipe id="rocketnautics:crafting/equipment/jetpack" />

***

## 供氧舱室

<EmiSearch query="@create_submarine" />

<ItemGrid>
  <ItemIcon id="create_submarine:electrolyzer" />
  <ItemIcon id="create_submarine:oxygene_diffuser" />
</ItemGrid>

使用 Deep Seas 舱室工具，在 Sable 飞船内建造完好的密封舱室。飞船未破损时，Deep Air 让供氧舱室中的实体恢复呼吸。它不会密封船体，也不会制造氧气。

| 机器 | 要求 |
| --- | --- |
| <ItemLink id="create_submarine:electrolyzer" /> | 用水与 Forge Energy 产生氧气。 |
| <ItemLink id="create_submarine:oxygene_diffuser" /> | 位于密封舱室内，储罐有氧气，并接收红石信号。 |

将氧气供给连接到扩散器，并持续供氧。两种机器的 Ponder 演示说明供能、流体与红石要求。

<Recipe id="create_submarine:electrolyzer" />

<Recipe id="create_submarine:oxygen_diffuser" />

***

## 舱室重力

<EmiSearch query="@cosmonauticsdeepair" />

![飞船舱室中的重力设备](images/cosmo-gravity-room.png)

<ItemGrid>
  <ItemIcon id="cosmonauticsdeepair:gravity_generator" />
</ItemGrid>

<ItemLink id="cosmonauticsdeepair:gravity_generator" /> 在完好密封的舱室内提供局部重力。它需要 Forge Energy 与相邻红石信号，并且必须位于已组装的 Sable 飞船内。

重力与呼吸是不同的舱室功能。重力舱室本身不需要扩散器，但飞船至少应有一个供氧舱室，以维持 Deep Seas 的舱室追踪。发生器不会改变飞船的轨道重力。

<Recipe id="cosmonauticsdeepair:gravity_generator" />

***

## 个人移动装备

<ItemGrid>
  <ItemIcon id="rocketnautics:copper_leg_thrusters" />
  <ItemIcon id="rocketnautics:copper_anchor_boots" />
</ItemGrid>

| 装备 | 用途 |
| --- | --- |
| <ItemLink id="rocketnautics:copper_leg_thrusters" /> | 消耗加压空气来提供飞行与惯性阻尼。使用 <KeyBind id="key.rocketnautics.toggle_dampeners" /> 切换阻尼，默认按键为 Z。 |
| <ItemLink id="rocketnautics:copper_anchor_boots" /> | 靠近支撑地板时帮助保持落地，但不影响正在飞行的玩家，也不产生舱室重力。 |

<Recipe id="rocketnautics:crafting/equipment/copper_leg_thrusters" />

<Recipe id="rocketnautics:crafting/equipment/copper_anchor_boots" />

***

## 相关页面

- [水上载具](vehicles.water.md)
- [轨道飞行](space.vehicle-transfer.md)
- [维度](world.dimensions.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Cosmonautics: Deep Air](images/cosmo-rzqxjxfo-icon.png) [Cosmonautics: Deep Air](space.life-support.md) | 将 Deep Seas 密封舱室连接到太空呼吸与供能人工重力功能。 | <EmiSearch query="@cosmonauticsdeepair" /> |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| ![Create Deep Seas](images/catalog-mva5q4qz.png) [Create Deep Seas](vehicles.water.md) | 为 Aeronautics 船只与潜艇增加水上及水下航行部件。 | <EmiSearch query="@create_submarine" /> |
