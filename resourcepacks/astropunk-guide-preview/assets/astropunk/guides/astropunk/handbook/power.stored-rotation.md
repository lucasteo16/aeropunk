---
navigation:
  title: "Stored rotation"
  position: 8
  parent: reference.machines-storage.md
  icon: create:flywheel
---

# Stored rotation

## A battery for rotation

<EmiSearch query="@create_connected" /> <EmiSearch query="@createsprings" /> <EmiSearch query="@create" />

A <ItemLink id="create_connected:kinetic_battery" /> stores rotation as stress and gives it back later. It charges while it has no redstone signal and discharges while powered, which means a lever decides when the reserve runs the line.

<ItemGrid><ItemIcon id="create_connected:kinetic_battery" /><ItemIcon id="create_connected:kinetic_bridge" /><ItemIcon id="create:stressometer" /><ItemIcon id="create:analog_lever" /><ItemIcon id="createsprings:kinetic_interface" /><ItemIcon id="createsprings:portative_steam_engine" /><ItemIcon id="createsprings:punchcard" /></ItemGrid>

| Part | Behaviour |
| --- | --- |
| <ItemLink id="create_connected:kinetic_battery" /> | Charges unpowered, discharges powered |
| <ItemLink id="create_connected:kinetic_bridge" /> | Moves capacity between two separate networks |
| <ItemLink id="create:stressometer" /> | Shows what the battery is doing to the network |
| <ItemLink id="create:analog_lever" /> | A clean way to switch discharge on |

In the current release the battery keeps its charge in item form and only releases the stress the network actually needs, so you can carry a charged battery to a distant site instead of building a shaft line there. Capacity, discharge speed and stress impact are all configurable, so two packs can legitimately disagree about the numbers.

***

## Springs store the same thing differently

A <ItemLink id="createsprings:spring" /> holds rotation and releases it on demand. The difference is control. A spring responds to signal strength, so a comparator or an analog lever can set why and how hard it releases.

<ItemGrid><ItemIcon id="createsprings:spring" /><ItemIcon id="createsprings:large_spring_coil" /><ItemIcon id="createsprings:spring_alloy" /><ItemIcon id="createsprings:unfinished_spring" /><ItemIcon id="createsprings:friction_welder" /><ItemIcon id="createsprings:spring_base" /><ItemIcon id="createsprings:spring_catapult" /><ItemIcon id="createsprings:spring_drill" /><ItemIcon id="createsprings:spring_fan" /><ItemIcon id="createsprings:spring_launcher" /><ItemIcon id="createsprings:spring_saw" /><ItemIcon id="createsprings:spring_shove" /></ItemGrid>

| Part | Job |
| --- | --- |
| <ItemLink id="createsprings:spring_alloy" /> | The material springs are made from |
| <ItemLink id="createsprings:unfinished_spring" /> | The form that becomes a spring |
| <ItemLink id="createsprings:friction_welder" /> | Applies the alloy to the unfinished spring |
| <ItemLink id="createsprings:large_spring_coil" /> | A larger coil for bigger reserves |

The released recipe applies spring alloy to an unfinished spring with the friction welder, which needs rotation. That makes the first spring a two step project, and it is why spring alloy is worth stockpiling before you want a dozen.

A spring can also release with enough force to break blocks. Keep splash mode, or any high setting, away from a normal reserve, and test the setting on a throwaway structure.

***

## Which reserve fits

<ItemGrid><ItemIcon id="create_connected:kinetic_battery" /><ItemIcon id="createsprings:spring" /></ItemGrid>

| Reserve | Best for |
| --- | --- |
| Kinetic Battery | A compact buffer on one network, switched by redstone |
| Spring | Signal controlled output, and moving a reserve to where it is needed |

A battery answers a stoppage. A spring answers a demand that changes. Most bases need one of the two, and the choice is about how the reserve should switch on.

The first action is a battery on a line that already runs, with a lever on its discharge side. Watch the stressometer fall when the source stops, and watch production continue.

Reserves do not create capacity out of nothing. [Rotational power](machines.rotation.md) owns the stress budget and the speed rules.


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Create: Springs](images/create-springs-icon.png) [Create: Springs](power.stored-rotation.md) | Stores rotational energy in springs for later use. | <EmiSearch query="@createsprings" /> |
