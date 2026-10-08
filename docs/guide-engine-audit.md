# Guide engine audit

## Recommendation

Use GuideME 21.1.19 for the spacious, scrolling sandbox handbook, with one separate client-only NeoForge bridge and resource-pack pages. This is a source-supported design, not a tested integration. Patchouli 1.21.1-93-neoforge costs less for a conventional book with an inventory button, but less closely matches the requested interface. Modonomicon 1.21.1-1.120.7 offers the strongest built-in topic graph, but its server-loaded books and page serialization make it a worse fit for a small client-only extension.[1][2][3]

The bridge can cover item recipes, uses, search text, item-associated Ponder scenes, and explicitly registered help-screen adapters. It cannot promise arbitrary mod help screens or exact Ponder scene selection without further endpoint inspection. Keep those actions conditional, with readable unavailable states. Do not represent a resource pack as executable integration code.

## Scope and release evidence

Only public source, published archives, checksums, metadata and static class signatures were inspected. No mods were installed, no pack manifests were changed, no implementation was built, no game was launched and no commit was made.

All downloaded engine binaries and the Modonomicon source archive matched the SHA512 values in `research/astropunk-guidance/presentation-releases.json`. The selected EMI and Create binaries matched the checksums in this worktree's pack metadata. Source archives for GuideME and Patchouli were fetched at their release-tag revisions. Released GuideME extension signatures and EMI entry points were also checked directly in their binaries.

| Component | Exact identity | Evidence |
|---|---|---|
| GuideME | `21.1.19`, Modrinth `hFpGwC6q` | Tag `v21.1.19` resolves to `52334ccacf15d763ffe318281d38dca8ec7aaeb8`. Binary declares Minecraft `[1.21.1]` and NeoForge `[21.1.1,)`.[1][6] |
| Patchouli | `1.21.1-93-neoforge`, Modrinth `BIogJv2D` | Tag `release-1.21.1-93` resolves to `0c2fdffc7e611a828007cecae7bfc3d7b312040a`. Binary declares Minecraft `[1.21.1,1.21.2)`.[2][7] |
| Modonomicon | `1.21.1-1.120.7`, Modrinth `fbS7CiY6` | Matching publisher source archive inspected directly. Binary internal version is `1.120.7`. No release commit was established from the first tag listing, so the immutable version download and verified source archive are the authority here.[3][8] |
| EMI | `1.1.24+1.21.1+neoforge`, Modrinth `5sIPA1To` | `mods/emi.pw.toml`. Source tag `1.1.24+1.21.1` resolves to `322171ee1d85cb1809bb7afd23d432b685756247`; NeoForge binary signatures confirm the names below.[4][9] |
| Create | `1.21.1-6.0.10`, Modrinth `UjX6dr61` | `mods/create.pw.toml`. Binary requires NeoForge `[21.1.219,)` and bundles `ponder-neoforge-1.0.82+mc1.21.1.jar`.[5] |

There is no separate `mods/ponder.pw.toml` in the inspected worktree. Ponder is present inside Create's jar-in-jar metadata, not missing. The bundled version is the inspected baseline; a separately supplied newer Ponder could supersede it at loading time.[5]

Current GuideME documentation contains newer mapping names such as `Identifier.parse`. For this target, use the released `ResourceLocation` signatures instead. Do not copy current examples unchanged.[1][10]

## Capability classification

Built-in means shipped in the named release. Bridge means the engine exposes the necessary extension and the selected target has a callable entry point, but the connector is not shipped. Unverified means the available evidence does not establish the complete requested action.

