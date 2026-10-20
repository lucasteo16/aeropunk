---
navigation:
  title: "安装和操作载具武器"
  position: 9
  parent: reference.vehicles.md
  icon: minecraft:dispenser
---

# 安装和操作载具武器

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Big+Cannons+sliding+breech+muzzle+loading+cannon+mount+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Big+Cannons+%E6%BB%91%E5%8A%A8%E7%82%AE%E9%97%A9+%E5%89%8D%E8%A3%85+%E7%82%AE%E6%9E%B6+%E6%95%99%E7%A8%8B)

## 火炮组装

<EmiSearch query="@createbigcannons" /> <EmiSearch query="@create" />

![安装在船上的火炮](images/feedback-mounted-cannons.png)

<ItemGrid><ItemIcon id="createbigcannons:cannon_mount" /><ItemIcon id="createbigcannons:steel_cannon_barrel" /><ItemIcon id="createbigcannons:steel_sliding_breech" /><ItemIcon id="createbigcannons:bronze_autocannon_barrel" /><ItemIcon id="createbigcannons:autocannon_ammo_container" /></ItemGrid>

Big Cannons 火炮本身也需要组装：使用兼容的炮闩、药室和炮管，并通过 <ItemLink id="createbigcannons:cannon_mount" /> 安装。这一步与组装承载它的 Sable 船体是两件事。装弹前先查看炮架和炮闩的 Ponder。

| 武器家族 | 配套部件 | 先检查什么 |
| --- | --- | --- |
| 大型火炮 | 同类大型火炮的炮管、药室和炮闩材料 | 先完成所需加工与连接，再组装 |
| 自动炮 | 自动炮炮闩、复进簧和自动炮管 | 使用自动炮弹与对应弹药容器 |

青铜不只出现在一种武器家族中。材料同名不代表自动炮管能替代大型火炮管，不要只看颜色判断兼容性。

先在空旷靶场固定炮架，用 Ponder 确认组装信号和独立的开火输入，不是随便给某一面通电就完成。炮架、瞄准与装填循环验证通过后再装船。后坐力取决于具体武器，固定土豆炮的设置不能用来推断 Big Cannons 的后坐力。

## 装填与开火

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Big+Cannons+sliding+breech+loading+ramrod+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Big+Cannons+%E6%BB%91%E5%8A%A8%E7%82%AE%E9%97%A9+%E6%8E%A8%E5%BC%B9%E5%99%A8+%E8%A3%85%E5%A1%AB+%E6%95%99%E7%A8%8B)

<Recipe id="createbigcannons:ap_shot" />

装填方法由炮闩类型决定。上方滑动炮闩大型火炮使用从炮口一侧装填的流程：弹丸在前，发射药位于弹丸后方、靠近炮闩。用推弹器把装药推到发射位置，闭合炮闩，再通过炮架的开火输入发射。不要把所有炮闩都当成能依同一顺序塞入发射药和炮弹的开口。

先在空旷靶场使用适量兼容装药。无法开火时检查火炮是否已组装、炮闩是否闭合、弹药是否到位，以及炮架是否收到开火输入。不要靠增加装药来修复哑火。

<ItemLink id="createbigcannons:autocannon_ammo_container" /> 装的是自动炮弹。按自动炮炮闩的交互方式装填并连接，不是用来存放大型火炮炮弹的弹链。

## 弹药

<EmiSearch query="@create_radar" />

<ItemGrid><ItemIcon id="createbigcannons:ap_shell" /><ItemIcon id="createbigcannons:ap_shot" /><ItemIcon id="createbigcannons:bag_of_grapeshot" /><ItemIcon id="createbigcannons:big_cartridge" /><ItemIcon id="create_radar:guided_fuze" /></ItemGrid>

| 弹种 | 作用 | 目标 |
| --- | --- | --- |
| <ItemLink id="createbigcannons:ap_shell" /> | 穿甲 | 装甲船与方块 |
| <ItemLink id="createbigcannons:ap_shot" /> | 实心撞击 | 建筑结构 |
| <ItemLink id="createbigcannons:bag_of_grapeshot" /> | 近距离散布 | 人员与轻型载具 |
| <ItemLink id="createbigcannons:big_cartridge" /> | 发射药，不含弹丸 | 放在独立的兼容弹丸后方 |

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
