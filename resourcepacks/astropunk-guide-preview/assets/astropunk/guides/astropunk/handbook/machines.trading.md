---
navigation:
  title: "Trading"
  position: 13
  parent: reference.machines-storage.md
  icon: minecraft:emerald_block
---

# Trading

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Trading+floor+Trading+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Trading+floor+%E6%89%8B%E5%8A%A8%E4%BA%A4%E6%98%93%E4%B8%8E%E8%87%AA%E5%8A%A8%E4%BA%A4%E6%98%93+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## A depot at a workstation

<EmiSearch query="@trading_floor" />

A <ItemLink id="trading_floor:trading_depot" /> turns one villager trade into a machine input and output. The villager still owns the trade list. The depot only hands over what the trade wants and takes what it gives.

Place the depot against a workstation a villager has claimed, not against the villager.

<Recipe id="trading_floor:trading_depot" />

<ItemGrid><ItemIcon id="trading_floor:trading_depot" /><ItemIcon id="minecraft:lectern" /><ItemIcon id="minecraft:emerald" /><ItemIcon id="minecraft:book" /></ItemGrid>

| Part | What it supplies |
| --- | --- |
| <ItemLink id="trading_floor:trading_depot" /> | The machine interface for one trade |
| The claimed workstation | Ties the depot to one villager |
| The villager | Owns the trade list, prices and restock |
| <ItemLink id="minecraft:emerald" /> | The common currency, still paid by you |

Trades happen while the villager is working. A villager who cannot reach its workstation, or who is asleep, does not trade, and the depot will sit with its input inside.

***

## What a working depot does

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="trading_floor:trading_depot" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:mechanical_arm" /><ItemIcon id="create:display_link" /></ItemGrid>

| Result | Detail |
| --- | --- |
| Trades per work session | Up to 4 in this pack |
| Villager experience | Earned by the villager, on by default |
| Player experience | Off by default in this pack |
| Readout | Goggles and display links show the trade state |

The four trades per session is a pack setting, not a limit of the mod's design. It is enough to make an iron farm or a book trade worth automating, and low enough that a single depot will not fund a base on its own.

***

## Two depots, two inputs

A trade that costs two different items needs two depots, each with its own input. Their filters must match, or one of them must be left empty.

<ItemGrid><ItemIcon id="trading_floor:trading_depot" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:chute" /></ItemGrid>

| Arrangement | Behaviour |
| --- | --- |
| One depot, one input | Handles a single item trade |
| Two depots, matching filters | Both feed the same trade |
| Two depots, one filter empty | The empty one accepts anything |
| Two depots, different filters | The trade will not complete |

Feed each depot with a <ItemLink id="create:brass_funnel" /> set to the exact item. A filter that accepts a substitute item breaks the trade silently, because the villager will not accept it.

The next useful step is moving the payment in and the result out without a player. [Material routing](machines.logistics.md) covers belts, funnels and arms.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Trading floor](images/create-trading-floor-icon.png) [Create: Trading floor](machines.trading.md) | Automates villager trading through Create machinery. | <EmiSearch query="@trading_floor" /> |
