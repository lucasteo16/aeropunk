---
navigation:
  title: "用烹饪工具准备食物"
  position: 0
  parent: reference.food.md
  icon: farmersdelight:cooking_pot
item_ids:
  - farmersdelight:cooking_pot
  - farmersdelight:cutting_board
  - farmersdelight:skillet
  - farmersdelight:stove
---

# 用烹饪工具准备食物

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Farmer%27s%20Delight%20cooking%20pot%20stove%20cutting%20board%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20%E5%86%9C%E5%A4%AB%E4%B9%90%E4%BA%8B%20%E7%83%B9%E9%A5%AA%E9%94%85%20%E7%81%B6%E5%8F%B0%20%E5%88%87%E8%8F%9C%E6%9D%BF%20%E6%95%99%E7%A8%8B)

## 从一把刀和一块板开始

<EmiSearch query="@farmersdelight" />

<ItemGrid><ItemIcon id="farmersdelight:flint_knife" /><ItemIcon id="farmersdelight:cutting_board" /></ItemGrid>

燧石刀和切菜板是进入这个厨房最便宜的路径。刀还能从草类植物收稻草，并从动物身上拿到额外掉落，所以在做出任何设备之前就已经回本。

<Recipe id="farmersdelight:cutting_board" />

放下切菜板，手持 <ItemLink id="farmersdelight:cabbage" /> 对板使用，再手持刀对板使用。卷心菜变成两张 <ItemLink id="farmersdelight:cabbage_leaf" />，这是第一份有用的食材半成品，也是几种汤里的绿叶材料。

***

## 营地一餐

<ItemGrid><ItemIcon id="farmersdelight:cooking_pot" /><ItemIcon id="minecraft:campfire" /></ItemGrid>

锅需要正下方有热源，营火就够。灶台是不用燃料的便利设备，不是第一餐的前提。

1. 放下点燃的营火，把锅直接叠在营火上方一格，中间不放别的方块。
2. 使用锅，把棕色蘑菇和红色蘑菇放进两个食材格。
3. 把一个碗放进容器格。
4. 等大约十秒。冒泡并显示营火图标说明已受热，蘑菇煲会带着你放的碗出锅。

<Recipe id="farmersdelight:cooking_pot" />

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Block x="0" y="0" z="0" id="farmersdelight:stove" p:lit="true" p:facing="north" />
  <Block x="0" y="1" z="0" id="farmersdelight:cooking_pot" p:facing="north" p:support="none" />
  <BlockAnnotation x="0" y="1" z="0" color="#F28CBD">
    烹饪锅，位于热源上方一格
  </BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="0" color="#F28CBD">
    点燃的灶台，锅接受的热源之一
  </BlockAnnotation>
</GameScene>

图里用点燃的灶台，因为那是整洁的长期方案。同样的摆放放在营火上也能用。

手持料理完全不需要锅。<ItemLink id="farmersdelight:mutton_wrap" /> 是无序配方，用面包、熟羊肉、一种绿叶蔬菜和洋葱做成，不需要任何厨房设备。

***

## 板上的工具

| 工具 | 辨认 | 板上的作用 |
| --- | --- | --- |
| <ItemLink id="farmersdelight:flint_knife" /> | <ItemGrid><ItemIcon id="farmersdelight:flint_knife" /></ItemGrid> | 切食材、处理谷物，例如一颗卷心菜出两张叶片 |
| <ItemLink id="minecraft:iron_axe" /> | <ItemGrid><ItemIcon id="minecraft:iron_axe" /></ItemGrid> | 剥原木，拆开篮子得到帆布 |
| <ItemLink id="minecraft:iron_shovel" /> | <ItemGrid><ItemIcon id="minecraft:iron_shovel" /></ItemGrid> | 打散黏土与沙砾，例如黏土块出黏土球 |
| <ItemLink id="minecraft:iron_pickaxe" /> | <ItemGrid><ItemIcon id="minecraft:iron_pickaxe" /></ItemGrid> | 把砖块拆回四个红砖，把下界砖块拆回四个下界砖 |
| <ItemLink id="minecraft:shears" /> | <ItemGrid><ItemIcon id="minecraft:shears" /></ItemGrid> | 从皮革护甲取回一个皮革，从皮革马铠取回两个皮革 |

每加工一件，刀消耗一点耐久。板会先读副手，所以食材放副手、工具拿主手可以连续切同一种材料。

***

## 锅、煎锅与灶台

锅有六个食材格和一个容器格。营火、灵魂营火、火、灵魂火、岩浆、岩浆块和点燃的灶台都能加热，锅本身不烧燃料。装满料理的锅可以带着成品搬动，但食材格会掉落。

