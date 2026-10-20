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

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Cosmonautics+space+helmet+air+jetpack+oxygen+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Cosmonautics+%E5%A4%AA%E7%A9%BA%E5%A4%B4%E7%9B%94+%E7%A9%BA%E6%B0%94+%E5%96%B7%E6%B0%94%E8%83%8C%E5%8C%85+%E6%95%99%E7%A8%8B)

## 呼吸装备

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

<ItemGrid><ItemIcon id="create:copper_diving_helmet" /><ItemIcon id="create:copper_backtank" /><ItemIcon id="rocketnautics:space_helmet" /><ItemIcon id="rocketnautics:jetpack" /><ItemIcon id="create:netherite_backtank" /></ItemGrid>

Cosmonautics 会检查深空及其配置大气区间内的生物是否能呼吸，借用 Create 潜水装备与储存空气，而不是另建一套舱室氧气模拟。发射前应装备兼容头盔并充满供气设备。舱室供氧来自下文的 Deep Seas 与 Deep Air 联动。

| 部件 | 槽位 | 提供 |
| --- | --- | --- |
| <ItemLink id="create:copper_diving_helmet" /> | 头部 | 从连接的空气源呼吸 |
| <ItemLink id="create:copper_backtank" /> | 胸部 | 储存空气，飞行前充满 |
| <ItemLink id="rocketnautics:space_helmet" /> | 头部 | 从加压源呼吸，并带轨道显示 |
| <ItemLink id="rocketnautics:jetpack" /> | 胸部 | 加压空气与个人推力 |

铜潜水头盔与充满空气的铜制背罐可作为能合成的起步组合。本包太空头盔没有合成配方，不是这套起步装备的必要条件。

<Recipe id="create:crafting/appliances/copper_diving_helmet" />

<Recipe id="create:crafting/appliances/copper_backtank" />
## 喷气背包

<Recipe id="rocketnautics:crafting/equipment/jetpack" />

<ItemGrid><ItemIcon id="rocketnautics:jetpack" /><ItemIcon id="minecraft:lava_bucket" /><ItemIcon id="create:spout" /></ItemGrid>

<ItemLink id="rocketnautics:jetpack" /> 燃烧燃料。手持熔岩桶按住替代键点击可以补充，也可以在 <ItemLink id="create:spout" /> 处灌装。按 <KeyBind id="key.rocketnautics.toggle_jetpack" /> 切换系统，按住跳跃可以短促向上推进。

穿在身上时，它还会向需要加压空气的装备供气，同时缓慢消耗燃料。这项消耗与飞行开关无关，所以在真空里久留会慢慢耗尽燃料，即使一次也没推进。

## 密闭舱室

<EmiSearch query="@cosmonauticsdeepair" /> <EmiSearch query="@create_submarine" />

![船舱内的重力设备](images/cosmo-gravity-room.png)

<ItemGrid><ItemIcon id="create_submarine:electrolyzer" /><ItemIcon id="create_submarine:oxygene_diffuser" /><ItemIcon id="cosmonauticsdeepair:gravity_generator" /></ItemGrid>

船可以自带空气。在船体内部造一个完整的密闭舱，然后给它供气。

| 机器 | 需要 | 提供 |
| --- | --- | --- |
| <ItemLink id="create_submarine:electrolyzer" /> | 水与 Forge 能量，或模块槽中的传动轴 | 氧气 |
| <ItemLink id="create_submarine:oxygene_diffuser" /> | 罐中氧气与红石信号 | 密闭舱内的可呼吸空气 |
| <ItemLink id="cosmonauticsdeepair:gravity_generator" /> | Forge 能量与相邻红石信号 | 舱内局部重力 |

Deep Air 在潜艇舱室供氧且密封时恢复呼吸，不负责封堵破口或制造氧气。本包所选 Deep Seas 扩散器按固定工作量消耗氧气，不是按舱室体积扣除。供氧管路与扩散器控制见[水下航行](vehicles.water.md)。离开舱室仍要携带个人呼吸装备。

重力发生器是另一项舱室功能。它与扩散器不必在同一舱，但至少要让一个舱保持供氧，舱室追踪才继续有效。

<Recipe id="cosmonauticsdeepair:gravity_generator" />

<Recipe id="create_submarine:oxygen_diffuser" />

<Recipe id="create_submarine:electrolyzer" />
## 个人移动

<ItemGrid><ItemIcon id="rocketnautics:copper_leg_thrusters" /><ItemIcon id="rocketnautics:copper_anchor_boots" /></ItemGrid>

<ItemLink id="rocketnautics:copper_leg_thrusters" /> 用加压空气提供飞行与惯性阻尼，在太空中的效率是地面的四倍，水下是两倍。按 <KeyBind id="key.rocketnautics.toggle_dampeners" /> 切换阻尼。

<ItemLink id="rocketnautics:copper_anchor_boots" /> 在主动飞行之外把你固定在可支撑的地面上。它不为其他人创造重力，在悬空处也不起作用。

<Recipe id="rocketnautics:crafting/equipment/copper_leg_thrusters" />

<Recipe id="rocketnautics:crafting/equipment/copper_anchor_boots" />


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Cosmonautics: Deep Air](images/cosmo-rzqxjxfo-icon.png) [Cosmonautics: Deep Air](space.life-support.md) | 将 Deep Seas 密封舱室连接到太空呼吸与供能人工重力功能。 | <EmiSearch query="@cosmonauticsdeepair" /> |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| ![Create Deep Seas](images/catalog-mva5q4qz.png) [Create Deep Seas](vehicles.water.md) | 为 Aeronautics 船只与潜艇增加水上及水下航行部件。 | <EmiSearch query="@create_submarine" /> |
