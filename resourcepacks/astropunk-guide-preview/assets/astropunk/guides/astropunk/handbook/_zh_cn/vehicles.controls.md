---
navigation:
  title: "控制与稳定载具"
  position: 0
  parent: reference.vehicles.md
  icon: minecraft:minecart
---

# 控制与稳定载具

## 驾驶舱控制

<EmiSearch query="@aeroworks" />

<ItemGrid>
  <ItemIcon id="aeroworks:control_desk" />
  <ItemIcon id="aeroworks:joystick_module" />
  <ItemIcon id="aeroworks:throttle_quadrant_module" />
  <ItemIcon id="aeroworks:wheel_module" />
  <ItemIcon id="aeroworks:mechanical_servo" />
  <ItemIcon id="aeroworks:stepper_servo" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="aeroworks:control_desk" /> |
| <ItemLink id="aeroworks:joystick_module" /> |
| <ItemLink id="aeroworks:throttle_quadrant_module" /> |
| <ItemLink id="aeroworks:wheel_module" /> |
| <ItemLink id="aeroworks:mechanical_servo" /> |
| <ItemLink id="aeroworks:stepper_servo" /> |

Aeroworks 控制台支持方向盘、操纵杆、油门、踏板、拉杆、键盘与按钮面板模块。手持模块右键插槽进行安装，使用扳手拆除。潜行并右键配置各模块及其红石链路频率。空手右键接管，Escape 释放。相接的控制台构成同一控制台组，同时只能由一名玩家操作。

***

## 信号与传感器

<EmiSearch query="@create_tweaked_controllers" />

<ItemGrid>
  <ItemIcon id="simulated:steering_wheel" />
  <ItemIcon id="simulated:throttle_lever" />
  <ItemIcon id="simulated:altitude_sensor" />
  <ItemIcon id="simulated:velocity_sensor" />
  <ItemIcon id="simulated:gimbal_sensor" />
  <ItemIcon id="aeroworks:gyroscope" />
  <ItemIcon id="create_tweaked_controllers:tweaked_linked_controller" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="simulated:steering_wheel" /> |
| <ItemLink id="simulated:throttle_lever" /> |
| <ItemLink id="simulated:altitude_sensor" /> |
| <ItemLink id="simulated:velocity_sensor" /> |
| <ItemLink id="simulated:gimbal_sensor" /> |
| <ItemLink id="aeroworks:gyroscope" /> |
| <ItemLink id="create_tweaked_controllers:tweaked_linked_controller" /> |

方向与油门控制件提供手动输入，传感器报告高度、速度与万向状态。Aeroworks 增加陀螺仪和伺服器，Tweaked Linked Controllers 提供手持界面。信号行为请看控制台与伺服器思索演示。这些部件不会自行生成自动飞行程序。

***

## 接收器与驾驶舱设备

<EmiSearch query="@aeroengineering" />

<ItemGrid>
  <ItemIcon id="simulated:directional_linked_receiver" />
  <ItemIcon id="simulated:modulating_linked_receiver" />
  <ItemIcon id="simulated:optical_sensor" />
  <ItemIcon id="simulated:laser_sensor" />
  <ItemIcon id="aeroengineering:engine_monitor_helmet" />
  <ItemIcon id="aeroengineering:hud_display" />
  <ItemIcon id="aeroengineering:folding_landing_gear_bearing" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="simulated:directional_linked_receiver" /> |
| <ItemLink id="simulated:modulating_linked_receiver" /> |
| <ItemLink id="simulated:optical_sensor" /> |
| <ItemLink id="simulated:laser_sensor" /> |
| <ItemLink id="aeroengineering:engine_monitor_helmet" /> |
| <ItemLink id="aeroengineering:hud_display" /> |
| <ItemLink id="aeroengineering:folding_landing_gear_bearing" /> |

链接接收器与光学、激光传感器扩展控制线路。Aero Engineering 的座舱设备提供监测与起落架控制。按键与绑定请看物品帮助，座舱显示需要已链接的监测目标。

***

## 制作

<Recipe id="aeroworks:throttle_quadrant_module" />

## 相关物品

<EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:wrench" />
  <ItemIcon id="create:redstone_link" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create:wrench" /> |
| <ItemLink id="create:redstone_link" /> |

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create: Aeroworks](images/catalog-P26k79kP.png) [Create: Aeroworks](vehicles.controls.md) | 为 Aeronautics 载具增加陀螺仪与操纵杆等飞行控制部件。 | 已安装基准版 | <EmiSearch query="@aeroworks" /> |
| ![Create: Tweaked Controllers](images/catalog-H6bJ8Ju4.png) [Create: Tweaked Controllers](vehicles.controls.md) | 为机械动力运动结构增加高级手持控制器。 | 已安装基准版 | <EmiSearch query="@create_tweaked_controllers" /> |
