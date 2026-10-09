---
navigation:
  title: "Fishing"
  position: 0
  parent: reference.food.md
  icon: minecraft:apple
---

# Fishing

## Vanilla catches

<ItemGrid>
  <ItemIcon id="minecraft:cod" />
  <ItemIcon id="minecraft:salmon" />
  <ItemIcon id="minecraft:tropical_fish" />
  <ItemIcon id="minecraft:pufferfish" />
</ItemGrid>

A fishing rod supplies vanilla catches. Cod and salmon have cooked forms and cutting uses. Tropical fish and pufferfish should not be treated as equivalent cooked fillets.

- <ItemLink id="minecraft:cod" /> Catch with a fishing rod or harvest a cod fish. Cook it whole or use a cutting-board recipe for portions.
- <ItemLink id="minecraft:salmon" /> Catch with a fishing rod or harvest a salmon fish. Whole fish and cut portions are distinct recipe inputs.
- <ItemLink id="minecraft:tropical_fish" /> A vanilla catch with separate ingredient uses. It has no ordinary cooked-fish counterpart.
- <ItemLink id="minecraft:pufferfish" /> A vanilla catch that is unsafe as ordinary food. Check its specific recipe uses rather than packing it as cooked fish.

***

## Spawn fish meals

- Browse items: <EmiSearch query="@farmersdelight" /> <EmiSearch query="@spawn" />

<ItemGrid>
  <ItemIcon id="spawn:tuna_chunk" />
  <ItemIcon id="spawn:cooked_tuna_chunk" />
  <ItemIcon id="spawn:tuna_slice" />
  <ItemIcon id="spawn:tuna_roll" />
  <ItemIcon id="spawn:tuna_sandwich" />
  <ItemIcon id="spawn:herring" />
  <ItemIcon id="spawn:cooked_herring" />
  <ItemIcon id="spawn:herring_roll" />
  <ItemIcon id="spawn:canned_herring" />
  <ItemIcon id="spawn:bluefish" />
  <ItemIcon id="spawn:cooked_bluefish" />
  <ItemIcon id="spawn:bluefish_roll" />
</ItemGrid>

Recipe inputs and serving containers

<ItemGrid>
  <ItemIcon id="minecraft:dried_kelp" />
  <ItemIcon id="farmersdelight:cooked_rice" />
  <ItemIcon id="minecraft:bread" />
  <ItemIcon id="farmersdelight:cabbage" />
  <ItemIcon id="spawn:herring_slice" />
  <ItemIcon id="spawn:cooked_herring_slice" />
  <ItemIcon id="spawn:bluefish_slice" />
</ItemGrid>

Spawn adds aquatic creatures as ingredient sources. Tuna portions support rolls and sandwiches. Herring and Bluefish have their own cooked and rolled forms. Bucket capture and creature harvesting are different from ordinary fishing-rod loot.

- <ItemLink id="spawn:tuna_chunk" /> Keep this as an input for <ItemLink id="spawn:cooked_tuna_chunk" />. Its recipe uses cook in a furnace.
- <ItemLink id="spawn:cooked_tuna_chunk" /> Cook in a furnace using 1 <ItemLink id="spawn:tuna_chunk" />. Yield 1.
- <ItemLink id="spawn:tuna_slice" /> Cut on the cutting board with a knife using 1 <ItemLink id="spawn:tuna_chunk" />. Yield 2.
- <ItemLink id="spawn:tuna_roll" /> Combine in the crafting grid using 1 <ItemLink id="spawn:tuna_slice" /> plus 1 <ItemLink id="minecraft:dried_kelp" /> plus 1 <ItemLink id="farmersdelight:cooked_rice" />. Yield 3.
- <ItemLink id="spawn:tuna_sandwich" /> Combine in the crafting grid using 1 <ItemLink id="minecraft:bread" /> plus 1 <ItemLink id="spawn:cooked_tuna_chunk" /> plus 2 <ItemLink id="farmersdelight:cabbage" /> or another accepted cabbage. Yield 1.
- <ItemLink id="spawn:herring" /> Keep this as an input for <ItemLink id="spawn:cooked_herring" />. Its recipe uses cook in a furnace.
- <ItemLink id="spawn:cooked_herring" /> Cook in a furnace using 1 <ItemLink id="spawn:herring" />. Yield 1.
- <ItemLink id="spawn:herring_roll" /> Combine in the crafting grid using 3 <ItemLink id="spawn:herring_slice" /> plus 1 <ItemLink id="farmersdelight:cooked_rice" />. Yield 2.
- <ItemLink id="spawn:canned_herring" /> Arrange in the crafting grid using 9 <ItemLink id="spawn:cooked_herring_slice" />. Yield 1.
- <ItemLink id="spawn:bluefish" /> Keep this as an input for <ItemLink id="spawn:bluefish_roll" />. Its recipe uses combine in the crafting grid.
- <ItemLink id="spawn:cooked_bluefish" /> Cook in a furnace using 1 <ItemLink id="spawn:bluefish" />. Yield 1.
- <ItemLink id="spawn:bluefish_roll" /> Combine in the crafting grid using 2 <ItemLink id="spawn:bluefish_slice" /> plus 1 <ItemLink id="farmersdelight:cooked_rice" />. Yield 2.

