# 戶外木地板材料計算器 · Outdoor Wood Flooring Calculator

戶外木地板施工估算工具：依最大等分規則計算地板分段、總板數、面積對比，並估算面通、底通與鋁角用量。

An outdoor wood-flooring estimator: computes board segmentation, total board count, and area comparison, plus batten (面通), bottom batten (底通), and aluminum angle (鋁角) quantities.

## 使用方法 · How to use
1. 輸入空間長度 / 闊度、地板長度 / 闊度（毫米）。
2. 設定「最大等分規則」（每段不可超過此長度）與「每枝面通長度」。
3. 視需要勾選「啟用底通」「啟用鋁角」，並填寫鋁角高度。
4. 按「計算」；各維度輸入旁有 +/− 微調按鈕，便於單手操作。
5. 可切換淺色 / 深色主題。

1. Enter space length / width and board length / width (mm).
2. Set the max segment length and batten length per piece.
3. Optionally enable bottom batten and aluminum angle; enter aluminum height.
4. Press 計算 (Calculate). Use the +/− steppers for one-handed entry.
5. Toggle light / dark theme.

## 計算公式 · Formula
- 每板等分數 = ⌈地板長度 ÷ 最大等分規則⌉
- 每行等分數 = ⌈空間長度 ÷ 每段實際長度⌉
- 總行數 = ⌈空間闊度 ÷ 地板闊度⌉
- 總地板件數 = ⌈總等分數 ÷ 每板等分數⌉
- 面通行數 = 每行等分數 + 1
- 面通總長度 = 面通行數 × 空間闊度
- 所需面通支數 = ⌈面通總長度 ÷ 每枝面通長度⌉

## 特性 · Notes
- 手機優先（375px），系統字型，高對比，戶外強光可讀。
- 純單一 `index.html`，無外部依賴、無建置步驟。
- 支援淺色 / 深色主題切換。

## 本套件成員 · Part of the Jupiterlaw calculator suite
- [flooring-calculator](https://github.com/Jupiterlaw/flooring-calculator) — 地板材料
- [ourdoor_flooring_material_calculator](https://github.com/Jupiterlaw/ourdoor_flooring_material_calculator) — 本工具（戶外木地板 + 面通/底通/鋁角）
- [joist_calculater](https://github.com/Jupiterlaw/joist_calculater) — 龍骨（joist）佈局位置

© Jupiter's Design Limited
