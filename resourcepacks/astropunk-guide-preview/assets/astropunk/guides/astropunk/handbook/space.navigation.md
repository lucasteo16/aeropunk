---
navigation:
  title: "Space navigation"
  position: 12
  parent: reference.vehicles.md
  icon: rocketnautics:hologram_block
item_ids:
  - rocketnautics:hologram_block
  - rocketnautics:sputnik
---

# Space navigation

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Space+navigation+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+%E5%A4%AA%E7%A9%BA%E5%AF%BC%E8%88%AA+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## Planetary display

<EmiSearch query="@rocketnautics" />

![Hologram planetary display](images/cosmo-hologram.png)

Hologram planetary display

<ItemLink id="rocketnautics:hologram_block" /> draws the system you are in. Short-click its configuration points to change the scale, and read the body you are aiming for before you burn fuel.

<ItemGrid><ItemIcon id="rocketnautics:hologram_block" /><ItemIcon id="rocketnautics:sputnik" /><ItemIcon id="rocketnautics:space_helmet" /></ItemGrid>

The display is a model, not a destination selector. Selecting a body on it does not steer the ship and does not open a transfer.

What the pack actually uses is the transfer height. The Overworld and the Moon both send a body to Deep Space at height 20,000, and the same height is where a descent from Deep Space comes back in. Aim for a body, cross the height, and you have moved.

## Bodies and gravity

<Recipe id="rocketnautics:hologram_block" />

The system data in this pack gives each body a surface acceleration. The Overworld is 11.0 and the Moon is 2.0, so a lander tuned for the Overworld falls faster than it expects on the Moon. A ship that hovers easily at home will climb faster and brake later there.

| Body | Surface acceleration | Note |
| --- | --- | --- |
| Overworld | 11.0 | Starting point, thick air |
| Moon | 2.0 | Low gravity, no thick air |
| Mars, gas giant, ice world | Listed in the display | Check before you commit |

Air also thins with height. Above 21,000 the pack marks the atmosphere as low density and applies drowning, so a crew without a sealed helmet and air supply stops breathing long before the crossing. Drag falls to zero by 7,000, which is why a propeller stops helping in the upper atmosphere and a rocket takes over.

## Probe and helmet

<ItemLink id="rocketnautics:sputnik" /> keeps chunks loaded and reports biome colours for mapping. It is a survey tool, not a pilot, and it does not fly a route for you.

In Deep Space the Space Helmet shows an orbital display. <KeyBind id="key.rocketnautics.toggle_alignment" /> toggles the alignment helper. That changes what you see, not where the ship points.

<Recipe id="rocketnautics:sputnik" />

## Reading a trip before launch

| Check | Why it decides the trip |
| --- | --- |
| Surface acceleration of the target | Sets how fast you fall and how much braking thrust you need |
| Helmet and charged air supply | Above 21,000 the air stops supporting breathing |
| Thrust that works without air | A propeller loses its medium by 7,000 |
| Assembled hull and running fuel feed | An unassembled build has no physics and a dry feed makes no thrust |


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
