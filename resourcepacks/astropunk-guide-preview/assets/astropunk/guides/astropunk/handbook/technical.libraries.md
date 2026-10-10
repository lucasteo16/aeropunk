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
| ![Almanac](images/catalog-gi02250z.png) [Almanac](technical.libraries.md) | Shares loader-independent code and fixes item stacking issues caused by empty tags. | No separate item search |
| ![Apollib](images/catalog-vdi2ytax.png) [Apollib](technical.libraries.md) | Shared configuration and registry utilities. | No separate item search |
| ![Architectury API](images/catalog-lhga9tyq.png) [Architectury API](technical.libraries.md) | Shared cross-loader development interfaces. | No separate item search |
| ![Armor Model API](images/catalog-onz2nn2n.png) [Armor Model API](technical.libraries.md) | Renders custom armor geometry through the vanilla armor pipeline. | No separate item search |
| ![Athena](images/catalog-b1zv3dij.png) [Athena](technical.libraries.md) | Provides cross-loader connected block texture support. | No separate item search |
| ![BaguetteLib](images/catalog-ofkzpbru.png) [BaguetteLib](technical.libraries.md) | Death-handling and inventory-tracking support. | No separate item search |
| ![Balm](images/catalog-mbakmtvl.png) [Balm](technical.libraries.md) | Shares loader-independent systems so dependent mods can run on multiple loaders. | No separate item search |
| ![Bookshelf](images/catalog-uy4cnpcm.png) [Bookshelf](technical.libraries.md) | Provides shared serialization, data-pack features and debugging tools for dependent mods. | No separate item search |
| ![Bundle API](images/catalog-n8qn6z1a.png) [Bundle API](technical.libraries.md) | Provides larger bundles restricted to items selected by tags. | No separate item search |
| ![Cloth Config API](images/catalog-9s6osm5g.png) [Cloth Config API](technical.libraries.md) | Configuration screen library. | No separate item search |
| ![Collective](images/catalog-e0m1udsy.png) [Collective](technical.libraries.md) | Provides shared functionality for Serilum's utility mods. | No separate item search |
| ![Create: Dragons Plus](images/catalog-dzb1a5wv.png) [Create: Dragons Plus](technical.libraries.md) | Adds bulk fan processing and fluid tank access tools, plus shared Create addon utilities. | <EmiSearch query="@create_dragons_plus" /> |
| ![CreativeCore](images/catalog-osziadhq.png) [CreativeCore](technical.libraries.md) | Provides shared interface, configuration and network systems for CreativeMD's mods. | No separate item search |
| ![DragonLib](images/catalog-sbisgaov.png) [DragonLib](technical.libraries.md) | Provides cross-loader abstractions and shared systems for MisterJulsen's mods. | <EmiSearch query="@dragonlib" /> |
| ![EMF Compat: Core](images/catalog-hbgct5uu.png) [EMF Compat: Core](technical.libraries.md) | Shared framework for EMF compatibility modules. | No separate item search |
| ![Forgified Fabric API](images/catalog-aqlf1shp.png) [Forgified Fabric API](technical.libraries.md) | Fabric interfaces implemented on NeoForge. | No separate item search |
| ![Fzzy Config](images/catalog-hyykxjdp.png) [Fzzy Config](technical.libraries.md) | Configuration, validation and synchronization support. | No separate item search |
| ![Geckolib](images/catalog-8bmcqj2h.png) [Geckolib](technical.libraries.md) | Animation library for entities, blocks, items and armor. | No separate item search |
| ![GroovyModLoader (GML)](images/catalog-zg2tt2vu.png) [GroovyModLoader (GML)](technical.libraries.md) | Groovy language provider. | No separate item search |
| ![Iceberg](images/catalog-5faxolqx.png) [Iceberg](technical.libraries.md) | Provides extra events and utility functions for dependent mods. | No separate item search |
| ![JamLib](images/catalog-iyy9siz8.png) [JamLib](technical.libraries.md) | Provides platform abstractions and configuration support for JamCore mods. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [Konkrete](technical.libraries.md) | Provides the utility and configuration library required by FancyMenu. | No separate item search |
| ![Kotlin for Forge](images/catalog-ordspcfz.png) [Kotlin for Forge](technical.libraries.md) | Kotlin language provider and utilities. | No separate item search |
| ![Lionfish-API](images/catalog-fovacera.png) [Lionfish-API](technical.libraries.md) | Provides lightweight animation support for dependent mods. | No separate item search |
| ![Lithostitched](images/catalog-xadc71gb.png) [Lithostitched](technical.libraries.md) | World-generation configuration and compatibility support. | No separate item search |
| ![Lodestone](images/catalog-bn3xuwdo.png) [Lodestone](technical.libraries.md) | Shared rendering and feature code for dependent mods. | No separate item search |
| ![MaFgLib](images/catalog-ski34j7b.png) [MaFgLib](technical.libraries.md) | Shared code for Forge ports of masa's mods. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [Melody](technical.libraries.md) | Provides the audio library required by FancyMenu. This menu adds no custom music. | No separate item search |
| ![MidnightLib](images/catalog-codaaoxh.png) [MidnightLib](technical.libraries.md) | Lightweight configuration system. | No separate item search |
| ![Moonlight Lib](images/catalog-twkfqtec.png) [Moonlight Lib](technical.libraries.md) | Shared registration and dynamic content utilities. | <EmiSearch query="@moonlight" /> |
| ![More RPG Library](images/catalog-wkc3lwho.png) [More RPG Library](technical.libraries.md) | Provides shared attributes and status effects for More RPG class addons. | <EmiSearch query="@more_rpg_classes" /> |
| ![MRU](images/catalog-snvq2c0g.png) [MRU](technical.libraries.md) | Shares cross-version utilities used by Cassian and IMB11's mods. | No separate item search |
| ![oωo (owo-lib)](images/catalog-cckdolhs.png) [oωo (owo-lib)](technical.libraries.md) | General utilities, interfaces and configuration support. | No separate item search |
| ![Placebo](images/catalog-tcke8p2n.png) [Placebo](technical.libraries.md) | Provides shared code required by Shadows' mods without adding standalone gameplay. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [playerAnimator](technical.libraries.md) | Player animation library. | No separate item search |
| ![Prickle](images/catalog-aarl8giw.png) [Prickle](technical.libraries.md) | Provides structured configuration file handling for dependent mods. | No separate item search |
| ![Puzzles Lib](images/catalog-qagbst4m.png) [Puzzles Lib](technical.libraries.md) | Provides shared support systems required by Fuzss' mods. | No separate item search |
| ![Ranged Weapon API](images/catalog-aqaiio6d.png) [Ranged Weapon API](technical.libraries.md) | Bow and crossbow development support. | No separate item search |
| ![Resourceful Config](images/catalog-m1953qlq.png) [Resourceful Config](technical.libraries.md) | Provides cross-platform configuration files and settings interfaces. | No separate item search |
| ![Resourceful Lib](images/catalog-g1hivord.png) [Resourceful Lib](technical.libraries.md) | Provides shared networking, data encoding and interface utilities for dependent mods. | No separate item search |
| ![Ritchie's Projectile Library](images/catalog-b3pb093d.png) [Ritchie's Projectile Library](technical.libraries.md) | Supports long-range projectile synchronization and projectile chunk loading. | No separate item search |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | Framework for interactive moving block structures. | No separate item search |
| ![Searchables](images/catalog-fuuu3xnx.png) [Searchables](technical.libraries.md) | Search, filtering and completion support for interfaces. | No separate item search |
| ![Shield API](images/catalog-y9clify4.png) [Shield API](technical.libraries.md) | Custom shield model support. | No separate item search |
| ![Sinytra Connector](images/catalog-u58r1tmw.png) [Sinytra Connector](technical.libraries.md) | Compatibility layer for selected Fabric mods on NeoForge. | No separate item search |
| ![Sophisticated Core](images/catalog-nmoqtijg.png) [Sophisticated Core](technical.libraries.md) | Provides shared systems used by Sophisticated inventory and storage mods. | <EmiSearch query="@sophisticatedcore" /> |
| ![Spell Engine](images/catalog-xvowjaa2.png) [Spell Engine](technical.libraries.md) | Data-driven spell framework. | <EmiSearch query="@spell_engine" /> |
| ![Spell Power Attributes](images/catalog-8oowzsqp.png) [Spell Power Attributes](technical.libraries.md) | Spell-related attributes, effects and enchantment support. | No separate item search |
| ![Structure Pool API](images/catalog-lryzi08q.png) [Structure Pool API](technical.libraries.md) | Structure pool injection support. | No separate item search |
| ![Teal Lib](images/catalog-rlj1qf79.png) [Teal Lib](technical.libraries.md) | Provides shared animation and data-driven creature variant systems. | <EmiSearch query="@teallib" /> |
| ![YetAnotherConfigLib (YACL)](images/catalog-1eaoo2kr.png) [YetAnotherConfigLib (YACL)](technical.libraries.md) | Configuration screen construction library. | No separate item search |
| ![YUNG's API](images/catalog-ua7dfn59.png) [YUNG's API](technical.libraries.md) | Shared code for YUNG's mods. | No separate item search |
