---
navigation:
  title: "查看照明与管理刷怪"
  position: 0
  parent: reference.building.md
  icon: minecraft:torch
---

# 查看照明与管理刷怪

## 照明与生成

<EmiSearch query="@torchmaster" />

<ItemGrid>
  <ItemIcon id="torchmaster:megatorch" />
  <ItemIcon id="torchmaster:dreadlamp" />
  <ItemIcon id="torchmaster:feral_flare_lantern" />
  <ItemIcon id="torchmaster:frozen_pearl" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="torchmaster:megatorch" /> |
| <ItemLink id="torchmaster:dreadlamp" /> |
| <ItemLink id="torchmaster:feral_flare_lantern" /> |
| <ItemLink id="torchmaster:frozen_pearl" /> |

Mega Torch 抑制自然生成的敌对生物，Dread Lamp 抑制自然生成的被动生物。Feral Flare Lantern 放置隐形光源，Frozen Pearl 清理残留光源。作用半径及刷怪笼行为取决于服务器设置，不能保证阻止所有遭遇。

### 生成抑制

<Recipe id="torchmaster:megatorch" />

制作 <ItemLink id="torchmaster:megatorch" />，用于抑制自然生成的敌对生物，而非仅提供普通照明。

***

## 光照显示

Lighty 显示方块光照与天空光照，支持数字、地毯与叉形模式。使用 <KeyBind id="key.lighty.enable" /> 打开菜单，或使用 <KeyBind id="key.lighty.toggle" /> 切换显示。耕地显示用于检查生长光照，不会改变照明或阻止生物生成。

***

## 制作

<Recipe id="torchmaster:frozen_pearl" />

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Lighty](images/catalog-yjvkidnm.png) [Lighty](building.safety.md) | 叠加显示光照等级，帮助寻找暗处与可生成生物的地面。 | 无独立物品查询 |
| ![TorchMaster](images/catalog-tl8esrhx.png) [TorchMaster](building.safety.md) | 增加用于控制区域内敌对或其他生物生成的方块。 | <EmiSearch query="@torchmaster" /> |
