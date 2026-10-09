---
navigation:
  title: "发电、配电与用电"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
---

# 发电、配电与用电

## 发电与储能

- 浏览物品: <EmiSearch query="@electroenergetics" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="electroenergetics:alternator_rotor" />
  <ItemIcon id="electroenergetics:stator" />
  <ItemIcon id="electroenergetics:alternator_brushes" />
  <ItemIcon id="electroenergetics:accumulator" />
  <ItemIcon id="electroenergetics:capacitor" />
  <ItemIcon id="electroenergetics:high_voltage_capacitor" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="electroenergetics:alternator_rotor" />, <ItemLink id="electroenergetics:stator" />, <ItemLink id="electroenergetics:alternator_brushes" /> | Create: Electro Energetics 的交流发电机将旋转动力转为电力，另有三相电刷系列。 |
| <ItemLink id="electroenergetics:accumulator" />, <ItemLink id="electroenergetics:capacitor" />, <ItemLink id="electroenergetics:high_voltage_capacitor" /> | 储存电能以供后续使用。充电电压与极性请看蓄电池思索演示。 |

***

## 导线与调节

<ItemGrid>
  <ItemIcon id="electroenergetics:connector" />
  <ItemIcon id="electroenergetics:copper_wire_spool" />
  <ItemIcon id="electroenergetics:insulated_wire" />
  <ItemIcon id="electroenergetics:transformer" />
  <ItemIcon id="electroenergetics:transformer_core" />
  <ItemIcon id="electroenergetics:voltage_regulator" />
  <ItemIcon id="electroenergetics:fuse" />
  <ItemIcon id="electroenergetics:fuse_holder" />
  <ItemIcon id="electroenergetics:emergency_stop_button" />
  <ItemIcon id="electroenergetics:voltmeter" />
  <ItemIcon id="electroenergetics:ammeter" />
  <ItemIcon id="electroenergetics:clamp_meter" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="electroenergetics:connector" />, <ItemLink id="electroenergetics:copper_wire_spool" />, <ItemLink id="electroenergetics:insulated_wire" /> | 连接器系列，以及铜、铁、琥珀金与绝缘导线系列。 |
| <ItemLink id="electroenergetics:transformer" />, <ItemLink id="electroenergetics:transformer_core" />, <ItemLink id="electroenergetics:voltage_regulator" /> | 转换或调节电路电压。变压器铁芯有独立功率额定值与组装要求。 |
| <ItemLink id="electroenergetics:fuse" />, <ItemLink id="electroenergetics:fuse_holder" />, <ItemLink id="electroenergetics:emergency_stop_button" /> | 保险丝在电流过大时提供保护。保险丝座与紧急停止按钮是独立的电路控制组件。 |
| <ItemLink id="electroenergetics:voltmeter" />, <ItemLink id="electroenergetics:ammeter" />, <ItemLink id="electroenergetics:clamp_meter" /> | 用于测量电路电压与电流。钳形电流表读取导线中的电流。 |

***

## 用电设备与铁路

<ItemGrid>
  <ItemIcon id="electroenergetics:blue_electric_motor" />
  <ItemIcon id="electroenergetics:electric_pump" />
  <ItemIcon id="electroenergetics:bulb" />
  <ItemIcon id="electroenergetics:pantograph" />
  <ItemIcon id="electroenergetics:rail_contact_shoe" />
  <ItemIcon id="electroenergetics:catenary_holder" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="electroenergetics:blue_electric_motor" />, <ItemLink id="electroenergetics:electric_pump" />, <ItemLink id="electroenergetics:bulb" /> | 染色电动机、电泵、灯泡与电阻加热器。 |
| <ItemLink id="electroenergetics:pantograph" />, <ItemLink id="electroenergetics:rail_contact_shoe" />, <ItemLink id="electroenergetics:catenary_holder" /> | 受电弓、接触靴与架空线铁路组件。 |

***

## 初次使用

先查看交流发电机与连接导线的思索演示，再先装仪表后接电动机。此系统需要考虑电压与电流，带电导线不是通用电力管线。除非目标连接明确受支持，否则应与工业机器的电路分开。

- [工业机器](power.industry.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create: Electro Energetics](images/create-electro-energetics-icon.png) [Create: Electro Energetics](power.electricity.md) | 增加发电、输配电与电动机器，包括电力列车。 | 已安装基准版 | <EmiSearch query="@electroenergetics" /> |
