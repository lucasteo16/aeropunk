---
navigation:
  title: "安装和操作载具武器"
  position: 9
  parent: reference.vehicles.md
  icon: minecraft:dispenser
---

# 安装和操作载具武器

## 火炮组装

<EmiSearch query="@createbigcannons" />

![安装在船上的火炮](images/feedback-mounted-cannons.png)

安装在船上的火炮

<ItemGrid><ItemIcon id="createbigcannons:cannon_mount" /><ItemIcon id="createbigcannons:steel_cannon_barrel" /><ItemIcon id="createbigcannons:steel_sliding_breech" /><ItemIcon id="createbigcannons:bronze_autocannon_barrel" /><ItemIcon id="createbigcannons:autocannon_ammo_container" /></ItemGrid>

大型火炮由炮管、药室、炮闩和炮架组成，按这个顺序搭建。炮管决定长度，药室装发射药，炮闩是你打开装填的部分，炮架负责整个火炮的回转。

| 家族 | 部件 | 用途 |
| --- | --- | --- |
| 铸铁 | 炮管、药室、炮闩 | 便宜的前期火炮 |
| 青铜 | 炮管、药室、炮闩 | 自动炮作业 |
| 钢 | 炮管、滑动炮闩 | 标准舰炮 |
| 下界钢 | 炮管、药室、炮闩 | 重型端 |

各家族不能混用。钢炮管装不上青铜炮闩，所以在开炉之前就要定好家族。

把 <ItemLink id="createbigcannons:cannon_mount" /> 装在已组装的载体上。在 Sable 船上，炮架让火炮跟随船体，后坐力只按整合包里的土豆炮设置缩放那一种武器，所以大型火炮不会像土豆炮那样把船推开。

## 装填与开火

顺序是发射药、弹丸、闭闩。打开炮闩，放入发射药，放入炮弹，关上炮闩，然后给炮架红石信号开火。只响一声却不发射，通常是空膛，或者炮闩还开着。

<ItemLink id="createbigcannons:autocannon_ammo_container" /> 用弹链给自动炮持续供弹，不必每发都手动装填。把它对准进弹口，往容器里装弹即可。

<Recipe id="createbigcannons:ap_shot" />

## 弹药

<EmiSearch query="@create_radar" />

<ItemGrid><ItemIcon id="createbigcannons:ap_shell" /><ItemIcon id="createbigcannons:ap_shot" /><ItemIcon id="createbigcannons:bag_of_grapeshot" /><ItemIcon id="createbigcannons:big_cartridge" /><ItemIcon id="create_radar:guided_fuze" /></ItemGrid>

| 弹种 | 作用 | 目标 |
| --- | --- | --- |
| <ItemLink id="createbigcannons:ap_shell" /> | 穿甲 | 装甲船与方块 |
| <ItemLink id="createbigcannons:ap_shot" /> | 实心撞击 | 建筑结构 |
| <ItemLink id="createbigcannons:bag_of_grapeshot" /> | 近距离散布 | 人员与轻型载具 |
| <ItemLink id="createbigcannons:big_cartridge" /> | 药弹一体 | 快速装填 |

弹药要与口径配套。装不进炮管的炮弹就是无法装填的炮弹，配方浏览器会显示每种弹药属于哪个家族。

## 机载武器

<EmiSearch query="@aeroengineering" />

<ItemGrid><ItemIcon id="aeroengineering:missile_assembly_station" /><ItemIcon id="aeroengineering:air_to_air_missile" /><ItemIcon id="aeronautics:mounted_potato_cannon" /></ItemGrid>

AeroEngine 提供 <ItemLink id="aeroengineering:missile_assembly_station" /> 与 <ItemLink id="aeroengineering:air_to_air_missile" />。导弹依靠机载雷达锁定发射，所以要先造好组装台再计划拦截。

<ItemLink id="aeronautics:mounted_potato_cannon" /> 是轻量选择。它的后坐力在整合包里是 0.2，足以推动小船体，却推不动大船。

## 瞄准

<ItemGrid><ItemIcon id="create_radar:auto_yaw_controller" /><ItemIcon id="create_radar:auto_pitch_controller" /><ItemIcon id="create_radar:fire_controller" /></ItemGrid>

用[雷达](vehicles.radar.md)的偏航与俯仰控制器转动火炮，让火力控制器在炮口对准时触发。在移动甲板上手动开火也能用，但炮弹会带着船的速度。

***

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Big Cannons](images/catalog-gwp4jcjj.png) [Create Big Cannons](vehicles.weapons.md) | 为机械动力增加可组装的大炮与弹药。 | <EmiSearch query="@createbigcannons" /> |
