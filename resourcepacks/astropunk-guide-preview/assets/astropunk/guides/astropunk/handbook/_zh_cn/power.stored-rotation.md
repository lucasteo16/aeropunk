---
navigation:
  title: "储存旋转动力"
  position: 4
  parent: reference.machines-storage.md
  icon: create:flywheel
---

# 储存旋转动力

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Springs+rotational+spring+kinetic+battery+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Springs+%E6%97%8B%E8%BD%AC%E5%BC%B9%E7%B0%A7+%E5%8A%A8%E5%8A%9B%E7%94%B5%E6%B1%A0+%E6%95%99%E7%A8%8B)

## 旋转储备

<EmiSearch query="@create_connected" /> <EmiSearch query="@create" />

<ItemLink id="create_connected:kinetic_battery" /> 储存应力容量。未通红石时，它从正面输入抽取应力充能。接入红石后，它按设定的容量与转速放电。界面与比较器可读充能。其他动力源满足需求时，电池不会放电，但电池运输物品的传送带仍有少量消耗，这是其 Ponder 中说明的情况。

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="create_connected:kinetic_battery" /> | <ItemGrid><ItemIcon id="create_connected:kinetic_battery" /></ItemGrid> | 储存并输出应力容量 |
| <ItemLink id="create_connected:kinetic_bridge" /> | <ItemGrid><ItemIcon id="create_connected:kinetic_bridge" /></ItemGrid> | 在独立网络之间传递容量 |
| <ItemLink id="create:stressometer" /> | <ItemGrid><ItemIcon id="create:stressometer" /></ItemGrid> | 读取网络应力 |
| <ItemLink id="create:analog_lever" /> | <ItemGrid><ItemIcon id="create:analog_lever" /></ItemGrid> | 红石控制 |

1. 把电池正面接到正在运行的动力源，保持未通红石以充能。
2. 接入红石放电，对比储能与网络运行情况。
3. 要在电池间转移电量，给正在充能的电池右键另一块电池以使其放电，或给正在放电的电池右键已充能电池来转移电量。机械手与机械臂可自动操作。

电池作为物品时也会保留电量。串联电池可延长放电时间，并联则提高总应力容量。实际消耗取决于正在使用的应力容量，不要把电池当作固定时长的电源。

***

## 弹簧储存旋转动力

<EmiSearch query="@createsprings" />

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Springs+1.2+spring+charging+large+spring+tools+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Create+Springs+%E5%BC%B9%E7%B0%A7+%E5%85%85%E8%83%BD+%E5%A4%A7%E5%9E%8B%E5%BC%B9%E7%B0%A7+%E5%B7%A5%E5%85%B7+%E6%95%99%E7%A8%8B)

弹簧储存旋转动力。任一输入方向都能为它充能。红石会释放储存的动力，信号强度控制输出转速，刚度控制充能。用绊线钩可在旋转输出与飞溅模式之间切换，空手使用会切回旋转模式。

| 弹簧系统 | 外观 | 操作 |
| --- | --- | --- |
| <ItemLink id="createsprings:spring" /> | <ItemGrid><ItemIcon id="createsprings:spring" /></ItemGrid> | 由旋转充能，红石放电 |
| <ItemLink id="createsprings:large_spring_coil" /> | <ItemGrid><ItemIcon id="createsprings:large_spring_coil" /></ItemGrid> | 大弹簧由同向线圈组成，端面为三乘三，内部再加空心环 |
| <ItemLink id="createsprings:kinetic_interface" /> | <ItemGrid><ItemIcon id="createsprings:kinetic_interface" /></ItemGrid> | 一对接口相隔一格，可操作移动结构上的弹簧 |
| <ItemLink id="createsprings:spring_base" /> | <ItemGrid><ItemIcon id="createsprings:spring_base" /></ItemGrid> | 弹簧动力工具的底座 |

| 弹簧装置 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="createsprings:spring_catapult" /> | <ItemGrid><ItemIcon id="createsprings:spring_catapult" /></ItemGrid> | 放置前选好目标，放入物品并供旋转。没有目标时不会工作 |
| <ItemLink id="createsprings:spring_drill" /> | <ItemGrid><ItemIcon id="createsprings:spring_drill" /></ItemGrid> | 弹簧动力钻具 |
| <ItemLink id="createsprings:spring_saw" /> | <ItemGrid><ItemIcon id="createsprings:spring_saw" /></ItemGrid> | 弹簧动力锯具 |
| <ItemLink id="createsprings:spring_shove" /> | <ItemGrid><ItemIcon id="createsprings:spring_shove" /></ItemGrid> | 弹簧动力铲具 |
| <ItemLink id="createsprings:spring_fan" /> | <ItemGrid><ItemIcon id="createsprings:spring_fan" /></ItemGrid> | 弹簧动力便携风扇 |
| <ItemLink id="createsprings:spring_launcher" /> | <ItemGrid><ItemIcon id="createsprings:spring_launcher" /></ItemGrid> | 发射弹簧物品与方块 |
| <ItemLink id="createsprings:punchcard" /> | <ItemGrid><ItemIcon id="createsprings:punchcard" /></ItemGrid> | 为支持的工具编程 |
| <ItemLink id="createsprings:portative_steam_engine" /> | <ItemGrid><ItemIcon id="createsprings:portative_steam_engine" /></ItemGrid> | 带燃料、水与压力控制的便携蒸汽引擎 |

1. 将弹簧接到正在运转的轴上，先不要接入红石。两个旋转方向都能充能。接入红石后释放储存的旋转动力，信号强度决定输出转速。
2. 制作便携工具时，在物品栏中把已充能弹簧叠放到弹簧底座或支持的弹簧工具上。底座、钻头、锯、铲和风扇都最多容纳两根弹簧。挖掘或采集速度取决于工具转速。
3. 潜行右键穿孔卡以打开指令界面，选择执行工具和触发条件，再把卡叠放到兼容工具上。它负责动作编程，不负责储能。
4. 手持弹簧弹射器潜行右键选定目标，再放置、提供旋转动力并投入物品。没有选定目标时不会发射。

便携蒸汽引擎的界面由当前绑定的引擎界面按键打开。将熔炉燃料放入燃料槽，并随身携带水桶以补充水。模式决定支持的充能或工具加速功能。超速模式会增加压力，压力达到一百时引擎会爆炸，因此要观察压力表，不要一直开启超速。

<ItemGrid><ItemIcon id="createsprings:friction_welder" /><ItemIcon id="createsprings:spring_alloy" /><ItemIcon id="createsprings:unfinished_spring" /></ItemGrid>

摩擦焊接器通过两台焊接器之间的转速差加工中间的方块。弹簧合金和未完成弹簧的配方可在配方浏览器中查询，不要把这些原料当成已充能工具。

穿孔卡配置支持工具的操作指令，不储存旋转动力。便携蒸汽引擎是独立的随身引擎，不是弹簧。轴与网络应力见[旋转动力](machines.rotation.md)。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Springs](images/create-springs-icon.png) [Create: Springs](power.stored-rotation.md) | 将旋转动力存入弹簧，供之后释放使用。 | <EmiSearch query="@createsprings" /> |
