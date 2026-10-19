---
navigation:
  title: "选择光影、动态光源与远景"
  position: 5
  parent: reference.appearance.md
  icon: minecraft:lantern
---

# 选择光影、动态光源与远景

## 光影兼容

<EmiSearch query="@create" />

![Complementary Reimagined 景观](images/feedback-shader-reimagined.png)

Complementary Reimagined 景观

Iris Flywheel Compat 衔接 Iris 光影与 Create 机器使用的 Flywheel 优化渲染。Iris Veil Compat 衔接 Iris 与 Aeronautics、Sable 使用的 Veil 效果。这些属于客户端渲染兼容组件，并非额外光影风格或服务器玩法。

新安装选择 Complementary Reimagined，但默认关闭光影。在 Iris 中主动开启光影后，检查机器与船体效果。原有玩家设置会保留。Veil 兼容组件为早期测试版本，提供兼容支持不代表每种光影效果都能正确显示。

***

## 光影与远景

Iris 加载光影包，Distant Horizons 显示简化远景。它们是独立系统。

新安装默认启用 Distant Horizons 自适应传输速度，根据客户端性能调整地形数据传输。这不会设置渲染距离，也不会加快地形生成。原有玩家设置会保留。

| 内容 | 作用 |
| --- | --- |
| Distant Horizons | 在普通渲染距离之外显示简化地形。 |
| Iris Shaders | 加载光影包。 |

***

## 动态光源

Sodium Dynamic Lights 及其机械动力与 Sable 兼容组件仅供重型版使用。动态光源属于视觉效果，不保证服务器阻止生物生成。

| 内容 | 作用 |
| --- | --- |
| Create Sable Dynamic Lights（仅重型版） | 将动态光源扩展到机械动力与 Sable 结构。 |
| Sodium Dynamic Lights（仅重型版） | 提供动态光源与 Sodium 设置整合。 |

***

## 相关页面

- [光影风格](visuals.shader-packs.md)
- [视频选项](visuals.interface.md)
- [照明与生成](building.safety.md)


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| <ItemImage id="minecraft:painting" /> [Create Sable Dynamic Lights](visuals.lighting.md) | 为机械动力与 Sable 移动结构上的光源增加动态光照支持。 | 无独立物品查询 |
| ![Distant Horizons](images/catalog-ucdwusmi.png) [Distant Horizons](visuals.lighting.md) | 在普通渲染距离之外显示简化地形。 | 无独立物品查询 |
| ![Iris & Oculus Flywheel Compat](images/catalog-ndhymy2k.png) [Iris & Oculus Flywheel Compat](visuals.lighting.md) | 衔接 Iris 光影与 Flywheel 机器渲染。 | 无独立物品查询 |
| ![Iris Shaders](images/catalog-yl57xq9u.png) [Iris Shaders](visuals.lighting.md) | 加载光影包。 | 无独立物品查询 |
| ![Iris Veil Compat](images/catalog-owqycho4.png) [Iris Veil Compat](visuals.lighting.md) | 衔接 Iris 光影与 Veil 渲染效果。 | 无独立物品查询 |
| <ItemImage id="minecraft:painting" /> [Sodium Dynamic Lights](visuals.lighting.md) | 提供动态光源与 Sodium 设置整合。 | 无独立物品查询 |
