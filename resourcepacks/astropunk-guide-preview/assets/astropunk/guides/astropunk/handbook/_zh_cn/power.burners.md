---
navigation:
  title: "提供液体燃烧燃料"
  position: 9
  parent: reference.machines-storage.md
  icon: minecraft:lava_bucket
---

# 提供液体燃烧燃料

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Liquid+Fuel+Create%3A+Unified+Fuels+Liquid+fuels+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Liquid+Fuel+Create%3A+Unified+Fuels+%E6%8F%90%E4%BE%9B%E6%B6%B2%E4%BD%93%E7%87%83%E7%83%A7%E7%87%83%E6%96%99+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 热是独立的资源

<EmiSearch query="@create" />

<ItemLink id="create:blaze_burner" /> 为它上方的方块供热。它不是旋转，也不是电力，因此一台机器可能旋转充足却毫无反应，因为它的燃烧器是冷的。

先做一只 <ItemLink id="create:empty_blaze_burner" />。这是合成出来的物品，不是已收服的烈焰人。

<Recipe id="create:crafting/kinetics/empty_blaze_burner" />

<ItemGrid><ItemIcon id="create:empty_blaze_burner" /><ItemIcon id="create:blaze_burner" /><ItemIcon id="minecraft:blaze_rod" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| 状态 | 看到什么 |
| --- | --- |
| 空燃烧器 | 冷笼子，不供热 |
| 有燃料的燃烧器 | 内有烈焰人，普通热，两侧有火 |
| 过热燃烧器 | 火焰更高，供需要过热的配方使用 |

收服烈焰人时，放下空燃烧器，让烈焰人走进去。内有烈焰人的燃烧器可以用扳手取下搬走，烈焰人不会丢失。

***

## 投料或用管道供料

<ItemGrid><ItemIcon id="create:blaze_burner" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| 途径 | 得到什么 |
| --- | --- |
| 投入可燃物品 | 燃料持续期间提供普通热 |
| 烈焰蛋糕 | 过热，供明确要求过热的配方 |
| 通过管道送入液体燃料 | 不必手动补料的普通热 |
| 熔岩 | 只有普通热，从不过热 |

让管道途径成立的是 Create: Liquid Fuel。它不新增燃烧器，而是让现有燃烧器接受来自储罐的流体，因此一只储罐可以通过管道与泵供给一整排燃烧器。

本包的泵向两侧各输送 16 格流体，储罐每格存 8 桶。工作盆下方三只燃烧器需求不大，通常一只储罐就够。

***

## 统一燃料不等于任何燃料

<EmiSearch query="@tfmg" />

Create: Unified Fuels 通过共享燃料组连接受支持的用能设备，它生成兼容数据，不新增机器。所选版本覆盖 The Factory Must Grow、Crafts and Additions 的燃烧器、Liquid Fuel 与 Stuff 'N Additions 的加注罐等系统，前提是对应模组存在。

<ItemGrid><ItemIcon id="create:blaze_burner" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="tfmg:regular_engine" /></ItemGrid>

| 问题 | 答案在哪里 |
| --- | --- |
| 这种流体在这里能烧吗 | 看用能设备自己的条目，不看流体名称 |
| 能否过热 | 只有燃烧器列为可过热的燃料才行 |
| 柴油能被燃烧器接受吗 | 只有该燃烧器的燃料组包含它才行 |

精炼中间产物、工艺化学品与蒸汽不会自动成为可燃燃料。共享燃料供应服务于本来就接受同一燃料组的设备，它不是万能转换器。

跨基地铺线之前先用一桶测试。燃烧器拒收，说明该流体不在它的燃料组里，再多的管道也改变不了。

热与旋转在同一台机器上会合。[旋转动力](machines.rotation.md)说明传动一侧，[工业机械](power.industry.md)说明最耗热的炉子。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | 让机械动力烈焰人燃烧室使用泵入的液体燃料。 | 无独立物品查询 |
| <ItemImage id="create:crushing_wheel" /> [Create: Unified Fuels](power.burners.md) | 连接支持的 Create 燃料系统，不增加独立物品系列。 | 无独立物品查询 |
