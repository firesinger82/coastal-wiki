---
title: "SWAN 최근 연구동향 2023-2026 — ST6 보급·ML 하이브리드·data assimilation·TC coupling·기후 downscaling"
topic: swan
canonical_source: external
external_source: "WebSearch (2026-06-02) SWAN 2023-2026 최근 논문 survey. 주요: JMSE/Ocean Modelling/Ocean Dynamics/Expert Systems with Applications/JAMES/Frontiers Marine Science. 6 동향: (1) ST6 보급·calibration (2) ML/DL 하이브리드 SWH (3) data assimilation (4) regional+기후 downscaling (5) TC wave-surge coupling (6) wind drag/WBLM."
citation_status: source-needed
verification_method: "WebSearch 3회 (2026-06-02) — bibliographic(저널·권·연도·DOI)은 검색결과 기반 verified; **정량 finding(RMSE/R/correlation)은 검색 스니펫·abstract 수준** (full-text paywall ScienceDirect/MDPI 403). 동향 survey 성격 → citation_status: source-needed (개별 논문 primary fetch 시 verified 승격)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — WebSearch survey, 정량값 abstract-level"
verification_date: 2026-06-02
related:
  - models/SWAN/web-refs/swan-foundational-papers.md
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
---

# SWAN 최근 연구동향 2023-2026

> WebSearch survey (2026-06-02). SWAN 의 코드/이론은 [[swan-documentation-stack]] (v41.51)에 고정; 본 노트는 **응용·결합·calibration 연구동향**. ⚠ **정량값은 abstract/검색 스니펫 수준** (full-text paywall) → `source-needed` (primary fetch 시 verified 승격). 원논문은 [[swan-foundational-papers]].

## 1. ST6 physics 보급 + calibration (vs Komen default)

swantech §2.3.3 의 ST6([[swan-tech-ch2-dissipation-detailed]] §4) 가 최근 regional 응용서 default Komen 대비 우위 보고 다수.

- **"A Study on Enhancing the Accuracy of Wave Prediction Models Through SWAN Sensitivity Experiments: Focusing on Wind Input and Whitecapping Dissipation"**, *JMSE* **14**(5), 435 (2026). doi:10.3390/jmse14050435
  - 한국 동해안 겨울폭풍파. **ST6 default 가 최우수**: ME 0.052 m / RMSE 0.342 m / SI 0.129 / **R 0.964** (Komen 대비 개선). wind input + whitecapping 조합 민감도.
- **Liu Q et al. (2021)**, "Global Wave Hindcasts Using the Observation-Based Source Terms (ST6): Description and Validation", *JAMES*. doi:10.1029/2021MS002493 — ST6 global hindcast 검증.
- **"A general method to determine the optimal whitecapping dissipation coefficient in the SWAN model"**, *Frontiers in Marine Science* (2023). doi:10.3389/fmars.2023.1298727 — whitecapping 계수 최적화 방법론.
- 동향: ST6(관측기반)가 Komen(WAM Cycle 3)/Janssen(Cycle 4) 대비 wind-sea·swell 동시 개선. wind drag 의 **sea-state-dependent / WBLM(wave boundary layer model)** parameterization + 고차 drag coefficient (remote sensing 유도, WW3·SWAN 통합) 연구 진행.

## 2. ML/DL 하이브리드 SWH 예측 (SWAN 데이터 학습)

> **상세는 [[swan-ml-surrogate-models]] 별도** (surrogate DELWAVE/DeepONet/FNO/GNN + forecasting transformer/LSTM + hybrid PINO + review).

SWAN numerical 출력을 학습데이터로 한 **hybrid (numerical + data-driven)** SWH 예측이 급증.

- **"Enhancing significant wave height prediction based on numerical SWAN and Crossformer models with adaptive decomposition"**, *Expert Systems with Applications* (2025). [S0957417425021426] — SWAN + **Crossformer** + adaptive decomposition.
- **"Machine Learning-Based Short-Term Forecasting of Significant Wave Height During Typhoons Using SWAN Data: Pearl River Estuary"**, *JMSE* **13**(9), 1612 (2025). doi:10.3390/jmse13091612
  - **87 historical typhoon** SWAN 데이터. **LSTM > Random Forest** (3h forecast 낮은 RMSE·높은 R², wave peak 포착 우위).
- **Self-Attention ConvLSTM** 기반 regional SWH 예측 (SWAN 결합) 연구.
- **Durap (2025a/2025b)**: **Explainable AI(XAI)** + feature engineering 하이브리드 (black-box 한계 극복·해석성).
- 동향: SWAN 이 **고품질 학습 데이터 생성기** 역할 (특히 typhoon/extreme), DL 이 단기 forecast 가속·peak 보정.

