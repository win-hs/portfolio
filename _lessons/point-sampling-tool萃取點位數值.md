---
layout: lesson
body_class: page-course
title: Point Sampling Tool：萃取點位數值
seo_title: Point Sampling Tool：萃取點位數值｜QGIS 課程 · Field-Box
desc: 手上一堆點位，想知道每個點的海拔、坡度，或落在哪一個分區裡。裝 Point Sampling Tool 外掛，選好點位圖層和要萃取的圖層就能一次帶出來。
unit: skills
order: 4
permalink: /qgis/point-sampling-tool萃取點位數值/
hackmd: https://hackmd.io/HopZPsJ5Sxa7NRkrKexwHA
---

# [Point Sampling Tool] 萃取點位中的數值/資料
![]({{ site.baseurl }}/assets/img/lessons/S04-01.png)
1.先下載Point Sampling Tool插件

<br>

![]({{ site.baseurl }}/assets/img/lessons/S04-02.png)
2.載入點位圖層及要萃取的圖層（Raster或Polygon皆可），範例中以DEM為例，要以點位萃取DEM的海拔高度。

<br>

![]({{ site.baseurl }}/assets/img/lessons/S04-03.png)
3.`Plugins` -> `Analyses` -> `Point Sampling Tool`

<br>

![]({{ site.baseurl }}/assets/img/lessons/S04-04.png)
4.選擇點位圖層、選擇萃取後所輸出的新圖層需要顯示的欄位。

<br>

![]({{ site.baseurl }}/assets/img/lessons/S04-05.png)
5.萃取後的新圖層，就會出現海拔的欄位、

<br>
<br>
<br>

QGIS Version：QGIS 3.10.9
20201218
