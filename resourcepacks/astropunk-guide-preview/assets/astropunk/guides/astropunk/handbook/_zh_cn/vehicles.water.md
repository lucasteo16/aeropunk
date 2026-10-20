---
navigation:
  title: "操作船只与潜艇"
  position: 3
  parent: reference.vehicles.md
  icon: minecraft:oak_boat
---

# 操作船只与潜艇

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Deep+Seas+3+submarine+ballast+oxygen+diffuser+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Deep+Seas+%E6%BD%9C%E8%89%87+%E5%8E%8B%E8%BD%BD+%E6%B0%A7%E6%B0%94%E6%89%A9%E6%95%A3%E5%99%A8+%E6%95%99%E7%A8%8B)

## 船体

<EmiSearch query="@create" />

![Deep Seas 铜制潜艇](images/building-travel-submarine.png)

Deep Seas 铜制潜艇。

潜艇是作为模拟悬浮体建造的密闭船体，然后装上压载、推进与空气系统。组装方法见[组装](vehicles.assembly.md)。船体决定你能潜多深，所以耐压玻璃要在第一次下潜前装好，而不是之后补。

### 浮力与压载

<EmiSearch query="@create_submarine" />

<ItemGrid><ItemIcon id="create_submarine:floater" /><ItemIcon id="create_submarine:ballast_tank" /><ItemIcon id="create_submarine:ballast_vent" /></ItemGrid>

### 推进与转向

<ItemGrid><ItemIcon id="create_submarine:water_thruster" /><ItemIcon id="create_submarine:submarine_propeller" /><ItemIcon id="create_high_seas:rudder" /></ItemGrid>

### 甲板与压力设备

<ItemGrid><ItemIcon id="create_submarine:arresting_hook" /><ItemIcon id="create_submarine:decompression_chamber" /></ItemGrid>

### 水面小船

<EmiSearch query="@starcatcher" />

<ItemGrid><ItemIcon id="minecraft:oak_boat" /><ItemIcon id="starcatcher:oak_tackle_box_boat" /></ItemGrid>

<ItemLink id="create_submarine:floater" /> 让水面船保持浮起。它是浮体，不是下潜控制。

## 下潜与上浮

<Recipe id="create_submarine:ballast_tank" />

下潜系统由 <ItemLink id="create_submarine:ballast_vent" />、一台泵和一个或多个 <ItemLink id="create_submarine:ballast_tank" /> 组成，用管道连接。

1. 放置排海口，至少有一面接触海水。接触不到海水就没有可抽的东西。
2. 用机械泵把需要的排海口各面接到压载舱。
3. 从排海口把水抽进压载舱即下潜。舱越满，潜艇越重。
4. 反转泵把水推回排海口。压载舱排空，潜艇上浮。

排海口本身不需要旋转力，也不需要红石。真正搬水的是泵，所以不转的泵等于一套什么也不做的压载系统。船上装有 <ItemLink id="create_submarine:pump_controller" /> 与船载计算机时，计算机会判断管路方向，并按你在屏幕上设定的目标深度驱动水泵。

## 推进与转向

<ItemGrid><ItemIcon id="create_submarine:underwater_mine" /></ItemGrid>

| 部件 | 需要 | 提供 |
| --- | --- | --- |
| <ItemLink id="create_submarine:water_thruster" /> | 水压与旋转力 | 随两者提升的推力 |
| <ItemLink id="create_submarine:submarine_propeller" /> | 旋转力 | 稳定的水下推进 |
| <ItemLink id="create_high_seas:rudder" /> | 转向输入 | 改变船体方向 |

<ItemLink id="create_submarine:water_thruster" /> 消耗加压水产生推力，需要供水与旋转力。压力越大、转速越高，推力越大。<ItemLink id="create_submarine:submarine_propeller" /> 是更简单的驱动，只在水中工作，空气中无效。<ItemLink id="create_high_seas:rudder" /> 是转向面。

水面船也可以用螺旋桨，但螺旋桨在空气里推不动任何东西。

## 空气与压力

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Deep+Seas+oxygen+electrolyzer+shaft+diffuser+redstone+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Deep+Seas+%E6%B0%A7%E6%B0%94+%E7%94%B5%E8%A7%A3%E6%9C%BA+%E4%BC%A0%E5%8A%A8%E8%BD%B4+%E6%89%A9%E6%95%A3%E5%99%A8+%E7%BA%A2%E7%9F%B3+%E6%95%99%E7%A8%8B)

<ItemGrid><ItemIcon id="create_submarine:electrolyzer" /><ItemIcon id="create_submarine:oxygene_diffuser" /><ItemIcon id="create_submarine:barometer" /><ItemIcon id="create_submarine:copper_pressurizer" /><ItemIcon id="create_submarine:iron_pressurizer" /><ItemIcon id="create_submarine:phycological_membrane" /></ItemGrid>

| 机器 | 输入 | 输出 |
| --- | --- | --- |
| <ItemLink id="create_submarine:electrolyzer" /> | 水与 Forge 能量，或在模块槽放入传动轴 | 氧气 |
| <ItemLink id="create_submarine:oxygene_diffuser" /> | 储存的氧气与红石信号 | 密闭舱内的可呼吸空气 |
| <ItemLink id="create_submarine:barometer" /> | 无 | 深度，以及相对最弱方块的水压 |

本包所选版本由负责该潜艇的活动扩散器每二十个游戏刻消耗五十毫桶氧气，并非按舱室体积成比例扣除。扩散器需要供氧与红石信号。大舱仍须密封，但增加扩散器不能代替修补破口。电解机模块槽可放入传动轴以使用旋转动力，再把产出的氧气送到扩散器。

气压计把外部压力与船体最弱的方块比较。继续下潜前先读它，修补船体后也要看它。铜制与铁制耐压玻璃是能承压的窗，<ItemLink id="create_submarine:phycological_membrane" /> 可以充入空气。

## 寻找航路

<ItemGrid><ItemIcon id="create_submarine:sonar" /><ItemIcon id="create_submarine:pump_controller" /><ItemIcon id="create_submarine:industrial_alarm" /><ItemIcon id="create_submarine:steel_cable" /><ItemIcon id="create_submarine:pulley" /></ItemGrid>

<ItemLink id="create_submarine:sonar" /> 绘制船体周围的海床、岩石、其他船只与水雷。同一艘船上装有船载计算机时，它会增加地图页面，并让自动驾驶沿着海床保持龙骨离地。

钢缆与相对放置的滑轮让子层级沿固定线路移动，更适合潜水钟或缆车，而不是自由航行的潜艇。<ItemLink id="create_submarine:industrial_alarm" /> 用于提醒船员，水雷属于武器而不是工具。

<Recipe id="create_submarine:electrolyzer" />

***


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Deep Seas](images/catalog-mva5q4qz.png) [Create Deep Seas](vehicles.water.md) | 为 Aeronautics 船只与潜艇增加水上及水下航行部件。 | <EmiSearch query="@create_submarine" /> |
