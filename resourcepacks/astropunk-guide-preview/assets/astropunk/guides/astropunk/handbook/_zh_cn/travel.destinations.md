---
navigation:
  title: "使用固定与便携传送点"
  position: 13
  parent: reference.vehicles.md
  icon: minecraft:ender_pearl
---

# 使用固定与便携传送点

## 传送石网络

<EmiSearch query="@waystones" />

![山巅上的传送石](images/visual-mountaintop-waystone.png)

山巅上的传送石

<ItemGrid><ItemIcon id="waystones:waystone" /><ItemIcon id="waystones:mossy_waystone" /><ItemIcon id="waystones:deepslate_waystone" /><ItemIcon id="waystones:blackstone_waystone" /><ItemIcon id="waystones:sandy_waystone" /><ItemIcon id="waystones:red_nether_bricks_waystone" /><ItemIcon id="waystones:end_stone_waystone" /><ItemIcon id="waystones:mud_bricks_waystone" /><ItemIcon id="waystones:prismarine_waystone" /><ItemIcon id="waystones:purpur_waystone" /></ItemGrid>

<ItemLink id="waystones:waystone" /> 只有在你使用过一次之后才成为目的地。第一次使用会激活它并加入你的列表。未激活的石头不会出现在传送界面，这也是明明看得见的基地却不在列表里的常见原因。

材质只是外观。苔石、深板岩、黑石、砂岩、下界砖或末地石传送石与普通传送石行为相同。确认之前先看界面上的经验消耗与冷却，不要一路点过去。

## 随身与共享传送

<ItemGrid><ItemIcon id="waystones:warp_stone" /><ItemIcon id="waystones:blank_scroll" /><ItemIcon id="waystones:orange_sharestone" /><ItemIcon id="waystones:white_portstone" /><ItemIcon id="waystones:warp_plate" /><ItemIcon id="waystones:dormant_shard" /><ItemIcon id="waystones:attuned_shard" /></ItemGrid>

| 物品 | 范围 | 用法 |
| --- | --- | --- |
| <ItemLink id="waystones:warp_stone" /> | 个人，通往任意已激活石头 | 使用后打开列表 |
| <ItemLink id="waystones:blank_scroll" /> | 个人，单个目的地 | 对传送石使用以绑定 |
| <ItemLink id="waystones:orange_sharestone" /> | 群体，同色石头之间 | 连接相同颜色 |
| <ItemLink id="waystones:white_portstone" /> | 仅作为出发点 | 用目的地名额换取通行 |
| <ItemLink id="waystones:warp_plate" /> | 成对传送板 | 在一块中充能碎片，带到另一块 |

<ItemLink id="waystones:warp_plate" /> 是其中唯一不需要两端有传送石就能在两点间移动的方式。在第一块板中为 <ItemLink id="waystones:dormant_shard" /> 充能，再对第二块使用 <ItemLink id="waystones:attuned_shard" />。用下面的配方给共享石换色，就能把它归入另一组。

<Recipe id="waystones:orange_sharestone_recolor" />

## Tempad

<EmiSearch query="@tempad" />

![Tempad 传送设备](images/feedback-tempad.png)

Tempad 传送设备

<ItemGrid><ItemIcon id="tempad:tempad" /><ItemIcon id="tempad:location_card" /><ItemIcon id="tempad:timedoor_projector" /><ItemIcon id="tempad:workstation" /><ItemIcon id="tempad:chronon_generator" /><ItemIcon id="tempad:chronon_cell" /><ItemIcon id="tempad:card_wallet" /><ItemIcon id="tempad:chronometer" /><ItemIcon id="tempad:chronon_battery" /><ItemIcon id="tempad:location_broadcaster" /><ItemIcon id="tempad:timedoor_marker" /></ItemGrid>

<ItemLink id="tempad:tempad" /> 保存 <ItemLink id="tempad:location_card" /> 条目，并通过 <ItemLink id="tempad:timedoor_projector" /> 打开通往其中一处的门。它是坐标系统，不是网络。保存的位置是固定点，不会跟随移动的船，也不知道目的地是否仍然安全。

能量来自时间粒子设备。<ItemLink id="tempad:chronon_generator" /> 配 <ItemLink id="tempad:chronon_cell" /> 是固定供电，<ItemLink id="tempad:workstation" /> 用来制作卡片与设备。穿门之前先在 Tempad 界面确认卡片。

## 移动目的地

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="waystones:waystone" /><ItemIcon id="simulated:physics_assembler" /></ItemGrid>

Waystones: Sable 让传送石能随已组装载体移动。把传送石装在船上并激活，它就会出现在 Sable 分组里。它把玩家传送到移动中的石头，而不是把船传送到别的维度。

Create: AeroWarptics 在同一维度内迁移已组装的船。两者都不是跨维度搬运整艘船。跨维度请见[轨道飞行](space.vehicle-transfer.md)。

## 如何选择

<ItemGrid><ItemIcon id="minecraft:obsidian" /></ItemGrid>

| 需求 | 使用 |
| --- | --- |
| 常回的基地网络 | 传送石 |
| 朋友共用一处基地 | 共享石 |
| 两端都没有传送石的两点 | 传送板 |
| 随身携带的坐标列表 | Tempad |
| 随船移动的目的地 | Waystones: Sable |

***

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Waystones Recipes](images/catalog-wqpkgqnj.png) [Create Waystones Recipes](travel.destinations.md) | 修改 Waystones 配方，改用机械动力材料与制作方式。 | 无独立物品查询 |
| <ItemImage id="minecraft:minecart" /> [Create: AeroWarptics](travel.destinations.md) | 增加用于转移 Aeronautics 物理载具的工具。 | 无独立物品查询 |
| ![NetherPortalFix](images/catalog-npzr02et.png) [NetherPortalFix](travel.destinations.md) | 修正玩家往返下界传送门时的返回目的地。 | 无独立物品查询 |
| ![Tempad](images/catalog-gknwt7xu.png) [Tempad](travel.destinations.md) | 用便携及固定设备开启通往已保存地点的传送门。 | <EmiSearch query="@tempad" /> |
| ![Waystones](images/catalog-lopkhb2a.png) [Waystones](travel.destinations.md) | 增加需激活的目的地石碑与便携传送物品，支持地点间旅行。 | <EmiSearch query="@waystones" /> |
| ![Waystones: Sable (Create Aeronautics Addon)](images/catalog-bxhpgfck.png) [Waystones: Sable (Create Aeronautics Addon)](travel.destinations.md) | 修复 Sable 移动结构上的 Waystones 传送与目的地处理。 | 无独立物品查询 |
