# Astropunk editions

The default main branch is the lean gameplay baseline. The main-heavy branch independently inherits main and adds the optional client visual stack. Apply shared gameplay, fixes and updates to main first, then merge main into main-heavy. Do not merge heavy-only visuals back into main. Both have separate Git workspaces and use native packwiz and Just exports.

The split follows Lucas’s disabled screenshot selections. Heavy adds Fancy Crops, all four Fresh Animations packs, Simple Grass Flowers, Visual Effects+, Create Sable Dynamic Lights, Eating Animations, Not Enough Animations and its Entity Model Features compatibility addon, Explosive Enhancement, Fancy World Animations, Particle Effects, Particular Reforged, Ripple, Sodium Dynamic Lights and Team Capes. Heavy also initializes Interactic fancy item rendering as enabled; lean initializes it as disabled. Interactic gameplay settings and artifact remain identical. Configured Defaults preserves existing ordinary configuration files, so use fresh imports to compare the presets.

Spawn Animations and Spawn Animations Compats are excluded from both editions. Spark is server-only in both, which excludes client profiling and profiling local single-player through a bundled spark installation. Rendering optimizations and gameplay animation libraries are retained. Better Leaves, shaders, Distant Horizons, audio additions, Mandala’s dark interface and Hide Experimental Warning are retained; they were not part of this screenshot-defined removal batch. Shader and Distant Horizons rendering preferences remain initially disabled, not restrictions on player choices.

Northstar remains experimental and on hold. Retired optimizer and isolation branches have been removed after promotion or supersession. Packaging checks do not establish runtime compatibility or measured frame rates. Lucas reported a large improvement after disabling the screenshot group; no individual cost is established.

The optimizer trial was manually tested by Lucas and promoted to both editions. Shared additions are Async Logger, Jasione and ServerCore. Northstar remains on hold because of its rendering issue.

## Ship teleportation additions in 0.5.0

Main includes Create: AeroWarptics 1.3.0 for same-dimension relocation of assembled Aeronautics ships and AeroEngine fuel compat 0.0.2 for accepting shared fuel tags, including TFMG Community Edition kerosene. The fuel addon accepts the broader common fuel tag, not only kerosene, and does not rebalance each fuel's energy value.

Lucas authorized inclusion before functional travel and fuel testing. The fresh official launcher instance reached world entry, saved and shut down normally. Its latest and debug logs contained no fatal markers or error-level messages naming these additions. Nonfatal recipe, model, Sable property, item-browser and Distant Horizons with Chunky integration errors remain separate unresolved findings. Actual teleportation, passenger and inventory preservation, and fuel consumption are unverified.

The original isolated proposal and packaging evidence are retained in docs/ship-teleportation-proposal.md and docs/ship-teleportation-verification.json as historical records. No live installation is updated and no push is performed.
