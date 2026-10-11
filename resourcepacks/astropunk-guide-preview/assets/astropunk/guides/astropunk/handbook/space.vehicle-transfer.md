---
navigation:
  title: "Orbital flight"
  position: 0
  parent: reference.vehicles.md
  icon: rocketnautics:rocket_thruster
item_ids:
  - rocketnautics:rocket_thruster
---

# Orbital flight

## Rocket Thruster

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="rocketnautics:rocket_thruster" />
</ItemGrid>

<ItemLink id="rocketnautics:rocket_thruster" />

Use <ItemLink id="create:mechanical_crafter" /> to make the liquid-fuel Rocket Thruster. Find the mechanical crafting recipe in the recipe browser. Its Ponder lesson shows the engine and tank arrangement.

***

## Orbital flight

Build a physical craft that Sable can assemble as a moving sublevel, then fit and fuel the Rocket Thruster. Supply Lava, shown by <ItemLink id="minecraft:lava_bucket" />, through the fluid system. The bucket represents the fluid, not a consumed crafting ingredient. The engine accepts fluids in its rocket-fuel tag, not arbitrary liquids, and produces thrust on an assembled physical ship. Keep its fuel supply running. Rotation does not directly drive this engine.

The Overworld to space boundary is the ship's world Y coordinate 20,000. It is not measured upward from the launch site. Crossing it with an assembled, physics-ready ship transfers the craft and nearby passengers into Deep Space. This is an orbital flight transition, not a direct jump from a Rocket Thruster to the Moon. The Moon and Mars are separate linked dimensions in the planetary system.

Do not treat a sky rendering change alone as proof that the ship entered another dimension.

- [Space destinations](space.destinations.md) Landable worlds and the planetary records.
- [Space life support](space.life-support.md) Breathing and gravity inside an intact spacecraft compartment.
- [Space navigation](space.navigation.md) Use the planetary overview without mistaking it for autopilot.

***

## Surface entry

In Deep Space, approaching within the current linked planet's transfer boundary brings the ship back into its surface dimension. For the Overworld, Moon and Mars, that boundary is 20,000 blocks from the planetary surface. The return places the ship at world Y 19,000, not on the ground. This is dimension entry, not touchdown or automatic landing.

Slow descent before world Y 2,500. Downward ship speeds above 60 blocks per second cause heating between Y 1,000 and Y 2,500, and stronger heating can damage nearby passengers.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics Expansion](space.navigation.md) | Adds the landable Mars dimension, terrain and planetary record. | <EmiSearch query="@rocketnautics_addon" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | Framework for interactive moving block structures. | No separate item search |
