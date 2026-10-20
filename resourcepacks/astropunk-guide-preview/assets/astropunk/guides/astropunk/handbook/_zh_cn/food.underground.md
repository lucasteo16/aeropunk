---
navigation:
  title: "用地下食材烹饪"
  position: 5
  parent: reference.food.md
  icon: minecraft:brown_mushroom
---

# 用地下食材烹饪

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Miner%27s%20Delight%20cave%20carrot%20copper%20pot%20gossypium%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Miner%27s%20Delight%20%E6%B4%9E%E7%A9%B4%E8%83%A1%E8%90%9D%E5%8D%9C%20%E9%93%9C%E9%94%85%20%E6%A3%89%E8%8A%B1%20%E6%95%99%E7%A8%8B)

## 洞穴胡萝卜

<EmiSearch query="@farmersdelight" /> <EmiSearch query="@minersdelight" />

![洞穴里的厨房](images/visual-cavern-kitchen.png)

| 阶段 | 外观 | 怎么得到 |
| --- | --- | --- |
| <ItemLink id="minersdelight:wild_cave_carrots" /> | <ItemGrid><ItemIcon id="minersdelight:wild_cave_carrots" /></ItemGrid> | 在洞穴打掉野生丛，或用剪刀整丛搬走 |
| <ItemLink id="minersdelight:cave_carrot" /> | <ItemGrid><ItemIcon id="minersdelight:cave_carrot" /></ItemGrid> | 收割野生丛，之后用胡萝卜本身补种 |
| <ItemLink id="minersdelight:gossypium" /> | <ItemGrid><ItemIcon id="minersdelight:gossypium" /></ItemGrid> | 从肥沃土壤上的野生胡萝卜旁长出，不是靠种子播种 |

把 <ItemLink id="minersdelight:cave_carrot" /> 种在耕地上就能开一垄，成熟后收割。放在 <ItemLink id="farmersdelight:rich_soil" /> 上的野生丛会扩散：它的随机生长会复制自身，或者在附近的空位放下 <ItemLink id="minersdelight:gossypium" />。因此肥沃土壤上的野生丛才是稳定拿到棉花的办法，一个棉花可以合成两根线。

第一份熟食很简单。把 <ItemLink id="minersdelight:cave_carrot" /> 放进熔炉烘烤，或者用营火与烟熏炉的对应配方，烤好就能直接吃，产物是 <ItemLink id="minersdelight:baked_cave_carrot" />。

<Recipe id="minersdelight:baked_cave_carrot" />

洞穴胡萝卜是锅类配方的材料，可以做 <ItemLink id="minersdelight:cave_soup" />。<ItemLink id="minersdelight:copper_carrot" /> 是另一种加工品，不是烤胡萝卜。

***

## 铜锅

<Recipe id="minersdelight:copper_pot" />

<Recipe id="minersdelight:copper_cup" />

<ItemLink id="minersdelight:copper_pot" /> 是独立设备。它有四个食材格和一个容器格，做的是 Farmer's Delight 的锅类配方，而且只有下方方块是热源时才会工作，这条热量规则和铁锅一致。

1. 在锅下方放热源，把锅放在上面。
2. 把最多四样食材放进食材格。
3. 把 <ItemLink id="minersdelight:copper_cup" /> 放进指定的容器格。锅会用一个格子显示成品、另一个格子放可取出的结果，取的时候取输出格而不是展示格。
4. 等烹饪结束，从输出格取出成品。

四个食材格意味着需要六样材料的铁锅配方在这里放不下。放得下又有杯装形态的例子是 <ItemLink id="minersdelight:vegetable_soup_cup" />：四个食材格放胡萝卜、土豆、甜菜根和一种绿叶蔬菜，容器格放铜杯，锅就把这锅汤盛成一杯。

杯装取决于料理本身。容器决定锅盛进什么，料理决定有没有杯装形态。没有杯装形态的料理，放杯子也不会变成杯装。

用铜杯盛装这些杯装料理。<ItemLink id="minersdelight:water_cup" /> 与 <ItemLink id="minersdelight:milk_cup" /> 是装好的容器内容，不是煮出来的料理，<ItemLink id="minersdelight:powder_snow_cup" /> 是冷饮。

***

## 地下蛋白

蜘蛛、洞穴节肢动物、蝙蝠与蠹虫提供这一页的肉类来源。这些是战利品与刀类掉落，不是农田作物。

