---
navigation:
  title: "熔岩泉"
  position: 9
  parent: reference.machines-storage.md
  icon: create:mechanical_drill
---

# 熔岩泉

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Molten+Vents+activate+underwater+vent+orestone+lava+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Molten+Vents+%E6%B5%B7%E5%BA%95%E7%86%94%E5%B2%A9%E6%B3%89+%E6%BF%80%E6%B4%BB+%E7%9F%BF%E7%9F%B3+%E5%B2%A9%E6%B5%86+%E6%95%99%E7%A8%8B)

## 海底的熔岩泉

<EmiSearch query="@molten_vents" />

![休眠熔岩泉](images/molten-vent-dormant.png)

在本整合包中，熔岩泉生成于水下。休眠泉是一片矿石构造，内部藏有表面带岩浆的核心。激活后，把熔岩放在激活核心上，该处熔岩源会被消耗并变成对应矿石。泉不会生成熔岩，每次转换都需要新的熔岩源。

| 泉 | 外观 | 产出 |
| --- | --- | --- |
| <ItemLink id="molten_vents:active_molten_asurine" /> | <ItemGrid><ItemIcon id="molten_vents:active_molten_asurine" /></ItemGrid> | 阿斯瑞恩矿石 |
| <ItemLink id="molten_vents:active_molten_veridium" /> | <ItemGrid><ItemIcon id="molten_vents:active_molten_veridium" /></ItemGrid> | 维瑞丁矿石 |
| <ItemLink id="molten_vents:active_molten_crimsite" /> | <ItemGrid><ItemIcon id="molten_vents:active_molten_crimsite" /></ItemGrid> | 克里姆赛特矿石 |
| <ItemLink id="molten_vents:active_molten_ochrum" /> | <ItemGrid><ItemIcon id="molten_vents:active_molten_ochrum" /></ItemGrid> | 奥克鲁姆矿石 |
| <ItemLink id="molten_vents:active_molten_scorchia" /> | <ItemGrid><ItemIcon id="molten_vents:active_molten_scorchia" /></ItemGrid> | 斯科奇亚矿石 |
| <ItemLink id="molten_vents:active_molten_scoria" /> | <ItemGrid><ItemIcon id="molten_vents:active_molten_scoria" /></ItemGrid> | 斯科利亚矿石 |

每一族都有休眠与激活两种方块。休眠形态在泉体外壳里，什么也不做，激活形态才会把熔岩变成石头。

***

## 激活熔岩泉

1. 清空泉体内部，直到找到与周围矿石相同、但表面带岩浆的那一块。
2. 在岩浆核心旁引爆 TNT，让爆炸触及核心。
3. 看岩浆变亮，这一块就激活了。

<GameScene zoom="3" interactive={true}>
<Block id="molten_vents:dormant_molten_asurine" />
<Block x="2" id="molten_vents:active_molten_asurine" />
</GameScene>

暗色核心处于休眠状态，更亮的核心已被激活。

<ItemLink id="molten_vents:dormant_molten_asurine" />

激活与供料：<ItemLink id="minecraft:tnt" />与<ItemLink id="minecraft:lava_bucket" />.

| 看到的现象 | 原因 |
| --- | --- |
| 爆炸毫无反应 | 炸的是普通矿石，不是岩浆核心 |
| 泉还是暗的 | 爆炸没有触及核心 |
| 熔岩停在冷泉上 | 核心从未被激活 |

这里的水下作业要留出游泳空间，并准备好呼吸手段。

***

## 进熔岩，出石头

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="create:hose_pulley" /><ItemIcon id="create:fluid_pipe" /><ItemIcon id="create:mechanical_pump" /></ItemGrid>

把熔岩放到激活的泉上，熔岩会被消耗并替换成该泉的矿石，所以泉是把熔岩转换成建筑与粉碎材料的装置，本身不产生东西。

| 供料方式 | 适合什么情况 |
| --- | --- |
| 手提桶 | 验证泉是否工作 |
| 熔岩湖上的 <ItemLink id="create:hose_pulley" /> | 熔岩来源仍需补充，除非该流体体积满足软管滑轮的无限源规则 |
| 从储罐抽取 | 已经在为燃料或浇铸输送熔岩 |

转换成功后，收集生成的矿石，并补充熔岩源再重复操作。具体收集与补料布局取决于地点，建议先用桶确认转换成功，再考虑自动化。

- [材料加工](machines.ore-processing.md) 粉碎与清洗矿石。
- [物品与流体输送](machines.logistics.md) 把石头运走的传送带。
- [加工供热](power.burners.md) 可能也需要这些熔岩的热源。

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create: Molten Vents](images/create-molten-vents-icon.png) [Create: Molten Vents](machines.renewables.md) | 通过熔融喷口提供可再生的机械动力含矿石材。 | <EmiSearch query="@molten_vents" /> |
