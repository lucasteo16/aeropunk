---
navigation:
  title: "太空导航"
  position: 12
  parent: reference.vehicles.md
  icon: rocketnautics:hologram_block
item_ids:
  - rocketnautics:hologram_block
  - rocketnautics:sputnik
---

# 太空导航

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Cosmonautics+hologram+Earth+Moon+navigation+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Cosmonautics+%E5%85%A8%E6%81%AF%E5%9B%BE+%E5%9C%B0%E7%90%83+%E6%9C%88%E7%90%83+%E5%AF%BC%E8%88%AA+%E6%95%99%E7%A8%8B)

## 行星显示

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

![全息行星显示](images/cosmo-hologram.png)

全息行星显示

<ItemLink id="rocketnautics:hologram_block" /> 绘制所在星系。短按它的配置点可以改变比例，在消耗燃料之前先看清目标天体。

<ItemGrid><ItemIcon id="rocketnautics:hologram_block" /><ItemIcon id="rocketnautics:sputnik" /><ItemIcon id="rocketnautics:space_helmet" /></ItemGrid>

显示只是模型，不是目的地选择器。在它上面选中天体不会操控飞船，也不会开启转移。

本包真正使用的是转移高度。主世界与月球都在高度 20000 把载体送入深空，从深空返回也在这个高度进入。对准天体，越过高度，就完成了移动。

## 天体与重力

<Recipe id="rocketnautics:hologram_block" />

本包星系把主世界和月球连接到地表维度。全息图还显示其他天体，不要仅因看见模型就规划着陆。

| 已连接地表 | 配置表面加速度 | 对飞行的影响 |
| --- | --- | --- |
| 主世界 | 11.0 | 重力强于月球 |
| 月球 | 2.0 | 悬停所需推力更小，应重新调整操作幅度 |

初始速度相同时，低重力不会让下落加速更快。推进、载具质量和当前速度仍会影响结果，应实际测试悬停与制动，不要照搬主世界油门。

主世界高度超过 5,000 后就无法正常呼吸，早于阻力在 7,000 降为零和上升至 20,000 时的转移。发射前就应戴好头盔并充满供气设备。所选版本的大气表使用高度上界：21,000 是低密度溺水区间的上界，不是起点。深空与月球同样需要呼吸方案。参见[生命维持](space.life-support.md)与[太空飞行](space.vehicle-transfer.md)。

## 探测器与头盔

<ItemLink id="rocketnautics:sputnik" /> 保持区块加载并报告生物群系颜色用于制图。它是勘测工具，不是驾驶员，也不会替你飞航线。

在深空中，太空头盔会显示轨道信息。按 <KeyBind id="key.rocketnautics.toggle_alignment" /> 切换对齐辅助。它改变你看到的内容，不改变船的朝向。

<Recipe id="rocketnautics:sputnik" />


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
