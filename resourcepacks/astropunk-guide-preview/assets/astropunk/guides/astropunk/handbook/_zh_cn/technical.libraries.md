---
navigation:
  title: "查询支持库与框架"
  position: 0
  parent: reference.technical.md
  icon: minecraft:bookshelf
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

<EmiSearch query="@more_rpg_classes" /> <EmiSearch query="@spell_engine" />

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

<EmiSearch query="@dragonlib" /> <EmiSearch query="@moonlight" /> <EmiSearch query="@sophisticatedcore" /> <EmiSearch query="@teallib" />

以下列出其他支持库。依赖库应与使用它们的模组一起保留。库的名称并不代表增加了新方块、配方或遭遇。

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

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Almanac](images/catalog-gi02250z.png) [Almanac](technical.libraries.md) | 共享跨加载器代码，并修复空标签导致的物品无法堆叠问题。 | 无独立物品查询 |
| ![Apollib](images/catalog-vdi2ytax.png) [Apollib](technical.libraries.md) | 共享设置与注册工具。 | 无独立物品查询 |
| ![Architectury API](images/catalog-lhga9tyq.png) [Architectury API](technical.libraries.md) | 共享跨加载器开发接口。 | 无独立物品查询 |
| ![Armor Model API](images/catalog-onz2nn2n.png) [Armor Model API](technical.libraries.md) | 通过原版盔甲流程渲染自定义盔甲几何模型。 | 无独立物品查询 |
| ![Athena](images/catalog-b1zv3dij.png) [Athena](technical.libraries.md) | 提供跨加载器的方块连接纹理支持。 | 无独立物品查询 |
| ![BaguetteLib](images/catalog-ofkzpbru.png) [BaguetteLib](technical.libraries.md) | 死亡处理与物品栏追踪支持。 | 无独立物品查询 |
| ![Balm](images/catalog-mbakmtvl.png) [Balm](technical.libraries.md) | 共享独立于加载器的系统，让依赖模组可用于多种加载器。 | 无独立物品查询 |
| ![Bookshelf](images/catalog-uy4cnpcm.png) [Bookshelf](technical.libraries.md) | 为依赖模组提供共享数据序列化、数据包功能与调试工具。 | 无独立物品查询 |
| ![Bundle API](images/catalog-n8qn6z1a.png) [Bundle API](technical.libraries.md) | 提供更大容量的收纳袋，并用标签限定可收纳物品。 | 无独立物品查询 |
| ![Cloth Config API](images/catalog-9s6osm5g.png) [Cloth Config API](technical.libraries.md) | 设置界面库。 | 无独立物品查询 |
| ![Collective](images/catalog-e0m1udsy.png) [Collective](technical.libraries.md) | 为 Serilum 实用模组提供共享功能。 | 无独立物品查询 |
| ![Create: Dragons Plus](images/catalog-dzb1a5wv.png) [Create: Dragons Plus](technical.libraries.md) | 增加风扇批量加工与储液罐存取工具，并提供机械动力附加模组共享工具。 | <EmiSearch query="@create_dragons_plus" /> |
| ![CreativeCore](images/catalog-osziadhq.png) [CreativeCore](technical.libraries.md) | 为 CreativeMD 模组提供共享界面、设置与网络系统。 | 无独立物品查询 |
| ![DragonLib](images/catalog-sbisgaov.png) [DragonLib](technical.libraries.md) | 为 MisterJulsen 模组提供跨加载器抽象层与共享系统。 | <EmiSearch query="@dragonlib" /> |
| ![EMF Compat: Core](images/catalog-hbgct5uu.png) [EMF Compat: Core](technical.libraries.md) | EMF 兼容组件共享框架。 | 无独立物品查询 |
| ![Forgified Fabric API](images/catalog-aqlf1shp.png) [Forgified Fabric API](technical.libraries.md) | 在 NeoForge 上实现的 Fabric 接口。 | 无独立物品查询 |
| ![Fzzy Config](images/catalog-hyykxjdp.png) [Fzzy Config](technical.libraries.md) | 设置、校验与同步支持。 | 无独立物品查询 |
| ![Geckolib](images/catalog-8bmcqj2h.png) [Geckolib](technical.libraries.md) | 实体、方块、物品与盔甲动画库。 | 无独立物品查询 |
| ![GroovyModLoader (GML)](images/catalog-zg2tt2vu.png) [GroovyModLoader (GML)](technical.libraries.md) | Groovy 语言支持。 | 无独立物品查询 |
| ![Iceberg](images/catalog-5faxolqx.png) [Iceberg](technical.libraries.md) | 为依赖模组提供额外事件与工具函数。 | 无独立物品查询 |
| ![JamLib](images/catalog-iyy9siz8.png) [JamLib](technical.libraries.md) | 为 JamCore 模组提供平台抽象层与设置支持。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [Konkrete](technical.libraries.md) | 提供 FancyMenu 所需的工具与配置支持库。 | 无独立物品查询 |
| ![Kotlin for Forge](images/catalog-ordspcfz.png) [Kotlin for Forge](technical.libraries.md) | Kotlin 语言支持与工具。 | 无独立物品查询 |
| ![Lionfish-API](images/catalog-fovacera.png) [Lionfish-API](technical.libraries.md) | 为依赖模组提供轻量动画支持。 | 无独立物品查询 |
| ![Lithostitched](images/catalog-xadc71gb.png) [Lithostitched](technical.libraries.md) | 世界生成设置与兼容支持。 | 无独立物品查询 |
| ![Lodestone](images/catalog-bn3xuwdo.png) [Lodestone](technical.libraries.md) | 依赖模组使用的共享渲染与功能代码。 | 无独立物品查询 |
| ![MaFgLib](images/catalog-ski34j7b.png) [MaFgLib](technical.libraries.md) | masa 模组 Forge 移植版使用的共享代码。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [Melody](technical.libraries.md) | 提供 FancyMenu 所需的音频支持库。本菜单没有添加自定义音乐。 | 无独立物品查询 |
| ![MidnightLib](images/catalog-codaaoxh.png) [MidnightLib](technical.libraries.md) | 轻量设置系统。 | 无独立物品查询 |
| ![Moonlight Lib](images/catalog-twkfqtec.png) [Moonlight Lib](technical.libraries.md) | 共享注册与动态内容工具。 | <EmiSearch query="@moonlight" /> |
| ![More RPG Library](images/catalog-wkc3lwho.png) [More RPG Library](technical.libraries.md) | 为 More RPG 职业附加模组提供共享属性与状态效果。 | <EmiSearch query="@more_rpg_classes" /> |
| ![MRU](images/catalog-snvq2c0g.png) [MRU](technical.libraries.md) | 共享 Cassian 与 IMB11 模组使用的跨版本工具。 | 无独立物品查询 |
| ![oωo (owo-lib)](images/catalog-cckdolhs.png) [oωo (owo-lib)](technical.libraries.md) | 通用工具、界面与设置支持。 | 无独立物品查询 |
| ![Placebo](images/catalog-tcke8p2n.png) [Placebo](technical.libraries.md) | 提供 Shadows 模组所需的共享代码，不增加独立玩法。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [playerAnimator](technical.libraries.md) | 玩家动画库。 | 无独立物品查询 |
| ![Prickle](images/catalog-aarl8giw.png) [Prickle](technical.libraries.md) | 为依赖模组提供结构化设置文件处理。 | 无独立物品查询 |
| ![Puzzles Lib](images/catalog-qagbst4m.png) [Puzzles Lib](technical.libraries.md) | 提供 Fuzss 模组所需的共享支持系统。 | 无独立物品查询 |
| ![Ranged Weapon API](images/catalog-aqaiio6d.png) [Ranged Weapon API](technical.libraries.md) | 弓与弩开发支持。 | 无独立物品查询 |
| ![Resourceful Config](images/catalog-m1953qlq.png) [Resourceful Config](technical.libraries.md) | 提供跨平台设置文件与设置界面。 | 无独立物品查询 |
| ![Resourceful Lib](images/catalog-g1hivord.png) [Resourceful Lib](technical.libraries.md) | 为依赖模组提供共享网络通信、数据编码与界面工具。 | 无独立物品查询 |
| ![Ritchie's Projectile Library](images/catalog-b3pb093d.png) [Ritchie's Projectile Library](technical.libraries.md) | 提供远程弹射物同步与弹射物区块加载支持。 | 无独立物品查询 |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | 可交互移动方块结构框架。 | 无独立物品查询 |
| ![Searchables](images/catalog-fuuu3xnx.png) [Searchables](technical.libraries.md) | 界面搜索、筛选与补全支持。 | 无独立物品查询 |
| ![Shield API](images/catalog-y9clify4.png) [Shield API](technical.libraries.md) | 自定义盾牌模型支持。 | 无独立物品查询 |
| ![Sinytra Connector](images/catalog-u58r1tmw.png) [Sinytra Connector](technical.libraries.md) | 让部分选定的 Fabric 模组在 NeoForge 上运行的兼容层。 | 无独立物品查询 |
| ![Sophisticated Core](images/catalog-nmoqtijg.png) [Sophisticated Core](technical.libraries.md) | 为 Sophisticated 物品栏与存储模组提供共享系统。 | <EmiSearch query="@sophisticatedcore" /> |
| ![Spell Engine](images/catalog-xvowjaa2.png) [Spell Engine](technical.libraries.md) | 数据驱动法术框架。 | <EmiSearch query="@spell_engine" /> |
| ![Spell Power Attributes](images/catalog-8oowzsqp.png) [Spell Power Attributes](technical.libraries.md) | 法术相关属性、效果与附魔支持。 | 无独立物品查询 |
| ![Structure Pool API](images/catalog-lryzi08q.png) [Structure Pool API](technical.libraries.md) | 结构池扩展支持。 | 无独立物品查询 |
| ![Teal Lib](images/catalog-rlj1qf79.png) [Teal Lib](technical.libraries.md) | 提供共享动画与数据驱动的生物变体系统。 | <EmiSearch query="@teallib" /> |
| ![YetAnotherConfigLib (YACL)](images/catalog-1eaoo2kr.png) [YetAnotherConfigLib (YACL)](technical.libraries.md) | 设置界面构建库。 | 无独立物品查询 |
| ![YUNG's API](images/catalog-ua7dfn59.png) [YUNG's API](technical.libraries.md) | YUNG 模组共享代码。 | 无独立物品查询 |
