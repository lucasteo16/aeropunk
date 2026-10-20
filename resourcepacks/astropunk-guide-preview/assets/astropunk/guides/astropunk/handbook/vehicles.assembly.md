---
navigation:
  title: "Vehicle assembly"
  position: 4
  parent: reference.vehicles.md
  icon: create:mechanical_bearing
---

# Vehicle assembly

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Aeronautics+Sable+Simulated+assembler+glue+vehicle+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Aeronautics+Sable+%E8%BD%BD%E5%85%B7+%E7%BB%84%E8%A3%85%E5%99%A8+%E8%83%B6+%E6%95%99%E7%A8%8B)

## Assembly order

<EmiSearch query="@create" />

![Cloud Skipper airship build](images/visual-assembled-airship.png)

<ItemGrid><ItemIcon id="simulated:physics_assembler" /><ItemIcon id="simulated:honey_glue" /><ItemIcon id="create:super_glue" /><ItemIcon id="simulated:contraption_diagram" /><ItemIcon id="simulated:navigation_table" /></ItemGrid>

<Recipe id="simulated:physics_assembler" />

<Recipe id="offroad:borehead_bearing" />

Sable vehicles begin as ordinary connected blocks. Keep the first build small: a hull, a reachable control position and the equipment needed for one movement test. A train uses the station workflow in [Railway building](transport.railway-builder.md), not this assembler.

1. Build a connected hull away from terrain and other structures you do not want to include. Use <ItemLink id="create:super_glue" /> where parts need to be joined.
2. Place <ItemLink id="simulated:physics_assembler" /> against the intended structure and use its assembly action. Check that the complete intended hull becomes one moving sublevel and no dock blocks were included.
3. Before installing thrust, confirm that the assembled object can be moved and that its controls are reachable. Add the machinery for [airships](vehicles.airships.md), [underwater travel](vehicles.water.md) or [spaceflight](space.vehicle-transfer.md) only after that basic test.
4. For rebuilding, bring the vehicle to a clear supported position and disassemble through an assembler. The original assembler does not have to remain aboard.

Do not glue the craft to the launch platform. A missing part or an attached piece of terrain is an assembly problem, not something to compensate for with a larger engine.

## Moving a body before it flies

A new body starts as one block. Assemble it once, then build the rest onto the assembled block, so every part joins the same physics object from the first piece instead of being glued together later.

<ItemGrid><ItemIcon id="simulated:iron_handle" /><ItemIcon id="simulated:physics_assembler" /><ItemIcon id="simulated:honey_glue" /></ItemGrid>

Small bodies can be punched around, but mass rises with size, so fit an <ItemLink id="simulated:iron_handle" /> and sneak use it to drag the body where you want it. Drag first, then finish the hull, because a half-built body is lighter than a finished one.

Diagonal steps stay attached, so a stair-shaped hull does not need a glued strip on every step. A part with no connection in any direction breaks off as its own separate body, which is how a glued joint failing in flight looks on the ground.

## Connections and splitting

### Docking

<ItemGrid><ItemIcon id="simulated:docking_connector" /></ItemGrid>

### Ropes and couplings

<ItemGrid><ItemIcon id="simulated:rope_winch" /><ItemIcon id="simulated:rope_connector" /><ItemIcon id="simulated:rope_coupling" /></ItemGrid>

### Joining and articulation

<ItemGrid><ItemIcon id="minecraft:slime_ball" /><ItemIcon id="simulated:swivel_bearing" /><ItemIcon id="simulated:spring" /></ItemGrid>

Two bodies stay separate unless you join them. Use a <ItemLink id="minecraft:slime_ball" /> to select and merge Simulated Contraptions. Sneak-use clears the selection. Disconnected sections of one body can split off into separate bodies when their connecting joint is broken.

Docking connectors join a moving body to a fixed one. Rope parts tow and tether, and the swivel bearing and spring absorb the movement between two bodies instead of passing it through the frame.

| Part | Holds what to what | Use it for |
| --- | --- | --- |
| <ItemLink id="simulated:docking_connector" /> | Moving body to a fixed dock | Mooring an airship or loading a barge |
| <ItemLink id="simulated:rope_winch" /> and <ItemLink id="simulated:rope_connector" /> | Two points along a rope | Towing and securing a load |
| <ItemLink id="simulated:swivel_bearing" /> | Two bodies that must rotate | A trailed car or a swinging mount |
| <ItemLink id="simulated:spring" /> | Two bodies that must move apart and back | Suspension and shock absorption |

## Wheels

<ItemGrid><ItemIcon id="offroad:wheel_mount" /><ItemIcon id="offroad:small_tire" /><ItemIcon id="offroad:tire" /><ItemIcon id="offroad:large_tire" /><ItemIcon id="offroad:monstrous_tire" /><ItemIcon id="offroad:borehead_bearing" /></ItemGrid>

A <ItemLink id="offroad:wheel_mount" /> takes one tire on its front face. The pack refuses a tire placed anywhere else, so aim at the mount face that points away from the chassis. Mounts carry the body, they do not drive it, so a rolling chassis still needs a propeller, thruster or engine and a steering input.

<ItemLink id="offroad:borehead_bearing" /> spins a cutting head for excavation. It is a work attachment, not a wheel.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Aeronautics](images/catalog-owak0q19.png) [Create Aeronautics](vehicles.assembly.md) | Turns block-built vehicles into controllable physical moving structures. | No separate item search |
