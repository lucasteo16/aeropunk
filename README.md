# Astropunk

A Minecraft sandbox built around Create industry, flying ships and exploration, with farming, magic, character classes and optional space travel.

## Playing

- Import the supplied `.mrpack` into Modrinth App or Prism Launcher. Let the launcher install the declared Minecraft and NeoForge versions.
- Use the hosting client when joining the hosted server; it includes the saved server listing. Other editions are described below.
- Open the Astropunk handbook with the comma key or the Guide button. It covers the pack's activities, equipment and recipes in English and Simplified Chinese.
- Shaders and Distant Horizons rendering start disabled. The bundled shaders include low-quality defaults; existing player settings are preserved.

Minecraft 1.21.1 and NeoForge 21.1.259 are the current baseline. The exact edition version and loader requirements are recorded in [pack.toml](pack.toml).

## Editions and branches

Every edition is named **Astropunk**. Branch names and artifact filenames distinguish their contents.

| Branch | Purpose |
|---|---|
| `main` | Stable shared gameplay pack |
| `main-light` | Main gameplay without the nine selected environmental audio and custom entity appearance mods |
| `dev` | Integration of shared changes before stable promotion |
| `main-heavy` | Stable pack with additional visual effects |
| `admin/hosting` | Hosted-server authentication and the saved client server listing |
| `admin/hosting-light` | Hosting with the same nine exclusions as Light |
| `admin/worldgen` | Private world-generation tools, including OpenCL acceleration |

Handbook work takes place on `dev`. Shared changes move from `dev` into `main`. Light, Heavy and hosting inherit `main`; Hosting Light inherits hosting; world generation inherits `dev`. All supported source branches receive shared fixes and the same base release version. Edition-specific differences stay downstream.

## Building packs

Install [packwiz](https://packwiz.infra.link/), [Just](https://just.systems/) and Python 3.11 or newer. Ordinary Modrinth packs from hosting and Hosting Light are the primary client deliveries. From the requested edition's working directory, run:

```text
just export-modrinth
```

Exports go into `dist` and retain the newest two release versions. Source synchronization never automatically exports another edition or launches tests. Heavy, standalone Light, World Generation and Main are exported only when requested.

`just export-curseforge` and `just export-server` remain available on demand. `just export-instance` retains official Minecraft launcher instance creation. Managed-server uploads and server tests are separate requested operations. A native server export is a pack distribution, not a fully materialized server installation; manifest references must be resolved before upload, and managed providers supply Minecraft, NeoForge and Java.

Use ordinary manifest-based Modrinth packs rather than bundled self-contained clients. Complete standalone server bundles and duplicate live-client filenames are retired. Existing deliveries are not deleted by this policy change.

Packwiz normally shares its user cache across worktrees. No repository recipe selects an edition-specific packwiz cache. Worktrees preserve committed edition differences without requiring separate downloaded-mod copies for each export.

Use `just --list` for other maintenance commands. Update shared mod selections on `dev`, not directly on stable editions.

## Documentation

- [Hosted-server setup and live distributions](https://github.com/lucasteo16/aeropunk/blob/admin/hosting/docs/hosting.md)
- [Handbook access and controls](docs/handbook-access.md)
- [Handbook authoring](docs/handbook-authoring-standard.md)

Past changes remain in Git history. This README describes how to use the project, not the history of its development.
