---
navigation:
  title: "组装和操作移动载具"
  position: 4
  parent: reference.vehicles.md
  icon: create:mechanical_bearing
---

# 组装和操作移动载具

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Aeronautics+Vehicle+assembly+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Aeronautics+%E7%BB%84%E8%A3%85%E5%92%8C%E6%93%8D%E4%BD%9C%E7%A7%BB%E5%8A%A8%E8%BD%BD%E5%85%B7+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 组装顺序

<EmiSearch query="@create" />

![Cloud Skipper 飞艇成品](images/visual-assembled-airship.png)

Cloud Skipper 飞艇成品

<ItemGrid><ItemIcon id="simulated:physics_assembler" /><ItemIcon id="simulated:honey_glue" /><ItemIcon id="create:super_glue" /><ItemIcon id="simulated:contraption_diagram" /><ItemIcon id="simulated:navigation_table" /></ItemGrid>

模拟悬浮体是把一组方块变成单一物理实体。先造形状，再涂胶，最后组装。

1. 先在原地造好船体、甲板和挂点，轮子、轴承与动力装置也要提前装好。
2. 用 <ItemLink id="create:super_glue" /> 或 <ItemLink id="simulated:honey_glue" /> 标记整体。胶水按面连接，所以船体要粘到甲板，甲板要粘到机械。
3. 把 <ItemLink id="simulated:physics_assembler" /> 贴在结构上，对着它长按使用，然后拉下扳手。

斜边上的方块会被一并纳入，阶梯状船体不需要每一级都补一条胶。首次组装用过的组装器之后不再需要，任意一台组装器都能把实体重新拆开。

| 提示 | 含义 | 处理 |
| --- | --- | --- |
| Cannot disassemble onto the same Simulated Contraption! | 组装器本身属于要拆开的实体 | 把组装器移出实体 |
| Too fast to disassemble! | 实体还在移动 | 先停稳再试 |
| Too far from the ground to disassemble! | 实体太高，方块放不回地面 | 降低高度或在实地上方组装 |
| Could not align Simulated Contraption to disassemble! | 保存的布局已经放不回原空间 | 清空落点区域 |

<Recipe id="simulated:physics_assembler" />

<Recipe id="offroad:borehead_bearing" />
## 飞行之前先移动实体

新实体从一块方块开始。先组装这一块，再把其余部分直接建造在已组装的方块上，这样从第一块起所有部件就属于同一个物理实体，不必事后补胶。

<ItemGrid><ItemIcon id="simulated:iron_handle" /><ItemIcon id="simulated:physics_assembler" /><ItemIcon id="simulated:honey_glue" /></ItemGrid>

小实体可以用手打走，但体积越大质量越高，所以装上 <ItemLink id="simulated:iron_handle" />，潜行使用即可拖曳到想要的位置。先拖到位再补完船体，因为半成品比成品轻。

阶梯状的斜面会自动连在一起，不需要每一级都补一条胶。任何方向都连不上的部件会脱离成独立实体，飞行中粘合处断裂在地面上看到的就是这个样子。

## 连接与分离

<ItemGrid><ItemIcon id="simulated:docking_connector" /><ItemIcon id="simulated:paired_docking_connector" /><ItemIcon id="simulated:rope_winch" /><ItemIcon id="simulated:rope_connector" /><ItemIcon id="simulated:rope_coupling" /><ItemIcon id="simulated:merging_glue" /><ItemIcon id="simulated:swivel_bearing" /><ItemIcon id="simulated:spring" /></ItemGrid>

两个实体默认各自独立。黏液球能把任意两个模拟悬浮体合并，<ItemLink id="simulated:merging_glue" /> 则跨过两个实体之间的空隙涂胶。同一实体的断开部分会自行分离，飞行中粘合处被破坏时就是这样。

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
