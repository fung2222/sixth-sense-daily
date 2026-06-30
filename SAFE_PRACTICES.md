# Sono 網站安全開發守則

> 目標：以後加遊戲、加工具、改內容時，盡量避免再出現 Tab 失效、Modal 重複、功能無反應等問題。

## 目前現況（2026-06-30）

- 檔案中仍有 **6 個重複** 的 Tab Event Listener 和工具箱 Event Listener（網站功能正常，但屬於技術債）。
- 所有工具已模組化，每個工具有獨立 trigger。
- Tab 切換使用 Event Listener（非 inline onclick）。
- 遊戲列表使用 `.game-list` + `.game-item` 結構。

---

## 以後加新遊戲規則

1. 在 `.game-list` 區塊最尾加入新 `<div class="game-item">`。
2. 參考現有遊戲模板（例如 猜拳火柴人、火柴人格鬥）。
3. 新遊戲盡量放在 `games/` 資料夾，並使用獨立 SVG 圖示。
4. 遊戲卡片使用 `onclick="toggleGame(this)"`（現有機制）。

**禁止**：在中間插入新遊戲或改動現有遊戲順序（除非一次過重新排序）。

---

## 以後加新工具規則（最重要）

### 正確做法：
1. **只改最後一個** 工具箱 Event Listener。
2. 在 listener 入面加入一行：
   ```js
   else if (id === '新工具Trigger') open新工具Modal();
   ```
3. 新工具的 Modal HTML 放在 `<body>` 最尾。
4. 新工具的 JS 函數（`open新工具Modal`、`init新工具` 等）放在檔案最尾的 `<script>` 區塊。
5. 如果需要初始化邏輯，新增 `init新工具Trigger()` 函數，並在最後初始化。

### 嚴禁做法：
- 不要在中間任何位置再插入新的 `document.querySelectorAll('.card.tool-sm')` listener。
- 不要重複整個 listener block。
- 不要用 Python 字串替換大範圍修改 HTML/JS。

---

## Modal 命名規範

- Modal ID：`xxx-modal`（例如 `mtr-modal`、`weather-modal`）
- 開啟函數：`openXxxModal()`
- 關閉按鈕：使用現有 `.modal-close` class

---

## 日常改動流程

1. **改動前**：`git status` 確認乾淨
2. **大改動前**：先 commit（或建立新 branch）
3. **改動後**：即時測試以下項目：
   - Tab 切換（每日 / 遊戲 / 工具箱）
   - 工具箱所有工具點擊
   - AI 聊天 widget 展開/收起
   - 遊戲卡片展開
4. **有問題**：立即 revert，唔好繼續疊加修改

---

## 關於 MTR 到站時間工具

之前曾經因為重複插入 listener 而導致整個 Tab 系統失效。  
以後加 MTR 必須嚴格遵守「只改最後一個 listener」規則。

---

## 總結

- **少動結構，多改內容**
- **永遠只喺最後一個 listener 加新工具**
- **改完即測，壞咗即還原**

遵守以上規則，之後加遊戲同工具出錯機會會大幅降低。