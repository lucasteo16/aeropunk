# Cosmonautics trial

This independent trial branches from lightweight main at a08434f. Main, heavy and the held Northstar branch remain unchanged.

Pack version: `0.5.0-test.cosmonautics.2`.

Additional selections:

- Create Cosmonautics `26.08.307`, Modrinth project `micg1iTH`, release `HuCMavv8`, published beta.
- Cosmonautics: Deep Air `1.0.2`, Modrinth project `rzqxJXfo`, release `IxjdMVIp`, localized breathing and gravity through the existing Create: Deep Seas systems.
- Create Cosmonautics Expansion `1.0.0`, Modrinth project `gD7M0IgY`, release `48ItKoZ3`, packaged Mars dimension.

All baseline mod metadata remains byte-identical. Northstar and its bridges are not included. Addon dependency bounds were inspected without overriding them. Deep Air declares an optional `cosmonautics` dependency while the selected base declares `rocketnautics`; this identifier discrepancy is retained for manual functional testing, not treated as proof the bridge works. Expansion website licensing and embedded licensing disagree; redistribution permission has not been established.

Released archive inspection confirmed packaged Moon and deep-space dimensions and bundled Dimensional Sable `1.0.5`. Required Minecraft, NeoForge, Create, Aeronautics and Sable dependencies are present in the baseline. The Create dependency declaration uses the unusual lower bound `1.21.1`; baseline Create `6.0.10` is above that bound. No dependency declarations were overridden.

Sources:

- https://modrinth.com/mod/create-cosmonatics/version/HuCMavv8
- https://www.curseforge.com/minecraft/mc-mods/create-cosmonautics/files/8612744
- https://github.com/CosmonauticsTeam/Create-Cosmonautics

Preparation and file verification do not establish startup or gameplay compatibility. Manual checks should cover fresh world entry, rendering with the player's chosen Distant Horizons setting, rocket construction and travel, passengers and inventories, then saving and reopening. Neither a game nor a server was launched during preparation.
