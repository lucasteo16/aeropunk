---
navigation:
  title: "加工矿石与原料"
  position: 4
  parent: reference.machines-storage.md
  icon: create:millstone
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# 加工矿石与原料

## 共享材料产物

<EmiSearch query="@createdeco" /> <EmiSearch query="@create" />

Almost Unified 在本整合包仅统一共享的安山合金板与锌板配方标签，优先使用 Create Deco 产物。它不统一所有金属、铂或 Witcher 装备。

原有物品仍显示在配方浏览器中，战利品也不统一。制作精确物品过滤器前，检查实际配方产物与接受的原料。材料名称相同，不代表两个物品都符合指定物品配方。

***

## 矿物加工机器

<ItemGrid>
  <ItemIcon id="create:millstone" />
  <ItemIcon id="create:crushing_wheel" />
  <ItemIcon id="create:encased_fan" />
</ItemGrid>

| 机器 | 加工方式 |
| --- | --- |
| <ItemLink id="create:millstone" /> | 磨碎 |
| <ItemLink id="create:crushing_wheel" /> | 粉碎 |
| <ItemLink id="create:encased_fan" /> | 配合水进行洗涤 |

机器排列和动力供应请看思索演示。

***

## 磨石

<Recipe id="create:crafting/kinetics/millstone" />

***

## 磨碎小麦

<ItemGrid>
  <ItemIcon id="minecraft:wheat" />
  <ItemIcon id="create:millstone" />
  <ItemIcon id="create:wheat_flour" />
  <ItemIcon id="minecraft:wheat_seeds" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="minecraft:wheat" /> |
| <ItemLink id="create:millstone" /> |
| <ItemLink id="create:wheat_flour" /> |
| <ItemLink id="minecraft:wheat_seeds" /> |

| 输入 | 产物 |
| --- | --- |
| 一个小麦 | 一份小麦粉 |
| 额外产物，概率百分之二十五 | 两份小麦粉 |
| 额外产物，概率百分之二十五 | 一份小麦种子 |

***

## 粉碎粗铁

<ItemGrid>
  <ItemIcon id="minecraft:raw_iron" />
  <ItemIcon id="create:crushing_wheel" />
  <ItemIcon id="create:crushed_raw_iron" />
  <ItemIcon id="create:experience_nugget" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="minecraft:raw_iron" /> |
| <ItemLink id="create:crushing_wheel" /> |
| <ItemLink id="create:crushed_raw_iron" /> |
| <ItemLink id="create:experience_nugget" /> |

| 输入 | 产物 |
| --- | --- |
| 一个粗铁 | 一个粉碎铁矿石 |
| 额外产物，概率百分之七十五 | 一个经验颗粒 |

***

## 洗涤铁矿石

<ItemGrid>
  <ItemIcon id="create:crushed_raw_iron" />
  <ItemIcon id="create:encased_fan" />
  <ItemIcon id="minecraft:water_bucket" />
  <ItemIcon id="minecraft:iron_nugget" />
  <ItemIcon id="minecraft:redstone" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="create:crushed_raw_iron" /> |
| <ItemLink id="create:encased_fan" /> |
| <ItemLink id="minecraft:water_bucket" /> |
| <ItemLink id="minecraft:iron_nugget" /> |
| <ItemLink id="minecraft:redstone" /> |

| 输入 | 产物 |
| --- | --- |
| 一个粉碎铁矿石 | 九个铁粒 |
| 额外产物，概率百分之七十五 | 一个红石 |

水是鼓风机的加工介质，不会消耗一桶水。原料输送和产物收集见物品输送。

- [物品输送](machines.logistics.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Almost Unified](images/catalog-sdasaqez.png) [Almost Unified](machines.ore-processing.md) | 仅统一共享的安山合金与锌板配方材料。 | 无独立物品查询 |
| ![Create](images/create-icon.png) [Create](machines.ore-processing.md) | 增加用于加工、运输与自动建造的旋转动力机器。 | <EmiSearch query="@create" /> |