| Requirement | GuideME 21.1.19 | Patchouli 93 | Modonomicon 1.120.7 |
|---|---|---|---|
| Spacious scrolling content | Built-in document layout, sidebar, scrolling and independent scale.[1] | Built-in book pages, not a free scrolling document. Replacing the overall interface is outside a small component bridge.[2] | Built-in node and index views, single and double entry pages. Good topic map, not GuideME's document model.[3] |
| Custom clickable text | Bridge using `LytFlowLink.setClickCallback`.[1] | Bridge using `ICustomComponent.mouseClicked` in templates.[2] | Custom page renderer bridge; custom page types also require loaders and network serialization.[3] |
| Custom tags and buttons | Public `TagCompiler.EXTENSION_POINT`, `GuideBuilder.extension`, `LytWidget(AbstractWidget)` are built-in extension hooks. Actual pack actions require bridge code.[1][6] | Built-in templates and `patchouli:custom` component mechanism load a named Java class. `IComponentRenderContext.registerButton` provides callbacks.[2] | Built-in `LoaderRegistry.registerPageLoader` and `PageRendererRegistry.registerPageRenderer`, rather than GuideME-style custom inline tags.[3] |
| EMI recipes and uses | Bridge. No native EMI connector was found in released default extensions.[1][4] | Bridge. Do not treat the built-in recipe pages or JEI integration as verified EMI action buttons.[2][4] | Bridge. Same distinction between inline recipe display and opening EMI.[3][4] |
| Set and display EMI query | Bridge for all three. Setting text alone does not open an item-browser screen.[4][9] | Bridge | Bridge |
| Open Create Ponder | Bridge to item-associated Ponder interface. Exact individual scene targeting remains unverified.[5] | Same endpoint bridge | Same endpoint bridge |
| Open other mod help | Bridge per verified mod adapter. Universal help-screen opening is unsupported as a generic promise. | Same limitation | Same limitation |
| Inventory button without carried item | Bridge. Built-in hold-G action requires a hovered item with an indexed guide page; it is not an always-visible home button.[1] | Built-in opt-in `inventoryButtonBook`, empty by default. Does not require owning the book.[2] | No stock inventory home button established from inspected source. Bridge required.[3] |
| Pause-menu button | Bridge for all three. No built-in button established in the inspected releases. | Bridge | Bridge |
| Permission-free local opening | `GuidesCommon.openGuide` takes the local player and opens locally; client `guidemec` opening has no permission predicate.[1] | Client `PatchouliAPI.get().openBookGUI(bookId)` and inventory callback are item-free local paths.[2] | Local `BookGuiManager.openBook(BookAddress)` exists, but the book must already be loaded and built.[3] |
| English and Chinese | Built-in translated-page selection, default-page fallback and Chinese search analyzer.[1] | Built-in localized entry files with English fallback, or translation keys; search is narrower.[2] | Built-in Minecraft translation keys and localized text search. Book data itself is server loaded.[3] |

## Exact GuideME extension boundary

Register one guide through `Guide.builder(guideId)` and attach a `TagCompiler` through `GuideBuilder.extension(TagCompiler.EXTENSION_POINT, compiler)`. The compiler declares its names with `getTagNames`, handles block and inline contexts separately, and can supply searchable text through `index`. Emit `LytFlowLink` for inline actions or `LytWidget` for normal Minecraft buttons. `LytWidget` forwards pointer events and adjusts document coordinates. Keyboard focus, narration and clipping of custom widgets still need prototype verification.[1][6]

The released ordinary link parser supports page links and web links using `http` or `https`. It does not implement an arbitrary action-protocol dispatcher. Invented links such as `emi:search` will not become working integrations merely by appearing in Markdown. Use the custom tag hook instead.[1]

Proposed tag names such as `EmiRecipes`, `EmiUses`, `EmiSearch`, `Ponder` and `ModHelp` would belong to the bridge, not GuideME. Keep attributes limited to validated item identifiers, recipe identifiers, queries and adapter names. Never expose reflection, arbitrary class names, server commands or scripts to page authors.

Important registration trap: data-driven guide definitions in `assets/<namespace>/guideme_guides/<guide>.json` build their own default extensions. The released loader can prefer a data-driven guide over a statically registered guide with the same identifier. Do not add a competing guide definition for the bridge-owned guide. Register the extended guide in code and distribute only its content and assets through the resource pack.[1]

## Target action constraints

### EMI

The selected binary exports `EmiApi.displayRecipes(EmiIngredient)`, `displayUses(EmiIngredient)`, `displayRecipe(EmiRecipe)` and `setSearchText(String)`. Resolve item identifiers into real stacks and wrap them with `EmiStack.of`. Resolve explicit recipe identifiers through the recipe manager rather than inventing identifiers from output items.[4][9]

