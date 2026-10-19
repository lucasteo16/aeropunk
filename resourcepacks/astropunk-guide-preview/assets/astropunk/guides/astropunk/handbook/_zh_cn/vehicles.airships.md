---
navigation:
  title: "建造与平衡飞行船"
  position: 7
  parent: reference.vehicles.md
  icon: minecraft:elytra
---

# 建造与平衡飞行船

## 密闭体积产生升力

<EmiSearch query="@aeroencasedpipe" /> <EmiSearch query="@ballastmod" />

![不同船体与升力布置的飞艇](images/visual-airship-designs.png)

不同船体与升力布置的飞艇

<ItemGrid><ItemIcon id="aeronautics:white_envelope" /><ItemIcon id="aeronautics:adjustable_burner" /><ItemIcon id="aeronautics:steam_vent" /><ItemIcon id="aeronautics:levitite" /><ItemIcon id="aeronautics:levitite_blend" /><ItemIcon id="ballastmod:ballast_stones" /><ItemIcon id="aeroencasedpipe:white_envelope_encased_pipe" /><ItemIcon id="aeronautics:white_envelope_encased_shaft" /><ItemIcon id="simulated:white_symmetric_sail" /></ItemGrid>

<ItemLink id="aeronautics:white_envelope" /> 本身不产生升力。气囊方块构成外壳，被包住的空气方块才会充满热气。本包给热气的升力是每立方米 1.5 千克，所以浮力取决于被包住的体积，而不是方块数量。

三条规则决定气囊能不能用。

1. 外壳必须气密。气囊方块、包壳传动轴和包壳流体管道都算气密。
2. 热气从上往下填充。五层气囊的第三层破了一个洞，就只有上面两层被充满。
3. 气囊内部的建筑会占用体积。桅杆、管道和走道要留在外壳外面。

对着气囊使用染料即可上色。再用同一种颜色会把染料扩散到相邻气囊，整只气囊因此可以很快染完。

<Recipe id="aeronautics:adjustable_burner" />
## 燃烧器与排汽口

<Recipe id="aeronautics:white_envelope" />

<ItemLink id="aeronautics:adjustable_burner" /> 装在气囊下方，收到红石信号后向气囊充入热气。输入面板设定最大输出，本包上限为 500，红石强度按比例下调这一输出。多台燃烧器可以向同一只气囊叠加，大船体因此才有可用的爬升率。

燃烧器最多搜索 80 格找到气囊，所以吊舱里的燃烧器也能供给甲板上方的气囊。<ItemLink id="aeronautics:steam_vent" /> 是蒸汽方案，上限为 5000，不需要火。

气压随高度下降，升力也随之下降。气囊不会一直保持同样的爬升速度，<ItemLink id="simulated:altitude_sensor" /> 正是读取气压与精确高度的仪表。

## 浮岩

<ItemLink id="aeronautics:levitite" /> 是第三种升力来源，提供固定的反重力，并带有低速强、高速弱的阻力。单靠浮岩能把船体托住，却不能让它爬升，所以它常用来托起重船体，再由螺旋桨推动。用火、烈焰燃烧器或营火加热 <ItemLink id="aeronautics:levitite_blend" /> 会凝固成浮岩，凝固后的方块无法再采集。用作模具的黏土会在凝固过程中被消耗。

| 升力来源 | 提供 | 本包限制 |
| --- | --- | --- |
| 热气气囊 | 由密闭体积产生升力 | 每立方米 1.5 千克，燃烧器输出 500 |
| 蒸汽排汽口 | 用蒸汽产生同样的升力 | 输出 5000，不需要火 |
| 浮岩 | 固定升力与低速阻力 | 无法自行爬升 |
| 压舱石 | 通过增加质量抵消升力 | 最多八层 |

## 配平与推力

<ItemGrid><ItemIcon id="aeronautics:propeller_bearing" /><ItemIcon id="aeronautics:gyroscopic_propeller_bearing" /><ItemIcon id="aeronautics:wooden_propeller" /><ItemIcon id="aeronautics:andesite_propeller" /><ItemIcon id="aeronautics:smart_propeller" /></ItemGrid>

<ItemLink id="ballastmod:ballast_stones" /> 每加一层就增加质量，最多八层。用它设定静止高度，让气囊停在一个高度，而不是在爬升与失速之间来回起伏。

前进靠螺旋桨。<ItemLink id="aeronautics:propeller_bearing" /> 能带动至少两块帆面组成的结构，帆面越多推力越大。反转旋转方向就反转推力。倒装的 <ItemLink id="aeronautics:gyroscopic_propeller_bearing" /> 能稳定头重脚轻的船体，红石信号会把倾角归零。

## 视角与身体倾斜

Aeronautics Camera Sync 让视角跟随倾斜甲板，Aeronautics Player Tilt 让身体一起转。两者都不操控飞船。

| 操作 | 你的按键 | 默认 |
| --- | --- | --- |
| 切换视角倾斜 | <KeyBind id="key.aero_cam_sync.toggle" /> | I |
| 切换身体倾斜 | <KeyBind id="key.aero_player_tilt.toggle" /> | O |
| 视角设置 | <KeyBind id="key.aero_cam_sync.open_config" /> | 未绑定 |
| 身体倾斜设置 | <KeyBind id="key.aero_player_tilt.open_config" /> | 未绑定 |


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:minecart" /> [Aeronautics Camera Sync](vehicles.airships.md) | 让镜头与旋转的 Sable 飞船同步。 | 无独立物品查询 |
| <ItemImage id="minecraft:minecart" /> [Aeronautics Player Tilt](vehicles.airships.md) | 调整玩家朝向及下落行为，使其适应 Sable 子空间。 | 无独立物品查询 |
| ![Create Aeronautics: Encased Fluid Pipes](images/catalog-ddalvt8m.png) [Create Aeronautics: Encased Fluid Pipes](vehicles.airships.md) | 允许用 Aeronautics 热气囊包覆机械动力流体管道。 | <EmiSearch query="@aeroencasedpipe" /> |
| ![Create: Ballast](images/catalog-5ypxyrfg.png) [Create: Ballast](vehicles.airships.md) | 增加可叠层压载方块，用于调整载具质量与平衡。 | <EmiSearch query="@ballastmod" /> |
