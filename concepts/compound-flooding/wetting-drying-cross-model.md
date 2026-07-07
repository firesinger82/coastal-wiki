---
title: "침수-노출(wetting & drying) cross-model 대조 — 8개 천수 모델 (임계수심·마스크·hflow·hysteresis·질량보존)"
topic: compound-flooding
canonical_source: self
citation_status: verified
verification_method: "전 행이 각 모델 verified source-analysis 노트로 소급(셀에 노트 링크+file:line). 대표 anchor 직접 재확인(2026-07-07): LISFLOOD-FP fp_acc.cpp:66-68(hflow=max(z+h)−max(z), DepthThresh=1e-3 lisflood.cpp:171). ROMS 는 전용 노트 부재(§5 disclosed). 미커버 셀 §5 표기."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/Delft3D/source-analysis/delft3d_drying_flooding.md
  - models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md
  - models/SWASH/source-analysis/swash-wetting-drying-runup.md
  - models/SFINCS/source-analysis/sfincs_flow_solver.md
  - models/LISFLOOD-FP/source-analysis/lisflood-fp-classic-acc-flow.md
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/FUNWAVE/source-analysis/funwave-physics-sources.md
---

# 침수-노출(wetting & drying) cross-model 대조 (8모델)

> **Canonical source 규칙**: 각 모델 상세는 source-analysis 노트가 진실의 원천 — 본 노트는 대조 축만. cross-model 시리즈 5탄(EOS·transport·[[bottom-friction-cross-model]]·[[vertical-mixing-cross-model]] 후속).
> **왜 compound-flooding 에**: 조위+강우+월파의 복합침수는 육-해 전이대의 마름/젖음 전선을 정확히 옮기는 능력에 결과가 좌우됨 — 침수범위·최대 침수심의 1차 결정자.

## 1. 판정 임계·마스크 방식 대조

| 모델 | 임계수심(기본) | 마스크 방식 | edge wet 판정 | hysteresis | 근거 |
|---|---|---|---|---|---|
| **Delft3D-FLOW** | `Dryflc` 0.05–0.1 / `Drycrt`=0.5·Dryflc / `Dco`~0.1 | 셀(KFS)+face(KFU/KFV) 마스크 | `HU<Drycrt`→KFU=0, KFS=OR(4면) | **있음**(Drycrt<Dryflc) | [[delft3d_drying_flooding]] |
| **ADCIRC** | `H0`(fort.15) / `HABSMIN`=0.8H0 / `HOFF`=1.2H0 | 노드(NODECODE)+요소(NOFF) | 노드 HTOT≤H0→dry, 요소 NCTOT 판정 | **있음**(HABSMIN<HOFF) | [[adcirc-wetting-drying-implementation]] |
| **SWASH** | `epshu`(=epsdry, 적응형 ≤1cm) | face(wetu)+cell(wets) | `hu>epshu`→wetu=1, cell=OR(face) | 없음(대칭) | [[swash-wetting-drying-runup]] |
| **SFINCS** | `huthresh` 0.05(subgrid 시 0 강제) | edge(kfuv)+구조(kcuv) | `max(zs)>max(zb)+huthresh` | 없음 | [[sfincs_flow_solver]] |
| **LISFLOOD-FP** | `DepthThresh` 1e-3 / `MaxHflow` 10 | edge(MaskTest)+DryCheck | **hflow=max(z+h)−max(z)>DepthThresh** | 없음 | [[lisflood-fp-classic-acc-flow]] |
| **XBeach** | 흐름 eps(값 미커버) / 사면 `hswitch` 0.01·`wetslp` 0.15·`dryslp` 1.0 | cell(wetz) | wetz gating(산정식 미커버) | 사면만(wet/dry 안식각) | [[xbeach_flow_solver]]·[[xbeach_avalanching]] |
| **FUNWAVE** | `MinDepth` 0.001/0.01 · `MinDepthFrc` 0.01/0.1 | cell(MASK)+9점(MASK9) | `η<−Depth`→dry | 없음 | [[funwave-physics-sources]] |
| **ROMS** | `Dcrit` 0.10 m | 셀(rmask_wet)+edge(u/v mask_wet, 부호있는 {0,±1,2}) | `ζ+h≤Dcrit`→dry, edge 부호로 방향 | 없음(**one-way flux** 대체) | [[roms_wetting_drying]] |

## 2. ★핵심 통찰 — "hflow = max(수면) − max(바닥)" 공통 정의

**LISFLOOD-FP 와 SFINCS 는 edge wet 판정이 사실상 동형**:
- LISFLOOD: `hflow = max(z0+h0, z1+h1) − max(z0, z1)`, `max(·,0)`, `min(·, MaxHflow)`(fp_acc.cpp:66-68) — 두 셀 중 **높은 수면에서 높은 바닥을 뺀** edge 위 유효 통수심.
- SFINCS: `hu` wet 판정 `max(zs(nm),zs(nmu)) > max(zb)+huthresh`(sfincs_momentum.f90:177-183) — 동일 구조.