The release source's `setPages` creates an inventory screen when there is no handled screen. A guide screen is not a handled inventory screen, so opening recipes from the guide can discard the guide as the immediate return target. Preserve guide identifier, page, anchor and scroll state in the bridge if a return button is required. Empty recipe collections produce no new screen. The bridge should show a useful missing-recipe state instead of silently doing nothing.[4]

`setSearchText` only changes the field. A search action must also open an appropriate inventory screen while a player is present. It does not supply a standalone search-window operation. Recipe viewing and searching do not require cheat mode; never use item-giving or server-command paths.[4]

Prefer stable queries based on mod identifiers such as `@create`, and item-based recipe buttons, rather than translated display names. Human-readable queries can vary with Minecraft language and EMI indexing. A translated guide is not proof that every English query finds the same Chinese items. Do not automatically translate arbitrary EMI query syntax.

### Create and Ponder

In bundled Ponder `1.0.82+mc1.21.1`, public static `net.createmod.ponder.foundation.ui.PonderUI.of(ResourceLocation)` and `of(ItemStack)` return a Ponder interface. `PonderIndex.getSceneAccess()` is also exported. These establish an item-oriented screen bridge; they do not establish an arbitrary scene-identifier constructor. `PonderUI` lives under `foundation`, not the formal `api` package, so this is a version-sensitive integration.[5]

Opening the returned interface through the client screen system is the proposed connector. Confirm missing scenes, Create addon registration and Catnip navigation before promising reliable return behavior. Embedding live Ponder inside a GuideME document was not verified. GuideME's own structure scenes are a separate built-in feature, not a substitute for Create's narrated scenes.[1][5]

### Other help screens and buttons

Use a fixed adapter registry keyed by help topic. Each adapter must inspect that mod's selected release, check availability and call its local opening method. Patchouli-backed help can use its public client opening method when the book identifier is verified. A mod with no opening hook may need a larger integration; do not call that automatically small.[2]

Use client screen initialization events for new inventory and pause buttons, rather than replacing existing buttons. GuideME's server `guide` command has an operator permission predicate, so it is not the access route. Use local guide opening. Disable world-dependent actions at the main menu or without a player.[1]

Patchouli's built-in inventory integration replaces the first `ImageButton` it finds, including the normal recipe-book location. This saves code but carries a coexistence cost. Preserve the ordinary recipe button when assessing the lowest-cost option.[2]

## Language paths and search

For bridge guide identifier `aeropunk:handbook`, the default English page would be `assets/aeropunk/guides/aeropunk/handbook/index.md`. Its Simplified Chinese translation would be `assets/aeropunk/guides/aeropunk/handbook/_zh_cn/index.md`. Keep stable page identifiers and anchors between languages. Root pages are the English originals; an `_en_us` folder is not required. Missing Chinese pages fall back independently to the default file. A translation-only page without a default counterpart is not a reliable discovery path, because the loader enumerates original pages and then selects translations.[1][11][12]

GuideME's released `Analyzers` maps `en_us` to its English analyzer and `zh_cn`, `zh_hk`, `zh_tw` to Lucene `CJKAnalyzer`. Unknown language codes are treated as English. The search index contains the selected translated or fallback version of each page, not both complete languages simultaneously. Its parser searches the indexed language fields, so English fallback pages can remain searchable in a Chinese session, but English synonyms absent from translated text are not automatically supplied. Add bilingual terminology deliberately where useful. Search returns at most 25 hits, and parse failures return an empty result list.[1]

Patchouli entry paths use `assets/<namespace>/patchouli_books/<book>/en_us/entries/<entry>.json` and the corresponding `zh_cn` path. The English entries are the discovery baseline; loading tries the active-language file then the original. An `i18n` book can instead use keys in `assets/<namespace>/lang/en_us.json` and `zh_cn.json`. Released entry search checks localized names and associated item names, rather than GuideME's full-page Lucene index.[2]

Modonomicon book definitions use `data/<namespace>/modonomicon/books/`, with text keys in `assets/<namespace>/lang/en_us.json` and `zh_cn.json`. `BookTextHolder` resolves strings through Minecraft `I18n`, and text pages search localized title and text with substring matching. Provide English translation keys so missing Chinese keys have a useful fallback. Its default font fallback locales include `zh_cn`, `ja_jp` and `ko_kr`; Traditional Chinese font behavior needs its own gate.[3]

