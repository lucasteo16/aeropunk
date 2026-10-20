---
navigation:
  title: "钢铁与石油"
  position: 8
  parent: reference.machines-storage.md
  icon: minecraft:iron_ingot
---

# 钢铁与石油

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+coke+oven+blast+furnace+oil+engines) · [中文](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+%E7%84%A6%E7%82%AD%E7%82%89+%E9%AB%98%E7%82%89+%E7%9F%B3%E6%B2%B9+%E5%BC%95%E6%93%8E)

## 先制焦炭

<EmiSearch query="@tfmg" />

Coke Oven Ponder 展示从任意侧面加入煤。二氧化碳从顶部排出，木馏油可从其他面抽取，煤焦炭会在一段时间后从机器掉出。需要提高产量时可并排布置多台焦炭炉。

<ItemGrid><ItemIcon id="tfmg:coke_oven" /><ItemIcon id="tfmg:coal_coke" /><ItemIcon id="tfmg:creosote_bucket" /></ItemGrid>

<Recipe id="tfmg:crafting/materials/coke_oven" />

焦炭炉的原料是 <ItemLink id="minecraft:coal" />。

***

## 建造可工作的高炉

Blast Furnace Ponder 展示用耐火砖围成圆柱，并安装高炉输出方块与舱口。高炉必须有强化方块才能工作，强化并非仅用于提速。物料从顶部开口加入，舱口接入热风。顶部还可安装第二个舱口收集炉气，投入其中的物品会落入高炉。

<ItemGrid><ItemIcon id="tfmg:fireproof_bricks" /><ItemIcon id="tfmg:blast_furnace_output" /><ItemIcon id="tfmg:blast_furnace_hatch" /><ItemIcon id="tfmg:blast_stove" /></ItemGrid>

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+blast+furnace+reinforcement+hot+air) · [中文](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+%E9%AB%98%E7%82%89+%E5%BC%BA%E5%8C%96+%E7%83%AD%E9%A3%8E)

Blast Stove Ponder 明确了各面用途：底部输入燃料，侧面输入空气，顶部输出热风。二氧化碳会积累并可能使炉子停工，因此要把它排到附近的烟囱或排气口。先确认热风送达高炉，再投入铁料。

***

## 寻找石油并蒸馏

从底部用 Machine Input 为地表扫描器供能。顶部网格代表周围区块，中心格是所在区块。含油区块会在数秒内亮起，用区块边界确认目标位置。

<ItemGrid><ItemIcon id="tfmg:surface_scanner" /><ItemIcon id="tfmg:pumpjack_base" /><ItemIcon id="tfmg:industrial_pipe" /></ItemGrid>

Pumpjack Ponder 的路线从油藏铺设工业管道到地表开始。把抽油机底座放在管道顶端，后方放锤架，在曲柄与底座上方安装连接件和机头，用抽油机锤部件连接并涂抹超级胶水固定。最后安装 Machine Input，并在其上方放置曲柄提供动力。

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+pumpjack+crude+oil+distillation+tower) · [中文](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+%E6%8A%BD%E6%B2%B9%E6%9C%BA+%E5%8E%9F%E6%B2%B9+%E8%92%B8%E9%A6%8F%E5%A1%94)

蒸馏塔底部用钢制储罐组装，在储罐旁安装钢制蒸馏控制器，再加最多六个蒸馏输出口，并在它们之间连接工业管道。储罐下方放置热源，原油输入控制器，通过塔身刻度确认供能。产物经蒸馏输出口和管道导出。

<ItemGrid><ItemIcon id="tfmg:steel_distillation_controller" /><ItemIcon id="tfmg:steel_distillation_output" /><ItemIcon id="tfmg:steel_fluid_tank" /><ItemIcon id="tfmg:industrial_pipe" /></ItemGrid>

***

## 选择加工附件

化学槽可安装不同附件来改变用途。插入搅拌叶片后用于搅拌。两个电极架配铜电极可组成电解器。三个石墨电极可组成高炉。部分配方需要加热。

<ItemGrid><ItemIcon id="tfmg:steel_chemical_vat" /><ItemIcon id="tfmg:industrial_mixer" /><ItemIcon id="tfmg:copper_electrode" /><ItemIcon id="tfmg:graphite_electrode" /></ItemGrid>

<ItemGrid><ItemIcon id="tfmg:casting_basin" /></ItemGrid>

