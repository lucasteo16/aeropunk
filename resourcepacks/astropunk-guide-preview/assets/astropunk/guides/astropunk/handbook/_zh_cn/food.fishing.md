---
navigation:
  title: "钓鱼与水产食材"
  position: 3
  parent: reference.food.md
  icon: minecraft:cod
item_ids:
  - starcatcher:starcatcher_rod
  - starcatcher:starcatcher_guide
  - starcatcher:tackle_box_cyan
  - starcatcher:fish_radar
---

# 钓鱼与水产食材

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Starcatcher%20fishing%20rod%20guide%20minigame%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Starcatcher%20%E9%92%93%E9%B1%BC%20%E9%B1%BC%E7%AB%BF%20%E6%8C%87%E5%8D%97%20%E5%B0%8F%E6%B8%B8%E6%88%8F%20%E6%95%99%E7%A8%8B)

## 先拿到指南


只有 Starcatcher's Rod 能进入 Starcatcher 的渔获表。它的配方需要一个钩和一个浮标，模组明确说明缺少这两样鱼竿不能工作。


Starcatcher's Guide 是每种鱼的查询入口。它会列出鱼需要的生物群系、流体、高度、光照、时间、天气和鱼饵，出门前先读一条词条。

<Recipe id="starcatcher:starcatcher_rod" />

<Recipe id="starcatcher:starcatcher_guide" />

1. 用两根木棍、一根线、一个钩和一个浮标合成鱼竿。
2. 用鱼竿和一本书无序合成指南。
3. 使用指南，或按「打开指南」按键阅读词条。

每条词条都写明生物群系、流体、维度、高度区间与光照，以及时间和天气条件。群系只是第一层筛选，因为同一群系里的地表湖与洞穴水池可能出不同的鱼。先读词条再选水域，条件清单只以指南为准。

<EmiSearch query="@starcatcher" />

***

## 第一次抛竿

![收线中的 Starcatcher 渔获](images/visual-fishing-reeling.png)

收线中的 Starcatcher 渔获

1. 站在符合所选词条的水边抛竿。
2. 等鱼咬钩后收线，鱼上钩会打开小游戏。
3. 用 <KeyBind id="key.starcatcher.minigame_hit" /> 命中高亮区域，直到计量条填满。

渔获入包，或它的桶装形态入包，并且指南记录了词条，才算成功。原版鱼竿在同一片水域仍然只出原版战利品。

***

## 钓具

<ItemGrid><ItemIcon id="starcatcher:hook" /><ItemIcon id="starcatcher:bobber" /></ItemGrid>

每次抛竿都需要一个钩和一个浮标。除此之外，钩、浮标与鱼饵都是同一次抛竿上的调整项，目标鱼的条件写在指南词条里。

<ItemGrid><ItemIcon id="starcatcher:worm" /><ItemIcon id="starcatcher:cherry_bait" /><ItemIcon id="starcatcher:tackle_box_cyan" /></ItemGrid>

鱼饵会改变抛竿的调整项，工具箱可以存放配件并直接更换，不必回合成台。一次只换一项，再抛一次短竿，才能判断是哪一项起了作用。

***


## 留下渔获

<ItemGrid><ItemIcon id="starcatcher:aquarium" /><ItemIcon id="starcatcher:oak_fish_plaque" /><ItemIcon id="starcatcher:tournament_stand" /><ItemIcon id="starcatcher:fish_radar" /></ItemGrid>

多数渔获是食物，做法见[海鲜料理](food.seafood.md)。桶可以带着活鱼，<ItemLink id="starcatcher:aquarium" /> 能养桶装鱼并按记录尺寸缩放模型。<ItemLink id="starcatcher:oak_fish_plaque" /> 把一条渔获挂上墙，<ItemLink id="starcatcher:tournament_stand" /> 用来举办限时比赛，<ItemLink id="starcatcher:fish_radar" /> 读取附近的钓鱼可能性。

- [海鲜料理](food.seafood.md) 把渔获做成料理。
- [饥饿与多样性](food.hunger.md) 把鱼安排进多样饮食。
- [作物食材](food.growing.md) 种出搭配鱼的主食与蔬菜。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Hybrid Aquatic + Starcatcher Compatibility](images/catalog-onrvj8th.png) [Hybrid Aquatic + Starcatcher Compatibility](food.fishing.md) | 把 Hybrid Aquatic 渔获加入 Starcatcher 钓鱼系统。 | <EmiSearch query="@hybrid_aquatic" /> |
| ![Starcatcher](images/catalog-h2jxvxnr.png) [Starcatcher](food.fishing.md) | 加入依栖息地变化的渔获、钓具与钓鱼图鉴。 | <EmiSearch query="@starcatcher" /> |
