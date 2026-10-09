---
navigation:
  title: "用机器制作食物"
  position: 0
  parent: reference.food.md
  icon: minecraft:apple
---

# 用机器制作食物

## 切片

- 浏览物品: <EmiSearch query="@farmersdelight" /> <EmiSearch query="@sliceanddice" />

<ItemGrid>
  <ItemIcon id="sliceanddice:slicer" />
  <ItemIcon id="farmersdelight:cutting_board" />
  <ItemIcon id="farmersdelight:flint_knife" />
</ItemGrid>

<ItemLink id="sliceanddice:slicer" /> 自动执行切割，并不会把所有食材直接做成完整料理。<ItemLink id="farmersdelight:flint_knife" /> 是手工切割工具。先决定切割产物，再供应所需原料与工具。组装方式可查看原生 Ponder 帮助。手工 <ItemLink id="farmersdelight:cutting_board" /> 配方说明了整块食材与分切小份为何是不同原料。

### 切片机合成

<Recipe id="sliceanddice:slicer" />

先制作 <ItemLink id="sliceanddice:slicer" />，再连接原料运输并装入所需切割工具。

***

## 饮品与农业流体

- 浏览物品: <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="farmersdelight:hot_cocoa" />
  <ItemIcon id="farmersdelight:apple_cider" />
  <ItemIcon id="sliceanddice:sprinkler" />
  <ItemIcon id="sliceanddice:fertilizer_bucket" />
</ItemGrid>

Slice & Dice 为 <ItemLink id="farmersdelight:hot_cocoa" /> 与 <ItemLink id="farmersdelight:apple_cider" /> 提供 Create 注液和排液配方。流体处理与准备饮品原料是不同加工阶段。<ItemLink id="sliceanddice:sprinkler" /> 与 <ItemLink id="sliceanddice:fertilizer_bucket" /> 用于作物生产，并非料理盛装容器。

***

## 厨房整合

Create: Central Kitchen 提供烹饪整合，并非另一套食物菜单。连接食材输送和成品仓储前，先查看目标料理的实际机器配方。共用食材不代表所有锅中料理都有机器版本。

- [烹饪工具](food.utensils.md)
- [作物生产](food.growing.md)
- [机器与仓储](reference.machines-storage.md)

***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create Slice & Dice](images/slice-and-dice-icon.png) [Create Slice & Dice](food.machine-cooking.md) | 增加自动进行 Farmer's Delight 食材处理的机械动力机器。 | 已安装基准版 | <EmiSearch query="@sliceanddice" /> |
| ![Create: Central Kitchen](images/create-central-kitchen-icon.png) [Create: Central Kitchen](food.machine-cooking.md) | 将其他烹饪模组接入机械动力机器，实现食物自动加工。 | 已安装基准版 | 无独立物品查询 |
