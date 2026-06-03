---
title: "XBeach tide & 외력 입력(compute_tide_zs0.F90 + readtide/readwind/rainfall.F90) — 조위 zs0 초기화·경계보간(corner→edge) + wind/rainfall 시계열 reader"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/compute_tide_zs0.F90 (649) + readtide.F90(94) + readwind.F90(112) + rainfall.F90(104) 직접 read — tide_init/tide_boundary_timestep/timeinterp_tide/boundaryinterp_tide(corner→edge)/fill_tide_grid file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — tide 보간·외력 reader verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_boundary_conditions.md
  - models/XBeach/source-analysis/xbeach_groundwater.md
---

# XBeach tide & 외력 입력 (compute_tide / readtide / readwind / rainfall)

> `compute_tide_zs0.F90`(649) + `readtide/readwind/rainfall.F90` 직접 read. **조위(tide) zs0 와 wind·rainfall 외력** 입력·보간. [[xbeach_flow_boundary_conditions]] 의 flow_bc 가 매 step 호출하는 tide 갱신.

## 1. Tide (compute_tide_zs0.F90, module compute_tide_module)

조위는 **모델 4 corner point** 의 시계열로 주어지고, 경계·domain 으로 보간:
| 루틴 | 역할 |
|---|---|
| `tide_init`(:49) | xmaster 가 전 격자 tide 초기화 |
| `tide_boundary_timestep` | 매 step 경계 zs0 갱신(all process) |
| `timeinterp_tide`(private) | tide 시계열 → 현재 시각 보간 |
| `boundaryinterp_tide`(private) | 4 corner → 경계 edge 따라 보간 |
| `boundaryinterp_tide_complex` | 복잡 경계(interpolation·split·MPI) |
| `fill_tide_grid`(private) | 초기장 zs0 채움(corner+boundary 생성값) |

- corner 거리 가중(`ndistcorners/sdistcorners`)으로 경계 edge 보간. tidetype(instant/velocity/hybrid, [[xbeach_flow_boundary_conditions]])에 따라 적용.
- `zs0` = still water level(조위+surge) → flow_init 수위·flow_bc 경계.

## 2. Wind (readwind.F90, 112)

wind 시계열(`wind.txt`: t, windv, windth) 읽기 → 시변 wind 속도/방향. [[xbeach_flow_solver]] 의 wind stress(WSX/WSY) + [[xbeach_wave_breaking]]/wind growth 입력. (XBeach 는 주로 wave-driven; wind 은 보조.)

## 3. Rainfall (rainfall.F90, 104)

강우 시계열 → 수위 source(질량 추가). [[xbeach_groundwater]] infiltration 과 연계(육상 침투/지표류). 소규모 모듈.

## 4. 연결

- [[xbeach_flow_boundary_conditions]] — flow_bc 가 tide_boundary_timestep 호출, tidetype 적용
- [[xbeach_flow_solver]] — wind stress / rainfall source
- [[xbeach_groundwater]] — rainfall infiltration
