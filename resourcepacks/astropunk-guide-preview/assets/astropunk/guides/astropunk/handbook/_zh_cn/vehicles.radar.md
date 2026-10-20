---
navigation:
  title: "读取雷达信息"
  position: 8
  parent: reference.vehicles.md
  icon: minecraft:sculk_sensor
---

# 读取雷达信息

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Radars+radar+bearing+monitor+network+data+link+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Radars+%E9%9B%B7%E8%BE%BE+%E7%9B%91%E8%A7%86%E5%99%A8+%E7%BD%91%E7%BB%9C%E6%8E%A7%E5%88%B6%E5%99%A8+%E6%95%B0%E6%8D%AE%E9%93%BE+%E6%95%99%E7%A8%8B)

## 探测链

<EmiSearch query="@create_radar" /> <EmiSearch query="@create" />

![雷达天线组件](images/feedback-radar-dish.png)

雷达天线组件

<ItemGrid><ItemIcon id="create_radar:radar_bearing" /><ItemIcon id="create_radar:radar_receiver_block" /><ItemIcon id="create_radar:radar_dish_block" /><ItemIcon id="create_radar:radar_plate_block" /><ItemIcon id="create_radar:monitor" /><ItemIcon id="create_radar:data_link" /></ItemGrid>

一部雷达由轴承、接收器、天线阵和显示器组成，按这个顺序连接。

1. 放下 <ItemLink id="create_radar:radar_bearing" /> 并给它旋转力，由它扫动天线阵。
2. 在旁边放下 <ItemLink id="create_radar:radar_receiver_block" />。
3. 用 <ItemLink id="create_radar:radar_dish_block" /> 造天线，或用 <ItemLink id="create_radar:radar_plate_block" /> 造平板。两者可以混用，每增加一件都扩大范围。
4. 在你要看的位置放下 <ItemLink id="create_radar:monitor" />，用 <ItemLink id="create_radar:data_link" /> 把两者连起来。
5. 右键链接设置频道。

只转的轴承什么也探测不到。没有接收器的天线阵什么也报不出来。显示器显示的是接收器送来的内容，所以在怀疑天线之前先看链接颜色。

## 网络与过滤器

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Radars+network+controller+filters+data+link+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Radars+%E7%BD%91%E7%BB%9C%E6%8E%A7%E5%88%B6%E5%99%A8+%E8%BF%87%E6%BB%A4%E5%99%A8+%E6%95%B0%E6%8D%AE%E9%93%BE+%E6%95%99%E7%A8%8B)

### 网络过滤

<ItemGrid><ItemIcon id="create_radar:network_filterer" /><ItemIcon id="create_radar:radar_filter_item" /><ItemIcon id="create_radar:target_filter_item" /><ItemIcon id="create_radar:ident_filter_item" /></ItemGrid>

### 识别与警报

<ItemGrid><ItemIcon id="create_radar:identification_transponder" /><ItemIcon id="create_radar:radar_safe_zone_designator" /><ItemIcon id="create_radar:radar_warning_receiver" /></ItemGrid>

<ItemLink id="create_radar:network_filterer" /> 是雷达网络的中心。它接受过滤器，用来限制网络能看见什么、能做什么，并像单部雷达一样连到显示器。

| 过滤器 | 限制内容 | 适用时机 |
| --- | --- | --- |
| <ItemLink id="create_radar:radar_filter_item" /> | 屏幕上出现哪些目标 | 画面过于杂乱 |
| <ItemLink id="create_radar:target_filter_item" /> | 哪些目标可以被锁定 | 与友军共用空域 |
| <ItemLink id="create_radar:ident_filter_item" /> | 接受哪些身份 | 使用应答机时 |

友方飞行器装上 <ItemLink id="create_radar:identification_transponder" /> 就会被识别为已知目标。<ItemLink id="create_radar:radar_warning_receiver" /> 在被跟踪时提醒本机，<ItemLink id="create_radar:radar_safe_zone_designator" /> 则把某个位置排除在火力网络之外。

## 火力控制

<ItemGrid><ItemIcon id="create_radar:auto_yaw_controller" /><ItemIcon id="create_radar:auto_pitch_controller" /><ItemIcon id="create_radar:fire_controller" /><ItemIcon id="create_radar:guided_fuze" /></ItemGrid>

炮塔需要在炮架下方装偏航控制器，旁边装俯仰控制器。两者都用数据链接连好，然后在显示器上选择目标。<ItemLink id="create_radar:fire_controller" /> 只在火炮对准时输出红石，真正开火的是这个信号。

红色数据链接属于火力网络，蓝色属于雷达网络。两者接反，是炮塔会跟随却始终不开火的常见原因。

<Recipe id="create_radar:crafting/auto_pitch_controller" />

## 机载雷达

<EmiSearch query="@aeroengineering" />

<ItemGrid><ItemIcon id="aeroengineering:airborne_radar" /><ItemIcon id="create_radar:binoculars" /><ItemIcon id="create_radar:plane_radar" /></ItemGrid>

AeroEngine 的 <ItemLink id="aeroengineering:airborne_radar" /> 是另一套仪表。它切换目标、确认锁定并向导弹发送发射频率，所以它与飞机自己的武器配套，而不是接入地面雷达网络。<ItemLink id="create_radar:binoculars" /> 用来在画面含糊时用肉眼确认目标。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Radars](images/catalog-blu2yqfq.png) [Create: Radars](vehicles.radar.md) | 为机械动力建筑增加探测与追踪目标的雷达设备。 | <EmiSearch query="@create_radar" /> |
