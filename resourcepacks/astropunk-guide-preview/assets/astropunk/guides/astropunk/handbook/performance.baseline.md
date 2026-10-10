---
navigation:
  title: "Performance"
  position: 0
  parent: reference.technical.md
  icon: minecraft:clock
---

# Performance

## Rendering

<EmiSearch query="@create" />

These components reduce rendering work in different parts of the client. They are not additional visual effects.

| Component | Function |
| --- | --- |
| Sodium | Replaces the terrain rendering engine. |
| ImmediatelyFast | Optimizes immediate-mode rendering. |
| Entity Culling | Avoids rendering hidden entities and block entities. |
| More Culling | Skips selected hidden rendering faces. |
| Cull Leaves | Skips selected hidden leaf geometry. |
| Flerovium | Optimizes item, particle and entity rendering. |
| AsyncParticles | Particle processing and rendering optimization. |
| Kerria | Accelerates animated texture processing. |
| CreateBetterFps | Create rendering optimization for shader use. |

***

## Simulation & terrain

<EmiSearch query="@createlazytick" />

These components target game logic, creature processing, Create machines or terrain preparation.

| Component | Function |
| --- | --- |
| Lithium | Optimizes game logic in single-player and servers. |
| AI Improvements: Performance Tuning | Vanilla creature behavior optimization. |
| Clumps | Combines experience orbs to reduce separate orb processing. |
| Let Me Despawn | Adjusts creature despawn rules to reduce unintended persistent creatures. |
| Create: LazyTick | Create machine tick optimization. |
| Concurrent Chunk Management Engine (NeoForge) | Chunk management and generation optimization. |
| Structure Layout Optimizer | Optimizes jigsaw structure layout processing. |

***

## Memory & loading

Memory, loading and general fixes address different costs from terrain rendering.

| Component | Function |
| --- | --- |
| FerriteCore | Reduces memory use. |
| ModernFix | Performance, memory and bug-fix changes. |
| quick pack | Accelerates compressed data-pack and resource-pack loading. |
| BadOptimizations | Optimizations outside the main terrain renderer. |

***

## Input & idle use

Input processing and background resource use are separate from active-world simulation. Optimization support does not establish a measured frame-rate gain on your computer.

| Component | Function |
| --- | --- |
| Ixeris | Buffered raw input and threaded event polling. |
| Dynamic FPS | Reduces resource use in the background or while idle. |

***

## Related topics

- [Diagnostics](server.tools.md)
- [Lighting & distance](visuals.lighting.md)


## Shared optimizers

| Component | Function |
| --- | --- |
| Async Logger | Processes logging asynchronously. |
| Jasione | Reduces repeated enumeration-array allocations. |
| ServerCore | Optimizes server processing, including the integrated single-player server. |


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![AI Improvements: Performance Tuning](images/catalog-dsvgwcji.png) [AI Improvements: Performance Tuning](performance.baseline.md) | Vanilla creature behavior optimization. | No separate item search |
| ![AsyncParticles](images/catalog-c3onkd5k.png) [AsyncParticles](performance.baseline.md) | Particle processing and rendering optimization. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [BadOptimizations](performance.baseline.md) | Optimizations outside the main terrain renderer. | No separate item search |
| ![Clumps](images/catalog-wnxd13zp.png) [Clumps](performance.baseline.md) | Combines experience orbs to reduce separate orb processing. | No separate item search |
| ![Concurrent Chunk Management Engine (NeoForge)](images/catalog-colsi5ir.png) [Concurrent Chunk Management Engine (NeoForge)](performance.baseline.md) | Chunk management and generation optimization. | No separate item search |
| ![Create: LazyTick](images/catalog-z0d7hfh4.png) [Create: LazyTick](performance.baseline.md) | Create machine tick optimization. | <EmiSearch query="@createlazytick" /> |
| ![CreateBetterFps](images/catalog-lmyihznh.png) [CreateBetterFps](performance.baseline.md) | Create rendering optimization for shader use. | No separate item search |
| ![Cull Leaves](images/catalog-gnxdlcop.png) [Cull Leaves](performance.baseline.md) | Skips selected hidden leaf geometry. | No separate item search |
| ![Dynamic FPS](images/catalog-lq3k71q1.png) [Dynamic FPS](performance.baseline.md) | Reduces resource use in the background or while idle. | No separate item search |
| ![Entity Culling](images/catalog-nnagcjsb.png) [Entity Culling](performance.baseline.md) | Avoids rendering hidden entities and block entities. | No separate item search |
| ![FerriteCore](images/catalog-uxxizfis.png) [FerriteCore](performance.baseline.md) | Reduces memory use. | No separate item search |
| ![Flerovium](images/catalog-4rh1mobu.png) [Flerovium](performance.baseline.md) | Optimizes item, particle and entity rendering. | No separate item search |
| ![ImmediatelyFast](images/catalog-5zwdcrci.png) [ImmediatelyFast](performance.baseline.md) | Optimizes immediate-mode rendering. | No separate item search |
| ![Ixeris](images/catalog-p8rjpjic.png) [Ixeris](performance.baseline.md) | Buffered raw input and threaded event polling. | No separate item search |
| ![Kerria](images/catalog-f0ruqtf7.png) [Kerria](performance.baseline.md) | Accelerates animated texture processing. | No separate item search |
| ![Let Me Despawn](images/catalog-ve2fn5qn.png) [Let Me Despawn](performance.baseline.md) | Adjusts creature despawn rules to reduce unintended persistent creatures. | No separate item search |
| ![Lithium](images/catalog-gvqqbuqz.png) [Lithium](performance.baseline.md) | Optimizes game logic in single-player and servers. | No separate item search |
| ![ModernFix](images/catalog-nmdcb62a.png) [ModernFix](performance.baseline.md) | Performance, memory and bug-fix changes. | No separate item search |
| ![More Culling](images/catalog-51shyzvl.png) [More Culling](performance.baseline.md) | Skips selected hidden rendering faces. | No separate item search |
| ![quick pack](images/catalog-psisfj4o.png) [quick pack](performance.baseline.md) | Accelerates compressed data-pack and resource-pack loading. | No separate item search |
| ![Sodium](images/catalog-aanobbmi.png) [Sodium](performance.baseline.md) | Replaces the terrain rendering engine. | No separate item search |
| ![Structure Layout Optimizer](images/catalog-aypu0ohc.png) [Structure Layout Optimizer](performance.baseline.md) | Optimizes jigsaw structure layout processing. | No separate item search |
