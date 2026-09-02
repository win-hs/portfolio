# Field-Box 網站建置規格書

給 Claude Code 執行。目標是產出一個可直接上傳 GitHub Pages 的 Jekyll 靜態網站。

---

## 1. 專案目標

把兩個分散的入口合併成單一網站：

| 現況 | 處置 |
|---|---|
| `sites.google.com/view/fieldbox` — Google Sites 做的工具選單頁 | **廢除**，內容由本專案取代 |
| `hackmd.io/AtD_ktGZQbOBhzvRZlk3iQ` — QGIS 課程索引 | **保留**，本站以外連方式整合 |

新站 = 工具選單 + QGIS 課程索引，合併為單頁。

**第一階段不搬 HackMD 內容**，課程連結全部指向現有 HackMD note。之後若要搬遷，只需替換 `_data/course.yml` 中的 url 欄位，版面不動。

---

## 2. 硬性限制

1. **無建置流程。** 只用 GitHub Pages 原生支援的 Jekyll，不得引入需要本機 `bundle exec` 或 CI 的功能。
2. **不使用任何 Jekyll plugin。** GitHub Pages 白名單以外的 plugin 一律不用。
3. **不使用外部 CDN、不引入 JS 框架。** 全站零 JavaScript。字型使用系統字型堆疊，不得連 Google Fonts。
4. **內容與版面必須分離。** 所有會變動的文字放在 `_data/*.yml`，模板只負責迴圈輸出。非工程背景的維護者必須能只改 YAML 就更新網站。
5. **單一路徑，不做 fallback。** 不寫「若某欄位不存在則顯示預設值」這類防禦邏輯；欄位缺漏就讓它顯示為空，由維護者自己看出來修正。

---

## 3. 部署設定

- Repo 名稱：`fieldbox`
- 發佈網址：`https://win-hs.github.io/fieldbox/`
- `baseurl: "/fieldbox"`，`url: "https://win-hs.github.io"`
- 站內資源一律用 `{{ site.baseurl }}/...`
- **工具連結例外**：五個工具是 domain 根目錄下的獨立 repo（`/coordinate-converter/` 等），連結直接使用 YAML 中的絕對路徑，**不得**套上 baseurl

---

## 4. 檔案結構

```
fieldbox/
├── _config.yml
├── _data/
│   ├── tools.yml
│   └── course.yml
├── _layouts/
│   └── default.html
├── assets/
│   └── css/
│       └── style.css
├── index.html
└── README.md          ← 給維護者看的操作說明，需排除在建置外
```

---

## 5. 資料檔規格

### `_data/tools.yml`

陣列，每項五個欄位：

```yaml
- mark: C          # 圓形標記內的單一字母
  name: Coord-Converter
  zh: 座標批次轉換
  desc: TWD97 二度分帶與 WGS84 經緯度互轉，支援整份 CSV 一次處理。
  url: /coordinate-converter/
```

五項工具（`url` 為已上線的真實網址）：

| mark | name | zh | url |
|---|---|---|---|
| G | GoTime | 開工吉時 | `/gotime` |
| C | Coord-Converter | 座標批次轉換 | `/coordinate-converter/` |
| T | Triangulation | 三角定位 | `/triangulation/` |
| B | BatchTriangulation | 批次三角定位 | `/batch-triangulation/` |
| M | Mappin | 照片地圖標記 | `/mappin/` |

`desc` 欄位為暫定文案，維護者會自行修正，照抄即可。

### `_data/course.yml`

三個 key：`basics`、`skills`、`resources`，各為 `{title, url}` 陣列。完整內容見附錄 A。

---

## 6. 版面規格

### 6.1 設計 token（CSS 變數）

```
--paper:     #F1F3EE   頁面底色
--ink:       #16231B   主要文字
--moss:      #3E5C48   次要文字、連結
--moss-soft: #7B9483   輔助說明文字
--contour:   #CBD6C8   等高線
--tape:      #E0A81E   強調色（測量布條黃），僅用於重點標記
--rule:      #D3DBCF   分隔線、格線
```

容器最大寬度 `1040px`，左右 padding `28px`。

### 6.2 字型

```
標題："Songti TC", "Noto Serif TC", "PMingLiU", serif
內文："PingFang TC", "Noto Sans TC", "Microsoft JhengHei", -apple-system, sans-serif
數據/座標：ui-monospace, "SFMono-Regular", Menlo, monospace
```

