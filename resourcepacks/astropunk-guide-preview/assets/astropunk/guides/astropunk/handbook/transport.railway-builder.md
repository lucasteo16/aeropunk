---
navigation:
  title: "Railways"
  position: 2
  parent: reference.vehicles.md
  icon: create:track
---

# Railways

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+train+assembly+station+seated+conductor+schedule+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+%E5%88%97%E8%BD%A6+%E7%BB%84%E8%A3%85+%E8%BD%A6%E7%AB%99+%E4%B9%98%E5%8A%A1%E5%91%98+%E6%97%B6%E5%88%BB%E8%A1%A8+%E6%95%99%E7%A8%8B)

## Line, station, schedule

<EmiSearch query="@create" />

![Train bodywork with Bells & Whistles fittings](images/visual-train-fittings.png)

<ItemGrid><ItemIcon id="create:track" /><ItemIcon id="create:track_station" /><ItemIcon id="create:controls" /><ItemIcon id="create:schedule" /><ItemIcon id="create:railway_casing" /></ItemGrid>

<Recipe id="create:crafting/kinetics/track_station" />

<Recipe id="create:crafting/kinetics/controls" />

A working train needs connected <ItemLink id="create:track" />, a <ItemLink id="create:track_station" /> and <ItemLink id="create:controls" /> facing the travel direction. Start with two named stations on a short line so you can check the complete route before expanding it.

1. Place the station beside the track and enter its assembly mode. This is different from assembling a Sable ship.
2. Place <ItemLink id="create:railway_casing" /> on the highlighted track to make bogies. Build the carriages over them and glue each carriage together. Fit controls where the driver can reach them.
3. Assemble through the station interface. If assembly is refused, read its message and check bogie placement and the connected carriage structure.
4. Take control and drive the short route manually. Check that the line is continuous and that there is room at each station to stop.
5. For automatic operation, place a seated conductor in front of the controls and use a completed <ItemLink id="create:schedule" /> on that conductor. Add the named destination stations and a wait condition for each stop, such as a timed wait or cargo condition. Configure whether the route repeats.

A schedule belongs to the conductor, not an unspecified slot inside the train. Manual driving does not require one. If an automatic train waits indefinitely, inspect the active wait condition, the destination name and the signals ahead before changing its engines.

## Track families

<ItemGrid><ItemIcon id="create:track" /><ItemIcon id="create:track_station" /><ItemIcon id="create:controls" /><ItemIcon id="create:schedule" /></ItemGrid>

Create supplies the standard track and the station and controls that go with it. Steam 'n' Rails extends the families with narrower and wider gauges, switches, signals and conductor equipment. Gauge is not cosmetic. A train assembles on the track it was built against, and a switch only joins tracks of the same gauge.

Build a short test line in the gauge you intend to use before you build the main line. Changing gauge halfway through is a rebuild, not an adjustment.

## Bogies

<ItemGrid><ItemIcon id="create:railway_casing" /></ItemGrid>

Blocks & Bogies adds a bogie customization interface rather than a second inventory of bogie items. Open the interface on a placed bogie and preview the available wheel arrangements, frame sizes and valve-gear styles. Its driver and truck categories describe the chosen design. they are not a requirement to fit one powered bogie per train or calculate an axle count from carriage weight.

Choose the style for the carriage you are building, then check its appearance on a short curve before fitting the whole train. Track-gauge compatibility belongs to the track and bogie combination, not to an invented physical derailing rule for decorative wheel length.

## Freight and passengers

<ItemGrid><ItemIcon id="create:schedule" /><ItemIcon id="create:track_station" /></ItemGrid>

A carriage carries what you put in it. Seats, storage and fluid tanks are ordinary blocks inside the train body, and the schedule decides where it stops. For passenger information and route search, see [Train travel](transport.passenger.md).


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Blocks & Bogies](images/catalog-j4arnqwy.png) [Create: Blocks & Bogies](transport.railway-builder.md) | Adds larger Create train bogies, including visible valve gear variants. | No separate item search |
| ![Steam 'n' Rails Neoforge](images/catalog-l3jv0qzi.png) [Steam 'n' Rails Neoforge](transport.railway-builder.md) | Expands Create railways with additional track and train components. | <EmiSearch query="@railways" /> |
