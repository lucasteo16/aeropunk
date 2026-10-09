# Native recipe-browser query integration

## Result and activation prerequisite

The helper now compiles a native GuideME `EmiSearch` component through the public `GuideBuilder.extension(TagCompiler.EXTENSION_POINT, compiler)` endpoint. `HandbookAccess` registers the query-enabled handbook on the client setup event through `enqueueWork`. The selected release is GuideME 21.1.19, with EMI 1.1.24 for Minecraft 1.21.1 and NeoForge.

Before parent integration, the resource definition at `resourcepacks/astropunk-guide-preview/assets/astropunk/guideme_guides/handbook.json` overrode the same-identifier static guide. That replacement had no custom compiler. The native registry test executes this override and demonstrates the loss of the query component. Parent integration has archived and removed that JSON definition from both the source pack and the selected installed fallback, and installed the tested helper after confirming Minecraft was closed. A user-controlled next launch loads the new Java classes. Keep all guide pages, translations and images in their existing resource locations. The helper preserves the existing `Astropunk Handbook` display name, default language, default guide folder, start page, built-in extensions and development-source properties.

This task did not change the JSON definition, page generator, mod roster, packaged mod folder, launcher instance or running game. New Java code requires the helper artifact to be distributed and Minecraft restarted. A resource reload alone cannot activate it. No live installation was performed.

## Supported markup

```mdx
Browse the <EmiSearch query="@create" /> catalog.

Browse <EmiSearch query="@create">Create items</EmiSearch>.

<EmiSearch query="@reinfshulker" />

<EmiSearch query='@"Farmer&#39;s Delight"'>Farmer's Delight items</EmiSearch>

<EmiSearch query="backpack">Backpacks!</EmiSearch>

<EmiSearch query="背包">背包</EmiSearch>

<EmiSearch query="@create | @minecraft" />
```

Inline and standalone block forms compile through GuideME's native dispatcher. The required query must be a nonblank quoted string. JavaScript expression attributes are rejected. Entity escapes decode through the native parser. A self-closing component displays the exact query; children supply a custom label. The compiler makes the link pink using packed color `0xffF28CBD` and explicitly disables italics. Native link hover behavior still underlines it. The query is passed unchanged to the opening callback.

There is no invented URL scheme or command handler. Wrapping ordinary `@create` text in `Color` does not make it clickable. No built-in query-opening component was found in the selected GuideME default tag compiler list; a scan of its class files found no direct `dev/emi/` references. Ordinary external links are not used for this integration.

## Opening and return behavior

The compiled endpoint first checks for a player and optional EMI presence. Without EMI, it leaves the guide open and displays the query in a short client message. EMI calls live in a nested presence-only class, so the outer guard and native component can load without EMI classes. The headless registration and compilation test runs both with and without the EMI jar on its classpath.

When EMI is present, the helper saves the current guide screen, opens a handled screen backed by the player's existing `InventoryMenu`, and then calls the selected public `EmiApi.setSearchText(String)` method. The selected setter only mutates the search widget; it does not open a screen. The ordering test checks the compiled helper's `Minecraft.setScreen` call before its search mutation.

The handled screen extends `AbstractContainerScreen<InventoryMenu>` rather than `InventoryScreen`. Vanilla `InventoryScreen` redirects creative players during initialization, which would discard the custom return callback. The helper renders the vanilla inventory background and tooltips. Its `onClose` restores the saved screen object rather than reopening the handbook start page. Native container keyboard handling calls `onClose` for the inventory key; Escape also uses the screen close endpoint.

This is an implementation and compiled-call verification, not a gameplay reproduction. No game was launched. The actual overlay layout, survival and creative interaction, search results, Escape return and return after following a recipe remain manual checks after the user's restart. EMI's disabled or hidden overlay settings are respected, not silently rewritten. Opening the handled screen cannot guarantee a visible overlay when the player has disabled it. The query filters the item catalog; it does not filter every recipe category or promise that every addon provides items.

## Exact selected EMI namespace semantics

The released `EmiSearch.bake()` bytecode adds both of these strings to the mod suffix index for each indexed stack:

