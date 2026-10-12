# Fishing habitat integration

## Scope

The Minecraft 1.21.1 development pack uses Starcatcher 3.3.7 and Terralith 2.6.2, with Hybrid Aquatic 1.7.4 and its Starcatcher bridge 0.6.1. Paxi loads the fishing habitat pack globally, including new single-player and dedicated-server worlds. No played world or retained server has been updated.

The handbook lists 95 Terralith biomes. The released Terralith namespace contains the same count. The coverage table records every identifier once, including the rare island and skyland biomes omitted by Terralith's own all-biomes tag. Existing shared forest, jungle and taiga membership is retained.

## Habitat policy

Cherry fish also occur in Sakura Grove, Sakura Valley, Snowy Cherry Grove and Spring Skylands, which generates cherry trees. Cold freshwater follows Terralith's frozen and cold landscape groups, including winter islands and skylands, Birch Taiga and Windswept Spires. Arid, desert, badlands and savanna freshwater uses the warm-lake selection, including Granite Cliffs under Terralith's warm classification. Snowy Badlands is explicitly excluded from warm fish definitions because the upstream badlands tag includes it. Existing upstream category membership is never removed.

Flower-rich valleys and spring skylands receive flower-forest fish. Terralith's native flower-forest classification also supplies Petal Bass to Cloud Forest, both Moonlight biomes and both Sakura biomes. Open grasslands receive the prairie-themed Sunflower Carp. Birch Taiga retains birch habitat membership. Moonlight groves receive dark enchanted-forest fish. Frozen cliffs, glacial chasms and emerald peaks gain the ice-spike selection. Deep Warm Ocean joins ocean, deep-ocean and warm-ocean fishing groups, including the Hybrid bridge's deep warm ocean category.

Fungal caves and Underground Jungle receive lush-cave fish. Stone and thermal caves receive geological dripstone fish. Frostfire Caves contains actual sculk and dripstone features in the released terrain definitions, so it receives both matching cave selections. Ordinary deep, infested and mantle caves retain the existing underground freshwater selection instead of inventing new species or importing unrelated Nether fish.

The remaining landscapes retain temperate freshwater, forest, jungle or taiga selections. A biome assignment does not guarantee naturally generated water at every position. Surface and underground elevation limits still apply, as do time, weather, bait, light, fluid and other catch requirements.

## Implementation

Existing Starcatcher biome tags are extended additively. Six custom habitat tags include their original vanilla biome and appropriate Terralith equivalents. A seventh custom tag includes the original Hybrid deep warm ocean group and Terralith's equivalent. Thirty-three fish and associated collectible definitions have habitat overrides. Ten belong to the Hybrid bridge, twenty-one belong to Starcatcher, and two belong to its bundled Create integration. The eight warm-lake fish definitions exclude Snowy Badlands. The original rarity, base chance, bait, weather, time, light, dimension, fluid, elevation, difficulty, weight, size, treasures and reward fields are preserved.

No global Minecraft or Hybrid spawning tags are broadened. The custom deep warm ocean group is used only by fish definitions, because the original Hybrid API group also controls natural creature spawns. This connects fishing without treating arbitrary oceans as reefs or trenches or increasing wildlife density through habitat overrides.

## Verification and maintenance

Static verification checks all 95 coverage rows against the released registry, resolves habitat tags, verifies that every biome admits at least one water-fish entry at an appropriate surface or underground elevation, preserves vanilla tag entries, and compares every overridden definition with its publisher original. Archive verification checks native exports, mod metadata checksums and identical datapack bytes in client and server outputs.

The current review and per-biome results are in fishing-habitat-review.md and fishing-habitat-review.json. The earlier fishing-habitat-verification.json is retained as the 0.10.0 development snapshot. This is not a Minecraft startup or gameplay test. Fresh-world fishing, moving-boat fishing, underwater wildlife density, structure placement and the beta bridge remain untested. Recheck the thirty-three copied definitions after updating Starcatcher or the bridge, because replacement resources do not automatically inherit upstream changes. Prefer additive tag updates when a later upstream release exposes additional habitat tags.

## Sources

- https://modrinth.com/mod/starcatcher/version/eiqihg0A
- https://modrinth.com/mod/terralith/version/IY93YaEe
- https://modrinth.com/mod/hybrid-aquatic-starcatcher-compatibility/version/dx5fbOBU
- https://github.com/wdiscute/starcatcher/wiki/For-Modpack-Developers
