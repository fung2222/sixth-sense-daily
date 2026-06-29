# Games 管理指南

## 新增遊戲步驟

1. 在 `games/` 資料夾建立 SVG 檔案
   - 檔案命名：使用小寫 + 連字號，例如 `new-game.svg`
   - 建議尺寸：`viewBox="0 0 48 48"`
   - 使用統一 gradient 顏色：
     ```xml
     <linearGradient id="gxxx" x1="0%" y1="0%" x2="100%" y2="100%">
       <stop offset="0%" stop-color="#6bff6b"/>
       <stop offset="100%" stop-color="#00d4ff"/>
     </linearGradient>
     ```

2. 在 `index.html` 嘅 Games tab 加入以下模板：

```html
<!-- ── 遊戲名稱 ── -->
<div class="game-item">
  <div class="game-header" onclick="toggleGame(this)">
    <img src="games/new-game.svg" class="game-logo" alt="遊戲名稱">
    <div class="game-info">
      <span class="game-name">遊戲名稱</span>
      <span class="game-tag">類型</span>
    </div>
    <svg class="game-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <polyline points="6 9 12 15 18 9"/>
    </svg>
  </div>
  <div class="game-body">
    <p class="game-desc">遊戲簡介（1-2 句）</p>
    <a href="#" class="game-play-btn">▶ 開始遊戲</a>
  </div>
</div>
```

3. 遊戲類型標籤建議：
   - `經典`、`數字`、`派對`、`策略`、`動作`

4. 完成後記得 commit + push

## SVG 命名規則

- 使用小寫 + 連字號
- 避免使用中文檔名
- 範例：`snake.svg`、`2048.svg`、`memory-match.svg`
