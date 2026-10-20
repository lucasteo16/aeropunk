---
navigation:
  title: "Cooking tools"
  position: 0
  parent: reference.food.md
  icon: farmersdelight:cooking_pot
item_ids:
  - farmersdelight:cooking_pot
  - farmersdelight:cutting_board
  - farmersdelight:skillet
  - farmersdelight:stove
---

# Cooking tools

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Farmer%27s%20Delight%20cooking%20pot%20stove%20cutting%20board%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20%E5%86%9C%E5%A4%AB%E4%B9%90%E4%BA%8B%20%E7%83%B9%E9%A5%AA%E9%94%85%20%E7%81%B6%E5%8F%B0%20%E5%88%87%E8%8F%9C%E6%9D%BF%20%E6%95%99%E7%A8%8B)

## Start with a knife and a board

<EmiSearch query="@farmersdelight" />

<ItemGrid><ItemIcon id="farmersdelight:flint_knife" /><ItemIcon id="farmersdelight:cutting_board" /></ItemGrid>

A flint knife and a cutting board are the cheapest way into this kitchen. A knife also gathers straw from grassy plants and gives extra drops from animals, so it pays for itself before any station exists.

<Recipe id="farmersdelight:cutting_board" />

Place the board, use a <ItemLink id="farmersdelight:cabbage" /> on it, then use the board while holding the knife. The cabbage becomes two <ItemLink id="farmersdelight:cabbage_leaf" />, which is your first useful food part and the green ingredient in several soups.

***

## A campsite meal

<ItemGrid><ItemIcon id="farmersdelight:cooking_pot" /><ItemIcon id="minecraft:campfire" /></ItemGrid>

A pot needs heat directly below it, and a campfire is enough. A stove is a convenience that never needs fuel, not a requirement for the first meal.

1. Place a lit campfire, then place the pot directly on top of it, one block above the flame with nothing in between.
2. Use the pot and put one brown mushroom and one red mushroom in two ingredient slots.
3. Put one bowl in the container slot.
4. Wait about ten seconds. Bubbles and a campfire icon mean the pot is heated, and the stew leaves the pot inside your bowl.

<Recipe id="farmersdelight:cooking_pot" />

<GameScene zoom="4" interactive={true}>
  <IsometricCamera yaw="135" pitch="15" />
  <Block x="0" y="0" z="0" id="farmersdelight:stove" p:lit="true" p:facing="north" />
  <Block x="0" y="1" z="0" id="farmersdelight:cooking_pot" p:facing="north" p:support="none" />
  <BlockAnnotation x="0" y="1" z="0" color="#F28CBD">
    Cooking pot, one block above the heat
  </BlockAnnotation>
  <BlockAnnotation x="0" y="0" z="0" color="#F28CBD">
    Lit stove, one of the heat sources a pot accepts
  </BlockAnnotation>
</GameScene>

The scene shows a lit stove because that is the tidy permanent setup. The same placement works on a campfire.

A handheld meal needs no pot at all. A <ItemLink id="farmersdelight:mutton_wrap" /> is bread, cooked mutton, a leafy green and an onion in a shapeless recipe, so it needs no kitchen station.

***

## Board tools

| Tool | Identify it | Board operation |
| --- | --- | --- |
| <ItemLink id="farmersdelight:flint_knife" /> | <ItemGrid><ItemIcon id="farmersdelight:flint_knife" /></ItemGrid> | Cuts food and opens grain, for example a cabbage into two leaves |
| <ItemLink id="minecraft:iron_axe" /> | <ItemGrid><ItemIcon id="minecraft:iron_axe" /></ItemGrid> | Strips logs and takes baskets apart into canvas |
| <ItemLink id="minecraft:iron_shovel" /> | <ItemGrid><ItemIcon id="minecraft:iron_shovel" /></ItemGrid> | Breaks clay and gravel down, for example clay into clay balls |
| <ItemLink id="minecraft:iron_pickaxe" /> | <ItemGrid><ItemIcon id="minecraft:iron_pickaxe" /></ItemGrid> | Breaks bricks back into four bricks, and nether bricks into four nether bricks |
| <ItemLink id="minecraft:shears" /> | <ItemGrid><ItemIcon id="minecraft:shears" /></ItemGrid> | Recovers one leather from leather armor and two leather from leather horse armor |

A knife loses one durability per item processed. The board reads your off hand first, so an ingredient in the off hand and a tool in the main hand repeats the same cut.

***

## Pot, skillet and stove

The pot has six ingredient slots and one container slot. Campfires, soul campfires, fire, soul fire, lava, magma blocks and a lit stove all heat it, and it never burns fuel. A loaded pot can be moved with its meals inside, but its ingredient slots drop.

