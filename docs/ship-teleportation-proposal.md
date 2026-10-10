# Ship teleportation patch proposal

## Scope

Prepare an isolated patch from main commit 34cb006, on patch/ship-teleportation. Do not merge into the guide branch or main, push, launch Minecraft, import a pack or alter an installed instance.

Select Create: AeroWarptics 1.3.0, CurseForge project 1659672 and file 8787426, after inspecting its published binary. It supplies whole-airship relocation, not space destinations. Waystones: Sable remains the separate passenger destination bridge.

Select AeroEngine fuel compat 0.0.2, Modrinth project RNUSzf19 and version iQWqNLQY, after checking the exact selected AeroEngine method and TFMG Community Edition fluid tags. This is a real integration addon, not a proposed custom recipe or a replacement engine.

## Selected baseline and declared compatibility

The patch targets Minecraft 1.21.1 and NeoForge 21.1.255. Main selects Create 6.0.10, Create Aeronautics bundled 1.3.2, Sable 2.0.6, GeckoLib 4.9.3, AeroEngine release 1.3.0 and TFMG Community Edition 1.3.1.

The downloaded AeroWarptics binary declares Minecraft [1.21.1,1.22), NeoForge [21,), Create [6.0.10,), Sable [2.0.0,3.0.0), Simulated [1.3.0,), Aeronautics [1.3.0,) and GeckoLib [4.8.0,). These selected versions meet those ranges. Simulated is supplied by the bundled Aeronautics archive, not a new standalone addition.

AeroEngine release 1.3.0 declares the internal mod identifier aeroengineering and internal version 1.0.2. The fuel addon requires aeroengineering [1.0.2,). Its required mixin targets com.cxw.aeroengineering.registry.ModFluids.isAviationKerosene with a FluidStack argument and boolean result. That exact static method exists in the checksum-selected AeroEngine binary.

The fuel addon accepts the common fluid tags c:kerosene, c:fuel, c:gasoline, c:plantoil and c:ethanol. The selected TFMG Community Edition archive includes tfmg:kerosene and its flowing form in c:kerosene. Its c:fuel tag is broader and also includes diesel, gasoline, naphtha, creosote and several gases. This addon does not provide per-fuel energy balancing or a kerosene-only policy. Its return-true injection preserves AeroEngine's original aviation kerosene fallback. Published source matches the selected binary's target and tag strings.

## Destination boundary

AeroWarptics 1.3.0 contains a CrossDimensionWarp extension hook. Static inspection resolves all 94 referenced Sable method descriptors against the checksum-selected Sable 2.0.6 archive, including inherited methods, and finds no missing Sable classes. No class in the selected AeroWarptics release calls CrossDimensionWarp.setHandler. Cross-dimensional support requires an external handler and the corresponding setting. A hook is not a shipped Northstar connector. Treat this patch as same-dimension ship teleportation, with no space destinations or cross-dimensional transfer promise. The guide branch currently does not include AeroWarptics. Keep its guide prose explicitly deferred while explaining the isolated patch separately.

## Distribution and verification

Add only the two exact releases through native packwiz commands. Preserve all baseline mod metadata, settings and game resources. Keep ordinary selections unpinned under the existing selective-hold policy. Bump this backward-compatible feature batch from 0.3.0 to 0.4.0. Refresh and export natively, verify archive integrity, manifest membership, packaged hashes and documentation exclusion. Record execution results separately. Packaging and static binary inspection do not prove game startup, applied mixins, ship movement, passenger safety or rendered guide layout.

## Sources and downloaded binary checksums

- https://www.curseforge.com/minecraft/mc-mods/create-aerowarptics/files/8787426
- https://modrinth.com/mod/aeroengine-fuel-compat/version/iQWqNLQY
- https://github.com/fartunrus/AeroEngine-fuel-compat
- https://modrinth.com/mod/aeroengine/version/eqi1VZul
- https://modrinth.com/mod/tfmg-community-edition/version/LNfoHEO4

AeroWarptics binary SHA-256: 121d1e10fdce23695d9b9c4baebdde3b0feaf42e4847447f5fd78cbb3bf6fa2d.

Fuel compatibility binary SHA-256: 305d5e6345cf6005e8dd2e32584f81d99ce6ebb3f8001d49c29566c8c259682a. Its SHA-512 matches the exact Modrinth release. All inspected baseline binaries match their packwiz SHA-512 selections.
