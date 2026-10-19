---
navigation:
  title: "生产可再生原料"
  position: 6
  parent: reference.machines-storage.md
  icon: create:mechanical_drill
---

# 生产可再生原料

## 本包的喷口在水下

<EmiSearch query="@molten_vents" /> <EmiSearch query="@create" />

熔岩喷口是可再生的 Create 矿石岩来源。本包关闭了陆地喷口，只开启水下喷口，因此在陆地上找是白费力气。沿海床寻找。

<ItemGrid><ItemIcon id="molten_vents:dormant_molten_asurine" /><ItemIcon id="molten_vents:active_molten_asurine" /><ItemIcon id="molten_vents:active_molten_veridium" /><ItemIcon id="molten_vents:active_molten_crimsite" /><ItemIcon id="molten_vents:active_molten_ochrum" /><ItemIcon id="molten_vents:active_molten_scorchia" /><ItemIcon id="molten_vents:active_molten_scoria" /></ItemGrid>

| 方块 | 状态 |
| --- | --- |
| 休眠喷口方块 | 在喷口外壳内部，尚未激活 |
| 激活喷口方块 | 熔岩落上去时产出对应石材 |
| 矿石岩 | 喷口产出的建筑与粉碎材料 |

共有六个家族，蔚蓝岩、辉绿岩、绯红岩、赭金岩、焦黑岩与焦岩。每个家族都有休眠与激活形态。要找的是带岩浆的那一块，而不是周围普通的矿石岩。

***

## 三步唤醒喷口

1. 挖开喷口内部的方块，直到找到与周围矿石岩相同、但表面带岩浆的那一块。
2. 用爆炸破坏这块休眠核心。一块炸药或一只充能苦力怕就足以引爆。
3. 看岩浆变亮。这一块此时已经激活。

<ItemGrid><ItemIcon id="minecraft:tnt" /><ItemIcon id="molten_vents:active_molten_ochrum" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| 步骤 | 可能遇到的情况 | 原因 |
| --- | --- | --- |
| 爆炸没有反应 | 打错了方块 | 普通矿石岩外观相似，核心带岩浆 |
| 喷口仍然发暗 | 爆炸距离太远 | 爆炸必须触及核心方块 |
| 熔岩停在表面 | 喷口仍在休眠 | 必须先激活再倒熔岩 |

在开阔水域操作，留出走位空间。本包的喷口在海里，所以要带呼吸手段和光源。

***

## 熔岩进去，石材出来

倒在激活喷口上的熔岩会变成该喷口的矿石岩。熔岩被消耗并替换成石头，因此喷口是转换器，不是发生器。

<ItemGrid><ItemIcon id="minecraft:lava_bucket" /><ItemIcon id="create:hose_pulley" /><ItemIcon id="create:mechanical_pump" /><ItemIcon id="create:fluid_pipe" /></ItemGrid>

| 供料方式 | 适用场合 |
| --- | --- |
| 手提水桶 | 验证喷口，一次几组 |
| 熔岩湖上的 <ItemLink id="create:hose_pulley" /> | 湖体足够大，可视为无限 |
| 从储罐抽取 | 已经在为燃料或浇铸搬运熔岩 |

本包里软管滑轮把一万格以上的水体视为无限，因此地下的熔岩湖比洞穴里的一小池熔岩更值钱。滑轮触及 128 格，通常足以架在喷口上方，让石头落向下方收集。

喷口产出的石头走正常矿物路线。[矿物加工](machines.ore-processing.md)说明如何粉碎与洗涤，[物料输送](machines.logistics.md)说明把它运走的传送带。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Molten Vents](images/create-molten-vents-icon.png) [Create: Molten Vents](machines.renewables.md) | 通过熔融喷口提供可再生的机械动力含矿石材。 | <EmiSearch query="@molten_vents" /> |
