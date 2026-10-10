# GuideME scenes and authoring capabilities

## Scope

Reviewed the official authoring, scene, Markdown and custom recipe documentation against Astropunk's selected GuideME 21.1.19 source, revision `52334ccacf15d763ffe318281d38dca8ec7aaeb8`. This is authoring research, not a rendered scene acceptance test. No game was launched and no installed resources were changed.

## Armor stands

A complete equipment display is supported in principle. The built-in `Entity` scene element accepts `minecraft:armor_stand` and a quoted `data` attribute containing Minecraft textual binary-tag data. `MdxAttrs.getCompoundTag` parses that string with the native parser, and `EntityElementCompiler` loads the entity through the native entity loader. It applies position and rotation, adds the entity to the scene and ticks it once.

Use a direct `Entity` element inside `GameScene` for the equipped stand. Do not rely on an armor stand saved into an imported structure. `ImportStructureElementCompiler` explicitly calls `setIgnoreEntities(true)`, so entities in those files are omitted in this release.

Keep native four-piece item grids alongside an equipped model, with names and tooltips. A rotating model explains appearance, not armor values, school bonuses, acquisition or set membership. Check every selected item registration and the Minecraft version's equipment serialization before constructing the entity data. Some custom armor renderers may behave differently on armor stands and players, so a correct identifier and parsed page do not establish rendered compatibility.

Start with a representative set rather than adding ninety scenes to each language at once. Assess visual scale, page length, performance, empty slots and modded rendering before expansion. Reuse the same scene asset between languages, translating annotations separately.

## Good uses in existing topics

- Equipment can compare complete outfits and show weapons held with a set. Retain the item references and equipment relationships.
- Food and farming can show a verified Cooking Pot and heat-source arrangement, with annotations identifying the parts.
- Building can demonstrate block variants, orientation and shape differences more clearly than a decorative icon.
- Machines and storage can explain a short verified connection or input and output arrangement that lacks existing help.
- Creatures and bosses can show selected registered entities where their renderer works in the scene. Keep authentic encounter imagery when habitat, scale or surrounding structures matter.

Continue using Create Ponder for its supported machinery. Scene rendering is not proof that a machine arrangement operates, a vehicle assembles, fluids transfer or a boss can spawn under normal gameplay conditions.

## Scene capabilities checked in the selected source

`DefaultExtensions` registers `GameScene` and the built-in scene elements without requiring a new Astropunk compiler. `SceneTagCompiler` accepts `zoom`, `padding`, `background`, `interactive` and `fullWidth`. Interactive scenes are opt-in.

`Block` places registered block states. `ImportStructure` loads compressed binary structure files or textual structure files, resolves asset paths relative to the page and supports positional offsets. `Entity` adds native entities with optional data and rotation. `IsometricCamera` controls the view.

Block, box, line and diamond annotations supply spatial explanation and tooltips. Annotation templates must follow the blocks or structure imports they annotate. Block removal must follow placement. The selected compiler registers `RemoveBlocks`, although one sentence in the current documentation incorrectly spells the tag `RemoveBlock`.

Current documentation gives the default entity rotation as minus forty-five degrees. The selected release uses minus ninety degrees. Explicit camera and entity rotation avoid relying on that discrepancy.

## Other useful authoring features

- `BlockImage` provides a native block rendering with supported state properties, useful when a whole scene would add no information.
- `Row` and `Column` provide spacing and alignment. Full-width layout is separate from a scene's own full-width attribute.
- `ItemLink` uses `item_ids` associations for the target page and supplies localized names and tooltips. Component-bearing items need their actual data components, not just the vanilla wrapper identifier.
- `Recipe`, `RecipeFor` and `RecipesFor` serve distinct purposes. A custom processing type requires a registered renderer. The selected default recipe mappings cover crafting, blasting, smelting and smithing, not every vanilla or modded recipe type.
- `KeyBind` reflects the current binding rather than a hard-coded key.
- `SubPages` derives links from navigation. `CategoryIndex` supplies an orthogonal category listing, not a reason to restore competing catalog navigation.
- `CommandLink` runs a normal client command without bypassing permissions. It is not a substitute for the native item-browser query extension.
- Floating images allow wrapping and explicit clearing. Prefer layouts that remain readable at compact widths.
- Current documentation examples are discovery aids, not release guarantees. In particular, the selected inline item-grid compiler rejects whitespace text children even though a documented example includes spacing.

## Verification gates

Validate the exact scene markup with the selected parser, then the scene compiler, then native entity data and item registry loading. A structural probe that normalizes items or skips scenes cannot certify scene content. Keep missing-resource, invalid-entity and malformed-data negative controls. Finally verify actual models, annotations, camera framing and interaction in a user-controlled game session.

Only add a scene to the distributed book when it improves instruction and its verification boundary is explicit. Do not replace working references with untested model displays. Preserve the prohibition on computer use and game launches.

## Sources

- [Official authoring reference](https://guideme.appliedenergistics.org/authoring/)
- [Official game scenes reference](https://guideme.appliedenergistics.org/authoring/game-scenes)
- [Official Markdown reference](https://guideme.appliedenergistics.org/authoring/markdown)
- [Official custom recipe integration](https://guideme.appliedenergistics.org/integration/recipe-types)
- Selected source evidence under `build/handbook-access/evidence/GuideME-52334ccacf15d763ffe318281d38dca8ec7aaeb8`, specifically `DefaultExtensions`, `SceneTagCompiler`, `EntityElementCompiler`, `ImportStructureElementCompiler` and `MdxAttrs`.
