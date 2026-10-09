---
navigation:
  title: "了解管理员与诊断工具"
  position: 0
  parent: reference.technical.md
  icon: minecraft:redstone
---

# 了解管理员与诊断工具

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

| 模组或内容 | 状态 | 英文官方简介 |
| --- | --- | --- |
| ![Chunky](images/catalog-fALzjamp.png) [Chunky](server.tools.md) | 已安装基准版 | Pre-generates chunks, quickly and efficiently |
| ![Configured Defaults](images/catalog-SISoSFPP.png) [Configured Defaults](server.tools.md) | 已安装基准版 | Allows for providing defaults for files absent in .minecraft like configs. A quintessential modpack utility. |
| ![Observable](images/catalog-VYRu7qmG.png) [Observable](server.tools.md) | 已安装基准版 | See what's lagging your server. |
| ![spark](images/catalog-l6YH9Als.png) [spark](server.tools.md) | 已安装基准版 | spark is a performance profiler for Minecraft clients, servers and proxies. |
