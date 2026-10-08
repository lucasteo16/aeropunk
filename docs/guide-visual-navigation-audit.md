# GuideME 21.1.19 visual navigation and theme audit

## Recommendation

Use a resource-only image-card dashboard, with short category landing pages beneath it. Do not promise a movable mindmap, a selectable dark theme, or an arbitrarily deep sidebar in this release. Image links and wrapping rows are supported, but the sidebar renders only roots and their immediate children, and the client theme selector always returns `LIGHT_MODE`.[3][6][8]

建议先做图片卡片首页，再用分类页面逐层展开。21.1.19 的侧栏只显示顶层和下一层，主题选择固定为 `LIGHT_MODE`。真正可以拖动和缩放的节点思维导图需要自定义客户端界面，不能只靠资源包实现。[6][8][22]

## Evidence boundary

The release is GuideME 21.1.19 for Minecraft 1.21.1.[1] The inspected release tag resolves to commit `52334ccacf15d763ffe318281d38dca8ec7aaeb8`. All source citations below use that immutable commit, not the current branch.

The existing research download `guideme-21.1.19.jar` declares `Implementation-Version: 21.1.19`. Its SHA256 checksum is `2ce254edb931c3c3cf81d69abaf8f4ce5b871bf85e64984f366bf044173bd66a`, matching the digest returned by the official release asset endpoint. Released classes include `BoxTagCompiler`, `GuideNavBar`, `DataDrivenGuide`, `GuideQueryParser`, and `LytImage`. Direct class-file inspection found that `currentLightDarkMode()` consists of loading `LightDarkMode.LIGHT_MODE` and returning it. This independently confirms the important theme limitation in the tagged source.[1][8]

This is static source and released-binary inspection, not a rendered visual test. No installation, implementation, build, Minecraft launch, or commit was performed. Image click behavior is traced through compilation and event dispatch, not exercised in Minecraft.

The public authoring and data driven guide pages are moving documentation. Their descriptions of image resources, navigation parents, and custom symbolic colors agree with the release in the areas checked, but their later changes are not evidence that a feature shipped in 21.1.19.[23][24] 

The tagged documentation is also not sufficient by itself: the theme runtime and sidebar renderer expose limitations that the general authoring description does not explain.[6][8]

## Resource-only visual components

| Capability | Exact release finding | Design consequence |
|---|---|---|
| Clickable image tile | Markdown image children compile inside `LytFlowLink`; images become inline blocks. Event dispatch walks flow ancestors until a handler accepts the click.[3][22] | A Markdown link around an image is a supported image tile. A plain image is not a navigation button. |
| Native card component | Default tag registration has no `Card` compiler.[2] | Draw the card surface, border, and illustration into an image. Only the linked image footprint is the card hit target, not surrounding column whitespace. |
| Rows and columns | `Row` and `Column` accept `gap`, `alignItems`, and `fullWidth`. Rows use `LytHBox`, whose wrapping defaults to true.[4][27] | Arrange repeated small tiles in wrapping rows. These are content layouts, not browser layout containers. |
| General grid | No generic `Grid` compiler is registered. `ItemGrid` is an item showcase, not an arbitrary category-card grid.[2] | Use wrapping rows for the dashboard. Do not assume fixed grid tracks or automatic equal-height cards. |
| Image dimensions | `LytImage` divides source dimensions by four, then proportionally shrinks an image that exceeds available width.[5] | Prepare consistent source dimensions. Ordinary Markdown images have no checked author-controlled width or height attributes. |
| Category lists | `SubPages` lists immediate navigation children and can include their item icons. `CategoryIndex` produces a text list, not cards.[17][2] | Use cards at entry points and compact child lists deeper down. |
| Links and tooltips | Markdown links and the `a` compiler support page destinations and optional tooltip titles.[3][19] | Keep destination paths explicit. A tooltip is not a browser hover animation. |

A card dashboard is a sequence of laid-out links in a vertically scrolling document. A true spatial mindmap preserves node positions and connecting edges in a two-dimensional coordinate space, supports dragging the viewport and zooming around a focal point, and translates pointer coordinates back into node coordinates. The released document screen provides vertical document scrolling, not that canvas behavior.[22] The built-in `GameScene` tag is a separate scene feature, not a category-node graph compiler.[2]

## Homepage and category depth

The default start page is `index.md`. The released Java builder exposes `startPage(ResourceLocation)`, but the resource guide definition codec has only `item_settings`, `default_language`, and `custom_colors`. Do not invent a resource `start_page` setting.[16][9]

Navigation `parent` relationships build a recursive tree, and nodes are sorted by position and title.[18] That does not mean the sidebar displays the full tree. `GuideNavBar.recreateRows()` adds root rows and one loop over their children, without recursively adding grandchildren.[6]

