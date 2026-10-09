---
navigation:
  title: "加工矿石与原料"
  position: 0
  parent: reference.machines-storage.md
  icon: create:crushing_wheel
item_ids:
  - create:millstone
  - create:crushing_wheel
  - create:encased_fan
  - create:crushed_raw_iron
---

# 加工矿石与原料

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
