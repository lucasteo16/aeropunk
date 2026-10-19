---
navigation:
  title: "控制与稳定载具"
  position: 5
  parent: reference.vehicles.md
  icon: create:controls
---

# 控制与稳定载具

## 控制台与模块

<EmiSearch query="@aeroworks" /> <EmiSearch query="@create" />

![装有 Aeroworks 控制模块的驾驶舱](images/visual-cockpit-controls.png)

装有 Aeroworks 控制模块的驾驶舱

<ItemGrid><ItemIcon id="aeroworks:control_desk" /><ItemIcon id="aeroworks:joystick_module" /><ItemIcon id="aeroworks:throttle_quadrant_module" /><ItemIcon id="aeroworks:wheel_module" /><ItemIcon id="aeroworks:lever_module" /><ItemIcon id="aeroworks:pedal_module" /><ItemIcon id="aeroworks:button_panel_module" /><ItemIcon id="create:redstone_link" /><ItemIcon id="create:wrench" /></ItemGrid>

<ItemLink id="aeroworks:control_desk" /> 是一块插槽板。手持模块右键插槽即可装上，用扳手可以取下。取下的模块保留设置，调好的摇杆可以直接换到另一艘船上。

潜行使用已放置的控制件可以打开配置，按键、红石链接频率和模块选项都在这里设置。手持模块时潜行使用空气即可配置该模块。同一控制台可以装多个模块，小模块也能装进大插槽。

空手右键控制台即可接管。此后键盘和鼠标会带动已安装的控制件，每个方向都在各自的红石链接频率上发送信号，强度随推动幅度变化。按 Escape 放开控制。

相邻的控制台会组成一个操控台组。同一时间只有一名玩家能控制一个操控台组，隔开摆放的控制台则是独立工位。驾驶座和节流工位并排时因此像同一个驾驶舱一样工作。

## 伺服机构

<ItemGrid><ItemIcon id="aeroworks:mechanical_servo" /><ItemIcon id="aeroworks:stepper_servo" /><ItemIcon id="aeroworks:gyroscope" /></ItemGrid>

伺服机构把红石信号还原成轴的角度，控制台通道就是这样带动舵面的。

| 部件 | 信号到角度 | 方块上的设置 |
| --- | --- | --- |
| <ItemLink id="aeroworks:mechanical_servo" /> | 在设定范围内按信号强度成比例转动 | 右键设置转动范围 |
| <ItemLink id="aeroworks:stepper_servo" /> | 分级转动，每个信号等级走一档 | 右键设置每档角度 |

两者都会先转完当前动作再响应新信号，所以输入变化快时会慢一个动作，而不是直接跳过去。步进伺服两侧都能接收信号，一侧正转一侧反转，两侧同时通电则原地保持。<ItemLink id="aeroworks:gyroscope" /> 用于保持机体水平，属于稳定装置，不是输入装置。

## 传感器与接收器

<EmiSearch query="@create_tweaked_controllers" />

<ItemGrid><ItemIcon id="simulated:steering_wheel" /><ItemIcon id="simulated:throttle_lever" /><ItemIcon id="simulated:altitude_sensor" /><ItemIcon id="simulated:velocity_sensor" /><ItemIcon id="simulated:gimbal_sensor" /><ItemIcon id="simulated:directional_linked_receiver" /><ItemIcon id="simulated:optical_sensor" /><ItemIcon id="simulated:laser_sensor" /><ItemIcon id="create_tweaked_controllers:tweaked_linked_controller" /><ItemIcon id="simulated:modulating_linked_receiver" /></ItemGrid>

手动输入是你去转的方块，传感器是替你读数的方块。

| 部件 | 作用 | 读取方式 |
| --- | --- | --- |
| <ItemLink id="simulated:steering_wheel" /> | 连续转向输入 | 右键拖动 |
| <ItemLink id="simulated:throttle_lever" /> | 连续油门输入 | 右键拖动 |
| <ItemLink id="simulated:altitude_sensor" /> | 按高度输出红石强度，上下限在界面里设定 | 戴工程师护目镜可读气压与精确高度 |
| <ItemLink id="simulated:velocity_sensor" /> | 相对速度，以及靠近或远离方向 | 打开界面 |
| <ItemLink id="simulated:gimbal_sensor" /> | 两个轴上的倾斜角 | 打开界面 |
| <ItemLink id="simulated:optical_sensor" /> | 探测到的方块与距离 | 打开界面 |
| <ItemLink id="simulated:laser_sensor" /> | 沿直线测距 | 打开界面 |

高度传感器默认越高输出越强，也可以反过来，这是不用程序就能守住某一高度层的常用做法。接收器把控制台或链接的通道送到船体远端，不必让线缆穿过整个外壳。

## 合成

<EmiSearch query="@aeroengineering" />

<ItemGrid><ItemIcon id="aeroengineering:engine_monitor_helmet" /><ItemIcon id="aeroengineering:folding_landing_gear_bearing" /><ItemIcon id="aeroengineering:hud_display" /></ItemGrid>

<Recipe id="aeroworks:throttle_quadrant_module" />


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Aeroworks](images/catalog-p26k79kp.png) [Create: Aeroworks](vehicles.controls.md) | 为 Aeronautics 载具增加陀螺仪与操纵杆等飞行控制部件。 | <EmiSearch query="@aeroworks" /> |
| ![Create: Tweaked Controllers](images/catalog-h6bj8ju4.png) [Create: Tweaked Controllers](vehicles.controls.md) | 为机械动力运动结构增加高级手持控制器。 | <EmiSearch query="@create_tweaked_controllers" /> |
