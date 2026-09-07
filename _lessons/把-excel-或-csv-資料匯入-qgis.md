---
layout: lesson
body_class: page-course
title: 把 Excel 或 CSV 資料匯入 QGIS
seo_title: 把 Excel 或 CSV 資料匯入 QGIS｜QGIS 課程 · Field-Box
desc: 野外記錄多半躺在 Excel 裡。先另存成 CSV（有中文請選 UTF-8），再用 Add Delimited Text Layer 指定 XY 欄位和座標系統，點位就會出現在圖上。
unit: basics
order: 11
permalink: /qgis/把-excel-或-csv-資料匯入-qgis/
hackmd: https://hackmd.io/n3KZy9-0RuyJT5hRzP1gKw
---

# 把Excel或csv資料匯到QGIS中

我們的資料或Raw data常常是存在Excel裏面中，要如何匯入Qgis呢？

![]({{ site.baseurl }}/assets/img/lessons/B11-01.png)
1.原始檔案為Excel格式。

<br>

![]({{ site.baseurl }}/assets/img/lessons/B11-02.png)
2.將Excel格式另存成CSV格式，如果資料有中文建議用CSV UTF-8格式

<br>

![]({{ site.baseurl }}/assets/img/lessons/B11-03.png)
3.`Layer` -> `Add Layer` -> `Add Delimited Text Layer`

<br>

![]({{ site.baseurl }}/assets/img/lessons/B11-04.png)
4.File Format（檔案格式）->選擇CSV
XY Field -> 選擇XY座標的對應欄位
Geometry CRS（座標系統） ->選擇XY軸座標系統

<br>

![]({{ site.baseurl }}/assets/img/lessons/B11-05.png)
5.匯入成功就會看到點位出現在圖中。
<br>
<br>
<br>

QGIS Version：QGIS 3.10.9
 Date: 20201218
