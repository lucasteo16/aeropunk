---
navigation:
  title: "输送、筛选与分配物品"
  position: 5
  parent: reference.machines-storage.md
  icon: create:brass_funnel
---

# 输送、筛选与分配物品

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Additional+Logistics+Item+routing+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Create%3A+Additional+Logistics+%E8%BE%93%E9%80%81%E3%80%81%E7%AD%9B%E9%80%89%E4%B8%8E%E5%88%86%E9%85%8D%E7%89%A9%E5%93%81+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 先做一条干净的线

<EmiSearch query="@create" />

传送带在容器与机器之间搬运物品。<ItemLink id="create:andesite_funnel" /> 从容器取出物品放到带上，另一端的漏斗把它送进机器。

先做一个输入容器、一条传送带、一只漏斗。它跑起来之后再去规划工厂。

<Recipe id="create:crafting/logistics/andesite_funnel" />

<ItemGrid><ItemIcon id="create:belt_connector" /><ItemIcon id="create:andesite_funnel" /><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:chute" /></ItemGrid>

| 部件 | 本包限制 |
| --- | --- |
| 机械传送带 | 最长 20 格 |
| 安山漏斗 | 每 8 游戏刻取出一次 |
| 黄铜漏斗 | 速率相同，可过滤并指定数量 |
| 滑槽 | 垂直下落，不需要旋转 |

要看到的结果是无人开箱也有物品在移动。如果带在动却没有东西送到，通常是漏斗方向装反了，一面取出，另一面送入。

***

## 过滤器决定什么能走

<ItemLink id="create:brass_funnel" /> 在设置里放过滤器，只搬运匹配的物品。<ItemLink id="create:brass_tunnel" /> 按过滤器把一路物品分到多个出口。

<ItemGrid><ItemIcon id="create:brass_funnel" /><ItemIcon id="create:brass_tunnel" /><ItemIcon id="create:mechanical_arm" /><ItemIcon id="create:smart_fluid_pipe" /></ItemGrid>

| 部件 | 有用的事实 |
| --- | --- |
| <ItemLink id="create:brass_funnel" /> | 过滤器加指定数量，机器正好拿到该拿的份数 |
| <ItemLink id="create:brass_tunnel" /> | 每 10 游戏刻分配一次 |
| <ItemLink id="create:mechanical_arm" /> | 触及 5 格，一个点服务多个输入与输出 |
| <ItemLink id="create:smart_fluid_pipe" /> | 像黄铜漏斗过滤物品那样过滤流体 |

一台机器要三种原料、出两种产物、空间又紧时，机械臂就是答案。本包里它的触及固定为 5 格，因此要围绕它摆机器，而不是硬拉长手臂。

***

## 包裹搬运的是库存

<EmiSearch query="@createadditionallogistics" /> <EmiSearch query="@create_connected" />

Create 6 的包裹系统把散装物品变成写着地址的包裹。<ItemLink id="create:packager" /> 打包，<ItemLink id="create:stock_link" /> 把容器当作库存读取，<ItemLink id="create:package_frogport" /> 在另一端收包裹。

<ItemGrid><ItemIcon id="create:packager" /><ItemIcon id="create:stock_link" /><ItemIcon id="create:package_frogport" /><ItemIcon id="create:redstone_requester" /><ItemIcon id="create:chain_conveyor" /></ItemGrid>

| 部件 | 作用 |
| --- | --- |
| <ItemLink id="create:packager" /> | 把一箱物品打成包裹 |
| <ItemLink id="create:stock_link" /> | 把容器接入库存网络 |
| <ItemLink id="create:package_frogport" /> | 接收寄到它地址的包裹 |
| <ItemLink id="create:chain_conveyor" /> | 运送 20 个包裹，最长 32 格，可有 4 个连接 |
| <ItemLink id="create:redstone_requester" /> | 不用工厂仪表也能请求库存 |

有了工厂仪表之后，Additional Logistics 的两项设置很关键。承诺上限限制一只仪表同时持有的未完成请求，避免慢线被原料包裹淹没。额外库存让补货仪表在低于目标时多订一批，而不是一次只补一件。

该模组还提供收银机。本包在服务端配置里关闭了股票行情，因此把收银机当作店铺摆设，而不是交易行情工具。

| 附加部件 | 区别 |
| --- | --- |
| <ItemLink id="createadditionallogistics:package_accelerator" /> | 加快打包机，代价是应力 |
| <ItemLink id="createadditionallogistics:package_editor" /> | 按规则改写包裹地址 |
| <ItemLink id="createadditionallogistics:cash_register" /> | 把店铺销售记入账本 |
| <ItemLink id="createadditionallogistics:sales_ledger" /> | 收银机写入的账本 |
| <ItemLink id="createadditionallogistics:lazy_shaft" /> | 超过两格的连线更省材料 |
| <ItemLink id="createadditionallogistics:lazy_cogwheel" /> | 齿轮上的同样节省 |
| <ItemLink id="createadditionallogistics:flexible_shaft" /> | 用扳手逐面设置连接 |
| <ItemLink id="create_connected:brass_chute" /> | 带黄铜过滤的滑槽 |
| <ItemLink id="createadditionallogistics:network_monitor" /> | 列车网络读数，属于计算机联动而非库存界面 |

***

## 流体遵循同样的规则

<ItemGrid><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:hose_pulley" /></ItemGrid>

| 部件 | 本包限制 |
| --- | --- |
| <ItemLink id="create:mechanical_pump" /> | 两侧各推或抽 16 格 |
| <ItemLink id="create:fluid_tank" /> | 每格 8 桶，最高 32 格 |
| <ItemLink id="create:hose_pulley" /> | 触及 128 格流体 |
| 软管滑轮与大水体 | 一万格以上水源视为无限 |

让熔岩湖变成工厂原料的就是软管滑轮。低于一万格的阈值时，它只会抽干眼前的水体，小池塘抽完就空了。

下一步值得做的是让产线自己装满、自己取空的储存。[大宗储存](storage.bulk.md)说明储物仓与筒仓。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Additional Logistics](images/catalog-czaz7aje.png) [Create: Additional Logistics](machines.logistics.md) | 扩展机械动力包裹处理，增加商店收银设备并改进工厂库存控制。 | <EmiSearch query="@createadditionallogistics" /> |
