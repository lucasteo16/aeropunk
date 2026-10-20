---
navigation:
  title: "Bulk storage"
  position: 2
  parent: reference.machines-storage.md
  icon: create:item_vault
---

# Bulk storage

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+mod+item+vault+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E7%89%A9%E5%93%81%E4%BB%93%E5%BA%93+%E6%95%99%E7%A8%8B)

## Vault capacity

<EmiSearch query="@create" />

An <ItemLink id="create:item_vault" /> is bulk factory storage. Connected vault blocks form one store, and this pack gives every block 20 stacks of capacity.

<Recipe id="create:crafting/kinetics/item_vault" />

A vault has a square cross section up to three blocks wide, and it grows in length up to three times that width. Capacity follows the formed block count.

| Vault shape | Blocks | Capacity |
| --- | --- | --- |
| One by one by one | 1 | 20 stacks |
| Two by two cross section, six blocks long | 24 | 480 stacks |
| Three by three cross section, nine blocks long | 81 | 1620 stacks |

There is no chest screen. Contents cannot be added or removed by hand, so every item enters and leaves through an item transfer component on a face.

***

## First vault

1. Place a chest and a hopper directly above it, pointing down into the chest.
2. Put one vault block directly above that hopper, then another hopper above the vault, also pointing down.
3. Put a few items into the upper hopper. It inserts into the vault, while the lower hopper extracts into the chest.
4. Open the chest to confirm the items arrive. For storage rather than continuous transfer, lock the lower hopper with redstone when you want to retain the contents.

Success looks like items leaving the vault into the chest through the lower hopper. There is no vault inventory window to open.

| Part | View | Role |
| --- | --- | --- |
| <ItemLink id="create:item_vault" /> | <ItemGrid><ItemIcon id="create:item_vault" /></ItemGrid> | Bulk item storage |
| <ItemLink id="minecraft:hopper" /> | <ItemGrid><ItemIcon id="minecraft:hopper" /></ItemGrid> | Inserts from above or extracts from below, output points into the receiving container |
| <ItemLink id="minecraft:chest" /> | <ItemGrid><ItemIcon id="minecraft:chest" /></ItemGrid> | Receives the extracted items |
| <ItemLink id="create:brass_funnel" /> | <ItemGrid><ItemIcon id="create:brass_funnel" /></ItemGrid> | Filtered insert or extract on one face |
| <ItemLink id="create:chute" /> | <ItemGrid><ItemIcon id="create:chute" /></ItemGrid> | Vertical item movement |

For expansion and automation layouts, open the Item Vault Ponder lessons Dimensions of an Item Vault and Storing Items in Vaults.

***

## Other installed storage families

<EmiSearch query="@create_connected" /> <EmiSearch query="@create_vibrant_vaults" />

| Storage block | View | Role |
| --- | --- | --- |
| <ItemLink id="create_connected:item_silo" /> | <ItemGrid><ItemIcon id="create_connected:item_silo" /></ItemGrid> | Vertical bulk item storage |
| <ItemLink id="create_vibrant_vaults:shipping_container" /> | <ItemGrid><ItemIcon id="create_vibrant_vaults:shipping_container" /><ItemIcon id="create_vibrant_vaults:vertical_shipping_container" /></ItemGrid> | Container-styled vault variants |
| <ItemLink id="create_vibrant_vaults:basic_shipping_container" /> | <ItemGrid><ItemIcon id="create_vibrant_vaults:basic_shipping_container" /><ItemIcon id="create_vibrant_vaults:vertical_basic_shipping_container" /></ItemGrid> | Basic container variants |
| <ItemLink id="create_vibrant_vaults:vertical_item_vault" /> | <ItemGrid><ItemIcon id="create_vibrant_vaults:vertical_item_vault" /></ItemGrid> | Tall vault for a narrow room |

Colours and container skins change appearance, not the item capacity rule. The fluid branch is separate from item storage and does not add item capacity.

| Fluid storage | View | Role |
| --- | --- | --- |
| <ItemLink id="create_connected:fluid_vessel" /> | <ItemGrid><ItemIcon id="create_connected:fluid_vessel" /></ItemGrid> | Fluid tank, not an item store |

***

## Access in tight spaces

| Interface | View | Role and limits |
| --- | --- | --- |
| <ItemLink id="create_connected:inventory_access_port" /> | <ItemGrid><ItemIcon id="create_connected:inventory_access_port" /></ItemGrid> | Extends one inventory's access, adds no space, cannot be daisy-chained, disabled by redstone |
| <ItemLink id="create_connected:inventory_bridge" /> | <ItemGrid><ItemIcon id="create_connected:inventory_bridge" /></ItemGrid> | Exposes two inventories only to components attached to the bridge, cannot be daisy-chained, disabled by redstone |
| <ItemLink id="create:stock_link" /> | <ItemGrid><ItemIcon id="create:stock_link" /></ItemGrid> | Joins a stock network, with packagers supplying inventory |

A bridge filter decides which inventory receives an inserted item, rejects items that match neither filter, and also applies when items are extracted. An access port is the simpler choice when one buried vault only needs a reachable face.

Stock Links belong to the logistics network: a stock-linked packager makes its inventory available to that network. They are not a required part of filling one vault.

- [Item and fluid routing](machines.logistics.md) Belts, arms, packagers and stock networks.
- [Storage handling](storage.handling.md) Shared item movement and filters.
- [Portable storage](storage.portable.md) Backpacks and shulker boxes for carrying.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Vibrant Vaults](images/catalog-hddn8ksr.png) [Create: Vibrant Vaults](storage.bulk.md) | Adds more color and material variants of Create item vaults. | <EmiSearch query="@create_vibrant_vaults" /> |