이 정의는 **둑/제방(높은 바닥)이 양쪽 수면보다 높으면 자동으로 flux 차단**(hflow=0) — 계단형 지형에서 물리적으로 옳은 월류 게이트. 2D 범람 모델(SFINCS·LISFLOOD)의 표준. cell-center 수심이 아니라 **edge 위 유효 수심**으로 판정하는 게 핵심.

## 3. 마스크 위상 3계열

1. **노드 기반(유한요소)**: ADCIRC `NODECODE`(1/0) — 요소 활성은 wet 노드 수(NCTOT)로. 별도 velocity-point 없음.
2. **셀+face 기반(유한차분/체적)**: Delft3D(KFS/KFU)·SWASH(wets/wetu)·SFINCS(kfuv)·LISFLOOD(MaskTest)·ROMS(rmask_wet/umask_wet) — **face(velocity-point)가 1차 판정 주체, cell 은 face 의 OR**. 보수적 wetting(둘러싼 face 전부 dry 여야 cell dry). ★ROMS 만 edge mask 가 부호 있는 `{0,±1,2}`로 flux 방향 인코딩(다른 모델 0/1) — [[roms_wetting_drying]] §2.
3. **셀+분산게이트**: FUNWAVE MASK(wet/dry) + **MASK9**(9점곱) — MASK9 는 셀과 8이웃 모두 wet 일 때만 1 → **완전 습윤 내부에서만 Boussinesq 분산항 활성, 물가는 자동 NSWE 강등**. 위상해상 모델 특유(SWASH breaking 도 유사: breaking 점을 dry 처리해 비정수압 제외).

## 4. 질량보존·음수수심 방지 대조

| 모델 | 방식 |
|---|---|
| Delft3D | dry 셀 인접 flux(qxk/qyk)=0 + drying 발생 시 SUD 연속식 재반복(adi.f90:422-428) |
| ADCIRC | momentum 에 NODECODE 곱(dry=0), HTOT<HABSMIN 시 ETA 상향 clip, anti-flooding 가드 다수 |
| SWASH | hs<0→s1 보정, hs<−epsdry→epsdry 적응 증가, limiter 전 음수심 시 cycle |
| SFINCS | subgrid 부피역산 z_volume, 음부피 셀 유출차단 q=min(q,0) + uvlim 10 m/s |
| LISFLOOD | Q·dh<0(질량오차)→순수 Bates 재계산, h<0→0 clip, FV1/DG2 zero_discharge |
| FUNWAVE | ★drying 손실질량 Dmass 누적 → **ETA −= Dmass/WetArea** 전역 재분배 |
| XBeach | 아발란치 면적보정 dAfac |

★FUNWAVE 의 Dmass 재분배가 유일한 **전역 질량 되돌림** — 다른 모델은 국소 clip/차단(전역 보존은 flux 0 로 간접 확보).

## 5. ★함정·미커버 (disclosed gaps)

- **hysteresis 있음/없음**: Delft3D·ADCIRC 는 이중임계(젖음>마름)로 채터링 억제 — dry↔wet 반복 진동 방지. SFINCS·LISFLOOD·SWASH·FUNWAVE 는 단일임계(대칭). ROMS 는 이중임계 대신 **one-way flux(유입만 허용)+fast-step 평균 이진화**로 채터링 관리([[roms_wetting_drying]] §3-4). 채터링은 단일임계 모델에서 Δt·limiter 로 관리.
- **ADCIRC 비율 하드코딩**: HABSMIN=0.8H0·HOFF=1.2H0 고정 — 조정하려면 H0 자체 변경. 수심 5m clamp 제거 메시는 H0=0.1 필수(안 하면 천해 영구 dry).
- **재습윤 게이트 강도차**: ADCIRC 가 가장 엄격(2 wet 이웃 + HOFF + VELMIN 동시) — 고립 dry 노드 self-activate 불가. SFINCS/LISFLOOD/SWASH 는 임계 회복 즉시 재습윤.
- **미커버(위키 갭)**: XBeach 흐름 solver eps 값·wetz 산정식 수치 미기재(사면 wetslp/dryslp 만 완비). LISFLOOD `tol_h` 노트 미명시(DepthThresh·thin_depth 만). (ROMS 는 [[roms_wetting_drying]] 신설로 해소 — 8모델 전원 커버.)

## 6. 관련

- [[delft3d_drying_flooding]]·[[adcirc-wetting-drying-implementation]]·[[swash-wetting-drying-runup]]·[[sfincs_flow_solver]]·[[lisflood-fp-classic-acc-flow]]·[[xbeach_flow_solver]]·[[funwave-physics-sources]] — 모델별 canonical
- [[bottom-friction-cross-model]]·[[vertical-mixing-cross-model]] — cross-model 시리즈
- `concepts/compound-flooding/01-concept.md` — 복합침수 개념(본 노트가 전이대 수치처리 심화)
