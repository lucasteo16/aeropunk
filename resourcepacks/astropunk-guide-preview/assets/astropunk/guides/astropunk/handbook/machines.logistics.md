---
navigation:
  title: "Item routing"
  position: 5
  parent: reference.machines-storage.md
  icon: create:brass_funnel
---

# Item routing

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Additional+Logistics+Item+routing+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Additional+Logistics+%E8%BE%93%E9%80%81%E3%80%81%E7%AD%9B%E9%80%89%E4%B8%8E%E5%88%86%E9%85%8D%E7%89%A9%E5%93%81+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## One clean line

<EmiSearch query="@create" />

A belt carries items between a container and a machine. An <ItemLink id="create:andesite_funnel" /> picks items up from the container and drops them onto the belt, and a second funnel at the far end moves them into the machine.

Start with one input container, one belt and one funnel. Get that running before you plan a factory.

<Recipe id="create:crafting/logistics/andesite_funnel" />

<ItemGrid><ItemIcon id="create:belt_connector" /><ItemIcon id="create:andesite_funnel" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:chute" /></ItemGrid>

| Part | Limit in this pack |
| --- | --- |
| Mechanical belt | 20 blocks maximum length |
| Andesite funnel | Extracts once every 8 game ticks |
| Brass funnel | Same rate, with filtering and a count |
| Chute | Vertical drop, no rotation needed |

The expected result is items moving without anyone opening a chest. If the belt moves but nothing arrives, the funnel is facing the wrong way, since one side extracts and the other inserts.

***

## Filters decide what moves

A <ItemLink id="create:brass_funnel" /> takes a filter in its settings and moves only matching items. A <ItemLink id="create:brass_tunnel" /> splits one stream across several outputs according to its filters.

<ItemGrid><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:brass_tunnel" /><ItemIcon id="create:mechanical_arm" /><ItemIcon id="create:smart_fluid_pipe" /></ItemGrid>

| Part | Useful fact |
| --- | --- |
| <ItemLink id="create:brass_funnel" /> | Filter plus a requested count, so a machine gets exactly its input |
| <ItemLink id="create:brass_tunnel" /> | Distributes every 10 game ticks |
| <ItemLink id="create:mechanical_arm" /> | Reaches 5 blocks and serves several inputs and outputs from one point |
| <ItemLink id="create:smart_fluid_pipe" /> | Filters fluids the same way a brass funnel filters items |

A mechanical arm is the answer when one machine needs three ingredients and produces two outputs in a tight space. It has a fixed reach of 5 blocks in this pack, so lay the machines out around it rather than stretching the arm.

***

## Packages move stock, not items

<EmiSearch query="@createadditionallogistics" /> <EmiSearch query="@create_connected" />

Create 6 packaging turns loose items into addressed packages. A <ItemLink id="create:packager" /> packs, a <ItemLink id="create:stock_link" /> reads a container as stock, and a <ItemLink id="create:package_frogport" /> receives a package at the far end.

<ItemGrid><ItemIcon id="create:packager" /><ItemIcon id="create:stock_link" /><ItemIcon id="create:package_frogport" /><ItemIcon id="create:redstone_requester" /><ItemIcon id="create:chain_conveyor" /></ItemGrid>

| Part | Role |
| --- | --- |
| <ItemLink id="create:packager" /> | Turns a container of items into a package |
| <ItemLink id="create:stock_link" /> | Exposes a container to the stock network |
| <ItemLink id="create:package_frogport" /> | Accepts packages addressed to its address |
| <ItemLink id="create:chain_conveyor" /> | Carries 20 packages, up to 32 blocks, with 4 connections |
| <ItemLink id="create:redstone_requester" /> | Requests stock without a factory gauge |

Two settings from Additional Logistics matter once a factory gauge exists. Promise Limits caps how many open promises one gauge may hold, which stops a slow line from being flooded with ingredient packages. Additional Stock lets a restocker request extra above its target instead of topping up by one item at a time.

The mod also supplies a cash register. This pack disables stock tickers in its server configuration, so treat the register as shop furniture rather than a stock market.

| Additional part | Difference |
| --- | --- |
| <ItemLink id="createadditionallogistics:package_accelerator" /> | Speeds the packager, at a stress cost |
| <ItemLink id="createadditionallogistics:package_editor" /> | Rewrites package addresses by rule |
| <ItemLink id="createadditionallogistics:cash_register" /> | Records shop sales in a ledger |
| <ItemLink id="createadditionallogistics:sales_ledger" /> | The ledger the register writes to |
| <ItemLink id="createadditionallogistics:lazy_shaft" /> | Cheaper over runs longer than two blocks |
| <ItemLink id="createadditionallogistics:lazy_cogwheel" /> | The same saving on a cogwheel |
| <ItemLink id="createadditionallogistics:flexible_shaft" /> | Wrench set connections on individual sides |
| <ItemLink id="create_connected:brass_chute" /> | A chute with brass filtering |
| <ItemLink id="createadditionallogistics:network_monitor" /> | Train network readout, a computer integration rather than a stock screen |

***

## Fluids follow the same rules

<ItemGrid><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:hose_pulley" /></ItemGrid>

| Part | Limit in this pack |
| --- | --- |
| <ItemLink id="create:mechanical_pump" /> | Pushes or pulls 16 blocks on either side |
| <ItemLink id="create:fluid_tank" /> | 8 buckets per block, up to 32 blocks tall |
| <ItemLink id="create:hose_pulley" /> | Reaches 128 blocks of fluid |
| Hose pulley on a large body | A body of 10000 or more source blocks counts as infinite |

The hose pulley is how a lava lake becomes a factory input. Below that 10000 block threshold it simply drains what it finds, so a small pond will empty and stay empty.

The next useful step is storage that a line can fill and empty without a player. [Bulk storage](storage.bulk.md) covers vaults and silos.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Additional Logistics](images/catalog-czaz7aje.png) [Create: Additional Logistics](machines.logistics.md) | Expands Create package handling with shop registers and improved factory stock controls. | <EmiSearch query="@createadditionallogistics" /> |
