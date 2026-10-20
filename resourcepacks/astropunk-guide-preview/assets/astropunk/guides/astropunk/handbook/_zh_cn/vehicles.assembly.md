---
navigation:
  title: "组装和操作移动载具"
  position: 4
  parent: reference.vehicles.md
  icon: create:mechanical_bearing
---

# 组装和操作移动载具

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Aeronautics+Sable+Simulated+assembler+glue+vehicle+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Aeronautics+Sable+%E8%BD%BD%E5%85%B7+%E7%BB%84%E8%A3%85%E5%99%A8+%E8%83%B6+%E6%95%99%E7%A8%8B)

## 组装顺序

<EmiSearch query="@create" />

![Cloud Skipper 飞艇成品](images/visual-assembled-airship.png)

<ItemGrid><ItemIcon id="simulated:physics_assembler" /><ItemIcon id="simulated:honey_glue" /><ItemIcon id="create:super_glue" /><ItemIcon id="simulated:contraption_diagram" /><ItemIcon id="simulated:navigation_table" /></ItemGrid>

<Recipe id="simulated:physics_assembler" />

<Recipe id="offroad:borehead_bearing" />

Sable 载具最初是普通的相连方块。第一艘只做小船体、可到达的驾驶位和一次移动测试需要的设备。列车使用[铁路建造](transport.railway-builder.md)中的车站流程，不使用这里的组装器。

1. 在远离地形和无关建筑的位置搭建相连船体，需要连接部件时使用 <ItemLink id="create:super_glue" />。
2. 将 <ItemLink id="simulated:physics_assembler" /> 放在目标结构旁，使用组装操作。确认预期船体完整地成为一个可移动子层级，没有把码头方块带进去。
3. 先确认组装体能移动、控制位可到达，再安装[飞艇](vehicles.airships.md)、[水下航行](vehicles.water.md)或[太空飞行](space.vehicle-transfer.md)设备。
4. 改建前把载具移到有支撑且周围空旷的位置，通过组装器拆回方块。最初使用的组装器不必一直留在船上。

不要把载具粘在发射台上。漏掉部件或把地形一起组装进去，是组装问题，不应靠加大发动机来补偿。

## 飞行之前先移动实体

新实体从一块方块开始。先组装这一块，再把其余部分直接建造在已组装的方块上，这样从第一块起所有部件就属于同一个物理实体，不必事后补胶。

<ItemGrid><ItemIcon id="simulated:iron_handle" /><ItemIcon id="simulated:physics_assembler" /><ItemIcon id="simulated:honey_glue" /></ItemGrid>

小实体可以用手打走，但体积越大质量越高，所以装上 <ItemLink id="simulated:iron_handle" />，潜行使用即可拖曳到想要的位置。先拖到位再补完船体，因为半成品比成品轻。

阶梯状的斜面会自动连在一起，不需要每一级都补一条胶。任何方向都连不上的部件会脱离成独立实体，飞行中粘合处断裂在地面上看到的就是这个样子。

## 连接与分离

### 对接

<ItemGrid><ItemIcon id="simulated:docking_connector" /></ItemGrid>

### 绳索与连接

<ItemGrid><ItemIcon id="simulated:rope_winch" /><ItemIcon id="simulated:rope_connector" /><ItemIcon id="simulated:rope_coupling" /></ItemGrid>

### 合并与活动连接

<ItemGrid><ItemIcon id="minecraft:slime_ball" /><ItemIcon id="simulated:swivel_bearing" /><ItemIcon id="simulated:spring" /></ItemGrid>

两个实体在合并前保持独立。使用 <ItemLink id="minecraft:slime_ball" /> 选择并合并模拟结构，潜行使用可清除选择。一个实体的连接被破坏后，断开的部分可以分离成独立实体。

对接连接器把移动实体接到固定结构上。绳索部件用来拖曳和系留，万向轴承与弹簧则吸收两个实体之间的相对运动，不让这股力直接传进骨架。

| 部件 | 连接对象 | 用途 |
| --- | --- | --- |
| <ItemLink id="simulated:docking_connector" /> | 移动实体与固定码头 | 飞艇系泊、驳船装卸 |
| <ItemLink id="simulated:rope_winch" /> 与 <ItemLink id="simulated:rope_connector" /> | 绳索两端的固定点 | 拖曳与固定货物 |
| <ItemLink id="simulated:swivel_bearing" /> | 需要相对转动的两个实体 | 拖挂车厢、摆动挂架 |
| <ItemLink id="simulated:spring" /> | 需要拉开又回位的两个实体 | 悬挂与减震 |

## 轮子

<ItemGrid><ItemIcon id="offroad:wheel_mount" /><ItemIcon id="offroad:small_tire" /><ItemIcon id="offroad:tire" /><ItemIcon id="offroad:large_tire" /><ItemIcon id="offroad:monstrous_tire" /><ItemIcon id="offroad:borehead_bearing" /></ItemGrid>

<ItemLink id="offroad:wheel_mount" /> 只接受装在前面的一个轮胎。装在别的面上会被拒绝，所以要对准背向底盘的那一面。轮架只承重，不提供动力，会滚的底盘仍然需要螺旋桨、推进器或发动机，以及转向输入。

<ItemLink id="offroad:borehead_bearing" /> 带动挖掘刀头，属于作业附件，不是轮子。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Aeronautics](images/catalog-owak0q19.png) [Create Aeronautics](vehicles.assembly.md) | 将方块搭建的载具变成可操控的物理移动结构。 | 无独立物品查询 |
