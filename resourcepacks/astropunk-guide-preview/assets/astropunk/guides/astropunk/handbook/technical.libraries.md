---
navigation:
  title: "Libraries"
  position: 0
  parent: reference.technical.md
  icon: minecraft:redstone
---

# Libraries

## Loaders & languages

These components supply shared interfaces or language support. Connector supports selected Fabric mods on NeoForge, not every Fabric release.

| Component | Function |
| --- | --- |
| Sinytra Connector | Compatibility layer for selected Fabric mods on NeoForge. |
| Forgified Fabric API | Fabric interfaces implemented on NeoForge. |
| Architectury API | Shared cross-loader development interfaces. |
| Balm | Cross-loader abstraction library. |
| GroovyModLoader (GML) | Groovy language provider. |
| Kotlin for Forge | Kotlin language provider and utilities. |

***

## Configuration

These libraries provide settings, validation or settings-screen construction for other mods. They are not independent gameplay activities.

| Component | Function |
| --- | --- |
| Cloth Config API | Configuration screen library. |
| Fzzy Config | Configuration, validation and synchronization support. |
| MidnightLib | Lightweight configuration system. |
| Prickle | Configuration file support. |
| Resourceful Config | Cross-platform configuration support. |
| YetAnotherConfigLib (YACL) | Configuration screen construction library. |
| Apollib | Shared configuration and registry utilities. |

***

## Models & animation

These frameworks support animation, armor models and connected textures used by other content. A framework alone does not add a complete animated resource pack.

| Component | Function |
| --- | --- |
| Armor Model API | Renders custom armor geometry through the vanilla armor pipeline. |
| Geckolib | Animation library for entities, blocks, items and armor. |
| Lionfish-API | Animation framework. |
| playerAnimator | Player animation library. |
| EMF Compat: Core | Shared framework for EMF compatibility modules. |
| Athena | Connected-texture framework. |

***

## World & structures

These components support world generation or moving structures. Use the gameplay pages for destinations and vehicle components.

| Component | Function |
| --- | --- |
| Lithostitched | World-generation configuration and compatibility support. |
| Structure Pool API | Structure pool injection support. |
| YUNG's API | Shared code for YUNG's mods. |
| Sable | Framework for interactive moving block structures. |

***

## Combat frameworks

These components supply shared spell, attribute, weapon and projectile systems. Class equipment and spell choices are documented separately.

| Component | Function |
| --- | --- |
| More RPG Library | Shared framework for the More RPG series. |
| Spell Engine | Data-driven spell framework. |
| Spell Power Attributes | Spell-related attributes, effects and enchantment support. |
| Ranged Weapon API | Bow and crossbow development support. |
| Shield API | Custom shield model support. |
| Ritchie's Projectile Library | Projectile development support. |

***

## Shared code

Other installed supporting libraries are listed below. Keep required dependencies with the mods that use them. A library name is not a promise of new blocks, recipes or encounters.

| Component | Function |
| --- | --- |
| Almanac | Shared loader-independent code. |
| BaguetteLib | Death-handling and inventory-tracking support. |
| Bookshelf | Shared code library. |
| Bundle API | Item-tag-based bundle support. |
| Collective | Shared code for Serilum's mods. |
| CreativeCore | Shared core utilities. |
| DragonLib | Shared code for dependent mods. |
| Iceberg | Shared events and utilities. |
| JamLib | Cross-platform shared code. |
| Lodestone | Shared rendering and feature code for dependent mods. |
| MaFgLib | Shared code for Forge ports of masa's mods. |
| Moonlight Lib | Shared registration and dynamic content utilities. |
| MRU | Shared framework for dependent mods. |
| oωo (owo-lib) | General utilities, interfaces and configuration support. |
| Placebo | Shared foundation, not standalone gameplay content. |
| Puzzles Lib | Shared systems for Fuzss mods. |
| Resourceful Lib | Shared code library. |
| Searchables | Search, filtering and completion support for interfaces. |
| Sophisticated Core | Shared code for Sophisticated mods. |
| Teal Lib | Shared code library. |

***

## Related topics

- [Magic](combat.magic.md)
- [Vehicle assembly](vehicles.assembly.md)
- [Resource packs](visuals.resource-packs.md)


***

## Related mods

