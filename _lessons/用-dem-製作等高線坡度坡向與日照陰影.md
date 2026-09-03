---
layout: lesson
title: 用 DEM 製作等高線、坡度、坡向與日照陰影
unit: basics
order: 8
permalink: /qgis/用-dem-製作等高線坡度坡向與日照陰影/
hackmd: https://hackmd.io/ttr0tFNvSBKwpeHjUEaJUg
---

# 如何用數值高程模型(DEM)製作等高線(Contour)、坡度(Slope)、坡向(Aspect)及日照陰影圖(Hillshade)



<details markdown="1">
<summary>如何用數值高程模型(DEM)製作等高線(Contour)</summary>

![]({{ site.baseurl }}/assets/img/lessons/B08-01.png)
1.`Raster` -> `Extraction` -> `Contour`

<br>

![]({{ site.baseurl }}/assets/img/lessons/B08-02.png)
2.輸入圖層位置、等高線間距、資料參考欄位、圖層儲存位置，再點`run`

<br>


</details>




<details markdown="1">
<summary>如何用數值高程模型(DEM)分析坡度(Slope)</summary>

![]({{ site.baseurl }}/assets/img/lessons/B08-03.png)
1.`Raster` -> `Analysis` -> `Slope`

<br>

![]({{ site.baseurl }}/assets/img/lessons/B08-04.png)
2.輸入圖層位置、圖層儲存位置，其他參數若無特殊需求，維持預設就好，再點`Run`

<br>


</details>



<details markdown="1">
<summary>如何用數值高程模型(DEM)分析坡向(Aspect)</summary>

![]({{ site.baseurl }}/assets/img/lessons/B08-05.png)
1.`Raster` -> `Analysis` -> `Aspect`

<br>

![]({{ site.baseurl }}/assets/img/lessons/B08-06.png)
2.輸入圖層位置、圖層儲存位置，其他參數若無特殊需求，維持預設就好，再點`Run`
<br>

</details>




<details markdown="1">
<summary>如何用數值高程模型(DEM)製作日照陰影圖(Hillshade)</summary>

![]({{ site.baseurl }}/assets/img/lessons/B08-07.png)
1.`Raster` -> `Analysis` -> `Hillshade`

<br>

![]({{ site.baseurl }}/assets/img/lessons/B08-08.png)
2.輸入圖層位置、圖層儲存位置，其他參數若無特殊需求，維持預設就好，再點`Run`

<br>


</details>



<br>

延伸閲讀：
1. [QGIS 如何製作一張專業又漂亮的地形圖](https://www.youtube.com/watch?v=QzOao-tc7Ag&ab_channel=%E9%BB%83%E6%95%8F%E9%83%8E)
2. [如何做好看的等高線圖](https://www.youtube.com/watch?v=0oyZ0gwLKXY&ab_channel=OpenSourceOptions)
<br>

### 什麽是數值高程模型(DEM)？
> 以數值化三度空間坐標表達地表高程。通常抽取地面上等距離樣本點記錄其高程及地面坐標。此類資料可以轉化為等高線、坡度及坡向資料，並可以做3D空間的虛擬實境展示。DEM在環境研究及實務上十分重要，是對地形視覺模擬或更細緻之環境模擬模式中的基礎資料。(摘自國家研究員辭書)

<br>
<br>
<br>

QGIS Version：QGIS 3.10.9
Date: 20201113
