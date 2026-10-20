---
navigation:
  title: "饥饿、饮食多样性与食物携带"
  position: 1
  parent: reference.food.md
  icon: minecraft:apple
---

# 饥饿、饮食多样性与食物携带

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Farmer%27s%20Delight%20hunger%20saturation%20diet%20variety%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20%E5%86%9C%E5%A4%AB%E4%B9%90%E4%BA%8B%20%E9%A5%A5%E9%A5%BF%20%E9%A5%B1%E5%92%8C%E5%BA%A6%20%E9%A5%AE%E9%A3%9F%E5%A4%9A%E6%A0%B7%E6%80%A7%20%E6%95%99%E7%A8%8B)

## 先看懂食物

<ItemGrid><ItemIcon id="minecraft:bread" /><ItemIcon id="minecraft:cooked_beef" /><ItemIcon id="minecraft:apple" /></ItemGrid>

本整合包安装了 AppleSkin，食物提示会直接显示两个数值，不需要按键。

| 行 | 控制什么 | 显示位置 |
| --- | --- | --- |
| 饥饿值 | 回复可见的饥饿条 | 物品提示与饥饿条预览 |
| 饱和度 | 饥饿值下降前先消耗的隐藏储备 | 物品提示与饱和度叠加显示 |
| 效果 | 带时长的药水图标 | 物品提示与自身效果列表 |

饱和度决定疾跑与战斗时饥饿条能撑多久，所以饥饿值更低、饱和度更高的食物可能更耐久。效果行是选择的另一半，它属于那道料理，而不属于某一类食物。

***

## 舒适与滋养

<EmiSearch query="@farmersdelight" />

Farmer's Delight 增加了两种效果，本整合包保留了原版汤类覆盖，所以普通汤也有它们。

<ItemGrid><ItemIcon id="minecraft:mushroom_stew" /><ItemIcon id="minecraft:beetroot_soup" /><ItemIcon id="minecraft:rabbit_stew" /></ItemGrid>

| 效果 | 作用 | 可见标志 |
| --- | --- | --- |
| 舒适 | 无论多饿都提供自然生命恢复 | 生命条上的滚动叠加，本整合包已开启 |
| 滋养 | 阻止饥饿条下降，用饱和度回血时除外 | 饥饿条上的金色叠加，本整合包已开启 |

受伤又饿到无法自然回血时，要找带舒适的食物。长时间战斗前，要找带滋养的食物，因为饥饿条不再下降。直接读手上料理的效果行，效果来自物品本身，不来自碗或盘子。

汤类覆盖包括 <ItemLink id="minecraft:mushroom_stew" />、<ItemLink id="minecraft:beetroot_soup" /> 与 <ItemLink id="minecraft:rabbit_stew" />，本整合包还让这三种汤像料理一样堆叠到十六。

***

## 食物多样性

<EmiSearch query="@solonion" />

<ItemGrid><ItemIcon id="solonion:food_book" /><ItemIcon id="solonion:lunchbag" /><ItemIcon id="solonion:lunchbox" /><ItemIcon id="solonion:golden_lunchbox" /></ItemGrid>

本整合包记录最近十六种计入的料理，旧记录会逐时衰减退出。每种不同食物占一条最强记录，再吃一次只刷新这条，不会新增。

<ItemLink id="solonion:food_book" /> 显示当前食物多样性、各阈值上下方的好处，以及仍在计入的食物队列。好处是属性类的，包含生命、伤害、生命恢复、移动速度与护甲韧性，所以记录越宽，属性收益越实在，而不只是习惯。

| 设定 | 本整合包的取值 | 结果 |
| --- | --- | --- |
| 记录数量 | 16 | 只统计近期料理 |
| 多样性衰减 | 开启 | 旧记录会退出 |
| 重复食用 | 刷新一条 | 再吃同一道菜不提高多样性 |

两种不同的汤加一份盛宴分餐，比一整箱相同的炖菜更有用，食物书也会写明还差几餐才解锁下一档好处。

***

## 带饭出门

<ItemGrid><ItemIcon id="solonion:lunchbag" /><ItemIcon id="solonion:lunchbox" /><ItemIcon id="solonion:golden_lunchbox" /></ItemGrid>

<ItemLink id="solonion:lunchbag" /> 用一个格子装多种料理。潜行并使用它打开容器，把食物放进去。饥饿时直接使用装有食物的容器即可进食，不会打开界面。用一个铁块可升级成 <ItemLink id="solonion:lunchbox" />，保留内容并增加容量，<ItemLink id="solonion:golden_lunchbox" /> 是最大形态。

- [烹饪工具与料理](food.utensils.md) 锅、切菜板与料理分组。
- [作物食材](food.growing.md) 用农田作物做便宜碗装料理。
- [海鲜料理](food.seafood.md) 用鱼类拓宽饮食记录。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![AppleSkin](images/catalog-esafcjcv.png) [AppleSkin](food.hunger.md) | 在物品提示与饥饿条中显示食物恢复量及饱和度。 | 无独立物品查询 |
| <ItemImage id="minecraft:wheat" /> [Short Stacks](food.hunger.md) | 调整食物堆叠上限，改变每格物品栏可携带的食物数量。 | 无独立物品查询 |
| ![Spice of Life Onion](images/catalog-ehgygkjz.png) [Spice of Life Onion](food.hunger.md) | 根据近期饮食的滚动记录奖励食物多样性。 | <EmiSearch query="@solonion" /> |
