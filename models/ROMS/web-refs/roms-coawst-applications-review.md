---
title: "ROMS·COAWST 적용 리뷰 — Adriatic Sea (Carniel·Russo·Benetazzo 2013, full-PDF)"
model: ROMS
canonical_source: external
citation_status: verified
verification_method: "arxiv:1309.7600v4 full PDF 직접 read (pdftotext, 237줄 전체). 본 노트의 모든 단언은 논문 본문에서 실제 읽은 내용만 인용 — 논문에 없는 격자·검증 수치 날조 금지. COAWST 결합 구성은 논문이 명시한 ROMS+SWAN(MCT 결합)만 기술; WW3/WRF는 본 논문에 등장하지 않으므로 미기술."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/ROMS/web-refs/roms-coawst-adriatic-applications.md
  - models/ROMS/web-refs/roms-official-resources.md
  - models/ROMS/source-analysis/roms_wec.md
  - models/ROMS/source-analysis/roms_atmospheric_forcing.md
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/README.md
---

# ROMS·COAWST 적용 리뷰 — Adriatic Sea (Carniel et al. 2013)

> ROMS/COAWST 가 반폐쇄해(Adriatic Sea)에서 **순수 hydrodynamic 구성 → 완전 결합 COAWST** 로 발전한 운영·연구 적용 사례 리뷰의 full-PDF 정리. 모델 메커닉 자체는 [`source-analysis/`](../source-analysis/) 가 canonical, 본 노트는 적용 맥락(application context) 참조.
>
> 기존 [`roms-coawst-adriatic-applications.md`](roms-coawst-adriatic-applications.md) 는 동일 논문의 abstract-level 요약(`source-needed`). 본 노트는 full-PDF read 후 본문 5개 적용 사례까지 확장한 `verified` 버전.

## 1. 출처

| 항목 | 값 |
|---|---|
| 제목 | "A review of modeling applications using ROMS model and COAWST system in the Adriatic sea region" |
| 저자 | Sandro Carniel (ISMAR-CNR), Aniello Russo (Univ. Politecnica delle Marche), Alvise Benetazzo (ISMAR-CNR) |
| arxiv ID | **1309.7600v4** |
| canonical_source | external (논문) |
| citation_status | **verified** (bibliographic + full-PDF) |

## 2. 리뷰의 범위 (abstract·서론)

논문은 ROMS(www.myroms.org) 패밀리 — community·3-D·hydrostatic·finite-difference, Reynolds Averaged Navier-Stokes 방정식 해석 모델 — 의 Adriatic Sea 적용을 정리한다 (본문 line 38-40). 최초의 순수 hydrodynamic 구성에서 시작해 현재의 **COAWST (Coupled Ocean-Atmosphere-Wave-Sediment Transport)** 시스템까지 발전했으며, 광범위한 공간·시간 스케일을 다루어 **ICZM (Integrated Coastal Zone Management)** 및 **MSP (Marine Spatial Planning)** 활동을 지원한다 (abstract).

현재 운영 구성 3종 (abstract, line 16-18):

| 운영 시스템 | 목적 | 결합 |
|---|---|---|
| ROMS 운영판 | 매일 hydrodynamic + 해수면 3일 예보 | 단독 |
| 두 번째 ROMS | 주요 biogeochemical 특성 모델링 | Fennel 모듈 |
| 세 번째 (COAWST) | 극한 파랑 예보 | **ROMS ↔ SWAN 양방향 결합** |

운영 모델은 oil-spill 분산, storm surge, 폭풍 시 해안 morphodynamic 변화, Po 강 saline wedge 침입 등 sub-model 을 구동하여 민·환경 보호 활동을 지원한다 (line 19-21). 출력은 **NetCDF CF-compliant** 포맷으로 작성되어 **THREDDS Data Server** 를 통해 배포된다 (line 25-26).

## 3. 본문이 다룬 적용 사례 5종

### 3.1 AdriaROMS 4.0 — hydrodynamic 예보 + 전용 sub-model (§1)

- 전체 Adriatic 해역에 대해 **균일 2 km 해상도** 격자에서 매일 예보 (line 55-56).
- Air-sea heat·momentum·water flux 는 **COSMO-I7** 시간별 출력으로부터 interactive 하게 계산 (line 56-57) — cf. ROMS 의 atmospheric forcing 처리는 [`roms_atmospheric_forcing`](../source-analysis/roms_atmospheric_forcing.md).
- 주요 조석 성분을 open boundary 에 부과, Po 강 유량은 real-time 데이터, 그 외 48개 강·karstic spring 은 monthly climatology 로 도입 (line 57-59). Otranto Strait open-boundary 의 T/S/sea level/velocity 는 GNOO Mediterranean Forecasting System 이 제공 (line 59-61).
- 출력은 ARPA-SIMC 에서 여러 운영 응용 구동: 침수 조기경보용 morphodynamic 1D 모델(Emilia Romagna 해안 프로파일), Rimini 해수욕장 수질 예측(Delft3D 기반, "Previbalneazione" 프로젝트), oil-spill rapid response, Po 강 saline wedge 침입 예측 (line 62-75).

### 3.2 EMMA — hypoxia(저산소) 이벤트 예보 (§2)

