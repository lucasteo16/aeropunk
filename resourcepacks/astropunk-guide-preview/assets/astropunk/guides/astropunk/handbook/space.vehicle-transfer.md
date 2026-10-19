---
navigation:
  title: "Orbital flight"
  position: 10
  parent: reference.vehicles.md
  icon: rocketnautics:rocket_thruster
item_ids:
  - rocketnautics:rocket_thruster
---

# Orbital flight

## Launch vehicle

<EmiSearch query="@rocketnautics" />

![Spacecraft above Earth](images/feedback-earth-orbit.png)

Spacecraft above Earth

<ItemGrid><ItemIcon id="rocketnautics:rocket_thruster" /><ItemIcon id="rocketnautics:booster_thruster" /><ItemIcon id="rocketnautics:thruster_mount" /><ItemIcon id="rocketnautics:rcs_thruster" /><ItemIcon id="rocketnautics:fluid_hose" /><ItemIcon id="rocketnautics:titanium_ingot" /></ItemGrid>

An orbital ship is a Simulated Contraption with a rocket engine, a fuel feed and a thrust mount. Build the hull as described in [Assembly](vehicles.assembly.md), then fit the engine.

| Part | Job |
| --- | --- |
| <ItemLink id="rocketnautics:rocket_thruster" /> | Main thrust, burns liquid fuel |
| <ItemLink id="rocketnautics:booster_thruster" /> | Extra thrust for the first climb |
| <ItemLink id="rocketnautics:thruster_mount" /> | Holds the engine to the hull |
| <ItemLink id="rocketnautics:rcs_thruster" /> | Small corrections once in vacuum |
| <ItemLink id="rocketnautics:fluid_hose" /> | Carries fuel from tank to engine |

The engine burns fuel, not rotation. Feed it through the ship's fluid system and keep the tank above the engine feed, because a dry feed gives no thrust even with a full tank elsewhere.

## Crossing into Deep Space

The pack puts the transfer at height 20,000. Climb above it and the ship, plus the passengers aboard, moves into Deep Space. That is a world height, not a height above the launch pad, so a base on a mountain starts the count higher.

| Height | What changes | What to do |
| --- | --- | --- |
| 7,000 | Drag has fallen to zero | Stop relying on propellers |
| 20,000 | Transfer height into Deep Space | Cross it with fuel left for the return |
| 21,000 | Low density air and drowning | Have a sealed helmet and air supply aboard |

The crew needs that air supply before the crossing, as covered in [Space life support](space.life-support.md).

A change in sky colour is not a transfer. Check the world height and the dimension name, not the view.

## Arriving

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="rocketnautics:rcs_thruster" /><ItemIcon id="simulated:altitude_sensor" /><ItemIcon id="simulated:velocity_sensor" /><ItemIcon id="create:mechanical_crafter" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

Approach the linked body in Deep Space and cross the same transfer height inward. The ship arrives high above that surface, not landed and not on autopilot, so plan the descent before you cross.

1. Cut thrust early and let gravity do the work.
2. Keep some fuel for the landing burn, because the return trip needs the same crossing.
3. Watch the altitude sensor and the velocity sensor rather than the view, since the ground arrives fast in low gravity.
4. Land on flat ground. A hull that touches down on a slope slides before it settles.

The Moon's surface acceleration is 2.0 against the Overworld's 11.0, so the same descent that lands gently at home overshoots there. Reduce the descent burn, not the approach speed alone.

The return is the same crossing in reverse. Climb back above 20,000, cross into Deep Space, approach the Overworld and descend. Carry enough fuel for both crossings, because there is no fuel depot on the Moon unless you build one.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | Framework for interactive moving block structures. | No separate item search |
