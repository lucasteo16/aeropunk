# Astropunk Handbook Access

Client-only helper for Minecraft 1.21.1, NeoForge 21.1.255 and GuideME 21.1.19. It does not package GuideME or handbook content.

## Controls

- Adds an ordinary, narrated Handbook button to survival and creative inventory screens, without removing or replacing existing controls.
- Finds an available position outside the inventory panel and visible existing widgets. If the entire screen has no free button area, leaves existing controls intact and relies on the shortcut.
- Adds Open Astropunk Handbook to Minecraft Controls, under Astropunk Handbook. The default is F9, so GuideME's existing contextual G control is untouched.
- The assigned keyboard shortcut works in the world and for otherwise unhandled keys in inventory. It does not intercept chat, text entry or other screens.
- Opens the local player's `astropunk:handbook` through the released public `GuidesCommon.openGuide(Player, ResourceLocation)` endpoint. Missing handbook resources produce a localized client message. No helper items, server commands, permission checks or custom network packets are involved.
- Supplies English and Simplified Chinese interface labels.

GuideME itself retains its normal installation requirements. The helper introduces no server installation requirement. No dedicated server or multiplayer runtime has been exercised.

## Native live editing

The client mod constructor inspects the actual game directory through `FMLPaths.GAMEDIR`. Only when `resourcepacks/astropunk-guide-preview` is a symbolic link and its handbook source directory exists, it fills missing system properties:

- `guideme.astropunk.handbook.sources` points to `assets/astropunk/guides/astropunk/handbook` inside that symbolic resource pack.
- `guideme.astropunk.handbook.sourcesNamespace` is `astropunk`.

Existing property values are preserved independently. Ordinary directories, archived exports, missing previews and broken links do not activate automatic authoring mode. The helper neither creates links nor writes source files, resource packs, launcher settings or configuration files. The automatic setup takes effect when this helper starts on the next client restart.

### Released startup timing

Source baseline is GuideME commit `52334ccacf15d763ffe318281d38dca8ec7aaeb8`, also checked against the published 21.1.19 jar.

1. NeoForge 21.1.255 `Minecraft` calls `ClientModLoader.begin` before initial resource loading.
2. `CommonModLoader.begin` calls `ModLoader.gatherAndInitializeMods`, which constructs the helper. The helper fills system properties at the beginning of its constructor, before registering its event listeners.
3. GuideME `GuideReloadListener.prepare`, lines 47 and 48, discovers data-driven definitions during resource reload. `loadDataDrivenGuides`, lines 124 to 134, constructs `Guide.builder(guideId)`.
4. `GuideBuilder`, lines 52 to 59, reads the source properties in its constructor. `build`, lines 251 and 252, enables the source watcher by default when sources exist.
5. `MutableGuide.watchDevelopmentSources`, `setPages` and `tick` load development pages and apply watched changes through the native watcher.

Therefore setting the properties during helper construction precedes creation of the resource-defined handbook. The helper never registers a competing guide. Timing is established from released source, not from a launched game.

## Native text size investigation

GuideME 21.1.19 has no independent text-size or zoom setting in its client configuration. `gui.fullWidthLayout` changes available layout width, not font size. `gui.adaptiveScaling` corrects Minecraft font behavior at scales one and three; it does not normally enlarge scale four.

In released `DocumentScreen.calculateEffectiveScale`, scale one becomes two and scale three becomes four. Other scales remain unchanged unless the scaled window is too small, in which case the engine reduces the scale. Consequently the parent's confirmed scale four with full-width layout and adaptive scaling enabled is not a native text zoom control.

`DefaultStyles.BASE_STYLE` uses font scale one with `Minecraft.UNIFORM_FONT`. `TextStyle.Builder.fontScale(Float)` is a real public Java styling method, but the released built-in tag compilers expose no `fontScale` attribute. Increasing Minecraft's interface scale is the native global size control when the window supports it. Changing only handbook font size would require a separately designed document customization, not a fabricated configuration key. This helper does not alter fonts, interface scale, engine styles or the data-driven guide registration.

## Build and evidence

The official NeoForge 1.21.1 ModDevGradle template supplies the genuine Gradle wrapper. Build uses ModDevGradle 2.0.148, Gradle 9.2.1 and a locally downloaded Java 21 toolchain. Dependencies and Gradle caches are isolated under this project.

Run `bash build.sh` from this directory. It performs a clean build, runs nine JUnit tests and verifies the actual jar with `verify_artifact.py`.

Tests cover missing-guide feedback, successful opening dispatch, absent-player safety, collision-free button placement, no-space fallback, symbolic-preview activation, ordinary exports, explicit source overrides and broken links. Red test evidence is retained in the `red-*.log` files. Archive verification checks the client-only annotation, dependency metadata, exact released public method descriptors, locale parity, F9 default, no packaged engine or guide definitions, and no reflection or packet registration.

`build-output.log` and `verification-output.log` record the successful build and archive inspection. `final-build.log` records the last clean build and archive verification together.

Run `python validate_syntax.py` for syntax-only validation of the parent's 198 handbook pages. This separate harness uses the actual shaded MdAst parser in the released GuideME jar and the exact syntax extensions from `PageCompiler.parse`. It includes a deliberately malformed native tag as a negative control. `syntax-validation-output.log` records all 198 pages passing with zero parser failures. Only the parser and its logging dependency are on this harness's runtime classpath, not Minecraft. Syntax success does not establish item identifiers, tag semantics, compiled layouts, frontmatter semantics or rendered interaction; parent source tests handle links and coverage.

Game rendering, keyboard interaction, non-operator multiplayer, resource reloads and live watcher behavior remain runtime-untested. No game was launched and no launcher installation, pack export or commit was performed.