<ItemGrid><ItemIcon id="farmersdelight:skillet" /><ItemIcon id="farmersdelight:stove" /></ItemGrid>

A held skillet cooks one item beside heat and a placed skillet cooks a whole stack. A lit stove holds six items and cooks campfire recipes without fuel, and its top face must stay clear of blocks.

| Station | Heat | Capacity | Use it for |
| --- | --- | --- | --- |
| Skillet in hand | Any nearby heat | One item | Cooking while travelling |
| Placed skillet | Heat block underneath | One stack | A batch beside a hopper |
| Stove | None after lighting | Six items | Fuel free cooking at a base |
| Cooking pot | Heat block underneath | Six ingredients and one container | Combined meals |

***

## Serving a feast

| Feast | Identify it | Portion you take | Take it with |
| --- | --- | --- | --- |
| <ItemLink id="farmersdelight:roast_chicken_block" /> | <ItemGrid><ItemIcon id="farmersdelight:roast_chicken_block" /></ItemGrid> | <ItemLink id="farmersdelight:roast_chicken" /> | A bowl |
| <ItemLink id="farmersdelight:honey_glazed_ham_block" /> | <ItemGrid><ItemIcon id="farmersdelight:honey_glazed_ham_block" /></ItemGrid> | <ItemLink id="farmersdelight:honey_glazed_ham" /> | A bowl |
| <ItemLink id="farmersdelight:shepherds_pie_block" /> | <ItemGrid><ItemIcon id="farmersdelight:shepherds_pie_block" /></ItemGrid> | <ItemLink id="farmersdelight:shepherds_pie" /> | A bowl |
| <ItemLink id="farmersdelight:stuffed_pumpkin_block" /> | <ItemGrid><ItemIcon id="farmersdelight:stuffed_pumpkin_block" /></ItemGrid> | <ItemLink id="farmersdelight:stuffed_pumpkin" /> | A bowl |

Place the feast and use a bowl on it to take one portion. A placed feast gives four portions. The portion item is what you eat, and the display name is not the container it needs.

A placed pie holds four slices. Use it with a knife to take a slice you can carry, or use it empty-handed while you are hungry to eat a slice in place.

***

## Food families