<ItemGrid><ItemIcon id="farmersdelight:skillet" /><ItemIcon id="farmersdelight:stove" /></ItemGrid>

手持煎锅靠近热源一次煎一件，放下的煎锅一次处理一整堆。点燃的灶台能放六件物品，不用燃料做营火配方，顶面不能压方块。

| 设备 | 热源 | 容量 | 适合做什么 |
| --- | --- | --- | --- |
| 手持煎锅 | 附近任意热源 | 一次一件 | 赶路时煎几块 |
| 放下的煎锅 | 下方热源方块 | 一整堆 | 在基地批量处理 |
| 灶台 | 点燃后不需要 | 六件 | 基地里的免燃料烹饪 |
| 烹饪锅 | 下方热源方块 | 六格食材加一个容器 | 混合料理 |

***

## 分盛宴

| 盛宴 | 辨认 | 取到的分餐 | 用什么取 |
| --- | --- | --- | --- |
| <ItemLink id="farmersdelight:roast_chicken_block" /> | <ItemGrid><ItemIcon id="farmersdelight:roast_chicken_block" /></ItemGrid> | <ItemLink id="farmersdelight:roast_chicken" /> | 碗 |
| <ItemLink id="farmersdelight:honey_glazed_ham_block" /> | <ItemGrid><ItemIcon id="farmersdelight:honey_glazed_ham_block" /></ItemGrid> | <ItemLink id="farmersdelight:honey_glazed_ham" /> | 碗 |
| <ItemLink id="farmersdelight:shepherds_pie_block" /> | <ItemGrid><ItemIcon id="farmersdelight:shepherds_pie_block" /></ItemGrid> | <ItemLink id="farmersdelight:shepherds_pie" /> | 碗 |
| <ItemLink id="farmersdelight:stuffed_pumpkin_block" /> | <ItemGrid><ItemIcon id="farmersdelight:stuffed_pumpkin_block" /></ItemGrid> | <ItemLink id="farmersdelight:stuffed_pumpkin" /> | 碗 |

放下盛宴，手持碗对它使用即可取走一份。放下的盛宴共四份。真正吃的是取到的分餐，而显示名称不代表它需要的容器。

放下的整张派共四片。手持刀对它使用可以取下一片随身带走，饿的时候空手对它使用则当场吃掉一片。

***

## 料理分组

