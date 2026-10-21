# Astropunk editions

The active branches are `dev`, `main`, `main-light`, `main-heavy`, `admin/hosting` and `admin/worldgen`. All keep the display name Astropunk. Main has no version suffix; the other branches retain `-dev`, `-light`, `-heavy`, `-hosting` and `-worldgen` respectively.

## Shared changes and release completion

Shared features and fixes enter `dev`, are promoted into `main`, then merge downstream into Light, Heavy and hosting. World generation inherits `dev`. A global fix first discovered on an edition must be applied to the shared baseline before the change is finished. Do not merge an entire administrator or visual edition upstream to transfer one shared fix.

Every completed change batch uses one base release version across all six active branches, preserving their suffixes. A branch-specific correction still requires aligning the release family. New shared feature work starts only after the previous accepted shared fixes have reached every active branch. Matching a remote branch is not evidence that shared maintenance is synchronized.

Use normal Git commits and merges, preserving edition-only additions and removals. Before publication, check clean worktrees, shared-fix ancestry, exact edition membership, indexed-file checksums and matching base versions. Push the explicit coordinated branch set and read back every remote commit. No force pushes or hidden local patches are needed. Exports and deployments remain separate actions and must not be claimed current when intentionally not rebuilt.

## Edition boundaries

Light removes only the nine entries declared in its tracked `docs/light-edition.json`. Heavy adds the optional client visual stack. Hosting adds authentication policy, the saved server listing and its remaining edition-specific information tools. World generation adds private acceleration tools. Shared utility features, including Just Enough Breeding on both client and server, belong to the shared baseline rather than hosting alone.

The Light baseline reference must advance with each accepted Main merge. Keep shared tests identical across editions and account for legitimate edition differences explicitly, rather than maintaining divergent copies of common tests.

The split follows Lucas’s disabled screenshot selections. Heavy adds Fancy Crops, all four Fresh Animations packs, Simple Grass Flowers, Visual Effects+, Create Sable Dynamic Lights, Eating Animations, Not Enough Animations and its Entity Model Features compatibility addon, Explosive Enhancement, Fancy World Animations, Particle Effects, Particular Reforged, Ripple, Sodium Dynamic Lights and Team Capes. Heavy also initializes Interactic fancy item rendering as enabled; lean initializes it as disabled. Interactic gameplay settings and artifact remain identical. Configured Defaults preserves existing ordinary configuration files, so use fresh imports to compare the presets.

Spawn Animations and Spawn Animations Compats are excluded from both editions. Spark is server-only in both, which excludes client profiling and profiling local single-player through a bundled spark installation. Rendering optimizations and gameplay animation libraries are retained. Better Leaves, shaders, Distant Horizons, audio additions, Mandala’s dark interface and Hide Experimental Warning are retained; they were not part of this screenshot-defined removal batch. Shader and Distant Horizons rendering preferences remain initially disabled, not restrictions on player choices.

## Reproducible source

Track all authored pack inputs, edition definitions, dependency declarations, build instructions and required automation. Ignore generated exports, downloaded dependency caches, runtime output, worlds and secrets deliberately. A clean clone must not depend on a unique ignored snapshot, a local-only exclusion or an untracked build command. Downloaded dependencies need declared versions and checksum validation. Private server credentials and world backups are separate from pack-source reproducibility.

Worktree directories are replaceable checkouts, not another source of truth. Historical trials are retained by Git archive tags where applicable, not treated as active releases. Packaging checks are distinct from game startup and player verification; Lucas's successful hosted breeding test establishes the accepted behavior for Just Enough Breeding 3.3.1.