Deeper categories can still be opened through explicit page links and successive `SubPages` landing pages.[3][17]

The sidebar has no verified resource setting to hide it only on the homepage. `GuideScreen` creates it unconditionally and pins it when the scaled screen is wide enough. Narrow layouts use the hover-open strip.[7][6] With no navigation nodes anywhere, `GuideNavBar` skips rendering, but `GuideScreen` still reserves sidebar space when pinned. Removing navigation metadata is therefore not equivalent to a full-width, sidebar-free homepage, and it also removes the tree that `SubPages` uses.[6][7][17]

Recommendation: retain a shallow sidebar as a secondary route. Use category pages to carry the deeper hierarchy. If homepage-only sidebar suppression and recovery of its width are mandatory, that requires a client layout change, not frontmatter.

## Theme and styling

| Area | Resource-only scope in 21.1.19 | Requires client code or has a limitation |
|---|---|---|
| Text accents | `custom_colors` defines symbolic colors with `dark_mode` and `light_mode`; pages can use the `Color` tag.[9][2] | This adds named text colors, not a stylesheet or a complete screen theme. |
| Dark and light selection | Both variants exist in color representations.[9][29] | `GuideMEClient.currentLightDarkMode()` always returns `LIGHT_MODE`; no theme toggle is defined in the inspected client configuration.[8] |
| Screen background | A resource pack can replace the shared `guideme:background` sprite selected by `GuiAssets`.[15] | The screen tints it with `GUIDE_SCREEN_BACKGROUND` and overlays the document rectangle with the fixed color `0x40333333`. This is not a per-guide background property.[7] |
| Card backgrounds | Bake the background and border into each linked image.[3][5] | No released generic card background, corner radius, shadow, or hover stylesheet is registered.[2] |
| Fonts | Minecraft font resources can be replaced through ordinary resource packs. Guide body styling selects `Minecraft.UNIFORM_FONT`; primary headings select `Minecraft.DEFAULT_FONT`.[14] | No per-guide resource font setting is present in `DataDrivenGuide`. Replacing shared fonts affects other consumers. Custom local typography needs Java text styles or a custom compiler.[9][14] |
| Text sizing | Standard headings use predefined scales. Item and block illustrations have their own tag compilers.[14][2] | No browser-style universal font-size attribute or stylesheet was found in the default tag set.[2][4] |
| Screen sizing | Client settings include `adaptiveScaling` and `fullWidthLayout`; the document screen has a maximum centered width and adaptive scaling logic.[8][22] | These are client presentation settings, not dashboard zoom or resource-defined canvas dimensions. |
| Icons | Navigation metadata supplies item icons; `SubPages` can display them. Item images can serve as additional illustrations.[6][17][2] | Arbitrary category artwork belongs in page image resources, not an assumed image-file navigation-icon field. |

The internal symbolic screen colors are not automatically overridable through `custom_colors`. The resource map is registered as a `SymbolicColorResolver`, whereas the screen passes enum values directly to rendering.[10][7][29] Use named colors for authored text and image artwork for visual surfaces. Do not describe this as browser-like cascading style sheets.

The light-mode name does not imply a pale page. The built-in screen background and body colors are largely the same in both variants, and the actual released screen already uses a dark backdrop.[29][7] Design the first prototype for the observed released palette rather than promising two selectable themes.

## English queries under Simplified Chinese

Keep English pages at the baseline paths, use `default_language` with `en_us`, and place Simplified Chinese equivalents under `_zh_cn` while preserving logical page paths. The loader discovers baseline pages first, substitutes the selected-language page when available, and otherwise keeps the baseline page. A translation without its baseline page is not a reliable independent discovery route.[10]

The guide indexes the pages selected for the current load, not every translation of every page. Chinese replacements therefore do not automatically retain the English original text in the search index.[10][11] `zh_cn` maps to `CJKAnalyzer`. The query parser searches the language-specific title and body fields for every language currently indexed; it does not simply restrict matches to the interface locale.[13][12]

For predictable English discoverability on a Chinese page, include explicit English aliases in visible prose, image alternative text, or Markdown link titles. `PageIndexer` indexes ordinary text, image alternative text and titles, and link titles. Arbitrary frontmatter alias fields are not indexed by that code.[21] `ItemLink` displays the current translated item name, but its compiler does not override the default indexing method to add that generated name. Do not rely on a self-closing `ItemLink` to provide English search aliases.[20][25]

Suggested visible alias line: `搜索词：Mechanical Press, Water Wheel, Stress Capacity`.

