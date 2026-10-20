---
navigation:
  title: "建造列车、轨道与车站"
  position: 2
  parent: reference.vehicles.md
  icon: create:track
---

# 建造列车、轨道与车站

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+train+assembly+station+seated+conductor+schedule+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+%E5%88%97%E8%BD%A6+%E7%BB%84%E8%A3%85+%E8%BD%A6%E7%AB%99+%E4%B9%98%E5%8A%A1%E5%91%98+%E6%97%B6%E5%88%BB%E8%A1%A8+%E6%95%99%E7%A8%8B)

## 线路、车站与时刻表

<EmiSearch query="@create" />

![装有 Bells & Whistles 配件的列车车体](images/visual-train-fittings.png)

<ItemGrid><ItemIcon id="create:track" /><ItemIcon id="create:track_station" /><ItemIcon id="create:controls" /><ItemIcon id="create:schedule" /><ItemIcon id="create:railway_casing" /></ItemGrid>

<Recipe id="create:crafting/kinetics/track_station" />

<Recipe id="create:crafting/kinetics/controls" />

一列可用的列车需要连续的 <ItemLink id="create:track" />、<ItemLink id="create:track_station" />，以及朝向行进方向的 <ItemLink id="create:controls" />。先用一条短线连接两座已命名车站，验证整段路线再扩建。

1. 将车站放在轨道旁，进入车站的组装模式。这与组装 Sable 飞船不同。
2. 在高亮轨道上放置 <ItemLink id="create:railway_casing" /> 生成转向架，在其上搭建车厢，用胶连接每节车厢的结构，并在驾驶位安装控制器。
3. 在车站界面中组装。若被拒绝，先读错误消息，再检查转向架位置与车厢连接。
4. 手动驾驶这段短线，确认轨道连续，两端都有停车空间。
5. 自动运行需要坐在控制器前方的乘务员。对乘务员使用已填写的 <ItemLink id="create:schedule" />，为各站添加目的地名称与等待条件，例如定时等待或货物条件，并设置是否循环。

时刻表交给乘务员，不是放进列车里某个未说明的槽。手动驾驶不需要时刻表。自动列车一直等待时，先检查当前等待条件、目的地名称和前方信号，再考虑动力问题。

## 轨道家族

<ItemGrid><ItemIcon id="create:track" /><ItemIcon id="create:track_station" /><ItemIcon id="create:controls" /><ItemIcon id="create:schedule" /></ItemGrid>

Create 提供标准轨道以及配套的车站与控制。Steam 'n' Rails 扩展出更窄和更宽的轨距、道岔、信号与乘务设备。轨距不是装饰。列车在哪种轨道上组装，就属于哪种轨距，道岔也只连接同轨距的轨道。

在铺主线之前，先用打算使用的轨距修一段短测试线。中途换轨距等于重建，而不是调整。

## 转向架

<ItemGrid><ItemIcon id="create:railway_casing" /></ItemGrid>

Blocks & Bogies 提供转向架定制界面，而不是另一套独立物品。对已放置的转向架打开界面，预览轮组、框架尺寸与气门机构样式。菜单中的驱动与承载分类描述所选造型，不代表每列车必须安装一个动力转向架，也不要求按车厢重量计算轴数。

按车厢造型选择样式，先在短弯道上检查外观，再应用到整列车。轨距兼容性取决于轨道与转向架的组合，不要把装饰轮组的长度当成会导致物理脱轨的规则。

## 货运与客运

<ItemGrid><ItemIcon id="create:schedule" /><ItemIcon id="create:track_station" /></ItemGrid>

车厢装什么由你决定。座椅、储物与流体罐都是车体内的普通方块，停靠位置由时刻表决定。乘客信息与线路查询见[列车出行](transport.passenger.md)。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Blocks & Bogies](images/catalog-j4arnqwy.png) [Create: Blocks & Bogies](transport.railway-builder.md) | 增加更大的机械动力列车转向架，含带可见阀动机构的款式。 | 无独立物品查询 |
| ![Steam 'n' Rails Neoforge](images/catalog-l3jv0qzi.png) [Steam 'n' Rails Neoforge](transport.railway-builder.md) | 为机械动力铁路增加轨道与列车部件。 | <EmiSearch query="@railways" /> |
