# Field-Box 維護說明

網站網址：https://win-hs.github.io/portfolio/

## 怎麼改東西

在 GitHub 網頁上點開要改的檔案，按右上角的鉛筆圖示，改完捲到最下面按 Commit changes。
約一分鐘後網站就會更新，重新整理網頁即可看到。

## 改工具的說明文字

改 `_data/tools.yml`，找到那個工具的 `desc` 那一行，把冒號後面的文字換掉。

```yaml
- mark: C
  name: Coord-Converter
  zh: 座標批次轉換
  desc: 這一行就是網頁上顯示的說明文字。
  url: /coordinate-converter/
```

## 新增一個工具

複製 `_data/tools.yml` 裡任何一整段五行，貼到檔案最後面，再把五個欄位改成新工具的內容。

- `mark`：格子左上角圓圈裡的那個字母，一個字
- `name`：英文名
- `zh`：中文名
- `desc`：說明文字
- `url`：工具的網址，開頭要有斜線，例如 `/mappin/`

段落之間空一行。前面的 `- ` 和每行開頭的兩個空格都不能刪。

## 改課程連結或順序

改 `_data/course.yml`。裡面分三區：

- `basics` 入門基礎，網頁上會自動編號，所以這裡的排列順序就是上課順序
- `skills` 實用技巧
- `resources` 上課資源

每一課兩行，`title` 是顯示的標題，`url` 是 HackMD 網址。
要換順序就整組兩行搬動，要刪就整組兩行刪掉，要新增就複製一組貼上再改。

## 規矩

只用 GitHub 網頁介面編輯，只動 main 分支。
不要開新分支、不要用 Pull Request。分支和合併衝突處理起來很麻煩，維護這個網站不需要用到。

## 不要碰的東西

`_layouts/` 和 `assets/` 這兩個資料夾是版面和樣式，改壞了整個網站會跑版。
