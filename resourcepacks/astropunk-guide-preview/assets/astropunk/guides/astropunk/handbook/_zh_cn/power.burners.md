---
navigation:
  title: "加工供热"
  position: 7
  parent: reference.machines-storage.md
  icon: minecraft:lava_bucket
---

# 加工供热

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+blaze+burner+feeding+liquid+fuel+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+%E7%87%83%E7%83%A7%E5%99%A8+%E6%B6%B2%E4%BD%93%E7%87%83%E6%96%99+%E6%95%99%E7%A8%8B)

## 给上方机器供热

<EmiSearch query="@create" />

<GameScene zoom="3" interactive={true}>
<Block id="create:blaze_burner" />
<Block y="1" id="create:basin" />
</GameScene>

工作盆位于燃烧器正上方。图中只展示供热位置，不是完整的搅拌装置。

<ItemLink id="create:blaze_burner" /> 为正上方的方块供热。热不是传动轴旋转，也不是电。先合成 <ItemLink id="create:empty_blaze_burner" />，再手持空燃烧器右键烈焰人捕获它，或使用烈焰人刷怪笼。之后把燃烧器放在需要热量的机器下方。

<Recipe id="create:crafting/kinetics/empty_blaze_burner" />

| 状态或输入 | 外观 | 结果 |
| --- | --- | --- |
| 空笼 | <ItemGrid><ItemIcon id="create:empty_blaze_burner" /></ItemGrid> | 不供热 |
| 捕获烈焰人 | <ItemGrid><ItemIcon id="create:blaze_burner" /></ItemGrid> | 加燃料后提供普通热 |
| <ItemLink id="create:blaze_cake" /> | <ItemGrid><ItemIcon id="create:blaze_cake" /></ItemGrid> | 提供超级加热 |

燃烧器工作时会改变可见状态。检查燃烧器状态与上方机器，不要根据传动轴在转就推断有热量。

***

## 手动或管道供料

<ItemGrid><ItemIcon id="create:blaze_burner" /><ItemIcon id="minecraft:lava_bucket" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /></ItemGrid>

1. 手动启动时，手持可燃物品右键燃烧器。要超级加热则喂入烈焰蛋糕。
2. 自动送入物品时用机械手或机械臂。漏斗或丢落物品不是文档记载的供料方式。
3. 输送流体时，用管道连接储罐与燃烧器，再驱动机械泵朝燃烧器方向抽送。

熔岩提供普通热。流体供料先从熔岩开始。燃料兼容性取决于燃烧器和燃料形态，不要因为另一种液体能在工业引擎中燃烧，就直接拿来替代。

- [钢铁与石油](power.industry.md) 焦炭、钢铁、石油加工与引擎。
- [旋转动力](machines.rotation.md) 独立的传动轴网络。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | 让机械动力烈焰人燃烧室使用泵入的液体燃料。 | 无独立物品查询 |
| <ItemImage id="create:crushing_wheel" /> [Create: Unified Fuels](power.burners.md) | 连接支持的 Create 燃料系统，不增加独立物品系列。 | 无独立物品查询 |
