---
navigation:
  title: "Rotational power"
  position: 0
  parent: reference.machines-storage.md
  icon: create:cogwheel
---

# Rotational power

## Sources & transmission

<EmiSearch query="@create_connected" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:water_wheel" />
  <ItemIcon id="create:large_water_wheel" />
  <ItemIcon id="create:windmill_bearing" />
  <ItemIcon id="create:steam_engine" />
  <ItemIcon id="create:shaft" />
  <ItemIcon id="create:cogwheel" />
  <ItemIcon id="create:gearbox" />
  <ItemIcon id="create_connected:cross_connector" />
  <ItemIcon id="create_connected:parallel_gearbox" />
  <ItemIcon id="create_connected:six_way_gearbox" />
  <ItemIcon id="create_connected:brass_gearbox" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create:water_wheel" />, <ItemLink id="create:large_water_wheel" />, <ItemLink id="create:windmill_bearing" />, <ItemLink id="create:steam_engine" /> | Create supplies water, wind and steam rotation. |
| <ItemLink id="create:shaft" />, <ItemLink id="create:cogwheel" />, <ItemLink id="create:gearbox" /> | Shaft, cogwheel and gearbox transmission. |
| <ItemLink id="create_connected:cross_connector" />, <ItemLink id="create_connected:parallel_gearbox" />, <ItemLink id="create_connected:six_way_gearbox" />, <ItemLink id="create_connected:brass_gearbox" /> | Create: Connected adds independent crossing, parallel routing, six-sided connections and wrench-configurable output directions. |

***

## Clutches & controls

<ItemGrid>
  <ItemIcon id="create_connected:inverted_clutch" />
  <ItemIcon id="create_connected:inverted_gearshift" />
  <ItemIcon id="create_connected:centrifugal_clutch" />
  <ItemIcon id="create_connected:freewheel_clutch" />
  <ItemIcon id="create_connected:overstress_clutch" />
  <ItemIcon id="create_connected:brake" />
  <ItemIcon id="create_connected:shear_pin" />
  <ItemIcon id="create_connected:kinetic_bridge" />
  <ItemIcon id="create_connected:encased_chain_cogwheel" />
  <ItemIcon id="create_connected:crank_wheel" />
</ItemGrid>

| Items & families | Use |
| --- | --- |
| <ItemLink id="create_connected:inverted_clutch" />, <ItemLink id="create_connected:inverted_gearshift" /> | Redstone-enabled clutch and inverted gearshift variants. |
| <ItemLink id="create_connected:centrifugal_clutch" />, <ItemLink id="create_connected:freewheel_clutch" />, <ItemLink id="create_connected:overstress_clutch" /> | Couple by speed threshold or direction. Disconnect on overstress. |
| <ItemLink id="create_connected:brake" />, <ItemLink id="create_connected:shear_pin" /> | Brake and shear-pin protection components. |
| <ItemLink id="create_connected:kinetic_bridge" />, <ItemLink id="create_connected:encased_chain_cogwheel" />, <ItemLink id="create_connected:crank_wheel" /> | Compact bridges, chain transmission and manual crank wheels. |

***

## Getting started

### First transmission

<Recipe id="create:crafting/kinetics/shaft" />

Two <ItemLink id="create:andesite_alloy" /> make eight <ItemLink id="create:shaft" />.

### First power source

<Recipe id="create:crafting/kinetics/water_wheel" />

Craft <ItemLink id="create:water_wheel" /> for the first powered machine. Use its Ponder entry for the water arrangement.

### Machine tool

<Recipe id="create:crafting/kinetics/wrench" />

Keep <ItemLink id="create:wrench" /> ready when adjusting Create components.

Begin with a Water Wheel, shaft and one machine. Use each component's Ponder entry for placement and direction. Add a clutch only when a branch needs independent control. Energy reserves are in Stored rotation.

- [Stored rotation](power.stored-rotation.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Connected](images/create-connected-icon.png) [Create: Connected](machines.rotation.md) | Adds Create transmission components and flexible storage arrangements. | <EmiSearch query="@create_connected" /> |
