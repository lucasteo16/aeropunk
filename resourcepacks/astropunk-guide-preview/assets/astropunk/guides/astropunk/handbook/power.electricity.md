---
navigation:
  title: "Electricity"
  position: 11
  parent: reference.machines-storage.md
  icon: minecraft:lightning_rod
---

# Electricity

## Rotation becomes voltage

<EmiSearch query="@electroenergetics" /> <EmiSearch query="@create" />

Create: Electro Energetics does not store a magical energy number. A source induces a voltage, a device lets current flow, and the current does the work. That is why a short circuit, a long thin wire and a badly matched transformer all change the result.

The alternator is the join between the two systems. Rotation turns it, and it produces current.

<ItemGrid><ItemIcon id="electroenergetics:alternator_rotor" /><ItemIcon id="electroenergetics:stator" /><ItemIcon id="electroenergetics:alternator_brushes" /><ItemIcon id="electroenergetics:accumulator" /><ItemIcon id="electroenergetics:capacitor" /><ItemIcon id="electroenergetics:high_voltage_capacitor" /><ItemIcon id="electroenergetics:transformer_core" /></ItemGrid>

| Part | Job |
| --- | --- |
| <ItemLink id="electroenergetics:alternator_rotor" /> | The turning part of an alternator |
| <ItemLink id="electroenergetics:stator" /> | The stationary winding around the rotor |
| <ItemLink id="electroenergetics:alternator_brushes" /> | Carries current to the moving part, with a three phase variant in the same family |
| <ItemLink id="electroenergetics:accumulator" /> | Stores charge for later draw |
| <ItemLink id="electroenergetics:capacitor" /> | A small buffer that smooths a changing draw |
| <ItemLink id="electroenergetics:high_voltage_capacitor" /> | The same role on a high voltage section |

Build the alternator on the same shaft line as your workshop. The Ponder entry for the alternator shows the assembled shape, and it is faster to follow that than to guess the block order.

***

## Wire a circuit in one direction

<ItemGrid><ItemIcon id="electroenergetics:connector" /><ItemIcon id="electroenergetics:copper_wire_spool" /><ItemIcon id="electroenergetics:insulated_wire" /><ItemIcon id="electroenergetics:fuse" /><ItemIcon id="electroenergetics:voltmeter" /><ItemIcon id="electroenergetics:ammeter" /></ItemGrid>

| Part | Use |
| --- | --- |
| <ItemLink id="electroenergetics:connector" /> | Termination point for a wire on a block |
| <ItemLink id="electroenergetics:copper_wire_spool" /> | Lays wire between connectors |
| <ItemLink id="electroenergetics:insulated_wire" /> | Wire for runs that need insulation |
| <ItemLink id="electroenergetics:fuse" /> with a fuse holder | Opens the circuit before a fault damages it |
| <ItemLink id="electroenergetics:fuse_holder" /> | Holds a fuse in the line |
| <ItemLink id="electroenergetics:voltmeter" /> | Reads the voltage at a point |
| <ItemLink id="electroenergetics:clamp_meter" /> | Reads current through a wire without breaking the run |
| <ItemLink id="electroenergetics:ammeter" /> | Reads the current through a point |

1. Place a connector on the alternator output and another on the machine.
2. Run a spool between them and watch the wire take the shape you drew.
3. Fit a fuse in its holder between source and load.
4. Read the voltmeter at the source, then at the load.

A voltage that falls between the two readings is the wire and the distance, not a broken machine. That is the difference between this and a fluid style power system, and the reason a meter is the first purchase rather than the last.

***

## Motors, pumps and heat

<ItemGrid><ItemIcon id="electroenergetics:blue_electric_motor" /><ItemIcon id="electroenergetics:electric_pump" /><ItemIcon id="electroenergetics:bulb" /><ItemIcon id="electroenergetics:transformer" /><ItemIcon id="electroenergetics:voltage_regulator" /></ItemGrid>

| Consumer | Gives you |
| --- | --- |
| Electric motor | Rotation without a shaft line, in several colors |
| <ItemLink id="electroenergetics:electric_pump" /> | Fluid movement at a distance from the workshop |
| <ItemLink id="electroenergetics:bulb" /> | Light and a visible sign that the circuit is live |
| Resistive heater | Heat for machines that want it |

A <ItemLink id="electroenergetics:transformer" /> changes voltage between sections, and a <ItemLink id="electroenergetics:voltage_regulator" /> holds a section steady. Put the transformer where the wire length changes, not at every machine.

The mod also converts between its own electricity and Forge Energy devices through a dedicated converter block, which is how it feeds machines from other mods. It runs its simulation off the main thread and keeps working in unloaded chunks, so a long transmission line between two bases behaves the same whether or not you stand beside it.

***

## Electrified rail

<ItemGrid><ItemIcon id="electroenergetics:pantograph" /><ItemIcon id="electroenergetics:rail_contact_shoe" /><ItemIcon id="electroenergetics:catenary_holder" /><ItemIcon id="electroenergetics:emergency_stop_button" /></ItemGrid>

| Part | Role |
| --- | --- |
| <ItemLink id="electroenergetics:catenary_holder" /> | Holds the overhead wire above the track |
| <ItemLink id="electroenergetics:pantograph" /> | Collects current from overhead wire |
| <ItemLink id="electroenergetics:rail_contact_shoe" /> | Collects current from a third rail |
| <ItemLink id="electroenergetics:emergency_stop_button" /> | Cuts the section by hand |

Electrified rail is a separate project from a workshop circuit. Run the overhead line first, test the pantograph on one short section, then extend. [Railways](transport.passenger.md) covers the trains themselves.

The next useful step, once a circuit is stable, is moving the same work into an industrial process line. [Industrial machinery](power.industry.md) covers that separate system.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Electro Energetics](images/create-electro-energetics-icon.png) [Create: Electro Energetics](power.electricity.md) | Adds electricity generation, transmission and powered machinery, including electric trains. | <EmiSearch query="@electroenergetics" /> |
