---
title: "표사이동 — 06 모델 적용 (EFDC SED · Delft3D-SED · XBeach · ROMS)"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable source-code 직접 분석 (codex 보조, models/EFDC/source-analysis/sediment/ 의 efdc_sediment.md 인용) — SedTran-Original (ISTRAN(6,7) cohesive/noncohesive) vs SEDZLJ unified bed model 구분, Krone-Partheniades, Van Rijn, Christoffersen-Jonsson wave-current shear. Delft3D/XBeach/ROMS source-analysis 도 본 위키 promote 완료 (models/<MODEL>/source-analysis/sediment/). CONVENTIONS.md §3 canonical source 분리 — 본 페이지는 요약 + 링크."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21 → 2026-05-23 (보강·verified)
verification_by: "Claude Opus 4.7 (1M context) — EFDC SED source-code + 4 모델 promote 완료 cross-ref"
verification_date: 2026-05-23
---

# 표사이동 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉 디테일은 `models/<model>/source-analysis/sediment/` 가 진실의 원천. 본 페이지는 요약 + 링크.

## 1. 모델별 표사 forcing·output

### 1.1 입력 (Forcing) — 공통

각 모델은 다음 forcing 필요:
- **수심**: BADA + parquet (`models/SWAN/source-analysis/wink-pattern.md` §5)
- **흐름**: EFDC/ADCIRC 출력 또는 KHOA 수치조류도
- **파**: SWAN 출력 (`H_s`, `T_p`, 방향, radiation stress)
- **풍**: JMA-MSM 또는 KMA
- **초기 bed**: KHOA 저질조사 (d_{50}, multi-layer composition)

### 1.2 출력 — 공통

- 부유 농도 (mg/L) 3D 격자
- Bed 표고 변화 (m, 시계열)
- Bed 입자 분포 변화 (다층)
- 침전·재부유 flux (kg/m²/s)

## 2. EFDC SED (사용자 주력) — 2 분기 모델

> Canonical: [`models/EFDC/source-analysis/sediment/`](../../models/EFDC/source-analysis/sediment/) — 본 위키 promote 완료 (2026-05-23).

EFDC+ Stable 의 sediment transport 는 **두 분기 system** ([`models/EFDC/source-analysis/sediment/efdc_sediment.md`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md) source-code level 분석 인용):

### 2.1 SedTran-Original (legacy, ISTRAN(6,7))

- **ISTRAN(6) ≥ 1**: cohesive sediment 활성 → `CALSED` (Krone-Partheniades)
- **ISTRAN(7) ≥ 1**: noncohesive 활성 → `CALSND` (Van Rijn 1984, Engelund-Hansen)
- 별도 cohesive/noncohesive 처리, bed 모델 단순

Source 분기: `SedTran-Original/ssedtox.f90:868-880`

| Condition | Behavior | File:Line |
|---|---|---|
| `ISTRAN(6) >= 1 .and. LSEDZLJ` | SEDZLJ 사용 | `ssedtox.f90:868-872` |
| `ISTRAN(6) >= 1 .and. !LSEDZLJ` | CALSED (cohesive only) | `ssedtox.f90:872-874` |
| `ISTRAN(7) >= 1 .and. !LSEDZLJ` | CALSND (noncohesive only) | `ssedtox.f90:878-880` |

### 2.2 SEDZLJ (modern, unified)

- size-class 기반 unified cohesive + noncohesive
- multi-bed-layer dynamics (active layer + 다층 깊이 underlayer)
- Christoffersen-Jonsson wave-current shear stress
- **ISTRAN(7) 자동 disable** when SEDZLJ — unified model 이 둘 다 처리 (`s_sedic.f90:353-355`)

SEDZLJ 활성화 시 추가 arrays (`varalloc.f90:1119-1156`):
- `BULKDENS`, `D50`, `LAYERACTIVE`, `PERSED`, `TAU`, `TAUCOR`, `TSED`, `TSED0` 등

### 2.3 입력 파일 (`efdc.inp` 핵심 카드)

- `NSED` = cohesive sediment classes 수
- `NSND` = noncohesive sediment classes 수
- `SDEN` = sediment density
- `TAUR` / `TAUC` = erosion / critical shear stress
- `IMODE_PARTHENIADES`, `IMODE_VANRIJN` 등 sub-model 선택
- SEDZLJ: 추가 `LSEDZLJ` flag + bed property 파일

### 2.4 한국 적용 사례

사용자 축산항 (영덕) 시뮬:
- Idealized 침퇴적 ±1.5 cm/yr 산출
- 15년 누적 ±22 cm
- → 별도 `experience/efdc-chuksan-sediment.md` (작성 검토)

### 2.5 관련 source-analysis 노트

[`models/EFDC/source-analysis/sediment/`](../../models/EFDC/source-analysis/sediment/) 에 정리된 노트:
- `efdc_sediment.md` (이 §의 source)
- `efdc-water-level-good-current-bad.md` (관련 failure pattern, source-analysis 분류)

기타 EFDC source-analysis ([`models/EFDC/source-analysis/`](../../models/EFDC/source-analysis/)) 18개 노트 — calibration, boundary, hydro core, wetdry 등.

## 3. Delft3D-SED

> Canonical: [`models/Delft3D/source-analysis/sediment/`](../../models/Delft3D/source-analysis/sediment/) — promote 완료.

### 3.1 모듈 구조