***

## Shellfish & capture

<ItemGrid>
  <ItemIcon id="spawn:clam" />
  <ItemIcon id="spawn:cooked_clam" />
  <ItemIcon id="spawn:steamed_clams" />
  <ItemIcon id="spawn:clam_chowder" />
  <ItemIcon id="spawn:coastal_crab_claw" />
  <ItemIcon id="spawn:crab_boil" />
  <ItemIcon id="spawn:casting_net" />
  <ItemIcon id="spawn:herring_bucket" />
  <ItemIcon id="spawn:bluefish_bucket" />
</ItemGrid>

Recipe inputs and serving containers

<ItemGrid>
  <ItemIcon id="minecraft:bread" />
  <ItemIcon id="farmersdelight:cabbage" />
  <ItemIcon id="farmersdelight:tomato" />
  <ItemIcon id="farmersdelight:onion" />
  <ItemIcon id="minecraft:potato" />
  <ItemIcon id="farmersdelight:milk_bottle" />
  <ItemIcon id="minecraft:bowl" />
  <ItemIcon id="spawn:shell_fragments" />
  <ItemIcon id="minecraft:string" />
</ItemGrid>

Clams supply a shellfish branch and Coastal Crab Claws supply crab dishes. With Farmer’s Delight selected, Clam Chowder uses cooked clam, potato and milk in a heated cooking pot, with a bowl for serving. The fallback crafting recipe without Farmer’s Delight is not the selected route.

- <ItemLink id="spawn:clam" /> Keep this as an input for <ItemLink id="spawn:cooked_clam" />. Its recipe uses cook in a furnace.
- <ItemLink id="spawn:cooked_clam" /> Cook in a furnace using 1 <ItemLink id="spawn:clam" />. Yield 1.
- <ItemLink id="spawn:steamed_clams" /> Combine in the crafting grid using 1 <ItemLink id="minecraft:bread" /> or another accepted bread plus 2 <ItemLink id="spawn:cooked_clam" /> plus 1 <ItemLink id="farmersdelight:cabbage" /> or another accepted cabbage plus 1 <ItemLink id="farmersdelight:tomato" /> or another accepted tomato plus 1 <ItemLink id="farmersdelight:onion" /> or another accepted onion. Yield 1.
- <ItemLink id="spawn:clam_chowder" /> Combine in a heated cooking pot using 1 <ItemLink id="spawn:cooked_clam" /> plus 1 <ItemLink id="minecraft:potato" /> plus 1 <ItemLink id="farmersdelight:milk_bottle" />. Yield 1. Serve in <ItemLink id="minecraft:bowl" />.
- <ItemLink id="spawn:coastal_crab_claw" /> This entry is a serving, container or specialized ingredient rather than a complete meal recipe. Inspect its serving action or tooltip before planning production.
- <ItemLink id="spawn:crab_boil" /> This entry is a serving, container or specialized ingredient rather than a complete meal recipe. Inspect its serving action or tooltip before planning production.
- <ItemLink id="spawn:casting_net" /> Arrange in the crafting grid using 1 <ItemLink id="spawn:shell_fragments" /> plus 6 <ItemLink id="minecraft:string" />. Yield 1.
- <ItemLink id="spawn:herring_bucket" /> This entry is a serving, container or specialized ingredient rather than a complete meal recipe. Inspect its serving action or tooltip before planning production.
- <ItemLink id="spawn:bluefish_bucket" /> This entry is a serving, container or specialized ingredient rather than a complete meal recipe. Inspect its serving action or tooltip before planning production.

***

## Related topics

- [Food & hunger](food.hunger.md)
- [Crop ingredients](food.growing.md)
- [Cooking tools](food.utensils.md)
