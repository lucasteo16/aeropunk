---
navigation:
  title: "Electrical circuits"
  position: 5
  parent: reference.machines-storage.md
  icon: minecraft:lightning_rod
---

# Electrical circuits

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+Electro+Energetics+1.1.3+electricity+guide) · [中文](https://www.youtube.com/results?search_query=Minecraft+Create+Electro+Energetics+1.1.3+%E7%94%B5%E5%8A%9B%E6%95%99%E7%A8%8B)

## Build the alternator

<EmiSearch query="@electroenergetics" /> <EmiSearch query="@create" />

Create: Electro Energetics converts rotation to electricity at an alternator. In the Ponder lesson Setting up an alternator, surround the rotors with stators, then connect rotational drive.

<ItemGrid><ItemIcon id="electroenergetics:alternator_rotor" /><ItemIcon id="electroenergetics:stator" /><ItemIcon id="electroenergetics:alternator_brushes" /></ItemGrid>

For the physical arrangement, open the lesson rather than guessing the rotor and stator layout.

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+alternator+stator+rotor+setup) · [中文](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+%E5%8F%91%E7%94%B5%E6%9C%BA+%E5%AE%9A%E5%AD%90+%E8%BD%AC%E5%AD%90+%E5%AE%89%E8%A3%85)

***

## Close the first circuit

<ItemGrid><ItemIcon id="electroenergetics:connector" /><ItemIcon id="electroenergetics:copper_wire_spool" /><ItemIcon id="electroenergetics:blue_electric_motor" /><ItemIcon id="electroenergetics:bulb" /></ItemGrid>

1. Place electrical connectors at the alternator output and at a bulb or blue electric motor.
2. Use the copper wire spool to connect alternator positive to the load, then connect the load return to alternator negative. Both legs are required for a closed circuit.
3. Start the rotation source. A lit bulb or turning motor is a direct first success.
4. Use Connecting Wires in Ponder to learn how to remove a wire with an empty spool.

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+closed+circuit+copper+wire+connectors+blue+electric+motor) · [中文](https://www.youtube.com/results?search_query=Create+Electro+Energetics+1.1.3+%E9%97%AD%E5%90%88%E7%94%B5%E8%B7%AF+%E9%93%9C%E7%BA%BF+%E6%8E%A5%E7%BA%BF%E7%AB%AF+%E8%93%9D%E8%89%B2%E7%94%B5%E5%8A%A8%E6%9C%BA)

***

## Protect, measure, and transform

| Component | View | Use |
| --- | --- | --- |
| <ItemLink id="electroenergetics:fuse_holder" /> | <ItemGrid><ItemIcon id="electroenergetics:fuse_holder" /></ItemGrid> | Holds a protective fuse in series |
| <ItemLink id="electroenergetics:voltmeter" /> | <ItemGrid><ItemIcon id="electroenergetics:voltmeter" /></ItemGrid> | Connect in parallel across two points to read their voltage difference |
| <ItemLink id="electroenergetics:ammeter" /> | <ItemGrid><ItemIcon id="electroenergetics:ammeter" /></ItemGrid> | Insert in series to measure current |
| <ItemLink id="electroenergetics:clamp_meter" /> | <ItemGrid><ItemIcon id="electroenergetics:clamp_meter" /></ItemGrid> | Right-click a wire to read current without breaking it |
| <ItemLink id="electroenergetics:transformer_core" /> | <ItemGrid><ItemIcon id="electroenergetics:transformer_core" /></ItemGrid> | Core for a configured transformer assembly |
| <ItemLink id="electroenergetics:high_voltage_capacitor" /> | <ItemGrid><ItemIcon id="electroenergetics:high_voltage_capacitor" /></ItemGrid> | High-voltage energy storage component |
| <ItemLink id="electroenergetics:accumulator" /> | <ItemGrid><ItemIcon id="electroenergetics:accumulator" /></ItemGrid> | Stores electrical energy, connect positive to positive and negative to negative |
| <ItemLink id="electroenergetics:emergency_stop_button" /> | <ItemGrid><ItemIcon id="electroenergetics:emergency_stop_button" /></ItemGrid> | Right-click to engage and open its internal switch, shift right-click to disengage |

The transformer core lesson requires radiator panels around the core and transformer oil over it to increase its power rating. Do not exceed that rating. A voltmeter reads between two points, not an absolute voltage at one point.

***

## Choose the next electrical component

After the first circuit works, add only the component your next job needs. A transformer changes voltage by its configured ratio. A regulator has separate source, ground and load terminals, so wiring it like a two-terminal bulb will not work.

| Part | View | Use |
| --- | --- | --- |
| <ItemLink id="electroenergetics:fuse" /> | <ItemGrid><ItemIcon id="electroenergetics:fuse" /></ItemGrid> | Fit inside a Fuse Holder in the circuit path |
| <ItemLink id="electroenergetics:insulated_wire" /> | <ItemGrid><ItemIcon id="electroenergetics:insulated_wire" /></ItemGrid> | Insulated wiring material |
| <ItemLink id="electroenergetics:capacitor" /> | <ItemGrid><ItemIcon id="electroenergetics:capacitor" /></ItemGrid> | Electrical capacitor component |
| <ItemLink id="electroenergetics:electric_pump" /> | <ItemGrid><ItemIcon id="electroenergetics:electric_pump" /></ItemGrid> | Electric fluid-pumping machine |
| <ItemLink id="electroenergetics:transformer" /> | <ItemGrid><ItemIcon id="electroenergetics:transformer" /></ItemGrid> | Set its ratio to step voltage up or down |
| <ItemLink id="electroenergetics:voltage_regulator" /> | <ItemGrid><ItemIcon id="electroenergetics:voltage_regulator" /></ItemGrid> | Source connects at the top input, negative at the bottom ground, load at the output, then close the return circuit |

***

## Supply the railway

<ItemGrid><ItemIcon id="electroenergetics:catenary_holder" /><ItemIcon id="electroenergetics:pantograph" /><ItemIcon id="electroenergetics:rail_contact_shoe" /></ItemGrid>

For overhead supply, connect positive to the catenary and negative to a ground rod. An electric train needs its motor and a pantograph touching the catenary. A rail contact shoe is the selected Ponder's third-rail alternative. See [passenger rail](transport.passenger.md) for train operation.

- [Steel and oil](power.industry.md) for furnaces, oil processing and engines.

***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Electro Energetics](images/create-electro-energetics-icon.png) [Create: Electro Energetics](power.electricity.md) | Adds electricity generation, transmission and powered machinery, including electric trains. | <EmiSearch query="@electroenergetics" /> |
