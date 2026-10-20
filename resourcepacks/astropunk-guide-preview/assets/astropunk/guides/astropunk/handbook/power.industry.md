---
navigation:
  title: "Steel & oil"
  position: 8
  parent: reference.machines-storage.md
  icon: minecraft:iron_ingot
---

# Steel & oil

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+coke+oven+blast+furnace+oil+engines) · [中文](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+%E7%84%A6%E7%82%AD%E7%82%89+%E9%AB%98%E7%82%89+%E7%9F%B3%E6%B2%B9+%E5%BC%95%E6%93%8E)

## Make coke first

<EmiSearch query="@tfmg" />

The Coke Oven Ponder shows coal inserted from any side. Carbon dioxide exits at the top, creosote can be extracted from another face, and coal coke eventually falls from the machine. Use a row of ovens when the slow output must scale.

<ItemGrid><ItemIcon id="tfmg:coke_oven" /><ItemIcon id="tfmg:coal_coke" /><ItemIcon id="tfmg:creosote_bucket" /></ItemGrid>

<Recipe id="tfmg:crafting/materials/coke_oven" />

<ItemLink id="minecraft:coal" /> is the coke oven input.

***

## Build a working blast furnace

The Blast Furnace Ponder describes a fireproof-brick cylinder with a blast-furnace output and a hatch. Reinforcements are required for operation, not merely a speed upgrade. Insert material through the opening at the top. Use the hatch for the hot-air input. A second hatch at the top can collect furnace gas, with inserted items falling into the furnace.

<ItemGrid><ItemIcon id="tfmg:fireproof_bricks" /><ItemIcon id="tfmg:blast_furnace_output" /><ItemIcon id="tfmg:blast_furnace_hatch" /><ItemIcon id="tfmg:blast_stove" /></ItemGrid>

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+blast+furnace+reinforcement+hot+air) · [中文](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+%E9%AB%98%E7%82%89+%E5%BC%BA%E5%8C%96+%E7%83%AD%E9%A3%8E)

The Blast Stove Ponder assigns its faces: fuel enters from below, air from the side, and hot air exits above. Carbon dioxide accumulates and can stall the stove, so route it to a nearby smokestack or exhaust. Confirm hot air reaches the furnace before feeding an iron batch.

***

## Find oil and distill it

Power the Surface Scanner from below with a Machine Input. Its top grid represents nearby chunks, with the current chunk at the centre. Chunks containing an oil deposit should light within seconds. Use chunk borders to identify the target.

<ItemGrid><ItemIcon id="tfmg:surface_scanner" /><ItemIcon id="tfmg:pumpjack_base" /><ItemIcon id="tfmg:industrial_pipe" /></ItemGrid>

The Pumpjack Ponder route begins with industrial pipe from the deposit to the surface. Put the pumpjack base on that pipe, place the hammer holder behind it, assemble the connector and head over the crank and base, join the hammer parts, and super glue the assembly. Finish with a Machine Input and crank above it to provide drive.

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+pumpjack+crude+oil+distillation+tower) · [中文](https://www.youtube.com/results?search_query=The+Factory+Must+Grow+Community+1.3.2a+%E6%8A%BD%E6%B2%B9%E6%9C%BA+%E5%8E%9F%E6%B2%B9+%E8%92%B8%E9%A6%8F%E5%A1%94)

For the distillation tower, assemble steel tanks as the base, place the Steel Distillation Controller beside them, then add up to six Distillation Outputs with industrial pipes between them. Put a heat source below the tanks, feed oil into the controller, and use the tower dial to confirm power. Outputs leave through the Distillation Outputs and pipes.

<ItemGrid><ItemIcon id="tfmg:steel_distillation_controller" /><ItemIcon id="tfmg:steel_distillation_output" /><ItemIcon id="tfmg:steel_fluid_tank" /><ItemIcon id="tfmg:industrial_pipe" /></ItemGrid>

***

## Choose a process attachment

The Chemical Vat takes attachments that change its job. Insert the mixer blade for mixing. Two electrode holders with copper electrodes make an electrolyzer. Three graphite electrodes make a blast furnace. Some recipes require heating.

<ItemGrid><ItemIcon id="tfmg:steel_chemical_vat" /><ItemIcon id="tfmg:industrial_mixer" /><ItemIcon id="tfmg:copper_electrode" /><ItemIcon id="tfmg:graphite_electrode" /></ItemGrid>

<ItemGrid><ItemIcon id="tfmg:casting_basin" /></ItemGrid>

For metal casting, supply molten steel to the casting basin and leave enough output space, since its internal storage is limited.

***

## Operate engines and winding machines

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+TFMG+Community+1.3.2a+regular+engine+turbine+engine+setup) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+TFMG+%E5%BC%95%E6%93%8E+%E6%B6%A1%E8%BD%AE%E5%BC%95%E6%93%8E+%E5%BB%BA%E9%80%A0+%E7%87%83%E6%96%99+%E6%95%99%E7%A8%8B)

