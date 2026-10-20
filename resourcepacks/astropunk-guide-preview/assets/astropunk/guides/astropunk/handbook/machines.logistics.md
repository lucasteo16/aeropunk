---
navigation:
  title: "Item & fluid routing"
  position: 10
  parent: reference.machines-storage.md
  icon: create:brass_funnel
---

# Item & fluid routing

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+mod+belts+funnels+packagers+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E4%BC%A0%E9%80%81%E5%B8%A6+%E6%BC%8F%E6%96%97+%E6%89%93%E5%8C%85%E6%9C%BA+%E7%89%A9%E6%B5%81%E6%95%99%E7%A8%8B)

## Connect and move a first item

<EmiSearch query="@create" />

Hold <ItemLink id="create:belt_connector" /> and right click two shafts in a supported alignment to connect them. Rotate either shaft and both turn at the same speed and direction. Drop an item onto the moving belt. Empty-hand right click picks it up. Open these Ponder lessons: Using Mechanical Belts and Valid Orientations for Mechanical Belts.

| Part | View | Use |
| --- | --- | --- |
| Belt | <ItemGrid><ItemIcon id="create:belt_connector" /></ItemGrid> | Connects two shafts and carries items |
| Andesite Funnel | <ItemGrid><ItemIcon id="create:andesite_funnel" /></ItemGrid> | Transfers one item at a time |
| Brass Funnel | <ItemGrid><ItemIcon id="create:brass_funnel" /></ItemGrid> | Transfers up to a stack, with filter and amount panel |

Place a funnel normally to extract from an inventory, sneak-place to insert, then use a wrench to flip it. Redstone disables it. On belts, movement direction determines transfer direction. A brass filter slot accepts only matching stacks.

***

## Sort, drop and collect

<EmiSearch query="@create_connected" />

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+6+brass+tunnel+sorting+mechanical+arm+input+output+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+6+%E9%BB%84%E9%93%9C%E9%9A%A7%E9%81%93+%E5%88%86%E6%8B%A3+%E6%9C%BA%E6%A2%B0%E8%87%82+%E8%BE%93%E5%85%A5+%E8%BE%93%E5%87%BA+%E6%95%99%E7%A8%8B)

| Part | View | Distinction |
| --- | --- | --- |
| Andesite Tunnel | <ItemGrid><ItemIcon id="create:andesite_tunnel" /></ItemGrid> | Covers a belt and splits exactly one item off when side connections are present |
| Brass Tunnel | <ItemGrid><ItemIcon id="create:brass_tunnel" /></ItemGrid> | Inbound filters reject non-matches. Outbound filters sort by item. Distribution modes choose among valid outputs. |
| Chute | <ItemGrid><ItemIcon id="create:chute" /></ItemGrid> | Moves items vertically between inventories |
| Brass Chute | <ItemGrid><ItemIcon id="create_connected:brass_chute" /></ItemGrid> | Use for the addon chute route shown in its item help |

For a chute, place it between the inventories. A wrench opens a side window. An encased fan at the top or bottom lets it move items upward. Goggles show the movement direction.

Assign a <ItemLink id="create:mechanical_arm" /> before placing it. Right click supported depots or funnels while holding the arm to add targets. Right click again changes blue input to yellow output, and left click removes a target. Then place and power the arm. Not every inventory is directly supported, so use a depot or funnel as an interface when needed. Brass funnel targets pass their filters to the arm.

***

## Packages and stock requests

<EmiSearch query="@createadditionallogistics" />

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+6+stock+network+packager+stock+link+stock+ticker+address+complete+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+6+%E6%89%93%E5%8C%85%E6%9C%BA+%E5%BA%93%E5%AD%98%E9%93%BE%E6%8E%A5+%E5%BA%93%E5%AD%98%E6%8A%A5%E4%BB%B7%E5%99%A8+%E5%9C%B0%E5%9D%80+%E5%AE%8C%E6%95%B4%E6%95%99%E7%A8%8B)