- LIFE-Environment framework 하의 EMMA(Environmental Management through monitoring and Modelling of Anoxia) 프로젝트. 북부 Adriatic(특히 Rimini 일대) 단기 hypoxic 이벤트 예보 (line 81-87).
- ROMS 의 **Fennel biogeochemical 모듈** 채택 — 수층 pelagic nitrogen cycle + water-sediment 계면 remineralisation 재현. 무기 질소(nitrate·ammonium), 식·동물플랑크톤 biomass, small/large detritus, 무기 탄소, 용존 산소 dynamics 포함 (line 88-92).
- Air-sea flux 는 비정수압 limited-area 모델 **COSMO-I7** (수평 7 km, ECMWF 경계조건) 출력으로 계산 (line 93-96).
- 수평 해상도 ~2 km, 3시간마다 출력, 적분 기간은 2007 늦봄부터 (line 97-98).

### 3.3 NA-COAWST — 결합 wave-current 시스템 (§3)

- 북부 Adriatic 의 COAWST 운영판(NA-COAWST), **양방향 wave-current interaction** 포함 (line 105-106).
- **ROMS ↔ SWAN 결합은 Modeling Coupling Toolkit(MCT) 로 수행** (line 106-107) — cf. ROMS 측 wave-effect-on-current 메커닉은 [`roms_wec`](../source-analysis/roms_wec.md) (vortex-force·Stokes drift·breaking dissipation + SWAN 교환 필드).
- 도메인: 북부 Adriatic sub-basin, **0.5 km 수평 해상도**, 최대 수심 100 m. 격자는 AdriaROMS 4.0 격자에 정확히 맞도록 설계 (line 107-109).
- AdriaROMS 4.0 및 SWAN ITALIA 운영 모델이 남동측 open boundary 의 currents·level·T·S·파랑 특성 조건을 제공, 조석 성분도 부과 (line 109-112).
- **2011-11-25 부터 운영 가동** (line 111-112).
- 결합에서 ocean 모델은 wave 모델에 currents·자유표면 elevation 을 Benetazzo et al. (2013) 공식으로 제공 (line 113-114). 심한 폭풍 시 결합 모델이 larger-wave 영역·sediment blob 등 소규모 feature 를 더 정밀하게 결정 (line 116-119). Acqua Alta tower 및 Jesolo 일대 AWAC(2013 겨울 설치) 센서 결과가 NA-COAWST 의 개선된 예보를 뒷받침하는 것으로 보임 (line 119-122).

### 3.4 small pelagic fish 알·유생 수송·분산 (§4)

- ROMS 출력으로 구동되는 **Individual Based Model(IBM)** 로 멸치·정어리 알·유생 수송·확산 연구 (line 124-128). 서로 다른 대기·해양 특성(current·river runoff) 의 2년을 다룬 일련의 IBM 시뮬레이션.

### 3.5 Bevano 강 하구 고해상 nearshore sediment dynamics (§5)

- ROMS 의 fully 3-D, SWAN 과 양방향 결합 + 전용 sediment transport 모듈로 구성된 통합 wave-current-sediment 모델 (line 131-134).
- microtidal·low-energy 파랑 환경인 Bevano 강 하구(2006 timber engineering 으로 인공 개조)의 morphological 변화 모델링 (line 135-139).
- 결과: 30년 빈도 홍수 시 secondary inlet 개통 가능성 확인, ebb tide 가 small ebb delta/swash bar 생성을 지배 — "minimum maintenance option strategy" 로 채택 (line 142-146).

## 4. 결론에서 강조한 ROMS·COAWST 역량

논문 결론(line 148-181)은 사용된 numerical tool 이 embedding 한 state-of-the-art 역량을 명시:

- up-to-date **bottom boundary layer** 기술,
- **wetting and drying** 능력,
- 고급 **vertical mixing** 및 **wave-current interaction** scheme (Kantha and Carniel 2003; Carniel et al. 2009),
- **biogeochemical 모듈**,
- one-way·two-way successive **nesting** + full two-way coupling → 이탈리아 연안 매우 고해상 도달, river mouth 환경 상세 시뮬레이션 (line 161-166).

데이터 배포는 "Users and Data Producers entry barriers" 극복을 위해 NetCDF(CF convention) + **THREDDS Data Server(TDS)** 사용, OpenSearch·OGC Catalog Services 등 표준 query 로 discovery 가능, "INSPIRE compliant web service" 지향 (line 167-181).

## 5. 본 위키 연계

| 본 노트 항목 | 위키 canonical |
|---|---|
| wave-current interaction (NA-COAWST §3.3) | [`roms_wec`](../source-analysis/roms_wec.md) — vortex-force·Stokes·breaking + SWAN 교환 필드 |
| air-sea flux (COSMO-I7 forcing §3.1·3.2) | [`roms_atmospheric_forcing`](../source-analysis/roms_atmospheric_forcing.md) |
| 자료동화 일반 | [`roms_4dvar`](../source-analysis/roms_4dvar.md) (본 논문은 4D-Var 미사용 — 운영판은 forecast 중심) |
| 공식 자원·COAWST 출처 | [`roms-official-resources`](roms-official-resources.md) |
| 동일 논문 abstract-level 요약 | [`roms-coawst-adriatic-applications`](roms-coawst-adriatic-applications.md) |

## 6. 주의 (날조 방지 기록)

- 본 논문이 명시한 결합 구성은 **ROMS ↔ SWAN (MCT 경유)** 뿐이다. COAWST 시스템 전반은 WRF·WW3·CSTMS 등을 포함하지만(별도 canonical: [`roms-official-resources`](roms-official-resources.md)), **본 논문 본문에는 WW3·WRF 가 등장하지 않으므로** 본 노트에서 해당 결합을 적용 사실로 기술하지 않는다.
- 격자 해상도(2 km / 0.5 km), 운영 개시일(2011-11-25), COSMO-I7 해상도(7 km) 등 정량값은 모두 본문 line 에서 직접 인용한 것이다.
