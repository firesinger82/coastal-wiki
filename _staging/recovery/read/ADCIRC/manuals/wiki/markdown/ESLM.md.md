---
file: models/ADCIRC/raw/manuals/wiki/markdown/ESLM.md
lines: 13
sha256: 5c66cb1e5faba6c03f7ca2db39afb38f8b5c1d76fb6a8de698740b4fa743d8a9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ESLM.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 제목·판본 표기·빈 줄을 포함한다(1–4). ESLM — `fort.15`에서 수평 와점성(horizontal eddy viscosity)을 설정하는 매개변수이다(5). 원문: `ESLM is a parameter in the [fort.15 file](/Fort.15_file) to set the [horizontal eddy viscosity](/Horizontal_eddy_viscosity).` (5). |
| 7–10 | Usage Notes — 양수일 때 공간적으로 일정한 수평 와점성을 지정한다(9). 음수일 때 Smagorinsky 난류 폐쇄(turbulence closure)를 사용하며 공간적으로 일정한 계수는 `ESLM`의 절댓값이다(9). 적용 조건과 차원은 원문을 옮긴다. 원문: ``A positive `ESLM` indicates a spatially constant [horizontal eddy viscosity](/Horizontal_eddy_viscosity) with dimensions [L²/T]. A negative value of `ESLM` invokes the [Smagorinsky-type](https://en.wikipedia.org/wiki/Turbulence_modeling#Smagorinsky_model_for_the_sub-grid_scale_eddy_viscosity) turbulence closure model[&#91;1&#93;](#cite_note-smag1-1) using a spatially constant coefficient equal to the absolute value of `ESLM`. Users should refer to the [horizontal eddy viscosity](/Horizontal_eddy_viscosity) section for more information.`` (9). |
| 11–13 | References — Smagorinsky(1963)의 논문과 DOI 링크를 제공한다(11–13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 9: 양수와 음수의 적용 조건은 있으나 `ESLM = 0`일 때의 동작은 이 파일에 없다.