| 原料 | 外观 | 来源 |
| --- | --- | --- |
| <ItemLink id="minersdelight:arthropod" /> | <ItemGrid><ItemIcon id="minersdelight:arthropod" /></ItemGrid> | 主手持刀击杀蜜蜂、蠹虫与末影螨，且目标没有着火时 |
| <ItemLink id="minersdelight:spider_leg" /> | <ItemGrid><ItemIcon id="minersdelight:spider_leg" /></ItemGrid> | 主手持刀击杀蜘蛛，且目标没有着火时，而且只是概率掉落 |
| <ItemLink id="minersdelight:bat_wing" /> | <ItemGrid><ItemIcon id="minersdelight:bat_wing" /></ItemGrid> | 用刀击杀未着火的蝙蝠得两个，不用刀击杀有概率得一个 |
| <ItemLink id="minersdelight:silverfish_eggs" /> | <ItemGrid><ItemIcon id="minersdelight:silverfish_eggs" /></ItemGrid> | 用镐破坏被虫蚀的方块有概率得到，或用刀击杀未着火的蠹虫也有概率得到 |

| 熟制分份 | 外观 | 怎么做 |
| --- | --- | --- |
| <ItemLink id="minersdelight:cooked_arthropod" /> | <ItemGrid><ItemIcon id="minersdelight:cooked_arthropod" /></ItemGrid> | 熔炉或营火 |
| <ItemLink id="minersdelight:baked_spider_leg" /> | <ItemGrid><ItemIcon id="minersdelight:baked_spider_leg" /></ItemGrid> | 熔炉、营火或烟熏炉 |
| <ItemLink id="minersdelight:smoked_bat_wing" /> | <ItemGrid><ItemIcon id="minersdelight:smoked_bat_wing" /></ItemGrid> | 熔炉、营火或烟熏炉 |
| <ItemLink id="minersdelight:baked_squid" /> | <ItemGrid><ItemIcon id="minersdelight:baked_squid" /></ItemGrid> | 熔炉、营火或烟熏炉 |
| <ItemLink id="minersdelight:baked_tentacles" /> | <ItemGrid><ItemIcon id="minersdelight:baked_tentacles" /></ItemGrid> | 熔炉、营火或烟熏炉 |

***

## 蛋白料理

| 分组 | 外观 | 用途 |
| --- | --- | --- |
| 锅类料理 | <ItemGrid><ItemIcon id="minersdelight:insect_stew" /><ItemIcon id="minersdelight:bat_soup" /><ItemIcon id="minersdelight:bat_rolls" /></ItemGrid> | 在受热烹饪锅中制作的炖菜与卷。 |
| 三明治与卷 | <ItemGrid><ItemIcon id="minersdelight:insect_sandwich" /><ItemIcon id="minersdelight:insect_wrap" /></ItemGrid> | 可手持食用的昆虫料理。 |
| 洞穴汉堡 | <ItemGrid><ItemIcon id="minersdelight:cave_hamburger" /></ItemGrid> | 用面包、脆能量棒或素饼、熏蝙蝠翼，以及两份烤触手或棕色蘑菇合成。 |
| 洞穴烤串 | <ItemGrid><ItemIcon id="minersdelight:improvised_barbecue_stick" /></ItemGrid> | 用烤洞穴胡萝卜、棕色蘑菇、熏蝙蝠翼与木杆合成。 |
| 调味节肢动物 | <ItemGrid><ItemIcon id="minersdelight:seasoned_arthropods" /></ItemGrid> | 加工后的节肢动物料理。 |
| 鱼子酱 | <ItemGrid><ItemIcon id="minersdelight:weird_caviar" /></ItemGrid> | 用蠹虫卵制作的蛋类料理。 |
| 蜜汁蛛肢盘 | <ItemGrid><ItemIcon id="minersdelight:plate_of_glazed_arachnid_limbs" /></ItemGrid> | 盘装的蛛肢分份。 |
| 蝙蝠曲奇 | <ItemGrid><ItemIcon id="minersdelight:bat_cookie" /></ItemGrid> | 用蝙蝠翼制作的甜点。 |

***

## 鱿鱼与植物料理

| 分组 | 外观 | 用途 |
| --- | --- | --- |
| 整只鱿鱼 | <ItemGrid><ItemIcon id="minersdelight:squid" /><ItemIcon id="minersdelight:glow_squid" /></ItemGrid> | 两种不同的生鱿鱼食材。 |
| 触手 | <ItemGrid><ItemIcon id="minersdelight:tentacles" /></ItemGrid> | 供烹饪使用的生分份。 |
| 鱿鱼料理 | <ItemGrid><ItemIcon id="minersdelight:bowl_of_stuffed_squid" /><ItemIcon id="minersdelight:takoyaki" /><ItemIcon id="minersdelight:squid_sandwich" /><ItemIcon id="minersdelight:tentacles_on_a_stick" /></ItemGrid> | 酿鱿鱼碗、章鱼烧、三明治与烤串。 |

<ItemLink id="minersdelight:vegan_patty" /> 是生料中间物。三种成品以它为基础。素丸意面也可以使用烤洞穴胡萝卜或素饼，发光墨汁意面则使用鱼、意面、发光浆果与发光墨囊。

