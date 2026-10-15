# Space travel titles

The Paxi resource pack `astropunk-space-titles` supplies Traveler's Titles names for Luna, Deep Space and all seven lunar biomes in English and Simplified Chinese. The earlier Mars entries were retired with Create Cosmonautics Expansion.

The selected Cosmonautics English language files lack biome names, and Traveler's Titles 5.1.3 lacks their dimension titles. Upstream documents resource-pack title customization; its 1.21 render manager skips biomes with no translation and uses question marks for unnamed dimensions. These omissions explain missing biome names but do not establish every cause of a title failing to display in Lucas's running installation.

Use Traveler's Titles-specific biome keys rather than renaming biomes globally. No new mods, colors, sounds, gameplay changes or title setting overrides are introduced. Lunar Terrae, Lunar Maria and Lunar Megaregolith use geological terminology. Other biome names describe the existing content rather than claiming that randomly generated features correspond to named real-world locations. Luna is a conventional Latin name, not a claim that the Moon lacks an official common name.

Verify key coverage against released archive biome identifiers and dimension identifiers, matching English and Chinese keys, valid JSON and exact resource inclusion in exports. In-game display, ship interiors, surface-only title restrictions, biome history caching and debug-overlay suppression remain untested. This is a small localization fix, not a renderer patch. Existing player title preferences are preserved.

Sources:

- https://www.curseforge.com/minecraft/mc-mods/travelers-titles
- https://github.com/YUNG-GANG/Travelers-Titles/blob/1.21/Common/src/main/java/com/yungnickyoung/minecraft/travelerstitles/render/TitleRenderManager.java
- https://science.nasa.gov/moon/composition/
- Released `cosmonautics-26.08.307.jar`, `rocketnautics_addon-1.0.0.jar` and `TravelersTitles-1.21.1-NeoForge-5.1.3.jar` language and biome resources.