铸造时将钢水送入铸造盆，并为产物留出足够空间，因为盆内储量有限。

***

## 操作引擎与绕线机

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+TFMG+Community+1.3.2a+regular+engine+turbine+engine+setup) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+TFMG+%E5%BC%95%E6%93%8E+%E6%B6%A1%E8%BD%AE%E5%BC%95%E6%93%8E+%E5%BB%BA%E9%80%A0+%E7%87%83%E6%96%99+%E6%95%99%E7%A8%8B)

Ponder 展示常规引擎的组装方式，用空白蓝图切换型号，插入同型号气缸后完成组装。对组装完成的引擎使用传动轴即可建立旋转输出。常规引擎和涡轮引擎的布局可查阅上方对应教程，燃料与连接方式不能直接照搬大型引擎。

<ItemGrid><ItemIcon id="tfmg:regular_engine" /><ItemIcon id="tfmg:radial_engine" /><ItemIcon id="tfmg:turbine_engine" /><ItemIcon id="tfmg:large_engine" /><ItemIcon id="tfmg:simple_large_engine" /></ItemGrid>

大型引擎需要传动轴输出、从侧面输入燃料、持续供气并排出二氧化碳。具体引擎可用燃料以该引擎的提示为准。

绕线机先用右键放入线轴，再右键放入待加工物品。提供旋转后开始绕线，完成时自动停止。漏斗可输入原料并取出成品，机械手可装入线轴。

<ItemGrid><ItemIcon id="tfmg:winding_machine" /><ItemIcon id="tfmg:empty_spool" /><ItemIcon id="tfmg:machine_input" /><ItemIcon id="tfmg:engine_cylinder" /></ItemGrid>

***

## 连接工业工坊电网

用传动轴驱动发电机，通过对应电缆系统连接工业用电设备，再用设置扳手右键电气方块分配组别。同组部件分配电压，不同组保留完整电压。电动机开始转动就是首次有效结果。变压器、电位器和开关会建立子网络，扩建前先查看各自的 Ponder 条目。

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="tfmg:generator" /> | <ItemGrid><ItemIcon id="tfmg:generator" /></ItemGrid> | 将旋转动力转换为工业电力 |
| <ItemLink id="tfmg:electric_motor" /> | <ItemGrid><ItemIcon id="tfmg:electric_motor" /></ItemGrid> | 将工业电力转换为旋转动力 |
| <ItemLink id="tfmg:heavy_electric_motor" /> | <ItemGrid><ItemIcon id="tfmg:heavy_electric_motor" /></ItemGrid> | 重型电动机系列 |
| <ItemLink id="tfmg:copper_cable_hub" /> | <ItemGrid><ItemIcon id="tfmg:copper_cable_hub" /></ItemGrid> | 工业网络的电缆连接点 |
| <ItemLink id="tfmg:transformer" /> | <ItemGrid><ItemIcon id="tfmg:transformer" /></ItemGrid> | 按初级与次级线圈匝数比改变子网络电压 |
| <ItemLink id="tfmg:voltmeter" /> | <ItemGrid><ItemIcon id="tfmg:voltmeter" /></ItemGrid> | 读取工业电网状态 |
| <ItemLink id="tfmg:electricians_wrench" /> | <ItemGrid><ItemIcon id="tfmg:electricians_wrench" /></ItemGrid> | 右键电气方块，打开其分组设置 |
| <ItemLink id="tfmg:freezer" /> | <ItemGrid><ItemIcon id="tfmg:freezer" /></ItemGrid> | 冷却加工机器 |
| <ItemLink id="tfmg:compressor" /> | <ItemGrid><ItemIcon id="tfmg:compressor" /></ItemGrid> | 压缩与供气机器 |
| <ItemLink id="tfmg:steel_pipe" /> | <ItemGrid><ItemIcon id="tfmg:steel_pipe" /></ItemGrid> | 钢制流体管道系列，不同于工业管道 |

- [电力](power.electricity.md)，了解独立的 Electro Energetics 电路系统。TFMG 使用自己的分组电力机制，但转换器可能连接不同系统，不要断言两者必然不兼容。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: TFMG Community Edition](images/tfmg-community-edition-icon.png) [Create: TFMG Community Edition](power.industry.md) | 以社区维护版本为机械动力扩展重工业与石油加工。 | <EmiSearch query="@tfmg" /> |
