---
navigation:
  title: "太空导航"
  position: 0
  parent: reference.vehicles.md
  icon: rocketnautics:hologram_block
item_ids:
  - rocketnautics:hologram_block
  - rocketnautics:sputnik
---

# 太空导航

## 行星总览

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@rocketnautics_addon" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="rocketnautics:hologram_block" />
  <ItemIcon id="rocketnautics:sputnik" />
</ItemGrid>

<ItemLink id="rocketnautics:hologram_block" />

<Recipe id="rocketnautics:hologram_block" />

放置全息桌，即可按不同缩放比例查看宇宙。短按桌面上的配置点可以调整显示比例。它适合作为天体总览，不是目的地选择器，也不是自动驾驶控制器。

<ItemLink id="rocketnautics:sputnik" />

<Recipe id="rocketnautics:sputnik" />

Sputnik Probe 是一个持续运行的区块加载器，也会报告生物群系颜色。物品说明提及与 ComputerCraft 的制图集成，但这项集成不是航线控制。

基础 Cosmonautics 行星数据包括主世界、月球、火星、气态巨行星与冰世界。独立的火星维度由 Create Cosmonautics Expansion 提供。在这些天体中，连接到可登陆地表的维度只有月球与火星。

- [太空目的地](space.destinations.md) 查看已包含的可登陆世界。
- [轨道飞行](space.vehicle-transfer.md) 查看物理飞船的转换边界。

***

## 头盔显示

在深空中，<ItemLink id="rocketnautics:space_helmet" /> 提供轨道显示。使用 <KeyBind id="key.rocketnautics.toggle_alignment" /> 切换对齐辅助，模组默认按键为 Y。该功能只改变显示，不会控制飞船转向。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | 新增轨道飞行、月球、火箭与呼吸装备，以及行星展示。 | <EmiSearch query="@rocketnautics" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics Expansion](space.navigation.md) | 新增可登陆的火星维度、地貌与行星数据。 | <EmiSearch query="@rocketnautics_addon" /> |
