---
title: "ADCIRC nodal attributes (fort.13) — 공간변화 파라미터 시스템: bottom friction(Manning/Chezy/quadratic→Cd) + tau0 primitive weighting + directional wind roughness + canopy + bridge pilings + internal tide drag + startdry/geoid offset"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F (3193) 직접 read — attribute CASE 카탈로그(636-686) + Apply2DBottomFriction(2271, Manning→Cd FRIC=g·n²/H^(1/3)) + CalculateTimeVaryingTau0(2117) + Apply2DInternalWaveDrag(2516) + ApplyDirectionalWindReduction(2804) + ApplyCanopyCoefficient(2922) file:line 인용. Luettich-Westerink ADCIRC."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — fort.13 attribute 카탈로그·friction 변환·apply 루틴 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
---

# ADCIRC nodal attributes (fort.13) 시스템

> `src/nodalattr.F`(3193) 직접 read. ADCIRC 의 **공간변화 파라미터**(fort.13) 시스템 — bottom friction·tau0·wind roughness·canopy·internal tide 등을 node별로 지정. [[adcirc-momentum-implementation]] 의 `FRIC`(bottom friction 계수)·[[adcirc-gwce-implementation]] 의 tau0·[[adcirc-tidal-forcing]] 의 internal tide drag 의 **입력 소스**. fort.15 의 `NWP` + fort.13 파일.

## 1. Attribute 카탈로그 (nodalattr.F:636-686)

fort.13 가 지원하는 nodal attribute (이름 = fort.13 키워드):

| attribute | 역할 | apply |
|---|---|---|
| `primitive_weighting_in_continuity_equation` | **tau0** (GWCE 가중) | CalculateTimeVaryingTau0 |
| `quadratic_friction_coefficient_at_sea_floor` | Cd (quadratic) | Apply2DBottomFriction |
| `mannings_n_at_sea_floor` | **Manning n → Cd** | 〃 (§3) |
| `chezy_friction_coefficient_at_sea_floor` | Chezy C → Cd | 〃 |
| `bottom_roughness_length` | z₀ (log-law) | 〃 |
| `bridge_pilings_friction_parameters` | 교각 항력(BK/BALPHA/BDELX) | 〃 (FricBP) |
| `surface_directional_effective_roughness_length` | **방향별 wind 감쇠**(12 sector) | ApplyDirectionalWindReduction |
| `surface_canopy_coefficient` | 식생 canopy(wind 0/1) | ApplyCanopyCoefficient |
| `surface_submergence_state` | **startdry**(초기 건조) | wetting-drying |
| `sea_surface_height_above_geoid` | datum offset(평균해면-geoid) | barotropic |
| `wave_refraction_in_swan` | SWAN 굴절 토글 | SWAN 결합 |
| `advection_state` | advection 국소 on/off | momentum |
| `elemental_slope_limiter` | DG slope limiter | [[adcirc-dg-continuity-solver]] |
| `initial_river_elevation` | 하천 초기수위 | cold start |
| `overland_reduction_factor` | 육상 흐름 감소 | overland |
| `condensed_nodes` | 노드 병합 | mesh |
| (internal tide) | **internal tide friction** | Apply2DInternalWaveDrag |

- 읽기: XDMF(`readNodalAttrXDMF` :552) 또는 legacy fort.13. 각 attr = {units, number_of_values, default_values, per-node 값}. default 로 채우고 지정 node 만 override.

## 2. Bottom friction 적용 (Apply2DBottomFriction, :2271)

여러 friction attribute 를 단일 `FRIC` 계수로 통합 → [[adcirc-momentum-implementation]] §4 의 `TK = FRIC·(...)` 입력.

## 3. Manning's n → Cd 변환 (:2316-2365) ★

```fortran
IF (LoadManningsN) FRIC(I) = g*ManningsN(I)**2 / (DP(I)+IFNLFA*ETA2(I))**(1/3)   ! Cd = g·n²/H^(1/3)
IF (FRIC(I) < BFCdLLimit) FRIC(I) = BFCdLLimit                                    ! 하한
```
- **Manning → 무차원 항력계수** `C_d = g·n²/H^{1/3}` (Manning-Strickler). `H = DP + IFNLFA·ETA2`(비선형 finite-amp 수심).
- `BFCdLLimit` = quadratic friction 하한(깊은 물 과소 friction 방지). Chezy: `C_d = g/C²`, bottom roughness: log-law z₀.
- **VEW1D channel** wet-perimeter 보정(WPFac = (1+2H/W)^{2/3}, :2339) + subgrid barrier overtopping friction(:2346).
- → FRIC 가 momentum `TK = FRIC·(IFLINBF + |U|/H·(...))` 로 매 step bed shear 산출.

## 4. tau0 — time-varying primitive weighting (CalculateTimeVaryingTau0, :2117)

GWCE 의 `τ₀`(numerical weighting between primitive continuity ↔ wave equation). attribute 로 node별 지정 또는 **time-varying**(수심·유속 기반 자동) — 천해 large τ₀(primitive 우세, mass 보존), 심해 small τ₀(wave eq). [[adcirc-gwce-implementation]] §A GWCE 행렬의 핵심 계수.

## 5. Wind roughness·canopy

- **ApplyDirectionalWindReduction** (:2804): `surface_directional_effective_roughness_length` = 12 방위(30°) sector별 유효 roughness → 풍향에 따라 wind drag 감쇠(육상 식생·건물 조도). land-falling hurricane 의 육상 wind 감소 핵심.
- **ApplyCanopyCoefficient** (:2922): `surface_canopy_coefficient` = 0 이면 canopy 아래 wind stress 차단(밀림·습지 식생).

## 6. Internal tide drag (Apply2DInternalWaveDrag, :2516)

[[adcirc-tidal-forcing]] §4 의 internal tide wave drag 적용 루틴(여기 nodalattr.F 에 실제 코드, internaltide.F90 은 보조). 시간평균 유속 × drag tensor `TKM` → 운동량 sink (deep-ocean 성층 조석 소산).

## 7. 연결

- [[adcirc-momentum-implementation]] — FRIC → bottom friction TK (§4); directional wind·canopy → wind stress; advection_state
- [[adcirc-gwce-implementation]] — tau0 primitive weighting
- [[adcirc-tidal-forcing]] — internal tide wave drag(Apply2DInternalWaveDrag)
- [[adcirc-wetting-drying-implementation]] — startdry(surface_submergence_state)
- fort.13(nodal attributes) + fort.15 NWP — 입력 형식([[adcirc-fort-files-reference]])
