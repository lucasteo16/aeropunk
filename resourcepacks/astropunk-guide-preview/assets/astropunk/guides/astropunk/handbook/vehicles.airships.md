---
navigation:
  title: "Airships"
  position: 7
  parent: reference.vehicles.md
  icon: minecraft:elytra
---

# Airships

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Aeronautics+envelope+balloon+burner+blazeboil+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Aeronautics+%E9%A3%9E%E8%89%87+%E6%B0%94%E5%9B%8A+%E7%87%83%E7%83%A7%E5%99%A8+%E6%B5%AE%E5%B2%A9+%E6%95%99%E7%A8%8B)

## Lift from a sealed volume

<EmiSearch query="@create" />

![Airships with different hulls and lift arrangements](images/visual-airship-designs.png)

Airships with different hulls and lift arrangements

### Envelope equipment

<ItemGrid><ItemIcon id="aeronautics:white_envelope" /><ItemIcon id="aeronautics:adjustable_burner" /><ItemIcon id="aeronautics:steam_vent" /></ItemGrid>

### Lift material and ballast

<EmiSearch query="@ballastmod" />

<ItemGrid><ItemIcon id="aeronautics:levitite" /><ItemIcon id="aeronautics:levitite_blend_bucket" /><ItemIcon id="ballastmod:ballast_stones" /></ItemGrid>

### Pass-throughs and sail

<EmiSearch query="@aeroencasedpipe" />

<ItemGrid><ItemIcon id="aeroencasedpipe:white_envelope_encased_pipe" /><ItemIcon id="aeronautics:white_envelope_encased_shaft" /><ItemIcon id="simulated:white_symmetric_sail" /></ItemGrid>

An <ItemLink id="aeronautics:white_envelope" /> does not lift by itself. Envelope blocks form the skin, and the enclosed air blocks fill with hot air. The pack gives hot air 1.5 kilograms of lift per cubic metre, so a balloon's lift is its trapped volume, not its block count.

Three rules decide whether a balloon works.

1. The skin must be airtight. Envelope blocks, envelope encased shafts and the encased fluid pipes all count.
2. Air fills from the top down. A hole in the third layer of a five layer balloon leaves only the top two layers filled.
3. Anything built inside the balloon reduces the trapped volume. Keep masts, pipes and walkways outside the skin.

Dye an envelope by using dye on it. Using the same colour again spreads the dye to the neighbouring envelopes, which is the quick way to paint a whole balloon.

<Recipe id="aeronautics:adjustable_burner" />
## Burner and vent

<Recipe id="aeronautics:white_envelope" />

A <ItemLink id="aeronautics:adjustable_burner" /> sits under the balloon and fills it with hot air when it has a redstone signal. Its input panel sets the maximum output, capped at 500 in this pack, and the redstone strength scales that output down proportionally. Several burners combine into one balloon, which is how large hulls get a usable climb rate.

The burner searches up to 80 blocks for its balloon, so a burner in the gondola can feed an envelope above the deck. A <ItemLink id="aeronautics:steam_vent" /> is the steam alternative, with a cap of 5000, and it does not need a fire.

Lift falls as air pressure falls. The balloon does not keep climbing at the same rate, and the <ItemLink id="simulated:altitude_sensor" /> is the instrument that reads both air pressure and exact height.

## Levitite

<ItemGrid><ItemIcon id="aeronautics:levitite" /><ItemIcon id="aeronautics:levitite_blend_bucket" /></ItemGrid>

<ItemLink id="aeronautics:levitite" /> is the third lift source. It provides a fixed anti-gravity force and a drag that is strong at low speed and weak at high speed. Levitite alone can hold a body up but cannot make it climb, so it is used to carry a heavy hull that a propeller then moves. Curing Levitite Blend with fire, a blaze burner or a campfire turns the fluid into Levitite, and the cured block cannot be collected again. Clay used as a mould is destroyed during curing.

| Lift source | Gives | Limit in this pack |
| --- | --- | --- |
| Hot air envelope | Lift from trapped volume | 1.5 kilograms per cubic metre, burner output 500 |
| Steam vent | The same lift from steam | Output 5000, no fire needed |
| Levitite | Fixed lift with low-speed drag | Cannot climb on its own |
| Ballast stones | Removes lift by adding mass | Eight layers |

## Trim and thrust

<ItemGrid><ItemIcon id="aeronautics:propeller_bearing" /><ItemIcon id="aeronautics:gyroscopic_propeller_bearing" /><ItemIcon id="aeronautics:wooden_propeller" /><ItemIcon id="aeronautics:andesite_propeller" /><ItemIcon id="aeronautics:smart_propeller" /></ItemGrid>

<ItemLink id="ballastmod:ballast_stones" /> gain mass with each added layer, up to eight. Use them to set the resting height so the balloon holds a level instead of porpoising between climb and stall.

Forward motion comes from a propeller. A <ItemLink id="aeronautics:propeller_bearing" /> turns any sail structure of at least two sail blocks, and more sails mean more thrust. Reverse the rotation to reverse the thrust. An upside down <ItemLink id="aeronautics:gyroscopic_propeller_bearing" /> stabilises a top-heavy hull, and a redstone signal resets its tilt to zero.


Aeronautics Camera Sync tilts the view with a sloping deck, and Aeronautics Player Tilt turns the body with it. Neither steers the ship.

| Action | Your key | Default |
| --- | --- | --- |
| Toggle camera tilt | <KeyBind id="key.aero_cam_sync.toggle" /> | I |
| Toggle player tilt | <KeyBind id="key.aero_player_tilt.toggle" /> | O |
| Camera settings | <KeyBind id="key.aero_cam_sync.open_config" /> | Unbound |
| Player tilt settings | <KeyBind id="key.aero_player_tilt.open_config" /> | Unbound |


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Aeronautics Camera Sync](vehicles.airships.md) | Synchronizes the camera with rotating Sable ships. | No separate item search |
| <ItemImage id="minecraft:minecart" /> [Aeronautics Player Tilt](vehicles.airships.md) | Aligns player orientation and falling behavior with Sable sublevels. | No separate item search |
| ![Create Aeronautics: Encased Fluid Pipes](images/catalog-ddalvt8m.png) [Create Aeronautics: Encased Fluid Pipes](vehicles.airships.md) | Lets Aeronautics hot air envelopes encase Create fluid pipes. | <EmiSearch query="@aeroencasedpipe" /> |
| ![Create: Ballast](images/catalog-5ypxyrfg.png) [Create: Ballast](vehicles.airships.md) | Adds layered ballast blocks for adjusting vehicle mass and balance. | <EmiSearch query="@ballastmod" /> |
