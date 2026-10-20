---
navigation:
  title: "用机器制作食物"
  position: 9
  parent: reference.food.md
  icon: minecraft:smoker
---

# 用机器制作食物

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Create%20Slice%20and%20Dice%20slicer%20sprinkler%20Central%20Kitchen%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Create%20Slice%20and%20Dice%20%E5%88%87%E7%89%87%E6%9C%BA%20%E6%B4%92%E6%B0%B4%E5%99%A8%20%E4%B8%AD%E5%A4%AE%E5%8E%A8%E6%88%BF%20%E6%95%99%E7%A8%8B)

## 第一次切片

<EmiSearch query="@create" /> <EmiSearch query="@sliceanddice" />

![受热烹饪锅旁的机械备料](images/visual-automatic-cooking.png)


<Recipe id="sliceanddice:slicer" />

<ItemLink id="sliceanddice:slicer" /> 执行切菜板配方。它自己的 Ponder 条目是 Cutting with the slicer，从切片机物品打开，那一段演示的就是受支持的搭建方式。手持刀或斧右键机器即可装刀，本整合包把这两种都当作切割工具。

1. 把切片机朝向目标摆放。对着传送带或置物台时一次切一件，对着大锅时处理锅里的物品。
2. 手持要用的刀或斧右键装刀。
3. 从传动轴提供旋转动力。方向不对时用 <ItemLink id="create:gearshift" /> 换向，它通过红石信号切换输出方向。
4. 送入一颗卷心菜，从输出侧收叶片。

漏斗或滑槽负责把物品送进送出，这才让单台机器变成产线。成功的标志和切菜板一致：一颗卷心菜出两张叶片。

工具会磨损。本整合包开启了工具耐久消耗，搭长产线之前先备好备用刀或维修方案。

锅类配方是另一种情况。Slice and Dice 把它们转换成受热搅拌配方，也就是大锅上方的搅拌机，而不是切片机直接煮整份料理。本整合包的大锅烹饪热度条件是 HEATED，所以锅下方需要烈焰人燃烧室提供热量。

***

## 洒水器

<ItemGrid><ItemIcon id="sliceanddice:sprinkler" /></ItemGrid>

洒水器喷洒的是装入的流体，流体决定效果。它通过管道供给，放在管道下方，不需要旋转动力。

| 流体 | 作用 |
| --- | --- |
| 水 | 打湿下方地面，让耕地保持湿润 |
| <ItemGrid><ItemIcon id="sliceanddice:fertilizer_bucket" /></ItemGrid> <ItemLink id="sliceanddice:fertilizer_bucket" /> | 对作物施加骨粉效果 |
| 药水 | 对范围内的生物施加对应效果 |
| 岩浆 | 对范围内的生物造成伤害 |

本整合包把洒水器储罐设为 300 毫桶、每次消耗 100 毫桶，水平范围五个方块。

液体肥料在搅拌机里用堆肥制成。在田地上方放洒水器之前先建好肥料供应，因为水能保持耕地湿润，但不会施加肥料的骨粉催熟效果。

***

## 中央厨房

<EmiSearch query="@farmersdelight" />

Central Kitchen 把 Create 物流接到 Farmer's Delight 设备上，并自带 Ponder 演示。要看的条目是 Cutting board、Cooking pot 与 Heat source，也就是这些搭建受支持的目标。

| 机器 | 辨认 | 在这里做什么 |
| --- | --- | --- |
| <ItemLink id="create:mechanical_arm" /> | <ItemGrid><ItemIcon id="create:mechanical_arm" /></ItemGrid> | 把原料放到切菜板上，也给烹饪锅装料 |
| <ItemLink id="create:deployer" /> | <ItemGrid><ItemIcon id="create:deployer" /></ItemGrid> | 使用模式下装刀，在板上切割原料 |
| <ItemLink id="create:mechanical_saw" /> | <ItemGrid><ItemIcon id="create:mechanical_saw" /></ItemGrid> | 不用刀物品就能切割已转换的切菜板配方 |
| <ItemLink id="create:andesite_funnel" /> | <ItemGrid><ItemIcon id="create:andesite_funnel" /></ItemGrid> | 把做好的食物从锅里取出 |
| <ItemLink id="create:blaze_burner" /> | <ItemGrid><ItemIcon id="create:blaze_burner" /></ItemGrid> | 为锅或煎锅提供热量 |

本整合包开启了切菜板到锯切与到机械手的两条转换路线，所以锯和机械手都可用。

- [作物食材](food.growing.md) 这些机器处理的作物。
- [烹饪工具与料理](food.utensils.md) 被自动化的设备。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Slice & Dice](images/slice-and-dice-icon.png) [Create Slice & Dice](food.machine-cooking.md) | 增加自动进行 Farmer's Delight 食材处理的机械动力机器。 | <EmiSearch query="@sliceanddice" /> |
| ![Create: Central Kitchen](images/create-central-kitchen-icon.png) [Create: Central Kitchen](food.machine-cooking.md) | 将其他烹饪模组接入机械动力机器，实现食物自动加工。 | 无独立物品查询 |
