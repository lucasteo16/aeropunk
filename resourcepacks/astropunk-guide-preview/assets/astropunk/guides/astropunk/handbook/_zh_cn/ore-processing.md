---
navigation:
  title: 矿石加工
  icon: create:crushing_wheel
  parent: index.md
item_ids:
  - create:crushing_wheel
  - create:crushed_raw_iron
---

# 矿石加工

用机械动力的设备把原料加工成有用的产物。先看配方，再选工艺，不要以为机器越大就一定能获得更多金属。

<Row>
  <ItemImage id="minecraft:raw_iron" />
  <ItemImage id="create:crushing_wheel" />
  <ItemImage id="create:crushed_raw_iron" />
  <ItemImage id="create:encased_fan" />
</Row>

## 从粗铁开始

粉碎粗铁可以得到粉碎铁矿石，并有概率得到经验颗粒。洗涤粉碎铁矿石可以得到铁粒，并有概率得到红石。

在物品浏览器中搜索 `@create`，再查找粉碎轮和鼓风机。英文检索词：Crushing Wheel, Encased Fan, Raw Iron。建造之前先查看配方和已有的思索演示。

## 查看配方

下面先测试普通合成配方。物品提示与链接使用游戏中的真实物品。

<RecipeFor id="minecraft:iron_ingot" fallbackText="这个配方暂时无法显示。" />

机械动力的加工配方使用自定义类型。下面是显示能力检查，不代表默认渲染器一定支持。若无法显示，请在物品浏览器中查看相应材料。

<Recipe id="create:crushing/raw_iron" fallbackText="粉碎配方需要自定义渲染器。请在物品浏览器中查看粗铁。" />

<Recipe id="create:splashing/crushed_raw_iron" fallbackText="洗涤配方需要自定义渲染器。请在物品浏览器中查看粉碎铁矿石。" />

## 查看机器外形

这个交互场景展示真实方块模型和注释，不是一台已经组装或供能的加工机器。

<GameScene zoom="3" interactive={true}>
  <Block id="create:crushing_wheel" x="0" />
  <Block id="create:encased_fan" x="2" />
  <BlockAnnotation x="0">粉碎轮。实际排列方式请查看它的思索演示。</BlockAnnotation>
  <BlockAnnotation x="2">鼓风机。加工装置的布置取决于你要进行的工艺。</BlockAnnotation>
</GameScene>

## 继续探索

原料输送和产物收集属于仓储与物流，相关指南尚未编写。

[返回活动指南](index.md)

这一版测试文字、布局、物品模型、配方支持和交互场景。直接打开物品浏览器与思索的按钮，以及图标地图式首页，尚未实现。
