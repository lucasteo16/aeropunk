---
navigation:
  title: "储存旋转动力"
  position: 8
  parent: reference.machines-storage.md
  icon: create:flywheel
---

# 储存旋转动力

## 旋转用的蓄电池

<EmiSearch query="@create_connected" /> <EmiSearch query="@createsprings" /> <EmiSearch query="@create" />

<ItemLink id="create_connected:kinetic_battery" /> 把旋转存为应力，之后再放出来。没有红石信号时充电，通电时放电，因此由一只拉杆决定储备什么时候带动线路。

<ItemGrid><ItemIcon id="create_connected:kinetic_battery" /><ItemIcon id="create_connected:kinetic_bridge" /><ItemIcon id="create:stressometer" /><ItemIcon id="create:analog_lever" /><ItemIcon id="createsprings:kinetic_interface" /><ItemIcon id="createsprings:portative_steam_engine" /><ItemIcon id="createsprings:punchcard" /><ItemIcon id="createsprings:spring_base" /><ItemIcon id="createsprings:spring_catapult" /><ItemIcon id="createsprings:spring_drill" /><ItemIcon id="createsprings:spring_fan" /><ItemIcon id="createsprings:spring_launcher" /><ItemIcon id="createsprings:spring_saw" /><ItemIcon id="createsprings:spring_shove" /></ItemGrid>

| 部件 | 行为 |
| --- | --- |
| <ItemLink id="create_connected:kinetic_battery" /> | 无信号充电，有信号放电 |
| <ItemLink id="create_connected:kinetic_bridge" /> | 在两个独立网络之间转移容量 |
| <ItemLink id="create:stressometer" /> | 显示蓄电池对网络做了什么 |
| <ItemLink id="create:analog_lever" /> | 干净的放电开关 |

在当前版本中，蓄电池以物品形态保留电量，并且只释放网络实际需要的应力，因此可以把充满的蓄电池带到远处的工地，而不必在那里拉一条轴。容量、放电速度与应力消耗都可配置，不同整合包的数字因此可以不同。

***

## 弹簧用另一种方式存同样的东西

<ItemLink id="createsprings:spring" /> 储存旋转，按需释放。区别在控制方式。弹簧响应红石信号强度，因此比较器或模拟拉杆可以决定它释放多少、为什么释放。

<ItemGrid><ItemIcon id="createsprings:spring" /><ItemIcon id="createsprings:large_spring_coil" /><ItemIcon id="createsprings:spring_alloy" /><ItemIcon id="createsprings:unfinished_spring" /><ItemIcon id="createsprings:friction_welder" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="createsprings:spring_alloy" /> | 制作弹簧的材料 |
| <ItemLink id="createsprings:unfinished_spring" /> | 会成为弹簧的形态 |
| <ItemLink id="createsprings:friction_welder" /> | 把合金应用到未完成的弹簧上 |
| <ItemLink id="createsprings:large_spring_coil" /> | 更大储备用的大线圈 |

已发布的配方用摩擦焊接机把弹簧合金应用到未完成的弹簧上，而焊接机需要旋转。因此第一只弹簧是两步工程，这也是在需要一打弹簧之前就囤合金的理由。

弹簧释放的力量也能破坏方块。把溅射模式或任何高设定与普通储备分开，并且先用临时建筑测试设定。

***

## 三种储备怎么选

<ItemGrid><ItemIcon id="create_connected:kinetic_battery" /><ItemIcon id="createsprings:spring" /></ItemGrid>

| 储备 | 适合什么 |
| --- | --- |
| 动力蓄电池 | 同一网络上的紧凑缓冲，用红石切换 |
| 弹簧 | 按信号控制输出，把储备移动到需要的地方 |

蓄电池应对停转。弹簧应对变化的需求。多数基地只需要其中一个，区别在于储备该如何开启。

第一步是在一条已经在转的线上装蓄电池，并在放电侧装拉杆。电源停下时看应力表下降，同时看生产继续。

储备不会凭空创造容量。[旋转动力](machines.rotation.md)统一说明应力预算与转速规则。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Springs](images/create-springs-icon.png) [Create: Springs](power.stored-rotation.md) | 将旋转动力存入弹簧，供之后释放使用。 | <EmiSearch query="@createsprings" /> |
