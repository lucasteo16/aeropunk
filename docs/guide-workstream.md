# Guide workstream

## Isolation

Branch: `test/guide`.

Workspace: `/home/tsb/Projects/lucas/astropunk-guide`.

Base: light `main` at `34cb006`.

The older heavy-based preview is preserved at tag `archive/guide-heavy-preview-2`. It is no longer the active guide branch. Keep main, main-heavy and other testing worktrees unchanged.

Only handbook resources, authoring scripts and guide research were migrated. GuideME 21.1.19 was added through packwiz. Main's current mod selections, configurations and defaults remain authoritative. The guide-enabled resource-pack entry is appended to the light defaults.

## Content

English and Simplified Chinese only. Every topic is freely readable. Existing Ponder demonstrations remain the preferred construction help. Custom external-screen actions are not implemented.

The original inventory and research documents are historical source snapshots. `handbook-draft-manifest.json` records current installed membership. Optional heavy-edition content is visibly marked as not installed in the light preview. Deferred additions remain separate.

## Live development

After importing the light preview as a dedicated instance, its guide resource-pack folder can be linked to this workspace. Preserve the imported folder in a local archive before replacing it with a symbolic link. Link only the guide resource pack, never mods, configurations or worlds.

GuideME's native live-preview source property should point at `resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook` in this workspace. It watches page edits while Minecraft runs. A symbolic link by itself only exposes current file bytes; automatic page refresh comes from live-preview mode. New compiled mods still require a restart.
