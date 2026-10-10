---
navigation:
  title: "了解暂缓加入的优化模组"
  position: 0
  parent: reference.technical.md
  icon: minecraft:repeater
---

# 了解暂缓加入的优化模组

## 独立试验

实验性优化模组会先在独立分支测试。Async Logger、Jasione 和 ServerCore 现已纳入共用模组包。

- [共用优化模组](performance.baseline.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:redstone" /> [Async Logger](performance.deferred.md) | 异步日志处理。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [Jasione](performance.deferred.md) | 减少重复的枚举数组分配。 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [ServerCore](performance.deferred.md) | 优化服务器区块刻处理与生物生成，并提供可调整的负载控制。 | 无独立物品查询 |
