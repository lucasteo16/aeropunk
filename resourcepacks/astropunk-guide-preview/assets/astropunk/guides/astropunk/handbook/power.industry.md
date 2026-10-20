---
navigation:
  title: "Materials & fuels"
  position: 10
  parent: reference.machines-storage.md
  icon: minecraft:iron_ingot
---

# Materials & fuels

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+TFMG+Community+Edition+Materials+%26+fuels+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+TFMG+Community+Edition+%E5%B7%A5%E4%B8%9A%E6%9D%90%E6%96%99%E4%B8%8E%E7%87%83%E6%96%99%E7%B3%BB%E7%BB%9F+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## Coke before steel

<EmiSearch query="@tfmg" /> <EmiSearch query="@create" />

Create: The Factory Must Grow starts with a coke oven, because steel needs coke and coke needs coal. The oven is a square multiblock, from one block up to six by six, and every oven block must face the same way.

<Recipe id="tfmg:crafting/materials/coke_oven" />

<ItemGrid><ItemIcon id="tfmg:coke_oven" /><ItemIcon id="tfmg:coal_coke" /><ItemIcon id="tfmg:creosote_bucket" /><ItemIcon id="minecraft:coal" /><ItemIcon id="tfmg:casting_basin" /><ItemIcon id="tfmg:industrial_mixer" /><ItemIcon id="tfmg:steel_chemical_vat" /><ItemIcon id="tfmg:copper_cable_hub" /><ItemIcon id="tfmg:steel_distillation_output" /><ItemIcon id="tfmg:steel_fluid_tank" /><ItemIcon id="tfmg:steel_pipe" /></ItemGrid>

| Rule | Why it matters |
| --- | --- |
| Square shape | Rectangles do not assemble |
| All blocks face one way | The output side is the marked face |
| Pump carbon dioxide from the top | It accumulates and blocks the process |
| Pump creosote from another side | It is a byproduct with its own use |

A larger square finishes a batch faster and produces less creosote per item, according to the official wiki. A small oven is the right first build, and a larger one is a throughput decision later.

***

## Steel needs hot air

The blast furnace turns iron into molten steel and silicon, and it will not run on fuel alone. It needs a supply of hot air for each process, so the air heater is part of the build rather than an upgrade.

<ItemGrid><ItemIcon id="tfmg:blast_furnace_output" /><ItemIcon id="tfmg:blast_furnace_hatch" /><ItemIcon id="tfmg:blast_stove" /><ItemIcon id="tfmg:fireproof_bricks" /></ItemGrid>

| Part | Role |
| --- | --- |
| <ItemLink id="tfmg:blast_furnace_output" /> | The output block, the face everything points at |
| <ItemLink id="tfmg:blast_furnace_hatch" /> | Input and access point |
| <ItemLink id="tfmg:blast_stove" /> | Supplies the hot air |
| <ItemLink id="tfmg:fireproof_bricks" /> and reinforcement | The shell, and the speed upgrade |

The furnace consumes fuel on a fixed timer while it is running, and reinforcement blocks make each process faster. Build it beside the coke oven so coke arrives without a trip, and keep the hatch reachable for a funnel.

***

## Oil, distillation and engines

<ItemGrid><ItemIcon id="tfmg:surface_scanner" /><ItemIcon id="tfmg:pumpjack_base" /><ItemIcon id="tfmg:industrial_pipe" /><ItemIcon id="tfmg:steel_distillation_controller" /><ItemIcon id="tfmg:regular_engine" /><ItemIcon id="tfmg:large_engine" /></ItemGrid>

| Stage | Part |
| --- | --- |
| Find a deposit | <ItemLink id="tfmg:surface_scanner" /> reports oil under the chunk |
| Extract | <ItemLink id="tfmg:pumpjack_base" /> with pipes and a drive |
| Move it | <ItemLink id="tfmg:industrial_pipe" /> rather than a bucket line |
| Split it | <ItemLink id="tfmg:steel_distillation_controller" /> with outputs |
| Cast or mix | <ItemLink id="tfmg:casting_basin" />, <ItemLink id="tfmg:industrial_mixer" />, <ItemLink id="tfmg:steel_chemical_vat" /> |
| Burn it | <ItemLink id="tfmg:regular_engine" />, <ItemLink id="tfmg:simple_large_engine" />, <ItemLink id="tfmg:large_engine" />, <ItemLink id="tfmg:radial_engine" />, <ItemLink id="tfmg:turbine_engine" /> |

Engines are rotation sources, not generators of electricity. Each family has its own fuel appetite, and the large engines accept less refined fuel while asking for a steady air supply. Follow the pumpjack entry before laying the extraction route, because the pipe layout is easier to copy than to derive.

***

## Its own electrical grid

<ItemGrid><ItemIcon id="tfmg:generator" /><ItemIcon id="tfmg:electric_motor" /><ItemIcon id="tfmg:heavy_electric_motor" /><ItemIcon id="tfmg:transformer" /><ItemIcon id="tfmg:voltmeter" /><ItemIcon id="tfmg:electricians_wrench" /></ItemGrid>

| Part | Job |
| --- | --- |
| <ItemLink id="tfmg:generator" /> | Produces electricity from rotation |
| <ItemLink id="tfmg:electric_motor" /> | Turns electricity back into rotation |
| <ItemLink id="tfmg:heavy_electric_motor" /> | The larger motor for heavy loads |
| <ItemLink id="tfmg:transformer" /> | Moves between voltage groups |
| <ItemLink id="tfmg:voltmeter" /> | Reads the industrial circuit |
| <ItemLink id="tfmg:electricians_wrench" /> | Configures the industrial electrical parts |
| <ItemLink id="tfmg:winding_machine" /> | Winds a spool around an input while rotation is supplied |
| <ItemLink id="tfmg:freezer" /> and <ItemLink id="tfmg:compressor" /> | Cooling and compression stages |

This grid is not the Electro Energetics grid. The two mods model electricity differently and their parts do not plug into each other, so pick one for a given building and keep it there. [Electricity](power.electricity.md) covers the other system.

Next step is heat, because the coke oven and the blast furnace both burn something. [Burners and fuel](power.burners.md) covers the heat side.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: TFMG Community Edition](images/tfmg-community-edition-icon.png) [Create: TFMG Community Edition](power.industry.md) | Expands Create with heavy industry and oil processing in a community-maintained fork. | <EmiSearch query="@tfmg" /> |