- Delft3D-FLOW + SED: `.mor` (morphology), `.sed` (sediment props), `.bnd` (boundary)
- **Van Rijn 1984 / 2007** bedload + suspended
- **Partheniades-Krone** cohesive
- Morphology 결합: time scale acceleration (`MorFac > 1` for long-term)

### 3.2 핵심 노트

[`models/Delft3D/source-analysis/sediment/delft3d_sediment.md`](../../models/Delft3D/source-analysis/sediment/delft3d_sediment.md) — Delft3D 의 sediment 처리 (codex source-code 분석).

기타 — `delft3d_dredge_dump.md`, `delft3d_flow_wave_coupling.md` 등.

## 4. XBeach Sediment

> Canonical: [`models/XBeach/source-analysis/`](../../models/XBeach/source-analysis/) — promote 완료 (16개 노트).

### 4.1 적용 범위

- 폭풍 침식 시뮬 (수일~수주)
- **Soulsby-van Rijn** transport formula
- Dune avalanching (mass transport)
- 짧은 시간 scale, 강 storm 사건 (Maemi, Hinnamnor 등) 한국 적용

### 4.2 핵심 노트

`models/XBeach/source-analysis/` 의 16 노트 중:
- `xbeach.md`, `xbeach_morphology.md`, `xbeach_avalanching.md`, `xbeach_bed_friction.md` 등

## 5. ROMS Sediment

> Canonical: [`models/ROMS/source-analysis/sediment/`](../../models/ROMS/source-analysis/sediment/) — promote 완료.

ROMS-CSTMS (Community Sediment Transport Modeling System):
- bedload + suspended + bed dynamics
- COAWST 통합 (ROMS + SWAN + Atmospheric)
- Soulsby wave-current bottom stress

`models/ROMS/source-analysis/sediment/roms_sediment.md` — codex source-code 분석.

## 6. 평가·검증

### 6.1 메트릭

| 항목 | 정의 | 기준 |
|---|---|---|
| Bed elevation RMSE | √mean((Δz_model − Δz_obs)²) | < 0.1 m (반년-1년) |
| Suspended C RMSE | mg/L | < 50 mg/L (점착) |
| Sandwave migration speed | m/year | 사용자 정점 의존 |
| Sediment budget | sum(Δz) over domain | 균형 확인 |

### 6.2 검증 데이터 source

- **KHOA 저질조사**: d_{50}, multi-layer composition (정점별)
- **MOF/사용자 OBS**: 부유 농도 시계열
- **Multibeam survey**: bed 표고 변화 (repeat survey, 6개월-1년 단위)
- **Side-scan sonar**: sandwave migration

## 7. 다른 토픽과의 교차

- **tides** (`concepts/tides/`): 조류 비대칭 → 표사 방향 결정
- **currents** (`concepts/currents/`): 흐름 forcing 직접 적용
- **waves** (`concepts/waves/`): radiation stress → longshore·cross-shore 표사
- **littoral-drift** (`concepts/littoral-drift/`): 연안 longshore 표사 (CERC·Komar — `01-concept.md` §3)
- **storm-surge** (`concepts/storm-surge/`): 폭풍 침식·범람 (XBeach + sed)

## 8. 본 위키 source-analysis 구조 (promote 완료)

```
models/
├── EFDC/source-analysis/        — 18 노트 (sediment + general)
│   └── sediment/                 — efdc_sediment.md
├── Delft3D/source-analysis/      — 10 노트
│   ├── sediment/                 — delft3d_sediment.md 등
│   └── wave/
├── ADCIRC/source-analysis/        — 41 노트
│   ├── storm-surge/              — 7 노트
│   └── tide/
├── SWAN/source-analysis/          — 21 노트
│   └── wave/                     — 다수
├── XBeach/source-analysis/        — 16 노트
│   └── wave/
└── ROMS/source-analysis/          — 11 노트
    └── sediment/                  — roms_sediment.md
```

총 **117 source-analysis 노트** (이번 promote + 기존). 모두 codex source-code 분석 기반 verified.

## 9. 외부 인용

- EFDC: USEPA · DSI · TetraTech (EFDC+ Stable maintainer)
- Delft3D: Deltares — Lesser et al. 2004 (Coastal Eng 51:883-915)
- XBeach: Deltares — Roelvink et al. 2009 (Coastal Eng 56:1133-1152)
- ROMS: Rutgers — Shchepetkin & McWilliams 2005 (Ocean Modelling 9:347-404)
- Van Rijn (1984·1993·2007) — bedload·suspended 표준 식
- Soulsby (1997) "Dynamics of Marine Sands" — wave-current shear stress

## 10. 연결

- [`01-concept.md`](01-concept.md) ~ [`05-examples.md`](05-examples.md) — 도메인 layer
- 모델별 canonical ([`models/`](../../models/)):
  - [`models/EFDC/source-analysis/`](../../models/EFDC/source-analysis/) — 사용자 주력 (18 노트)
  - [`models/Delft3D/source-analysis/`](../../models/Delft3D/source-analysis/) (10)
  - [`models/XBeach/source-analysis/`](../../models/XBeach/source-analysis/) (16)
  - [`models/ROMS/source-analysis/`](../../models/ROMS/source-analysis/) (11)
- [`concepts/littoral-drift/01-concept.md`](../littoral-drift/01-concept.md) — 연안 longshore (인접)
