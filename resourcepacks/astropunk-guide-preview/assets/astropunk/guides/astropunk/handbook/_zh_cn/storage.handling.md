---
navigation:
  title: "整理、转移与丢弃物品"
  position: 1
  parent: reference.machines-storage.md
  icon: minecraft:bundle
---

# 整理、转移与丢弃物品

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Interactic+Renewed+Mouse+Tweaks+Inventory+tools+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Interactic+Renewed+Mouse+Tweaks+%E6%95%B4%E7%90%86%E3%80%81%E8%BD%AC%E7%A7%BB%E4%B8%8E%E4%B8%A2%E5%BC%83%E7%89%A9%E5%93%81+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## 物品栏本身就是界面

储存的时间大多耗在界面上，而不是容器里。本包装了三个界面模组，去掉重复的拖拽与点击。

打开任何受支持的容器，使用它的搜索栏与排序按钮。Sophisticated Inventory Interactions 在受支持的界面里加入搜索、玩家物品栏排序、容器排序与转移控制。

<ItemGrid><ItemIcon id="minecraft:chest" /><ItemIcon id="minecraft:hopper" /><ItemIcon id="minecraft:shulker_box" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| 界面操作 | 省掉什么 |
| --- | --- |
| 搜索栏 | 在一整箱里翻找一件物品 |
| 排序按钮 | 每次倒完东西后手动整理 |
| 转移控制 | 一叠一叠地按住 Shift 点击 |
| 在格子上滚动鼠标滚轮 | 手动拖动一叠物品 |

鼠标滚轮与拖拽由 Mouse Tweaks 处理。它是便利模组，具体手势值得在控制界面里确认一次，而不是假定与别的整合包相同。

***

## 什么会被捡起

<EmiSearch query="@interactic" />

<ItemGrid><ItemIcon id="interactic:item_filter" /><ItemIcon id="minecraft:hopper" /></ItemGrid>

| 设置 | 影响 |
| --- | --- |
| 过滤器内容 | 允许被收集的物品 |
| 拾取规则 | 过滤器是否决定进入物品栏的东西 |
| 渲染规则 | 被过滤的掉落是否以不同方式显示 |

Interactic Renewed 把拾取与渲染分开，因此过滤器可以把杂物从视野里隐藏，而不改变你实际收集的东西。下矿前就设好，别等物品栏塞满石头再设。

让掉落物更容易看清与拾取的也是这个模组。把某件物品从渲染里隐藏，不会阻止你捡起它。

***

## 垃圾桶不是储存

| 本包设置 | 取值 |
| --- | --- |
| 即时删除 | 关闭，物品会留在格子里 |
| 隐藏时仍可删除 | 关闭 |
| 禁止删除清单 | 为空，默认不保护任何物品 |
| 提示 | 开启 |

TrashSlot 给物品栏界面增加一个格子，并不新增物品。真正重要的是即时删除关闭。格子里的物品在被清空之前都还在，你因此有一次取回的机会。打开即时删除，等于对所有物品一次取消这次机会。

禁止删除清单为空，所以 TrashSlot 本身不保护任何东西。如果贵重物品总是掉进去，把它加进清单，而不是靠小心。

搬运按键与手册的当前绑定见[操作与按键](help.controls.md)。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Interactic Renewed](images/catalog-bm12h14f.png) [Interactic Renewed](storage.handling.md) | 改进玩家与世界中掉落物品的交互方式。 | <EmiSearch query="@interactic" /> |
| ![Mouse Tweaks](images/catalog-ac3cm3vq.png) [Mouse Tweaks](storage.handling.md) | 增加鼠标拖动与滚轮快捷操作，便于移动物品栏中的物品堆。 | 无独立物品查询 |
| ![Sophisticated Inventory Interactions](images/catalog-orgy0jio.png) [Sophisticated Inventory Interactions](storage.handling.md) | 为受支持的物品栏界面增加整理、搜索与转移操作。 | 无独立物品查询 |
| ![TrashSlot](images/catalog-vryk0bv7.png) [TrashSlot](storage.handling.md) | 在物品栏增加垃圾格，用于丢弃不需要的物品。 | 无独立物品查询 |
