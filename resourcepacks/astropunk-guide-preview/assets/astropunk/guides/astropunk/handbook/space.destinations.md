---
navigation:
  title: "Space destinations"
  position: 0
  parent: reference.vehicles.md
  icon: rocketnautics:lunar_rock
---

# Space destinations

## Landable destinations

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@rocketnautics_addon" /> <EmiSearch query="@create" />

Cosmonautics links the Overworld to a landable Moon dimension. Create Cosmonautics Expansion adds a landable Mars dimension. The base release also defines a gas giant and an ice world as celestial bodies, but their planet records do not link to playable surface dimensions. Seeing a planet in the sky or the planetary display is not proof that it has a landing world.

| Destination | Included terrain |
| --- | --- |
| Moon | Lunar highlands, maria and rocky chasms |
| Mars | Plains, frostlands and underground caves |

The Moon and Mars have dimension definitions as well as planet records. Deep Space is a transit dimension for physical spacecraft, not another planetary surface.

- [Dimensions](world.dimensions.md) The pack's landable dimensions and terrain.
- [Orbital flight](space.vehicle-transfer.md) Build and fly a physical spacecraft.

***

## Getting there

Build a physical ship that Sable can assemble as a moving sublevel. Fit a liquid-fuel <ItemLink id="rocketnautics:rocket_thruster" /> and consult its built-in Ponder lesson for the engine setup. The transition check uses the ship's world Y coordinate. The Overworld planet data sets the transfer height to 20,000, which is a coordinate, not a distance above the launch pad. When an assembled ship with a valid physics handle crosses that boundary, the transition system moves the ship and nearby passengers into Deep Space. The destination planet data links the Moon and Mars dimensions to the orbital universe.

The <ItemLink id="rocketnautics:hologram_block" /> displays the celestial system. It does not select a destination or pilot a landing.

- [Orbital flight](space.vehicle-transfer.md) Rocket construction and the Overworld to Deep Space transition.
- [Space navigation](space.navigation.md) Read the planetary display and distinguish it from a flight control.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics](space.destinations.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
| <ItemImage id="minecraft:minecart" /> [Create Cosmonautics Expansion](space.navigation.md) | Adds the landable Mars dimension, terrain and planetary record. | <EmiSearch query="@rocketnautics_addon" /> |
