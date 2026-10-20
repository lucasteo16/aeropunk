---
navigation:
  title: "发电、配电与用电"
  position: 11
  parent: reference.machines-storage.md
  icon: minecraft:lightning_rod
---

# 发电、配电与用电

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Electro+Energetics+Electricity+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Electro+Energetics+%E5%8F%91%E7%94%B5%E3%80%81%E9%85%8D%E7%94%B5%E4%B8%8E%E7%94%A8%E7%94%B5+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 旋转变成电压

<EmiSearch query="@electroenergetics" /> <EmiSearch query="@create" />

Create: Electro Energetics 不储存一个抽象的能量数字。电源感应出电压，设备让电流通过，电流做功。短路、又长又细的导线、匹配不当的变压器，都会因此改变结果。

交流发电机是两套系统的接合点。旋转带动它，它产出电流。

<ItemGrid><ItemIcon id="electroenergetics:alternator_rotor" /><ItemIcon id="electroenergetics:stator" /><ItemIcon id="electroenergetics:alternator_brushes" /><ItemIcon id="electroenergetics:accumulator" /><ItemIcon id="electroenergetics:capacitor" /><ItemIcon id="electroenergetics:high_voltage_capacitor" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="electroenergetics:alternator_rotor" /> | 发电机中旋转的部分 |
| <ItemLink id="electroenergetics:stator" /> | 环绕转子的固定绕组 |
| <ItemLink id="electroenergetics:alternator_brushes" /> | 把电流送到旋转部分，另有同族的三相变体 |
| <ItemLink id="electroenergetics:accumulator" /> | 储存电荷供之后取用 |
| <ItemLink id="electroenergetics:capacitor" /> | 平滑波动负载的小缓冲 |
| <ItemLink id="electroenergetics:high_voltage_capacitor" /> | 高压区段上的同样角色 |

把发电机接在工坊同一条轴线上。发电机的思索条目展示组装形态，照着做比猜方块顺序快。

***

## 单向接一条电路

<ItemGrid><ItemIcon id="electroenergetics:connector" /><ItemIcon id="electroenergetics:copper_wire_spool" /><ItemIcon id="electroenergetics:insulated_wire" /><ItemIcon id="electroenergetics:fuse" /><ItemIcon id="electroenergetics:voltmeter" /><ItemIcon id="electroenergetics:ammeter" /></ItemGrid>

| 部件 | 用途 |
| --- | --- |
| <ItemLink id="electroenergetics:connector" /> | 导线在方块上的接线点 |
| <ItemLink id="electroenergetics:copper_wire_spool" /> | 在接线点之间铺设导线 |
| <ItemLink id="electroenergetics:insulated_wire" /> | 需要绝缘的线路 |
| 带底座的 <ItemLink id="electroenergetics:fuse" /> | 在故障损坏线路前断开电路 |
| <ItemLink id="electroenergetics:fuse_holder" /> | 把保险丝固定在线路中 |
| <ItemLink id="electroenergetics:voltmeter" /> | 读取某点的电压 |
| <ItemLink id="electroenergetics:clamp_meter" /> | 不拆线就能读取导线中的电流 |
| <ItemLink id="electroenergetics:ammeter" /> | 读取通过某点的电流 |

1. 在发电机输出端与机器上各放一个接线点。
2. 用线轴在两点之间拉线，导线会按你画出的形状铺设。
3. 在电源与负载之间装上带底座的保险丝。
4. 先在电源端读电压表，再到负载端读一次。

两次读数之间的落差来自导线与距离，不是机器坏了。这正是它与流体式能源系统的区别，也是为什么电表该先买而不是最后买。

***

## 电机、泵与热

<ItemGrid><ItemIcon id="electroenergetics:blue_electric_motor" /><ItemIcon id="electroenergetics:electric_pump" /><ItemIcon id="electroenergetics:bulb" /><ItemIcon id="electroenergetics:transformer" /><ItemIcon id="electroenergetics:voltage_regulator" /><ItemIcon id="electroenergetics:transformer_core" /></ItemGrid>

| 用电设备 | 给你什么 |
| --- | --- |
| 电动机 | 不必拉轴就能得到旋转，有多种颜色 |
| <ItemLink id="electroenergetics:electric_pump" /> | 在远离工坊的位置输送流体 |
| <ItemLink id="electroenergetics:bulb" /> | 照明，也是电路带电的可见信号 |
| 电阻加热器 | 为需要热的机器供热 |

<ItemLink id="electroenergetics:transformer" /> 在区段之间改变电压，<ItemLink id="electroenergetics:voltage_regulator" /> 让一个区段保持稳定。变压器装在导线长度变化的地方，而不是每台机器旁边都装。

模组还提供专门的转换方块，在本模组电力与其他模组的 Forge Energy 设备之间转换，这是它驱动外部机器的途径。它的模拟在主线程之外运行，在未加载的区块里也继续工作，因此两座基地之间的长输电线路，无论你站在哪一边表现都一样。

***

## 电气化铁路

<ItemGrid><ItemIcon id="electroenergetics:pantograph" /><ItemIcon id="electroenergetics:rail_contact_shoe" /><ItemIcon id="electroenergetics:catenary_holder" /><ItemIcon id="electroenergetics:emergency_stop_button" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="electroenergetics:catenary_holder" /> | 把接触网架在轨道上方 |
| <ItemLink id="electroenergetics:pantograph" /> | 从上方接触网取流 |
| <ItemLink id="electroenergetics:rail_contact_shoe" /> | 从第三轨取流 |
| <ItemLink id="electroenergetics:emergency_stop_button" /> | 手动切断该区段 |

电气化铁路是独立于工坊电路的另一件事。先架好接触网，在一小段上测试受电弓，再延伸。[铁路](transport.passenger.md)说明列车本身。

电路稳定之后，下一步是把同样的活交给工业产线。[工业机械](power.industry.md)说明那套独立系统。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Electro Energetics](images/create-electro-energetics-icon.png) [Create: Electro Energetics](power.electricity.md) | 增加发电、输配电与电动机器，包括电力列车。 | <EmiSearch query="@electroenergetics" /> |
