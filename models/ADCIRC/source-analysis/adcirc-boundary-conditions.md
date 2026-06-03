---
title: "ADCIRC 경계조건 — IBTYPE 카탈로그(elevation/land no-flow/island/specified flux/radiation/internal barrier±pipes/weir 64) + normal flux BC + sponge(absorbing) layer"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/boundaries.F (675) + normal_flow_boundary.F90 (106) + sponge_layer.F90 (880) 직접 read — IBTYPE 분류(specifiedFluxBoundaryTypes=(2,12,22,32,52):179, flux 3/13/23·4/24/64·5/25, weir 64), sponge SSIGMA_ETA/MNX/MNY + momentum SPNGCOEF(momentum.F VCOEFXX) file:line 인용. Luettich-Westerink ADCIRC."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — IBTYPE 카탈로그·flux BC·sponge 메커니즘 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
  - models/ADCIRC/source-analysis/adcirc-fort-files-reference.md
---

# ADCIRC 경계조건 — IBTYPE / flux / sponge

> `boundaries.F`(675) + `normal_flow_boundary.F90`(106) + `sponge_layer.F90`(880) 직접 read. ADCIRC fort.14 의 **경계 세그먼트 타입(IBTYPE)** 시스템 + normal flux 적용 + **흡수(sponge) 경계**. open(elevation) 조석 BC 는 [[adcirc-tidal-forcing]] 의 body-force 와 별개의 경계 forcing.

## 1. 두 경계 부류 (boundaries.F)

- **Elevation(open) boundaries** `IBTYPEE`: 조위 지정(fort.15 tidal constituent 또는 fort.19 시계열). `p_nope`/`p_neta` 세그먼트·node 수.
- **Flux/land boundaries** `IBTYPE`: 육지·섬·flux·barrier. `nvell(k)` = 세그먼트별 node 수.

## 2. IBTYPE 카탈로그 (boundaries.F:100-179) ★

| IBTYPE | 종류 | 처리 |
|---|---|---|
| **0 / 10 / 20** | mainland (no normal flow) | 0 free-slip / 10 no-slip / 20 ... tangential 차이 |
| **1 / 11 / 21** | island (no normal flow, 폐곡선) | 〃 |
| **2 / 12 / 22** | **specified normal flux** (+tangential) | `specifiedFluxBoundaryTypes=(2,12,22,32,52)` (:179), fort.15/fort.20 |
| **3 / 13 / 23** | **outward normal flux**(radiation/유출) | 외향 흐름 허용 |
| **30** | radiation (Flather-type) | 유출 radiation |
| **4 / 24** | **internal barrier**(levee, 단방향 overflow) | weir overflow 식, paired node(`ibconnr` dual) |
| **5 / 25** | internal barrier + **cross pipes**(culvert) | 4/24 + flowthrough pipe |
| **64** | **vertical element wall**(submerged weir, SB) | `ISSUBMERGED64`, 양면 flux |
| **52 / 102 / 112 / 122 / 152** | river / special | baroclinic river BC(`totalbcrivernodes`) |

- `+100` 변형(102/112/122) = baroclinic river 등 특수. weir(barrier) node 는 paired(`weir`/`weird` dual node, :611-614) — 양쪽 수위차로 overflow.
- `CSII/SIII` = flux 경계 node 의 법선 cos/sin(접선/법선 분해).

## 3. Normal flux BC (normal_flow_boundary.F90, 106)

specified-flux 경계(IBTYPE 2/12/22/32/52)에서 **법선 flux `QN2`** 를 essential 하게 부과. `VelNorm = -QN2/H`(법선 유속). fort.20(시계열) 또는 fort.15 의 flux per unit width.

## 4. Sponge (absorbing) layer (sponge_layer.F90, 880) ★

외향파를 흡수해 **경계 반사 방지**(DW 구현). damping 계수:
- `SSIGMA_ETA`(absorblayer_sigma_eta) = 수위 감쇠 σ / `SSIGMA_MNX`·`SSIGMA_MNY` = 운동량 x/y 감쇠 σ.
- 경계에서 내부로 갈수록 σ 감소(layer 두께). FEM 으로 `∫σφᵢφⱼ dx` 정확 적분(:70).
- **momentum 결합**: [[adcirc-momentum-implementation]] §3 `VCOEFXX = DTO2*(TKM + SPNGCOEF_X)` — sponge 계수가 friction 처럼 운동량 감쇠 항에 추가(`SPNGCOEF_X/Y`). wind 도 sponge 내 무효(momentum.F:740 `absorblayer_sigma_mnx>1e-9 → WSX=0`).
- 용도: 대양 open boundary 에서 outgoing tide/surge 흡수(유한영역 반사 spurious 제거), tsunami·storm-surge radiation.

## 5. 정리

| 경계 | forcing/처리 | 입력 |
|---|---|---|
| elevation(open) | 조위 지정 | fort.15 tidal / fort.19 |
| specified flux | 법선 flux QN2 | fort.15 / fort.20 |
| radiation(3/30) | 외향 유출 | — |
| land/island(0/1) | no normal flow | fort.14 |
| barrier(4/5/24/64) | weir overflow + pipe | fort.14 barrier height |
| sponge | 흡수 damping | fort.13/15 absorbing layer |

## 6. 연결

- [[adcirc-momentum-implementation]] — sponge SPNGCOEF → VCOEFXX 운동량 감쇠 + wind 무효
- [[adcirc-tidal-forcing]] — elevation open-BC 조석 forcing(body-force 와 구분)
- [[adcirc-fort-files-reference]] — fort.14 boundary segment / fort.15 NOPE·NBOU / fort.19·20 시계열
- Luettich & Westerink ADCIRC users manual (IBTYPE 정의)
