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

## 鱼竿与钓具

<EmiSearch query="@starcatcher" />

![收竿中的 Starcatcher 渔获](images/visual-fishing-reeling.png)

收竿中的 Starcatcher 渔获

<ItemGrid><ItemIcon id="starcatcher:starcatcher_rod" /><ItemIcon id="starcatcher:starcatcher_guide" /><ItemIcon id="starcatcher:hook" /><ItemIcon id="starcatcher:bobber" /><ItemIcon id="starcatcher:tackle_box_cyan" /></ItemGrid>

Starcatcher 用自带的渔获表、收竿小游戏和图鉴取代原版钓鱼结果。只有本模组的鱼竿能进入这张表。原版钓鱼竿在同一片水域仍然只钓出原版战利品。

| 物品 | 作用 |
| --- | --- |
| <ItemLink id="starcatcher:starcatcher_rod" /> | 抛向 Starcatcher 渔获条目，并开启小游戏。 |
| <ItemLink id="starcatcher:starcatcher_guide" /> | 打开渔获图鉴、每种鱼的条件与小游戏设置。 |
| <ItemLink id="starcatcher:hook" /> | 鱼竿配件，改变鱼在收竿过程中的行为。 |
| <ItemLink id="starcatcher:bobber" /> | 鱼竿配件，改变咬钩时间与可能出现的条目。 |
| <ItemLink id="starcatcher:tackle_box_cyan" /> | 收纳鱼与钓具，不必工作台就能更换配件。 |

***

## 制作鱼竿与图鉴

![钓具箱与鱼竿配件](images/visual-fishing-tackle.png)

钓具箱与鱼竿配件

<Recipe id="starcatcher:starcatcher_rod" />

<Recipe id="starcatcher:starcatcher_guide" />

1. 制作 <ItemLink id="starcatcher:starcatcher_rod" />，第一次抛竿前装好一个鱼钩与一个浮标。
2. 随身带 <ItemLink id="starcatcher:starcatcher_guide" />。鱼种的完整条件只写在这里。
3. 抛入水中，等鱼咬钩后收竿，鱼上钩时小游戏随之开始。
4. 用 <KeyBind id="key.starcatcher.minigame_hit" /> 击中高亮判定区，直到收竿进度填满。

鱼或它的装桶形态进入背包，并且图鉴新增条目，才算这次渔获成立。空竿说明水域符合条件而鱼没有选中，此时应回看图鉴中该鱼种的条件，而不是随意换生物群系。

***

## 配件改变收竿方式

<ItemGrid><ItemIcon id="starcatcher:worm" /><ItemIcon id="starcatcher:cherry_bait" /><ItemIcon id="starcatcher:amethyst_hook" /><ItemIcon id="starcatcher:vanilla_hook" /><ItemIcon id="starcatcher:vanilla_bobber" /><ItemIcon id="minecraft:bucket" /></ItemGrid>

| 配件 | 对渔获的影响 |
| --- | --- |
| <ItemLink id="starcatcher:worm" /> | 常见鱼饵，缩短等待并扩大可出现的条目范围。 |
| <ItemLink id="starcatcher:cherry_bait" /> | 让樱花地形条目比通用池更容易出现。 |
| <ItemLink id="starcatcher:amethyst_hook" /> | 未做下界合金升级时，熔岩钓鱼必需此配件。 |
| 原版风味鱼钩配原版风味浮标 | 跳过小游戏，渔获按普通收竿结算。 |
| <ItemLink id="minecraft:bucket" /> | 作为递交物品，用于图鉴注明可装桶的鱼种。 |

偏好的鱼饵提高鱼种出现的概率。必需的鱼饵是硬性条件，缺少它这次抛竿就不会出现该鱼种。图鉴在每种鱼的条目上标出两者的区别。

***

## 决定渔获的条件

| 条件 | 抛竿前要确认的内容 |
| --- | --- |
| 生物群系 | 条目写明的具体栖息地，而不是附近相似的群系。 |
| 流体 | 水与熔岩分属两张表。熔岩需要紫水晶鱼钩或下界合金鱼竿。 |
| 维度 | 下界与末地条目只在对应维度成立。 |
| 高度与光照 | 同一生物群系内，地表、洞穴与高山条目不同。 |
| 时间与天气 | 群系匹配之后，白天、夜晚、雨天与雷暴仍然是限制。 |

![鱼种条目与垂钓条件](images/visual-fishing-guide.png)

鱼种条目与垂钓条件

这五项都以图鉴为准。栖息地页面只缩小寻找范围，不能覆盖鱼种自身的条件。

***

## Hybrid Aquatic 条目

<ItemGrid><ItemIcon id="starcatcher:starcatcher_rod" /><ItemIcon id="starcatcher:starcatcher_guide" /><ItemIcon id="starcatcher:fish_radar" /></ItemGrid>

<EmiSearch query="@hybrid_aquatic" />

兼容组件把 Hybrid Aquatic 的鱼注册为 Starcatcher 条目，各自带有条件与难度。它们和原生条目一样被记录、展示与计数。浮标旁有 Hybrid Aquatic 的生物在游动，不代表这里能钓到它，因为生物生成与鱼竿条目是两套系统。

***

## 保存与展示渔获

![水族箱中的活体渔获](images/visual-fishing-aquariums.png)

水族箱中的活体渔获

<ItemGrid><ItemIcon id="starcatcher:oak_tackle_box_boat" /><ItemIcon id="starcatcher:aquarium" /><ItemIcon id="starcatcher:oak_fish_plaque" /><ItemIcon id="starcatcher:tournament_stand" /><ItemIcon id="starcatcher:fish_radar" /></ItemGrid>

钓具箱船在走水路时一并携带钓具。水族箱容纳装桶的活鱼，并按记录的体型缩放模型。鱼类标本牌陈列单条渔获。比赛台用于玩家之间的限时比赛。<ItemLink id="starcatcher:fish_radar" /> 读取附近的垂钓可能性，等图鉴已有条目后再做更合适。

***

- [钓鱼栖息地](fishing.habitats.md)
- [海鲜与加工](food.seafood.md)
- [水生生物](adventure.aquatic.md)
- [食物堆叠与多样性](food.hunger.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Hybrid Aquatic + Starcatcher Compatibility](images/catalog-onrvj8th.png) [Hybrid Aquatic + Starcatcher Compatibility](food.fishing.md) | 把 Hybrid Aquatic 渔获加入 Starcatcher 钓鱼系统。 | <EmiSearch query="@hybrid_aquatic" /> |
| ![Starcatcher](images/catalog-h2jxvxnr.png) [Starcatcher](food.fishing.md) | 加入依栖息地变化的渔获、钓具与钓鱼图鉴。 | <EmiSearch query="@starcatcher" /> |