## Client-only feasibility and cost

The separate GuideME action bridge can be client-only: no new items, registries, gameplay state, server packets or permission checks are needed for these local actions. Register it only on the client and keep optional EMI, Ponder and other help adapters isolated from class loading when absent. Content updates should remain resource-pack changes, not bridge rebuilds.

This does not make GuideME itself client-only. The released engine registers an item, a data component, command argument types and a non-optional play-to-client payload. Its publisher classifies it for client and server. Retain normal engine installation on both sides for the proposal; a client-only engine installation was not verified and is not implied by the client-only bridge.[1][6]

Patchouli likewise needs a registered book definition: a resource pack alone is not the normal complete creation path. The release discovers `data/<modid>/patchouli_books/<book>/book.json` in mod roots, plus its external book folder, while client content can live in resources. A small integration can supply that definition and custom components. This is the lowest cost if book pages and its replacement inventory button are acceptable.[2]

Modonomicon loads definitions through its server data listener and synchronizes books to clients. Its client reload listener clears font and rendering caches but does not load the resource JSON into the book registry. Custom page types require a JSON loader, network loader and renderer. A client-only renderer over existing page types is plausible, but a new custom page type is not established as a client-only resource-pack feature. That is a material cost disadvantage for this handbook.[3]

Maximum flexibility for this request belongs to GuideME's document extension points. Maximum built-in node-map flexibility belongs to Modonomicon. Lowest initial book-authoring cost belongs to Patchouli. None offers every requested external action as resource-only content.

## Licensing and maintenance

GuideME's release license is GNU Lesser General Public License version 3, with embedded Markdown code under the MIT license and Lucene under Apache License version 2. A separate application using the public interfaces is distinguished from an engine fork by the license itself. Preserve notices and review distribution obligations rather than copying engine internals.[1]

Patchouli declares Creative Commons Attribution NonCommercial ShareAlike 3.0. Modonomicon declares `MIT AND CC-BY-4.0`, with its Java source marked MIT. Review the relevant code and artwork separately; neither engine's license automatically grants rights to reused mod screenshots or translated third-party prose.[2][3][7][8]

Modrinth project downloads at retrieval were GuideME 3,165,689, Patchouli 35,651,289 and Modonomicon 1,332,448. These are provider-specific adoption signals, not unique players or compatibility measurements. The existing release snapshot records respective exact-release downloads of 41,378, 704,846 and 13,873; these snapshot counts were not refreshed. CurseForge counts were not collected.[13][14][15]

Keep the bridge dependency surface narrow. GuideME's public tag and widget hooks reduce the need for a fork, but Ponder's `foundation` opening class and per-mod help hooks remain maintenance liabilities. Recheck signatures whenever selected endpoint versions change. GuideME 21.1.19's published notes mention startup-crash fixes, so release status alone is not evidence that this assembled pack has passed startup.

## Prototype acceptance gates

These are proposed future tests, not tests performed by this audit.

1. Compile against the exact released GuideME, EMI and bundled Ponder signatures without newer Minecraft mapping names or engine patches. Keep the bridge absent from dedicated-server exports while the engine remains installed normally.
2. Open the handbook from inventory and pause menus in survival, with an empty inventory, cheats disabled and a non-operator multiplayer account. Preserve vanilla controls and avoid command permission paths.
3. Exercise custom inline links and visible buttons at small and large interface scales, including scrolled pages. Confirm pointer hit boxes, keyboard focus, narration and clipping before approving the widget design.
4. Open recipes, uses and one explicit recipe from real selected items. Handle missing items, empty results and late recipe indexing. Return to the original guide page and scroll position instead of trapping the user in inventory.
5. Set an EMI query and visibly open its results, rather than merely changing hidden text. Check stable mod queries and localized name queries in both English and Simplified Chinese.
6. Open a known Create item scene and a verified addon item scene using the bundled Ponder release. Handle an item with no scene. Verify navigation back to the guide. Treat direct scene selection as optional until an exact supported endpoint is established.
7. Verify at least one real selected mod help adapter without an item or server command. Disable unavailable help actions cleanly. Do not approve a universal help action from one successful adapter.
8. Switch between `en_us` and `zh_cn`, leave one Chinese page untranslated, and confirm independent English fallback, stable links, anchors and readable fonts. Check Chinese search, mixed-language fallback search and retained English terminology.
9. Reload the resource pack without rebuilding the bridge. Confirm custom tags remain attached, content refreshes and no competing data-driven guide replaces the extended guide.
10. Join a normal server with a client-only bridge and confirm there is no new bridge handshake or server dependency. Separately test optional target removal and stale identifiers without a client crash.

