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
| `admin/worldgen` | Private world-generation tools, including OpenCL acceleration |

Handbook work takes place on `dev`. Shared changes move from `dev` into `main`. Light, Heavy and hosting inherit `main`; world generation inherits `dev`. Edition-specific changes stay downstream.

## Building packs

Install [packwiz](https://packwiz.infra.link/), [Just](https://just.systems/) and Python 3.11 or newer. From the selected branch's working directory:

```text
just export-modrinth
just export-curseforge
just export-server
```

Exports go into `dist`. Normal exports retain the newest two release versions. The server export is a pack distribution, not a complete Minecraft and NeoForge installation; managed providers supply the game runtime.

Use `just --list` for other maintenance commands. Update shared mod selections on `dev`, not directly on stable editions.

## Documentation

- [Hosted-server setup and live distributions](https://github.com/lucasteo16/aeropunk/blob/admin/hosting/docs/hosting.md)
- [Handbook access and controls](docs/handbook-access.md)
- [Handbook authoring](docs/handbook-authoring-standard.md)

Past changes remain in Git history. This README describes how to use the project, not the history of its development.
