---
navigation:
  title: "Fishing"
  position: 3
  parent: reference.food.md
  icon: minecraft:cod
item_ids:
  - starcatcher:starcatcher_rod
  - starcatcher:starcatcher_guide
  - starcatcher:tackle_box_cyan
  - starcatcher:fish_radar
---

# Fishing

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Starcatcher%20fishing%20rod%20guide%20minigame%20tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft%201.21.1%20Starcatcher%20%E9%92%93%E9%B1%BC%20%E9%B1%BC%E7%AB%BF%20%E6%8C%87%E5%8D%97%20%E5%B0%8F%E6%B8%B8%E6%88%8F%20%E6%95%99%E7%A8%8B)

## Get the guide


Starcatcher's Rod is the only rod that reaches the Starcatcher catch table. It needs one hook and one bobber in its recipe, and the mod states that a rod will not work without both.


Starcatcher's Guide is the lookup for every species. It lists the biome, fluid, height, light, time, weather and bait each fish needs, so read an entry before you travel.

<Recipe id="starcatcher:starcatcher_rod" />

<Recipe id="starcatcher:starcatcher_guide" />

1. Craft the rod from two sticks, one string, a hook and a bobber.
2. Craft the guide from the rod and one book, shapeless.
3. Use the guide, or press the Open guide key binding, to read entries.

Each entry states the biome, the fluid, the dimension, the height band and light, and the time and weather it needs. Biome is only the first filter, because one biome can hold a surface lake and a cave pool with different fish. Read the entry, then choose the water, and treat the guide as the only condition list.

<EmiSearch query="@starcatcher" />

***

## First cast

![Reeling in a Starcatcher catch](images/visual-fishing-reeling.png)

Reeling in a Starcatcher catch

1. Stand at water that matches the entry you picked and cast.
2. Wait for the bite, then reel. A minigame opens with the fish on the hook.
3. Hit the highlighted zones with <KeyBind id="key.starcatcher.minigame_hit" /> until the meter fills.

The catch is confirmed when the fish item, or its bucket form, reaches your inventory and the guide records the entry. A vanilla fishing rod still pulls vanilla loot from the same water.

***

## Tackle

<ItemGrid><ItemIcon id="starcatcher:hook" /><ItemIcon id="starcatcher:bobber" /></ItemGrid>

A hook and a bobber are the two parts every cast needs. Beyond that, hooks, bobbers and baits act as modifiers on the same cast, and the guide entry states the conditions for the fish you want.

<ItemGrid><ItemIcon id="starcatcher:worm" /><ItemIcon id="starcatcher:cherry_bait" /><ItemIcon id="starcatcher:tackle_box_cyan" /></ItemGrid>

Baits change the modifiers of a cast, and the tackle box stores attachments and swaps them without a crafting table. Change one attachment at a time, then repeat a short cast, so you can tell which change helped.

***


## Keep the catch

<ItemGrid><ItemIcon id="starcatcher:aquarium" /><ItemIcon id="starcatcher:oak_fish_plaque" /><ItemIcon id="starcatcher:tournament_stand" /><ItemIcon id="starcatcher:fish_radar" /></ItemGrid>

Most catches are food and belong in [Seafood](food.seafood.md). A bucket keeps a catch alive, and <ItemLink id="starcatcher:aquarium" /> holds bucketed fish and scales the model to the recorded size. A <ItemLink id="starcatcher:oak_fish_plaque" /> mounts one catch, a <ItemLink id="starcatcher:tournament_stand" /> runs a timed contest, and <ItemLink id="starcatcher:fish_radar" /> reads fishing possibilities nearby.

- [Seafood](food.seafood.md) Cook the catch.
- [Hunger & variety](food.hunger.md) Fit fish into a varied diet.
- [Crop ingredients](food.growing.md) Grow the starch and vegetables beside the fish.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Hybrid Aquatic + Starcatcher Compatibility](images/catalog-onrvj8th.png) [Hybrid Aquatic + Starcatcher Compatibility](food.fishing.md) | Adds Hybrid Aquatic catches to Starcatcher fishing. | <EmiSearch query="@hybrid_aquatic" /> |
| ![Starcatcher](images/catalog-h2jxvxnr.png) [Starcatcher](food.fishing.md) | Adds habitat-dependent fishing, equipment and a fishing guide. | <EmiSearch query="@starcatcher" /> |
