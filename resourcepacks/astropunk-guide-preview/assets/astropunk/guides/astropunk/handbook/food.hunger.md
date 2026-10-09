---
navigation:
  title: "Hunger & variety"
  position: 0
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

AppleSkin shows both hunger restoration and saturation in food tooltips. Hunger fills the visible bar. Saturation is the reserve spent before that bar falls. Compare <ItemLink id="minecraft:bread" /> with <ItemLink id="minecraft:cooked_beef" /> instead of judging a meal by its name. Use <ItemLink id="minecraft:apple" /> as a fruit comparison too. Status effects are separate from both values.

***

## Rolling diet

<ItemGrid>
  <ItemIcon id="solonion:food_book" />
  <ItemIcon id="solonion:lunchbag" />
  <ItemIcon id="solonion:lunchbox" />
  <ItemIcon id="solonion:golden_lunchbox" />
</ItemGrid>

The pack tracks the last 16 counted meals with dietary decay enabled. Each distinct food contributes its strongest remaining entry. Eating the same food refreshes its own contribution but does not add another distinct food. Other foods become older and eventually leave the history, so rewards depend on the current diet rather than lifetime discoveries.

Use the inventory diet button or <ItemLink id="solonion:food_book" /> to inspect variety and rewards. The selected release enables the inventory button by default, so checking your diet does not require carrying the book. Its shipped detriment list is empty. Repetition can lower variety and remove rewards, but it is not a rule that repeatedly eaten food restores less hunger.

***

## Packing meals

<ItemGrid>
  <ItemIcon id="solonion:lunchbag" />
  <ItemIcon id="solonion:lunchbox" />
  <ItemIcon id="solonion:golden_lunchbox" />
</ItemGrid>

Use <ItemLink id="solonion:lunchbag" /> or <ItemLink id="solonion:lunchbox" /> for food storage. <ItemLink id="solonion:golden_lunchbox" /> is another container, not another edible dish. Short Stacks changes food stack limits, so inspect the actual limit before filling your bag. Carry different finished meals to maintain diet variety, and compare their filling power separately.

- [Kitchen meals](food.utensils.md)
- [Crop ingredients](food.growing.md)
- [Fish meals](food.fishing.md)
