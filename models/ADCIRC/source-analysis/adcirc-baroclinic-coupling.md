---
title: "ADCIRC 2D-baroclinic 결합 (couple2baroclinic3D.F) — 외부 3D 모델 fort.11.nc 의 depth-avg 경압압력경사(BPGX/BPGY)·부력진동수·MLD·internal tide dispersion 시공간 보간 → 2D 운동량"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/couple2baroclinic3D.F (1168) 직접 read — Module Couple2BC3D + Read_BC3D_NetCDF(113, BPGX/BPGY/SigTS/NB/NM/MLD/CDisp/DispX/DispY) + Put_BC3D_on_ADCIRC_Grid(855 공간보간) + Update_BC3D_Info(714 시간보간) + FBPG_Disp_from_BC3D(1012) + 적용(momentum.F:473-477 VIDBCPDXOH) file:line 인용. WJP(Westerink-Pringle?) 개발."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — BC3D 결합 데이터·보간·적용 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-tidal-forcing.md
  - models/ADCIRC/source-analysis/adcirc-nodal-attributes.md
  - models/ADCIRC/source-analysis/adcirc-3d-mode.md
---

# ADCIRC 2D-baroclinic 결합 (couple2baroclinic3D.F)

> `src/couple2baroclinic3D.F`(1168, Module `Couple2BC3D`) 직접 read. **2D barotropic ADCIRC** 가 외부 **3D baroclinic ocean model**(예: HYCOM)의 경압 효과를 받는 결합 — full 3D([[adcirc-3d-mode]]) 없이 baroclinic pressure gradient + internal tide 를 포함. `CBaroclinic` 활성 시 [[adcirc-momentum-implementation]] §1 의 baroclinic pressure 항(momentum.F:473) 공급원.

## 1. 개념 (module 주석 :39-52)

- 외부 3D 모델이 산출한 **depth-averaged 경압 압력경사**(BPGX/BPGY)를 ADCIRC 2D 운동량에 더함 → 2D 모델이 밀도구배 효과(하구 염분쐐기·대양 경압류)를 흉내.
- **good oceanographic practice 주석**(WJP, :41-50): in-situ 밀도/온도 직접 보간은 부정확 → 본래는 Conservative T/S(SA, θ) 를 보간 후 N·ρ 재계산해야. 현 구현은 외부 모델이 미리 계산한 **BPG·N·dispersion 을 직접 read**(공간 절약 위해 2 timestep 만 보관·보간).

## 2. 입력 — fort.11.nc NetCDF (Read_BC3D_NetCDF :113)

`densityFileName`(기본 `fort.11.nc`) 에서 읽는 변수:

| 변수 | 내용 |
|---|---|
| `BPGX`/`BPGY` | depth-averaged 동서/남북 **baroclinic pressure gradient** |
| `SigTS` | 자유표면 sigmat 밀도 |
| `NB`/`NM` | **부력진동수**(buoyancy frequency) bottom / mid-depth |
| `MLD` | mixed layer depth |
| `CDisp`/`DispX`/`DispY` | **internal tide dispersion**(LoadIT_Fric 시) |

- staggered grid 보간계수(XI/YI vs XIc/YIc/YIs) — BPGX 는 u-point, BPGY 는 v-point 격자(:137-139).
- `LoadIT_Fric`(nodalattr, [[adcirc-nodal-attributes]]) + `HBREAK` 연계(:36, :144).

## 3. 보간 (공간 + 시간)

- **공간** `Put_BC3D_on_ADCIRC_Grid`(:855) / `Read_BC3D_NetCDF_on_ADCIRC_Grid`(:479): BC3D lon/lat 정규격자 → ADCIRC unstructured node 보간(`Get_LonLatDepthTime` :174 좌표·보간계수).
- **시간** `Update_BC3D_Info`(:714): **2 timestep 만 메모리 보관**, 그 사이 선형 보간(`densityTimeIterator` skip). `Initial_BC3D_NetCDF`(:627) cold-start 초기화.

## 4. 적용 — momentum (FBPG_Disp_from_BC3D :1012 → momentum.F:473)

```fortran
! momentum.F:474-477 (CBaroclinic)
DBCPDX1A = VIDBCPDXOH(NM1) * AreaIE     ! 정점별 수직적분 baroclinic pressure gradient / H × element 면적
```
- `VIDBCPDXOH` = **V**ertically **I**ntegrated **B**aroclinic **P**ressure gradient / **H** (FBPG_Disp_from_BC3D 가 BPGX·SigTS 등으로 산출) → momentum elemental 항(element 3 node NM1/2/3 평균).
- internal tide dispersion(`DispX/DispY`)도 같은 루틴에서 운동량 항으로 → [[adcirc-tidal-forcing]] §4 internal tide drag 의 외부-3D 공급 버전.

## 5. 위치 — 2D vs 3D

| 방식 | 경압 처리 |
|---|---|
| **2D + BC3D 결합**(본 노트) | 외부 3D 모델의 depth-avg BPG 를 read·보간 (경량, 대양 조석+경압) |
| **full 3D**([[adcirc-3d-mode]]) | ADCIRC 자체 연직 분해(vsmy.F) + 내부 밀도·baroclinic |

→ BC3D 결합 = global tide+surge 모델에 baroclinic/internal-tide 보정을 저비용으로 추가하는 경로(full 3D 비용 회피).

## 6. 연결

- [[adcirc-momentum-implementation]] — VIDBCPDXOH → baroclinic pressure 항(momentum.F:473)
- [[adcirc-tidal-forcing]] — internal tide dispersion(DispX/DispY, CDisp) 외부 공급
- [[adcirc-nodal-attributes]] — LoadIT_Fric·HBREAK internal tide friction 연계
- [[adcirc-3d-mode]] — full 3D 경압(대안)
- 외부 3D ocean model(HYCOM 등) → fort.11.nc BPG/N/dispersion preprocessor
