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
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "강우 단위 변환·시각 보간·연속식 소비와 지하수 계산 순서를 결속"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: 강우 단위 변환·시각 보간·연속식 소비와 지하수 계산 순서를 결속. 기존 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인이 아니다. [원문 구간·SHA와 연결 판정](../../../_staging/total-read/model-audit/XBeach/connectivity/runtime-20260912/evidence.json)을 따르며 원본 솔버는 수정하지 않았다.

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

## 3. Rainfall의 단위와 소비 시점

`rainfall_init`은 `xmaster`에서 실행하며, 상수 입력과 파일의 강우율을 **mm/hr에서 m/s로 변환**한다 (`/1000/3600`). 파일 입력은 시각 0으로 초기 보간하고, 강우가 꺼져 있으면 `rainfallrate=0`으로 초기화한다. (`rainfall.F90:22-70`; 초기 호출 `libxbeach.F90:177`)

`flow`는 수평 유량 경계를 적용한 뒤 `rainfall==1`이면 `rainfall_update`를 호출한다. 시계열 경로는 현재 `par%t`로 보간하며, 이어지는 1D/2D 연속식 모두 `-infil + rainfallrate`를 사용한다. (`rainfall.F90:92-100`; `flow_timestep.F90:724-751`)

MPI에서 `constantRainfall` 방송은 `t<=dt` 조건을 가진다 (`rainfall.F90:86-90`). 지하수의 `gwflow`는 이 강우 갱신과 `flow`보다 먼저 호출되므로, 여기서 갱신한 강우를 같은 스텝의 앞선 침투 계산에 직접 넘긴다고 해석하지 않는다. 강우는 우선 연속식의 표면수 공급항이다. (`libxbeach.F90:304-307`; [[xbeach-coupled-physics-contracts]])

## 4. 연결

- [[xbeach_flow_boundary_conditions]] — flow_bc 가 tide_boundary_timestep 호출, tidetype 적용
- [[xbeach_flow_solver]] — wind stress / rainfall source
- [[xbeach_groundwater]] — 연속식이 함께 소비하는 `infil` 계산
