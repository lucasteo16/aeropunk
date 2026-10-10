# Project layout

The original repository at `/home/tsb/Projects/lucas/aeropunk` is the main branch workspace. Do not create a separate main worktree. The remaining sibling folders are Git worktrees only: astropunk-heavy, astropunk-guide and astropunk-northstar.

Keep project-owned generated data inside its source repository or worktree. Use ignored dist, build, reports, instance-templates, instance-runs and .archive folders as appropriate. Both Git and packwiz must exclude templates, test installations, backups, worlds and archived data. The parent Projects directory is not an Astropunk working directory.

The main repository owns the existing official-launcher templates and test installations. An export from another worktree defaults to that worktree's own ignored folders; an explicit template argument can point at main's template. Launcher-owned runtime libraries and account settings remain in the launcher's native location, and native packwiz downloads remain in the normal shared cache.

Before relocating a registered test installation, close the launcher and game, preserve all game-file hashes, back up launcher profiles privately, update only affected gameDir fields, and read back the complete profile document. Disposable tests may still contain worlds, so do not delete them implicitly during workspace cleanup.

The obsolete distribution archive was removed after replacement exports were verified. Potentially unique handbook references and retired workspace snapshots are retained in the repository's ignored .archive folder, not directly beneath Projects.
