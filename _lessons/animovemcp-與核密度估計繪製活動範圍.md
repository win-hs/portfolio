---
layout: lesson
title: Animove：MCP 與核密度估計繪製活動範圍
unit: skills
order: 5
permalink: /qgis/animovemcp-與核密度估計繪製活動範圍/
hackmd: https://hackmd.io/aHwb42fiQx2iNNYfStEKYw
---

# [Animove] 動物活動範圍繪製：最小凸多邊形法（Minimum Convex Polygon, MCP）與核密度估計 （Kernel Density Estimated） 
<br>

> 最小凸多邊形法（Minimum Convex Polygon, MCP）與核密度估計 （Kernel Density Estimated） 之定義請先參考文獻：
> 1. 最小凸多邊形法（Minimum Convex Polygon, MCP）：Mohr, C. O. (1947). Table of equivalent populations of North American small mammals. The American Midland Naturalist, 37(1), 223-249.
> 2. 核密度估計 （Kernel Density Estimated）：Worton, B. J. (1989). Kernel methods for estimating the utilization distribution in home‐range studies. Ecology, 70(1), 164-168.


<br>



![]({{ site.baseurl }}/assets/img/lessons/S05-01.png)
1.先下載Animove插件

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-02.png)
2.如安裝時發生錯誤資訊`(error message: Couldn't load plugin 'sextante_animove' due to an error when calling its classFactory() method)`，請先以OSGeo Shell安裝 *statsmodels* package

打開QGIS資料夾中的OSGeo Shell，並輸入`pip install statsmodels`

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-03.png)
3.載入要分析的點位圖層

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-04.png)
4.在Processing Toolbox中搜尋`animove`


<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-05.png)
5.選擇點位圖層、選擇個體編號的欄位、選擇需要選擇多少%的點位繪製MCP（此部分以繪製95%MCP為例）

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-06.png)
6.完成後的新圖層就為點位圖層的95%MCP

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-07.png)
7.若要繪製95%的KDE，則先選擇95%MCP中的點位

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-08.png)
8.選擇kernel density estimation 功能，勾選`selected features only`，並選擇參數。

<br>

![]({{ site.baseurl }}/assets/img/lessons/S05-09.png)
9.完成後的圖層即為95% KDE

<br>
<br>
<br>

QGIS Version：QGIS 3.34.8
20241208