| Family | Items | What it is |
| --- | --- | --- |
| Raw ingredients | <ItemGrid><ItemIcon id="farmersdelight:cabbage" /><ItemIcon id="farmersdelight:tomato" /><ItemIcon id="farmersdelight:onion" /><ItemIcon id="farmersdelight:rice" /><ItemIcon id="minecraft:carrot" /><ItemIcon id="minecraft:potato" /></ItemGrid> | Gathered crops, before any station touches them. Sources are in [Crop ingredients](food.growing.md). |
| Meat and fish | <ItemGrid><ItemIcon id="minecraft:beef" /><ItemIcon id="minecraft:porkchop" /><ItemIcon id="minecraft:chicken" /><ItemIcon id="minecraft:mutton" /><ItemIcon id="minecraft:cod" /><ItemIcon id="minecraft:salmon" /></ItemGrid> | Raw cuts from farms and water. Fish sourcing is in [Fishing](food.fishing.md). |
| Board parts | <ItemGrid><ItemIcon id="farmersdelight:cabbage_leaf" /><ItemIcon id="farmersdelight:minced_beef" /><ItemIcon id="farmersdelight:salmon_slice" /><ItemIcon id="farmersdelight:cod_slice" /><ItemIcon id="farmersdelight:pumpkin_slice" /><ItemIcon id="farmersdelight:bacon" /></ItemGrid> | Cut portions used as ingredients in other dishes. |
| Kitchen parts | <ItemGrid><ItemIcon id="farmersdelight:wheat_dough" /><ItemIcon id="farmersdelight:raw_pasta" /><ItemIcon id="farmersdelight:tomato_sauce" /><ItemIcon id="farmersdelight:cooked_rice" /><ItemIcon id="farmersdelight:cooked_bacon" /><ItemIcon id="farmersdelight:beef_patty" /></ItemGrid> | Prepared ingredients for other dishes, including dough, pasta, sauce, rice and cooked meat. |
| Sandwiches | <ItemGrid><ItemIcon id="farmersdelight:egg_sandwich" /><ItemIcon id="farmersdelight:chicken_sandwich" /><ItemIcon id="farmersdelight:bacon_sandwich" /><ItemIcon id="farmersdelight:hamburger" /><ItemIcon id="farmersdelight:mutton_wrap" /></ItemGrid> | Bread based food eaten from the hand, with no bowl afterwards. |
| Rolls and dumplings | <ItemGrid><ItemIcon id="farmersdelight:dumplings" /><ItemIcon id="farmersdelight:cabbage_rolls" /><ItemIcon id="farmersdelight:salmon_roll" /><ItemIcon id="farmersdelight:cod_roll" /><ItemIcon id="farmersdelight:kelp_roll" /></ItemGrid> | Wrapped or rolled portions, useful when bread is short. |
| Pot bowls | <ItemGrid><ItemIcon id="farmersdelight:vegetable_soup" /><ItemIcon id="farmersdelight:beef_stew" /><ItemIcon id="farmersdelight:fish_stew" /><ItemIcon id="farmersdelight:fried_rice" /><ItemIcon id="farmersdelight:mushroom_rice" /><ItemIcon id="farmersdelight:noodle_soup" /></ItemGrid> | Meals cooked in the pot and served into a bowl. |
| More pot bowls | <ItemGrid><ItemIcon id="farmersdelight:pumpkin_soup" /><ItemIcon id="farmersdelight:onion_soup" /><ItemIcon id="farmersdelight:bone_broth" /><ItemIcon id="farmersdelight:ratatouille" /><ItemIcon id="farmersdelight:baked_cod_stew" /><ItemIcon id="farmersdelight:chicken_soup" /></ItemGrid> | Further pot meals, several of them cheap on crops or bones. |
| Pasta meals | <ItemGrid><ItemIcon id="farmersdelight:pasta_with_meatballs" /><ItemIcon id="farmersdelight:pasta_with_mutton_chop" /><ItemIcon id="farmersdelight:vegetable_noodles" /><ItemIcon id="farmersdelight:squid_ink_pasta" /></ItemGrid> | Pasta and sauce dishes that use the board and pot parts above. |
| Meat and egg meals | <ItemGrid><ItemIcon id="farmersdelight:steak_and_potatoes" /><ItemIcon id="farmersdelight:bacon_and_eggs" /><ItemIcon id="farmersdelight:roasted_mutton_chops" /><ItemIcon id="farmersdelight:grilled_salmon" /><ItemIcon id="farmersdelight:fried_egg" /></ItemGrid> | Bacon and eggs, grilled salmon, roasted mutton chops and steak and potatoes are shapeless crafts using prepared ingredients. Fried eggs can be cooked over heat. |
| Salads | <ItemGrid><ItemIcon id="farmersdelight:gleaming_salad" /><ItemIcon id="farmersdelight:fruit_salad" /></ItemGrid> | Cold plates assembled from crops and fruit, with no heat. |
| Baked sweets | <ItemGrid><ItemIcon id="farmersdelight:apple_pie" /><ItemIcon id="farmersdelight:sweet_berry_cheesecake" /><ItemIcon id="farmersdelight:chocolate_pie" /><ItemIcon id="minecraft:pumpkin_pie" /><ItemIcon id="farmersdelight:sweet_berry_cookie" /><ItemIcon id="farmersdelight:honey_cookie" /></ItemGrid> | Pies and cookies made by crafting. Placed pies can be eaten in portions or cut into slices. |
| Pie slices | <ItemGrid><ItemIcon id="farmersdelight:apple_pie_slice" /><ItemIcon id="farmersdelight:sweet_berry_cheesecake_slice" /><ItemIcon id="farmersdelight:chocolate_pie_slice" /><ItemIcon id="farmersdelight:pumpkin_pie_slice" /></ItemGrid> | The carried form of a baked pie. Four slices make a whole pie again. |
| Frozen treats | <ItemGrid><ItemIcon id="farmersdelight:melon_popsicle" /></ItemGrid> | The one frozen dessert here, eaten from the hand. |
| Drinks and custard | <ItemGrid><ItemIcon id="farmersdelight:hot_cocoa" /><ItemIcon id="farmersdelight:apple_cider" /><ItemIcon id="farmersdelight:melon_juice" /><ItemIcon id="farmersdelight:glow_berry_custard" /></ItemGrid> | Hot cocoa, apple cider and glow berry custard are pot recipes with no separate container input. Melon juice is a shapeless craft. |

- [Hunger & variety](food.hunger.md) Effects, the Food Book and lunch containers.
- [Crop ingredients](food.growing.md) Grow the vegetables above.
- [Machine kitchens](food.machine-cooking.md) Automate slicing and drinks.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Farmer's Delight](images/catalog-r2oftaxm.png) [Farmer's Delight](food.utensils.md) | Adds crops, cooking utensils and meal preparation with cutting boards and cooking pots. | <EmiSearch query="@farmersdelight" /> |
