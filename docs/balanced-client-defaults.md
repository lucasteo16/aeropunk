# Balanced client defaults

The first-install templates under `configureddefaults/config` retain all selected mods and apply four conservative changes:

| Consumer | Setting | Default | Pack preset |
|---|---|---|---|
| Sound Physics Remastered 1.5.1 | `environment_evaluation_ray_count` | 32 | 24 |
| Sound Physics Remastered 1.5.1 | `max_sound_processing_distance` | 512.0 | 384.0 |
| Presence Footsteps NeoForge 1.12.0-beta.1 | `maxSteppingEntities` | 50 | 32 |
| Entity Texture Features 7.2.5 | `textureUpdateFrequency_V2` | `Fast` | `Average` |

The audio templates intentionally contain only the approved overrides; the native readers retain other release defaults. Presence Footsteps loads JSON into its initialized instance, preserving omitted fields. Sound Physics builds typed entries with native defaults. The existing Entity Texture Features preset moves from active configuration into Configured Defaults with only its update-frequency value changed, preserving every other authored setting and avoiding a competing active override.

Four reflection bounces, accurate occlusion, directional effects, all footstep entity categories, rain physics, model animation detail and glowing textures remain unchanged. The sound processing cutoff does not mute distant sounds. The footstep value is a non-player crowd threshold, not a hard limit on players or total audible entities. Texture frequency controls changing variant rules, not animation playback speed.

Configured Defaults copies these ordinary files only when the corresponding destination file is absent. Existing player settings are preserved and are not merged per key. Testing an existing installation requires deliberate manual changes or a fresh import; the pack does not modify played instances.

No frame-rate improvement or perceptual-quality percentage has been measured. These are modest calculation-budget adjustments, not a substitute for the Light edition's removals.