Latin aliases inside Chinese content can be queried through the Chinese analyzer, and English fallback pages can be searched through their English fields. Exact token behavior, multiword ordering, prefixes, result ranking, and highlighted snippets still require later in-game acceptance checks. Source inspection supports the design, not a guarantee for every query.[11][12][13]

This is GuideME page search. It does not establish English item-browser matching under a Chinese locale, nor automatically change an external recipe browser's query.[11] Only English and Simplified Chinese content are recommended here.

## Client bridge boundary

A genuine mindmap needs a custom client screen or interactive graph component with node and edge data, viewport state, pan and zoom input handling, hit testing, readable labels, and return-state preservation. The released extension route is `GuideBuilder.extension` with `TagCompiler.EXTENSION_POINT`; a custom tag compiler can create custom layout content. `GuideUiHost.navigateTo(PageAnchor)` supplies the link back into guide pages.[16][25][26] These hooks are extension points, not a shipped mindmap implementation.

A standalone client screen is the cleaner candidate if the homepage must suppress all guide chrome and occupy the viewport. An embedded custom component could keep ordinary guide navigation but would still need custom input and rendering. Neither approach is resource-only. Registration must also respect the released resource guide precedence: resource definitions with the same guide identifier are loaded before static guides, so an extended static guide cannot be assumed to win.[10]

Likewise, the default tag list does not contain automatic Ponder or EMI action connectors.[2] Embedded guide recipes, commands, page links, and scenes should not be presented as external action integration. Any such bridge needs its own released endpoint audit and screen-return contract.

## Smallest attractive homepage prototype

This is a proposed later prototype, not an implementation in this audit.

- Create one `index.md` with a small brand illustration, a short introduction, and six equal-size illustrated category tiles. Suggested names are Getting started, Building, Power, Automation, Exploration, and Troubleshooting. Suggested Simplified Chinese labels are 入门、建造、动力、自动化、探索、故障排查.
- Use a wrapping `Row` with a `Column` per tile. Put a Markdown-linked image and a separate linked text label in each column. Keep text live rather than baking it into artwork, so both locales remain readable and searchable. No native `Card` or generic `Grid` is assumed.[3][4][27]
- Start with tile artwork measuring 480 by 256 source pixels, which the released image layout initially presents at 120 by 64 before any width reduction. This is a proposed size chosen around the verified fourfold reduction, not a tested responsive specification.[5]
- Use a charcoal image surface with one restrained copper accent, consistent illustration crops, and sufficient empty space. Retain the released screen palette and use a custom symbolic accent only for selected authored text.[9][7]
- Create six category landing pages, each with a sentence explaining its scope and a short child list. Add one deeper path, Automation, Transport, Item routing, to demonstrate depth beyond the sidebar. Prefer shallow secondary sidebar entries and explicit page navigation for deeper levels.[6][17]
- Supply English baseline pages, matching `_zh_cn` translations, and a short English alias line on Chinese detail pages. Keep artwork shared unless a translated image is necessary.[10][21][28]

Later approval checks should cover image and label click targets, narrow-screen wrapping, the wide-screen sidebar width, repeated category descent and return navigation, Chinese glyph readability, English alias queries under `zh_cn`, and resource reload behavior. Dark-mode switching, graph interaction, Ponder actions, and EMI actions remain outside this smallest prototype.

## Sources

[1] https://github.com/AppliedEnergistics/GuideME/releases/tag/v21.1.19
[2] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/extensions/DefaultExtensions.java
[3] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/compiler/PageCompiler.java
[4] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/compiler/tags/BoxTagCompiler.java
[5] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/document/block/LytImage.java
[6] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/screen/GuideNavBar.java
[7] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/screen/GuideScreen.java
[8] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/GuideMEClient.java
[9] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/datadriven/DataDrivenGuide.java
[10] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/GuideReloadListener.java
[11] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/search/GuideSearch.java
[12] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/search/GuideQueryParser.java
[13] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/search/Analyzers.java
[14] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/document/DefaultStyles.java
[15] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/render/GuiAssets.java
[16] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/GuideBuilder.java
[17] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/compiler/tags/SubPagesCompiler.java
[18] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/navigation/NavigationTree.java
[19] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/compiler/tags/ATagCompiler.java
[20] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/compiler/tags/ItemLinkCompiler.java
[21] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/search/PageIndexer.java
[22] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/screen/DocumentScreen.java
[23] https://guideme.appliedenergistics.org/authoring
[24] https://guideme.appliedenergistics.org/data-driven-guides
[25] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/compiler/TagCompiler.java
[26] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/ui/GuideUiHost.java
[27] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/document/block/LytHBox.java
[28] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/internal/MutableGuide.java
[29] https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/src/main/java/guideme/color/SymbolicColor.java
