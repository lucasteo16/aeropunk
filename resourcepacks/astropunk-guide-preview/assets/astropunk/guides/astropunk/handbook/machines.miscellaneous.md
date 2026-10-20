---
navigation:
  title: "Tools & drones"
  position: 11
  parent: reference.machines-storage.md
  icon: create:wrench
---

# Tools & drones

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Stuff+Additions+portable+drill+refill+drone+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E9%99%84%E5%8A%A0%E7%89%A9%E5%93%81+%E4%BE%BF%E6%90%BA%E9%92%BB%E5%A4%B4+%E8%A1%A5%E7%BB%99+%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%95%99%E7%A8%8B)

## Refill and use a portable tool

<EmiSearch query="@create_sa" />

Fill a filling tank by right clicking a water source with it. Fueling tanks draw lava instead. Keep the filled tank in your inventory and the compatible tool in your main hand. Its fluid bar rises as it refills. Water and fuel use separate tank families.

| Tool | View | Use |
| --- | --- | --- |
| Portable Drill | <ItemGrid><ItemIcon id="create_sa:portable_drill" /></ItemGrid> | Hold it to mine blocks at high speed. It wears durability and is correct for drops except blocks tagged as requiring diamond tools |
| Grappling Whisk | <ItemGrid><ItemIcon id="create_sa:grapplin_whisk" /></ItemGrid> | Right click to launch the hook. A hooked hand pose indicates attachment |
| Copper Magnet | <ItemGrid><ItemIcon id="create_sa:copper_magnet" /></ItemGrid> | Hold in hand to attract nearby drops |
| Block Picker | <ItemGrid><ItemIcon id="create_sa:block_picker" /></ItemGrid> | With water stored, right click a block with empty space above it to lift it. Spawners and blocks with hardness fifty or more cannot be lifted. Keep the picker selected to carry it. Right click empty air to release. It settles into a free destination or drops resources if blocked. Do not use this as a promise of safe transport for filled containers. |

The drill's progress and the grappling whisk's fuel bar make consumption visible. Filling tanks carry water, fueling tanks carry fuel. Small, medium and large sizes differ in capacity. These are portable refill items, not placed recharge stations.

***

## Tanks and engines

<EmiSearch query="@create" />

| Family | View | Use |
| --- | --- | --- |
| Filling tanks | <ItemGrid><ItemIcon id="create_sa:small_filling_tank" /><ItemIcon id="create_sa:medium_filling_tank" /><ItemIcon id="create_sa:large_filling_tank" /><ItemIcon id="create_sa:creative_filling_tank" /></ItemGrid> | Carry water for tools |
| Fueling tanks | <ItemGrid><ItemIcon id="create_sa:small_fueling_tank" /><ItemIcon id="create_sa:medium_fueling_tank" /><ItemIcon id="create_sa:large_fueling_tank" /></ItemGrid> | Carry accepted fuel for tools |
| Fixed steam engine | <ItemGrid><ItemIcon id="create:steam_engine" /></ItemGrid> | The Create boiler engine, distinct from portable engine components |
| Portable engines | <ItemGrid><ItemIcon id="create_sa:steam_engine" /><ItemIcon id="create_sa:hydraulic_engine" /><ItemIcon id="create_sa:heat_engine" /></ItemGrid> | Select the engine matching the device. They are separate steam, hydraulic and heat variants |


***

## Deploy and control a drone

<ItemGrid><ItemIcon id="create_sa:brass_drone_item" /><ItemIcon id="create_sa:drone_controller" /><ItemIcon id="create_sa:brass_drill_head" /><ItemIcon id="create_sa:copper_magnet" /><ItemIcon id="create_sa:fan_component" /><ItemIcon id="create_sa:vault_component" /></ItemGrid>

1. Hold the Brass Drone in your main hand and right click a block's top face. The drone appears above it and belongs to you. Survival deployment consumes the item.
2. Right click the drone with an empty hand to pause or resume its movement. Hold the controller in either hand to guide your unpaused drone.
3. Press <KeyBind id="key.create_sa.increase_reach" /> to move its target farther along your line of sight, or <KeyBind id="key.create_sa.decrease_reach" /> to bring it closer. The defaults are the Up and Down keys. Press once per adjustment. Putting the controller away resets the reach and action.
4. Hold a Brass Drill Head, Copper Magnet, Fan Component or Vault Component and right click the drone to attach that enabled module. It appears on the drone and consumes one component outside creative mode.
5. Right click empty air with the controller to toggle the module action. For drilling, guide it above a breakable block and trigger the action. A removed block and drops confirm success. A successful drill action resets rather than continuing forever.

Right clicking the drone itself controls pausing, not the module action.

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Stuff+Additions+2.1.4+drone+controller+block+picker+guide) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Create+Stuff+Additions+%E6%97%A0%E4%BA%BA%E6%9C%BA+%E6%8E%A7%E5%88%B6%E5%99%A8+%E6%96%B9%E5%9D%97%E6%8B%BE%E5%8F%96%E5%99%A8+%E6%95%99%E7%A8%8B)

***

- [Material processing](machines.ore-processing.md) Fan media and processing.
- [Rotational power](machines.rotation.md) Fixed machine drives.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create Stuff 'N Additions](images/catalog-aq9quuqg.png) [Create Stuff 'N Additions](machines.miscellaneous.md) | Adds Create-themed powered equipment and wearable tools. | <EmiSearch query="@create_sa" /> |
