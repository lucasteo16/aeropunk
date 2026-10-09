---
navigation:
  title: "提供液体燃烧燃料"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
---

# 提供液体燃烧燃料

## 燃烧器与流体供应

<EmiSearch query="@create" />

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

从捕获烈焰人的燃烧室开始，并检查熔岩供给线路。不要假定柴油、汽油或所有油类都能使用。所选 Liquid Fuel 文件仅定义熔岩及来自其他模组的特定联动流体。接燃料管线前，请在物品浏览器确认实际流体。燃烧室布局与加热状态请看 Create 思索演示。

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create: Liquid Fuel](images/create-liquid-fuel-icon.png) [Create: Liquid Fuel](power.burners.md) | 让机械动力烈焰人燃烧室使用泵入的液体燃料。 | 已安装基准版 | 无独立物品查询 |
