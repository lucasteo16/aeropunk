---
navigation:
  title: "Server tools"
  position: 0
  parent: reference.technical.md
  icon: minecraft:redstone
---

# Server tools

## Terrain preparation

Chunky generates terrain before players explore it. This is an administrator workload, not a rendering-distance setting. Large generation jobs consume processing time and disk space.

| Component | Function |
| --- | --- |
| Chunky | Generates terrain ahead of exploration. |

***

## Diagnostics

Observable and spark identify processing costs. Client rendering and server simulation are different workloads. A server recording does not measure shader rendering cost. Access can depend on server permissions.

| Component | Function |
| --- | --- |
| Observable | Identifies expensive server processing. |
| spark | Profiles client and server performance. |

***

## Pack defaults

Configured Defaults provides initial files when they are missing. Existing player choices are not the same as the packaged defaults. It is a pack-maintenance utility, not a performance profiler.

| Component | Function |
| --- | --- |
| Configured Defaults | Supplies packaged defaults for missing files. |

***

## Related topics

- [Optimization](performance.baseline.md)


***

## Related mods

| Mod or content | Status | Publisher description |
| --- | --- | --- |
| ![Chunky](images/catalog-fALzjamp.png) [Chunky](server.tools.md) | Baseline, installed | Pre-generates chunks, quickly and efficiently |
| ![Configured Defaults](images/catalog-SISoSFPP.png) [Configured Defaults](server.tools.md) | Baseline, installed | Allows for providing defaults for files absent in .minecraft like configs. A quintessential modpack utility. |
| ![Observable](images/catalog-VYRu7qmG.png) [Observable](server.tools.md) | Baseline, installed | See what's lagging your server. |
| ![spark](images/catalog-l6YH9Als.png) [spark](server.tools.md) | Baseline, installed | spark is a performance profiler for Minecraft clients, servers and proxies. |
