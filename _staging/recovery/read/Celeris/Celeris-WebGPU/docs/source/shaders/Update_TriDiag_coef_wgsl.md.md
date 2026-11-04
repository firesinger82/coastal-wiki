---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Update_TriDiag_coef_wgsl.md
lines: 26
sha256: c11577384f3f0f5600ae46a2ae28f63175ca9db5fdf0c52d78995274b181bc1d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Update_TriDiag_coef_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Update_TriDiag_coef.wgsl`

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 원문 링크·설명이다(1–3). 표준 Boussinesq x/y 암시 계수를 만든다(1–7). `coefMatx`·`coefMaty`의 `r/g/b/a`는 하대각/대각/상대각/unused·우변 placeholder다(11–16). 경계·near-dry 항등형은 `a = 0`, `b = 1`, `c = 0`이다(18). |
| 20–26 | 습윤 내부는 국소 수심·이웃 수심 경사·`Bcoef`·격자 간격으로 계수를 만들고 PCR이 `current_stateUVstar` 우변과 결합한다(22). 이 파일에도 COULWAVE 분기가 있으나 별도 `Update_TriDiag_coef_COULWAVE.wgsl`은 다른 우변 계약이므로 `main.js` 선택을 확인해야 한다(26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16: 문서는 표준 계수 alpha를 unused/right-hand-side placeholder로 표시한다.
- 26: 문서는 표준 파일 안 COULWAVE 분기와 별도 COULWAVE 파일의 우변 계약 차이를 적는다.
