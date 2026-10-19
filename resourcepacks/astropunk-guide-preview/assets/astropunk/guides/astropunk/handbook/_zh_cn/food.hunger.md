---
navigation:
  title: "饥饿、饮食多样性与食物携带"
  position: 1
  parent: reference.food.md
  icon: minecraft:apple
---

# 饥饿、饮食多样性与食物携带

## 解读食物数值

![餐桌上的多种料理](images/visual-shared-feast.png)

餐桌上的多种料理

<ItemGrid><ItemIcon id="minecraft:apple" /><ItemIcon id="minecraft:bread" /><ItemIcon id="minecraft:cooked_beef" /></ItemGrid>

本包装有 AppleSkin，所有食物提示都会直接显示饥饿值与饱和度，不必按住按键。在物品栏里把光标移到 <ItemLink id="minecraft:bread" />、<ItemLink id="minecraft:cooked_beef" /> 或 <ItemLink id="minecraft:apple" /> 上，先读两行数值再决定带什么。

饥饿值一行补充可见的饥饿条。饱和度一行是饥饿条下降前先消耗的隐藏储备。饱和度高的食物即使饥饿值较低，也能让饥饿条在奔跑、跳跃和战斗中维持更久。AppleSkin 还会在饥饿条上叠加饱和度，并预览手中食物能补充的量，吃之前就能看到差多少。

状态效果与这两个数值无关。一份料理可能恢复的饥饿值很少，却能提供有用的效果。

| 提示行 | 控制的内容 | 查看位置 |
| --- | --- | --- |
| 饥饿值 | 补充可见饥饿条 | 食物提示与饥饿条预览 |
| 饱和度 | 饥饿值下降前消耗的隐藏储备 | 食物提示与饱和度叠加 |
| 效果 | 药水图标与持续时间 | 食物提示与物品栏 |

***

## 饮食多样性

<EmiSearch query="@solonion" />

<ItemGrid><ItemIcon id="solonion:food_book" /><ItemIcon id="solonion:lunchbag" /><ItemIcon id="solonion:lunchbox" /><ItemIcon id="solonion:golden_lunchbox" /></ItemGrid>

本包记录最近十六次计入饮食的进食，并启用多样性衰减。每种不同食物只贡献其仍在记录中的最强条目。再次吃同一种食物只会刷新它，不会多出一条记录。其他食物会逐渐离开记录，因此奖励取决于当前饮食，而不是过去吃过的全部种类。

从物品栏按钮或 <ItemLink id="solonion:food_book" /> 打开饮食界面。物品栏按钮默认启用，不把手册放进背包也能查看多样性。随包提供的负面惩罚列表为空，饮食单一只会少拿奖励，不会附加惩罚效果。

| 设置 | 本包取值 | 影响 |
| --- | --- | --- |
| 记录餐数 | 16 | 只有近期进食计入 |
| 多样性衰减 | 启用 | 旧记录会离开列表 |
| 物品栏饮食按钮 | 启用 | 不带手册也能查看 |
| 负面惩罚列表 | 空 | 重复进食没有惩罚 |

重复进食会降低多样性，但不会让同一种食物恢复的饥饿值变少。

***

## 盛装形式的效果

<EmiSearch query="@farmersdelight" />

<ItemGrid><ItemIcon id="farmersdelight:beef_stew" /><ItemIcon id="farmersdelight:steak_and_potatoes" /><ItemIcon id="minecraft:mushroom_stew" /></ItemGrid>

农夫乐事把两种效果绑定在盛装形式上。像 <ItemLink id="farmersdelight:beef_stew" /> 这样的碗装料理给予舒适，即使饥饿值过低无法正常回血，自然恢复仍会继续。像 <ItemLink id="farmersdelight:steak_and_potatoes" /> 这样的盘装料理给予滋养，暂停奔跑、跳跃和攻击造成的饥饿值与饱和度消耗。

本包启用了汤类覆盖，原版汤和炖菜也会给予滋养。只差一份便宜的 <ItemLink id="minecraft:mushroom_stew" /> 就能在旅途中止住饥饿值下降。

| 盛装形式 | 效果 | 适用场合 |
| --- | --- | --- |
| 碗装料理 | 舒适 | 饥饿时仍要恢复生命 |
| 盘装料理 | 滋养 | 战斗或长跑中维持饥饿条 |
| 原版汤 | 滋养 | 前期便宜的止饿食物 |

***

## 出行口粮

![食物手册、餐袋与餐盒](images/visual-diet-containers.png)

食物手册、餐袋与餐盒

<ItemGrid><ItemIcon id="solonion:lunchbag" /><ItemIcon id="solonion:lunchbox" /><ItemIcon id="solonion:golden_lunchbox" /></ItemGrid>

用 <ItemLink id="solonion:lunchbag" /> 或 <ItemLink id="solonion:lunchbox" /> 收纳料理。<ItemLink id="solonion:golden_lunchbox" /> 是更大的容器，不是另一种料理。Short Stacks 按饥饿值限制每格可放的食物数量，越饱腹的料理占用的格子越多。容器能腾出物品栏位置，但不会改变堆叠上限。

带两三种不同料理，而不是只带一叠。这样十六次进食记录保持多样，也能同时准备一份舒适料理和一份滋养料理，应对不同情况。

- [厨房料理](food.utensils.md)
- [作物食材](food.growing.md)
- [鱼类料理](food.seafood.md)

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![AppleSkin](images/catalog-esafcjcv.png) [AppleSkin](food.hunger.md) | 在物品提示与饥饿条中显示食物恢复量及饱和度。 | 无独立物品查询 |
| <ItemImage id="minecraft:wheat" /> [Short Stacks](food.hunger.md) | 调整食物堆叠上限，改变每格物品栏可携带的食物数量。 | 无独立物品查询 |
| ![Spice of Life Onion](images/catalog-ehgygkjz.png) [Spice of Life Onion](food.hunger.md) | 根据近期饮食的滚动记录奖励食物多样性。 | <EmiSearch query="@solonion" /> |
