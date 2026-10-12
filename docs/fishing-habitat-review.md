# Fishing habitat review

## Result

Development release 0.10.1 covers all 95 Terralith biome identifiers. Biome-themed live fish occur in 86 biomes, or 90.5 percent, compared with 83 before this review. Including Clam and Conch raises themed aquatic coverage to 87 biomes, or 91.6 percent. Counts exclude collectibles and junk. They measure biome types, not generated terrain area or catch probability.

## Corrections and additions

- Snowy Badlands inherited six desert fish through the upstream common badlands tag despite being frozen. The six Starcatcher warm-lake definitions and two bundled Create counterparts now blacklist this biome. Its eight cold freshwater fish remain available. This leaves upstream biome tags intact.
- Spring Skylands generates cherry trees through its released tree placement. Its catch habitat now includes the five cherry fish alongside Petal Bass.
- Petal Bass now follows the common flower-forest tag as well as the explicitly selected flower biomes. This adds Cloud Forest, both Moonlight biomes and both Sakura biomes, bringing Terralith flower coverage from five biomes to ten.
- Birch Taiga has temperature 0.22, and Windswept Spires has temperature 0.2 with spruce trees. Both now share the eight cold freshwater fish already used in other cool taiga and highland habitats.
- Granite Cliffs is in Terralith's released warm and lukewarm groups. It now shares the six warm freshwater fish rather than only the general freshwater pool.
- The coverage table now identifies Mirage Isles' existing mushroom fish instead of describing it only as temperate freshwater. This is a documentation correction, not a new fishing change.

## Retained choices

The other assignments remain suitable under the existing habitat policy. Cold selections follow Terralith's own cold and frozen groups, including its unusual classification of Moonlight landscapes. Geological cave fish are shared with stone caves, flower fish with flowering landscapes, and Sunflower Carp with open grassland equivalents. These are intentional broader habitat themes, not a strict requirement that every position contain the original vanilla vegetation.

Dense-bamboo catches remain restricted to the original Bamboo Jungle habitat. Sparse bamboo in Terralith jungles and Sakura groves is not enough evidence to treat them as dense bamboo forests. Nether and End catches retain their original dimension restrictions; no lava fish were moved into ordinary Overworld water.

## Verification

All 33 replacement definitions preserve every original non-biome field, including rarity, chance, bait, time, weather, fluid, dimension, elevation, difficulty and rewards. The review checks positive and negative habitat matches, all 95 biome identifiers, and water eligibility at suitable surface or underground elevation. It does not alter Minecraft or Hybrid creature-spawning tags. The current per-biome results are in fishing-habitat-review.json; fishing-habitat-verification.json remains the earlier development snapshot.

The selected released archives are the source for biome features, native tag membership and fish definitions. No startup, terrain-area measurement or fishing gameplay test was performed. Native exports are checked separately for identical habitat files, unchanged mod payloads and the current release version. Stable branches, played installations and the retained server remain unchanged.
