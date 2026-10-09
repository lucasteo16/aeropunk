---
navigation:
  title: "了解当前性能优化系统"
  position: 0
  parent: reference.technical.md
  icon: minecraft:redstone
---

# 了解当前性能优化系统

## 渲染

这些组件减少客户端不同部分的渲染工作，并不是额外视觉效果。

| 内容 | 作用 |
| --- | --- |
| Sodium | 替换地形渲染引擎。 |
| ImmediatelyFast | 优化即时模式渲染。 |
| Entity Culling | 避免渲染被遮挡的实体与方块实体。 |
| More Culling | 跳过部分不可见的渲染面。 |
| Cull Leaves | 跳过部分不可见的树叶几何面。 |
| Flerovium | 优化物品、粒子与实体渲染。 |
| AsyncParticles | 优化粒子运算与渲染。 |
| Kerria | 加速动态纹理处理。 |
| CreateBetterFps | 优化使用光影时的机械动力渲染。 |

***

## 模拟与地形

<EmiSearch query="@create" /> <EmiSearch query="@createlazytick" />

这些组件针对游戏逻辑、生物处理、机械动力机器或地形准备。

| 内容 | 作用 |
| --- | --- |
| Lithium | 优化单人游戏与服务器的游戏逻辑。 |
| AI Improvements: Performance Tuning | 优化原版生物行为处理。 |
| Clumps | 合并经验球，减少独立经验球的处理。 |
| Let Me Despawn | 调整生物消失规则，减少意外永久保留的生物。 |
| Create: LazyTick | 优化机械动力机器的刻处理。 |
| Concurrent Chunk Management Engine (NeoForge) | 优化区块管理与生成。 |
| Structure Layout Optimizer | 优化拼图结构布局处理。 |

***

## 内存与加载

内存、加载与通用修复处理的开销不同于地形渲染。

| 内容 | 作用 |
| --- | --- |
| FerriteCore | 减少内存占用。 |
| ModernFix | 提供性能、内存与错误修复改进。 |
| quick pack | 加速压缩数据包与资源包加载。 |
| BadOptimizations | 优化主地形渲染器以外的处理。 |

***

## 输入与空闲

输入处理与后台资源使用不同于活动世界模拟。已安装不代表已经测得你的电脑能提升多少帧率。

| 内容 | 作用 |
| --- | --- |
| Ixeris | 提供缓冲原始输入与独立线程事件轮询。 |
| Dynamic FPS | 降低后台或空闲时的资源使用。 |

***

## 相关页面

- [诊断工具](server.tools.md)
- [光照与远景](visuals.lighting.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![AI Improvements: Performance Tuning](images/catalog-DSVgwcji.png) [AI Improvements: Performance Tuning](performance.baseline.md) | 优化原版生物行为处理。 | 已安装基准版 | 无独立物品查询 |
| ![AsyncParticles](images/catalog-c3onkd5k.png) [AsyncParticles](performance.baseline.md) | 优化粒子运算与渲染。 | 已安装基准版 | 无独立物品查询 |
| <ItemImage id="minecraft:redstone" /> [BadOptimizations](performance.baseline.md) | 优化主地形渲染器以外的处理。 | 已安装基准版 | 无独立物品查询 |
| ![Clumps](images/catalog-Wnxd13zP.png) [Clumps](performance.baseline.md) | 合并经验球，减少独立经验球的处理。 | 已安装基准版 | 无独立物品查询 |
| ![Concurrent Chunk Management Engine (NeoForge)](images/catalog-COlSi5iR.png) [Concurrent Chunk Management Engine (NeoForge)](performance.baseline.md) | 优化区块管理与生成。 | 已安装基准版 | 无独立物品查询 |
| ![Create: LazyTick](images/catalog-Z0d7hFh4.png) [Create: LazyTick](performance.baseline.md) | 优化机械动力机器的刻处理。 | 已安装基准版 | <EmiSearch query="@createlazytick" /> |
| ![CreateBetterFps](images/catalog-lMYIHZNH.png) [CreateBetterFps](performance.baseline.md) | 优化使用光影时的机械动力渲染。 | 已安装基准版 | 无独立物品查询 |
| ![Cull Leaves](images/catalog-GNxdLCoP.png) [Cull Leaves](performance.baseline.md) | 跳过部分不可见的树叶几何面。 | 已安装基准版 | 无独立物品查询 |
| ![Dynamic FPS](images/catalog-LQ3K71Q1.png) [Dynamic FPS](performance.baseline.md) | 降低后台或空闲时的资源使用。 | 已安装基准版 | 无独立物品查询 |
| ![Entity Culling](images/catalog-NNAgCjsB.png) [Entity Culling](performance.baseline.md) | 避免渲染被遮挡的实体与方块实体。 | 已安装基准版 | 无独立物品查询 |
| ![FerriteCore](images/catalog-uXXizFIs.png) [FerriteCore](performance.baseline.md) | 减少内存占用。 | 已安装基准版 | 无独立物品查询 |
| ![Flerovium](images/catalog-4Rh1Mobu.png) [Flerovium](performance.baseline.md) | 优化物品、粒子与实体渲染。 | 已安装基准版 | 无独立物品查询 |
| ![ImmediatelyFast](images/catalog-5ZwdcRci.png) [ImmediatelyFast](performance.baseline.md) | 优化即时模式渲染。 | 已安装基准版 | 无独立物品查询 |
| ![Ixeris](images/catalog-p8RJPJIC.png) [Ixeris](performance.baseline.md) | 提供缓冲原始输入与独立线程事件轮询。 | 已安装基准版 | 无独立物品查询 |
| ![Kerria](images/catalog-f0ruQTF7.png) [Kerria](performance.baseline.md) | 加速动态纹理处理。 | 已安装基准版 | 无独立物品查询 |
| ![Let Me Despawn](images/catalog-vE2FN5qn.png) [Let Me Despawn](performance.baseline.md) | 调整生物消失规则，减少意外永久保留的生物。 | 已安装基准版 | 无独立物品查询 |
| ![Lithium](images/catalog-gvQqBUqZ.png) [Lithium](performance.baseline.md) | 优化单人游戏与服务器的游戏逻辑。 | 已安装基准版 | 无独立物品查询 |
| ![ModernFix](images/catalog-nmDcB62a.png) [ModernFix](performance.baseline.md) | 提供性能、内存与错误修复改进。 | 已安装基准版 | 无独立物品查询 |
| ![More Culling](images/catalog-51shyZVL.png) [More Culling](performance.baseline.md) | 跳过部分不可见的渲染面。 | 已安装基准版 | 无独立物品查询 |
| ![quick pack](images/catalog-pSISfJ4O.png) [quick pack](performance.baseline.md) | 加速压缩数据包与资源包加载。 | 已安装基准版 | 无独立物品查询 |
| ![Sodium](images/catalog-AANobbMI.png) [Sodium](performance.baseline.md) | 替换地形渲染引擎。 | 已安装基准版 | 无独立物品查询 |
| ![Structure Layout Optimizer](images/catalog-ayPU0OHc.png) [Structure Layout Optimizer](performance.baseline.md) | 优化拼图结构布局处理。 | 已安装基准版 | 无独立物品查询 |
