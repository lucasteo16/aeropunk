---
navigation:
  title: "物品与流体输送"
  position: 10
  parent: reference.machines-storage.md
  icon: create:brass_funnel
---

# 物品与流体输送

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+mod+belts+funnels+packagers+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+%E4%BC%A0%E9%80%81%E5%B8%A6+%E6%BC%8F%E6%96%97+%E6%89%93%E5%8C%85%E6%9C%BA+%E7%89%A9%E6%B5%81%E6%95%99%E7%A8%8B)

## 连接传送带并运送物品

<EmiSearch query="@create" />

手持 <ItemLink id="create:belt_connector" />，右键点击两个方向受支持的轴即可连接。转动任一轴，两者会以相同方向与转速转动。把物品丢上移动的传送带，空手右键可取下。Ponder 课程包括 Using Mechanical Belts 与 Valid Orientations for Mechanical Belts。

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| 传送带 | <ItemGrid><ItemIcon id="create:belt_connector" /></ItemGrid> | 连接两根轴并运送物品 |
| 安山漏斗 | <ItemGrid><ItemIcon id="create:andesite_funnel" /></ItemGrid> | 一次传送一件物品 |
| 黄铜漏斗 | <ItemGrid><ItemIcon id="create:brass_funnel" /></ItemGrid> | 最多传送一整堆，带过滤与数量面板 |

普通放置漏斗会从库存取物，潜行放置会向库存送物，再用扳手翻转方向。红石信号会停用漏斗。在传送带上，传送带运动方向决定传输方向。黄铜过滤槽只接受匹配物品堆。

***

## 分拣、落料与收集

<EmiSearch query="@create_connected" />

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+6+brass+tunnel+sorting+mechanical+arm+input+output+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+6+%E9%BB%84%E9%93%9C%E9%9A%A7%E9%81%93+%E5%88%86%E6%8B%A3+%E6%9C%BA%E6%A2%B0%E8%87%82+%E8%BE%93%E5%85%A5+%E8%BE%93%E5%87%BA+%E6%95%99%E7%A8%8B)

| 部件 | 外观 | 区别 |
| --- | --- | --- |
| 安山隧道 | <ItemGrid><ItemIcon id="create:andesite_tunnel" /></ItemGrid> | 覆盖传送带，有侧面连接时恰好分出一件物品 |
| 黄铜隧道 | <ItemGrid><ItemIcon id="create:brass_tunnel" /></ItemGrid> | 输入过滤会挡住不匹配物，输出过滤按物品分拣，分配模式决定有效出口的选择 |
| 滑槽 | <ItemGrid><ItemIcon id="create:chute" /></ItemGrid> | 在库存之间竖直运输物品 |
| 黄铜滑槽 | <ItemGrid><ItemIcon id="create_connected:brass_chute" /></ItemGrid> | 按其物品帮助用于扩展滑槽路线 |

把滑槽放在两个库存之间，扳手可开侧窗。顶部或底部加鼓风风扇后可向上移动物品，护目镜会显示移动方向。

<ItemLink id="create:mechanical_arm" /> 必须先指定目标再放置。手持机械臂右键点击支持的压台或漏斗以添加目标，再次右键把蓝色输入切换成黄色输出，左键移除目标，然后放置并供能。并非所有库存都可直接交互，必要时用压台或漏斗作接口。黄铜漏斗目标会把过滤规则传给机械臂。

***

## 包裹与库存请求

<EmiSearch query="@createadditionallogistics" />

