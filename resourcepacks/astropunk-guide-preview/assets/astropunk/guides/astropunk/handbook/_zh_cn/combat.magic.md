---
navigation:
  title: "法术与支援职业"
  position: 6
  parent: reference.skills.md
  icon: minecraft:blaze_rod
---

# 法术与支援职业

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+RPG+Series+Runes+rune+pouch+Wizards+casting+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+RPG+Series+Runes+%E7%AC%A6%E6%96%87%E8%A2%8B+%E6%B3%95%E5%B8%88+%E6%96%BD%E6%B3%95+%E6%95%99%E7%A8%8B)

## 施法与支援

| 职业 | 玩法 |
| --- | --- |
| [奥术法师](class.arcane.md) | 奥术弹射物与光束。 |
| [火焰法师](class.fire.md) | 火焰攻击与持续燃烧区域。 |
| [冰霜法师](class.frost.md) | 冰霜攻击与防护。 |
| [水系法师](class.aqua.md) | 水系伤害与治疗区域。 |
| [地系法师](class.terra.md) | 地系攻击与地面防护。 |
| [风系法师](class.wind.md) | 风系攻击与龙卷风区域。 |
| [圣骑士](class.paladin.md) | 近战、治疗与防护。 |
| [牧师](class.priest.md) | 治疗光束与群体防护。 |
| [吟游诗人](class.bard.md) | 乐器攻击与辅助乐曲。 |
| [猎魔人](class.witcher.md) | 剑术与控制、防护法印。 |

各职业文章收录入门配方、书籍、完整职业书招式表与装备。猎魔人的剑术书与法印书属于同一职业。

- [法术与招式](combat.abilities.md) 共用的绑定步骤、卷轴与施法操作。
- [技能成长](combat.skills.md) 相互独立的职业与武器点数。

![使用法杖施展奥术](images/visual-arcane-casting.png)

***

## 武器法术与乐曲

<ItemGrid>
  <ItemIcon id="wizards:staff_arcane" />
  <ItemIcon id="elemental_wizards_rpg:staff_aqua" />
  <ItemIcon id="paladins:holy_staff" />
  <ItemIcon id="bards_rpg:wooden_lute" />
  <ItemIcon id="bards_rpg:diamond_lyre" />
</ItemGrid>

魔杖、法杖与乐器可能自带主动武器法术，不必从职业书学习这些招式。奥术、火焰、冰霜、水、地与风法器各有学派攻击，神圣法器支持治疗。不同独特吟游乐器携带不同乐曲。查看手持物品的完整招式与施法条件。职业文章另行收录通过书籍学习的招式。

***

## 符文与符文袋

这些物品栏用于识别可选物品，并非必须配齐的套装或合成配方。同组物品仅共享所列用途或属性组合，具体数值、效果与槽位要求请查看各自提示。

符文合成工作站

<ItemGrid>
  <ItemIcon id="runes:crafting_altar" />
</ItemGrid>

装备式符文储存

<ItemGrid>
  <ItemIcon id="runes:small_rune_pouch" />
  <ItemIcon id="runes:medium_rune_pouch" />
  <ItemIcon id="runes:large_rune_pouch" />
</ItemGrid>

施法材料

<ItemGrid>
  <ItemIcon id="runes:arcane_stone" />
  <ItemIcon id="runes:fire_stone" />
  <ItemIcon id="runes:frost_stone" />
  <ItemIcon id="runes:healing_stone" />
  <ItemIcon id="runes:lightning_stone" />
  <ItemIcon id="runes:soul_stone" />
</ItemGrid>

符文是施法弹药，不会让你学会法术。先看所选法术的消耗，再制作对应符文。只有标有符文消耗的法术才会消耗符文。符文袋节省携带空间，不会生成符文，也不会免除消耗。

1. 从法术要求的符文入手。火系入门可把合适的石质基材与煤进行无序合成，得到 2 个火焰符文。其他学派与替代材料请查配方浏览器。
2. 有符文祭坛后，打开界面，把石质基材与对应材料放入两个原料槽，再取出符文。同样的煤配方在祭坛产出 8 个火焰符文。祭坛能提高补给效率，但第一次施法不需要先造祭坛。
3. 按下方配方制作符文袋。在背包中用光标拿起符文袋，右键符文堆叠以装入。查看袋内物品，再把符文袋放入支持的箭袋饰品槽。施法时可直接消耗已装备袋中的对应符文。
4. 出发前，找有效目标试放一次消耗较少的法术。若提示缺少符文，依次检查符文种类、数量、袋内物品与装备槽位。入门时也可直接把散装符文放在背包中。

闪电符文与灵魂符文属于物品目录，并非每个施法者都要收集的材料。以实际使用法术的消耗为准。符文袋配方需要 Bundle API，当前选择已包含此依赖。

<Recipe id="runes:pouch/small_rune_pouch" />

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Bard (RPG Series Plus)](images/catalog-kl7bjgmw.png) [Bard (RPG Series Plus)](combat.magic.md) | 增加以歌曲与歌谣支援队友的吟游诗人职业。 | <EmiSearch query="@bards_rpg" /> |
| ![Elemental Wizards (RPG Series Plus)](images/catalog-pez4h4i0.png) [Elemental Wizards (RPG Series Plus)](combat.magic.md) | 为 Wizards 增加大地、水与风元素施法分支职业。 | <EmiSearch query="@elemental_wizards_rpg" /> |
| ![Paladins & Priests (RPG Series)](images/catalog-fxxkhale.png) [Paladins & Priests (RPG Series)](combat.magic.md) | 增加专注防护与治疗的圣骑士及牧师职业。 | <EmiSearch query="@paladins" /> |
| ![Runes](images/catalog-lp9yrr1e.png) [Runes](combat.magic.md) | 增加可制作的符文，作为施法消耗的弹药。 | <EmiSearch query="@runes" /> |
| ![Witcher (RPG Series Plus)](images/catalog-4ew1c7gj.png) [Witcher (RPG Series Plus)](combat.magic.md) | 增加以猎杀怪物为主题的猎魔人职业与战斗能力。 | <EmiSearch query="@witcher_rpg" /> |
| ![Wizards (RPG Series)](images/catalog-nkgaqmda.png) [Wizards (RPG Series)](combat.magic.md) | 增加使用奥术、火焰与冰霜法术的巫师战斗体系。 | <EmiSearch query="@wizards" /> |