Stop the prototype if satisfying these gates requires replacing GuideME's whole screen, reflective dispatch, engine patches or server gameplay state. Reassess scope rather than silently turning a small bridge into a custom handbook engine.

## Source navigation

Source citations use immutable release roots or exact version archives. Within GuideME's root, inspect `src/main/java/guideme/GuideBuilder.java`, `compiler/TagCompiler.java`, `compiler/LinkParser.java`, `document/flow/LytFlowLink.java`, `document/interaction/LytWidget.java`, `internal/GuideReloadListener.java`, `internal/search/Analyzers.java`, `internal/search/GuideSearch.java`, `internal/hotkey/OpenGuideHotkey.java`, `internal/GuideMEClientProxy.java` and `internal/GuideME.java`.[1]

Within Patchouli's root, inspect `Xplat/src/main/java/vazkii/patchouli/api/ICustomComponent.java`, `IComponentRenderContext.java`, `PatchouliAPI.java`, `client/book/template/component/ComponentCustom.java`, `client/book/BookContentsBuilder.java`, `client/book/BookEntry.java`, `common/book/BookRegistry.java`, `mixin/client/MixinInventoryScreen.java` and `NeoForge/src/main/java/vazkii/patchouli/neoforge/common/NeoForgePatchouliConfig.java`.[2]

Within the Modonomicon source archive, inspect `com/klikli_dev/modonomicon/data/LoaderRegistry.java`, `BookDataManager.java`, `client/render/page/PageRendererRegistry.java`, `client/gui/BookGuiManager.java`, `book/BookTextHolder.java`, `book/page/BookTextPage.java` and `config/ClientConfig.java`.[3]

EMI's behavior comes from `xplat/src/main/java/dev/emi/emi/api/EmiApi.java`; source uses intermediary-facing mapping names while the NeoForge binary confirms Mojang-facing stack and screen types. Ponder opening signatures were read from the exact nested archive's class method tables, not inferred from current Create documentation.[4][5][9]

## Sources

[1] https://github.com/AppliedEnergistics/GuideME/tree/52334ccacf15d763ffe318281d38dca8ec7aaeb8
[2] https://github.com/VazkiiMods/Patchouli/tree/0c2fdffc7e611a828007cecae7bfc3d7b312040a
[3] https://cdn.modrinth.com/data/692GClaE/versions/fbS7CiY6/modonomicon-1.21.1-neoforge-1.120.7-sources.jar
[4] https://github.com/emilyploszaj/emi/tree/322171ee1d85cb1809bb7afd23d432b685756247
[5] https://cdn.modrinth.com/data/LNytGWDc/versions/UjX6dr61/create-1.21.1-6.0.10.jar
[6] https://cdn.modrinth.com/data/Ck4E7v7R/versions/hFpGwC6q/guideme-21.1.19.jar
[7] https://cdn.modrinth.com/data/nU0bVIaL/versions/BIogJv2D/Patchouli-1.21.1-93-NEOFORGE.jar
[8] https://cdn.modrinth.com/data/692GClaE/versions/fbS7CiY6/modonomicon-1.21.1-neoforge-1.120.7.jar
[9] https://cdn.modrinth.com/data/fRiHVvU7/versions/5sIPA1To/emi-1.1.24%2B1.21.1%2Bneoforge.jar
[10] https://guideme.appliedenergistics.org/integration
[11] https://guideme.appliedenergistics.org/translation
[12] https://guideme.appliedenergistics.org/authoring
[13] https://api.modrinth.com/v2/project/guideme
[14] https://api.modrinth.com/v2/project/patchouli
[15] https://api.modrinth.com/v2/project/modonomicon
