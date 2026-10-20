---
navigation:
  title: "Process heat"
  position: 7
  parent: reference.machines-storage.md
  icon: minecraft:lava_bucket
---

# Process heat

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+blaze+burner+feeding+liquid+fuel+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+%E7%87%83%E7%83%A7%E5%99%A8+%E6%B6%B2%E4%BD%93%E7%87%83%E6%96%99+%E6%95%99%E7%A8%8B)

## Heat for the machine above

<EmiSearch query="@create" />

<GameScene zoom="3" interactive={true}>
<Block id="create:blaze_burner" />
<Block y="1" id="create:basin" />
</GameScene>

A basin sits directly above its burner. This shows the heat connection, not a complete mixing machine.

A <ItemLink id="create:blaze_burner" /> supplies heat to the block directly above it. Heat is not shaft rotation or electricity. Craft an <ItemLink id="create:empty_blaze_burner" />, then right-click a Blaze with it to capture the Blaze, or use the Blaze spawner. The burner can then be placed beneath a heat-using machine.

<Recipe id="create:crafting/kinetics/empty_blaze_burner" />

| State or input | View | Result |
| --- | --- | --- |
| Empty cage | <ItemGrid><ItemIcon id="create:empty_blaze_burner" /></ItemGrid> | No heat |
| Captured Blaze | <ItemGrid><ItemIcon id="create:blaze_burner" /></ItemGrid> | Ordinary heat when fueled |
| <ItemLink id="create:blaze_cake" /> | <ItemGrid><ItemIcon id="create:blaze_cake" /></ItemGrid> | Superheated heat |

The burner state changes when it is working. Check the visible burner state and the machine above it, rather than inferring heat from a shaft turning.

***

## Feed it by hand or pipe

<ItemGrid><ItemIcon id="create:blaze_burner" /><ItemIcon id="minecraft:lava_bucket" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /></ItemGrid>

1. For a manual start, right-click the burner with a flammable item. To superheat, feed it a Blaze Cake.
2. For automated item feeding, use a Deployer or Mechanical Arm. A hopper or dropped item is not the documented feed method.
3. For fluid, connect a tank and burner with pipes, then drive a mechanical pump in the direction of the burner.

Lava supplies ordinary heat. Start the fluid route with lava. Fuel compatibility is specific to the burner and fuel form, so do not substitute another liquid merely because it burns in an industrial engine.

- [Steel and oil](power.industry.md) Coke, steel, oil processing and engines.
- [Rotational power](machines.rotation.md) The separate shaft network.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | Lets Create blaze burners consume pumped liquid fuel. | No separate item search |
| <ItemImage id="create:crushing_wheel" /> [Create: Unified Fuels](power.burners.md) | Connects supported Create fuel systems without adding a separate item catalog. | No separate item search |
