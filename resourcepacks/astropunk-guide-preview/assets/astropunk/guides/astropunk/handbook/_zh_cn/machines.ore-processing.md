---
navigation:
  title: "材料加工"
  position: 6
  parent: reference.machines-storage.md
  icon: create:millstone
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# 材料加工

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+mod+millstone+crushing+washing+tutorial+English) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E7%A3%A8%E7%9F%B3+%E7%B2%89%E7%A2%8E%E8%BD%AE+%E6%B4%97%E6%B6%A4+%E6%95%99%E7%A8%8B)

## 从磨石开始

<EmiSearch query="@create" />

<ItemLink id="create:millstone" /> 从上方接收物品，空手右键取出产物。先按[旋转动力](machines.rotation.md)中的水车、竖直齿轮箱和向上传动轴布置，将磨石直接放在轴上方，再从顶部投入一份小麦。齿轮转动并产生面粉，就说明首次加工成功。

<Recipe id="create:crafting/kinetics/millstone" />

| 机器 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="create:millstone" /> | <ItemGrid><ItemIcon id="create:millstone" /></ItemGrid> | 一次一件，顶部输入，空手右键取出 |
| <ItemLink id="create:crushing_wheel" /> | <ItemGrid><ItemIcon id="create:crushing_wheel" /></ItemGrid> | 两个轮子相对旋转，顶部输入 |
| <ItemLink id="create:encased_fan" /> | <ItemGrid><ItemIcon id="create:encased_fan" /></ItemGrid> | 在气流中加工传送带或压台上的物品 |
| <ItemLink id="create:mechanical_press" /> | <ItemGrid><ItemIcon id="create:mechanical_press" /></ItemGrid> | 压制压台、传送带或锅盆上的物品 |
| <ItemLink id="create:mechanical_mixer" /> | <ItemGrid><ItemIcon id="create:mechanical_mixer" /></ItemGrid> | 搅拌锅盆内物品 |

一份 <ItemLink id="minecraft:wheat" /> 固定产出一份 <ItemLink id="create:wheat_flour" />，另有独立的百分之二十五概率额外产出两份面粉，以及独立的百分之二十五概率产出一颗 <ItemLink id="minecraft:wheat_seeds" />。额外面粉判定成功时，总共得到三份面粉。

<EmiSearch query="小麦面粉" />

选择匹配结果查看完整原料与概率产物。

***

## 粉碎、洗涤与风扇介质

Ponder 的 Processing Items with Crushing Wheels 课程说明，物品从顶部投入两个相对转动的轮子之间。粉碎 <ItemLink id="minecraft:raw_iron" /> 产出一份 <ItemLink id="create:crushed_raw_iron" />，并有百分之七十五概率得到 <ItemLink id="create:experience_nugget" />。洗涤粉碎粗铁会得到九颗 <ItemLink id="minecraft:iron_nugget" />，并有百分之七十五概率得到 <ItemLink id="minecraft:redstone" />。

| 风扇介质 | 外观 | 操作 |
| --- | --- | --- |
| 水 | <ItemGrid><ItemIcon id="minecraft:water_bucket" /></ItemGrid> | 洗涤物品 |
| 熔岩 | <ItemGrid><ItemIcon id="minecraft:lava_bucket" /></ItemGrid> | 高炉烧炼，但会摧毁气流中的食物 |
| 火或营火 | <ItemGrid><ItemIcon id="minecraft:campfire" /></ItemGrid> | 烟熏物品 |
| 灵魂火或灵魂营火 | <ItemGrid><ItemIcon id="minecraft:soul_campfire" /></ItemGrid> | 缠魂物品 |

把选定介质放在气流路径中，让传送带或压台带着物品穿过。气流方向与范围取决于旋转。风扇转速影响范围，不影响加工速度。加工食物时用火烟熏，不要用熔岩高炉。

***

## 原位压制与混合

把 <ItemLink id="create:depot" /> 放在压机下方可压制单件物品，或用 <ItemLink id="create:basin" /> 压制填满的二乘二或三乘三合成配方。部分锅盆配方需要 <ItemLink id="create:blaze_burner" /> 加热。没有有效出料龙头时，锅盆会保留产物。装有龙头时，产物会导向下方侧面。

| 工作台 | 外观 | 用途 |
| --- | --- | --- |
| 压台 | <ItemGrid><ItemIcon id="create:depot" /></ItemGrid> | 在压机下方托住物品堆 |
| 锅盆 | <ItemGrid><ItemIcon id="create:basin" /></ItemGrid> | 容纳物品与流体批次，供上方搅拌器或压机加工 |
| 烈焰燃烧器 | <ItemGrid><ItemIcon id="create:blaze_burner" /></ItemGrid> | 为要求加热的锅盆配方供热 |

混合时把搅拌器放在锅盆上方，并让上部齿轮与传动齿轮咬合。根据搅拌器提示提供所需转速，查看出料龙头或锅盆内保留的产物确认完成。准确的混合或压制配方请查配方浏览器。

<ItemLink id="create:andesite_alloy" /> 是扩建加工工坊前常用的合成材料。

- [旋转动力](machines.rotation.md) 第一套传动与应力。
- [物品与流体输送](machines.logistics.md) 传送带与物品移动。
- [烹饪工具](food.utensils.md) 食物专用准备方式。

***

## 实用加工配方

<Recipe id="stam1ocreatetweaks:blasting/blue_dye" />

<EmiSearch query="幻翼膜" />

<EmiSearch query="棕色蘑菇方块" />

<EmiSearch query="红色蘑菇方块" />

| 加工方式 | 原料 | 产物 |
| --- | --- | --- |
| 灵魂火气流缠魂 | 一根 <ItemLink id="minecraft:feather" /> | 一片 <ItemLink id="minecraft:phantom_membrane" /> |
| 压机与工作盆压实 | 四个 <ItemLink id="minecraft:brown_mushroom" /> | 一个 <ItemLink id="minecraft:brown_mushroom_block" /> |
| 压机与工作盆压实 | 四个 <ItemLink id="minecraft:red_mushroom" /> | 一个 <ItemLink id="minecraft:red_mushroom_block" /> |
| 高炉烧炼 | 一个 <ItemLink id="minecraft:prismarine_shard" /> | 一份 <ItemLink id="minecraft:blue_dye" /> |

蓝色染料配方见上方配方卡。缠魂和压实配方可在配方浏览器中查找以下产物后，选择对应产物的加工配方。幻翼膜使用灵魂火气流，蘑菇块使用工作盆上方已供能的压机。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Almost Unified](images/catalog-sdasaqez.png) [Almost Unified](machines.ore-processing.md) | 仅统一共享的安山合金与锌板配方材料。 | 无独立物品查询 |
| ![Create](images/create-icon.png) [Create](machines.ore-processing.md) | 增加用于加工、运输与自动建造的旋转动力机器。 | <EmiSearch query="@create" /> |
| ![Create: Stam1o Tweaks](images/catalog-46rgf8h2.png) [Create: Stam1o Tweaks](machines.ore-processing.md) | 调整机械动力配方，并让潜水靴抵消漂浮效果。 | 无独立物品查询 |
