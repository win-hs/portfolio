# Field-Box 維護說明

網站網址：https://win-hs.github.io/portfolio/

網站有兩頁：

- 首頁（作品）—— 五個工具
- QGIS 課程平台 —— 課程目錄，底下 21 篇課程各自一頁

兩邊的內容放在不同地方，改法也不一樣。

---

## 改工具（首頁）

工具的文字放在 `_data/tools.yml`，直接在 GitHub 網頁上改。

點開檔案，按右上角鉛筆圖示，改完捲到最下面按 Commit changes，約一分鐘後網站更新。

改說明文字就改 `desc` 那一行：

```yaml
- logo: coord-converter.png
  name: Coord-Converter
  zh: 座標批次轉換
  desc: 這一行就是網頁上顯示的說明文字。
  url: /coordinate-converter/
```

新增工具就複製一整段五行貼到檔案最後面，再改內容。

- `logo`：logo 圖檔的檔名，圖檔放在 `assets/img/logos/`
- `name`：英文名
- `zh`：中文名，網頁上顯示成「英文名：中文名」
- `desc`：說明文字
- `url`：工具網址，開頭要有斜線，例如 `/mappin/`

段落之間空一行。前面的 `- ` 和每行開頭的兩個空格都不能刪。

新增工具前要先把 logo 圖放進 repo：在 `assets/img/logos/` 按 Add file → Upload files 上傳，再把檔名填到 `logo` 那一行。logo 原稿在 `logo.pptx`，從 PowerPoint 另存成去背 PNG 即可。

---

## 改課程

課程**不在 GitHub 上改**，在 Obsidian 改。

課程原稿在 `E:\8_Obsidian\Obsidian\QGIS課程\`，那裡是唯一的來源。網站上的課程頁是從那裡產生出來的。

### 改一課的內容

在 Obsidian 打開那篇改，圖片直接貼上即可。

### 新增一課

在 `QGIS課程\` 新增一篇筆記，開頭必須有這四行：

```
---
title: 用 Field Calculator 批次計算欄位
unit: basics
order: 13
---
```

- `title`：課程目錄上顯示的標題
- `unit`：`basics` 入門基礎、`skills` 實用技巧、`resources` 上課資源
- `order`：在該單元裡的排序，數字小的在前

檔名建議沿用現有格式（`B13-用 Field Calculator 批次計算欄位`），前綴只影響 Obsidian 裡的排序，不影響網站。

### 摺疊區塊

課程裡可以收合的段落，在 Obsidian 寫成：

```
> [!note]- 這是標題
> 這裡是收合起來的內容
> ![[圖片.png]]
```

`[!note]` 後面那個減號是「預設收合」的意思，拿掉就變成展開。

### 改完之後

課程改完不會自動上線，要跑一次同步：

```bash
python E:\9_ClaudeSpace\github.io\Portfolio\tools\sync.py
```

跑完再把 repo 的變更 commit 並 push。這兩步可以直接請 Claude 做。

---

## 規矩

**GitHub 上只用網頁介面編輯，只動 main 分支。** 不要開新分支、不要用 Pull Request。分支和合併衝突處理起來很麻煩，維護這個網站不需要用到。

**不要在 GitHub 上改 `_lessons/` 和 `assets/img/lessons/`。** 這兩個資料夾是同步腳本產生的，下次同步會整個重建，改了會被蓋掉。課程一律在 Obsidian 改。

**不要碰 `_layouts/` 和 `assets/css/`。** 這是版面和樣式，改壞了整個網站會跑版。
