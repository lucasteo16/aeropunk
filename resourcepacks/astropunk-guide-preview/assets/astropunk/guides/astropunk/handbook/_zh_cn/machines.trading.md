---
navigation:
  title: "手动交易与自动交易"
  position: 13
  parent: reference.machines-storage.md
  icon: minecraft:emerald_block
---

# 手动交易与自动交易

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Trading+Floor+trading+depot+villager+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E4%BA%A4%E6%98%93%E7%AB%99+%E6%9D%91%E6%B0%91+%E6%95%99%E7%A8%8B)

## 将交易站连接到村民

<EmiSearch query="@trading_floor" /> <EmiSearch query="@create" />

把 <ItemLink id="trading_floor:trading_depot" /> 接到村民已认领的工作站。打开交易站，用交易过滤器选择一笔可用交易，再按列表放入准确成本物品。村民必须能到达工作站，并在正常工作时间工作。Ponder 课程包括 Trading with trading depots。

<Recipe id="trading_floor:trading_depot" />

| 部件 | 外观 | 作用 |
| --- | --- | --- |
| 交易站 | <ItemGrid><ItemIcon id="trading_floor:trading_depot" /></ItemGrid> | 存放该交易站的输入与产物 |
| 已认领工作站 | <ItemGrid><ItemIcon id="minecraft:lectern" /></ItemGrid> | 将交易站连接到对应村民 |
| 机械臂 | <ItemGrid><ItemIcon id="create:mechanical_arm" /></ItemGrid> | 配置后向受支持的交易站目标供料 |
| 交易物品 | <ItemGrid><ItemIcon id="minecraft:emerald" /><ItemIcon id="minecraft:book" /></ItemGrid> | 成本与结果取决于所选村民报价 |

村民下次工作时，若输入齐全，交易站会执行选定交易。用护目镜查看交易站信息与最近交易栏。用漏斗或滑槽从交易站取出产物。

***

## 双输入交易

需要两种不同成本物品的交易要用两个交易站。在第一个输入站设置交易过滤器，避免误选其他报价。第二个交易站在过滤器相同，或该站未设置过滤器时，会参与交易。这里指过滤器未设置，不是交易站库存为空。产物进入持有第一项交易输入的交易站。

| 路线 | 外观 | 用途 |
| --- | --- | --- |
| 单输入 | <ItemGrid><ItemIcon id="create:brass_funnel" /></ItemGrid> | 黄铜漏斗供给选定的准确成本 |
| 竖直传输 | <ItemGrid><ItemIcon id="create:chute" /></ItemGrid> | 滑槽竖直供料或取货 |
| 交易读数 | <ItemGrid><ItemIcon id="create:display_link" /></ItemGrid> | 可选状态显示 |

村民决定价格与补货。Ponder 课程包括 Trading with multiple trading depots。[物品与流体输送](machines.logistics.md)介绍物品移动。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Trading floor](images/create-trading-floor-icon.png) [Create: Trading floor](machines.trading.md) | 通过机械动力机器自动进行村民交易。 | <EmiSearch query="@trading_floor" /> |
