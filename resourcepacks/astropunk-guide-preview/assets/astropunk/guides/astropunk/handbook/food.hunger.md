---
navigation:
  title: "Hunger & variety"
  position: 1
  parent: reference.food.md
  icon: minecraft:apple
---

# Hunger & variety

## Hunger & saturation

<ItemGrid>
  <ItemIcon id="minecraft:apple" />
  <ItemIcon id="minecraft:bread" />
  <ItemIcon id="minecraft:cooked_beef" />
</ItemGrid>

AppleSkin shows both hunger restoration and saturation in food tooltips. Hunger fills the visible bar. Saturation is the reserve spent before that bar falls. Compare <ItemLink id="minecraft:bread" />, <ItemLink id="minecraft:cooked_beef" /> and <ItemLink id="minecraft:apple" /> by their tooltip values. Status effects are separate from both values.

***

## Rolling diet

<EmiSearch query="@solonion" />

<ItemGrid>
  <ItemIcon id="solonion:food_book" />
  <ItemIcon id="solonion:lunchbag" />
  <ItemIcon id="solonion:lunchbox" />
  <ItemIcon id="solonion:golden_lunchbox" />
</ItemGrid>

The pack tracks the last 16 counted meals with dietary decay enabled. Each distinct food contributes its strongest remaining entry. Eating the same food refreshes its own contribution but does not add another distinct food. Other foods become older and eventually leave the history, so rewards depend on the current diet rather than lifetime discoveries.

Use the inventory diet button or <ItemLink id="solonion:food_book" /> to inspect variety and rewards. The inventory button is enabled by default, so carrying the book is optional. Its shipped detriment list is empty. Repetition can lower variety and remove rewards, but it is not a rule that repeatedly eaten food restores less hunger.

***

## Packing meals

<ItemGrid>
  <ItemIcon id="solonion:lunchbag" />
  <ItemIcon id="solonion:lunchbox" />
  <ItemIcon id="solonion:golden_lunchbox" />
</ItemGrid>

Use <ItemLink id="solonion:lunchbag" /> or <ItemLink id="solonion:lunchbox" /> for food storage. <ItemLink id="solonion:golden_lunchbox" /> is another container, not another edible dish. Short Stacks changes food stack limits, so inspect the actual limit before filling your bag. Pack different meals for variety, then compare their filling power separately.

- [Kitchen meals](food.utensils.md)
- [Crop ingredients](food.growing.md)
- [Fish meals](food.fishing.md)

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![AppleSkin](images/catalog-esafcjcv.png) [AppleSkin](food.hunger.md) | Shows food hunger restoration and saturation in tooltips and the hunger display. | No separate item search |
| <ItemImage id="minecraft:wheat" /> [Short Stacks](food.hunger.md) | Changes food stack limits to alter how much food fits in each inventory slot. | No separate item search |
| ![Spice of Life Onion](images/catalog-ehgygkjz.png) [Spice of Life Onion](food.hunger.md) | Rewards dietary variety using a rolling history of recently eaten foods. | <EmiSearch query="@solonion" /> |
