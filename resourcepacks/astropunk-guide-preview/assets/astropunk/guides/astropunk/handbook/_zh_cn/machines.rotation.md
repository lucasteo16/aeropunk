---
navigation:
  title: "为机器提供旋转动力"
  position: 3
  parent: reference.machines-storage.md
  icon: create:cogwheel
---

# 为机器提供旋转动力

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+6+water+wheel+stress+stressometer+gearbox+gearshift+millstone+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+6+%E6%B0%B4%E8%BD%A6+%E5%BA%94%E5%8A%9B+%E5%BA%94%E5%8A%9B%E8%A1%A8+%E9%BD%BF%E8%BD%AE%E7%AE%B1+%E5%8F%98%E9%80%9F%E5%99%A8+%E7%9F%B3%E7%A3%A8+%E6%95%99%E7%A8%8B)

## 网络需要什么

<EmiSearch query="@create" />

旋转网络有来源提供的容量与机器产生的应力。应力低于容量时全部转动，超过容量就整条停住，直到负载降下来。

| 来源 | 外观 | 就位时的转速 | 该转速下的容量 |
| --- | --- | --- | --- |
| <ItemLink id="create:water_wheel" /> | <ItemGrid><ItemIcon id="create:water_wheel" /></ItemGrid> | 每分钟八转 | 256 应力单位 |
| <ItemLink id="create:large_water_wheel" /> | <ItemGrid><ItemIcon id="create:large_water_wheel" /></ItemGrid> | 每分钟四转 | 512 应力单位 |
| <ItemLink id="create:windmill_bearing" /> | <ItemGrid><ItemIcon id="create:windmill_bearing" /></ItemGrid> | 由帆组决定 | 用应力表比较 |
| <ItemLink id="create:steam_engine" /> | <ItemGrid><ItemIcon id="create:steam_engine" /></ItemGrid> | 由锅炉与引擎决定 | 用应力表比较 |

容量跟随来源的转速，所以两个水车的数字是运转时的输出。两种水车都从相邻水流取力，多盖几面不会继续提高输出。

| 仪表 | 外观 | 报告什么 |
| --- | --- | --- |
| <ItemLink id="create:stressometer" /> | <ItemGrid><ItemIcon id="create:stressometer" /></ItemGrid> | 所接网络的应力容量 |
| <ItemLink id="create:speedometer" /> | <ItemGrid><ItemIcon id="create:speedometer" /></ItemGrid> | 所接部件的转速 |

两种仪表都是放下的方块，报告它接入的网络。戴上 <ItemLink id="create:goggles" /> 可以看到更多细节，比较器也能读取它们。

***

## 第一条传动线

<Recipe id="create:crafting/kinetics/water_wheel" />

<Recipe id="create:crafting/kinetics/shaft" />

<Recipe id="create:crafting/kinetics/vertical_gearbox" />

石磨的帮助条目是 Processing Items in the Millstone。

<ItemGrid><ItemIcon id="create:millstone" /></ItemGrid>

1. 将 <ItemLink id="create:water_wheel" /> 放在流水中，从轮轴接出一段水平 <ItemLink id="create:shaft" />。
2. 在轴的末端放 <ItemLink id="create:vertical_gearbox" />，让一个水平接口对准轴、一个垂直接口朝上。需要时用扳手调整方向。
3. 从向上的接口接一段竖轴，再在竖轴正上方放 <ItemLink id="create:millstone" />，让轴从底部接入石磨。
4. 从顶部向石磨丢入小麦。研磨完成后，空手右键石磨取出成品。

石磨开始转并完成研磨，就是这条线工作正常。轴接在不被接受的方向上时什么都不会传递，看起来像网络停摆，但并不是过载。

石磨也支持自动化输入与抽出，顶部进料，成品从方块取出。

***

## 比例、轴向与反转

<EmiSearch query="@create_connected" />

| 部件 | 外观 | 对传动做了什么 |
| --- | --- | --- |
| <ItemLink id="create:shaft" /> | <ItemGrid><ItemIcon id="create:shaft" /></ItemGrid> | 沿同一轴传递旋转 |
| <ItemLink id="create:cogwheel" /> | <ItemGrid><ItemIcon id="create:cogwheel" /></ItemGrid> | 同尺寸齿轮啮合时转速不变、转向相反 |
| <ItemLink id="create:large_cogwheel" /> | <ItemGrid><ItemIcon id="create:large_cogwheel" /></ItemGrid> | 与小齿轮啮合时，大带小转速加倍，小带大转速减半 |
| <ItemLink id="create:gearbox" /> 与 <ItemLink id="create:vertical_gearbox" /> | <ItemGrid><ItemIcon id="create:gearbox" /><ItemIcon id="create:vertical_gearbox" /></ItemGrid> | 在拐角处传递，直线连接会反转 |
| <ItemLink id="create:gearshift" /> | <ItemGrid><ItemIcon id="create:gearshift" /></ItemGrid> | 直线传递，通电时反转 |
| <ItemLink id="create:wrench" /> | <ItemGrid><ItemIcon id="create:wrench" /></ItemGrid> | 旋转与配置已放置的动力部件 |

