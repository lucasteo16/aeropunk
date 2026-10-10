---
navigation:
  title: "Bulk storage"
  position: 0
  parent: reference.machines-storage.md
  icon: create:item_vault
---

# Bulk storage

## Vaults & containers

<EmiSearch query="@create_vibrant_vaults" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:item_vault" />
  <ItemIcon id="create_vibrant_vaults:basic_shipping_container" />
  <ItemIcon id="create_vibrant_vaults:shipping_container" />
  <ItemIcon id="create_vibrant_vaults:vertical_item_vault" />
  <ItemIcon id="create_vibrant_vaults:vertical_basic_shipping_container" />
  <ItemIcon id="create_vibrant_vaults:vertical_shipping_container" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create:item_vault" /> | Create item vault for connected workshop storage. |
| <ItemLink id="create_vibrant_vaults:basic_shipping_container" />, <ItemLink id="create_vibrant_vaults:shipping_container" /> | Create: Vibrant Vaults adds Basic Shipping Container and Shipping Container families. |
| <ItemLink id="create_vibrant_vaults:vertical_item_vault" />, <ItemLink id="create_vibrant_vaults:vertical_basic_shipping_container" />, <ItemLink id="create_vibrant_vaults:vertical_shipping_container" /> | Vertical vault and container variants. Dyed versions distinguish stockpiles visually. |

***

## Silos & access

<EmiSearch query="@create_connected" />

<ItemGrid>
  <ItemIcon id="create_connected:item_silo" />
  <ItemIcon id="create_connected:fluid_vessel" />
  <ItemIcon id="create_connected:inventory_access_port" />
  <ItemIcon id="create_connected:inventory_bridge" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create_connected:item_silo" />, <ItemLink id="create_connected:fluid_vessel" /> | Create: Connected adds a vertical item vault and a horizontal fluid tank. The vessel is less efficient as a boiler. |
| <ItemLink id="create_connected:inventory_access_port" />, <ItemLink id="create_connected:inventory_bridge" /> | Access ports extend an inventory connection. Bridges expose two inventories. Neither adds storage capacity. |

***

## Getting started

### Workshop vault

<Recipe id="create:crafting/kinetics/item_vault" />

Craft <ItemLink id="create:item_vault" />, then use its Ponder entry to connect the storage blocks.

Start with an Item Vault and its Ponder entry. Add an Inventory Access Port when a funnel or stock link cannot reach the container. Color does not establish a different capacity. Package routing is in Material routing.

- [Material routing](machines.logistics.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Vibrant Vaults](images/catalog-hddN8ksR.png) [Create: Vibrant Vaults](storage.bulk.md) | Adds more color and material variants of Create item vaults. | <EmiSearch query="@create_vibrant_vaults" /> |
