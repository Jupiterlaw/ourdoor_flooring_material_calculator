# Outdoor Flooring Material Calculator (戶外木地板材料計算器)

[![Calculator Suite](https://img.shields.io/badge/Calculator%20Suite-Outdoor%20Flooring-01696F?style=flat-square)](https://github.com/Jupiterlaw/calculator-suite)

戶外木地板及面通材料計算器 — 快速計算地板分段、總板數、面積對比，以及面通、底通與鋁角用量。

> **現場第一線工具**：專為工地環境設計，大按鈕、大字體、高對比度，即使在陽光直射下也能清晰閱讀。

---

## 功能特色

- **地板結構計算** — 按最大等分規則自動計算每板等分數、每段長度、總行數、總等分數
- **總地板件數** — 根據空間尺寸與地板規格計算所需總板數
- **面積對比** — 空間總面積 vs 實際地板總面積，提供面積差數據
- **面通數量計算** — 自動計算面通行數、總長度及所需支數
- **底通支援** — 可啟用底通計算，獨立顯示行數、長度與支數
- **鋁角計算** — 可選啟用鋁角總長度計算
- **暗色模式** — 一鍵切換亮/暗主題，適應不同環境光線
- **增量按鈕** — 每個輸入框配有 ± 按鈕，單手快速調整數值
- **即時計算** — 開啟頁面即自動計算，修改參數後點擊「計算」更新結果

---

## 快速開始

### 直接在瀏覽器使用

1. 打開 [GitHub Pages 連結](https://jupiterlaw.github.io/ourdoor_flooring_material_calculator/)（如有啟用）
2. 或直接下載 `index.html` 在瀏覽器開啟

### 本地使用

```bash
# 克隆倉庫
git clone https://github.com/Jupiterlaw/ourdoor_flooring_material_calculator.git

# 直接在瀏覽器打開 index.html
open index.html        # macOS
start index.html       # Windows
xdg-open index.html    # Linux
```

**無需任何依賴、無需構建、無需後端。** 一個 HTML 檔案，打開即用。

---

## 使用說明

1. **輸入空間尺寸**：空間長度 (mm) 與空間闊度 (mm)
2. **輸入地板規格**：地板長度 (mm) 與地板闊度 (mm)
3. **設定等分規則**：最大等分規則 (mm) — 每段不可超過此數值
4. **設定面通參數**：每枝面通長度 (mm)
5. **選擇性功能**：啟用底通 / 鋁角計算（如需要）
6. 按 **「計算」** 按鈕查看結果
7. 按 **「重設」** 清除所有結果

### 計算公式

| 項目 | 公式 |
|------|------|
| 每板等分數 | `ceil(地板長度 / 最大等分規則)` |
| 每段實際長度 | `地板長度 / 每板等分數` |
| 每行需要等分數 | `ceil(空間長度 / 每段長度)` |
| 總行數 | `ceil(空間闊度 / 地板闊度)` |
| 總地板件數 | `ceil(總等分數 / 每板等分數)` |
| 面通行數 | `每行等分數 + 1` |
| 面通總長度 | `面通行數 × 空間闊度` |
| 所需面通支數 | `ceil(面通總長度 / 每枝面通長度)` |

---

## 截圖

| 桌面版 | 手機版 |
|--------|--------|
| *(待添加)* | *(待添加)* |

---

## 瀏覽器支援

| Chrome | Firefox | Safari | Edge | Opera |
|--------|---------|--------|------|-------|
| ✅ 最新 | ✅ 最新 | ✅ 最新 | ✅ 最新 | ✅ 最新 |

亦支援 iOS Safari 及 Android Chrome 等行動瀏覽器。

---

## 開發資訊

### 專案結構

```
ourdoor_flooring_material_calculator/
├── index.html    # 完整計算器（HTML + CSS + JS 單一檔案）
└── README.md     # 本文件
```

### 技術棧

- 純 HTML5 / CSS3 / JavaScript（ES6）
- CSS Custom Properties 設計系統
- 無外部執行時期依賴
- 響應式設計（375px 手機到寬螢幕桌面）

### 設計系統

本計算器是 **Calculator Suite** 的一部分，共享設計語言規範於 [UI-SYSTEM.md](https://github.com/Jupiterlaw/calculator-suite/blob/main/UI-SYSTEM.md)（跨專案文件）。

---

## 相關專案

| 計算器 | 說明 |
|--------|------|
| [Flooring Calculator](https://github.com/Jupiterlaw/flooring-calculator) | 地板材料面積計算器（多區域、損耗率、包裝計算） |
| [Joist Calculator](https://github.com/Jupiterlaw/joist_calculater) | 龍骨佈局計算器（等分分段、位置表、CSV 匯出） |

---

## 授權

本專案採用 MIT 授權條款 — 詳見 LICENSE 檔案（如適用）。

---

## 貢獻

歡迎提交 Issue 或 Pull Request。請參閱 [PR-GUIDELINES.md](https://github.com/Jupiterlaw/calculator-suite/blob/main/PR-GUIDELINES.md) 了解分支命名、提交規範與 PR 流程。