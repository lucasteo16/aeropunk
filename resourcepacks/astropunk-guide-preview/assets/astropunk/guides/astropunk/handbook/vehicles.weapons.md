---
navigation:
  title: "Mounted weapons"
  position: 9
  parent: reference.vehicles.md
  icon: minecraft:dispenser
---

# Mounted weapons

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Big+Cannons+Mounted+weapons+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Big+Cannons+%E5%AE%89%E8%A3%85%E5%92%8C%E6%93%8D%E4%BD%9C%E8%BD%BD%E5%85%B7%E6%AD%A6%E5%99%A8+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## Cannon assembly

<EmiSearch query="@createbigcannons" />

![Cannons mounted on a ship](images/feedback-mounted-cannons.png)

Cannons mounted on a ship

<ItemGrid><ItemIcon id="createbigcannons:cannon_mount" /><ItemIcon id="createbigcannons:steel_cannon_barrel" /><ItemIcon id="createbigcannons:steel_sliding_breech" /><ItemIcon id="createbigcannons:bronze_autocannon_barrel" /><ItemIcon id="createbigcannons:autocannon_ammo_container" /></ItemGrid>

A large cannon is a barrel, a chamber, a breech and a mount, built in that order. The barrel is the length, the chamber holds the charge, the breech is what you open to load, and the mount is what the whole thing pivots on.

| Family | Parts | Fires |
| --- | --- | --- |
| Cast iron | Barrel, chamber, breech | Cheap early guns |
| Bronze | Barrel, chamber, breech | Autocannon work |
| Steel | Barrel, sliding breech | Standard ship gun |
| Nethersteel | Barrel, chamber, breech | The heavy end |

Families do not mix. A steel barrel will not seat a bronze breech, so decide the family before you start casting.

Mount it with the <ItemLink id="createbigcannons:cannon_mount" /> on an assembled body. On a Sable ship the mount is what makes the gun follow the hull, and the recoil is scaled by the pack's potato cannon setting only for that weapon, so a large cannon does not throw the ship the way the potato cannon does.

## Loading and firing

The load order is powder, then projectile, then close. Open the breech, insert the charge, insert the shell, close the breech, then give the mount a redstone signal to fire. A gun that clicks but does not fire is usually empty, or the breech is still open.

The <ItemLink id="createbigcannons:autocannon_ammo_container" /> feeds an autocannon a belt of rounds so it can fire repeatedly without reloading each shot. Point it into the feed and load the container instead of the breech.

<Recipe id="createbigcannons:ap_shot" />

## Ammunition

<EmiSearch query="@create_radar" />

<ItemGrid><ItemIcon id="createbigcannons:ap_shell" /><ItemIcon id="createbigcannons:ap_shot" /><ItemIcon id="createbigcannons:bag_of_grapeshot" /><ItemIcon id="createbigcannons:big_cartridge" /><ItemIcon id="create_radar:guided_fuze" /></ItemGrid>

| Round | Job | Target |
| --- | --- | --- |
| <ItemLink id="createbigcannons:ap_shell" /> | Pierces armour | Armoured ships and blocks |
| <ItemLink id="createbigcannons:ap_shot" /> | Solid impact | Structures |
| <ItemLink id="createbigcannons:bag_of_grapeshot" /> | Spread at short range | Crew and light craft |
| <ItemLink id="createbigcannons:big_cartridge" /> | Complete charge and round | Fast reloading |

Match the round to the bore. A shell that does not fit the barrel is a shell you cannot load, and the recipe browser shows which family each round belongs to.

## Aircraft weapons

<EmiSearch query="@aeroengineering" />

<ItemGrid><ItemIcon id="aeroengineering:missile_assembly_station" /><ItemIcon id="aeroengineering:air_to_air_missile" /><ItemIcon id="aeronautics:mounted_potato_cannon" /></ItemGrid>

AeroEngine supplies a <ItemLink id="aeroengineering:missile_assembly_station" /> and an <ItemLink id="aeroengineering:air_to_air_missile" />. The missile is fired from the aircraft radar lock, so build the station before you plan an intercept.

The <ItemLink id="aeronautics:mounted_potato_cannon" /> is the light option. Its recoil is a pack setting of 0.2, which is enough to nudge a small hull and not enough to stop a large one.

## Aiming

<ItemGrid><ItemIcon id="create_radar:auto_yaw_controller" /><ItemIcon id="create_radar:auto_pitch_controller" /><ItemIcon id="create_radar:fire_controller" /></ItemGrid>

Point the gun with a yaw and pitch controller from [Radar](vehicles.radar.md), and let the fire controller pull the trigger when the barrel is on target. Firing by hand from a moving deck works, but the shot inherits the ship's motion.

***

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Big Cannons](images/catalog-gwp4jcjj.png) [Create Big Cannons](vehicles.weapons.md) | Adds buildable large cannons and their ammunition to Create. | <EmiSearch query="@createbigcannons" /> |
