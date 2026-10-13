---
navigation:
  title: "提供液体燃烧燃料"
  position: 9
  parent: reference.machines-storage.md
  icon: minecraft:lava_bucket
---

# 提供液体燃烧燃料

## 统一燃料

<EmiSearch query="@create" />

![下界传送门旁的 Create 流体储罐](images/feedback-nether-tanks.png)

下界传送门旁的 Create 流体储罐

![烈焰燃烧室的流体供给](images/feedback-liquid-fuel.png)

烈焰燃烧室的流体供给

Create: Unified Fuels 通过共享燃料分类与生成的兼容数据连接受支持的燃料设备，不增加独立机器或物品目录。对应扩展存在时，所选版本涵盖 The Factory Must Grow、Crafts & Additions 燃烧室、Liquid Fuel 与 Stuff 'N Additions 燃料箱等系统。

设备能否使用燃料仍取决于设备、流体分类与实际配方。炼油中间产物、工艺化学品与蒸汽不会自动变成可燃燃料。不要假定任意流体都能驱动所有引擎或让所有燃烧室超级加热。连接共用燃料供应前，请检查配方浏览器。

- [材料与燃料](power.industry.md)

***

## 燃烧器与流体供应

<ItemGrid>
  <ItemIcon id="create:blaze_burner" />
  <ItemIcon id="create:fluid_tank" />
  <ItemIcon id="create:fluid_pipe" />
  <ItemIcon id="create:mechanical_pump" />
  <ItemIcon id="minecraft:lava_bucket" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create:blaze_burner" /> | Create 烈焰人燃烧室提供热量。Create: Liquid Fuel 扩展此燃烧室，并不增加独立机器。 |
| <ItemLink id="create:fluid_tank" />, <ItemLink id="create:fluid_pipe" />, <ItemLink id="create:mechanical_pump" /> | 储罐、管道与泵提供流体供应。 |
| <ItemLink id="minecraft:lava_bucket" /> | 该版本液体燃料定义接受熔岩并提供普通加热，而非超级加热。桶图标代表流体。 |

***

## 初次使用

### 空燃烧室

<Recipe id="create:crafting/kinetics/empty_blaze_burner" />

先制作 <ItemLink id="create:empty_blaze_burner" />。此时还不是装有烈焰人的 <ItemLink id="create:blaze_burner" />，需要用空燃烧室捕获烈焰人，再供应燃料。

从捕获烈焰人的燃烧室开始，并检查熔岩供给线路。不要假定柴油、汽油或所有油类都能使用。Unified Fuels 可以增加兼容条目，但每种设备仍有各自接受的流体。接燃料管线前，请在物品浏览器确认实际流体。燃烧室布局与加热状态请看 Create 思索演示。

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | 让机械动力烈焰人燃烧室使用泵入的液体燃料。 | 无独立物品查询 |
| <ItemImage id="create:crushing_wheel" /> [Create: Unified Fuels](power.burners.md) | 连接支持的 Create 燃料系统，不增加独立物品系列。 | 无独立物品查询 |
