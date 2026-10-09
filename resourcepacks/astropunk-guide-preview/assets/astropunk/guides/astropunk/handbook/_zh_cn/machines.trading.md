---
navigation:
  title: "手动交易与自动交易"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
---

# 手动交易与自动交易

## 交易置物台

- 浏览物品: <EmiSearch query="@trading_floor" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="trading_floor:trading_depot" />
  <ItemIcon id="minecraft:lectern" />
  <ItemIcon id="minecraft:emerald" />
  <ItemIcon id="create:brass_funnel" />
  <ItemIcon id="create:mechanical_arm" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="trading_floor:trading_depot" /> | Create: Trading Floor 将交易置物台连接到村民工作站。 |
| <ItemLink id="minecraft:lectern" />, <ItemLink id="minecraft:emerald" /> | 交易来自村民与其工作站，并非新机器自动生成配方。 |
| <ItemLink id="create:brass_funnel" />, <ItemLink id="create:mechanical_arm" /> | 用 Create 输送组件提供交易原料并收集产物。 |

***

## 初次使用

制作交易置物台并连接到村民使用的工作站。村民在正常工作时段再次工作时才会交易。双原料交易可使用两个置物台，其过滤条件须一致或其中一个为空。两种布局均有思索演示。

<Recipe id="trading_floor:trading_depot" />

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create: Trading floor](images/create-trading-floor-icon.png) [Create: Trading floor](machines.trading.md) | 通过机械动力机器自动进行村民交易。 | 已安装基准版 | <EmiSearch query="@trading_floor" /> |
