---
navigation:
  title: "为机器提供旋转动力"
  position: 3
  parent: reference.machines-storage.md
  icon: create:cogwheel
---

# 为机器提供旋转动力

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Connected+Rotational+power+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Connected+%E4%B8%BA%E6%9C%BA%E5%99%A8%E6%8F%90%E4%BE%9B%E6%97%8B%E8%BD%AC%E5%8A%A8%E5%8A%9B+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 先看应力，再看转速

<EmiSearch query="@create" />

每个旋转网络都有来自动力源的容量，也有来自机器的应力消耗。消耗低于容量时整个网络都在转。消耗超过容量的一刻，网络停转，上面所有东西都不工作。

本包保留应力机制，所以面对一台机器时，第一个问题不是它该转多快，而是网络带不带得动它。

<ItemGrid><ItemIcon id="create:water_wheel" /><ItemIcon id="create:large_water_wheel" /><ItemIcon id="create:windmill_bearing" /><ItemIcon id="create:steam_engine" /></ItemGrid>

| 动力源 | 容量 | 说明 |
| --- | --- | --- |
| <ItemLink id="create:water_wheel" /> | 32 点应力 | 最便宜的稳定来源 |
| <ItemLink id="create:large_water_wheel" /> | 128 点应力 | 四倍于小水车，高度相同 |
| <ItemLink id="create:windmill_bearing" /> | 512 点应力 | 上方需要组装风帆 |
| <ItemLink id="create:steam_engine" /> | 1024 点应力 | 需要锅炉与供水 |

本包把全局转速上限留在每分钟 256 转。应力消耗随转速上升，配置说明每提升一档转速，机器的消耗翻倍，因此让一条线转得更快，是用容量换产量。

***

## 转向与换向

<EmiSearch query="@create_connected" />

<ItemLink id="create:shaft" /> 把旋转原样传过去。<ItemLink id="create:cogwheel" /> 让轴转四分之一圈改变方向。<ItemLink id="create:gearbox" /> 把一个输入分成四个方向。

<ItemGrid><ItemIcon id="create:shaft" /><ItemIcon id="create:cogwheel" /><ItemIcon id="create:large_cogwheel" /><ItemIcon id="create:gearbox" /><ItemIcon id="create:wrench" /></ItemGrid>

| 部件 | 改变什么 |
| --- | --- |
| <ItemLink id="create:shaft" /> | 不改变，同轴同速 |
| <ItemLink id="create:cogwheel" /> 与第二只齿轮啮合 | 第二根轴反向 |
| <ItemLink id="create:large_cogwheel" /> 与小齿轮啮合 | 按尺寸比例改变转速，方向相反 |
| <ItemLink id="create:gearbox" /> | 四个面，相对两面同向 |

Create: Connected 补上了这套部件的空缺。每个部件解决不同的走线问题。

| 部件 | 区别 |
| --- | --- |
| <ItemLink id="create_connected:cross_connector" /> | 两个方向各自传递，互不干扰 |
| <ItemLink id="create_connected:parallel_gearbox" /> | 四个面同向 |
| <ItemLink id="create_connected:six_way_gearbox" /> | 六面都有轴，上下两面为半速 |
| <ItemLink id="create_connected:brass_gearbox" /> | 每个面的方向可单独用扳手配置 |
| <ItemLink id="create_connected:encased_chain_cogwheel" /> | 链条传动上再加一只齿轮 |
| <ItemLink id="create_connected:crank_wheel" /> | 带齿轮的手摇曲柄，用于紧凑的齿轮比 |
| <ItemLink id="create_connected:kinetic_bridge" /> | 在两个不合并的网络之间传递容量 |

旋转方向不是外观问题。两个网络只有在同向相接时才会合并。接上后如果反向，连接部件会断裂，所以在给新支线供能前用扳手确认方向。

风车至少需要八片风帆才能组装。之后每多八片风帆增加每分钟一转，因此普通风帆盘就是正常做法，不必做巨大的盘面。

***

<Recipe id="create:crafting/kinetics/wrench" />
## 让线路可控的部件

<ItemGrid><ItemIcon id="create:clutch" /><ItemIcon id="create:gearshift" /><ItemIcon id="create_connected:shear_pin" /><ItemIcon id="create_connected:overstress_clutch" /><ItemIcon id="create_connected:brake" /><ItemIcon id="create_connected:centrifugal_clutch" /><ItemIcon id="create_connected:freewheel_clutch" /><ItemIcon id="create_connected:inverted_clutch" /><ItemIcon id="create_connected:inverted_gearshift" /></ItemGrid>

| 部件 | 用途 |
| --- | --- |
| <ItemLink id="create:clutch" /> | 红石切断支线，动力源继续转 |
| <ItemLink id="create:gearshift" /> | 红石让支线反向 |
| <ItemLink id="create_connected:shear_pin" /> | 一次性连接件，超载时断开而不是拖停全网 |
| <ItemLink id="create_connected:overstress_clutch" /> | 网络超载后延时脱开，用扳手复位 |
| <ItemLink id="create_connected:brake" /> | 故意让网络超载来刹车 |

需要关掉而动力源继续转的支线，用离合器。宁可断开也不愿拖停全网的支线，用剪切销。

***

## 第一条传动线

两块 <ItemLink id="create:andesite_alloy" /> 做八根 <ItemLink id="create:shaft" />。这个比例正是短距离便宜、长距离昂贵的原因。

<Recipe id="create:crafting/kinetics/shaft" />

<Recipe id="create:crafting/kinetics/water_wheel" />

1. 把 <ItemLink id="create:water_wheel" /> 放在流动的水边，让水流推动桨叶。
2. 从水车接轴到要驱动的机器。
3. 在线上装一只 <ItemLink id="create:stressometer" />，对照容量与消耗。
4. 先看机器完整运行一个周期，再增加第二台。

要看到的结果是机器连续运转，应力表不高于容量。下一步值得做的是储备，让短暂中断不至于停掉生产。[旋转储备](power.stored-rotation.md)说明蓄电池与弹簧。

## 读数字

工程师护目镜会显示部件当前承受的应力和转速，卡住的机器会显示成具体数字而不是靠猜。速度表和应力表各测量单个部件，并且可以互相转换，改动前后用它们对比同一条传动线最直接。

<ItemGrid><ItemIcon id="create:goggles" /><ItemIcon id="create:speedometer" /><ItemIcon id="create:stressometer" /></ItemGrid>


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Connected](images/create-connected-icon.png) [Create: Connected](machines.rotation.md) | 为机械动力增加传动部件与更灵活的存储布置方式。 | <EmiSearch query="@create_connected" /> |
