---
navigation:
  title: "Libraries"
  position: 0
  parent: reference.technical.md
  icon: minecraft:bookshelf
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

<EmiSearch query="@more_rpg_classes" /> <EmiSearch query="@spell_engine" />

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

<EmiSearch query="@dragonlib" /> <EmiSearch query="@moonlight" /> <EmiSearch query="@sophisticatedcore" /> <EmiSearch query="@teallib" />

Other supporting libraries are listed below. Keep required dependencies with the mods that use them. A library name is not a promise of new blocks, recipes or encounters.

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

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Almanac](images/catalog-Gi02250Z.png) [Almanac](technical.libraries.md) | Shares loader-independent code and fixes item stacking issues caused by empty tags. | No separate item search |
| ![Apollib](images/catalog-VDI2Ytax.png) [Apollib](technical.libraries.md) | Shared configuration and registry utilities. | No separate item search |
| ![Architectury API](images/catalog-lhGA9TYQ.png) [Architectury API](technical.libraries.md) | Shared cross-loader development interfaces. | No separate item search |
| ![Armor Model API](images/catalog-onz2NN2n.png) [Armor Model API](technical.libraries.md) | Renders custom armor geometry through the vanilla armor pipeline. | No separate item search |
| ![Athena](images/catalog-b1ZV3DIJ.png) [Athena](technical.libraries.md) | Provides cross-loader connected block texture support. | No separate item search |
| ![BaguetteLib](images/catalog-OfKzpbRU.png) [BaguetteLib](technical.libraries.md) | Death-handling and inventory-tracking support. | No separate item search |
| ![Balm](images/catalog-MBAkmtvl.png) [Balm](technical.libraries.md) | Shares loader-independent systems so dependent mods can run on multiple loaders. | No separate item search |
| ![Bookshelf](images/catalog-uy4Cnpcm.png) [Bookshelf](technical.libraries.md) | Provides shared serialization, data-pack features and debugging tools for dependent mods. | No separate item search |
| ![Bundle API](images/catalog-n8QN6Z1a.png) [Bundle API](technical.libraries.md) | Provides larger bundles restricted to items selected by tags. | No separate item search |
| ![Cloth Config API](images/catalog-9s6osm5g.png) [Cloth Config API](technical.libraries.md) | Configuration screen library. | No separate item search |
| ![Collective](images/catalog-e0M1UDsY.png) [Collective](technical.libraries.md) | Provides shared functionality for Serilum's utility mods. | No separate item search |
| ![Create: Dragons Plus](images/catalog-dzb1a5WV.png) [Create: Dragons Plus](technical.libraries.md) | Adds bulk fan processing and fluid tank access tools, plus shared Create addon utilities. | <EmiSearch query="@create_dragons_plus" /> |
| ![CreativeCore](images/catalog-OsZiaDHq.png) [CreativeCore](technical.libraries.md) | Provides shared interface, configuration and network systems for CreativeMD's mods. | No separate item search |
| ![DragonLib](images/catalog-sbIsGaOV.png) [DragonLib](technical.libraries.md) | Provides cross-loader abstractions and shared systems for MisterJulsen's mods. | <EmiSearch query="@dragonlib" /> |
| ![EMF Compat: Core](images/catalog-hbGct5uU.png) [EMF Compat: Core](technical.libraries.md) | Shared framework for EMF compatibility modules. | No separate item search |
| ![Forgified Fabric API](images/catalog-Aqlf1Shp.png) [Forgified Fabric API](technical.libraries.md) | Fabric interfaces implemented on NeoForge. | No separate item search |
| ![Fzzy Config](images/catalog-hYykXjDp.png) [Fzzy Config](technical.libraries.md) | Configuration, validation and synchronization support. | No separate item search |
| ![Geckolib](images/catalog-8BmcQJ2H.png) [Geckolib](technical.libraries.md) | Animation library for entities, blocks, items and armor. | No separate item search |
| ![GroovyModLoader (GML)](images/catalog-zg2tT2Vu.png) [GroovyModLoader (GML)](technical.libraries.md) | Groovy language provider. | No separate item search |
| ![Iceberg](images/catalog-5faXoLqX.png) [Iceberg](technical.libraries.md) | Provides extra events and utility functions for dependent mods. | No separate item search |
| ![JamLib](images/catalog-IYY9Siz8.png) [JamLib](technical.libraries.md) | Provides platform abstractions and configuration support for JamCore mods. | No separate item search |
| ![Kotlin for Forge](images/catalog-ordsPcFz.png) [Kotlin for Forge](technical.libraries.md) | Kotlin language provider and utilities. | No separate item search |
| ![Lionfish-API](images/catalog-FoVacERa.png) [Lionfish-API](technical.libraries.md) | Provides lightweight animation support for dependent mods. | No separate item search |
| ![Lithostitched](images/catalog-XaDC71GB.png) [Lithostitched](technical.libraries.md) | World-generation configuration and compatibility support. | No separate item search |
| ![Lodestone](images/catalog-bN3xUWdo.png) [Lodestone](technical.libraries.md) | Shared rendering and feature code for dependent mods. | No separate item search |
| ![MaFgLib](images/catalog-SKI34J7B.png) [MaFgLib](technical.libraries.md) | Shared code for Forge ports of masa's mods. | No separate item search |
| ![MidnightLib](images/catalog-codAaoxh.png) [MidnightLib](technical.libraries.md) | Lightweight configuration system. | No separate item search |
| ![Moonlight Lib](images/catalog-twkfQtEc.png) [Moonlight Lib](technical.libraries.md) | Shared registration and dynamic content utilities. | <EmiSearch query="@moonlight" /> |
| ![More RPG Library](images/catalog-Wkc3lwHo.png) [More RPG Library](technical.libraries.md) | Provides shared attributes and status effects for More RPG class addons. | <EmiSearch query="@more_rpg_classes" /> |
| ![MRU](images/catalog-SNVQ2c0g.png) [MRU](technical.libraries.md) | Shares cross-version utilities used by Cassian and IMB11's mods. | No separate item search |
| ![oωo (owo-lib)](images/catalog-ccKDOlHs.png) [oωo (owo-lib)](technical.libraries.md) | General utilities, interfaces and configuration support. | No separate item search |
| ![Placebo](images/catalog-tCkE8p2N.png) [Placebo](technical.libraries.md) | Provides shared code required by Shadows' mods without adding standalone gameplay. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [playerAnimator](technical.libraries.md) | Player animation library. | No separate item search |
| ![Prickle](images/catalog-aaRl8GiW.png) [Prickle](technical.libraries.md) | Provides structured configuration file handling for dependent mods. | No separate item search |
| ![Puzzles Lib](images/catalog-QAGBst4M.png) [Puzzles Lib](technical.libraries.md) | Provides shared support systems required by Fuzss' mods. | No separate item search |
| ![Ranged Weapon API](images/catalog-AqaIIO6D.png) [Ranged Weapon API](technical.libraries.md) | Bow and crossbow development support. | No separate item search |
| ![Resourceful Config](images/catalog-M1953qlQ.png) [Resourceful Config](technical.libraries.md) | Provides cross-platform configuration files and settings interfaces. | No separate item search |
| ![Resourceful Lib](images/catalog-G1hIVOrD.png) [Resourceful Lib](technical.libraries.md) | Provides shared networking, data encoding and interface utilities for dependent mods. | No separate item search |
| ![Ritchie's Projectile Library](images/catalog-B3pb093D.png) [Ritchie's Projectile Library](technical.libraries.md) | Supports long-range projectile synchronization and projectile chunk loading. | No separate item search |
| ![Sable](images/catalog-T9PomCSv.png) [Sable](technical.libraries.md) | Framework for interactive moving block structures. | No separate item search |
| ![Searchables](images/catalog-fuuu3xnx.png) [Searchables](technical.libraries.md) | Search, filtering and completion support for interfaces. | No separate item search |
| ![Shield API](images/catalog-y9clIFY4.png) [Shield API](technical.libraries.md) | Custom shield model support. | No separate item search |
| ![Sinytra Connector](images/catalog-u58R1TMW.png) [Sinytra Connector](technical.libraries.md) | Compatibility layer for selected Fabric mods on NeoForge. | No separate item search |
| ![Sophisticated Core](images/catalog-nmoqTijg.png) [Sophisticated Core](technical.libraries.md) | Provides shared systems used by Sophisticated inventory and storage mods. | <EmiSearch query="@sophisticatedcore" /> |
| ![Spell Engine](images/catalog-XvoWJaA2.png) [Spell Engine](technical.libraries.md) | Data-driven spell framework. | <EmiSearch query="@spell_engine" /> |
| ![Spell Power Attributes](images/catalog-8ooWzSQP.png) [Spell Power Attributes](technical.libraries.md) | Spell-related attributes, effects and enchantment support. | No separate item search |
| ![Structure Pool API](images/catalog-LrYZi08Q.png) [Structure Pool API](technical.libraries.md) | Structure pool injection support. | No separate item search |
| ![Teal Lib](images/catalog-rLJ1qF79.png) [Teal Lib](technical.libraries.md) | Provides shared animation and data-driven creature variant systems. | <EmiSearch query="@teallib" /> |
| ![YetAnotherConfigLib (YACL)](images/catalog-1eAoo2KR.png) [YetAnotherConfigLib (YACL)](technical.libraries.md) | Configuration screen construction library. | No separate item search |
| ![YUNG's API](images/catalog-Ua7DFN59.png) [YUNG's API](technical.libraries.md) | Shared code for YUNG's mods. | No separate item search |
