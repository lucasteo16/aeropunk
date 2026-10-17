# Dimension borders

DimWorldBorder 1.1.1 is selected for Minecraft 1.21.1 and NeoForge. Native Modrinth project `KNfZi3IU`, version `gfbd1zeB`. The released universal artifact declares the selected Minecraft and NeoForge versions compatible and has no additional required library mods.

Include it in both exports so single-player administrators have the integrated-server functionality. Multiplayer clients do not need it when the server has it.

It provides independent vanilla-style boundaries rather than teleporting players away from ships. Sable ship interaction remains untested; a physical player barrier does not by itself prove ship collision containment.

No border sizes, centers or damage settings are changed in this batch. Keep the existing `astropunk-border` safety data pack unchanged. Its load-time Overworld cap must be checked against the mod's saved presets and restart behavior before relying on the combination. Never use a distributed server configuration to overwrite an administrator's saved border choices.

Commands, typed in game with operator permission:

```text
/dimworldborder minecraft:overworld get
/dimworldborder minecraft:overworld set 5000
/dimworldborder minecraft:the_nether get
/dimworldborder minecraft:the_end get
/dimworldborder rocketnautics:moon get
```

The number passed to `set` is the full square width. Use tab completion to confirm custom dimension identifiers in the running installation.

Before stable promotion, use a copied world to check separate dimension sizes and centers, saved settings after restart, synchronization after dimension travel, safety data pack behavior after reload, and a crewed Sable ship approaching the boundary. World data, played installations and stable branches are not modified by pack authoring.

Sources:

- https://modrinth.com/mod/dimworldborder
- https://gitlab.com/elifian/dimworldborder