內文 16px / line-height 1.75。

### 6.3 區塊順序

1. **頂部導覽列** — sticky，底部 1px 分隔線。左為站名，右為錨點連結（工具 / QGIS 課程 / 關於）。hover 時以 `--tape` 色底線標示。
2. **Hero** — 背景為 inline SVG 等高線（七條曲線 + 一個黃色十字準心標記），絕對定位鋪滿，`pointer-events: none`。前景為襯線大標、一段說明、一行 monospace 的補充資訊。
3. **工具區** (`#tools`) — 見 6.4。
4. **課程區** (`#course`) — 見 6.5，背景改為 `#EAEEE6` 並加上分隔線，明確區隔於工具區。
5. **頁尾** (`#about`) — 站點說明與聯絡信箱。

### 6.4 工具區版面

- **格線佈局，非卡片。** `display:grid`，`grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))`，`gap:1px`，容器背景設為 `--rule` 色以形成 1px 格線，每格自身背景為 `--paper`。
- **不得使用 border-radius、box-shadow 或漸層。** 五個工具是並列關係，視覺上應為等高線圖上的格網，而非浮起的卡片。
- 每格內容由上而下：圓形字母標記（30px、2px 邊框、`--moss` 色）→ 英文名 → 中文名 → 說明 → 底部靠齊的「開啟工具」。
- 整格為 `<a>`，hover 時整格底色變 `#E8EDE5`。

### 6.5 課程區版面

- 兩欄（`1fr 1fr`，gap 56px），左欄放入門基礎，右欄放實用技巧 + 上課資源 + 提示框。
- **入門基礎使用 `<ol>` 並以 CSS counter 顯示編號**，因為這 12 篇有明確學習順序。
- **實用技巧與上課資源使用 `<ul>`**，項目符號為 `--tape` 色的點，因為兩者無先後關係。
- 兩種清單的項目皆有底部 1px 分隔線。
- 提示框：左側 3px `--tape` 色實線，內容為「第一次上課？先看『上課前須知』把環境裝好，可以省下課堂上一半的時間。」

### 6.6 品質底線

- 響應式：760px 以下課程區改為單欄，其餘區塊自然收合。
- 鍵盤焦點可見（`:focus-visible` 與 hover 同樣式）。
- 尊重 `prefers-reduced-motion`。
- 全站不使用非使用者觸發的動畫。

---

## 7. README.md 規格

寫給**沒有程式背景**的維護者。必須涵蓋且僅涵蓋：

1. 如何在 GitHub 網頁介面上編輯檔案（點檔案 → 鉛筆 → 改 → Commit），約一分鐘後生效
2. 改工具說明 → 改 `_data/tools.yml` 的 `desc`
3. 新增工具 → 複製 `tools.yml` 中一整段五行貼到最後
4. 改課程連結或順序 → 改 `_data/course.yml`
5. **一條規矩：只用網頁介面編輯，只用 main 分支**，理由是避免 git 分支與合併衝突
6. 不要碰 `_layouts/` 與 `assets/`

語氣直接，不要教學式贅語，不要 emoji。

---

## 8. 驗收標準

- [ ] `jekyll build` 無錯誤、無警告
- [ ] 未使用任何 plugin，`Gemfile` 若存在僅含 `github-pages`
- [ ] 全站 HTML 中沒有 `<script>` 標籤
- [ ] 首頁的五項工具與 21 條課程連結全部由 `_data` 產生，模板中沒有任何硬編碼的工具名稱或課程標題
- [ ] 修改 `tools.yml` 中任一 `desc` 後重新建置，該文字正確更新
- [ ] 工具連結指向 `/coordinate-converter/` 而非 `/fieldbox/coordinate-converter/`
- [ ] CSS 中沒有 border-radius 與 box-shadow
- [ ] 375px 寬度下版面不破、不出現水平捲軸

---

## 附錄 A：課程資料完整內容

