---
navigation:
  title: "查询支持库与框架"
  position: 0
  parent: reference.technical.md
  icon: minecraft:redstone
---

# 查询支持库与框架

## 加载器与语言

这些组件提供共享接口或语言支持。Connector 让选定的 Fabric 模组在 NeoForge 上运行，不代表支持所有 Fabric 版本。

| 内容 | 作用 |
| --- | --- |
| Sinytra Connector | 让部分选定的 Fabric 模组在 NeoForge 上运行的兼容层。 |
| Forgified Fabric API | 在 NeoForge 上实现的 Fabric 接口。 |
| Architectury API | 共享跨加载器开发接口。 |
| Balm | 跨加载器抽象库。 |
| GroovyModLoader (GML) | Groovy 语言支持。 |
| Kotlin for Forge | Kotlin 语言支持与工具。 |

***

## 设置框架

这些库为其他模组提供设置、校验或设置界面构建，并不是独立玩法。

| 内容 | 作用 |
| --- | --- |
| Cloth Config API | 设置界面库。 |
| Fzzy Config | 设置、校验与同步支持。 |
| MidnightLib | 轻量设置系统。 |
| Prickle | 设置文件支持。 |
| Resourceful Config | 跨平台设置支持。 |
| YetAnotherConfigLib (YACL) | 设置界面构建库。 |
| Apollib | 共享设置与注册工具。 |

***

## 模型与动画

这些框架支持其他内容使用的动画、盔甲模型与连接纹理。单独的框架不会增加完整动态资源包。

| 内容 | 作用 |
| --- | --- |
| Armor Model API | 通过原版盔甲流程渲染自定义盔甲几何模型。 |
| Geckolib | 实体、方块、物品与盔甲动画库。 |
| Lionfish-API | 动画框架。 |
| playerAnimator | 玩家动画库。 |
| EMF Compat: Core | EMF 兼容组件共享框架。 |
| Athena | 连接纹理框架。 |

***

## 世界与结构

这些组件支持世界生成或移动结构。目的地与载具部件见玩法页面。

| 内容 | 作用 |
| --- | --- |
| Lithostitched | 世界生成设置与兼容支持。 |
| Structure Pool API | 结构池扩展支持。 |
| YUNG's API | YUNG 模组共享代码。 |
| Sable | 可交互移动方块结构框架。 |

***

## 战斗框架

这些组件提供共享法术、属性、武器与弹射物系统。职业装备与法术选择另有页面。

| 内容 | 作用 |
| --- | --- |
| More RPG Library | More RPG 系列共享框架。 |
| Spell Engine | 数据驱动法术框架。 |
| Spell Power Attributes | 法术相关属性、效果与附魔支持。 |
| Ranged Weapon API | 弓与弩开发支持。 |
| Shield API | 自定义盾牌模型支持。 |
| Ritchie's Projectile Library | 弹射物开发支持。 |

***

## 共享代码

以下列出其他已安装支持库。依赖库应与使用它们的模组一起保留。库的名称并不代表增加了新方块、配方或遭遇。

| 内容 | 作用 |
| --- | --- |
| Almanac | 共享跨加载器代码。 |
| BaguetteLib | 死亡处理与物品栏追踪支持。 |
| Bookshelf | 共享代码库。 |
| Bundle API | 基于物品标签的收纳袋支持。 |
| Collective | Serilum 模组的共享代码。 |
| CreativeCore | 共享核心工具。 |
| DragonLib | 依赖模组使用的共享代码。 |
| Iceberg | 共享事件与工具。 |
| JamLib | 跨平台共享代码。 |
| Lodestone | 依赖模组使用的共享渲染与功能代码。 |
| MaFgLib | masa 模组 Forge 移植版使用的共享代码。 |
| Moonlight Lib | 共享注册与动态内容工具。 |
| MRU | 依赖模组使用的共享框架。 |
| oωo (owo-lib) | 通用工具、界面与设置支持。 |
| Placebo | 共享基础，不是独立玩法内容。 |
| Puzzles Lib | Fuzss 模组使用的共享系统。 |
| Resourceful Lib | 共享代码库。 |
| Searchables | 界面搜索、筛选与补全支持。 |
| Sophisticated Core | Sophisticated 模组共享代码。 |
| Teal Lib | 共享代码库。 |

***

## 相关页面

- [法术](combat.magic.md)
- [载具组装](vehicles.assembly.md)
- [资源包](visuals.resource-packs.md)


***

## 相关模组

