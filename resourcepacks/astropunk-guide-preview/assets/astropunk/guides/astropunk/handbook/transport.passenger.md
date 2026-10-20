---
navigation:
  title: "Train travel"
  position: 1
  parent: reference.vehicles.md
  icon: minecraft:rail
---

# Train travel

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Railways+Navigator+Train+travel+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Railways+Navigator+%E4%B9%98%E5%9D%90%E5%88%97%E8%BD%A6%E5%87%BA%E8%A1%8C+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## Route search

<EmiSearch query="@createrailwaysnavigator" /> <EmiSearch query="@create" />

![Train bodywork with Bells & Whistles fittings](images/visual-train-fittings.png)

Train bodywork with Bells & Whistles fittings

<ItemGrid><ItemIcon id="createrailwaysnavigator:navigator" /><ItemIcon id="createrailwaysnavigator:train_station_clock" /><ItemIcon id="create:track_station" /></ItemGrid>

<ItemLink id="createrailwaysnavigator:navigator" /> searches the train network that already exists. It does not lay track and it does not move you. Open it, pick a departure station and a destination station, and it lists the services, the transfer stops and the live position of the trains on each leg.

The station list comes from placed <ItemLink id="create:track_station" /> blocks with names. An unnamed station cannot be chosen, and a station on a line with no schedule has no service to show.

A <ItemLink id="createrailwaysnavigator:train_station_clock" /> shows the time at a station and the next departure. Place it where passengers wait, not on the train.

## Passenger displays

<ItemGrid><ItemIcon id="createrailwaysnavigator:advanced_display" /><ItemIcon id="createrailwaysnavigator:advanced_display_block" /><ItemIcon id="createrailwaysnavigator:advanced_display_panel" /><ItemIcon id="createrailwaysnavigator:advanced_display_half_panel" /><ItemIcon id="createrailwaysnavigator:advanced_display_slab" /><ItemIcon id="createrailwaysnavigator:advanced_display_sloped" /><ItemIcon id="createrailwaysnavigator:advanced_display_small" /><ItemIcon id="create:wrench" /></ItemGrid>

The display family is one screen in several shapes, so it fits a wall, a slab, a slope or a small post.

| Shape | Fits |
| --- | --- |
| <ItemLink id="createrailwaysnavigator:advanced_display_block" /> | A full wall panel |
| <ItemLink id="createrailwaysnavigator:advanced_display_panel" /> | A wide wall strip |
| <ItemLink id="createrailwaysnavigator:advanced_display_half_panel" /> | A narrow strip |
| <ItemLink id="createrailwaysnavigator:advanced_display_slab" /> | A low ledge or counter |
| <ItemLink id="createrailwaysnavigator:advanced_display_sloped" /> | A angled mount over a platform |
| <ItemLink id="createrailwaysnavigator:advanced_display_small" /> | A post or a carriage interior |

Use a wrench on a placed display to choose what it shows. The options are train destination, passenger information, platform, departure board and static text. A destination display follows one train, so it belongs on the carriage. A platform or departure board display belongs at the station, where it can list several services.

<Recipe id="createrailwaysnavigator:advanced_display" />

## A working station

<ItemGrid><ItemIcon id="create:track_station" /><ItemIcon id="createrailwaysnavigator:advanced_display_block" /><ItemIcon id="createrailwaysnavigator:navigator" /></ItemGrid>

1. Name the station on the <ItemLink id="create:track_station" /> and confirm the train stops there in its schedule.
2. Place the platform display facing the waiting area and set it to departure board.
3. Place a train destination display inside each carriage and set it to the train.
4. Carry the Navigator and check that the service appears between the two stations before you invite anyone aboard.

If the Navigator finds no route, the fault is in the schedule or the station name, not in the Navigator.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Railways Navigator](images/catalog-dq3stxps.png) [Create Railways Navigator](transport.passenger.md) | Adds train route search, passenger information displays and schedule features. | <EmiSearch query="@createrailwaysnavigator" /> |