## 3. Data assimilation

- **"Estimating Coastal Winds by Assimilating High-Frequency Radar Spectrum Data in SWAN"** (PMC8659604) — HF radar spectrum → SWAN wind 추정 assimilation.
- **"Application of SWAN model for wave forecasting in the southern Baltic Sea supplemented with measurement and satellite data"**, *Environmental Modelling & Software* (2023). [S1364815223000105] — 측정 + 위성 data 보강.
- 동향: wide-area(위성) + local(HF radar/buoy) assimilation 으로 wind/wave BC 개선.

## 4. Regional 응용 + 기후 downscaling

- **"Regional Wave Analysis in the East China Sea Based on the SWAN Model"**, *JMSE* **13**(6), 1196 (2025). doi:10.3390/jmse13061196 — **ERA5 wind + ETOPO1 bathy, 0.05°×0.05°, 2009-2023** 고해상 wave energy 평가.
- **"On the capability of SWAN model for South Atlantic Ocean wave simulation"**, *Ocean Dynamics* **75**:51 (2025). [2025OcDyn..75...51Z]
- **"Dynamically downscaled future wave projections from SWAN model results for the main Hawaiian Islands"** (USGS Science Data Catalog) — 기후 wave projection downscaling.
- **"Assessing the impact of wave model calibration in the uncertainty of wave energy estimation"**, *Renewable Energy* (2023). [S0960148123006729] — wave energy 평가 불확실성.
- 동향: ERA5 reanalysis 강제 + 고해상 nearshore downscaling, **wave energy resource assessment** + 기후 projection.

## 5. Tropical cyclone wave-surge coupling

- **"Numeric Modeling of Sea Surface Wave Using WAVEWATCH-III and SWAN During Tropical Cyclones: An Overview"**, *JMSE* **13**(8), 1450 (2025). doi:10.3390/jmse13081450 — WW3·SWAN TC 모델링 overview.
- **"An efficient early warning system for typhoon storm surge based on time-varying advisories by coupled ADCIRC and SWAN"**, *Ocean Dynamics* (2015) — SWAN+ADCIRC 결합 조기경보 (본 위키 [[swan-unstructured-time-step]] Casey Dietrich 41.20 결합과 연결).
- 동향: **unstructured SWAN+ADCIRC** (단일 mesh wave+surge), WW3(대양)→SWAN(연안) nesting, time-varying advisory 운영. 본 위키 ADCIRC `adcirc-swan-coupling` (PR #498 SWANTimeControl)와 직접 관련.

## 6. 핵심 동향 요약

| 동향 | 키워드 | 본 위키 연결 |
|---|---|---|
| ST6 보급 | 관측기반 source, Komen 대비 우위, whitecapping 최적화 | [[swan-tech-ch2-dissipation-detailed]] §4 / [[swan-st6-babanin-implementation]] |
| ML 하이브리드 | LSTM/RF/Crossformer/ConvLSTM/XAI, SWAN=학습데이터 | (신규 영역) |
| Data assimilation | HF radar·위성, wind/wave BC | (신규) |
| 기후 downscaling | ERA5+고해상, wave energy, projection | (신규) |
| TC coupling | SWAN+ADCIRC unstructured, WW3 nesting | [[swan-unstructured-time-step]] / ADCIRC swan-coupling |
| wind drag | sea-state/WBLM, 고차 C_D | [[swan-tech-ch2-sources-sinks]] (Zijlema 2012 C_D) |

## 7. 한계

- **정량 finding(RMSE/R/correlation)은 검색 스니펫·abstract 수준** — full-text paywall(ScienceDirect/MDPI HTTP 403). primary fetch 시 verified 승격 + 정확값 보정 필요.
- DOI 일부는 검색결과 기반 (jmse14050435·jmse13091612·jmse13061196 등 MDPI 패턴 유도) — crossref 직접확인 권장.
- 2026 상반기 논문 일부만 포착 (June 2026 기준 검색) — Hermes coastal-research cron 으로 지속 추적 대상.

## 8. 연결

- [[swan-foundational-papers]] — 원논문 (ST6 Rogers/Zieger, QC Smit-Janssen/Akrish 등)
- [[swan-documentation-stack]] — SWAN v41.51 공식 docs
- [[swan-tech-ch2-dissipation-detailed]] — ST6 물리 (§2.3.3 §4)
- [[swan-unstructured-time-step]] — SWAN+ADCIRC 결합 (TC coupling)