| 模组或内容 | 状态 | 英文官方简介 |
| --- | --- | --- |
| ![Almanac](images/catalog-Gi02250Z.png) [Almanac](technical.libraries.md) | 已安装基准版 | Almanac is a library used by my mods with mostly loader independent shared code between multiple mods to avoid duplication of code. |
| ![Apollib](images/catalog-VDI2Ytax.png) [Apollib](technical.libraries.md) | 已安装基准版 | A tiny library for my configuration and registry utilities. |
| ![Architectury API](images/catalog-lhGA9TYQ.png) [Architectury API](technical.libraries.md) | 已安装基准版 | An intermediary api aimed to ease developing multiplatform mods. |
| ![Armor Model API](images/catalog-onz2NN2n.png) [Armor Model API](technical.libraries.md) | 已安装基准版 | Renders Bedrock/GeckoLib geo armor models through the vanilla armor pipeline. |
| ![Athena](images/catalog-b1ZV3DIJ.png) [Athena](technical.libraries.md) | 已安装基准版 | A crossplatform (Forge/Fabric) solution to connected block textures for 1.19.4+ |
| ![BaguetteLib](images/catalog-OfKzpbRU.png) [BaguetteLib](technical.libraries.md) | 已安装基准版 | Ever tried to make a mod that needs proper death handling or inventory tracking? Yeah, NeoForge events suck for that. |
| ![Balm](images/catalog-MBAkmtvl.png) [Balm](technical.libraries.md) | 已安装基准版 | Abstraction Layer for Multi-Loader Mods |
| ![Bookshelf](images/catalog-uy4Cnpcm.png) [Bookshelf](technical.libraries.md) | 已安装基准版 | An open source library for other mods! |
| ![Bundle API](images/catalog-n8QN6Z1a.png) [Bundle API](technical.libraries.md) | 已安装基准版 | Bundle API allows mod authors to easily add bundles that can hold more than 1 stack of items specified by an item tag. |
| ![Cloth Config API](images/catalog-9s6osm5g.png) [Cloth Config API](technical.libraries.md) | 已安装基准版 | Configuration Library for Minecraft Mods |
| ![Collective](images/catalog-e0M1UDsY.png) [Collective](technical.libraries.md) | 已安装基准版 | 🎓 Collective is a shared library with common code for all of Serilum's mods. |
| ![Create: Dragons Plus](images/catalog-dzb1a5WV.png) [Create: Dragons Plus](technical.libraries.md) | 已安装基准版 | Provide convenient features to players and dev utilities for Create addon developers. |
| ![CreativeCore](images/catalog-OsZiaDHq.png) [CreativeCore](technical.libraries.md) | 已安装基准版 | A core mod |
| ![DragonLib](images/catalog-sbIsGaOV.png) [DragonLib](technical.libraries.md) | 已安装基准版 | DragonLib is a small and simple library mod which contains code that is used by most of my mods. |
| ![EMF Compat: Core](images/catalog-hbGct5uU.png) [EMF Compat: Core](technical.libraries.md) | 已安装基准版 | Shared framework for the EMF Compat family. |
| ![Forgified Fabric API](images/catalog-Aqlf1Shp.png) [Forgified Fabric API](technical.libraries.md) | 已安装基准版 | Fabric API implemented on top of NeoForge |
| ![Fzzy Config](images/catalog-hYykXjDp.png) [Fzzy Config](technical.libraries.md) | 已安装基准版 | Config API with automatic GUIs, powerful validation options, server-client sync, and more! |
| ![Geckolib](images/catalog-8BmcQJ2H.png) [Geckolib](technical.libraries.md) | 已安装基准版 | A 3D animation library for entities, blocks, items, armor, and more! |
| ![GroovyModLoader (GML)](images/catalog-zg2tT2Vu.png) [GroovyModLoader (GML)](technical.libraries.md) | 已安装基准版 | NeoForge language provider for Groovy mods. |
| ![Iceberg](images/catalog-5faXoLqX.png) [Iceberg](technical.libraries.md) | 已安装基准版 | A modding library that contains new events, helpers, and utilities to make modder's lives easier. |
| ![JamLib](images/catalog-IYY9Siz8.png) [JamLib](technical.libraries.md) | 已安装基准版 | The platform-agnostic, Architectury based library used in all of JamCoreModding's mods |
| ![Kotlin for Forge](images/catalog-ordsPcFz.png) [Kotlin for Forge](technical.libraries.md) | 已安装基准版 | Adds a Kotlin language loader and provides some optional utilities. |
| ![Lionfish-API](images/catalog-FoVacERa.png) [Lionfish-API](technical.libraries.md) | 已安装基准版 | Very Light Animation Api |
| ![Lithostitched](images/catalog-XaDC71GB.png) [Lithostitched](technical.libraries.md) | 已安装基准版 | Library mod with new configurability and compatibility enhancements for worldgen |
| ![Lodestone](images/catalog-bN3xUWdo.png) [Lodestone](technical.libraries.md) | 已安装基准版 | A collection of code used throughout projects under the Lodestar team. |
| ![MaFgLib](images/catalog-SKI34J7B.png) [MaFgLib](technical.libraries.md) | 已安装基准版 | MaLiLib unofficial forge port. Library mod for the (Neo)Forge port of masa's mods. |
| ![MidnightLib](images/catalog-codAaoxh.png) [MidnightLib](technical.libraries.md) | 已安装基准版 | Common library providing a lightweight configuration system |
| ![Moonlight Lib](images/catalog-twkfQtEc.png) [Moonlight Lib](technical.libraries.md) | 已安装基准版 | dynamic data pack and registration, villager activities, custom map marker and a lot more |
| ![More RPG Library](images/catalog-Wkc3lwHo.png) [More RPG Library](technical.libraries.md) | 已安装基准版 | Library for the More RPG Classes & More RPG Content Series. |
| ![MRU](images/catalog-SNVQ2c0g.png) [MRU](technical.libraries.md) | 已安装基准版 | A library mod used by Cassian and IMB11's mods to function. |
| ![oωo (owo-lib)](images/catalog-ccKDOlHs.png) [oωo (owo-lib)](technical.libraries.md) | 已安装基准版 | A general utility, GUI and config library for modding on Fabric and Quilt |
| ![Placebo](images/catalog-tCkE8p2N.png) [Placebo](technical.libraries.md) | 已安装基准版 | Placebo is a library used by most of my mods. It does not provide any game-relevant features on its own (save for maybe a couple debug commands). |
| <ItemImage id="minecraft:redstone" /> [playerAnimator](technical.libraries.md) | 已安装基准版 | animate the player |
| ![Prickle](images/catalog-aaRl8GiW.png) [Prickle](technical.libraries.md) | 已安装基准版 | Prickle is a JSON based configuration file format brought to Minecraft. |
| ![Puzzles Lib](images/catalog-QAGBst4M.png) [Puzzles Lib](technical.libraries.md) | 已安装基准版 | Why is it called Puzzles? That's the puzzle. |
| ![Ranged Weapon API](images/catalog-AqaIIO6D.png) [Ranged Weapon API](technical.libraries.md) | 已安装基准版 | 🏹 Create fully functional bows and crossbows, with ease |
| ![Resourceful Config](images/catalog-M1953qlQ.png) [Resourceful Config](technical.libraries.md) | 已安装基准版 | Resourceful Config is a mod that allows for developers to make cross-platform configs |
| ![Resourceful Lib](images/catalog-G1hIVOrD.png) [Resourceful Lib](technical.libraries.md) | 已安装基准版 | Resourceful Lib |
| ![Ritchie's Projectile Library](images/catalog-B3pb093D.png) [Ritchie's Projectile Library](technical.libraries.md) | 已安装基准版 | A Minecraft modding library for better projectiles. |
| ![Sable](images/catalog-T9PomCSv.png) [Sable](technical.libraries.md) | 已安装基准版 | A library mod for interactive moving block structures, or "sub-levels" |
| ![Searchables](images/catalog-fuuu3xnx.png) [Searchables](technical.libraries.md) | 已安装基准版 | Searchables is a library mod that adds helper methods that allow for searching and filtering elements based on components, as well as offering built in auto-complete functionality. |
| ![Shield API](images/catalog-y9clIFY4.png) [Shield API](technical.libraries.md) | 已安装基准版 | Creating shields with custom models was never easier! |
| ![Sinytra Connector](images/catalog-u58R1TMW.png) [Sinytra Connector](technical.libraries.md) | 已安装基准版 | Lets you play Fabric mods on NeoForge |
| ![Sophisticated Core](images/catalog-nmoqTijg.png) [Sophisticated Core](technical.libraries.md) | 已安装基准版 | Library mod for Sophisticated mods |
| ![Spell Engine](images/catalog-XvoWJaA2.png) [Spell Engine](technical.libraries.md) | 已安装基准版 | 🪄 Data driven magic library |
| ![Spell Power Attributes](images/catalog-8ooWzSQP.png) [Spell Power Attributes](technical.libraries.md) | 已安装基准版 | 🔮 Spell Power entity attributes with related status effects and enchantments |
| ![Structure Pool API](images/catalog-LrYZi08Q.png) [Structure Pool API](technical.libraries.md) | 已安装基准版 | 📚 API to inject structures into structure pools. |
| ![Teal Lib](images/catalog-rLJ1qF79.png) [Teal Lib](technical.libraries.md) | 已安装基准版 | A library mod that's teal... That's the appeal |
| ![YetAnotherConfigLib (YACL)](images/catalog-1eAoo2KR.png) [YetAnotherConfigLib (YACL)](technical.libraries.md) | 已安装基准版 | A builder-based configuration library for Minecraft! |
| ![YUNG's API](images/catalog-Ua7DFN59.png) [YUNG's API](technical.libraries.md) | 已安装基准版 | Library mod for YUNG's mods. |
