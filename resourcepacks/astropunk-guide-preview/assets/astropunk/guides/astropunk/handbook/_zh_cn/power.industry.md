---
navigation:
  title: "工业材料与燃料系统"
  position: 10
  parent: reference.machines-storage.md
  icon: minecraft:iron_ingot
---

# 工业材料与燃料系统

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+TFMG+Community+Edition+Materials+%26+fuels+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+TFMG+Community+Edition+%E5%B7%A5%E4%B8%9A%E6%9D%90%E6%96%99%E4%B8%8E%E7%87%83%E6%96%99%E7%B3%BB%E7%BB%9F+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 先有焦炭，再有钢

<EmiSearch query="@tfmg" /> <EmiSearch query="@create" />

Create: The Factory Must Grow 从焦炉开始，因为钢需要焦炭，焦炭需要煤。焦炉是方形多方块结构，从一格到六乘六格，所有炉块必须朝向同一面。

<Recipe id="tfmg:crafting/materials/coke_oven" />

<ItemGrid><ItemIcon id="tfmg:coke_oven" /><ItemIcon id="tfmg:coal_coke" /><ItemIcon id="tfmg:creosote_bucket" /><ItemIcon id="minecraft:coal" /><ItemIcon id="tfmg:casting_basin" /><ItemIcon id="tfmg:industrial_mixer" /><ItemIcon id="tfmg:steel_chemical_vat" /><ItemIcon id="tfmg:copper_cable_hub" /><ItemIcon id="tfmg:steel_distillation_output" /><ItemIcon id="tfmg:steel_fluid_tank" /><ItemIcon id="tfmg:steel_pipe" /></ItemGrid>

| 规则 | 为什么重要 |
| --- | --- |
| 必须是方形 | 长方形无法组装 |
| 所有方块朝同一面 | 输出在标记的那一面 |
| 从顶部抽出二氧化碳 | 积聚会堵住过程 |
| 从其他面抽出杂酚油 | 它是有独立用途的副产物 |

按官方维基说明，更大的方形每批完成得更快，每份产物的杂酚油更少。先建小炉，之后再把大炉当作产量决策。

***

## 炼钢需要热风

高炉把铁变成熔融钢与硅，只靠燃料不行。每次加工都需要热风供应，因此加热炉是结构的一部分，不是升级件。

<ItemGrid><ItemIcon id="tfmg:blast_furnace_output" /><ItemIcon id="tfmg:blast_furnace_hatch" /><ItemIcon id="tfmg:blast_stove" /><ItemIcon id="tfmg:fireproof_bricks" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="tfmg:blast_furnace_output" /> | 输出方块，所有部件朝向它 |
| <ItemLink id="tfmg:blast_furnace_hatch" /> | 输入与操作入口 |
| <ItemLink id="tfmg:blast_stove" /> | 提供热风 |
| <ItemLink id="tfmg:fireproof_bricks" /> 与加固块 | 外壳，以及提速升级 |

运行中的高炉按固定计时消耗燃料，加固方块让每次加工更快。把它建在焦炉旁边，焦炭就不必搬运，同时让输入口保持可被漏斗触及。

***

## 石油、蒸馏与引擎

<ItemGrid><ItemIcon id="tfmg:surface_scanner" /><ItemIcon id="tfmg:pumpjack_base" /><ItemIcon id="tfmg:industrial_pipe" /><ItemIcon id="tfmg:steel_distillation_controller" /><ItemIcon id="tfmg:regular_engine" /><ItemIcon id="tfmg:large_engine" /></ItemGrid>

| 阶段 | 部件 |
| --- | --- |
| 找矿藏 | <ItemLink id="tfmg:surface_scanner" /> 报告区块下方的石油 |
| 抽取 | <ItemLink id="tfmg:pumpjack_base" /> 配管道与传动 |
| 输送 | 用 <ItemLink id="tfmg:industrial_pipe" />，而不是一桶桶搬 |
| 分馏 | <ItemLink id="tfmg:steel_distillation_controller" /> 配输出 |
| 浇铸或混合 | <ItemLink id="tfmg:casting_basin" />、<ItemLink id="tfmg:industrial_mixer" />、<ItemLink id="tfmg:steel_chemical_vat" /> |
| 燃烧 | <ItemLink id="tfmg:regular_engine" />、<ItemLink id="tfmg:simple_large_engine" />、<ItemLink id="tfmg:large_engine" />、<ItemLink id="tfmg:radial_engine" />、<ItemLink id="tfmg:turbine_engine" /> |

引擎是旋转来源，不是发电设备。每个家族对燃料的要求不同，大型引擎接受更粗糙的燃料，但需要稳定的空气供应。铺抽取路线之前先看抽油机条目，管道布局照着做比自行推导容易。

***

## 它自己的电网

<ItemGrid><ItemIcon id="tfmg:generator" /><ItemIcon id="tfmg:electric_motor" /><ItemIcon id="tfmg:heavy_electric_motor" /><ItemIcon id="tfmg:transformer" /><ItemIcon id="tfmg:voltmeter" /><ItemIcon id="tfmg:electricians_wrench" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="tfmg:generator" /> | 把旋转变成电力 |
| <ItemLink id="tfmg:electric_motor" /> | 把电力变回旋转 |
| <ItemLink id="tfmg:heavy_electric_motor" /> | 承担重负载的大型电机 |
| <ItemLink id="tfmg:transformer" /> | 在电压组之间转换 |
| <ItemLink id="tfmg:voltmeter" /> | 读取工业电路 |
| <ItemLink id="tfmg:electricians_wrench" /> | 配置工业电气部件 |
| <ItemLink id="tfmg:winding_machine" /> | 有旋转输入时把线轴绕在原料外 |
| <ItemLink id="tfmg:freezer" /> 与 <ItemLink id="tfmg:compressor" /> | 冷却与压缩工段 |

这套电网不是 Electro Energetics 的电网。两个模组对电的建模方式不同，部件不能互相接入，因此一座建筑选一套并保持一致。[电力](power.electricity.md)说明另一套系统。

下一步是热，因为焦炉与高炉都要烧东西。[燃烧与燃料](power.burners.md)说明供热一侧。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: TFMG Community Edition](images/tfmg-community-edition-icon.png) [Create: TFMG Community Edition](power.industry.md) | 以社区维护版本为机械动力扩展重工业与石油加工。 | <EmiSearch query="@tfmg" /> |
