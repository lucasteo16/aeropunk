---
navigation:
  title: "种植与收获食材"
  position: 2
  parent: reference.food.md
  icon: minecraft:wheat
---

# 种植与收获食材

## 野生作物与种子

<EmiSearch query="@farmersdelight" />

![厨房食材菜园](images/visual-garden-crops.png)

厨房食材菜园

<ItemGrid><ItemIcon id="farmersdelight:wild_cabbages" /><ItemIcon id="farmersdelight:wild_tomatoes" /><ItemIcon id="farmersdelight:wild_onions" /><ItemIcon id="farmersdelight:wild_rice" /></ItemGrid>

农夫乐事的作物会生长在气候相符的野外。徒手破坏野生植株会得到种子或可种植的物品，偶尔还会得到作物本身。用剪刀采集则可整株取回，重新种下作为装饰或种子来源。对野生植株使用骨粉会让它在原地增殖，一次发现就能变成一整排。

| 野生植株 | 生长地点 | 获得物 |
| --- | --- | --- |
| <ItemGrid><ItemIcon id="farmersdelight:wild_cabbages" /></ItemGrid> | 海滩与海岸 | 卷心菜种子 |
| <ItemGrid><ItemIcon id="farmersdelight:wild_tomatoes" /></ItemGrid> | 干旱气候 | 番茄种子 |
| <ItemGrid><ItemIcon id="farmersdelight:wild_onions" /></ItemGrid> | 温带气候 | 洋葱 |
| <ItemGrid><ItemIcon id="farmersdelight:wild_rice" /></ItemGrid> | 沼泽与丛林 | 稻米 |

村庄农田和箱子中也会出现这些作物的样本，跑一趟村庄就能凑齐菜园，不必长途寻找。

***

## 种植与收获

<ItemGrid><ItemIcon id="farmersdelight:cabbage_seeds" /><ItemIcon id="farmersdelight:cabbage" /><ItemIcon id="farmersdelight:tomato_seeds" /><ItemIcon id="farmersdelight:tomato" /><ItemIcon id="farmersdelight:onion" /><ItemIcon id="farmersdelight:rice_panicle" /><ItemIcon id="farmersdelight:rice" /><ItemIcon id="farmersdelight:straw" /></ItemGrid>

把 <ItemLink id="farmersdelight:cabbage_seeds" /> 与 <ItemLink id="farmersdelight:tomato_seeds" /> 像普通作物一样种在耕地上。<ItemLink id="farmersdelight:onion" /> 直接用鳞茎种植。

番茄会攀爬。在种下的番茄上方放一根 <ItemLink id="farmersdelight:rope" />，藤蔓会顺着绳子生长。本包中破坏成熟的藤蔓会留下绳子，下一次种植仍可使用同一支撑。

稻米种在浅水中。收获成熟的 <ItemLink id="farmersdelight:rice_panicle" /> 后选择加工方式。直接合成得到一份 <ItemLink id="farmersdelight:rice" />。用刀在 <ItemLink id="farmersdelight:cutting_board" /> 上切割，则得到一份稻米和一份 <ItemLink id="farmersdelight:straw" />。砧板路线稻米数量相同，还多出可用于绳子、帆布和合成的稻草。

***

## 肥沃土壤

<ItemGrid><ItemIcon id="farmersdelight:organic_compost" /><ItemIcon id="farmersdelight:rich_soil" /><ItemIcon id="minecraft:brown_mushroom" /><ItemIcon id="minecraft:podzol" /></ItemGrid>

合成 <ItemLink id="farmersdelight:organic_compost" />，放置后等待。阳光和附近的水会加快分解。相邻的堆肥、肥沃土壤、菌丝、灰化土和蘑菇都是促进方块，能让它更快转化。堆肥最终变成 <ItemLink id="farmersdelight:rich_soil" />。

肥沃土壤会像免费的骨粉一样促进作物生长，本包中每次生长判定有百分之二十的概率触发。用锄头把它变成 肥沃耕地，耕地也能保留这份加成。肥沃耕地还能抵抗踩踏，南瓜或西瓜长在上面也不会变回泥土。

在黑暗处种在肥沃土壤上的蘑菇会长成两到五个菌盖的菌落。徒手破坏可收走全部菌盖，用剪刀则能整株取回。

***

## 收获辅助

<EmiSearch query="@create_integrated_farming" /> <EmiSearch query="@create" />

<ItemGrid><ItemIcon id="minecraft:bone_meal" /><ItemIcon id="farmersdelight:rich_soil" /></ItemGrid>

RightClickHarvest 让你右键一次就完成收获与补种。本包配置为无需锄头，空手即可操作。Smarter Farmers 让村民补种与作物匹配的种子，模组作物也包含在内。Universal Bone Meal 让骨粉能催熟原版拒绝的植物，例如甘蔗和仙人掌。

这些辅助改变的是田间操作方式，不改变作物产量。围绕某种作物搭建自动农场前先确认它的收获方式，模组植物可能需要额外支持。

| 辅助模组 | 改变的内容 | 不变的内容 |
| --- | --- | --- |
| RightClickHarvest | 一次点击完成收获与补种 | 作物掉落 |
| Smarter Farmers | 村民为模组作物补种 | 村民交易 |
| Universal Bone Meal | 骨粉可用于更多植物 | 受支持作物的生长速度 |
| Create: Integrated Farming | 真空收割机在区域内收获并补种 | 作物掉落 |

***

## 料理与材料

<EmiSearch query="@minersdelight" /> <EmiSearch query="@mynethersdelight" />

下表按制作工作站分组，列出本章其余物品。将光标移到图标上查看食物数值，在配方浏览器中查看具体料理。

| 分类 | 物品 |
| --- | --- |
| 作物食材 | <ItemGrid><ItemIcon id="minecraft:wheat" /><ItemIcon id="minecraft:carrot" /><ItemIcon id="minecraft:potato" /><ItemIcon id="minecraft:beetroot" /><ItemIcon id="minecraft:pumpkin" /><ItemIcon id="minecraft:melon_slice" /></ItemGrid> |
| 土壤与地区作物 | <ItemGrid><ItemIcon id="minersdelight:cave_carrot" /><ItemIcon id="mynethersdelight:bullet_pepper" /></ItemGrid> |

- [地下作物](food.underground.md)
- [下界食材](food.nether.md)
- [机器厨房](food.machine-cooking.md)

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Integrated Farming](images/catalog-9k1pasfr.png) [Create: Integrated Farming](food.growing.md) | 为机械动力增加自动收割、渔网与家禽产物自动收集。 | <EmiSearch query="@create_integrated_farming" /> |
| ![Leaves Be Gone](images/catalog-avq17pqv.png) [Leaves Be Gone](food.growing.md) | 让树木被砍后失去支撑的树叶快速凋落。 | 无独立物品查询 |
| ![RightClickHarvest](images/catalog-cnejf5xm.png) [RightClickHarvest](food.growing.md) | 右键即可收获成熟作物，无需手动破坏再补种。 | 无独立物品查询 |
| ![Smarter Farmers (farmers replant)](images/catalog-bh6zomvp.png) [Smarter Farmers (farmers replant)](food.growing.md) | 让农民村民正确补种作物，也支持部分模组种子。 | 无独立物品查询 |
| ![Universal Bone Meal](images/catalog-66viit1y.png) [Universal Bone Meal](food.growing.md) | 让骨粉可用于原本不接受骨粉的植物。 | 无独立物品查询 |
