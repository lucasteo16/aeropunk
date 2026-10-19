---
navigation:
  title: "用机器制作食物"
  position: 10
  parent: reference.food.md
  icon: minecraft:smoker
---

# 用机器制作食物

## 切片机

<EmiSearch query="@farmersdelight" /> <EmiSearch query="@sliceanddice" />

![受热烹饪锅旁的机械加工](images/visual-automatic-cooking.png)

受热烹饪锅旁的机械加工

<ItemGrid><ItemIcon id="sliceanddice:slicer" /><ItemIcon id="farmersdelight:cutting_board" /><ItemIcon id="farmersdelight:flint_knife" /></ItemGrid>

<ItemLink id="sliceanddice:slicer" /> 把砧板加工自动化，但不会把食材直接变成成品料理。机器内需要装入刀具，本包中每加工一份物品都会消耗刀的耐久，因此要准备修理手段或备用刀具。

机器需要旋转动力。放入食材和正确的刀，它会产出与砧板相同的分割物。把产物送入下一台设备或仓储箱。

### 切片机合成

<Recipe id="sliceanddice:slicer" />

放置切片机，装入刀具，再连接旋转动力与食材输入。围绕产线建造前先查看机器界面里当前装入的工具。

***

## 喷灌器与水盆

<ItemGrid><ItemIcon id="sliceanddice:sprinkler" /><ItemIcon id="sliceanddice:fertilizer_bucket" /><ItemIcon id="minecraft:water_bucket" /></ItemGrid>

<ItemLink id="sliceanddice:sprinkler" /> 借助旋转为农田浇水施肥。本包中容量为三百毫桶，每次使用消耗一百毫桶，水平范围五格。一桶水可装三次。把它放在作物行上方并接入水源，也可以手动补充。

<ItemLink id="sliceanddice:fertilizer_bucket" /> 提供肥料。它与饮用水、食物容器分开存放。

Slice and Dice 还加入受热水盆烹饪。底部受热的水盆可批量完成农夫乐事的锅类配方，适合为整个基地一次做大量料理。

| 设置 | 本包取值 | 实际影响 |
| --- | --- | --- |
| 喷灌器容量 | 三百毫桶 | 一桶水可用三次 |
| 每次消耗 | 一百毫桶 | 按收获周期安排供水 |
| 水平范围 | 五格 | 覆盖十一格宽的条带 |
| 水盆热量 | 受热 | 需要受热的水盆底部 |

***

## 中央厨房

<EmiSearch query="@create" />

<ItemGrid><ItemIcon id="minecraft:redstone" /><ItemIcon id="farmersdelight:cooking_pot" /><ItemIcon id="farmersdelight:skillet" /><ItemIcon id="farmersdelight:stove" /></ItemGrid>

Create: Central Kitchen 把机械动力物流接到农夫乐事的设备上。机械手可以为受支持的 <ItemLink id="farmersdelight:cooking_pot" />、<ItemLink id="farmersdelight:skillet" />、炉灶和砧板装卸物品。打包机能把食材箱直接拆入锅中。锅炉加热器可作为烹饪热源，工作中的加热器还能加快锅与煎锅。

中央厨房还会把砧板配方转换为机械动力的锯切与 部署配方，让机械锯无需刀具也能切割食材。

不要假设每个锅类配方都有机器版本。搭建产线前在配方浏览器里打开目标料理，确认它实际的加工类型。

***

## 料理与材料

下表按制作工作站分组，列出本章其余物品。将光标移到图标上查看食物数值，在配方浏览器中查看具体料理。

| 分类 | 物品 |
| --- | --- |
| 饮品与农业流体 | <ItemGrid><ItemIcon id="farmersdelight:hot_cocoa" /><ItemIcon id="farmersdelight:apple_cider" /></ItemGrid> |

- [烹饪工具](food.utensils.md)
- [作物生产](food.growing.md)
- [机器与仓储](reference.machines-storage.md)

***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Slice & Dice](images/slice-and-dice-icon.png) [Create Slice & Dice](food.machine-cooking.md) | 增加自动进行 Farmer's Delight 食材处理的机械动力机器。 | <EmiSearch query="@sliceanddice" /> |
| ![Create: Central Kitchen](images/create-central-kitchen-icon.png) [Create: Central Kitchen](food.machine-cooking.md) | 将其他烹饪模组接入机械动力机器，实现食物自动加工。 | 无独立物品查询 |
