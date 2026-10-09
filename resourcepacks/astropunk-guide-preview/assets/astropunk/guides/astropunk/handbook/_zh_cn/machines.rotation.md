---
navigation:
  title: "为机器提供旋转动力"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
---

# 为机器提供旋转动力

## 动力源与传动

<ItemGrid>
  <ItemIcon id="create:water_wheel" />
  <ItemIcon id="create:large_water_wheel" />
  <ItemIcon id="create:windmill_bearing" />
  <ItemIcon id="create:steam_engine" />
  <ItemIcon id="create:shaft" />
  <ItemIcon id="create:cogwheel" />
  <ItemIcon id="create:gearbox" />
  <ItemIcon id="create_connected:cross_connector" />
  <ItemIcon id="create_connected:parallel_gearbox" />
  <ItemIcon id="create_connected:six_way_gearbox" />
  <ItemIcon id="create_connected:brass_gearbox" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create:water_wheel" />, <ItemLink id="create:large_water_wheel" />, <ItemLink id="create:windmill_bearing" />, <ItemLink id="create:steam_engine" /> | Create 提供水力、风力与蒸汽旋转动力。 |
| <ItemLink id="create:shaft" />, <ItemLink id="create:cogwheel" />, <ItemLink id="create:gearbox" /> | 传动杆、齿轮与齿轮箱传动。 |
| <ItemLink id="create_connected:cross_connector" />, <ItemLink id="create_connected:parallel_gearbox" />, <ItemLink id="create_connected:six_way_gearbox" />, <ItemLink id="create_connected:brass_gearbox" /> | Create: Connected 提供独立交叉传动、平行传动、六面连接与可用扳手配置的输出方向。 |

***

## 离合器与控制

<ItemGrid>
  <ItemIcon id="create_connected:inverted_clutch" />
  <ItemIcon id="create_connected:inverted_gearshift" />
  <ItemIcon id="create_connected:centrifugal_clutch" />
  <ItemIcon id="create_connected:freewheel_clutch" />
  <ItemIcon id="create_connected:overstress_clutch" />
  <ItemIcon id="create_connected:brake" />
  <ItemIcon id="create_connected:shear_pin" />
  <ItemIcon id="create_connected:kinetic_bridge" />
  <ItemIcon id="create_connected:encased_chain_cogwheel" />
  <ItemIcon id="create_connected:crank_wheel" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create_connected:inverted_clutch" />, <ItemLink id="create_connected:inverted_gearshift" /> | 红石启用型离合器与反向齿轮换向器。 |
| <ItemLink id="create_connected:centrifugal_clutch" />, <ItemLink id="create_connected:freewheel_clutch" />, <ItemLink id="create_connected:overstress_clutch" /> | 按转速阈值或方向接通，或在应力过载时断开。 |
| <ItemLink id="create_connected:brake" />, <ItemLink id="create_connected:shear_pin" /> | 制动器与剪切销保护组件。 |
| <ItemLink id="create_connected:kinetic_bridge" />, <ItemLink id="create_connected:encased_chain_cogwheel" />, <ItemLink id="create_connected:crank_wheel" /> | 紧凑动力桥接器、链式传动与手动曲柄轮。 |

***

## 初次使用

### 基础传动

<Recipe id="create:crafting/kinetics/shaft" />

两个 <ItemLink id="create:andesite_alloy" /> 可制作八个 <ItemLink id="create:shaft" />。

### 基础动力源

<Recipe id="create:crafting/kinetics/water_wheel" />

制作 <ItemLink id="create:water_wheel" />，为第一台机器提供动力。水流布局请查看对应的思索演示。

### 机器工具

<Recipe id="create:crafting/kinetics/wrench" />

调整机械动力组件时，准备好 <ItemLink id="create:wrench" />。

从水车、传动杆和一台机器开始。排列与转向请查看对应组件的思索演示。需要单独控制分支时再增加离合器。动力储备见旋转动力储存。

- [旋转动力储存](power.stored-rotation.md)


***

## 相关模组

| 模组或内容 | 状态 | 英文官方简介 |
| --- | --- | --- |
| ![Create: Connected](images/create-connected-icon.png) [Create: Connected](machines.rotation.md) | 已安装基准版 | QoL blocks that you wish existed in Create - Highly configurable, disable what you don't need |
