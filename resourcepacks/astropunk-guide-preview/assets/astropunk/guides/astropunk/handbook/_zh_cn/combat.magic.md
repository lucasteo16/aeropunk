---
navigation:
  title: "选择法术与支援风格"
  position: 0
  parent: reference.skills.md
  icon: minecraft:blaze_rod
item_ids:
  - spell_engine:spell_binding
  - spell_engine:spell_book
  - spell_engine:spell_scroll
---

# 选择法术与支援风格

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

## 奥术

<EmiSearch query="@wizards" />

<ItemGrid>
  <ItemIcon id="wizards:wand_arcane" />
</ItemGrid>

<ItemLink id="wizards:wand_arcane" />

<Recipe id="wizards:wand_arcane" />

奥术魔法包含投射物、光束、范围攻击与自身效果。

| 能力 | 形式 |
| --- | --- |
| 奥秘飞弹 | 投射物 |
| 奥秘爆破 | 范围 |
| 奥秘射线 | 光束 |
| 奥秘弹幕 | 自身效果 |
| 闪现 | 自身效果 |
| 唤起 | 自身效果 |

***

## 火焰

<ItemGrid>
  <ItemIcon id="wizards:wand_novice" />
</ItemGrid>

<ItemLink id="wizards:wand_novice" />

<Recipe id="wizards:wand_novice" />

火焰魔法包含近距离范围、投射物与落下攻击。

| 能力 | 形式 |
| --- | --- |
| 烈焰吐息 | 范围 |
| 火焰斩 | 投射物 |
| 陨石术 | 落下攻击 |
| 火焰风暴 | 范围 |
| 火墙术 | 持续范围 |
| 火焰九头蛇 | 自身效果 |

***

## 冰霜

<ItemGrid>
  <ItemIcon id="wizards:wand_frost" />
</ItemGrid>

<ItemLink id="wizards:wand_frost" />

<Recipe id="wizards:wand_frost" />

冰霜魔法结合范围攻击、防护与投射物。

| 能力 | 形式 |
| --- | --- |
| 冰霜新星 | 范围 |
| 寒霜尖刺 | 持续范围 |
| 寒冰护盾 | 自身效果 |
| 寒冰之枪 | 投射物 |
| 暴风雪 | 落下攻击 |
| 冰霜元素 | 自身效果 |

***

## 水

<EmiSearch query="@elemental_wizards_rpg" />

<ItemGrid>
  <ItemIcon id="elemental_wizards_rpg:wand_kelp" />
</ItemGrid>

<ItemLink id="elemental_wizards_rpg:wand_kelp" />

<Recipe id="elemental_wizards_rpg:wand_kelp" />

水系魔法结合伤害法术与辅助区域。

| 能力 | 形式 |
| --- | --- |
| 泡泡光线 | 范围 |
| 水球 | 投射物 |
| 涌泉术 | 范围 |
| 高压水炮 | 光束 |
| 治愈雨云 | 自身效果 |
| 潮汐波 | 自身效果 |

***

## 土

<ItemGrid>
  <ItemIcon id="elemental_wizards_rpg:wand_clay" />
</ItemGrid>

<ItemLink id="elemental_wizards_rpg:wand_clay" />

<Recipe id="elemental_wizards_rpg:wand_clay" />

地系魔法结合防护、指定目标攻击与地面效果。

| 能力 | 形式 |
| --- | --- |
| 石化肌肤 | 范围 |
| 穿刺 | 瞄准目标 |
| 钟乳石阵 | 瞄准目标 |
| 碎石迸发 | 投射物 |
| 地震术 | 自身效果 |
| 土傀儡 | 自身效果 |

***

## 风

<ItemGrid>
  <ItemIcon id="elemental_wizards_rpg:wand_feather" />
</ItemGrid>

<ItemLink id="elemental_wizards_rpg:wand_feather" />

<Recipe id="elemental_wizards_rpg:wand_feather" />

风系魔法结合指定目标攻击、持续区域与自身效果。

| 能力 | 形式 |
| --- | --- |
| 气爆冲击 | 瞄准目标 |
| 旋风 | 自身效果 |
| 上升气流 | 瞄准目标 |
| 风场 | 瞄准目标 |
| 龙卷召唤 | 持续范围 |
| 风暴气流 | 投射物 |

***

## 圣骑士

<EmiSearch query="@paladins" />

<ItemGrid>
  <ItemIcon id="paladins:iron_mace" />
</ItemGrid>

<ItemLink id="paladins:iron_mace" />

<Recipe id="paladins:iron_mace" />

治疗学派与近战招式将辅助和贴身战斗结合。

| 能力 | 形式 |
| --- | --- |
| 快速治疗 | 瞄准目标 |
| 受祝打击 | 预备效果 |
| 神圣庇护 | 自身效果 |
| 审判 | 落下攻击 |
| 战旗 | 持续范围 |
| 焚毁 | 范围 |

***

## 牧师

<ItemGrid>
  <ItemIcon id="paladins:acolyte_wand" />
</ItemGrid>

<ItemLink id="paladins:acolyte_wand" />