| Mod or content | Status | Publisher description |
| --- | --- | --- |
| ![Almanac](images/catalog-Gi02250Z.png) [Almanac](technical.libraries.md) | Baseline, installed | Almanac is a library used by my mods with mostly loader independent shared code between multiple mods to avoid duplication of code. |
| ![Apollib](images/catalog-VDI2Ytax.png) [Apollib](technical.libraries.md) | Baseline, installed | A tiny library for my configuration and registry utilities. |
| ![Architectury API](images/catalog-lhGA9TYQ.png) [Architectury API](technical.libraries.md) | Baseline, installed | An intermediary api aimed to ease developing multiplatform mods. |
| ![Armor Model API](images/catalog-onz2NN2n.png) [Armor Model API](technical.libraries.md) | Baseline, installed | Renders Bedrock/GeckoLib geo armor models through the vanilla armor pipeline. |
| ![Athena](images/catalog-b1ZV3DIJ.png) [Athena](technical.libraries.md) | Baseline, installed | A crossplatform (Forge/Fabric) solution to connected block textures for 1.19.4+ |
| ![BaguetteLib](images/catalog-OfKzpbRU.png) [BaguetteLib](technical.libraries.md) | Baseline, installed | Ever tried to make a mod that needs proper death handling or inventory tracking? Yeah, NeoForge events suck for that. |
| ![Balm](images/catalog-MBAkmtvl.png) [Balm](technical.libraries.md) | Baseline, installed | Abstraction Layer for Multi-Loader Mods |
| ![Bookshelf](images/catalog-uy4Cnpcm.png) [Bookshelf](technical.libraries.md) | Baseline, installed | An open source library for other mods! |
| ![Bundle API](images/catalog-n8QN6Z1a.png) [Bundle API](technical.libraries.md) | Baseline, installed | Bundle API allows mod authors to easily add bundles that can hold more than 1 stack of items specified by an item tag. |
| ![Cloth Config API](images/catalog-9s6osm5g.png) [Cloth Config API](technical.libraries.md) | Baseline, installed | Configuration Library for Minecraft Mods |
| ![Collective](images/catalog-e0M1UDsY.png) [Collective](technical.libraries.md) | Baseline, installed | 🎓 Collective is a shared library with common code for all of Serilum's mods. |
| ![Create: Dragons Plus](images/catalog-dzb1a5WV.png) [Create: Dragons Plus](technical.libraries.md) | Baseline, installed | Provide convenient features to players and dev utilities for Create addon developers. |
| ![CreativeCore](images/catalog-OsZiaDHq.png) [CreativeCore](technical.libraries.md) | Baseline, installed | A core mod |
| ![DragonLib](images/catalog-sbIsGaOV.png) [DragonLib](technical.libraries.md) | Baseline, installed | DragonLib is a small and simple library mod which contains code that is used by most of my mods. |
| ![EMF Compat: Core](images/catalog-hbGct5uU.png) [EMF Compat: Core](technical.libraries.md) | Baseline, installed | Shared framework for the EMF Compat family. |
| ![Forgified Fabric API](images/catalog-Aqlf1Shp.png) [Forgified Fabric API](technical.libraries.md) | Baseline, installed | Fabric API implemented on top of NeoForge |
| ![Fzzy Config](images/catalog-hYykXjDp.png) [Fzzy Config](technical.libraries.md) | Baseline, installed | Config API with automatic GUIs, powerful validation options, server-client sync, and more! |
| ![Geckolib](images/catalog-8BmcQJ2H.png) [Geckolib](technical.libraries.md) | Baseline, installed | A 3D animation library for entities, blocks, items, armor, and more! |
| ![GroovyModLoader (GML)](images/catalog-zg2tT2Vu.png) [GroovyModLoader (GML)](technical.libraries.md) | Baseline, installed | NeoForge language provider for Groovy mods. |
| ![Iceberg](images/catalog-5faXoLqX.png) [Iceberg](technical.libraries.md) | Baseline, installed | A modding library that contains new events, helpers, and utilities to make modder's lives easier. |
| ![JamLib](images/catalog-IYY9Siz8.png) [JamLib](technical.libraries.md) | Baseline, installed | The platform-agnostic, Architectury based library used in all of JamCoreModding's mods |
| ![Kotlin for Forge](images/catalog-ordsPcFz.png) [Kotlin for Forge](technical.libraries.md) | Baseline, installed | Adds a Kotlin language loader and provides some optional utilities. |
| ![Lionfish-API](images/catalog-FoVacERa.png) [Lionfish-API](technical.libraries.md) | Baseline, installed | Very Light Animation Api |
| ![Lithostitched](images/catalog-XaDC71GB.png) [Lithostitched](technical.libraries.md) | Baseline, installed | Library mod with new configurability and compatibility enhancements for worldgen |
| ![Lodestone](images/catalog-bN3xUWdo.png) [Lodestone](technical.libraries.md) | Baseline, installed | A collection of code used throughout projects under the Lodestar team. |
| ![MaFgLib](images/catalog-SKI34J7B.png) [MaFgLib](technical.libraries.md) | Baseline, installed | MaLiLib unofficial forge port. Library mod for the (Neo)Forge port of masa's mods. |
| ![MidnightLib](images/catalog-codAaoxh.png) [MidnightLib](technical.libraries.md) | Baseline, installed | Common library providing a lightweight configuration system |
| ![Moonlight Lib](images/catalog-twkfQtEc.png) [Moonlight Lib](technical.libraries.md) | Baseline, installed | dynamic data pack and registration, villager activities, custom map marker and a lot more |
| ![More RPG Library](images/catalog-Wkc3lwHo.png) [More RPG Library](technical.libraries.md) | Baseline, installed | Library for the More RPG Classes & More RPG Content Series. |
| ![MRU](images/catalog-SNVQ2c0g.png) [MRU](technical.libraries.md) | Baseline, installed | A library mod used by Cassian and IMB11's mods to function. |
| ![oωo (owo-lib)](images/catalog-ccKDOlHs.png) [oωo (owo-lib)](technical.libraries.md) | Baseline, installed | A general utility, GUI and config library for modding on Fabric and Quilt |
| ![Placebo](images/catalog-tCkE8p2N.png) [Placebo](technical.libraries.md) | Baseline, installed | Placebo is a library used by most of my mods. It does not provide any game-relevant features on its own (save for maybe a couple debug commands). |
| <ItemImage id="minecraft:redstone" /> [playerAnimator](technical.libraries.md) | Baseline, installed | animate the player |
| ![Prickle](images/catalog-aaRl8GiW.png) [Prickle](technical.libraries.md) | Baseline, installed | Prickle is a JSON based configuration file format brought to Minecraft. |
| ![Puzzles Lib](images/catalog-QAGBst4M.png) [Puzzles Lib](technical.libraries.md) | Baseline, installed | Why is it called Puzzles? That's the puzzle. |
| ![Ranged Weapon API](images/catalog-AqaIIO6D.png) [Ranged Weapon API](technical.libraries.md) | Baseline, installed | 🏹 Create fully functional bows and crossbows, with ease |
| ![Resourceful Config](images/catalog-M1953qlQ.png) [Resourceful Config](technical.libraries.md) | Baseline, installed | Resourceful Config is a mod that allows for developers to make cross-platform configs |
| ![Resourceful Lib](images/catalog-G1hIVOrD.png) [Resourceful Lib](technical.libraries.md) | Baseline, installed | Resourceful Lib |
| ![Ritchie's Projectile Library](images/catalog-B3pb093D.png) [Ritchie's Projectile Library](technical.libraries.md) | Baseline, installed | A Minecraft modding library for better projectiles. |
| ![Sable](images/catalog-T9PomCSv.png) [Sable](technical.libraries.md) | Baseline, installed | A library mod for interactive moving block structures, or "sub-levels" |
| ![Searchables](images/catalog-fuuu3xnx.png) [Searchables](technical.libraries.md) | Baseline, installed | Searchables is a library mod that adds helper methods that allow for searching and filtering elements based on components, as well as offering built in auto-complete functionality. |
| ![Shield API](images/catalog-y9clIFY4.png) [Shield API](technical.libraries.md) | Baseline, installed | Creating shields with custom models was never easier! |
| ![Sinytra Connector](images/catalog-u58R1TMW.png) [Sinytra Connector](technical.libraries.md) | Baseline, installed | Lets you play Fabric mods on NeoForge |
| ![Sophisticated Core](images/catalog-nmoqTijg.png) [Sophisticated Core](technical.libraries.md) | Baseline, installed | Library mod for Sophisticated mods |
| ![Spell Engine](images/catalog-XvoWJaA2.png) [Spell Engine](technical.libraries.md) | Baseline, installed | 🪄 Data driven magic library |
| ![Spell Power Attributes](images/catalog-8ooWzSQP.png) [Spell Power Attributes](technical.libraries.md) | Baseline, installed | 🔮 Spell Power entity attributes with related status effects and enchantments |
| ![Structure Pool API](images/catalog-LrYZi08Q.png) [Structure Pool API](technical.libraries.md) | Baseline, installed | 📚 API to inject structures into structure pools. |
| ![Teal Lib](images/catalog-rLJ1qF79.png) [Teal Lib](technical.libraries.md) | Baseline, installed | A library mod that's teal... That's the appeal |
| ![YetAnotherConfigLib (YACL)](images/catalog-1eAoo2KR.png) [YetAnotherConfigLib (YACL)](technical.libraries.md) | Baseline, installed | A builder-based configuration library for Minecraft! |
| ![YUNG's API](images/catalog-Ua7DFN59.png) [YUNG's API](technical.libraries.md) | Baseline, installed | Library mod for YUNG's mods. |
