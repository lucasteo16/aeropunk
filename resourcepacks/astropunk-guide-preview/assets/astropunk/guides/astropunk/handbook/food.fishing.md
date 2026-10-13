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

## Starcatcher

<EmiSearch query="@starcatcher" />

![Reeling in a Starcatcher catch](images/visual-fishing-reeling.png)

Reeling in a Starcatcher catch

<ItemGrid>
  <ItemIcon id="starcatcher:starcatcher_rod" />
  <ItemIcon id="starcatcher:starcatcher_guide" />
  <ItemIcon id="starcatcher:hook" />
  <ItemIcon id="starcatcher:bobber" />
  <ItemIcon id="starcatcher:tackle_box_cyan" />
</ItemGrid>

Starcatcher adds habitat-dependent catches and a reeling minigame. Use <ItemLink id="starcatcher:starcatcher_rod" /> for these catches. An ordinary Minecraft rod supplies basic catches rather than the full Starcatcher collection.

| Equipment | Purpose |
| --- | --- |
| <ItemLink id="starcatcher:starcatcher_guide" /> | Catch collection, species requirements and the mod's fishing instructions. |
| <ItemLink id="starcatcher:hook" /> and <ItemLink id="starcatcher:bobber" /> | Required rod attachments. Different types change fishing modifiers. |
| <ItemLink id="starcatcher:tackle_box_cyan" /> | Stores catches and tackle, and lets you change rod attachments. Colored variants serve the same purpose. |

***

## Getting started

![Tackle Boxes and fishing attachments](images/visual-fishing-tackle.png)

Tackle Boxes and fishing attachments

<Recipe id="starcatcher:starcatcher_rod" />

<Recipe id="starcatcher:starcatcher_guide" />

1. Craft the rod and keep its hook and bobber fitted. Use a Tackle Box to change attachments.

2. Cast into suitable water and reel when a fish bites.

3. During the minigame, hit the fish's sweet spots using <KeyBind id="key.starcatcher.minigame_hit" />.

Frozen and treasure sweet spots behave differently. The Guide's Sweetspot Types and Minigame Settings entries explain the timing and provide practice.

Check a species in the Guide before choosing a fishing spot. Matching the biome alone is not enough. Fluid, dimension, elevation, time, weather, light and bait can also restrict a catch.

***

## Bait & special catches

<ItemGrid>
  <ItemIcon id="starcatcher:worm" />
  <ItemIcon id="starcatcher:cherry_bait" />
  <ItemIcon id="starcatcher:amethyst_hook" />
  <ItemIcon id="starcatcher:vanilla_hook" />
  <ItemIcon id="starcatcher:vanilla_bobber" />
  <ItemIcon id="minecraft:bucket" />
</ItemGrid>

Worms and specialized baits change lure time or catch selection. Cherry Bait favors cherry-grove fish. A preferred bait improves selection, while a required bait is a condition that must be met.

The Vanilla-flavoured Hook paired with the Vanilla-flavoured Bobber skips the minigame. Lava fishing needs an Amethyst Hook or a netherite-upgraded rod. Nether and End catches still require their own dimensions and fluids.

Use a bucket as bait for species whose Guide entry supports bucket capture. An Almighty Worm produces a living catch where the species supports it. Not every catch has a summonable model or a bucket form.

***

## Hybrid Aquatic catches

<EmiSearch query="@hybrid_aquatic" />

The Hybrid Aquatic compatibility addon adds its fish to Starcatcher's catch definitions. They share the Guide and minigame but keep their species-specific conditions. Natural swimming creatures and rod catches use different rules. Seeing an animal nearby does not guarantee a rod can catch it there.

***

## Storage & collecting

![Living catches in aquariums](images/visual-fishing-aquariums.png)

Living catches in aquariums

<ItemGrid>
  <ItemIcon id="starcatcher:oak_tackle_box_boat" />
  <ItemIcon id="starcatcher:aquarium" />
  <ItemIcon id="starcatcher:oak_fish_plaque" />
  <ItemIcon id="starcatcher:tournament_stand" />
  <ItemIcon id="starcatcher:fish_radar" />
</ItemGrid>

Tackle Box Boats combine boat travel with fishing storage. Aquariums hold living bucketed catches, while Fish Plaques display catches. A Tournament Stand hosts optional competitions. Fish Radar is a later tool for viewing local fishing possibilities, not a prerequisite for the first catch.

***

## Related topics

- [Fishing habitats](fishing.habitats.md)
- [Seafood & preparation](food.seafood.md)
- [Aquatic wildlife](adventure.aquatic.md)
- [Food stacks & variety](food.hunger.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Hybrid Aquatic + Starcatcher Compatibility](images/catalog-onrvj8th.png) [Hybrid Aquatic + Starcatcher Compatibility](food.fishing.md) | Adds Hybrid Aquatic catches to Starcatcher fishing. | <EmiSearch query="@hybrid_aquatic" /> |
| ![Starcatcher](images/catalog-h2jxvxnr.png) [Starcatcher](food.fishing.md) | Adds habitat-dependent fishing, equipment and a fishing guide. | <EmiSearch query="@starcatcher" /> |