1. `EmiUtil.getModName(stack.getId().getNamespace()).toLowerCase()`
2. `stack.getId().getNamespace().toLowerCase()`

The released `ModQuery` constructor lowercases its argument and searches `EmiSearch.mods` through Minecraft's `SuffixArray.search`. Its ordinary `matches` method checks identity membership in that search result.

Therefore a baked namespace query is supported even when its display name differs. Underscores remain literal. The real released `ModQuery` and real Minecraft `SuffixArray` were executed against an isolated index fixture: `create_foo` and `CREATE_FOO` match, `createfoo` and `create foo` do not, a display-name substring matches, and an absent token does not. Matching is substring-based, so `@create` can also include addon namespaces containing `create`. This is not an exact namespace equality operator.

The released `matchesUnbaked` fallback is narrower: it checks only the lowercased display name returned by `EmiUtil.getModName`, not the raw namespace. Treat namespace-based behavior as supported for the normal completed, baked item index; do not promise it during initial indexing.

The parent should use its SHA-verified selected namespace and item-model evidence rather than provider slugs. The candidate inventory is not a live registry dump. Libraries, audio and graphics providers without item catalogs should say `No item catalog`, or link a separately evidenced gameplay producer. Component-bearing vanilla stacks can require localized name queries, such as the Backpacks! examples above. The production-gated `create_abyss` namespace should remain excluded from ordinary catalog guidance.

## Tests and evidence boundaries

`test_query_integration.py` executes five test groups:

- Compiled native extension existence, originally failed before implementation.
- Selected public EMI setter, handled-screen inheritance, saved return target, screen-before-search ordering and optional-presence guard from real bytecode.
- Actual released `Guide.builder`, public extension registration, `Guides.getById`, native parsing, flow dispatcher, full block-page compilation and native link click callback. This runs with EMI present and absent.
- Native default extensions and the production guide title, disconnected-extension negative control, and same-identifier data-driven override with restoration.
- Selected mod-index bake evidence, native substring matcher execution, client-setup wiring and absence of bundled engine, EMI or test boundaries in the helper jar.

Two narrowly scoped classes exist only in `query-validation`: an audio field boundary avoids booting GuideMEClient's loader-dependent static initializer, and an index-storage field boundary avoids booting EMI's game registry. The compiler, registry, `LytFlowLink.mouseClicked`, `ModQuery` and Minecraft suffix matcher themselves come from the real selected artifacts. The fixture uses identity membership without a Minecraft item. It proves matching behavior, not the existence of live items. The compiled endpoint and return implementation are inspected, not invoked against a fabricated game client. Neither boundary is in the shipped helper.

Expected warnings occur for the deliberately disconnected native component negative control and headless terminal logging. An unsupported native component emits an error node directly instead of calling the probe sink's `appendError`; the negative control checks that no native link is produced.

## Reproduction

From the repository root, using the existing helper toolchain:

```sh
cd scripts/handbook-access
python prepare_query_dependency.py
JAVA_HOME="$PWD/toolchain/jdk-21.0.12.1+1" \
PATH="$PWD/toolchain/jdk-21.0.12.1+1/bin:$PATH" \
GRADLE_USER_HOME="$PWD/.gradle-user-home" \
./gradlew test build accessProbeClasspath -I access-probe.gradle --console=plain
python test_query_integration.py
python test_access_wiring.py
python test_open_endpoint.py
python verify_artifact.py
```

`prepare_query_dependency.py` obtains only the selected compile-only EMI dependency and checks its SHA512 against `mods/emi.pw.toml`. It does not install a mod. `build.sh` now includes this preparation and query test.

Evidence logs are under `scripts/handbook-access/build/query-integration`: `native-present.log`, `native-absent.log`, `native-mod-query.log` and `selected-mod-search-bytecode.log`.

The built artifact is `scripts/handbook-access/build/libs/astropunk-handbook-access-1.0.0.jar`. The artifact verifier prints its actual size and SHA256. It is build output only, not a live helper installation. The parent owns final packaging and should refresh the checksum after any further helper changes.
