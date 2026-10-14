# Astropunk Admin Worldgen

## Branch policy

Private administrator pack for offline world pregeneration. Branch `admin/worldgen` starts from committed `dev` at `676e971`. Worktree: `/home/tsb/Projects/lucas/astropunk-worldgen`. The development checkpoint `6f0e0cf` was subsequently merged, including the orientation trial and adaptive terrain transfer setting. Current administrator version: `0.12.0-admin-worldgen.1`.

Accept upstream changes from `dev` into this branch only. Do not merge or cherry-pick this branch back into `dev`, `main` or `main-heavy`. This is a workflow policy, not a technical Git access restriction. No automatic synchronization or remote publication is configured.

Update deliberately with `git merge dev` from this worktree after inspecting upstream changes. Preserve the administrator pack name, version, acceleration selections and this policy during conflicts. Do not import unrelated uncommitted work from the development worktree. Continue using native packwiz and existing Just export commands. Mod updates use the existing selective hold policy.

## Selected generation stack

- Concurrent Chunk Management Engine for NeoForge: `0.4.0-alpha.0.123+1.21.1`.
- OpenCL acceleration module: `0.4.0-alpha.0.123+1.21.1`.
- Fast Noise: `1.0.13+1.21.1+neoforge`.
- Existing Lithium, FerriteCore, Structure Layout Optimizer and Chunky are retained without unrelated updates.
- ScalableLux is excluded because the selected Sable 2.0.6 artifact explicitly declares it incompatible. The OpenCL nested mod descriptor declares ScalableLux optional, although Modrinth marks it required. Future packwiz updates may try to reintroduce it; check the result and remove it before export.

All original content and world generation settings are retained. This is not a stripped content pack. Existing Distant Horizons preferences are unchanged.

## Requirements and evaluation

Java 25 is required. The execution machine must expose an OpenCL 1.2 or newer device with double-precision support through `cl_khr_fp64`. Check the device with `clinfo` before launching. Do not install or change system graphics drivers as part of pack authoring.

The authoring host has the OpenCL loader, but its platform query returned error minus 1001 and zero platforms. No compatible device was available for an acceleration test. Java is not available through the current shell command path. These observations do not describe Lucas's Windows gaming machine.

Use disposable test worlds first, with a fixed seed and matching generation settings. Compare the accelerated pack against the unmodified development pack, checking terrain, biomes, structures, lighting, generation completion and throughput. Do not extend the only copy of a valuable world. An export passing integrity checks does not establish runtime compatibility or speed.

Upstream reports compatibility with Terralith, Incendium, Nullscape-style vanilla data packs and Tectonic from 3.0.20 onward. Custom density functions and custom generators can be incompatible. Compatibility of all Astropunk dimensions remains untested. Only noise and biome stages are accelerated.

For Distant Horizons acceleration, upstream requires Internal Server or Full Save Chunks generation mode. Rendering quality is independent. Do not change player presets automatically.

Upstream also suggests compact object headers, increased Chunky working count, collector selection based on allocation, executor parallelism and the experimental chunk serializer. These are evaluation candidates, not applied settings: hardware and memory on the actual generation machine must be established first. Preserve existing Java preferences until a measured trial warrants changes.

## Sources

- https://modrinth.com/mod/c2me-ocl
- https://github.com/RelativityMC/C2ME-fabric
- https://github.com/ryanhcode/sable/issues/367
- Selected OpenCL nested `META-INF/neoforge.mods.toml` and selected Sable `META-INF/neoforge.mods.toml` were inspected directly.