A regular engine is assembled by the Ponder, its type cycles with an empty schematic, and matching cylinders complete it. Clicking the assembled engine with a shaft creates its kinetic output. Use the tutorial links above for the regular and turbine layouts. Their fuel and connections are not interchangeable with the large engine.

<ItemGrid><ItemIcon id="tfmg:regular_engine" /><ItemIcon id="tfmg:radial_engine" /><ItemIcon id="tfmg:turbine_engine" /><ItemIcon id="tfmg:large_engine" /><ItemIcon id="tfmg:simple_large_engine" /></ItemGrid>

Large engines require a shaft output, fuel from the side, continuous air, and carbon dioxide exhaust. Use the engine tooltip to confirm supported fuel for the particular engine.

The Winding Machine takes a spool by right-click, then an input item by right-click to place it. Supply rotation. Winding starts and stops when complete. Funnels insert input items and extract outputs, while deployers insert spools.

<ItemGrid><ItemIcon id="tfmg:winding_machine" /><ItemIcon id="tfmg:empty_spool" /><ItemIcon id="tfmg:machine_input" /><ItemIcon id="tfmg:engine_cylinder" /></ItemGrid>

***

## Wire the industrial workshop

<EmiSearch query="@create" />

Drive a generator from your shaft network, connect an industrial consumer through the matching cable system, then use the Configuration Wrench on electrical blocks to assign groups. Components sharing a group split voltage. Separate groups retain the full voltage. A motor turning is the first useful result. The transformer, potentiometer and switch create subnetworks, so use their own Ponder entries before expanding the circuit.

| Part | View | Use |
| --- | --- | --- |
| <ItemLink id="tfmg:generator" /> | <ItemGrid><ItemIcon id="tfmg:generator" /></ItemGrid> | Converts shaft rotation into industrial electricity |
| <ItemLink id="tfmg:electric_motor" /> | <ItemGrid><ItemIcon id="tfmg:electric_motor" /></ItemGrid> | Converts industrial electricity into rotation |
| <ItemLink id="tfmg:heavy_electric_motor" /> | <ItemGrid><ItemIcon id="tfmg:heavy_electric_motor" /></ItemGrid> | Heavy electric-motor family |
| <ItemLink id="tfmg:copper_cable_hub" /> | <ItemGrid><ItemIcon id="tfmg:copper_cable_hub" /></ItemGrid> | Cable connection point for the industrial network |
| <ItemLink id="tfmg:transformer" /> | <ItemGrid><ItemIcon id="tfmg:transformer" /></ItemGrid> | Changes subnetwork voltage using the primary and secondary turns ratio |
| <ItemLink id="tfmg:voltmeter" /> | <ItemGrid><ItemIcon id="tfmg:voltmeter" /></ItemGrid> | Reads the industrial electrical network |
| <ItemLink id="tfmg:electricians_wrench" /> | <ItemGrid><ItemIcon id="tfmg:electricians_wrench" /></ItemGrid> | Right click an electrical block to open its group configuration |
| <ItemLink id="tfmg:freezer" /> | <ItemGrid><ItemIcon id="tfmg:freezer" /></ItemGrid> | Cooling-process machine |
| <ItemLink id="tfmg:compressor" /> | <ItemGrid><ItemIcon id="tfmg:compressor" /></ItemGrid> | Compression and air-supply machinery |
| <ItemLink id="tfmg:steel_pipe" /> | <ItemGrid><ItemIcon id="tfmg:steel_pipe" /></ItemGrid> | Steel fluid-pipe family, distinct from Industrial Pipe |

- [Electricity](power.electricity.md) for the separate Electro Energetics circuit system. TFMG has its own grouped electrical behavior. Converters may bridge systems, so do not assume they are universally incompatible.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: TFMG Community Edition](images/tfmg-community-edition-icon.png) [Create: TFMG Community Edition](power.industry.md) | Expands Create with heavy industry and oil processing in a community-maintained fork. | <EmiSearch query="@tfmg" /> |
