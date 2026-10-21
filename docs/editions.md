# Astropunk editions

The active branches are `dev`, `main`, `main-light`, `main-heavy`, `admin/hosting`, `admin/hosting-light` and `admin/worldgen`. All keep the display name Astropunk. Main has no version suffix; the other branches retain `-dev`, `-light`, `-heavy`, `-hosting`, `-hosting-light` and `-worldgen` respectively.

## Shared changes and release completion

Shared features and fixes enter `dev`, are promoted into `main`, then merge downstream into Light, Heavy and hosting. Hosting Light inherits hosting. World generation inherits `dev`. A global fix first discovered on an edition must be applied to the shared baseline before the change is finished. Do not merge an entire administrator or visual edition upstream to transfer one shared fix.

Every completed change batch uses one base release version across all seven active branches, preserving their suffixes. A branch-specific correction still requires aligning the release family. New shared feature work starts only after the previous accepted shared fixes have reached every active branch. Matching a remote branch is not evidence that shared maintenance is synchronized.

Use normal Git commits and merges, preserving edition-only additions and removals. Before publication, check clean worktrees, shared-fix ancestry, exact edition membership, indexed-file checksums and matching base versions. Push the explicit coordinated branch set and read back every remote commit. No force pushes or hidden local patches are needed. Exports and deployments remain separate actions and must not be claimed current when intentionally not rebuilt.

## Edition boundaries

Light and Hosting Light remove only the nine entries declared in their tracked `docs/light-edition.json`, relative to Main and hosting respectively. Heavy adds the optional client visual stack. Hosting adds authentication policy, the saved server listing and its remaining edition-specific information tools. World generation adds private acceleration tools. Shared utility features, including Just Enough Breeding on both client and server, belong to the shared baseline rather than hosting alone.

Each Light baseline reference must advance with the corresponding accepted parent merge. Keep shared tests identical across editions and account for legitimate edition differences explicitly, rather than maintaining divergent copies of common tests.

## Export policy

Keep every supported source branch synchronized, but build only requested deliveries. Regular hosting and Hosting Light Modrinth packs are the primary client formats. Main is the publishable baseline. Heavy, standalone Light and World Generation exports are on demand. CurseForge client exports, server exports, managed-host uploads, official-launcher instance creation and server tests are also on demand. A source commit, merge or version alignment never requires exporting every edition or launching a test.

Native Modrinth and CurseForge commands remain available. The self-contained bundled-client exporter, complete standalone-server builder and duplicate live-client filenames are retired. Existing archives, runtime installations, worlds and shared download caches are preserved. Historical experimental procedures remain historical, not release prerequisites.

Hosting Light is a normal Git branch and checkout. Clone the repository, check out `admin/hosting-light`, install the documented packwiz and Just prerequisites, and run `just export-modrinth`. There is no ignored snapshot, manual metadata-removal sequence or separate exporter needed to obtain that variant.

The standard packwiz cache is user-scoped, normally `~/.cache/packwiz/cache`, and the native recipes pass no cache override. The retained launcher exporter reads the same default cache. Different worktrees do not require distinct caches; this does not promise that unchanged downloads are never checked or that packaging itself is free.

The split follows Lucas’s disabled screenshot selections. Heavy adds Fancy Crops, all four Fresh Animations packs, Simple Grass Flowers, Visual Effects+, Create Sable Dynamic Lights, Eating Animations, Not Enough Animations and its Entity Model Features compatibility addon, Explosive Enhancement, Fancy World Animations, Particle Effects, Particular Reforged, Ripple, Sodium Dynamic Lights and Team Capes. Heavy also initializes Interactic fancy item rendering as enabled; lean initializes it as disabled. Interactic gameplay settings and artifact remain identical. Configured Defaults preserves existing ordinary configuration files, so use fresh imports to compare the presets.

Spawn Animations and Spawn Animations Compats are excluded from both editions. Spark is server-only in both, which excludes client profiling and profiling local single-player through a bundled spark installation. Rendering optimizations and gameplay animation libraries are retained. Better Leaves, shaders, Distant Horizons, audio additions, Mandala’s dark interface and Hide Experimental Warning are retained; they were not part of this screenshot-defined removal batch. Shader and Distant Horizons rendering preferences remain initially disabled, not restrictions on player choices.

## Reproducible source

Track all authored pack inputs, edition definitions, dependency declarations, build instructions and required automation. Ignore generated exports, downloaded dependency caches, runtime output, worlds and secrets deliberately. A clean clone must not depend on a unique ignored snapshot, a local-only exclusion or an untracked build command. Downloaded dependencies need declared versions and checksum validation. Private server credentials and world backups are separate from pack-source reproducibility.

Worktree directories are replaceable checkouts, not another source of truth. Historical trials are retained by Git archive tags where applicable, not treated as active releases. Packaging checks are distinct from game startup and player verification; Lucas's successful hosted breeding test establishes the accepted behavior for Just Enough Breeding 3.3.1.
