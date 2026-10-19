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

## 行星显示

<EmiSearch query="@rocketnautics" />

![全息行星显示](images/cosmo-hologram.png)

全息行星显示

<ItemLink id="rocketnautics:hologram_block" /> 绘制所在星系。短按它的配置点可以改变比例，在消耗燃料之前先看清目标天体。

<ItemGrid><ItemIcon id="rocketnautics:hologram_block" /><ItemIcon id="rocketnautics:sputnik" /><ItemIcon id="rocketnautics:space_helmet" /></ItemGrid>

显示只是模型，不是目的地选择器。在它上面选中天体不会操控飞船，也不会开启转移。

本包真正使用的是转移高度。主世界与月球都在高度 20000 把载体送入深空，从深空返回也在这个高度进入。对准天体，越过高度，就完成了移动。

## 天体与重力

<Recipe id="rocketnautics:hologram_block" />

本包的星系数据给每个天体设定了表面加速度。主世界是 11.0，月球是 2.0，所以按主世界调好的着陆器在月球上会比预想落得更快。在家门口轻松悬停的船，到那里会爬升更快、制动更晚。

| 天体 | 表面加速度 | 说明 |
| --- | --- | --- |
| 主世界 | 11.0 | 起点，空气浓厚 |
| 月球 | 2.0 | 低重力，没有浓厚空气 |
| 火星、气态巨行星、冰世界 | 在显示中列出 | 出发前先确认 |

空气也随高度变稀。21000 以上本包把大气标记为低密度并施加溺水效果，所以没有密闭头盔与供气的船员在越界之前就无法呼吸。阻力到 7000 已经降为零，这就是螺旋桨在高空失效、必须换用火箭的原因。

## 探测器与头盔

<ItemLink id="rocketnautics:sputnik" /> 保持区块加载并报告生物群系颜色用于制图。它是勘测工具，不是驾驶员，也不会替你飞航线。

在深空中，太空头盔会显示轨道信息。按 <KeyBind id="key.rocketnautics.toggle_alignment" /> 切换对齐辅助。它改变你看到的内容，不改变船的朝向。

<Recipe id="rocketnautics:sputnik" />

## 出发前读一遍

| 检查项 | 为何决定这趟行程 |
| --- | --- |
| 目标天体的表面加速度 | 决定下落速度与所需制动力 |
| 头盔与充满的空气供给 | 21000 以上空气无法支持呼吸 |
| 无空气仍有效的推进 | 螺旋桨到 7000 就失去介质 |
| 已组装的船体与运行中的燃料供给 | 未组装的结构没有物理，断油则没有推力 |


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
