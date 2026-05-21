---
title: "표사이동 — 06 모델 적용 (EFDC SED · Delft3D-SED · XBeach)"
topic: sediment-transport
canonical_source: self
citation_status: source-needed
verification_method: "AI cross-reference. 본 문서는 요약 + 링크 ([CONVENTIONS.md §3] canonical source 분리). 모델 디테일은 `models/<model>/`이 진실의 원천 (현재 EFDC stub) — 채워지면 source-needed → verified."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: ""
verification_date: ""
---

# 표사이동 — 06 모델 적용

> **Canonical source 규칙** ([CONVENTIONS.md §3](../../CONVENTIONS.md)): 모델 메커닉 디테일은 `models/<model>/`이 진실의 원천. 본 페이지는 요약 + 링크.

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

## 2. EFDC SED (사용자 주력)

> Canonical: [`models/EFDC/`](../../models/EFDC/) + `efdc-sed-trans-2003` source.

### 2.1 워크플로

```
1. SWAN (WINK middle → detail) → wave forcing
   ↓ H_s, T_p, radiation stress NetCDF
2. KHOA 수치조류도 또는 EFDC sub-grid → current forcing
   ↓
3. EFDC + SED 시뮬
   ↓ efdc.inp (NSED·NSND·SDEN·TAUR·TAUC 등)
   ↓ wave coupling (선택)
   ↓
4. 출력: bed elev·suspended C·bed thickness
   ↓
5. 검증: KHOA 저질·OBS·multibeam
```

### 2.2 사용자 축산항 시뮬

이전 사용자 작업 ([memory ID 1215]):
- Idealized 침퇴적 변화 ±1.5 cm/yr 산출
- 15년 누적 ±22 cm
- 보고서 산출물: cell_postmap_zoom/ideal/ 등

→ 실제 input·output 사례는 `experience/efdc-chuksan-sediment.md` (작성 검토).

## 3. Delft3D-SED

> Canonical: [`models/Delft3D/`](../../models/Delft3D/) (stub).

- D3D-4 FLOW + SED: `.mor`, `.sed`, `.bnd`
- Van Rijn (1984·2007) bedload + suspended
- Cohesive: Partheniades-Krone

## 4. XBeach Sediment

> Canonical: [`models/XBeach/`](../../models/XBeach/) (stub).

- 폭풍 침식 시뮬 (수일~수주)
- Soulsby-van Rijn 식
- Dune avalanching
- 한국 적용 사례 (서해 폭풍·태풍 시): 보강 대기

## 5. 평가·검증

### 5.1 메트릭

| 항목 | 정의 | 기준 |
|---|---|---|
| Bed elevation RMSE | √mean((Δz_model − Δz_obs)²) | < 0.1 m (반년-1년) |
| Suspended C RMSE | mg/L | < 50 mg/L (점착) |
| Sandwave migration speed | m/year | 사용자 정점 의존 |
| Sediment budget | sum(Δz) over domain | 균형 확인 |

### 5.2 검증 데이터 source

- **KHOA 저질조사**: d_{50}, multi-layer composition (정점별)
- **MOF/사용자 OBS**: 부유 농도 시계열
- **Multibeam survey**: bed 표고 변화 (repeat survey, 6개월-1년 단위)
- **Side-scan sonar**: sandwave migration

## 6. 다른 토픽과의 교차

- **tides** (`concepts/tides/`): 조류 비대칭 → 표사 방향 결정
- **currents** (`concepts/currents/`): 흐름 forcing 직접 적용
- **waves** (`concepts/waves/`): radiation stress → longshore·cross-shore 표사
- **littoral-drift** (미작성): 연안 따라 표사 (concepts/sediment-transport 확장 토픽)
- **storm-surge** (미작성): 폭풍 침식·범람 (XBeach + sed)

## 7. `verified` 승격 체크리스트

- [ ] `models/EFDC/source-analysis/sediment.md` 작성 — `efdc-sed-trans-2003` 발췌
- [ ] `models/EFDC/manual-notes/sediment-input-cards.md` — efdc.inp SED 카드
- [ ] `models/Delft3D/manual-notes/sed-input.md` — .mor, .sed
- [ ] `models/XBeach/manual-notes/morphology.md` — morphology=1, sedtrans
- [ ] 사용자 축산항 시뮬 결과 정량 통합 → `experience/`
- [ ] 한국 KHOA 저질·OBS 검증 정점 list

## 8. 연결

- `01`-`05` — 도메인 지식
- 모델별 canonical (`models/`):
  - [`models/EFDC/`](../../models/EFDC/) — 사용자 주력
  - [`models/Delft3D/`](../../models/Delft3D/) (stub)
  - [`models/XBeach/`](../../models/XBeach/) (stub)
- 외부 인용:
  - EFDC: USEPA · DSI
  - Delft3D: Deltares
  - XBeach: Deltares
  - Van Rijn (1984·1993·2007) — 모델 implementation의 기반 식
  - Soulsby (1997) — wave-current shear stress
