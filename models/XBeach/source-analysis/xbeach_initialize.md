---
title: "XBeach 초기화(initialize.F90) — grid_bathy(격자·수심) + wave_init/flow_init/sed_init/discharge_init + hotstart_init + drifter_init. 배열 할당·초기장 설정"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/initialize.F90 (1855) 직접 read — public setbathy_init/grid_bathy/drifter_init/wave_init/sed_init/flow_init/discharge_init/hotstart_init_1·2(5), grid_bathy 배열 allocate(59-69) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 초기화 루틴 인벤토리 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/XBeach/source-analysis/xbeach-bathymetry-input-foundation.md
---

# XBeach 초기화 (initialize.F90)

> `initialize.F90`(1855) 직접 read. simulation 시작 시 **격자·수심·상태배열 할당 및 초기장 설정**(module `initialize_module`). main 흐름: params 읽기 → `grid_bathy` → `*_init` 각 서브시스템.

## 1. 초기화 루틴 (public)

| 루틴 | 역할 |
|---|---|
| `grid_bathy` | 격자(x/y/xz/xu/xv) + bathymetry(zb/zb0/dzbdx) 배열 allocate·읽기(:59-69) |
| `setbathy_init` | bathymetry update(time-varying depth) 초기화 |
| `wave_init` | 파 상태(ee/rr/H/theta/sigt) 초기화 |
| `flow_init` | 흐름(uu/vv/zs/hh) 초기화 |
| `sed_init` | sediment(농도·bed composition) 초기화 |
| `discharge_init` | discharge BC 초기화 |
| `drifter_init` | Lagrangian drifter 초기화 |
| `hotstart_init_1/2` | hotstart(restart) 복원 |

## 2. grid_bathy

- 격자 좌표(`x/y` corner, `xz/yz` cell-center, `xu/yu`/`xv/yv` u·v-point) + metric. 1D/2D/curvilinear.
- bathymetry `zb`(+`zb0` 초기 보존, morphology 비교용), 경사 `dzbdx/dzbdy`([[xbeach_morphology]] avalanching·bed-slope). 입력은 [[xbeach-bathymetry-input-foundation]].

## 3. 서브시스템 초기화

- **wave_init**: ee(파에너지)=0 또는 boundary, sigt(상대 frequency), theta(방향 격자 ntheta).
- **flow_init**: zs(수위)=zs0(tide), uu/vv=0, hh(수심)=max(zs−zb, 0).
- **sed_init**: 다층 bed composition(grain fraction), 초기 농도.
- **hotstart**: 이전 run 의 상태 netCDF 복원(restart).

## 4. 연결

- [[xbeach_flow_solver]] / [[xbeach_wave_action_balance]] / [[xbeach_morphology]] — 초기화하는 상태배열의 solver
- [[xbeach-bathymetry-input-foundation]] — bathymetry 입력 형식
- params.F90 — 파라미터 읽기(초기화 선행)