![Tutorial](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+Create+6+stock+network+packager+stock+link+stock+ticker+address+complete+tutorial) · [中文](https://www.youtube.com/results?search_query=%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C+%E6%9C%BA%E6%A2%B0%E5%8A%A8%E5%8A%9B+6+%E6%89%93%E5%8C%85%E6%9C%BA+%E5%BA%93%E5%AD%98%E9%93%BE%E6%8E%A5+%E5%BA%93%E5%AD%98%E6%8A%A5%E4%BB%B7%E5%99%A8+%E5%9C%B0%E5%9D%80+%E5%AE%8C%E6%95%B4%E6%95%99%E7%A8%8B)

| 部件 | 外观 | 用途 |
| --- | --- | --- |
| 打包机 | <ItemGrid><ItemIcon id="create:packager" /></ItemGrid> | 红石信号下打包相连库存的物品，也会拆开投入其中的包裹 |
| 包裹过滤器 | <ItemGrid><ItemIcon id="create:package_filter" /></ItemGrid> | 按包裹地址分流，不按物品内容 |
| 包裹蛙港 | <ItemGrid><ItemIcon id="create:package_frogport" /></ItemGrid> | 包裹投递接口 |
| 库存链接 | <ItemGrid><ItemIcon id="create:stock_link" /></ItemGrid> | 让接入网络的打包机公开其库存 |
| 红石请求器 | <ItemGrid><ItemIcon id="create:redstone_requester" /></ItemGrid> | 通过网络请求库存 |

1. 将打包机装到供货库存上，放入少量测试物品，再给打包机一个红石脉冲。出现包裹就说明打包成功，先完成这一步再增加网络。
2. 用传送带把包裹送入另一台连接收货库存的打包机。只有收货库存能容纳整个包裹时才会拆包。
3. 在供货打包机上安装库存链接。手持另一个库存链接，放置前先右键第一个链接，就能加入同一网络。链接共享的是库存信息，不会传送实体包裹。
4. 手持 <ItemLink id="create:stock_ticker" />，放置前先右键库存链接以绑定网络。在报价器前放坐下的生物或烈焰燃烧器作为库存管理员，再右键管理员订购已有库存。自动订货时，红石请求器也要在放置前绑定同一链接，放置后右键打开界面设置订单，再发送脉冲。
5. 在订单中设置目标地址，并在运输路线上用包裹过滤器按地址分流。所订物品到达指定库存并成功拆包，就说明整条路线工作正常。

把库存链接接到打包机并连入网络。单独装在仓库上的链接不会显示数量。包裹仍需要运输路线。

***

| 扩展部件 | 外观 | 用途 |
| --- | --- | --- |
| <ItemLink id="createadditionallogistics:package_accelerator" /> | <ItemGrid><ItemIcon id="createadditionallogistics:package_accelerator" /></ItemGrid> | 消耗应力以加快正前方打包机 |
| <ItemLink id="createadditionallogistics:package_editor" /> | <ItemGrid><ItemIcon id="createadditionallogistics:package_editor" /></ItemGrid> | 按规则改写包裹地址 |
| <ItemLink id="createadditionallogistics:network_monitor" /> | <ItemGrid><ItemIcon id="createadditionallogistics:network_monitor" /></ItemGrid> | 显示库存网络信息 |
| <ItemLink id="createadditionallogistics:cash_register" /> | <ItemGrid><ItemIcon id="createadditionallogistics:cash_register" /></ItemGrid> | 记录销售的库存报价器替代设备 |
| <ItemLink id="createadditionallogistics:sales_ledger" /> | <ItemGrid><ItemIcon id="createadditionallogistics:sales_ledger" /></ItemGrid> | 对库存管理员使用，以请求补充已售物品 |

## 流体与长距离传动

| 家族 | 外观 | 用途 |
| --- | --- | --- |
| 流体管道 | <ItemGrid><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:smart_fluid_pipe" /><ItemIcon id="create:mechanical_pump" /></ItemGrid> | 输送流体，智能管道按流体过滤 |
| 流体存储与源头移动 | <ItemGrid><ItemIcon id="create:fluid_tank" /><ItemIcon id="create:hose_pulley" /></ItemGrid> | 储罐存放流体，吊索填充或抽取大片流体 |
| 物品输送 | <ItemGrid><ItemIcon id="create:chain_conveyor" /></ItemGrid> | 沿链条路线运送物品 |
| 轴传动 | <ItemGrid><ItemIcon id="createadditionallogistics:lazy_shaft" /><ItemIcon id="createadditionallogistics:lazy_cogwheel" /><ItemIcon id="createadditionallogistics:flexible_shaft" /></ItemGrid> | 懒惰轴适合超过两根的长列。懒惰齿轮需配合至少两根懒惰轴。用扳手切换柔性轴每侧的输出。 |

流体路线可用管道连接储罐、泵与目标。按泵上的箭头确定流向。反转泵的旋转输入不会改变流体方向，要用扳手转动箭头。

- [批量存储](storage.bulk.md) 仓库容量与形状。
- [存储处理](storage.handling.md) 共用库存搬运。
- [旋转动力](machines.rotation.md) 传动布置。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Additional Logistics](images/catalog-czaz7aje.png) [Create: Additional Logistics](machines.logistics.md) | 扩展机械动力包裹处理，增加商店收银设备并改进工厂库存控制。 | <EmiSearch query="@createadditionallogistics" /> |
