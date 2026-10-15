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

## Rocket propulsion

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

![Spacecraft above Earth](images/feedback-earth-orbit.png)

Spacecraft above Earth

<ItemGrid>
  <ItemIcon id="rocketnautics:rocket_thruster" />
  <ItemIcon id="create:mechanical_crafter" />
  <ItemIcon id="minecraft:lava_bucket" />
</ItemGrid>

| Equipment | Use |
| --- | --- |
| <ItemLink id="rocketnautics:rocket_thruster" /> | Liquid-fuel propulsion for an assembled physical ship. |
| <ItemLink id="create:mechanical_crafter" /> | Crafts the thruster. Find its mechanical crafting layout in the recipe browser. |
| <ItemLink id="minecraft:lava_bucket" /> | Represents Lava fuel. Supply the fluid through the ship's fluid system, rather than inserting a bucket as a crafting ingredient. |

The thruster burns rocket fuel, not rotational power. Lava is a supported starting fuel. Its Ponder scene shows the engine and tank arrangement.

***

## Leaving the Overworld

Assemble a physical spacecraft with Sable, fit the thruster and keep its fuel supply running. Crossing above world Y 20,000 transfers the ship and nearby passengers into Deep Space. This height is a world coordinate, not a distance above the launch pad.

Deep Space is the orbital route to planetary surfaces. A change in sky appearance alone does not indicate a dimension transition.

***

## Surface entry

Approach the current linked planet in Deep Space. Crossing inward to within 20,000 blocks of its surface transfers the ship into that planet's dimension at world Y 19,000. The Overworld and Moon use these boundaries. Surface entry leaves the ship high above the terrain, not landed or under automatic control.

Slow descent before world Y 2,500. Between Y 1,000 and Y 2,500, downward speeds above 60 blocks per second cause heating. Stronger heating can damage nearby passengers.

***

## Related topics

- [Assembly](vehicles.assembly.md)
- [Dimensions](world.dimensions.md)
- [Space life support](space.life-support.md)
- [Space navigation](space.navigation.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
| ![Sable](images/catalog-t9pomcsv.png) [Sable](technical.libraries.md) | Framework for interactive moving block structures. | No separate item search |
