---
title: "Delft3D-FLOW online sediment/morphology 커널 — compute_sediment 패키지 (erosed·bott3d)"
model: Delft3D
component: flow2d3d_kernel/compute_sediment
canonical_source: self
citation_status: verified
verification_method: "Delft3D structured FLOW(flow2d3d) 커널 소스 직접 read (models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute_sediment/). erosed.f90(1513줄)·bott3d.f90(1311줄) Function 주석 + 계산 흐름(call 라인) 직접 인용. 패키지 21파일 wc -l + Function 블록 직접 인용. canonical 알고리즘 reference = Lesser et al. 2004 Coastal Engineering 51:883-915 (publicly-known, web-refs/delft3d-official-resources §3.1)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - models/Delft3D/web-refs/delft3d-official-resources.md
  - models/Delft3D/source-analysis/delft3d_dredge_dump.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - concepts/sediment-transport/04-code-and-tools.md
---

# Delft3D-FLOW online sediment/morphology 커널

> Delft3D 의 간판 기능인 **online morphology**(hydrodynamics ↔ sediment ↔ bed 동시 결합)의 structured-grid(flow2d3d) 커널. canonical 알고리즘 = **Lesser et al. 2004** (`web-refs §3.1`). 경로: `src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute_sediment/`. (D-Flow FM 의 unstructured 버전은 별도 — [`delft3d_dflowfm_overview.md`](delft3d_dflowfm_overview.md))

## 1. 패키지 구성 (compute_sediment 21 파일)

| 파일 | 줄 | 역할 |
|---|---|---|
| `erosed.f90` | 1513 | **σ-model 침식/퇴적 + bedload + 부유확산 source/sink 계산** (핵심) |
| `z_erosed.f90` | 1510 | 위의 **Z-model**(고정수평층) 대응 |
| `bott3d.f90` | 1311 | **bed update** (BODSED 변화 = Exner) + 부유 transport 보정 + mixing layer |
| `z_bott3d.f90` | 1293 | bott3d 의 Z-model 대응 |
| `adjust_bedload.f90` | 531 | bedload 의 bed-slope·경계 보정 |
| `z_dwnvel.f90` / `dwnvel.f90` | 447 / 266 | near-bed 유속 성분(zeta 점) 계산 |
| `morstatistics.f90` | 222 | morphological 통계(시간평균 등) |
| `red_soursin.f90` (+z_) | 196 / 213 | **source/sink 감쇠** — 과대 bed level 변화 방지(안정화) |
| `upwbed.f90` | 189 | bedload cell중심 → 유속점 (upwind/central) |
| `avalan.f90` | 177 | **avalanching** (bed slope 한계 초과 시 사면붕괴 재분배) |
| `bndmorlyr.f90` | 153 | bed composition 경계조건 |
| `dredge_d3d4.f90` (+init/comm) | 146 | 준설/투기 ([`delft3d_dredge_dump.md`](delft3d_dredge_dump.md) 연계) |
| `d3d4_flocculate.f90` | 140 | mud **flocculation**(응집) |
| `compthick.f90` | 123 | transport + exchange(mixing) layer 두께 갱신 |
| `shearx.f90` | 105 | bed shear 저장 |
| `updwaqflxsed.f90` / `upbdps.f90` / `inised.f90` | 88 / 75 / — | WAQ flux 갱신 · bed datum · 초기화 |

핵심 use 모듈: `bedcomposition_module`(bed 층 조성) · `morphology_data_module` · `sediment_basics_module` · `compbsskin_module`(skin friction) · `m_sand_mud`(sand-mud 상호작용) — `erosed.f90:70-71`.

## 2. erosed.f90 — source/sink 계산 (Partheniades-Krone + bedload)

Function 주석 (`erosed.f90:46-58`): bed 에서의 sediment flux 를 **Partheniades-Krone formulation** 으로 계산, `SOURSE`/`SINKSE` 채워 `SOUR`/`SINK` 에 가산. sand 의 **bed load transport**(`SBUU`/`SBVV`) + 연직 **sediment diffusion**(`SEDDIF`) + sand bed-load 의 **wave asymmetry** + U/V 점 **bed slope** 효과 포함.

### 2.1 전처리 흐름 (시간스텝 시작부)

| 단계 | 라인 | 내용 |
|---|---|---|
| MORFAC 갱신 | `:554` `call updmorfac` | morphological acceleration factor(형태가속계수) 시간 갱신 |
| bed shear | `:562` `call shearx` | `taubmx` → `gdp%gdscour` 저장 |
| mud 층 두께 | `:569` `call detthcmud` | skin friction 용 (**Soulsby 2004**, `:566` 주석) |
| 배열 reset | `:583-608` | `sinkse`/`sourse`/`seddif`/bedload `sbcu..` 0 초기화 |
| top-layer 조성 | `:633` `call getfrac` | 표층 sediment fraction(`frac`, `anymud`) |
| near-bed 유속 | `:640` `call dwnvel` | zeta 점 유속 성분·크기 |
| fixfac | `:653` `call getfixfac` | bed sediment 두께 부족 시 **erosion 감쇠계수**(공급제한) |
| SRCMAX | `:666` 주석 | cohesive 전용 erosion flux 상한 (THRESH≤0 → ffthresh=1e-10 로 사실상 무제한) |