<Recipe id="paladins:acolyte_wand" />

治疗学派提供光束、治疗区域与防护。

| 能力 | 形式 |
| --- | --- |
| 圣光术 | 光束 |
| 治疗之环 | 范围 |
| 神圣屏障 | 自身效果 |
| 采光井 | 自身效果 |
| 悬浮 | 自身效果 |
| 忏悔 | 投射物 |

***

## 吟游诗人

<EmiSearch query="@bards_rpg" />

<ItemGrid>
  <ItemIcon id="bards_rpg:wooden_lute" />
</ItemGrid>

<ItemLink id="bards_rpg:wooden_lute" />

<Recipe id="bards_rpg:wooden_lute" />

乐器招式结合奥术攻击与辅助效果。

| 能力 | 形式 |
| --- | --- |
| 魔法歌谣 | 投射物 |
| 恶毒嘲讽 | 瞄准目标 |
| 守卫者赞歌 | 瞄准目标 |
| 返场 | 范围 |
| 军团赞歌 | 预备效果 |
| 渐强 | 投射物 |

***

## 猎魔人剑术

<EmiSearch query="@witcher_rpg" />

<ItemGrid>
  <ItemIcon id="witcher_rpg:iron_witcher_sword" />
</ItemGrid>

<ItemLink id="witcher_rpg:iron_witcher_sword" />

<Recipe id="witcher_rpg:iron_witcher_sword" />

猎魔人剑术提供近战攻击与自身效果。

| 能力 | 形式 |
| --- | --- |
| 速攻 | 近战攻击 |
| 猎魔人感官 | 范围 |
| 重击 | 近战攻击 |
| 战斗专注 | 自身效果 |
| 撕裂 | 近战攻击 |
| 回旋斩 | 范围 |

***

## 猎魔人法印

<ItemGrid>
  <ItemIcon id="witcher_rpg:iron_witcher_sword" />
</ItemGrid>

<ItemLink id="witcher_rpg:iron_witcher_sword" />

<Recipe id="witcher_rpg:iron_witcher_sword" />

猎魔人法印有各自学派，提供控制或防护效果。

| 能力 | 形式 |
| --- | --- |
| 阿尔德法印 | 范围 |
| 伊格尼法印 | 范围 |
| 亚登法印 | 持续范围 |
| 亚克席法印 | 瞄准目标 |
| 昆恩法印 | 自身效果 |
| 伊格尼火流 | 范围 |
| 阿尔德横扫 | 范围 |
| 亚登魔法陷阱 | 自身效果 |
| 亚克席傀儡 | 瞄准目标 |
| 昆恩主动护盾 | 自身效果 |

***

## 武器法术与乐曲

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

## 构筑相关

- [武器与护甲](equipment.weapons-armor.md) 选择武器类型，比较当前支持的各个变体。
- [技能成长](combat.skills.md) 在相连分支中分配职业与武器技能点。
- [战斗操作](combat.handling.md) 了解攻击模式、施法操作与翻滚。


***

## 治疗法器

铁钉头锤适合圣骑士近战起步，但没有治疗强度加成。以治疗为主时先制作侍僧魔杖，比较治疗强度，而不是攻击伤害。

<ItemGrid>
  <ItemIcon id="paladins:acolyte_wand" />
</ItemGrid>

<ItemLink id="paladins:acolyte_wand" />

<Recipe id="paladins:acolyte_wand" />



***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Bard (RPG Series Plus)](images/catalog-kL7Bjgmw.png) [Bard (RPG Series Plus)](combat.magic.md) | 增加以歌曲与歌谣支援队友的吟游诗人职业。 | 已安装基准版 | <EmiSearch query="@bards_rpg" /> |
| ![Elemental Wizards (RPG Series Plus)](images/catalog-PeZ4h4i0.png) [Elemental Wizards (RPG Series Plus)](combat.magic.md) | 为 Wizards 增加大地、水与风元素施法分支职业。 | 已安装基准版 | <EmiSearch query="@elemental_wizards_rpg" /> |
| ![Paladins & Priests (RPG Series)](images/catalog-FxXkHaLe.png) [Paladins & Priests (RPG Series)](combat.magic.md) | 增加专注防护与治疗的圣骑士及牧师职业。 | 已安装基准版 | <EmiSearch query="@paladins" /> |
| ![Runes](images/catalog-lP9Yrr1E.png) [Runes](combat.magic.md) | 增加可制作的符文，作为施法消耗的弹药。 | 已安装基准版 | <EmiSearch query="@runes" /> |
| ![Witcher (RPG Series Plus)](images/catalog-4eW1c7Gj.png) [Witcher (RPG Series Plus)](combat.magic.md) | 增加以猎杀怪物为主题的猎魔人职业与战斗能力。 | 已安装基准版 | <EmiSearch query="@witcher_rpg" /> |
| ![Wizards (RPG Series)](images/catalog-NkGaQMDA.png) [Wizards (RPG Series)](combat.magic.md) | 增加使用奥术、火焰与冰霜法术的巫师战斗体系。 | 已安装基准版 | <EmiSearch query="@wizards" /> |
