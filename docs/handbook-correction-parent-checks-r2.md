# Parent selected-artifact checks after revision two

These checks were actually run on cached selected artifacts. They are not a game launch, runtime registry dump or rendered page review.

## Board operations: previous all-data scan was false

In FarmersDelight-1.21.1-1.3.4.jar, the missing operations are ordinary recipe resources in `data/farmersdelight/recipe/salvaging`, not a hypothetical hidden fallback:

- `salvaging/bricks.json`: `farmersdelight:cutting`, one `minecraft:bricks` gives four `minecraft:brick`, tool array accepts `pickaxe_dig` item ability or `minecraft:pickaxes`.
- `salvaging/nether_bricks.json`: corresponding four nether bricks, same tool classes.
- `salvaging/leather_armor.json`: helmet, chestplate, leggings or boots gives one leather, tool accepts `shears_dig` or `c:tools/shear`.
- `salvaging/leather_horse_armor.json`: gives two leather with the same shears tool.

The earlier writer scan missed these despite claiming every cached jar was scanned. Search by serializer and recursively inspect all recipe folders, rather than assuming the resource directory matches the workstation name. `CuttingBoardBlockEntity.javap.txt` shows processStoredItemUsingTool calls the recipe manager. `CuttingBoardBlock.javap.txt` shows placing an item and processing it in-world. There is no board screen in that interaction.

## Feast containers

`ModItems.javap.txt` is the selected ModItems registration class. All four feast `_block` identifiers and the four corresponding portion items are explicitly registered. The portion suppliers call `bowlFoodItem`, including the portions displayed as 'Plate of' in English. `FeastBlock.javap.txt` compares the item in hand against the portion's crafting remainder before serving. Display names are not evidence that a separate plate item is needed. The player uses a bowl for these four feasts. Check the helper before publishing final wording.

## Lunch containers

`FoodContainerItem.javap.txt` lines 439 through 496 show use while crouching calls openMenu. Non-crouching use calls processRightClick, starts eating if contents are not empty and the player can eat. This resolves more than just opening the container. It is not evidence for a guaranteed particular meal-selection order.

## Reinforced shulker capacities

Selected `reinforced-shulker-boxes-3.2.1+1.21.1.jar`, `atonkish.reinfshulker.util.ReinforcingMaterialSettings` static initializer passes the following values to registerReinforcingMaterial:

| Material | Value |
| --- | --- |
| copper | 45 |
| iron | 54 |
| gold | 81 |
| diamond | 108 |
| netherite | 108 |

Saved bytecode is `ReinforcingMaterialSettings.javap.txt`. The core registration and box inventory getter must establish that this parameter is the inventory size, rather than assuming that from the integer alone. Check pack overrides too.

## Parent draft gates

`revision2-parent-audit.json` records seven topics, fourteen localized bodies. GuideME 21.1.19 syntax parser passed all fourteen, including a malformed native-tag negative control. It does not validate registry identities, tag attribute semantics or game rendering.

- All grids have canonical adjacent ItemIcon children.
- Food utensils English wrongly links `farmersdelight:iron_axe`, Chinese links `minecraft:iron_axe`.
- Food End English has an ItemLink to `ends_delight:shulker_soup` missing from Chinese.
- Utensils feast section is table text only in both locales.
- Fishing condition section is table text only in both locales. It should be merged into the book explanation, not decorated with another arbitrary grid.
- All other non-vanilla item references have asset discovery hints, not proof of runtime registration.

## Scene label behavior

GuideME 21.1.19 `AnnotationTagCompiler` compiles BlockAnnotation child text into tooltip content. It is not a permanently visible label. The scene requires visible placement prose as well as useful hover identification. Exact selected bytecode was saved separately.
