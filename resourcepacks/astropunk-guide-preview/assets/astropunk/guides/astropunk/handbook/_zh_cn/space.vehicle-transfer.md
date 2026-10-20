---
navigation:
  title: "轨道飞行"
  position: 10
  parent: reference.vehicles.md
  icon: rocketnautics:rocket_thruster
item_ids:
  - rocketnautics:rocket_thruster
---

# 轨道飞行

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Orbital+flight+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+%E8%BD%A8%E9%81%93%E9%A3%9E%E8%A1%8C+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 运载火箭

<EmiSearch query="@rocketnautics" />

![地球轨道上的飞船](images/feedback-earth-orbit.png)

地球轨道上的飞船

<ItemGrid><ItemIcon id="rocketnautics:rocket_thruster" /><ItemIcon id="rocketnautics:booster_thruster" /><ItemIcon id="rocketnautics:thruster_mount" /><ItemIcon id="rocketnautics:rcs_thruster" /><ItemIcon id="rocketnautics:fluid_hose" /><ItemIcon id="rocketnautics:titanium_ingot" /></ItemGrid>

轨道飞船是装有火箭发动机、燃料供给与推力座的模拟悬浮体。按[组装](vehicles.assembly.md)造好船体，再装发动机。

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="rocketnautics:rocket_thruster" /> | 主推力，燃烧液体燃料 |
| <ItemLink id="rocketnautics:booster_thruster" /> | 首段爬升的额外推力 |
| <ItemLink id="rocketnautics:thruster_mount" /> | 把发动机固定在船体上 |
| <ItemLink id="rocketnautics:rcs_thruster" /> | 进入真空后的微调 |
| <ItemLink id="rocketnautics:fluid_hose" /> | 把燃料从储罐送到发动机 |

发动机烧的是燃料，不是旋转力。通过船体流体系统供油，并让储罐高于发动机进油口，因为进油口干了就没有推力，储罐再满也没用。

## 越入深空

本包把转移高度设在 20000。爬升越过这个高度，飞船与船上乘客一起进入深空。这是世界高度，不是离发射台的高度，所以建在山上的基地起点更高。

| 高度 | 变化 | 应对 |
| --- | --- | --- |
| 7000 | 阻力降为零 | 不要再依赖螺旋桨 |
| 20000 | 进入深空的转移高度 | 越界时留好返程燃料 |
| 21000 | 低密度空气与溺水 | 船上备好密闭头盔与空气供给 |

越界之前就要备好空气供给，详见[太空生命维持](space.life-support.md)。

天空颜色变化不代表已经转移。看世界高度与维度名称，不要看风景。

## 抵达

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="rocketnautics:rcs_thruster" /><ItemIcon id="simulated:altitude_sensor" /><ItemIcon id="simulated:velocity_sensor" /><ItemIcon id="create:mechanical_crafter" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

在深空中接近已连接的天体，向内越过同一个转移高度。飞船会出现在该地表上方很高的位置，既没有着陆，也没有自动驾驶，所以越界之前先计划下降。

1. 提前收油，让重力完成剩下的工作。
2. 留一部分燃料给着陆点火，返程还要再越一次高度。
3. 看高度传感器与速度传感器，不要看风景，低重力下地面来得很快。
4. 在平地着陆。落在斜坡上的船体会先滑动再停下。

月球表面加速度是 2.0，主世界是 11.0，在家门口能轻着陆的同一套下降，在那里会冲过头。要减的是下降点火力度，不只是接近速度。

返程就是反向越界。重新爬升到 20000 以上，进入深空，接近主世界再下降。两次越界都要留够燃料，因为月球上没有加油站，除非你自己建一座。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | 可交互移动方块结构框架。 | 无独立物品查询 |
