# Guide engine decision and visual production policy

## Recommendation

Choose GuideME 21.1.19 with a small client integration for the item-icon homepage and contextual actions. Modonomicon is preferable if a native draggable node map is the overriding requirement; GuideME is preferable for spacious visual teaching and maintainable content. This is the recommended decision, not an installation or runtime certification.

The supplied first screenshot shows Modonomicon's native node navigation, but its second screenshot shows the compact book pages used for recipes. The third screenshot demonstrates a detailed three-dimensional machine scene; the fourth demonstrates Chinese text, item icons, recipes and a dense scrolling document. These latter teaching layouts align with the requested guide more closely than compact book spreads.

## Production policy

Lucas is not responsible for supplying images, building demonstration structures, translating pages, entering recipes or assembling guide content. These are agent-owned tasks. Existing items and blocks should be rendered by the game rather than painted as tutorial illustrations.

Generated artwork is allowed only for decorative backgrounds, branding, icons and theme surfaces. It is prohibited for instructional machine layouts, item appearances, recipes, wiring, vehicle construction or any visual used as evidence of gameplay behavior.

Prefer live item and block rendering, real recipe data, declaratively authored three-dimensional scenes, existing Ponder demonstrations and verified screenshots. Structure scenes can be defined from block identifiers and states or imported from structure files. They are illustrative models, not evidence of working machinery. Validate functional examples separately when gameplay testing is authorized.

A visual that cannot be captured or verified must remain an explicit pending item. Do not invent a plausible illustration or ask Lucas to create assets as the routine fallback. Report actual environmental or access blockers honestly; do not promise that every automated rendering or client-validation step is guaranteed to succeed.

## Built-in content references

The following features are documented in the exact GuideME release source at revision 52334ccacf15d763ffe318281d38dca8ec7aaeb8:

- ItemImage and BlockImage render actual game items and blocks, including block states.
- ItemLink displays localized item text and links to the assigned guide page. Recipe slots can reference those pages too.
- RecipeFor, RecipesFor and Recipe display real registered recipes. Custom machine recipe types need explicit support.
- ItemGrid displays related item icons. Row and Column arrange content.
- SubPages and CategoryIndex derive link lists from page metadata.
- KeyBind displays the player's actual binding rather than assuming a fixed key.
- GameScene displays an illustrative three-dimensional scene with blocks, entities and imported structures.
- BlockAnnotation, BoxAnnotation, LineAnnotation and DiamondAnnotation mark scene elements and carry explanatory tooltips.
- Markdown page links, search and localized files provide reference navigation.

These capabilities are documented and source-supported, not exercised in this pack. EMI search and recipe-screen actions, Ponder opening, persistent guide buttons and a spatial category homepage require the separate client integration.

## References

https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/docs/docs/30-authoring/index.md

https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/docs/docs/30-authoring/game-scenes.md

https://github.com/AppliedEnergistics/GuideME/blob/52334ccacf15d763ffe318281d38dca8ec7aaeb8/docs/docs/20-integration/custom-tag.md
