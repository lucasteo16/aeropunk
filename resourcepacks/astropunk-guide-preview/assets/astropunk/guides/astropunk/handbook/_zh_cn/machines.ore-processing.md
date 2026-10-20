---
navigation:
  title: "加工矿石与原料"
  position: 4
  parent: reference.machines-storage.md
  icon: create:millstone
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# 加工矿石与原料

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Almost+Unified+Ore+processing+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Almost+Unified+%E5%8A%A0%E5%B7%A5%E7%9F%BF%E7%9F%B3%E4%B8%8E%E5%8E%9F%E6%96%99+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 三个阶段各自的收益

<EmiSearch query="@create" />

粗矿直接烧炼只得到一块锭。先粉碎、再洗涤粉碎矿，能在同样的锭之外拿到经验，还有机会得到第二种材料，因此这些额外机器靠你已经挖到的矿就能回本。

先做一台 <ItemLink id="create:millstone" />。它需要旋转，但不需要水，也不需要第二只轮子，是用来看清整条流程最便宜的方式。

<ItemGrid><ItemIcon id="create:millstone" /><ItemIcon id="create:crushing_wheel" /><ItemIcon id="create:encased_fan" /></ItemGrid>

| 机器 | 旋转需求 | 作用 |
| --- | --- | --- |
| <ItemLink id="create:millstone" /> | 任意转速，4 点应力 | 磨碎，一次一个物品 |
| <ItemLink id="create:crushing_wheel" /> | 一对轮子，每只 8 点应力 | 粉碎，可大量投入 |
| <ItemLink id="create:encased_fan" /> | 任意转速，2 点应力 | 洗涤、烟熏、熔炼、缠魂 |

<Recipe id="create:crafting/kinetics/millstone" />

磨石也是谷物机器。投入小麦得到小麦粉，另有种子作为副产物。

<ItemGrid><ItemIcon id="minecraft:wheat" /><ItemIcon id="create:millstone" /><ItemIcon id="create:wheat_flour" /><ItemIcon id="minecraft:wheat_seeds" /></ItemGrid>

要看到的结果是机器持续转动、物品不断通过。如果它停住，说明应力网络超载，而不是机器坏了。应力预算由[旋转动力](machines.rotation.md)统一说明。

***

## 先粉碎再烧炼

一对 <ItemLink id="create:crushing_wheel" /> 相对放置，中间留出缝隙。丢进缝隙的物品会被粉碎，掉进去的生物也会受伤。

<ItemGrid><ItemIcon id="minecraft:raw_iron" /><ItemIcon id="create:crushed_raw_iron" /><ItemIcon id="create:experience_nugget" /></ItemGrid>

| 输入 | 产物 | 额外 |
| --- | --- | --- |
| 一个粗铁 | 一个粉碎铁矿 | 百分之七十五概率得到一个经验颗粒 |

整合包加入的每种矿都有自己的粉碎条目，配方浏览器会显示你手上那种矿的具体一行。磨石对谷物做类似的事，把小麦磨成小麦粉。

即使不需要矿粉，经验颗粒也是粉碎的理由。把颗粒和机械压床放进工作盆压制，之后触碰就能取出经验。

***

## 洗涤粉碎矿

洗涤需要穿过水的空气。在风扇正面直接放一格水源，物品放在水的另一侧，风扇就会把洗好的产物推向远端。

<ItemGrid><ItemIcon id="create:crushed_raw_iron" /><ItemIcon id="create:encased_fan" /><ItemIcon id="minecraft:water_bucket" /><ItemIcon id="minecraft:iron_nugget" /><ItemIcon id="minecraft:redstone" /></ItemGrid>

| 输入 | 产物 | 额外 |
| --- | --- | --- |
| 一个粉碎铁矿 | 九个铁粒 | 百分之七十五概率得到一个红石 |

九个铁粒合成一块锭，所以洗涤本身不增加铁。它增加的是红石，并把矿变成与锭同样方便堆叠的形态。本包把风扇加工时间设为 150 游戏刻，满速风扇下约七秒半。

水是加工介质，不是原料。水桶图标代表那格水方块，风扇不会消耗它。

***

## 当两种矿同名时

<EmiSearch query="@createdeco" />

本包的 Almost Unified 只统一共享的安山合金板与锌板配方标签，并优先采用 Create Deco 的产物。其余物品仍保留各自模组注册的那一件。

<ItemGrid><ItemIcon id="create:andesite_alloy" /></ItemGrid>

| 情况 | 做法 |
| --- | --- |
| 配方写着某种板 | 看配方浏览器接受的原料，而不是材料名称 |
| 要做精确物品过滤器 | 匹配配方真正消耗的那件物品 |
| 战利品或首领掉落看起来相同 | 当作另一件物品处理 |

名称相同不代表两件物品在精确物品过滤器里可以互换。做过滤器之前先看配方，整合包更新后再看一次。

下一步是不靠手搬，把这些机器连起来。[物料输送](machines.logistics.md)说明传送带、滑槽与机械臂。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Almost Unified](images/catalog-sdasaqez.png) [Almost Unified](machines.ore-processing.md) | 仅统一共享的安山合金与锌板配方材料。 | 无独立物品查询 |
| ![Create](images/create-icon.png) [Create](machines.ore-processing.md) | 增加用于加工、运输与自动建造的旋转动力机器。 | <EmiSearch query="@create" /> |
