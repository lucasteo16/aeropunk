---
navigation:
  title: "了解管理员与诊断工具"
  position: 3
  parent: reference.technical.md
  icon: minecraft:command_block
---

# 了解管理员与诊断工具

## 维度边界

DimWorldBorder 让各维度拥有独立的边界大小与中心，单人游戏的内置服务器也适用。多人游戏中，玩家遵循服务器边界，客户端无需安装此模组。

管理员应先查询边界，再修改设置。

| 命令 | 用途 |
| --- | --- |
| <Color color="#F28CBD">/dimworldborder minecraft:overworld get</Color> | 查询主世界边界 |
| <Color color="#F28CBD">/dimworldborder minecraft:the_nether get</Color> | 查询下界边界 |
| <Color color="#F28CBD">/dimworldborder rocketnautics:moon get</Color> | 查询月球边界 |
| <Color color="#F28CBD">/dimworldborder minecraft:overworld set 5000</Color> | 将主世界方形边界的完整宽度设为 5000 格 |

使用命令补全选择维度。整合包的安全数据包也会在加载时设置主世界范围限制。自定义大小后，应在重启或重载数据包后查询边界值。玩家边界不保证能容纳或阻挡整艘移动船体。

***

## 地形准备

Chunky 在玩家探索前生成地形。这是管理员任务，不是渲染距离设置。大型生成任务会占用处理时间与磁盘空间。

| 内容 | 作用 |
| --- | --- |
| Chunky | 在探索前预先生成地形。 |

***

## 诊断工具

Observable 与 spark 用于定位处理开销。客户端渲染与服务器模拟是不同工作负载。服务器记录不能衡量光影渲染开销，使用权限可能由服务器决定。

| 内容 | 作用 |
| --- | --- |
| Observable | 用于定位服务器耗时处理。 |
| spark | 分析客户端与服务器性能。 |

***

## 整合包默认设置

Configured Defaults 在文件缺失时提供初始文件。已有玩家设置与整合包默认值并不相同。它是整合包维护工具，不是性能分析器。

| 内容 | 作用 |
| --- | --- |
| Configured Defaults | 为缺失文件提供整合包默认设置。 |

***

## 相关页面

- [性能优化](performance.baseline.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Chunky](images/catalog-falzjamp.png) [Chunky](server.tools.md) | 在探索前预先生成地形。 | 无独立物品查询 |
| ![Configured Defaults](images/catalog-sisosfpp.png) [Configured Defaults](server.tools.md) | 为缺失文件提供整合包默认设置。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [DimWorldBorder](server.tools.md) | 为各个维度管理独立的实体边界。 | 无独立物品查询 |
| ![Observable](images/catalog-vyru7qmg.png) [Observable](server.tools.md) | 用于定位服务器耗时处理。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [Paxi](server.tools.md) | 加载共享数据包，包括自动设置太空世界边界的数据包。 | 无独立物品查询 |
| ![spark](images/catalog-l6yh9als.png) [spark](server.tools.md) | 分析客户端与服务器性能。 | 无独立物品查询 |
