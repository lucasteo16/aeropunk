---
navigation:
  title: "Hunger & variety"
  position: 1
  parent: reference.food.md
  icon: minecraft:apple
---

# Hunger & variety

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Farmer%27s%20Delight%20hunger%20saturation%20diet%20variety%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20%E5%86%9C%E5%A4%AB%E4%B9%90%E4%BA%8B%20%E9%A5%A5%E9%A5%BF%20%E9%A5%B1%E5%92%8C%E5%BA%A6%20%E9%A5%AE%E9%A3%9F%E5%A4%9A%E6%A0%B7%E6%80%A7%20%E6%95%99%E7%A8%8B)

## Read a food

<ItemGrid><ItemIcon id="minecraft:bread" /><ItemIcon id="minecraft:cooked_beef" /><ItemIcon id="minecraft:apple" /></ItemGrid>

AppleSkin is installed, so the food tooltip shows both values without a key press.

| Line | What it controls | Where you see it |
| --- | --- | --- |
| Hunger | Refills the visible bar | Tooltip and the hunger bar preview |
| Saturation | The hidden reserve spent before hunger falls | Tooltip and the saturation overlay |
| Effect | A potion icon and its duration | Tooltip as well as your effect list |

Saturation is the number that keeps the bar full while you sprint and fight, so a lower hunger value with higher saturation can still last longer. The effect line is the other half of the choice, and it belongs to the dish rather than to a food family.

***

## Comfort and Nourishment

<EmiSearch query="@farmersdelight" />

Farmer's Delight adds two effects, and this pack keeps the vanilla soup override on, so ordinary soups join them.

<ItemGrid><ItemIcon id="minecraft:mushroom_stew" /><ItemIcon id="minecraft:beetroot_soup" /><ItemIcon id="minecraft:rabbit_stew" /></ItemGrid>

| Effect | What it does | Visible sign |
| --- | --- | --- |
| Comfort | Provides natural regeneration, regardless of how hungry you are | A scrolling overlay on the health bar, enabled in this pack |
| Nourishment | Prevents the food meter from decreasing, except when healing with saturation | A gilded overlay on the hunger bar, enabled in this pack |

Comfort is the effect to look for when you are hurt and too hungry to regenerate on your own. Nourishment is the effect to look for before a long fight, because the bar stops draining. Read the effect line on the dish you are holding, because the effect comes from the item and not from the bowl or the plate.

The soup override covers <ItemLink id="minecraft:mushroom_stew" />, <ItemLink id="minecraft:beetroot_soup" /> and <ItemLink id="minecraft:rabbit_stew" />, and the pack also makes those three stack to sixteen like a cooked meal.

***

## Food variety

<EmiSearch query="@solonion" />

<ItemGrid><ItemIcon id="solonion:food_book" /><ItemIcon id="solonion:lunchbag" /><ItemIcon id="solonion:lunchbox" /><ItemIcon id="solonion:golden_lunchbox" /></ItemGrid>

The pack records your last sixteen counted meals, and old entries decay out of the record. A distinct food adds its strongest entry, and eating it again refreshes that entry instead of adding a second one.

<ItemLink id="solonion:food_book" /> shows current food diversity, the benefits above and below their thresholds, and the queue of foods still counting. Benefits are attribute based and include health, damage, regeneration, movement speed and armor toughness, so a wider record is a real stat gain and not only a habit.

| Setting | Value here | Result |
| --- | --- | --- |
| Tracked meals | 16 | Only recent meals count |
| Diversity decay | On | Old entries leave the record |
| Repetition | Refreshes one entry | Repeating a dish does not raise diversity |

Two different soups and one feast portion do more for the record than a chest of the same stew, and the Food Book states how many more meals a locked benefit needs.

***

## Carry meals

<ItemGrid><ItemIcon id="solonion:lunchbag" /><ItemIcon id="solonion:lunchbox" /><ItemIcon id="solonion:golden_lunchbox" /></ItemGrid>

A <ItemLink id="solonion:lunchbag" /> holds meals in one slot. Sneak and use it to open the container and place food inside. While you are hungry, an ordinary use of a filled container eats from it without opening the screen. One iron block upgrades it to a <ItemLink id="solonion:lunchbox" />, which keeps the contents and adds capacity, and the <ItemLink id="solonion:golden_lunchbox" /> is the largest form.

- [Cooking tools](food.utensils.md) The pot, the board and the meal groups.
- [Crop ingredients](food.growing.md) Cheap bowls from farm crops.
- [Seafood](food.seafood.md) Fish for a wider record.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![AppleSkin](images/catalog-esafcjcv.png) [AppleSkin](food.hunger.md) | Shows food hunger restoration and saturation in tooltips and the hunger display. | No separate item search |
| <ItemImage id="minecraft:wheat" /> [Short Stacks](food.hunger.md) | Changes food stack limits to alter how much food fits in each inventory slot. | No separate item search |
| ![Spice of Life Onion](images/catalog-ehgygkjz.png) [Spice of Life Onion](food.hunger.md) | Rewards dietary variety using a rolling history of recently eaten foods. | <EmiSearch query="@solonion" /> |
