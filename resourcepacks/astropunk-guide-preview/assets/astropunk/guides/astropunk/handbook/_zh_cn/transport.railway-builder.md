---
navigation:
  title: "建造列车、轨道与车站"
  position: 2
  parent: reference.vehicles.md
  icon: create:track
---

# 建造列车、轨道与车站

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Blocks+%26+Bogies+Steam+%27n%27+Rails+Neoforge+Railways+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Blocks+%26+Bogies+Steam+%27n%27+Rails+Neoforge+%E5%BB%BA%E9%80%A0%E5%88%97%E8%BD%A6%E3%80%81%E8%BD%A8%E9%81%93%E4%B8%8E%E8%BD%A6%E7%AB%99+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 线路、车站与时刻表

<EmiSearch query="@create" />

![装有 Bells & Whistles 配件的列车车体](images/visual-train-fittings.png)

装有 Bells & Whistles 配件的列车车体

<ItemGrid><ItemIcon id="create:track" /><ItemIcon id="create:track_station" /><ItemIcon id="create:controls" /><ItemIcon id="create:schedule" /><ItemIcon id="create:railway_casing" /></ItemGrid>

Create 列车按顺序需要三样东西。连续的 <ItemLink id="create:track" /> 线路，线路上的一座 <ItemLink id="create:track_station" />，以及要驾驶的车体内部的一块 <ItemLink id="create:controls" />。

先铺轨，并确认两端接上。一格缺口就足以让列车停下，弯道上的轨道还需要轮架能跟得上的半径。

然后把车厢当作普通方块结构造好，把列车控制装在里面。把车站放在轨道旁，命名，再通过车站组装列车。车站才是把方块变成列车的装置，附近没有车站的车厢只是建筑。

<ItemLink id="create:schedule" /> 是时刻表。放进列车，按想要的顺序加入车站并设置条件。没有时刻表的列车只跑一趟就停。

<Recipe id="create:crafting/kinetics/track_station" />

<Recipe id="create:crafting/kinetics/controls" />

## 轨道家族

<ItemGrid><ItemIcon id="create:track" /><ItemIcon id="create:track_station" /><ItemIcon id="create:controls" /><ItemIcon id="create:schedule" /></ItemGrid>

Create 提供标准轨道以及配套的车站与控制。Steam 'n' Rails 扩展出更窄和更宽的轨距、道岔、信号与乘务设备。轨距不是装饰。列车在哪种轨道上组装，就属于哪种轨距，道岔也只连接同轨距的轨道。

在铺主线之前，先用打算使用的轨距修一段短测试线。中途换轨距等于重建，而不是调整。

## 转向架

<ItemGrid><ItemIcon id="create:railway_casing" /></ItemGrid>

Blocks & Bogies 增加的是转向架定制界面，而不是另一套转向架物品。右键已放置的转向架打开界面，先选驱动或承载角色，再选菜单提供的轴数、尺寸与长度。气门机构样式是同一界面里的进一步选择，菜单也可以切到 Steam 'n' Rails 的样式。

| 选项 | 改变 | 保持一致 |
| --- | --- | --- |
| 角色 | 转向架驱动还是承载 | 每列车一个驱动转向架 |
| 轴数 | 接触轨道的轮数 | 与车厢重量匹配 |
| 尺寸与长度 | 车轮与框架占地 | 与弯道半径匹配 |
| 气门机构 | 可见运动 | 仅影响外观 |

并非所有组合都能互换。长转向架在急弯上会脱轨，短转向架则能通过，所以要在全线最急的弯道上测试组合。

## 货运与客运

<ItemGrid><ItemIcon id="create:schedule" /><ItemIcon id="create:track_station" /></ItemGrid>

车厢装什么由你决定。座椅、储物与流体罐都是车体内的普通方块，停靠位置由时刻表决定。乘客信息与线路查询见[列车出行](transport.passenger.md)。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Blocks & Bogies](images/catalog-j4arnqwy.png) [Create: Blocks & Bogies](transport.railway-builder.md) | 增加更大的机械动力列车转向架，含带可见阀动机构的款式。 | 无独立物品查询 |
| ![Steam 'n' Rails Neoforge](images/catalog-l3jv0qzi.png) [Steam 'n' Rails Neoforge](transport.railway-builder.md) | 为机械动力铁路增加轨道与列车部件。 | <EmiSearch query="@railways" /> |
