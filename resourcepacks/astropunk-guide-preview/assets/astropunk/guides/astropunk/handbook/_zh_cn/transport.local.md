---
navigation:
  title: "在基地内移动"
  position: 0
  parent: reference.vehicles.md
  icon: minecraft:powered_rail
---

# 在基地内移动

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+Simulated+Offroad+road+vehicles+handles+suspension+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+Simulated+Offroad+%E8%BD%A6%E8%BE%86+%E6%82%AC%E6%8C%82+%E6%89%8B%E6%9F%84+%E6%95%99%E7%A8%8B)

## 超导管道线路

<EmiSearch query="@create" /> <EmiSearch query="@create_hypertube" />

![超导管道段落与支架](images/visual-local-hypertubes.png)

超导管道段落与支架

<ItemGrid><ItemIcon id="create_hypertube:hypertube" /><ItemIcon id="create_hypertube:hypertube_entrance" /><ItemIcon id="create_hypertube:hypertube_accelerator" /><ItemIcon id="create_hypertube:hypertube_junction" /><ItemIcon id="create_hypertube:tube_scanner_attachment" /><ItemIcon id="create_hypertube:redstone_detector_tube_attachment" /></ItemGrid>

超导管道是把你发射出去的管子，不是你驾驶的载具。

1. 手持管道右键已放置的管道，再放下第二段。两段就此连接。
2. 用同样方式继续延长。用扳手可以改变单个段的段数。
3. 两端各装一个入口，并给它至少每分钟 16 转。转速越高，行进越快。
4. 沿线加入加速器提高速度，或用右键把某个加速器设为制动模式。

不转的入口只是墙上的一个洞。入口模式用扳手切换，红石探测器附件可以用信号切换模式。


| 部件 | 作用 | 设置方式 |
| --- | --- | --- |
| <ItemLink id="create_hypertube:hypertube_accelerator" /> | 提速或制动 | 右键切换制动模式 |
| <ItemLink id="create_hypertube:hypertube_junction" /> | 连接最多三段管道 | 扳手循环模式 |
| <ItemLink id="create_hypertube:tube_scanner_attachment" /> | 探测通行者 | 无需设置，直接输出红石 |
| <ItemLink id="create_hypertube:redstone_detector_tube_attachment" /> | 切换入口或加速器模式 | 由红石输入控制 |

分叉器最多连接三段管道。行进途中用移动键选择分支。继续模式下通行者总是走两侧管道，居中模式下总是走前方管道。探测器附件在这两种强制模式之间切换。

扫描附件对幼年生物输出 8 级红石，对成年生物输出 15 级，所以一条信号线就能统计经过的对象。附件也可以同时装在加速器的任意一侧。

## 步道

<EmiSearch query="@escalated" />

<ItemGrid><ItemIcon id="escalated:metal_walkway_steps" /><ItemIcon id="escalated:wooden_walkway_steps" /></ItemGrid>

Escalated 增加金属与木质两种移动步道。它们和 Create 其他机器一样靠旋转驱动，沿地面运送你，而不是穿过管道。把它们装在超导管道的车站一端，用来代替再建一个入口。

<Recipe id="escalated:metal_walkway_steps" />


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Escalated](images/catalog-lyobyg8q.png) [Create: Escalated](transport.local.md) | 为机械动力建筑增加旋转动力驱动的自动扶梯。 | <EmiSearch query="@escalated" /> |
| ![Create: Hypertubes](images/catalog-atddrg1y.png) [Create: Hypertubes](transport.local.md) | 增加管道交通，让玩家在机械动力建筑之间穿行。 | <EmiSearch query="@create_hypertube" /> |
