---
navigation:
  title: "钓鱼栖息地"
  position: 4
  parent: reference.food.md
  icon: minecraft:salmon
---

# 钓鱼栖息地

## 栖息地类型

<EmiSearch query="@hybrid_aquatic" /> <EmiSearch query="@starcatcher" />

![鱼种条目与垂钓条件](images/visual-fishing-guide.png)

鱼种条目与垂钓条件

<ItemGrid><ItemIcon id="starcatcher:starcatcher_guide" /><ItemIcon id="starcatcher:fish_radar" /></ItemGrid>

栖息地是第一道筛选，它描述三者的关系，你站立的水域、周围的地形，以及图鉴允许出现在此的鱼种。下表的地形标记用于辨认地形，不代表鱼。先对上标记，再到图鉴确认鱼种。

| 栖息地 | 地形标记 | 可期待的渔获 |
| --- | --- | --- |
| 寒冷淡水 | <ItemGrid><ItemIcon id="minecraft:ice" /></ItemGrid> Birch Taiga、Windswept Spires、冬季岛屿 | Frostjaw Trout、Wintery Pike |
| 温暖淡水 | <ItemGrid><ItemIcon id="minecraft:cactus" /></ItemGrid> 沙漠、恶地、热带草原、Granite Cliffs | Sandtail、Scorchfish、Mirage Carp、Agave Bream、Cactifish、Oasis Sturgeon |
| 樱花地形 | <ItemGrid><ItemIcon id="minecraft:cherry_sapling" /></ItemGrid> Sakura Grove、Sakura Valley、Snowy Cherry Grove、Spring Skylands | Blossomfish、Pink Koi |
| 繁花地形 | <ItemGrid><ItemIcon id="minecraft:poppy" /></ItemGrid> 繁花森林、Cloud Forest、Moonlight 地形 | Petal Bass |
| 开阔草地 | <ItemGrid><ItemIcon id="minecraft:sunflower" /></ItemGrid> 草原及类似的开阔草地 | Sunflower Carp |
| 黑森林 | <ItemGrid><ItemIcon id="minecraft:dark_oak_sapling" /></ItemGrid> 黑森林与 Moonlight 林地 | 魔法森林渔获 |
| 冰雪地形 | <ItemGrid><ItemIcon id="minecraft:packed_ice" /></ItemGrid> 冰冻峭壁、Glacial Chasm、Emerald Peaks | Aurora 与其他冰刺渔获 |
| 繁茂洞穴 | <ItemGrid><ItemIcon id="minecraft:moss_block" /></ItemGrid> 繁茂洞穴、真菌洞穴、Underground Jungle | Lush Pike、Mossfin、Shadowfin |
| 岩石洞穴 | <ItemGrid><ItemIcon id="minecraft:pointed_dripstone" /></ItemGrid> 滴水石洞穴、石质洞穴、地热洞穴 | Dripfin、Fossilized Angelfish |
| 深暗之域 | <ItemGrid><ItemIcon id="minecraft:sculk" /></ItemGrid> 深暗之域、Frostfire Caves | Sculkfish、Ward、Glowing Dark |
| 海洋 | <ItemGrid><ItemIcon id="minecraft:prismarine_crystals" /></ItemGrid> 海洋、深海、暖水海洋、Deep Warm Ocean | 海洋与深海渔获，以及 Hybrid Aquatic 海鱼 |

Snowy Badlands 是值得记住的例外。它看起来像温暖的恶地，整合包却把它归入寒冷淡水，因此六种暖水湖鱼种不会在那里出现。

***

## 四步选定钓点

1. 按上表认地形标记，不要只凭记忆中的群系名称。
2. 站到该地形内的水边。群系符合但脚下没有水块，就钓不到任何东西。
3. 在 <ItemLink id="starcatcher:starcatcher_guide" /> 中查看该鱼种的高度、光照、时间、天气与鱼饵条件。
4. 抛竿一次。渔获成立并写入图鉴，就说明栖息地对上了。

![寒冷湖泊岸边的垂钓](images/visual-fishing-reeling.png)

寒冷湖泊岸边的垂钓

***

## 同一群系内高度会分流

<ItemGrid><ItemIcon id="minecraft:ice" /><ItemIcon id="minecraft:sculk" /><ItemIcon id="minecraft:pointed_dripstone" /></ItemGrid>

| 同一群系中的位置 | 变化 |
| --- | --- |
| 地表湖泊或河流 | 地表淡水渔获，天气与日照条件仍然适用。 |
| 洞穴水域 | 地下渔获取代地表鱼种，繁茂洞穴与滴水石洞穴另有自己的条目。 |
| 高山或峭壁水潭 | 同样的群系在低海拔没有的寒冷与冰雪渔获会在此出现。 |

| 流体与维度 | 变化 |
| --- | --- |
| 熔岩 | 独立渔获表，需要紫水晶鱼钩或下界合金鱼竿。 |
| 下界的水 | 并不存在，下界条目属于熔岩。 |
| 末地的水 | 末地条目要求身处末地，看起来相似的主世界水池不行。 |

***

## Terralith 地形

<ItemGrid><ItemIcon id="minecraft:moss_block" /><ItemIcon id="minecraft:cherry_sapling" /><ItemIcon id="minecraft:dark_oak_sapling" /></ItemGrid>

整合包把全部九十五种 Terralith 生物群系接入地表或地下渔获选择。部分地形保留一般淡水、森林、丛林或针叶林鱼种，没有独有鱼种，有些则与邻近原版群系共用一类。Frostfire Caves 同时提供幽匿与滴水石渔获。稀疏竹子不算密集竹林，因此不解锁竹林条目。

群系符合条件时，你站立的具体位置也可能没有水。栖息地整合只改变哪些鱼竿渔获合法，不增加生物生成，不提高野生生物密度，也不改变渔获稀有度。

***

- [钓鱼装备](food.fishing.md)
- [水生生物与自然栖息地](adventure.aquatic.md)
- [维度](world.dimensions.md)
- [位置查找](maps.find.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Hybrid Aquatic + Starcatcher Compatibility](images/catalog-onrvj8th.png) [Hybrid Aquatic + Starcatcher Compatibility](food.fishing.md) | 把 Hybrid Aquatic 渔获加入 Starcatcher 钓鱼系统。 | <EmiSearch query="@hybrid_aquatic" /> |
| ![Starcatcher](images/catalog-h2jxvxnr.png) [Starcatcher](food.fishing.md) | 加入依栖息地变化的渔获、钓具与钓鱼图鉴。 | <EmiSearch query="@starcatcher" /> |
| ![Terralith](images/terralith-icon.png) [Terralith](world.dimensions.md) | 使用原版方块增加地表与洞穴生物群系。 | 无独立物品查询 |