### 2.2 nm 루프 — cohesive vs non-cohesive 분기

**Skin friction** (`:880` `call compbsskin`): mean 유속·파(uorb, tp) 로 bed skin shear 계산, fluff 분율 `afluff`(`:876` `get_alpha_fluff`, `iflufflyr` 1/2) 반영.

- **Cohesive (mud)** — `:1074` `call erosilt`:
  - Partheniades-Krone 침식/퇴적 → `sinktot`, `sourse(nm,l)`, `sourfluff`.
  - **Fluff layer**(`iflufflyr>0`): `iflufflyr==2` → `sinkse = sinktot*depfac` (`:1087`), `iflufflyr==1` → `sinkse=0`(`:1090`); fluff source 는 가용질량 한계 `min(sourfluff, mfltot/dt)`(`:1098`). fluff 미사용 시 `sinkse=sinktot`(`:1101`).
  - 총 fluff 질량 `mfltot`(`:1019-1024`)로 분율 `fracf`(`:1068`).

- **Non-cohesive (sand)** — `:1221` / `:1304` `call eqtran`:
  - sediment transport formula(van Rijn 등 `gdp%gdtrapar`) 호출 → 기준농도 `aks`, `sourse`/`sour_im`/`sinkse`(`:1264-1265`, 2D 변형 `:1335`).
  - `suspfrac`(`:324`) = 부유분이 advection-diffusion 식으로 수송되는지 여부.
  - bedload `sbcu/sbcv`(cell center) → 이후 `upwbed`/`adjust_bedload` 로 유속점·bed slope 보정.

→ `SOUR`/`SINK` 는 FLOW 의 부유사 농도 transport 식(`difu`)에 전달되어 수주 농도 진화. bed flux 는 `bott3d` 가 받음.

## 3. bott3d.f90 — bed update (Exner)

Function 주석 (`bott3d.f90` Function): (a) sand 부유사 transport **보정 벡터** 계산, (b) 출력용 **depth-integrated** 부유 transport, (c) **EROSED 의 source/sink + 신농도로 BODSED**(bed 질량) 변화 계산 = **Exner 형 bed level 갱신**, (d) BODSED 변화 기반 **새 mixing layer 두께** 산정.

→ `compthick.f90`(transport+exchange layer 두께) + `bedcomposition_module`(다층 bed 조성) 와 결합해 morphological 층 진화. **MORFAC** 로 형태변화를 hydrodynamic 대비 가속(장기 morphodynamic).

## 4. 안정화·bed-slope 보조

- **`red_soursin.f90`**(196): source/sink 를 줄여 **과대 bed level 변화 방지**(한 스텝 erosion 이 가용 sediment 초과하지 않도록) — morphodynamic 안정성 핵심.
- **`avalan.f90`**(177): bed slope 가 한계(repose angle)를 넘으면 **사면붕괴(avalanching)** 재분배.
- **`adjust_bedload.f90`**(531): bedload 의 bed-slope(상향/하향 경사) 보정 + 경계 처리. bed slope 효과(`erosed` Function `:56`).
- **`upwbed.f90`**(189): bedload rate 를 cell 중심 → 유속점으로 upwind/central 이송.

## 5. Z-model 대응 + sand-mud

- σ-model(`erosed`/`bott3d`) ↔ **Z-model**(`z_erosed`/`z_bott3d`/`z_dwnvel`/`z_red_soursin`) 쌍 — 연직격자 방식별 ([`delft3d_sigma_z.md`](delft3d_sigma_z.md)).
- **sand-mud 상호작용**(`m_sand_mud` 모듈, `erosed.f90:71`) + **flocculation**(`d3d4_flocculate.f90`) — 혼합 sediment 거동.

## 6. 본 위키 접점

- [`web-refs/delft3d-official-resources.md §3.1`](../web-refs/delft3d-official-resources.md) — **Lesser et al. 2004** (이 커널의 canonical 알고리즘 paper) + §3.4 van der Wegen 2008 장기 morphology.
- [`concepts/sediment-transport/04-code-and-tools.md §3`](../../../concepts/sediment-transport/04-code-and-tools.md) — Delft3D-SED + §10.1 copula 민감도(Delft3D-WAQ, 1804.04541)·Green-Naghdi DG.
- [`delft3d_dredge_dump.md`](delft3d_dredge_dump.md) — `dredge_d3d4.f90` (동일 패키지 내 준설/투기).
- EFDC SED([`models/EFDC/source-analysis/sediment/`](../../EFDC/source-analysis/)) 와 대비: EFDC SEDZLJ vs Delft3D Partheniades-Krone(mud) + eqtran(sand).

## 7. 미보강 (verified 확장 TODO)

- `erosilt`(Partheniades-Krone 식 본체) + `eqtran`(transport formula dispatch) 소스는 별도 패키지 — 식 verbatim 추출 시 후속 노트.
- van Rijn 1993/2007 vs Engelund-Hansen 등 transport formula 선택(`gdp%gdtrapar`) 카탈로그.
- `bedcomposition_module` 다층 bed 조성 알고리즘(graded sediment) deep.
- MORFAC(형태가속) 안정성·정확도 trade-off 정량.
