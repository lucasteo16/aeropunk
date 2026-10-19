---
navigation:
  title: "手动交易与自动交易"
  position: 13
  parent: reference.machines-storage.md
  icon: minecraft:emerald_block
---

# 手动交易与自动交易

## 工作站旁的交易站

<EmiSearch query="@trading_floor" />

<ItemLink id="trading_floor:trading_depot" /> 把一笔村民交易变成一个机器的输入与输出。交易清单仍然属于村民。交易站只负责交付交易要的东西，并取走交易给出的东西。

把交易站贴放在村民已经认领的工作站上，而不是贴在村民身上。

<Recipe id="trading_floor:trading_depot" />

<ItemGrid><ItemIcon id="trading_floor:trading_depot" /><ItemIcon id="minecraft:lectern" /><ItemIcon id="minecraft:emerald" /><ItemIcon id="minecraft:book" /></ItemGrid>

| 部件 | 提供什么 |
| --- | --- |
| <ItemLink id="trading_floor:trading_depot" /> | 单笔交易的机器接口 |
| 被认领的工作站 | 把交易站绑定到一位村民 |
| 村民 | 拥有交易清单、价格与补货 |
| <ItemLink id="minecraft:emerald" /> | 通用货币，仍需你来支付 |

交易在村民工作时段进行。够不到工作站或正在睡觉的村民不会交易，交易站会带着里面的输入一直停着。

***

## 一个能用的交易站

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="trading_floor:trading_depot" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:mechanical_arm" /><ItemIcon id="create:display_link" /></ItemGrid>

| 结果 | 细节 |
| --- | --- |
| 每个工作时段交易次数 | 本包最多 4 次 |
| 村民经验 | 归村民，默认开启 |
| 玩家经验 | 本包默认关闭 |
| 读数 | 护目镜与显示链接可显示交易状态 |

每时段四次是本包设置，不是模组设计的极限。它足以让铁农场或书籍交易值得自动化，也低到单靠一个交易站养不起整个基地。

***

## 两个交易站，两种输入

需要两种不同物品的交易要用两个交易站，各自带输入。两者的过滤器必须一致，或者其中一个留空。

<ItemGrid><ItemIcon id="trading_floor:trading_depot" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:chute" /></ItemGrid>

| 布置 | 行为 |
| --- | --- |
| 一个交易站，一种输入 | 处理单物品交易 |
| 两个交易站，过滤器一致 | 两者共同供给同一笔交易 |
| 两个交易站，一个过滤器留空 | 留空的那个接受任何物品 |
| 两个交易站，过滤器不同 | 交易无法完成 |

用设为精确物品的 <ItemLink id="create:brass_funnel" /> 给每个交易站供料。接受替代物品的过滤器会让交易悄悄失败，因为村民不会收下那件替代品。

下一步是不靠玩家把付款送进去、把产物取出来。[物料输送](machines.logistics.md)说明传送带、漏斗与机械臂。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Trading floor](images/create-trading-floor-icon.png) [Create: Trading floor](machines.trading.md) | 通过机械动力机器自动进行村民交易。 | <EmiSearch query="@trading_floor" /> |
