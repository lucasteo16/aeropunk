---
navigation:
  title: "Space life support"
  position: 11
  parent: reference.vehicles.md
  icon: rocketnautics:space_helmet
item_ids:
  - rocketnautics:space_helmet
  - rocketnautics:jetpack
  - rocketnautics:copper_leg_thrusters
  - rocketnautics:copper_anchor_boots
  - cosmonauticsdeepair:gravity_generator
  - create_submarine:electrolyzer
  - create_submarine:oxygene_diffuser
---

# Space life support

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Cosmonautics+space+helmet+air+jetpack+oxygen+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Cosmonautics+%E5%A4%AA%E7%A9%BA%E5%A4%B4%E7%9B%94+%E7%A9%BA%E6%B0%94+%E5%96%B7%E6%B0%94%E8%83%8C%E5%8C%85+%E6%95%99%E7%A8%8B)

## Breathing kit

<EmiSearch query="@rocketnautics" /> <EmiSearch query="@create" />

<ItemGrid><ItemIcon id="create:copper_diving_helmet" /><ItemIcon id="create:copper_backtank" /><ItemIcon id="rocketnautics:space_helmet" /><ItemIcon id="rocketnautics:jetpack" /><ItemIcon id="create:netherite_backtank" /></ItemGrid>

Cosmonautics checks whether living entities can breathe in space and in its configured atmosphere bands. It uses Create diving equipment and stored air rather than a separate cabin-oxygen simulation. Equip a compatible helmet and charged air supply before launch. Cabin oxygen is supplied by the separate Deep Seas and Deep Air integration described below.

| Piece | Slot | Supplies |
| --- | --- | --- |
| <ItemLink id="create:copper_diving_helmet" /> | Head | Lets you breathe from a connected air source |
| <ItemLink id="create:copper_backtank" /> | Chest | Stored air, charged before flight |
| <ItemLink id="rocketnautics:space_helmet" /> | Head | Breathing from a pressurised source, plus an orbital display |
| <ItemLink id="rocketnautics:jetpack" /> | Chest | Pressurised air and personal thrust |

A Copper Diving Helmet and charged Copper Backtank are a craftable starting pair. The Space Helmet has no crafting recipe in this pack, so it is not required for this starting setup.

<Recipe id="create:crafting/appliances/copper_diving_helmet" />

<Recipe id="create:crafting/appliances/copper_backtank" />

## Jetpack

<Recipe id="rocketnautics:crafting/equipment/jetpack" />

<ItemGrid><ItemIcon id="rocketnautics:jetpack" /><ItemIcon id="minecraft:lava_bucket" /><ItemIcon id="create:spout" /></ItemGrid>

The <ItemLink id="rocketnautics:jetpack" /> burns Fuel. Alternate-click it with a Lava Bucket to refill, or fill it at a <ItemLink id="create:spout" />. Press <KeyBind id="key.rocketnautics.toggle_jetpack" /> to toggle the systems, and hold jump for a short burst of vertical thrust.

Worn, it also supplies pressurised air to equipment that needs it, and it drains Fuel slowly while doing so. That drain continues whether or not you have flight toggled on, so a long stay in vacuum empties the tank even if you never thrust.

## Sealed rooms

<EmiSearch query="@cosmonauticsdeepair" /> <EmiSearch query="@create_submarine" />

![Gravity equipment in a ship compartment](images/cosmo-gravity-room.png)

<ItemGrid><ItemIcon id="create_submarine:electrolyzer" /><ItemIcon id="create_submarine:oxygene_diffuser" /><ItemIcon id="cosmonauticsdeepair:gravity_generator" /></ItemGrid>

A ship can carry its own air. Build an intact sealed compartment inside the hull, then supply it.

| Machine | Needs | Gives |
| --- | --- | --- |
| <ItemLink id="create_submarine:electrolyzer" /> | Water and Forge Energy, or a shaft in its module slot | Oxygen |
| <ItemLink id="create_submarine:oxygene_diffuser" /> | Oxygen in its tank and a redstone signal | Breathable air in the sealed room |
| <ItemLink id="cosmonauticsdeepair:gravity_generator" /> | Forge Energy and a neighbouring redstone signal | Local gravity in the room |

Deep Air restores breathing while the submarine compartment is supplied and sealed. it does not seal a breach or generate oxygen. The selected Deep Seas diffuser has a fixed operating drain, not a volume-proportional one. Follow [Underwater travel](vehicles.water.md) for the oxygen supply and diffuser controls. Keep personal breathing equipment for leaving the compartment.

The gravity generator is a separate room function. It does not need a diffuser in the same room, but keep at least one room oxygenated so the compartment tracking stays valid.

<Recipe id="cosmonauticsdeepair:gravity_generator" />

<Recipe id="create_submarine:oxygen_diffuser" />

<Recipe id="create_submarine:electrolyzer" />
## Personal movement

<ItemGrid><ItemIcon id="rocketnautics:copper_leg_thrusters" /><ItemIcon id="rocketnautics:copper_anchor_boots" /></ItemGrid>

<ItemLink id="rocketnautics:copper_leg_thrusters" /> give flight and inertial dampeners from pressurised air, and they are four times as efficient in space as on the ground and twice as efficient underwater. Toggle the dampeners with <KeyBind id="key.rocketnautics.toggle_dampeners" />.

<ItemLink id="rocketnautics:copper_anchor_boots" /> hold you to a supporting floor except while you are actively flying. They do not create gravity for anyone else and they do not work in open air.

<Recipe id="rocketnautics:crafting/equipment/copper_leg_thrusters" />

<Recipe id="rocketnautics:crafting/equipment/copper_anchor_boots" />


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Cosmonautics: Deep Air](images/cosmo-rzqxjxfo-icon.png) [Cosmonautics: Deep Air](space.life-support.md) | Connects sealed Deep Seas compartments to space breathing and powered artificial gravity. | <EmiSearch query="@cosmonauticsdeepair" /> |
| ![Create Cosmonautics](images/cosmo-micg1ith-icon.png) [Create Cosmonautics](world.dimensions.md) | Adds orbital flight, the Moon, rocket and breathing equipment, and a planetary display. | <EmiSearch query="@rocketnautics" /> |
| ![Create Deep Seas](images/catalog-mva5q4qz.png) [Create Deep Seas](vehicles.water.md) | Adds marine vehicle components for Aeronautics boats and submarines. | <EmiSearch query="@create_submarine" /> |