| 分组 | 物品 | 说明 |
| --- | --- | --- |
| 生食材 | <ItemGrid><ItemIcon id="farmersdelight:cabbage" /><ItemIcon id="farmersdelight:tomato" /><ItemIcon id="farmersdelight:onion" /><ItemIcon id="farmersdelight:rice" /><ItemIcon id="minecraft:carrot" /><ItemIcon id="minecraft:potato" /></ItemGrid> | 采集来的作物，未经设备处理。来源见[作物食材](food.growing.md)。 |
| 生肉与鱼 | <ItemGrid><ItemIcon id="minecraft:beef" /><ItemIcon id="minecraft:porkchop" /><ItemIcon id="minecraft:chicken" /><ItemIcon id="minecraft:mutton" /><ItemIcon id="minecraft:cod" /><ItemIcon id="minecraft:salmon" /></ItemGrid> | 农田与水域的生肉。鱼类来源见[钓鱼](food.fishing.md)。 |
| 切板半成品 | <ItemGrid><ItemIcon id="farmersdelight:cabbage_leaf" /><ItemIcon id="farmersdelight:minced_beef" /><ItemIcon id="farmersdelight:salmon_slice" /><ItemIcon id="farmersdelight:cod_slice" /><ItemIcon id="farmersdelight:pumpkin_slice" /><ItemIcon id="farmersdelight:bacon" /></ItemGrid> | 切出的分份食材，可用于其他料理。 |
| 厨房半成品 | <ItemGrid><ItemIcon id="farmersdelight:wheat_dough" /><ItemIcon id="farmersdelight:raw_pasta" /><ItemIcon id="farmersdelight:tomato_sauce" /><ItemIcon id="farmersdelight:cooked_rice" /><ItemIcon id="farmersdelight:cooked_bacon" /><ItemIcon id="farmersdelight:beef_patty" /></ItemGrid> | 供其他料理使用的半成品，包括面团、生意面、酱汁、米饭和熟肉。 |
| 三明治 | <ItemGrid><ItemIcon id="farmersdelight:egg_sandwich" /><ItemIcon id="farmersdelight:chicken_sandwich" /><ItemIcon id="farmersdelight:bacon_sandwich" /><ItemIcon id="farmersdelight:hamburger" /><ItemIcon id="farmersdelight:mutton_wrap" /></ItemGrid> | 面包类手持食物，吃完不留碗。 |
| 卷与饺子 | <ItemGrid><ItemIcon id="farmersdelight:dumplings" /><ItemIcon id="farmersdelight:cabbage_rolls" /><ItemIcon id="farmersdelight:salmon_roll" /><ItemIcon id="farmersdelight:cod_roll" /><ItemIcon id="farmersdelight:kelp_roll" /></ItemGrid> | 包起来的分份料理，面包不够时很实用。 |
| 锅装碗料理 | <ItemGrid><ItemIcon id="farmersdelight:vegetable_soup" /><ItemIcon id="farmersdelight:beef_stew" /><ItemIcon id="farmersdelight:fish_stew" /><ItemIcon id="farmersdelight:fried_rice" /><ItemIcon id="farmersdelight:mushroom_rice" /><ItemIcon id="farmersdelight:noodle_soup" /></ItemGrid> | 在锅里煮好并盛进碗的料理。 |
| 更多锅装碗料理 | <ItemGrid><ItemIcon id="farmersdelight:pumpkin_soup" /><ItemIcon id="farmersdelight:onion_soup" /><ItemIcon id="farmersdelight:bone_broth" /><ItemIcon id="farmersdelight:ratatouille" /><ItemIcon id="farmersdelight:baked_cod_stew" /><ItemIcon id="farmersdelight:chicken_soup" /></ItemGrid> | 其余锅料理，其中几种只用作物或骨头。 |
| 意面料理 | <ItemGrid><ItemIcon id="farmersdelight:pasta_with_meatballs" /><ItemIcon id="farmersdelight:pasta_with_mutton_chop" /><ItemIcon id="farmersdelight:vegetable_noodles" /><ItemIcon id="farmersdelight:squid_ink_pasta" /></ItemGrid> | 用意面与酱汁做成的料理，用到上面的半成品。 |
| 肉类与蛋料理 | <ItemGrid><ItemIcon id="farmersdelight:steak_and_potatoes" /><ItemIcon id="farmersdelight:bacon_and_eggs" /><ItemIcon id="farmersdelight:roasted_mutton_chops" /><ItemIcon id="farmersdelight:grilled_salmon" /><ItemIcon id="farmersdelight:fried_egg" /></ItemGrid> | 培根煎蛋、烤鲑鱼、烤羊排和土豆牛排都用备好的食材无序合成。煎蛋可通过加热制作。 |
| 沙拉 | <ItemGrid><ItemIcon id="farmersdelight:gleaming_salad" /><ItemIcon id="farmersdelight:fruit_salad" /></ItemGrid> | 用作物与水果拼成的冷盘，不用加热。 |
| 烘焙甜点 | <ItemGrid><ItemIcon id="farmersdelight:apple_pie" /><ItemIcon id="farmersdelight:sweet_berry_cheesecake" /><ItemIcon id="farmersdelight:chocolate_pie" /><ItemIcon id="minecraft:pumpkin_pie" /><ItemIcon id="farmersdelight:sweet_berry_cookie" /><ItemIcon id="farmersdelight:honey_cookie" /></ItemGrid> | 通过合成制作的派与饼干。放下的派可以分次食用，也可以切片。 |
| 派片 | <ItemGrid><ItemIcon id="farmersdelight:apple_pie_slice" /><ItemIcon id="farmersdelight:sweet_berry_cheesecake_slice" /><ItemIcon id="farmersdelight:chocolate_pie_slice" /><ItemIcon id="farmersdelight:pumpkin_pie_slice" /></ItemGrid> | 烘焙派的携带形态，四片可以合成回整张派。 |
| 冷冻甜点 | <ItemGrid><ItemIcon id="farmersdelight:melon_popsicle" /></ItemGrid> | 这里唯一的冷冻甜点，拿在手上吃。 |
| 饮品与蛋奶冻 | <ItemGrid><ItemIcon id="farmersdelight:hot_cocoa" /><ItemIcon id="farmersdelight:apple_cider" /><ItemIcon id="farmersdelight:melon_juice" /><ItemIcon id="farmersdelight:glow_berry_custard" /></ItemGrid> | 热可可、苹果酒和荧光浆果蛋奶冻在锅中制作，无需另放容器。西瓜汁用无序合成制作。 |

- [饥饿与多样性](food.hunger.md) 效果、食物书与午餐容器。
- [作物食材](food.growing.md) 种出上面的蔬菜。
- [机器厨房](food.machine-cooking.md) 自动切片与生产饮品。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Farmer's Delight](images/catalog-r2oftaxm.png) [Farmer's Delight](food.utensils.md) | 增加作物与厨具，可用砧板和烹饪锅处理食材及制作菜肴。 | <EmiSearch query="@farmersdelight" /> |
