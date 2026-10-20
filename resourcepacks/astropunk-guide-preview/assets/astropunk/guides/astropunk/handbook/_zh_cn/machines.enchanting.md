---
navigation:
  title: "附魔、修理与查看装备"
  position: 12
  parent: reference.machines-storage.md
  icon: minecraft:enchanting_table
---

# 附魔、修理与查看装备

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Enchantment+Industry+experience+fluid+printer+blaze+enchanter+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E9%99%84%E9%AD%94%E5%B7%A5%E4%B8%9A+%E6%B6%B2%E4%BD%93%E7%BB%8F%E9%AA%8C+%E6%89%93%E5%8D%B0%E6%9C%BA+%E7%83%88%E7%84%B0%E9%99%84%E9%AD%94%E5%99%A8+%E6%95%99%E7%A8%8B)

## 把经验变成液体

<EmiSearch query="@create_enchantment_industry" /> <EmiSearch query="@create" />

制作两个 <ItemLink id="create_enchantment_industry:mechanical_grindstone" />。手持其中一个右键已放置的物品排液口，将其变成 <ItemLink id="create_enchantment_industry:grindstone_drain" />。再在上方放置第二个机械磨石，并连接通往储罐的流体路线。给磨石供能并投入经验物品，例如经验颗粒，储罐就会装入液体经验。Ponder 课程包括 Introduction to Mechanical Grindstone。这不是把任意受损物品变成经验的通用来源。

<Recipe id="create_enchantment_industry:crafting/mechanical_grindstone" />

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| 机械磨石 | <ItemGrid><ItemIcon id="create_enchantment_industry:mechanical_grindstone" /></ItemGrid> | 将经验物品磨成流体，也能手持打磨 |
| 磨石排液口 | <ItemGrid><ItemIcon id="create_enchantment_industry:grindstone_drain" /></ItemGrid> | 收集磨石产出的液体经验 |
| 物品排液口 | <ItemGrid><ItemIcon id="create:item_drain" /></ItemGrid> | 从含流体物品中排出流体 |
| 经验存取口 | <ItemGrid><ItemIcon id="create_enchantment_industry:experience_hatch" /></ItemGrid> | 右键存入玩家经验，蹲下右键取回，面板设定数量 |
| 经验灯 | <ItemGrid><ItemIcon id="create_enchantment_industry:experience_lantern" /></ItemGrid> | 吸收附近经验球与玩家经验，亮度指示储量 |

***

## 附魔、锻造与打印

| 机器 | 外观 | 首次操作 |
| --- | --- | --- |
| 烈焰附魔器 | <ItemGrid><ItemIcon id="create_enchantment_industry:blaze_enchanter" /></ItemGrid> | 供给液体经验并设置附魔等级。手持要用作筛选依据的装备，右键面板的过滤槽以进入模板附魔模式，再投入空白附魔模板。生成范围仅限于该装备类型支持的附魔。护目镜显示所需输入、消耗、结果或无法启动的原因。 |
| 烈焰锻造器 | <ItemGrid><ItemIcon id="create_enchantment_industry:blaze_forger" /></ItemGrid> | 供给液体经验并选择侧面面板模式。合并兼容附魔或模板、应用模板，或将附魔提取到空白模板。开始下一批前取走两件产物。 |
| 打印机 | <ItemGrid><ItemIcon id="create_enchantment_industry:printer" /></ItemGrid> | 在过滤槽设定目标物品，再按打印配方供给对应流体与材料。一个实际用途是用所需液体经验复制附魔书。 |
| 附魔模板 | <ItemGrid><ItemIcon id="create_enchantment_industry:enchanting_template" /></ItemGrid> | 在受支持的操作间转移附魔 |

打印机过滤槽选择打印对象。准确流体与材料取决于具体配方。用配方浏览器查看所选任务的输入。锻造模式在侧面面板切换。Ponder 课程包括 Introduction to Blaze Enchanter、Introduction to Blaze Forger 与 Introduction to Printer。

***

## 修理与手动工具

注液器接入液体经验后，会修理带经验修补的传送带装备。把注液器放在传送带上方，装入流体，再让物品通过。损伤减少就是可见结果。

| 工具 | 外观 | 用途 |
| --- | --- | --- |
| 注液器 | <ItemGrid><ItemIcon id="create:spout" /></ItemGrid> | 在传送带上给经验修补装备注入液体经验 |
| 传送带 | <ItemGrid><ItemIcon id="create:belt_connector" /></ItemGrid> | 将装备送过注液器 |
| 铁砧 | <ItemGrid><ItemIcon id="minecraft:anvil" /></ItemGrid> | 手动修理与合并 |
| 命名牌 | <ItemGrid><ItemIcon id="minecraft:name_tag" /></ItemGrid> | 手动命名。Easy Anvils 改变其界面 |
| 附魔书 | <ItemGrid><ItemIcon id="minecraft:enchanted_book" /></ItemGrid> | 手动附魔来源与打印任务输入 |

- [旋转动力](machines.rotation.md) 驱动磨石与传送带。
- [物品与流体输送](machines.logistics.md) 运送机器输入与产物。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Enchantment Industry](images/create-enchantment-industry-icon.png) [Create: Enchantment Industry](machines.enchanting.md) | 用机械动力机器自动处理经验与附魔。 | <EmiSearch query="@create_enchantment_industry" /> |
| ![Easy Anvils](images/catalog-ozbr5jt5.png) [Easy Anvils](machines.enchanting.md) | 改进铁砧物品存放与费用，移除不断累积的维修惩罚。 | 无独立物品查询 |
