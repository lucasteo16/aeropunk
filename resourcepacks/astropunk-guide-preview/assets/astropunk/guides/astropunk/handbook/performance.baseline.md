---
navigation:
  title: "Performance"
  position: 0
  parent: reference.technical.md
  icon: minecraft:redstone
---

# Performance

## Rendering

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

Input processing and background resource use are separate from active-world simulation. Installation does not establish a measured frame-rate gain on your computer.

| Component | Function |
| --- | --- |
| Ixeris | Buffered raw input and threaded event polling. |
| Dynamic FPS | Reduces resource use in the background or while idle. |

***

## Related topics

- [Diagnostics](server.tools.md)
- [Lighting & distance](visuals.lighting.md)


***

## Related mods

| Mod or content | Status | Publisher description |
| --- | --- | --- |
| ![AI Improvements: Performance Tuning](images/catalog-DSVgwcji.png) [AI Improvements: Performance Tuning](performance.baseline.md) | Baseline, installed | Performance improvements for vanilla AI, with  the ability to turn off certain AI behaviors |
| ![AsyncParticles](images/catalog-c3onkd5k.png) [AsyncParticles](performance.baseline.md) | Baseline, installed | Async particle tick, GPU accelerated particle rendering. |
| <ItemImage id="minecraft:redstone" /> [BadOptimizations](performance.baseline.md) | Baseline, installed | Optimization mod that focuses on things other than rendering |
| ![Clumps](images/catalog-Wnxd13zP.png) [Clumps](performance.baseline.md) | Baseline, installed | Clumps XP orbs together to reduce lag |
| ![Concurrent Chunk Management Engine (NeoForge)](images/catalog-COlSi5iR.png) [Concurrent Chunk Management Engine (NeoForge)](performance.baseline.md) | Baseline, installed | A mod designed to improve the chunk performance of Minecraft. |
| ![Create: LazyTick](images/catalog-Z0d7hFh4.png) [Create: LazyTick](performance.baseline.md) | Baseline, installed | A commitment to optimizing Create lag in large quantities! |
| ![CreateBetterFps](images/catalog-lMYIHZNH.png) [CreateBetterFps](performance.baseline.md) | Baseline, installed | Improve your Create FPS when shaderpack is on, up to 50% |
| ![Cull Leaves](images/catalog-GNxdLCoP.png) [Cull Leaves](performance.baseline.md) | Baseline, installed | Adds culling to leaf blocks, providing a huge performance boost over vanilla. |
| ![Dynamic FPS](images/catalog-LQ3K71Q1.png) [Dynamic FPS](performance.baseline.md) | Baseline, installed | Reduce resource usage while Minecraft is in the background, idle, or on battery. |
| ![Entity Culling](images/catalog-NNAgCjsB.png) [Entity Culling](performance.baseline.md) | Baseline, installed | Using async path-tracing to hide Block-/Entities that are not visible |
| ![FerriteCore](images/catalog-uXXizFIs.png) [FerriteCore](performance.baseline.md) | Baseline, installed | Memory usage optimizations |
| ![Flerovium](images/catalog-4Rh1Mobu.png) [Flerovium](performance.baseline.md) | Baseline, installed | Greatly improve your fps with virtually no side-effects on graphics quality |
| ![ImmediatelyFast](images/catalog-5ZwdcRci.png) [ImmediatelyFast](performance.baseline.md) | Baseline, installed | Speed up immediate mode rendering in Minecraft |
| ![Ixeris](images/catalog-p8RJPJIC.png) [Ixeris](performance.baseline.md) | Baseline, installed | Buffered raw input and threaded event polling |
| ![Kerria](images/catalog-f0ruQTF7.png) [Kerria](performance.baseline.md) | Baseline, installed | Faster texture animation |
| ![Let Me Despawn](images/catalog-vE2FN5qn.png) [Let Me Despawn](performance.baseline.md) | Baseline, installed | Improves performance by tweaking mob despawn rules. Say bye to pesky unintentional persistent mobs. |
| ![Lithium](images/catalog-gvQqBUqZ.png) [Lithium](performance.baseline.md) | Baseline, installed | No-compromises game logic optimization mod, useful for both single-player games and multi-player servers. |
| ![ModernFix](images/catalog-nmDcB62a.png) [ModernFix](performance.baseline.md) | Baseline, installed | All-in-one mod that improves performance, reduces memory usage, and fixes many bugs. Compatible with all your favorite performance mods! |
| ![More Culling](images/catalog-51shyZVL.png) [More Culling](performance.baseline.md) | Baseline, installed | A mod that changes how multiple types of culling are handled in order to improve performance |
| ![quick pack](images/catalog-pSISfJ4O.png) [quick pack](performance.baseline.md) | Baseline, installed | Optimize datapack / resourcepack zip file loading times |
| ![Sodium](images/catalog-AANobbMI.png) [Sodium](performance.baseline.md) | Baseline, installed | A high-performance rendering engine replacement for Minecraft, which greatly improves frame rates and reduces micro-stutter. |
| ![Structure Layout Optimizer](images/catalog-ayPU0OHc.png) [Structure Layout Optimizer](performance.baseline.md) | Baseline, installed | Attempts to optimize the generation of Jigsaw Structures and NBT pieces |