| 厨房分组 | 外观 | 作用 |
| --- | --- | --- |
| 生素饼 | <ItemGrid><ItemIcon id="minersdelight:vegan_patty" /></ItemGrid> | 用于下列成品料理的加工素饼 |
| 素饼料理 | <ItemGrid><ItemIcon id="minersdelight:vegan_hamburger" /><ItemIcon id="minersdelight:vegan_wrap" /><ItemIcon id="minersdelight:vegan_steak_and_potatoes" /></ItemGrid> | 以素饼为基础的成品 |
| 洞穴意面 | <ItemGrid><ItemIcon id="minersdelight:pasta_with_veggieballs" /><ItemIcon id="minersdelight:glow_ink_pasta" /></ItemGrid> | 锅类意面，一道用烤洞穴胡萝卜或素饼、意面与番茄酱，一道用鱼、意面、发光浆果与发光墨囊 |
| 植物盘装 | <ItemGrid><ItemIcon id="minersdelight:fake_meatloaf" /><ItemIcon id="minersdelight:plate_of_fake_meatloaf" /></ItemGrid> | 锅做的素肉糕与它的盘装分份 |

***

## 杯装与能量棒

| 杯装 | 外观 | 里面是什么 |
| --- | --- | --- |
| <ItemLink id="minersdelight:water_cup" /> | <ItemGrid><ItemIcon id="minersdelight:water_cup" /></ItemGrid> | 水 |
| <ItemLink id="minersdelight:milk_cup" /> | <ItemGrid><ItemIcon id="minersdelight:milk_cup" /></ItemGrid> | 奶 |
| <ItemLink id="minersdelight:powder_snow_cup" /> | <ItemGrid><ItemIcon id="minersdelight:powder_snow_cup" /></ItemGrid> | 细雪 |
| <ItemLink id="minersdelight:cave_soup_cup" /> | <ItemGrid><ItemIcon id="minersdelight:cave_soup_cup" /></ItemGrid> | 洞穴浓汤 |
| <ItemLink id="minersdelight:bat_soup_cup" /> | <ItemGrid><ItemIcon id="minersdelight:bat_soup_cup" /></ItemGrid> | 蝙蝠汤 |
| <ItemLink id="minersdelight:insect_stew_cup" /> | <ItemGrid><ItemIcon id="minersdelight:insect_stew_cup" /></ItemGrid> | 昆虫炖菜 |

Farmer's Delight 的汤与炖菜也有杯装形态，所以铜锅可以把这些料理盛成一杯。

| 杯装分组 | 外观 | 里面是什么 |
| --- | --- | --- |
| 蔬菜与蘑菇汤 | <ItemGrid><ItemIcon id="minersdelight:beetroot_soup_cup" /><ItemIcon id="minersdelight:mushroom_stew_cup" /><ItemIcon id="minersdelight:onion_soup_cup" /><ItemIcon id="minersdelight:pumpkin_soup_cup" /><ItemIcon id="minersdelight:vegetable_soup_cup" /></ItemGrid> | 以蔬菜为主的汤与炖菜杯装 |
| 鱼与禽汤 | <ItemGrid><ItemIcon id="minersdelight:baked_cod_stew_cup" /><ItemIcon id="minersdelight:chicken_soup_cup" /><ItemIcon id="minersdelight:fish_stew_cup" /><ItemIcon id="minersdelight:noodle_soup_cup" /></ItemGrid> | 鱼、鸡肉与面汤的杯装 |
| 肉炖菜 | <ItemGrid><ItemIcon id="minersdelight:beef_stew_cup" /><ItemIcon id="minersdelight:rabbit_stew_cup" /><ItemIcon id="minersdelight:bone_broth_cup" /></ItemGrid> | 牛肉、兔肉与骨头炖菜的杯装 |

| 能量棒 | 外观 | 作用 |
| --- | --- | --- |
| <ItemLink id="minersdelight:crunchy_bar" /> | <ItemGrid><ItemIcon id="minersdelight:crunchy_bar" /></ItemGrid> | 用熟节肢动物与蠹虫卵合成，一次四个 |
| <ItemLink id="minersdelight:nutritional_bar" /> | <ItemGrid><ItemIcon id="minersdelight:nutritional_bar" /></ItemGrid> | 用四个脆能量棒、小麦与蜂蜜合成 |
| <ItemLink id="minersdelight:golden_nutritional_bar" /> | <ItemGrid><ItemIcon id="minersdelight:golden_nutritional_bar" /></ItemGrid> | 营养能量棒四周放金粒 |

- [烹饪工具与料理](food.utensils.md) 铁锅、切菜板与煎锅。
- [作物食材](food.growing.md) 洞穴这一垄之外的地面作物。
- [饥饿与多样性](food.hunger.md) 食物数值与饮食记录。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Miner's Delight](images/catalog-qmxbm4bq.png) [Miner's Delight](food.underground.md) | 为 Farmer's Delight 增加采矿主题的食物与烹饪工具。 | <EmiSearch query="@minersdelight" /> |
