---
navigation:
  title: "选择引擎与推进装置"
  position: 6
  parent: reference.vehicles.md
  icon: create:steam_engine
---

# 选择引擎与推进装置

## 推进家族

<EmiSearch query="@aeroengineering" /> <EmiSearch query="@rocketnautics" /> <EmiSearch query="@createpropulsion" /> <EmiSearch query="@create" />

![飞行器发动机工坊](images/visual-engine-workshop.png)

飞行器发动机工坊

<ItemGrid><ItemIcon id="createpropulsion:thruster" /><ItemIcon id="createpropulsion:vector_thruster" /><ItemIcon id="createpropulsion:solid_fuel_thruster" /><ItemIcon id="createpropulsion:ion_thruster" /><ItemIcon id="aeroengineering:engine_fan" /><ItemIcon id="aeroengineering:engine_turbine" /><ItemIcon id="rocketnautics:rocket_thruster" /><ItemIcon id="aeronautics:propeller_bearing" /><ItemIcon id="aeroengineering:turbine_component" /></ItemGrid>

本整合包有四种推动载体的方式，彼此不能互换。先选家族，再照着该家族自己的帮助做。

| 家族 | 产生运动的方式 | 需要 | 适用 |
| --- | --- | --- | --- |
| 螺旋桨轴承 | 让帆面结构在空气中旋转 | 旋转力与帆面 | 飞艇与飞机 |
| Create Propulsion 推进器 | 喷出流体或燃烧固体燃料 | 燃料与信号 | 大气与太空 |
| AeroEngine 涡轮 | 压缩并点燃煤油 | 完整核心与燃料 | 高速飞机 |
| 火箭推进器 | 在真空中燃烧液体燃料 | 燃料箱与输送 | 轨道发射 |

## Create Propulsion 推进器

<ItemGrid><ItemIcon id="createpropulsion:thruster" /><ItemIcon id="createpropulsion:vector_thruster" /><ItemIcon id="createpropulsion:solid_fuel_thruster" /><ItemIcon id="createpropulsion:liquid_vector_thruster" /><ItemIcon id="createpropulsion:ion_thruster" /><ItemIcon id="createpropulsion:stirling_engine" /></ItemGrid>

<ItemLink id="createpropulsion:thruster" /> 需要流体与红石输入。2x2 与 3x3 形式由同一种方块拼成，输入更多，属于更大的发动机，而不是另一种机器。

<ItemLink id="createpropulsion:vector_thruster" /> 可以让推力偏转。除前后两面外，每一面都有红石输入，给某一面通电，喷口就朝那一面转。信号强度 0 到 15 决定偏离中心的幅度，摇杆通道正是这样接进来的。液体矢量版本在此基础上增加了流体推力。

<ItemLink id="createpropulsion:solid_fuel_thruster" /> 从尾部装入固体物品燃烧，不需要管道。<ItemLink id="createpropulsion:ion_thruster" /> 消耗 Forge 能量与红石，推力小但持久，适合位置保持而不是起飞。

<ItemLink id="createpropulsion:stirling_engine" /> 方向相反，底部受热后输出旋转力，用来带动螺旋桨或泵，而不是推动船体。

## 涡轮核心

<ItemGrid><ItemIcon id="aeroengineering:engine_fan" /><ItemIcon id="aeroengineering:engine_compressor" /><ItemIcon id="aeroengineering:engine_combustor" /><ItemIcon id="aeroengineering:engine_turbine" /><ItemIcon id="aeroengineering:engine_exhaust_cone" /><ItemIcon id="aeroengineering:aviation_kerosene_bucket" /><ItemIcon id="aeroengineering:aviation_alloy_ingot" /><ItemIcon id="aeroengineering:aviation_alloy_sheet" /><ItemIcon id="aeroengineering:aviation_blade" /><ItemIcon id="aeroengineering:compressor_component" /></ItemGrid>

AeroEngine 核心按固定顺序叠放，风扇、压气机、燃烧室、涡轮、尾喷口。先造核心，再按该发动机的思索场景补外壳、喷口、燃料供给与齿轮箱。没有燃料供给的核心不会转出任何东西。

<Recipe id="aeroengineering:compressor_component" />

## 燃料与来源

<ItemGrid><ItemIcon id="aeroengineering:aviation_kerosene_bucket" /><ItemIcon id="createpropulsion:turpentine_bucket" /><ItemIcon id="createpropulsion:platinum_ingot" /><ItemIcon id="minecraft:lava_bucket" /><ItemIcon id="minecraft:redstone" /></ItemGrid>

| 燃料或输入 | 供给对象 | 供给方式 |
| --- | --- | --- |
| 航空煤油 | AeroEngine 涡轮 | 用流体管道接入发动机 |
| 松节油 | Create Propulsion 推进器 | 流体管道或储罐 |
| 固体物品 | 固体燃料推进器 | 从尾部装入 |
| 熔岩 | 火箭推进器 | 船体流体系统 |
| Forge 能量与红石 | 离子推进器 | 电力网络与信号 |

桶图标代表的是流体，这里没有任何步骤要求你放入桶。Create: The Factory Must Grow 也产出煤油，燃料兼容附属让 AeroEngine 可以接受它，因此一条炼油线能同时供应两个发动机家族。炼油流程见[石油与工业](power.industry.md)。

## 本包中的推力

<ItemGrid><ItemIcon id="aeronautics:propeller_bearing" /><ItemIcon id="aeronautics:wooden_propeller" /><ItemIcon id="aeronautics:andesite_propeller" /><ItemIcon id="aeronautics:smart_propeller" /></ItemGrid>

整合包按部件而不是按家族缩放推力。螺旋桨轴承只有基准推力的 0.2，木质、安山岩与智能螺旋桨都是 1.0。所以一个大螺旋桨胜过几个小轴承，只有两块帆面的轴承能推动轻船体，却推不动重船体。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![AeroEngine](images/catalog-crh10ijf.png) [AeroEngine](vehicles.engines.md) | 为机械动力增加模块化航空发动机与飞行控制仪表。 | <EmiSearch query="@aeroengineering" /> |
| ![AeroEngine fuel compat](images/cosmo-rnuszf19-icon.png) [AeroEngine fuel compat](vehicles.engines.md) | 让 AeroEngine 使用 Create: The Factory Must Grow 的煤油。 | <EmiSearch query="@aeroengineering" /> <EmiSearch query="@tfmg" /> |
| ![Create Propulsion: Simulated](images/catalog-apkohno9.png) [Create Propulsion: Simulated](vehicles.engines.md) | 增加推动 Sable 与 Aeronautics 载具的燃料推进器及电力推进器。 | <EmiSearch query="@createpropulsion" /> |
