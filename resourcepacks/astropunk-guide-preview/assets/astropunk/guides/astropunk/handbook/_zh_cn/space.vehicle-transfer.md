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

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Cosmonautics+Rocketnautics+rocket+Moon+transfer+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Cosmonautics+%E7%81%AB%E7%AE%AD+%E6%9C%88%E7%90%83+%E7%BB%B4%E5%BA%A6%E8%BD%AC%E7%A7%BB+%E6%95%99%E7%A8%8B)

## 运载火箭

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

![地球轨道上的飞船](images/feedback-earth-orbit.png)

<ItemGrid><ItemIcon id="rocketnautics:rocket_thruster" /><ItemIcon id="rocketnautics:booster_thruster" /><ItemIcon id="rocketnautics:thruster_mount" /><ItemIcon id="rocketnautics:rcs_thruster" /><ItemIcon id="rocketnautics:titanium_ingot" /></ItemGrid>

轨道飞船是装有火箭推进、储油和控制系统的已组装 Sable 载具。先按[组装](vehicles.assembly.md)完成船体，在低空验证燃料供给和转向，再尝试转移。

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="rocketnautics:rocket_thruster" /> | 火箭主推进 |
| <ItemLink id="rocketnautics:booster_thruster" /> | 额外发射推力 |
| <ItemLink id="rocketnautics:thruster_mount" /> | 推进器安装部件 |
| <ItemLink id="rocketnautics:rcs_thruster" /> | 姿态与机动推力 |

火箭燃料不是旋转动力。按所选推进器的配方与燃料要求连接管路，确认流体确实送达。储罐位置更高并不能证明供油正常。燃料与熔岩精炼流程应查配方浏览器，不要假定任意流体都能燃烧。

## 越入深空

![地表转移高度示意，非比例图](images/transport-space-transfer-zh_cn.png)

本包把转移高度设在 20000。爬升越过这个高度，飞船与船上乘客一起进入深空。这是世界高度，不是离发射台的高度，所以建在山上的基地起点更高。

| 高度 | 变化 | 应对 |
| --- | --- | --- |
| 7000 | 阻力降为零 | 不要再依赖螺旋桨 |
| 20000 | 进入深空的转移高度 | 越界时留好返程燃料 |
| 高于 5,000 | 主世界无法正常呼吸 | 发射前戴好头盔并充满供气设备 |

越界之前就要备好空气供给，详见[太空生命维持](space.life-support.md)。

天空颜色变化不代表已经转移。看世界高度与维度名称，不要看风景。

## 抵达

<ItemGrid><ItemIcon id="rocketnautics:rcs_thruster" /><ItemIcon id="simulated:altitude_sensor" /><ItemIcon id="simulated:velocity_sensor" /><ItemIcon id="create:mechanical_crafter" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

目的地必须配置了对应的地表维度。本包连接主世界与月球。全息图中出现某个天体，不代表它有可着陆世界。

从深空接近目标天体的转移边界。地表到达高度为 19,000，低于上升转移阈值 20,000，因此到达不等于落地。开始受控下降前先确认维度、高度与速度。

1. 留够制动、着陆和返程爬升的燃料。越界不会自动让飞船停下。
2. 用 <ItemLink id="simulated:altitude_sensor" /> 和 <ItemLink id="simulated:velocity_sensor" /> 判断高度与下降速度，保持载具可控，不要简单收油自由落体。
3. 用短暂调整测试制动。月球配置的表面加速度为 2.0，主世界为 11.0。低重力会改变悬停所需推力，不代表飞船反而下落更快。
4. 在空旷地面着陆后再拆解。返程重新爬升到 20,000 以上，在深空中朝主世界航行，再控制第二次下降。

高速进入天体很危险。成功转移不代表着陆速度安全。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | 可交互移动方块结构框架。 | 无独立物品查询 |
