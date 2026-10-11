---
navigation:
  title: "太空生命支持"
  position: 0
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

## 太空呼吸

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

航天头盔没有合成配方。可合成的呼吸装备为 <ItemLink id="create:copper_diving_helmet" /> 与已充气的 <ItemLink id="create:copper_backtank" />，分别穿在头部与胸部装备栏。穿戴前按背罐的 Ponder 说明充气。已充气的 <ItemLink id="create:netherite_backtank" /> 也是气源。喷气背包则消耗燃料供气，不是储存压缩空气。

<Recipe id="create:crafting/appliances/copper_diving_helmet" />

<Recipe id="create:crafting/appliances/copper_backtank" />

<ItemGrid>
  <ItemIcon id="rocketnautics:space_helmet" />
  <ItemIcon id="rocketnautics:jetpack" />
</ItemGrid>

<ItemLink id="rocketnautics:space_helmet" />

航天头盔需要搭配加压气源才能在太空中呼吸。Cosmonautics 喷气背包既是加压气源，也是需要燃料的飞行胸甲。将头盔穿在头部装备栏，将喷气背包穿在胸部装备栏。喷气背包会缓慢消耗燃料来持续供气。启用喷气背包系统后才能进行个人飞行。

<Recipe id="rocketnautics:crafting/equipment/jetpack" />

喷气背包使用熔岩作为燃料。物品提示说明可用 <ItemLink id="minecraft:lava_bucket" /> 补充，也可使用 <ItemLink id="create:spout" />。使用 <KeyBind id="key.rocketnautics.toggle_jetpack" /> 切换个人飞行功能。模组默认按键为 G。不需要飞行时关闭此功能可节省燃料，不会关闭加压供气。

<ItemLink id="rocketnautics:jetpack" />

***

## 密封飞船舱室

<EmiSearch query="@cosmonauticsdeepair" /> <EmiSearch query="@create_submarine" />

<ItemGrid>
  <ItemIcon id="create_submarine:electrolyzer" />
  <ItemIcon id="create_submarine:oxygene_diffuser" />
  <ItemIcon id="cosmonauticsdeepair:gravity_generator" />
</ItemGrid>

<ItemLink id="create_submarine:electrolyzer" />

<Recipe id="create_submarine:electrolyzer" />

使用 Deep Seas 舱室工具，在 Sable 飞船内部建造完好密封的房间。电解器需要水与 Forge Energy 才能制氧。将氧气供给连接到密封房间内的氧气扩散器。扩散器的储罐必须有氧气，并且方块要接收红石信号。Deep Air 会让密封、未破损且充满氧气的舱室中的实体恢复呼吸。它不会生成氧气，也不会修补船体。

<ItemLink id="create_submarine:oxygene_diffuser" />

<Recipe id="create_submarine:oxygen_diffuser" />

若要恢复该舱室中的重力，请在舱室内放置重力发生器，为其提供 Forge Energy，并在旁边提供红石信号。仅在它位于 Sable 子空间且同时满足信号与能量条件时才将其视为已启动。供氧用于呼吸。重力需要单独启动的重力发生器，但不需要氧气供应。

<ItemLink id="cosmonauticsdeepair:gravity_generator" />

<Recipe id="cosmonauticsdeepair:gravity_generator" />


Deep Air 会读取 Deep Seas 的密封舱室与氧气扩散器状态。保持舱室完好，并持续供氧。电解器与氧气扩散器的 Ponder 演示会说明供能、氧气和红石信号要求。

- [轨道飞行](space.vehicle-transfer.md) 建造并驾驶物理飞船。
- [太空目的地](space.destinations.md) 查看月球与火星目的地。

***

## 个人移动装备

<ItemGrid>
  <ItemIcon id="rocketnautics:copper_leg_thrusters" />
  <ItemIcon id="rocketnautics:copper_anchor_boots" />
</ItemGrid>

<ItemLink id="rocketnautics:copper_leg_thrusters" /> 消耗加压空气来提供飞行与惯性阻尼。使用 <KeyBind id="key.rocketnautics.toggle_dampeners" /> 切换阻尼，模组默认按键为 Z。

<Recipe id="rocketnautics:crafting/equipment/copper_leg_thrusters" />

<ItemLink id="rocketnautics:copper_anchor_boots" /> 可帮助你靠近支撑地板时保持落地。它们不会为整个房间生成重力，也不会将正在飞行的玩家压向地面。

<Recipe id="rocketnautics:crafting/equipment/copper_anchor_boots" />


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Cosmonautics: Deep Air](space.life-support.md) | 将 Deep Seas 密封舱室连接到太空呼吸与供能人工重力功能。 | <EmiSearch query="@cosmonauticsdeepair" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| ![Create Deep Seas](images/catalog-mva5q4qz.png) [Create Deep Seas](vehicles.water.md) | 为 Aeronautics 船只与潜艇增加水上及水下航行部件。 | <EmiSearch query="@create_submarine" /> |