普通齿轮箱在拐角处让轴互为镜像方向，并行齿轮箱在拐角处同向。两者直线连接都会反转。

Create: Connected 提供针对具体路由的部件。

| 部件 | 外观 | 不同之处 |
| --- | --- | --- |
| <ItemLink id="create_connected:cross_connector" /> | <ItemGrid><ItemIcon id="create_connected:cross_connector" /></ItemGrid> | 跨过中间传递旋转，两条线不相接 |
| <ItemLink id="create_connected:parallel_gearbox" /> | <ItemGrid><ItemIcon id="create_connected:parallel_gearbox" /></ItemGrid> | 拐角同向，直线反转 |
| <ItemLink id="create_connected:six_way_gearbox" /> | <ItemGrid><ItemIcon id="create_connected:six_way_gearbox" /></ItemGrid> | 六个面都能接轴 |
| <ItemLink id="create_connected:brass_gearbox" /> | <ItemGrid><ItemIcon id="create_connected:brass_gearbox" /></ItemGrid> | 每个面用扳手单独设置 |
| <ItemLink id="create_connected:encased_chain_cogwheel" /> | <ItemGrid><ItemIcon id="create_connected:encased_chain_cogwheel" /></ItemGrid> | 链条传动，本身也能接齿轮 |
| <ItemLink id="create_connected:kinetic_bridge" /> | <ItemGrid><ItemIcon id="create_connected:kinetic_bridge" /></ItemGrid> | 在两条独立网络之间传递设定数量的容量，可在数值面板调整 |

***

## 保护线路的开关

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="create:clutch" /> | <ItemGrid><ItemIcon id="create:clutch" /></ItemGrid> | 红石切断分支，来源继续转动 |
| <ItemLink id="create_connected:inverted_clutch" /> | <ItemGrid><ItemIcon id="create_connected:inverted_clutch" /></ItemGrid> | 只有通电时才传递 |
| <ItemLink id="create_connected:inverted_gearshift" /> | <ItemGrid><ItemIcon id="create_connected:inverted_gearshift" /></ItemGrid> | 默认反转，通电时原样传递 |
| <ItemLink id="create_connected:freewheel_clutch" /> | <ItemGrid><ItemIcon id="create_connected:freewheel_clutch" /></ItemGrid> | 输入旋转符合设定方向时才传递动力 |
| <ItemLink id="create_connected:centrifugal_clutch" /> | <ItemGrid><ItemIcon id="create_connected:centrifugal_clutch" /></ItemGrid> | 按设定的输入转速阈值接合 |
| <ItemLink id="create_connected:shear_pin" /> | <ItemGrid><ItemIcon id="create_connected:shear_pin" /></ItemGrid> | 一次性连接件，网络过载时断裂 |
| <ItemLink id="create_connected:overstress_clutch" /> | <ItemGrid><ItemIcon id="create_connected:overstress_clutch" /></ItemGrid> | 过载持续到设定延迟后脱开，排除过载后用扳手或红石脉冲复位 |
| <ItemLink id="create_connected:brake" /> | <ItemGrid><ItemIcon id="create_connected:brake" /></ItemGrid> | 收到红石信号时给网络施加很大的应力负载 |

***

## 手动与更大的来源

| 来源 | 外观 | 需要什么 |
| --- | --- | --- |
| <ItemLink id="create_connected:crank_wheel" /> | <ItemGrid><ItemIcon id="create_connected:crank_wheel" /></ItemGrid> | 放在地上的轮子用手摇。按住右键逆时针，潜行时按住右键顺时针 |
| <ItemLink id="create:windmill_bearing" /> | <ItemGrid><ItemIcon id="create:windmill_bearing" /></ItemGrid> | 轴承上装帆组 |
| <ItemLink id="create:steam_engine" /> | <ItemGrid><ItemIcon id="create:steam_engine" /></ItemGrid> | 锅炉供汽，活塞能自由运动 |

风车轴承与蒸汽引擎的思索课程会展示对应的发电装置布局。研磨与矿石处理见[材料加工](machines.ore-processing.md)。

- [旋转储存](power.stored-rotation.md) 把旋转储存起来稍后使用。
- [机器与存储](reference.machines-storage.md) 本主题所属分区。
- [物品与流体输送](machines.logistics.md) 传送带、漏斗与物品路由。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Connected](images/create-connected-icon.png) [Create: Connected](machines.rotation.md) | 为机械动力增加传动部件与更灵活的存储布置方式。 | <EmiSearch query="@create_connected" /> |
