---
navigation:
  title: "乘坐列车出行"
  position: 1
  parent: reference.vehicles.md
  icon: minecraft:rail
---

# 乘坐列车出行

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Create+train+passenger+schedule+conductor+railway+navigator+tutorial) · [中文](https://www.youtube.com/results?search_query=Create+%E5%88%97%E8%BD%A6+%E4%B9%98%E5%AE%A2+%E6%97%B6%E5%88%BB%E8%A1%A8+%E9%93%81%E8%B7%AF%E5%AF%BC%E8%88%AA+%E6%95%99%E7%A8%8B)

## 线路查询

<EmiSearch query="@createrailwaysnavigator" /> <EmiSearch query="@create" />

![装有 Bells & Whistles 配件的列车车体](images/visual-train-fittings.png)

装有 Bells & Whistles 配件的列车车体

<ItemGrid><ItemIcon id="createrailwaysnavigator:navigator" /><ItemIcon id="createrailwaysnavigator:train_station_clock" /><ItemIcon id="create:track_station" /></ItemGrid>

<ItemLink id="createrailwaysnavigator:navigator" /> 查询已经存在的铁路网络。它不铺轨，也不运送你。打开后选择出发站与目的站，它会列出车次、换乘站以及每一段上列车的实时位置。

车站列表来自已放置并命名的 <ItemLink id="create:track_station" />。没命名的车站无法选择，没有时刻表的线路也没有车次可显示。

<ItemLink id="createrailwaysnavigator:train_station_clock" /> 显示车站时间和下一班发车。它装在候车处，不装在车上。

## 乘客显示屏

### 显示外形

<ItemGrid><ItemIcon id="createrailwaysnavigator:advanced_display" /><ItemIcon id="createrailwaysnavigator:advanced_display_block" /><ItemIcon id="createrailwaysnavigator:advanced_display_panel" /><ItemIcon id="createrailwaysnavigator:advanced_display_half_panel" /><ItemIcon id="createrailwaysnavigator:advanced_display_slab" /><ItemIcon id="createrailwaysnavigator:advanced_display_sloped" /></ItemGrid>

### 紧凑显示与配置

<ItemGrid><ItemIcon id="createrailwaysnavigator:advanced_display_small" /><ItemIcon id="create:wrench" /></ItemGrid>

显示屏家族是同一块屏幕的多种形状，可装到墙面、台阶、斜面或小立柱上。

| 形状 | 适用位置 |
| --- | --- |
| <ItemLink id="createrailwaysnavigator:advanced_display_block" /> | 整面墙板 |
| <ItemLink id="createrailwaysnavigator:advanced_display_panel" /> | 宽墙条 |
| <ItemLink id="createrailwaysnavigator:advanced_display_half_panel" /> | 窄条 |
| <ItemLink id="createrailwaysnavigator:advanced_display_slab" /> | 矮台或柜台 |
| <ItemLink id="createrailwaysnavigator:advanced_display_sloped" /> | 站台上方的斜装 |
| <ItemLink id="createrailwaysnavigator:advanced_display_small" /> | 立柱或车厢内部 |

对已放置的显示屏使用扳手可以选择显示内容。可选项目包括列车终点、乘客信息、站台、发车板与静态文字。终点显示跟随某一列车，所以装在车厢里。站台或发车板装设在车站，可以列出多趟车次。

<Recipe id="createrailwaysnavigator:advanced_display" />

## 可用的车站

<ItemGrid><ItemIcon id="create:track_station" /><ItemIcon id="createrailwaysnavigator:advanced_display_block" /><ItemIcon id="createrailwaysnavigator:navigator" /></ItemGrid>

1. 在 <ItemLink id="create:track_station" /> 上给车站命名，并确认列车时刻表里会停靠该站。
2. 把站台显示屏朝向候车区，设为发车板。
3. 在每节车厢内装一块终点显示屏，绑定该列车。
4. 带着导航器确认两站之间能查到车次，再邀请乘客上车。

导航器查不到线路时，问题在时刻表或车站名，不在导航器。


***

## 相关模组

| 模组或内容 | 用途 | 物品查询 |
| --- | --- | --- |
| ![Create Railways Navigator](images/catalog-dq3stxps.png) [Create Railways Navigator](transport.passenger.md) | 增加列车路线搜索、乘客信息显示与时刻表功能。 | <EmiSearch query="@createrailwaysnavigator" /> |
