---
navigation:
  title: "调整模型与动画"
  position: 0
  parent: reference.appearance.md
  icon: minecraft:armor_stand
---

# 调整模型与动画

## 模型支持

Entity Model Features 与 Entity Texture Features 提供自定义模型与纹理支持。Model Gap Fix 修复可见模型缝隙。自定义动画外观也取决于已启用资源包。

| 内容 | 作用 |
| --- | --- |
| [EMF] Entity Model Features | 加载兼容资源包中的自定义实体模型。 |
| [ETF] Entity Texture Features | 支持随机、自定义与发光实体纹理。 |
| Model Gap Fix | 修复方块与物品模型的缝隙。 |

***

## 动画兼容

<EmiSearch query="@create" />

EMF Compat: Create 使机械动力动画适配动态玩家模型，其共享框架列在支持库页面。

| 内容 | 作用 |
| --- | --- |
| EMF Compat: Create | 使机械动力玩家动画适配自定义动态模型。 |

***

## 动作与生成动画

<EmiSearch query="@spawn" />

重型版增加进食、方块交互、第三人称动作与敌对生物生成动画。自定义动态模型需要启用兼容资源包。

| 内容 | 作用 |
| --- | --- |
| Eating Animations（仅重型版） | 增加进食动画。 |
| Fancy World Animations [FWA]（仅重型版） | 为门、拉杆等可交互方块增加动画。 |
| EMF Compat: Not Enough Animations（仅重型版） | 使 Not Enough Animations 适配自定义动态玩家模型。 |
| Not Enough Animations（仅重型版） | 在第三人称显示更多玩家动作。 |
| Spawn Animations Compats（仅重型版） | 为 Spawn Animations 补充兼容数据。 |
| Spawn Animations（仅重型版） | 为敌对生物生成增加动画。 |

***

## 相关页面

- [资源包](visuals.resource-packs.md)
- [支持库](technical.libraries.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![[EMF] Entity Model Features](images/catalog-4I1XuqiY.png) [[EMF] Entity Model Features](visuals.models.md) | 加载兼容资源包中的自定义实体模型。 | 无独立物品查询 |
| ![[ETF] Entity Texture Features](images/catalog-BVzZfTc1.png) [[ETF] Entity Texture Features](visuals.models.md) | 支持随机、自定义与发光实体纹理。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [Eating Animations](visuals.models.md) （仅重型版） | 增加进食动画。 | 无独立物品查询 |
| ![EMF Compat: Create](images/catalog-J9McOdzy.png) [EMF Compat: Create](visuals.models.md) | 使机械动力玩家动画适配自定义动态模型。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [EMF Compat: Not Enough Animations](visuals.models.md) （仅重型版） | 让 Not Enough Animations 玩家动作适配 Entity Model Features 自定义模型。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [Fancy World Animations [FWA]](visuals.models.md) （仅重型版） | 为门、拉杆等可交互方块增加动画。 | 无独立物品查询 |
| ![Model Gap Fix](images/catalog-QdG47OkI.png) [Model Gap Fix](visuals.models.md) | 修复方块与物品模型的缝隙。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [Not Enough Animations](visuals.models.md) （仅重型版） | 在第三人称显示更多玩家动作。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [Spawn Animations](visuals.models.md) （仅重型版） | 为敌对生物生成增加动画。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [Spawn Animations Compats](visuals.models.md) （仅重型版） | 让 Spawn Animations 的生成动画适配受支持的模组生物。 | 无独立物品查询 |
