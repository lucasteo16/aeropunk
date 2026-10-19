---
navigation:
  title: "携带便携储存装备"
  position: 0
  parent: reference.machines-storage.md
  icon: minecraft:shulker_box
---

# 携带便携储存装备

## 背包承担工作负载

<EmiSearch query="@sophisticatedbackpacks" />

<ItemLink id="sophisticatedbackpacks:backpack" /> 是穿在身上的箱子。每一级增加储存格与升级槽，取下背包时里面的东西仍然保留。

<ItemGrid><ItemIcon id="sophisticatedbackpacks:backpack" /><ItemIcon id="sophisticatedbackpacks:copper_backpack" /><ItemIcon id="sophisticatedbackpacks:iron_backpack" /><ItemIcon id="sophisticatedbackpacks:gold_backpack" /><ItemIcon id="sophisticatedbackpacks:diamond_backpack" /><ItemIcon id="sophisticatedbackpacks:netherite_backpack" /></ItemGrid>

| 等级 | 储存格 | 升级槽 |
| --- | --- | --- |
| <ItemLink id="sophisticatedbackpacks:backpack" /> | 9 | 1 |
| <ItemLink id="sophisticatedbackpacks:copper_backpack" /> | 18 | 1 |
| <ItemLink id="sophisticatedbackpacks:iron_backpack" /> | 27 | 2 |
| <ItemLink id="sophisticatedbackpacks:gold_backpack" /> | 36 | 2 |
| <ItemLink id="sophisticatedbackpacks:diamond_backpack" /> | 45 | 3 |
| <ItemLink id="sophisticatedbackpacks:netherite_backpack" /> | 54 | 3 |

皮革背包是第一件。之后每一步都是升级你已经在背的那一只，里面的东西会跟着升级保留。钻石一步需要潜影壳，下界合金一步是锻造升级。

本包有一条容易踩到的规则。潜影盒，包括加固潜影盒，都不能放进背包。服务端配置把原版与加固潜影盒全部列为背包禁用物品，因此背包不能用来套放潜影储存。

***

## 值得占一个槽的升级

<EmiSearch query="@chipped" /> <EmiSearch query="@create" />

<ItemGrid><ItemIcon id="sophisticatedbackpacks:upgrade_base" /><ItemIcon id="sophisticatedbackpacks:crafting_upgrade" /><ItemIcon id="sophisticatedbackpacks:stonecutter_upgrade" /><ItemIcon id="sophisticatedbackpacks:tool_swapper_upgrade" /><ItemIcon id="sophisticatedbackpacks:refill_upgrade" /><ItemIcon id="sophisticatedbackpacks:feeding_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/alchemy_bench_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/botanist_workbench_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/carpenters_table_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/glassblower_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/loom_table_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/mason_table_upgrade" /><ItemIcon id="sophisticatedbackpacks:chipped/tinkering_table_upgrade" /><ItemIcon id="sophisticatedbackpacks:jukebox_upgrade" /></ItemGrid>

| 升级 | 省掉什么 |
| --- | --- |
| <ItemLink id="sophisticatedbackpacks:crafting_upgrade" /> | 外出的工作台 |
| <ItemLink id="sophisticatedbackpacks:stonecutter_upgrade" /> | 切石机，用于成形方块 |
| <ItemLink id="sophisticatedbackpacks:tool_swapper_upgrade" /> | 开物品栏换工具 |
| <ItemLink id="sophisticatedbackpacks:refill_upgrade" /> | 从背包补满快捷栏那一叠 |
| <ItemLink id="sophisticatedbackpacks:feeding_upgrade" /> | 战斗中从背包进食 |

<Recipe id="sophisticatedbackpacks:upgrade_base" />

<Recipe id="sophisticatedbackpacks:crafting_upgrade" />

升级基底需要黄铜，因此第一件升级出现在 Create 工坊之后，而不是之前。本包还带七个 Chipped 工作站升级，把背包变成便携的植物学家工作台、吹玻璃台、木工台、石匠台、织布机、炼金台或修补台。

堆叠倍率、嵌套便携容器、自动加工、流体储存、能量储存与生物捕捉在这里都不可用。按基础版本规划，不要期待升级版。

***

## 大批搬运用潜影盒

<EmiSearch query="@reinfshulker" />

<ItemGrid><ItemIcon id="minecraft:shulker_box" /><ItemIcon id="reinfshulker:copper_shulker_box" /><ItemIcon id="reinfshulker:iron_shulker_box" /><ItemIcon id="reinfshulker:gold_shulker_box" /><ItemIcon id="reinfshulker:diamond_shulker_box" /><ItemIcon id="reinfshulker:netherite_shulker_box" /></ItemGrid>

| 潜影盒 | 格数 | 说明 |
| --- | --- | --- |
| 原版潜影盒 | 27 | 破坏后保留内容 |
| <ItemLink id="reinfshulker:copper_shulker_box" /> | 45 | 第一个加固等级 |
| <ItemLink id="reinfshulker:iron_shulker_box" /> | 54 | 与双箱相同 |
| <ItemLink id="reinfshulker:gold_shulker_box" /> | 81 | 三个箱子 |
| <ItemLink id="reinfshulker:diamond_shulker_box" /> | 108 | 四个箱子 |
| <ItemLink id="reinfshulker:netherite_shulker_box" /> | 108 | 抗爆炸、火焰与熔岩 |

加固潜影盒由加固箱子或成形配方制作，下界合金等级是锻造升级。任何等级都能染色，这是给一整面储存墙贴标签最便宜的办法。

Easy Shulker Boxes 让你直接从物品栏打开受支持的潜影盒，不必放下。本包默认把 Shulker Drops Two 的掉落设为两个壳，因此潜影农场回本更快。

下一步是工厂能自己装满的储存。[大宗储存](storage.bulk.md)说明储物仓与筒仓。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Easy Shulker Boxes](images/catalog-ga5eun8s.png) [Easy Shulker Boxes](storage.portable.md) | 让玩家直接在物品栏中查看与存取潜影盒内容。 | 无独立物品查询 |
| ![Reinforced Shulker Boxes](images/catalog-xlowusdn.png) [Reinforced Shulker Boxes](storage.portable.md) | 增加存储容量更大的升级潜影盒。 | <EmiSearch query="@reinfshulker" /> |
| ![Shulker Drops Two](images/catalog-ujxiyw47.png) [Shulker Drops Two](storage.portable.md) | 调整潜影贝壳掉落数量与概率，支持一次掉落两个壳。 | 无独立物品查询 |
| <ItemImage id="minecraft:chest" /> [Sophisticated Backpacks](storage.portable.md) | 增加可染色的分级背包，并提供指定的实用升级。 | <EmiSearch query="@sophisticatedbackpacks" /> |
| <ItemImage id="minecraft:chest" /> [Sophisticated Backpacks Create Integration](storage.portable.md) | 连接背包与 Create 原生移动结构。尚未验证 Sable 载具兼容性。 | 无独立物品查询 |