```yaml
basics:
  - title: 下載、安裝及開啟 QGIS
    url: https://hackmd.io/9Vm-AwItSqyaZ2wrUk2Lgw
  - title: 常用設定
    url: https://hackmd.io/PxigDGMIQhODQ4a_UOgQJQ
  - title: 加入向量、網格、圖磚圖層
    url: https://hackmd.io/4k49-6NlSqekwIlKXELUcw
  - title: 更改圖層座標格式（CRS）
    url: https://hackmd.io/Fy75zrcWSdWmb3fyiVFjKQ
  - title: 更改圖層的文字編碼
    url: https://hackmd.io/lbHbXiY3R4O6kiEd_EvApQ
  - title: 自訂圖徵樣式與標記
    url: https://hackmd.io/jpv-zEBMSCq-PcUJIM8Xzg
  - title: 地圖排版及輸出
    url: https://hackmd.io/8QLJ2KYuR-qq0IL5sZJPfg
  - title: 用 DEM 製作等高線、坡度、坡向與日照陰影
    url: https://hackmd.io/ttr0tFNvSBKwpeHjUEaJUg
  - title: 加入指北針、圖例、比例尺
    url: https://hackmd.io/T_C_Coq0RluhAaHviZS6bQ
  - title: 安裝外掛
    url: https://hackmd.io/hXKgu7JUR8GNAsk_3-dV_Q
  - title: 把 Excel 或 CSV 資料匯入 QGIS
    url: https://hackmd.io/n3KZy9-0RuyJT5hRzP1gKw
  - title: 只輸出選擇的圖徵或圖層
    url: https://hackmd.io/LXQ76p9NR9yA2-w7r3bPew

skills:
  - title: 把 Google Map 底圖加入 QGIS
    url: https://hackmd.io/C1ZwctoCSLeaLJ_5_5hf4w
  - title: 用 Quick Map Services 加入 OSM 底圖
    url: https://hackmd.io/Ar4w8oFhQfuDWMenDlcEyA
  - title: 地圖排版加入經緯度格線
    url: https://hackmd.io/R4sKo5xHTm2zTYlH18SI2g
  - title: "Point Sampling Tool：萃取點位數值"
    url: https://hackmd.io/HopZPsJ5Sxa7NRkrKexwHA
  - title: "Animove：MCP 與核密度估計繪製活動範圍"
    url: https://hackmd.io/aHwb42fiQx2iNNYfStEKYw

resources:
  - title: 上課前須知
    url: https://hackmd.io/P6CUQoXySReSu0eRv09pKA
  - title: 課程簡報與練習資料下載
    url: https://hackmd.io/xDRG9UwKRsaHuY8210wrgQ
  - title: 常見問題
    url: https://hackmd.io/PvUUcnGZRhSxNOW5nbZj7g
  - title: 學習資源、開放圖資與小工具整理
    url: https://hackmd.io/w2KRp5YURtqIhRK8XufNxA
```

---

## 附錄 B：文案

**Hero**

- 大標：野外用得上的／小工具與教學（兩行）
- 說明：座標轉換、無線電追蹤定位、照片點位標記，全部在瀏覽器裡跑。免安裝、免註冊，資料不會離開你的電腦或手機。
- Monospace 行：TWD97 / WGS84 · 開放原始碼 · 由生態調查現場需求長出來的工具

**工具區**

- 標題：工具｜副標：五項，持續增加中
- 引言：每個工具都是獨立的網頁，開了就能用。手機在野外也跑得動。

**課程區**

- 標題：QGIS 課程平台｜副標：野生動物保育所
- 引言：從安裝到出圖的完整教學，附課程簡報與練習資料。照著做就能完成一張可以放進報告的地圖。
- 分區標題：入門基礎 / 實用技巧 / 上課資源

**頁尾**

- 標題：關於 Field-Box
- 內文：這些工具來自實際的生態調查工作：需要什麼就寫什麼，寫完順手放上來給同樣需要的人用。全部在瀏覽器端運算，不上傳、不留存任何資料。
- 聯絡：發現問題或有功能想法，寄信給我：a.wen90@gmail.com

---

## 附錄 C：待確認事項

以下未定，先按預設實作，維護者確認後再調整：

1. **五個工具的 `desc` 文案為推測**，特別是 GoTime。維護者會直接改 YAML。
2. **與既有 portfolio 站的關係未定。** 本站建在 `/fieldbox/` 子路徑，不影響 `win-hs.github.io` 根目錄現有內容。若日後決定讓 Field-Box 佔據根目錄，只需改 `baseurl` 為空字串並搬移 repo。
3. **Google Sites 舊站**應在新站上線後放置轉址公告，觀察兩到三個月再關閉。
