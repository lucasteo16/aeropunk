---
navigation:
  title: "饥饿、饮食多样性与食物携带"
  position: 0
  parent: reference.food.md
  icon: minecraft:apple
---

# 饥饿、饮食多样性与食物携带

## 饥饿值与饱和度

<ItemGrid>
  <ItemIcon id="minecraft:apple" />
  <ItemIcon id="minecraft:bread" />
  <ItemIcon id="minecraft:cooked_beef" />
</ItemGrid>

AppleSkin 在食物提示中同时显示饥饿值恢复量与饱和度。饥饿值补充可见的饥饿条，饱和度则是饥饿条下降前先消耗的储备。比较 <ItemLink id="minecraft:bread" /> 与 <ItemLink id="minecraft:cooked_beef" /> 的实际提示，不要凭菜名判断饱腹能力。也可用 <ItemLink id="minecraft:apple" /> 比较水果的恢复量。状态效果与这两个数值是不同属性。

***

## 滚动饮食记录

<ItemGrid>
  <ItemIcon id="solonion:food_book" />
  <ItemIcon id="solonion:lunchbag" />
  <ItemIcon id="solonion:lunchbox" />
  <ItemIcon id="solonion:golden_lunchbox" />
</ItemGrid>

整合包记录最近十六次计入饮食的进食，并启用多样性衰减。每种不同食物只计算其仍在记录中的最强贡献。重复进食会刷新该食物自己的贡献，但不会多出一种食物。其他食物会逐渐变旧，最终离开记录。因此奖励取决于当前饮食，而不是一生吃过多少种。

通过物品栏的饮食按钮或 <ItemLink id="solonion:food_book" /> 查看多样性与奖励。所选版本默认启用物品栏按钮，因此检查饮食不必携带手册。该版本随附的负面惩罚列表为空。重复进食可能降低多样性并失去奖励，但不等于同一食物越吃越少恢复饥饿值。

***

## 准备口粮

<ItemGrid>
  <ItemIcon id="solonion:lunchbag" />
  <ItemIcon id="solonion:lunchbox" />
  <ItemIcon id="solonion:golden_lunchbox" />
</ItemGrid>

用 <ItemLink id="solonion:lunchbag" /> 或 <ItemLink id="solonion:lunchbox" /> 收纳食物。<ItemLink id="solonion:golden_lunchbox" /> 也是容器，并非可食用料理。Short Stacks 会改变食物堆叠上限，装满行囊前先查看实际限制。携带不同成品料理维持饮食多样性，同时单独比较各自的饱腹能力。

- [厨房料理](food.utensils.md)
- [作物食材](food.growing.md)
- [鱼类料理](food.fishing.md)

***

## 相关模组

| 模组或内容 | 状态 | 英文官方简介 |
| --- | --- | --- |
| ![AppleSkin](images/catalog-EsAfCjCV.png) [AppleSkin](food.hunger.md) | 已安装基准版 | Food/hunger-related HUD improvements |
| <ItemImage id="minecraft:wheat" /> [Short Stacks](food.hunger.md) | 已安装基准版 | 食物堆叠上限随饱腹能力变化。 |
| ![Spice of Life Onion](images/catalog-eHGYGKJz.png) [Spice of Life Onion](food.hunger.md) | 已安装基准版 | A mod designed to encourage dietary variety! |
