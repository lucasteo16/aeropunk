---
navigation:
  title: "电路"
  position: 5
  parent: reference.machines-storage.md
  icon: minecraft:lightning_rod
---

# 电路

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+Electro+Energetics+1.1.3+electricity+guide) · [中文](https://www.youtube.com/results?search_query=Minecraft+Create+Electro+Energetics+1.1.3+%E7%94%B5%E5%8A%9B%E6%95%99%E7%A8%8B)

## 安装交流发电机

<EmiSearch query="@electroenergetics" /> <EmiSearch query="@create" />

Create: Electro Energetics 在交流发电机处把旋转转换为电力。Ponder 条目 Setting up an alternator 要求用定子围住转子，再接入旋转动力。

<ItemGrid><ItemIcon id="electroenergetics:alternator_rotor" /><ItemIcon id="electroenergetics:stator" /><ItemIcon id="electroenergetics:alternator_brushes" /></ItemGrid>

具体方块布局请打开该条目，不要猜测转子和定子位置。

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+alternator+stator+rotor+setup) · [中文](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+%E5%8F%91%E7%94%B5%E6%9C%BA+%E5%AE%9A%E5%AD%90+%E8%BD%AC%E5%AD%90+%E5%AE%89%E8%A3%85)

***

## 接通第一条电路

<ItemGrid><ItemIcon id="electroenergetics:connector" /><ItemIcon id="electroenergetics:copper_wire_spool" /><ItemIcon id="electroenergetics:blue_electric_motor" /><ItemIcon id="electroenergetics:bulb" /></ItemGrid>

1. 在交流发电机输出端与灯泡或蓝色电动机处放置电气接线端。
2. 用铜线轴把发电机正极接到负载，再把负载回路接回发电机负极。闭合电路需要两条线路。
3. 启动旋转动力源。灯泡亮起或电动机转动，就是直接可见的首次成功信号。
4. 通过 Connecting Wires Ponder 学习如何用空线轴拆除导线。

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+closed+circuit+copper+wire+connectors+blue+electric+motor) · [中文](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+%E9%97%AD%E5%90%88%E7%94%B5%E8%B7%AF+%E9%93%9C%E7%BA%BF+%E6%8E%A5%E7%BA%BF%E7%AB%AF+%E8%93%9D%E8%89%B2%E7%94%B5%E5%8A%A8%E6%9C%BA)

***

## 保护、测量与变压

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="electroenergetics:fuse_holder" /> | <ItemGrid><ItemIcon id="electroenergetics:fuse_holder" /></ItemGrid> | 串联安装保险丝以保护电路 |
| <ItemLink id="electroenergetics:voltmeter" /> | <ItemGrid><ItemIcon id="electroenergetics:voltmeter" /></ItemGrid> | 并联接在两点之间，读取电压差 |
| <ItemLink id="electroenergetics:ammeter" /> | <ItemGrid><ItemIcon id="electroenergetics:ammeter" /></ItemGrid> | 串联接入以测量电流 |
| <ItemLink id="electroenergetics:clamp_meter" /> | <ItemGrid><ItemIcon id="electroenergetics:clamp_meter" /></ItemGrid> | 右键点击导线测量电流，无需断线 |
| <ItemLink id="electroenergetics:transformer_core" /> | <ItemGrid><ItemIcon id="electroenergetics:transformer_core" /></ItemGrid> | 变压器组装所需的铁芯 |
| <ItemLink id="electroenergetics:high_voltage_capacitor" /> | <ItemGrid><ItemIcon id="electroenergetics:high_voltage_capacitor" /></ItemGrid> | 高压储能部件 |
| <ItemLink id="electroenergetics:accumulator" /> | <ItemGrid><ItemIcon id="electroenergetics:accumulator" /></ItemGrid> | 储存电能，正极接正极，负极接负极 |
| <ItemLink id="electroenergetics:emergency_stop_button" /> | <ItemGrid><ItemIcon id="electroenergetics:emergency_stop_button" /></ItemGrid> | 右键进入急停并断开内部开关，潜行右键则解除 |

变压器铁芯条目要求在铁芯周围安装散热板，并在上方覆盖变压器油以提高额定功率。不要超过额定值。电压表测量两点之间的电压差，不是单点的绝对电压。

***

## 选择下一项电气部件

第一条电路工作后，再按用途增加部件。变压器按设定变比改变电压。稳压器分为电源、接地和负载端子，不能像只有两个接点的灯泡那样连接。

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="electroenergetics:fuse" /> | <ItemGrid><ItemIcon id="electroenergetics:fuse" /></ItemGrid> | 装入串联在电路中的保险丝座 |
| <ItemLink id="electroenergetics:insulated_wire" /> | <ItemGrid><ItemIcon id="electroenergetics:insulated_wire" /></ItemGrid> | 绝缘导线材料 |
| <ItemLink id="electroenergetics:capacitor" /> | <ItemGrid><ItemIcon id="electroenergetics:capacitor" /></ItemGrid> | 电容部件 |
| <ItemLink id="electroenergetics:electric_pump" /> | <ItemGrid><ItemIcon id="electroenergetics:electric_pump" /></ItemGrid> | 电动流体泵 |
| <ItemLink id="electroenergetics:transformer" /> | <ItemGrid><ItemIcon id="electroenergetics:transformer" /></ItemGrid> | 设定变比以升压或降压 |
| <ItemLink id="electroenergetics:voltage_regulator" /> | <ItemGrid><ItemIcon id="electroenergetics:voltage_regulator" /></ItemGrid> | 电源接顶部输入端，负极接底部接地端，负载接输出端，再接通回路 |

***

## 为铁路供电

<ItemGrid><ItemIcon id="electroenergetics:catenary_holder" /><ItemIcon id="electroenergetics:pantograph" /><ItemIcon id="electroenergetics:rail_contact_shoe" /></ItemGrid>

架空供电时，正极接触网，负极接地线杆。电动列车需要电动机，并让受电弓接触接触网。所选 Ponder 也展示了第三轨接触靴方案。列车操作见[客运铁路](transport.passenger.md)。

- [钢铁与石油](power.industry.md)，了解炉子、石油加工与引擎。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Electro Energetics](images/create-electro-energetics-icon.png) [Create: Electro Energetics](power.electricity.md) | 增加发电、输配电与电动机器，包括电力列车。 | <EmiSearch query="@electroenergetics" /> |