| Part | View | Use |
| --- | --- | --- |
| Packager | <ItemGrid><ItemIcon id="create:packager" /></ItemGrid> | Packages items from its attached inventory under redstone, or unpacks a package inserted into it |
| Package Filter | <ItemGrid><ItemIcon id="create:package_filter" /></ItemGrid> | Routes by package address, not item contents |
| Package Frogport | <ItemGrid><ItemIcon id="create:package_frogport" /></ItemGrid> | Package delivery interface |
| Stock Link | <ItemGrid><ItemIcon id="create:stock_link" /></ItemGrid> | Lets stock-linked packagers expose their inventories to the network |
| Redstone Requester | <ItemGrid><ItemIcon id="create:redstone_requester" /></ItemGrid> | Requests stock through the network |

1. Attach a Packager to the source inventory. Put a few test items inside and pulse the packager with redstone. A package should appear. This tests packing before adding a network.
2. Transport that package on a belt into a destination Packager attached to a receiving inventory. It unpacks only when the inventory can accept the entire contents.
3. Attach a Stock Link to the source Packager. Hold another Stock Link and right click the first before placing it to join that network. The links share stock information, not the physical packages.
4. Hold a <ItemLink id="create:stock_ticker" /> and right click the Stock Link before placement. Put a seated creature or a Blaze Burner in front as its Stock Keeper, then right click that keeper to order available stock. For automated orders, bind a Redstone Requester to the same link before placing it, right click its interface to set an order, and pulse it.
5. Set the requested destination address and use a Package Filter for that address on the transport route. The test succeeds when the requested goods arrive and unpack in the intended inventory.

Attach a stock link to a packager and connect it to the network. A link on a vault alone does not display a count. The package still needs a transport route.

***

| Addon | View | Role |
| --- | --- | --- |
| <ItemLink id="createadditionallogistics:package_accelerator" /> | <ItemGrid><ItemIcon id="createadditionallogistics:package_accelerator" /></ItemGrid> | Speeds the packager directly in front at a stress cost |
| <ItemLink id="createadditionallogistics:package_editor" /> | <ItemGrid><ItemIcon id="createadditionallogistics:package_editor" /></ItemGrid> | Rewrites package addresses using its rules |
| <ItemLink id="createadditionallogistics:network_monitor" /> | <ItemGrid><ItemIcon id="createadditionallogistics:network_monitor" /></ItemGrid> | Displays stock-network information |
| <ItemLink id="createadditionallogistics:cash_register" /> | <ItemGrid><ItemIcon id="createadditionallogistics:cash_register" /></ItemGrid> | Stock Ticker alternative that records sales |
| <ItemLink id="createadditionallogistics:sales_ledger" /> | <ItemGrid><ItemIcon id="createadditionallogistics:sales_ledger" /></ItemGrid> | Use on the Stock Keeper to request restocking sold goods |

## Fluids and long drives

| Family | View | Use |
| --- | --- | --- |
| Fluid pipes | <ItemGrid><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:smart_fluid_pipe" /><ItemIcon id="create:mechanical_pump" /></ItemGrid> | Move fluids. Smart pipe filters by fluid |
| Fluid storage and source movement | <ItemGrid><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:hose_pulley" /></ItemGrid> | Tank stores fluid. Hose pulley fills or drains large bodies |
| Item conveyance | <ItemGrid><ItemIcon id="create:chain_conveyor" /></ItemGrid> | Convey items along a chain route |
| Shaft routing | <ItemGrid><ItemIcon id="createadditionallogistics:lazy_shaft" /><ItemIcon id="createadditionallogistics:lazy_cogwheel" /><ItemIcon id="createadditionallogistics:flexible_shaft" /></ItemGrid> | Lazy shafts help runs longer than two. Lazy cogs are useful with at least two lazy shafts. Wrench a flexible shaft to toggle that side's output. |

For a fluid route, connect tank, pump and destination with pipes. Follow the arrow on the pump to set flow. Reversing the pump's rotational input does not reverse fluid flow. Use a wrench to change the arrow.

- [Bulk storage](storage.bulk.md) Vault capacity and shape.
- [Storage handling](storage.handling.md) Shared inventory transfer.
- [Rotational power](machines.rotation.md) Drive setup.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Additional Logistics](images/catalog-czaz7aje.png) [Create: Additional Logistics](machines.logistics.md) | Expands Create package handling with shop registers and improved factory stock controls. | <EmiSearch query="@createadditionallogistics" /> |
