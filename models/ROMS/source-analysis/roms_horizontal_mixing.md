---
title: "ROMS 수평 혼합(hmixing.F) — grid·deformation 의존 harmonic/biharmonic viscosity·diffusivity: Smagorinsky 1963 + Griffies-Hallberg 2000 biharmonic + vegetation 효과"
topic: roms
canonical_source: self
citation_status: verified
verification_method: "models/ROMS/raw/source_code/roms/ROMS/Nonlinear/hmixing.F (835) 직접 read — Smagorinsky 1963(19) + Griffies-Hallberg 2000 biharmonic(31-32) + hmixing_tile Hviscosity(117/195) + vegetation 효과(82) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — 수평 혼합 Smagorinsky/Griffies-Hallberg verbatim"
verification_date: 2026-06-04
related:
  - models/ROMS/source-analysis/roms_advection.md
  - models/ROMS/source-analysis/roms_vertical_mixing.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
---

# ROMS 수평 혼합 (hmixing.F)

> `hmixing.F`(835) 직접 read. ROMS 의 **수평 eddy viscosity·diffusivity 계수**를 흐름 변형률(deformation)·격자로부터 동적 산출(연직 혼합 [[roms_vertical_mixing]] 와 별개). 운동량·tracer 의 수평 확산항(visc2/visc4·diff2/diff4)에 들어감.

## 1. Smagorinsky (hmixing.F:19) ★

**Smagorinsky 1963** — 변형률 기반 subgrid viscosity:
```
A_M = C·Δx·Δy·|D|,   |D| = √((∂u/∂x−∂v/∂y)² + (∂v/∂x+∂u/∂y)²)
```
- 흐름 deformation(전단·신장)이 큰 곳(front·eddy)에서 viscosity↑ → 수치 안정 + 물리적 혼합. 격자크기(Δx·Δy) 의존. harmonic(2차, visc2).

## 2. Griffies-Hallberg 2000 — biharmonic (hmixing.F:31-32)

**Griffies & Hallberg 2000**: biharmonic(4차, visc4) **Smagorinsky-like** viscosity — 대규모 모델에서 scale-selective(작은 scale 만 강하게 감쇠, 큰 scale 보존). harmonic 보다 less diffusive(eddy 보존). `VISC_GRID`/`DIFF_GRID` 옵션.

## 3. 옵션·적용

- **harmonic vs biharmonic**: `UV_VIS2/TS_DIF2`(harmonic 2차) vs `UV_VIS4/TS_DIF4`(biharmonic 4차). 상수 또는 grid/deformation-dependent(Smagorinsky `VISC_GRID`).
- **rotated mixing**: isopycnal/geopotential 회전(가짜 대각혼합 억제). 
- **vegetation**(:82): 식생이 수평 viscosity 증가(canopy drag 난류).
- 산출 `Hviscosity`(:117) → [[roms_baroclinic_3d]] step3d_uv 운동량 + tracer 수평 확산.

## 4. 위치

- 수평 혼합 = 수치 안정(advection [[roms_advection]] 의 수치확산 보완) + 물리(meso-scale eddy 혼합). 연직([[roms_vertical_mixing]] GLS/KPP)과 독립.
- biharmonic 이 현대 high-res 모델 표준(eddy-permitting).

## 5. 연결

- [[roms_advection]] — 수평 확산이 advection 수치확산 보완
- [[roms_vertical_mixing]] — 연직 혼합(독립)
- [[roms_baroclinic_3d]] — Hviscosity → 운동량/tracer 수평 확산
- Smagorinsky 1963 / Griffies-Hallberg 2000
