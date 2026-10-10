---
navigation:
  title: "法术与支援职业"
  position: 0
  parent: reference.skills.md
  icon: minecraft:blaze_rod
item_ids:
  - spell_engine:spell_binding
  - spell_engine:spell_book
  - spell_engine:spell_scroll
---

# 法术与支援职业

## 法术与支援职业

选择职业，查看定位、入门配方、法术书、完整招式、技能与装备。

- [奥秘法师](class.arcane.md)
- [火焰法师](class.fire.md)
- [冰霜法师](class.frost.md)
- [水系法师](class.aqua.md)
- [土系法师](class.terra.md)
- [风系法师](class.wind.md)
- [圣骑士](class.paladin.md)
- [牧师](class.priest.md)
- [吟游诗人](class.bard.md)
- [猎魔人](class.witcher.md)

***

## 法术绑定

<EmiSearch query="@spell_engine" />

<ItemGrid>
  <ItemIcon id="spell_engine:spell_binding" />
  <ItemIcon id="minecraft:book" />
  <ItemIcon id="minecraft:lapis_lazuli" />
  <ItemIcon id="minecraft:bookshelf" />
  <ItemIcon id="spell_engine:spell_book" />
  <ItemIcon id="spell_engine:spell_scroll" />
</ItemGrid>

<ItemLink id="spell_engine:spell_binding" />

<Recipe id="spell_engine:spell_binding_table" />

1. 在绑定台放入普通书，选择职业法术书。创建书籍会消耗经验等级。
2. 将职业法术书放回绑定台，从其法术池中选择招式。满足界面显示的等级要求、等级消耗、青金石消耗与书架能量要求。同阶冲突或槽位上限可能阻止选择。
3. 将已配置的书放入适用的法术书槽，并手持兼容武器或法器。手持物品会筛选可用法术。

书籍携带学会的招式。技能树点数用于强化构筑，不能代替法术绑定。卷轴应用是绑定台的另一种模式，有自己的要求。职业书是 <ItemLink id="spell_engine:spell_book" /> 的配置变体，不是单独注册的物品。

***

## 施法要求

查看每个法术提示中的学派、目标、施法时间、材料消耗与冷却。备好所需符文或弹药。即使法术属于该书，手持武器不兼容时仍可能无法使用。

在按键设置中配置法术快捷栏。第一个招式的当前按键是 <KeyBind id="keybindings.spell_engine.spell_hotbar_1" />。施法条显示施法是否仍在进行。

***

## 武器法术与乐曲

<EmiSearch query="@bards_rpg" /> <EmiSearch query="@elemental_wizards_rpg" /> <EmiSearch query="@paladins" /> <EmiSearch query="@wizards" />

<ItemGrid>
  <ItemIcon id="wizards:staff_arcane" />
  <ItemIcon id="elemental_wizards_rpg:staff_aqua" />
  <ItemIcon id="paladins:holy_staff" />
  <ItemIcon id="bards_rpg:wooden_lute" />
  <ItemIcon id="bards_rpg:diamond_lyre" />
</ItemGrid>

魔杖、法杖与乐器可能自带主动武器法术，不必从职业书学习这些招式。奥术、火焰、冰霜、水、地与风法器各有学派攻击，神圣法器支持治疗。不同独特吟游乐器携带不同乐曲。查看手持物品的完整招式与施法条件。这些武器法术类型不同于上方完整的职业书招式列表。

***

## 符文与符文袋

<EmiSearch query="@runes" />

<ItemGrid>
  <ItemIcon id="runes:crafting_altar" />
  <ItemIcon id="runes:small_rune_pouch" />
  <ItemIcon id="runes:medium_rune_pouch" />
  <ItemIcon id="runes:large_rune_pouch" />
  <ItemIcon id="runes:arcane_stone" />
  <ItemIcon id="runes:fire_stone" />
  <ItemIcon id="runes:frost_stone" />
  <ItemIcon id="runes:healing_stone" />
  <ItemIcon id="runes:lightning_stone" />
  <ItemIcon id="runes:soul_stone" />
</ItemGrid>

| 物品 | 用途 |
| --- | --- |
| <ItemLink id="runes:crafting_altar" /> | 符文合成工作站 |
| <ItemLink id="runes:small_rune_pouch" /> | 装备式符文储存 |
| <ItemLink id="runes:medium_rune_pouch" /> | 装备式符文储存 |
| <ItemLink id="runes:large_rune_pouch" /> | 装备式符文储存 |
| <ItemLink id="runes:arcane_stone" /> | 施法材料 |
| <ItemLink id="runes:fire_stone" /> | 施法材料 |
| <ItemLink id="runes:frost_stone" /> | 施法材料 |
| <ItemLink id="runes:healing_stone" /> | 施法材料 |
| <ItemLink id="runes:lightning_stone" /> | 施法材料 |
| <ItemLink id="runes:soul_stone" /> | 施法材料 |

只有要求符文的法术才会消耗对应符文。已装备的符文袋可提供储存的符文。符文祭坛提供独立合成界面。当前选择包含 Bundle API，因此符文袋配方可用。

<Recipe id="runes:pouch/small_rune_pouch" />


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Bard (RPG Series Plus)](images/catalog-kL7Bjgmw.png) [Bard (RPG Series Plus)](combat.magic.md) | 增加以歌曲与歌谣支援队友的吟游诗人职业。 | <EmiSearch query="@bards_rpg" /> |
| ![Elemental Wizards (RPG Series Plus)](images/catalog-PeZ4h4i0.png) [Elemental Wizards (RPG Series Plus)](combat.magic.md) | 为 Wizards 增加大地、水与风元素施法分支职业。 | <EmiSearch query="@elemental_wizards_rpg" /> |
| ![Paladins & Priests (RPG Series)](images/catalog-FxXkHaLe.png) [Paladins & Priests (RPG Series)](combat.magic.md) | 增加专注防护与治疗的圣骑士及牧师职业。 | <EmiSearch query="@paladins" /> |
| ![Runes](images/catalog-lP9Yrr1E.png) [Runes](combat.magic.md) | 增加可制作的符文，作为施法消耗的弹药。 | <EmiSearch query="@runes" /> |
| ![Witcher (RPG Series Plus)](images/catalog-4eW1c7Gj.png) [Witcher (RPG Series Plus)](combat.magic.md) | 增加以猎杀怪物为主题的猎魔人职业与战斗能力。 | <EmiSearch query="@witcher_rpg" /> |
| ![Wizards (RPG Series)](images/catalog-NkGaQMDA.png) [Wizards (RPG Series)](combat.magic.md) | 增加使用奥术、火焰与冰霜法术的巫师战斗体系。 | <EmiSearch query="@wizards" /> |
