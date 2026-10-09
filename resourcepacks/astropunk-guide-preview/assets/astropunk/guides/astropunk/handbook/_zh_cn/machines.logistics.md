---
navigation:
  title: "输送、筛选与分配物品"
  position: 0
  parent: reference.machines-storage.md
  icon: create:brass_funnel
---

# 输送、筛选与分配物品

## 物品与流体

<EmiSearch query="@create_connected" /> <EmiSearch query="@create" />

<ItemGrid>
  <ItemIcon id="create:belt_connector" />
  <ItemIcon id="create:andesite_funnel" />
  <ItemIcon id="create:brass_funnel" />
  <ItemIcon id="create:brass_tunnel" />
  <ItemIcon id="create:chute" />
  <ItemIcon id="create_connected:brass_chute" />
  <ItemIcon id="create:mechanical_arm" />
  <ItemIcon id="create:fluid_pipe" />
  <ItemIcon id="create:mechanical_pump" />
  <ItemIcon id="create:smart_fluid_pipe" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create:belt_connector" />, <ItemLink id="create:andesite_funnel" />, <ItemLink id="create:brass_funnel" />, <ItemLink id="create:brass_tunnel" /> | Create 的传送带、漏斗与隧道输送物品，黄铜组件提供过滤。 |
| <ItemLink id="create:chute" />, <ItemLink id="create_connected:brass_chute" />, <ItemLink id="create:mechanical_arm" /> | 溜槽与机械臂连接加工工位。 |
| <ItemLink id="create:fluid_pipe" />, <ItemLink id="create:mechanical_pump" />, <ItemLink id="create:smart_fluid_pipe" /> | 管道、泵与过滤流体输送。 |

***

## 包裹与请求

<EmiSearch query="@createadditionallogistics" />

<ItemGrid>
  <ItemIcon id="create:packager" />
  <ItemIcon id="create:stock_link" />
  <ItemIcon id="create:redstone_requester" />
  <ItemIcon id="create:package_frogport" />
  <ItemIcon id="create:chain_conveyor" />
  <ItemIcon id="createadditionallogistics:package_accelerator" />
  <ItemIcon id="createadditionallogistics:package_editor" />
  <ItemIcon id="createadditionallogistics:cash_register" />
  <ItemIcon id="createadditionallogistics:lazy_shaft" />
  <ItemIcon id="createadditionallogistics:lazy_cogwheel" />
  <ItemIcon id="createadditionallogistics:flexible_shaft" />
</ItemGrid>

| 物品与系列 | 用途 |
| --- | --- |
| <ItemLink id="create:packager" />, <ItemLink id="create:stock_link" />, <ItemLink id="create:redstone_requester" /> | Create 的打包、库存网络与红石请求组件。 |
| <ItemLink id="create:package_frogport" />, <ItemLink id="create:chain_conveyor" /> | 通过蛙口与链式输送机转移包裹。 |
| <ItemLink id="createadditionallogistics:package_accelerator" />, <ItemLink id="createadditionallogistics:package_editor" />, <ItemLink id="createadditionallogistics:cash_register" /> | 以应力消耗换取打包机加速，按规则修改包裹地址，并将库存交易记录到台账。 |
| <ItemLink id="createadditionallogistics:lazy_shaft" />, <ItemLink id="createadditionallogistics:lazy_cogwheel" />, <ItemLink id="createadditionallogistics:flexible_shaft" /> | 超过两根的连续惰性传动杆可提高效率。柔性传动杆可用扳手逐面控制连接。 |

***

## 初次使用

### 基础物品连接

<Recipe id="create:crafting/logistics/andesite_funnel" />

制作 <ItemLink id="create:andesite_funnel" />，连接容器与物品运输线路。放置方式请看思索演示。

先用传送带或溜槽连接一个输入容器和一个输出容器，再添加库存网络。Create 组件的布局请看思索演示。Additional Logistics 还包含销售账簿与列车网络监视器外设。后者是计算机接口，不是独立库存界面。

## 相关物品

<ItemGrid>
  <ItemIcon id="createadditionallogistics:sales_ledger" />
  <ItemIcon id="createadditionallogistics:network_monitor" />
</ItemGrid>

| 图示物品 |
| --- |
| <ItemLink id="createadditionallogistics:sales_ledger" /> |
| <ItemLink id="createadditionallogistics:network_monitor" /> |

## 相关页面

- [浏览配方](help.search.md)


***

## 相关模组

| 模组或内容 | 用途 | 状态 | 物品查询 |
| --- | --- | --- | --- |
| ![Create: Additional Logistics](images/catalog-CZaz7aje.png) [Create: Additional Logistics](machines.logistics.md) | 扩展机械动力包裹处理，增加商店收银设备并改进工厂库存控制。 | 已安装基准版 | <EmiSearch query="@createadditionallogistics" /> |
