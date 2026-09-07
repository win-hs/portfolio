---
layout: lesson
body_class: page-course
title: 把 Google Map 底圖加入 QGIS
seo_title: 把 Google Map 底圖加入 QGIS｜QGIS 課程 · Field-Box
desc: 在 XYZ Tiles 新增連線、貼上網址，就能把 Google 的道路圖、地形圖或衛星影像當底圖用。四種底圖的網址都整理在文內。
unit: skills
order: 1
permalink: /qgis/把-google-map-底圖加入-qgis/
hackmd: https://hackmd.io/C1ZwctoCSLeaLJ_5_5hf4w
---

# 如何把Google Map底圖加入QGIS中


![]({{ site.baseurl }}/assets/img/lessons/S01-01.png)
1.右鍵 `XYZ Tiles`  -> 點選 `New Connection`
<br>

![]({{ site.baseurl }}/assets/img/lessons/S01-02.png)
2.打上名稱、貼上底圖連接網址
<br>

![]({{ site.baseurl }}/assets/img/lessons/S01-03.png)
3.右鍵 `Roadmap`（或其他名稱）  -> 點選 `Add Layer to Project`
<br>

```
Google底圖連接網址：

1. Google道路圖
http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z} 

2. Google地形+道路圖
http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}

3. Google道路（白色道路）
http://mt0.google.com/vt/lyrs=r&hl=en&x={x}&y={y}&z={z}

4. Google衛星（無道路圖）
http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}

5. Google地形
http://mt0.google.com/vt/lyrs=t&hl=en&x={x}&y={y}&z={z}

6. Google衛星+道路圖
http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}
```

<br>
<br>
<br>

QGIS Version：QGIS 3.10.9
Original content: https://www.hatarilabs.com/ih-en/how-to-add-a-google-map-in-qgis-3-tutorial
Edited and Translated by Hs.Win, Date: 20201113
