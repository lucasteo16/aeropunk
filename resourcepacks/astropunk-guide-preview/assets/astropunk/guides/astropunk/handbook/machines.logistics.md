---
navigation:
  title: "Item routing"
  position: 0
  parent: reference.machines-storage.md
  icon: create:brass_funnel
---

# Item routing

## Items & fluids

<EmiSearch query="@create_connected" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:belt_connector" />
  <ItemIcon id="create:andesite_funnel" />
  <ItemIcon id="create:brass_funnel" />
  <ItemIcon id="create:brass_tunnel" />
  <ItemIcon id="create:chute" />
  <ItemIcon id="create_connected:brass_chute" />
  <ItemIcon id="create:mechanical_arm" />
  <ItemIcon id="create:fluid_pipe" />
  <ItemIcon id="create:mechanical_pump" />
  <ItemIcon id="create:smart_fluid_pipe" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create:belt_connector" />, <ItemLink id="create:andesite_funnel" />, <ItemLink id="create:brass_funnel" />, <ItemLink id="create:brass_tunnel" /> | Create belts, funnels and tunnels route items. Brass components add filtering. |
| <ItemLink id="create:chute" />, <ItemLink id="create_connected:brass_chute" />, <ItemLink id="create:mechanical_arm" /> | Chutes and mechanical arms connect processing stations. |
| <ItemLink id="create:fluid_pipe" />, <ItemLink id="create:mechanical_pump" />, <ItemLink id="create:smart_fluid_pipe" /> | Pipes, pumps and filtered fluid routing. |

***

## Packages & requests

<EmiSearch query="@createadditionallogistics" />

<ItemGrid>
  <ItemIcon id="create:packager" />
  <ItemIcon id="create:stock_link" />
  <ItemIcon id="create:redstone_requester" />
  <ItemIcon id="create:package_frogport" />
  <ItemIcon id="create:chain_conveyor" />
  <ItemIcon id="createadditionallogistics:package_accelerator" />
  <ItemIcon id="createadditionallogistics:package_editor" />
  <ItemIcon id="createadditionallogistics:cash_register" />
  <ItemIcon id="createadditionallogistics:lazy_shaft" />
  <ItemIcon id="createadditionallogistics:lazy_cogwheel" />
  <ItemIcon id="createadditionallogistics:flexible_shaft" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create:packager" />, <ItemLink id="create:stock_link" />, <ItemLink id="create:redstone_requester" /> | Create packaging, stock networks and redstone requests. |
| <ItemLink id="create:package_frogport" />, <ItemLink id="create:chain_conveyor" /> | Package transfer through frogports and chain conveyors. |
| <ItemLink id="createadditionallogistics:package_accelerator" />, <ItemLink id="createadditionallogistics:package_editor" />, <ItemLink id="createadditionallogistics:cash_register" /> | Speeds up the packager at a stress cost, edits package addresses by rules and records stock-ticker sales in a ledger. |
| <ItemLink id="createadditionallogistics:lazy_shaft" />, <ItemLink id="createadditionallogistics:lazy_cogwheel" />, <ItemLink id="createadditionallogistics:flexible_shaft" /> | Lazy shafts are more efficient in runs of more than two. Flexible shafts allow wrench-controlled connections on individual sides. |

***

## Getting started

### First item connection

<Recipe id="create:crafting/logistics/andesite_funnel" />

Craft <ItemLink id="create:andesite_funnel" /> to connect a container to item transport. Use Ponder for placement.

Connect one input container and one output container to a belt or chute before adding a stock network. Ponder covers the Create components. Additional Logistics also includes a Sales Ledger and Train Network Monitor Peripheral. The peripheral is a computer integration, not a standalone stock screen.

## Related items

<ItemGrid>
  <ItemIcon id="createadditionallogistics:sales_ledger" />
  <ItemIcon id="createadditionallogistics:network_monitor" />
</ItemGrid>

| Shown items |
| --- |
| <ItemLink id="createadditionallogistics:sales_ledger" /> |
| <ItemLink id="createadditionallogistics:network_monitor" /> |

## Related topics

- [Browse recipe](help.search.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Additional Logistics](images/catalog-CZaz7aje.png) [Create: Additional Logistics](machines.logistics.md) | Expands Create package handling with shop registers and improved factory stock controls. | <EmiSearch query="@createadditionallogistics" /> |
