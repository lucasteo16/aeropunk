---
navigation:
  title: "Trading"
  position: 13
  parent: reference.machines-storage.md
  icon: minecraft:emerald_block
---

# Trading

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Trading+Floor+trading+depot+villager+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E4%BA%A4%E6%98%93%E7%AB%99+%E6%9D%91%E6%B0%91+%E6%95%99%E7%A8%8B)

## Connect a depot to a villager

<EmiSearch query="@trading_floor" /> <EmiSearch query="@create" />

Attach a <ItemLink id="trading_floor:trading_depot" /> to the workstation claimed by a villager. Open the depot and select an available trade with its trade filter, then supply the exact listed costs. The villager must be able to reach the workstation and work during normal work hours. Open the Ponder lesson Trading with trading depots.

<Recipe id="trading_floor:trading_depot" />

| Part | View | Role |
| --- | --- | --- |
| Trading Depot | <ItemGrid><ItemIcon id="trading_floor:trading_depot" /></ItemGrid> | Holds that depot's input and output |
| Claimed workstation | <ItemGrid><ItemIcon id="minecraft:lectern" /></ItemGrid> | Connects the depot to its villager |
| Mechanical Arm | <ItemGrid><ItemIcon id="create:mechanical_arm" /></ItemGrid> | Feeds supported trading-depot targets after configuration |
| Trade goods | <ItemGrid><ItemIcon id="minecraft:emerald" /><ItemIcon id="minecraft:book" /></ItemGrid> | Costs and results come from the selected villager offer |

When the villager next works, the depot performs the selected trade if its inputs are present. Check the depot information and last-trade field with goggles. Move the output from the depot with a funnel or chute.

***

## Trades with two inputs

Use two depots for a trade with two different costs. Set the trade filter on the first input depot to avoid unrelated offers. The second depot shares the trade when filters match, or when that other depot has no filter set. This means an unset filter, not an empty depot inventory. The output goes to the depot holding the first trade input.

| Route | View | Use |
| --- | --- | --- |
| Single input | <ItemGrid><ItemIcon id="create:brass_funnel" /></ItemGrid> | Brass funnel feeds the exact selected cost |
| Vertical transfer | <ItemGrid><ItemIcon id="create:chute" /></ItemGrid> | Chute feeds or removes items vertically |
| Trade readout | <ItemGrid><ItemIcon id="create:display_link" /></ItemGrid> | Optional status display |

The villager owns its prices and restocking. Open the Ponder lesson Trading with multiple trading depots. [Item and fluid routing](machines.logistics.md) covers item movement.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Trading floor](images/create-trading-floor-icon.png) [Create: Trading floor](machines.trading.md) | Automates villager trading through Create machinery. | <EmiSearch query="@trading_floor" /> |
