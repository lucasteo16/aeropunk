---
navigation:
  title: "工具与无人机"
  position: 11
  parent: reference.machines-storage.md
  icon: create:wrench
---

# 工具与无人机

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Stuff+Additions+portable+drill+refill+drone+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E9%99%84%E5%8A%A0%E7%89%A9%E5%93%81+%E4%BE%BF%E6%90%BA%E9%92%BB%E5%A4%B4+%E8%A1%A5%E7%BB%99+%E6%97%A0%E4%BA%BA%E6%9C%BA%E6%95%99%E7%A8%8B)

## 给便携工具补给并使用

<EmiSearch query="@create_sa" />

手持装水储罐右键水源即可装水，加燃料储罐则从熔岩源补给。把装好的储罐留在物品栏中，主手拿兼容工具，工具流体条上升就表示正在补给。水和燃料使用不同的储罐系列。

| 工具 | 外观 | 用途 |
| --- | --- | --- |
| 便携钻头 | <ItemGrid><ItemIcon id="create_sa:portable_drill" /></ItemGrid> | 手持高速挖掘方块，会消耗耐久。除需要钻石工具标签的方块外，可正确采集掉落 |
| 抓钩胡须 | <ItemGrid><ItemIcon id="create_sa:grapplin_whisk" /></ItemGrid> | 右键发射钩索，手臂呈拉弓姿势表示已钩住 |
| 铜磁铁 | <ItemGrid><ItemIcon id="create_sa:copper_magnet" /></ItemGrid> | 手持时吸引附近掉落物 |
| 方块拾取器 | <ItemGrid><ItemIcon id="create_sa:block_picker" /></ItemGrid> | 储有水时，右键上方为空气的方块将其举起。不能举起刷怪笼或硬度达到五十的方块。保持选中拾取器以搬运，对空气右键即可放下。落点空闲时恢复为方块，受阻时掉落资源。不要据此认为装有物品的容器可以安全搬运。 |

钻头挖掘进度与抓钩燃料条能显示消耗。装水储罐带水，加燃料储罐带燃料。小、中、大容量不同。这些是便携补给物品，不是放置后自动充能的机器。

***

## 储罐与引擎

<EmiSearch query="@create" />

| 家族 | 外观 | 用途 |
| --- | --- | --- |
| 装水储罐 | <ItemGrid><ItemIcon id="create_sa:small_filling_tank" /><ItemIcon id="create_sa:medium_filling_tank" /><ItemIcon id="create_sa:large_filling_tank" /><ItemIcon id="create_sa:creative_filling_tank" /></ItemGrid> | 为工具携带水 |
| 加燃料储罐 | <ItemGrid><ItemIcon id="create_sa:small_fueling_tank" /><ItemIcon id="create_sa:medium_fueling_tank" /><ItemIcon id="create_sa:large_fueling_tank" /></ItemGrid> | 为工具携带受支持燃料 |
| 固定蒸汽引擎 | <ItemGrid><ItemIcon id="create:steam_engine" /></ItemGrid> | 机械动力的锅炉引擎，不是便携引擎组件 |
| 便携引擎 | <ItemGrid><ItemIcon id="create_sa:steam_engine" /><ItemIcon id="create_sa:hydraulic_engine" /><ItemIcon id="create_sa:heat_engine" /></ItemGrid> | 选择与设备匹配的引擎，分别是蒸汽、水力与热能变体 |


***

## 部署并控制无人机

<ItemGrid><ItemIcon id="create_sa:brass_drone_item" /><ItemIcon id="create_sa:drone_controller" /><ItemIcon id="create_sa:brass_drill_head" /><ItemIcon id="create_sa:copper_magnet" /><ItemIcon id="create_sa:fan_component" /><ItemIcon id="create_sa:vault_component" /></ItemGrid>

1. 主手拿黄铜无人机，右键方块顶面。无人机会出现在上方并归你所有，生存模式会消耗该物品。
2. 空手右键无人机可暂停或恢复移动。任意一只手拿控制器，即可引导属于你的未停驻无人机。
3. 按 <KeyBind id="key.create_sa.increase_reach" /> 将目标沿视线推远，按 <KeyBind id="key.create_sa.decrease_reach" /> 将目标拉近。默认分别是向上和向下方向键，每次调整要单独按一下。收起控制器会重置控制距离和动作状态。
4. 手持黄铜钻头、铜磁铁、风扇组件或仓库组件，右键无人机以安装已启用的对应模块。组件会出现在机身上，非创造模式会消耗一个。
5. 手持控制器对空气右键，切换模块动作。钻掘时先把无人机引导到可破坏方块上方，再触发动作。方块消失并掉落物品表示成功，成功钻掘后动作会重置，不会无限连续运行。

直接右键无人机切换的是停驻状态，不是模块动作。

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create+Stuff+Additions+2.1.4+drone+controller+block+picker+guide) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+1.21.1+Create+Stuff+Additions+%E6%97%A0%E4%BA%BA%E6%9C%BA+%E6%8E%A7%E5%88%B6%E5%99%A8+%E6%96%B9%E5%9D%97%E6%8B%BE%E5%8F%96%E5%99%A8+%E6%95%99%E7%A8%8B)

***

- [材料加工](machines.ore-processing.md) 风扇介质与加工。
- [旋转动力](machines.rotation.md) 固定机器传动。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Stuff 'N Additions](images/catalog-aq9quuqg.png) [Create Stuff 'N Additions](machines.miscellaneous.md) | 增加机械动力主题的动力装备与可穿戴工具。 | <EmiSearch query="@create_sa" /> |
