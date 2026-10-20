---
navigation:
  title: "整理、转移与丢弃物品"
  position: 1
  parent: reference.machines-storage.md
  icon: minecraft:bundle
---

# 整理、转移与丢弃物品

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Sophisticated+Inventory+Interactions+TrashSlot+Mouse+Tweaks+chest+sorting+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Sophisticated+Inventory+Interactions+TrashSlot+Mouse+Tweaks+%E7%AE%B1%E5%AD%90+%E6%95%B4%E7%90%86+%E6%95%99%E7%A8%8B)

## 容器界面

![背包与垃圾桶格](images/visual-inventory-trash.png)

背包与垃圾桶格

Sophisticated Inventory Interactions 会给受支持的界面添加控件。本整合包为箱子、漏斗、发射器、潜影盒与马匹背包界面开启了它。

| 控件 | 作用 |
| --- | --- |
| 搜索框 | 把界面筛成匹配的格子，不移动物品 |
| 整理容器 | 重排打开的容器 |
| 整理背包 | 重排自己的格子，快捷栏保持原有顺序 |
| 移动按钮 | 默认转移与目的地物品匹配的内容，按住 Shift 时转移目的地能接收的全部物品 |

移动按钮有两种模式。不按 Shift 的左键只移动匹配目的地的物品，按住 Shift 的左键移动全部。可用格子不超过九个时搜索与排序开关会隐藏，所以漏斗与发射器没有它们，箱子有。

***


### 鼠标手势

Mouse Tweaks 为容器界面增加以下操作：

| 手势 | 结果 |
| --- | --- |
| 手持一组物品，按住左键拖过同类物品 | 将同类物品收进手持的这一组 |
| 按住 Shift 和左键拖过格子 | 将经过格子的物品快速转移到另一个物品栏 |
| 手持物品按住右键拖动 | 每次经过格子都放一件，重复经过也会继续放入 |
| 指向一组物品滚动滚轮 | 在该格与另一个物品栏之间转移物品 |

***

### 垃圾桶格

垃圾桶格隐藏时，按 <KeyBind id="key.trashslot.toggle" /> 显示它。

TrashSlot 会给受支持的界面加一个删除格。生存模式下最后放进去的物品可以取回，再放新的物品进去会替换它，这一步才是销毁。

| 本整合包的设定 | 取值 | 含义 |
| --- | --- | --- |
| 立即删除 | 关闭 | 放进去的物品先留在格子里，不会碰到就消失 |
| 隐藏时可删除 | 关闭 | 格子不显示时删除键无效 |
| 黑名单 | 空 | 配置默认不保护任何物品 |
| 提示 | 开启 | 第一次使用时说明用途 |

本整合包允许在创造模式使用删除键，创造模式的删除与立即删除设定无关，是永久删除。黑名单为空，贵重物品也不会受到删除保护。

## 拾取物品

<EmiSearch query="@interactic" />

<ItemGrid><ItemIcon id="interactic:item_filter" /></ItemGrid>

Interactic Renewed 提供 <ItemLink id="interactic:item_filter" />，用于选择性拾取。配方是四个铜锭围住一颗末影珍珠。

1. 手持过滤器并右键，打开物品列表。
2. 设置要过滤的物品。在界面中选择 Block（排除）可拒绝列表内物品，选择 Allow（允许）则只拾取列表内物品。
3. 关闭界面，手持过滤器潜行并右键，可开启或关闭过滤。这不会切换排除与允许模式。

启用过滤并选择 Block 模式后，走过列表内的掉落物时，它应留在地上，其他物品仍可正常拾取。关闭过滤后，列表不会阻止普通拾取。

***
- [物品与流体输送](machines.logistics.md) 传送带、漏斗、过滤器与路由。
- [大宗存储](storage.bulk.md) 仓库与更大容量存储。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Interactic Renewed](images/catalog-bm12h14f.png) [Interactic Renewed](storage.handling.md) | 改进玩家与世界中掉落物品的交互方式。 | <EmiSearch query="@interactic" /> |
| ![Mouse Tweaks](images/catalog-ac3cm3vq.png) [Mouse Tweaks](storage.handling.md) | 增加鼠标拖动与滚轮快捷操作，便于移动物品栏中的物品堆。 | 无独立物品查询 |
| ![Sophisticated Inventory Interactions](images/catalog-orgy0jio.png) [Sophisticated Inventory Interactions](storage.handling.md) | 为受支持的物品栏界面增加整理、搜索与转移操作。 | 无独立物品查询 |
| ![TrashSlot](images/catalog-vryk0bv7.png) [TrashSlot](storage.handling.md) | 在物品栏增加垃圾格，用于丢弃不需要的物品。 | 无独立物品查询 |
