---
title: "SWAN ML/surrogate 모델 — DELWAVE·DeepONet·FNO·GNN emulator + transformer/LSTM forecasting (2020-2026)"
topic: swan
canonical_source: external
external_source: "WebSearch + arxiv/GMD/저널 landing-page fetch (2026-06-02). SWAN surrogate/emulator + ML forecasting 연구. 핵심 직접확인: DELWAVE 1.0 (Mlakar 2024 GMD 17:4705-4725 open-access), DeepONet SWAN surrogate (Cai et al. 2026 arxiv:2604.06433 Dawson 그룹), review (Ferdaus 2025 arxiv:2511.21856)."
citation_status: verified
verification_method: "WebFetch 직접확인(verified): DELWAVE GMD open-access abstract+metrics / DeepONet arxiv:2604.06433 abstract / review arxiv:2511.21856. WebSearch snippet(abstract-level): GNN downscaling·FNO·CNN·Swin-LSTM·SWRL Net·PINO — 정량값 일부 snippet 기반(원문 확인 시 보정)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — WebFetch(DELWAVE/DeepONet/review) + WebSearch"
verification_date: 2026-06-02
related:
  - models/SWAN/web-refs/swan-recent-research-2024-2026.md
  - concepts/storm-surge/07-ml-emulators.md
  - models/SWAN/manual-notes/swan-unstructured-time-step.md
  - models/SWAN/web-refs/swan-foundational-papers.md
---

# SWAN ML/surrogate 모델 (2020-2026)

> WebSearch+fetch survey (2026-06-02). SWAN 의 **ML 대체/가속** 연구 — (A) surrogate/emulator (SWAN 대체) (B) forecasting (SWAN 데이터 시계열) (C) hybrid/physics-guided (D) downscaling. storm-surge 의 [[07-ml-emulators]] (PACT/StormNet, surge)와 wave 측 대응. ⚠ 직접확인(DELWAVE/DeepONet/review) 외 정량값은 abstract-level.

## A. Surrogate / emulator (SWAN 직접 대체)

### A.1 DELWAVE 1.0 — CNN point emulator ★ (verified)

- **Mlakar P, Ricchi A, Carniel S, Bonaldo D, Ličer M (2024)**, "DELWAVE 1.0: deep learning surrogate model of surface wave climate in the Adriatic Basin", *Geosci. Model Dev.* **17**, 4705-4725. doi:10.5194/gmd-17-4705-2024 (open-access)
- **Abstract (verbatim)**: "We propose a new point-prediction model, the **DEep Learning WAVe Emulating model (DELWAVE)**, which successfully emulates the behaviour of a numerical surface ocean wave model (Simulating WAves Nearshore, SWAN) at a **sparse set of locations**, thus enabling numerically cheap large-ensemble prediction over synoptic to climate timescales."
- **구조**: CNN 3-block — ① atmospheric encoder (per-input + joint + output) ② temporal collapse (1D conv) ③ regression (FC + skip)
- **성능 (MAE vs SWAN)**: **Hs 5-10 cm / mean dir 10-25° / Tm 0.2 s**, storm detection >95% precision·recall. **>100 wind field/sec** 처리
- **학습**: COSMO-CLM atmo + SWAN out (1971-1998), test 1998-2000 + **2071-2100 climate scenario** (Adriatic 6 정점: Acqua Alta·Ortona·Monopoli buoy 등)
- **의의**: numerically cheap **large-ensemble climate projection** (point prediction). SWAN 의 climate downscaling 가속.

### A.2 DeepONet — operator-learning surrogate (ADCIRC 결합 동기) ★ (verified)

- **Cai S, Dutta S, Loveland M, Valseth E, Rivera-Casillas P, Trahan C, Dawson C (2026)**, "Operator Learning for Surrogate Modeling of Wave-Induced Forces from Sea Surface Waves", arxiv:**2604.06433**
- **Abstract (요약)**: "Wave setup... radiation stress, motivates the **coupling of circulation models with wave models** to improve storm surge prediction, however, traditional numerical wave models are complex and computationally expensive. As a result... wave models are often executed at much **coarser temporal resolution** than circulation models. We explore **Deep Operator Networks (DeepONets)** as a surrogate for the **SWAN** numerical wave model... tested on 1-D and 2-D steady-state... realistic example of steady state wave simulation in **Duck, NC**, achieved consistently high accuracy in predicting the components of the **radiation stress gradient** and **significant wave height**."
- **구조**: DeepONet (operator learning), 예측 = radiation stress gradient + Hs
- **의의**: **Clint Dawson 그룹(ADCIRC)** — SWAN+ADCIRC coupling([[swan-unstructured-time-step]] Casey Dietrich 41.20)의 **wave 측 surrogate**. Surge 측 PACT([[07-ml-emulators]])와 대칭. Coupled wall-clock 절감 (wave 를 coarse temporal 대신 DeepONet).

### A.3 FNO / GNN / CNN surrogate (abstract-level)

- **FNO (Fourier Neural Operator)**: regional ocean modeling 적용 (*Frontiers Marine Science* 2024, fmars.2024.1383997). Digital Twin Earth-Coasts: FNO coastal flood surrogate **45× 가속** (arxiv:2110.07100, Jiang et al.)
- **GNN + polynomial ridge regression**: Hs **downscaling**, RMSE **0.3-2 cm**, **80× faster** than numerical (*Ocean Modelling* S1463500323000963)
- **CNN regional wind-wave surrogate** (*Coastal Eng/Applied Ocean Res* S0141118722002218)
- **PINO (Physics-Informed Neural Operator)**: nonlinear wavefield reconstruction real-time (arxiv:2508.03315) — physics loss 로 순수 data-driven 한계 극복

## B. Forecasting (SWAN/WW3 데이터 → 시계열 DL)

- **Crossformer + SWAN** adaptive decomposition Hs (*Expert Systems with Applications* 2025, S0957417425021426) — [[swan-recent-research-2024-2026]] §2
- **LSTM > Random Forest** typhoon Hs 3h (Pearl River, 87 typhoon SWAN, *JMSE* 13:1612)
- **Swin transformer-LSTM** high-res ocean wave (Chinese marginal seas, reanalysis-driven)
- **Self-Attention ConvLSTM** regional Hs
- **SWRL Net** (*Weather and Forecasting* 35(6), 2020) — spectral residual DL 로 short-term wave forecast 개선 (numerical 위 residual correction)
- **ANN port wave forecast** (WW3 기반, *Ocean Eng* S0029801822008496)

## C. Hybrid / physics-guided

- **Physics-guided DL** skillful wind-wave (PMC11616684) — 물리 제약 결합
- **WW3 + ML hindcast 개선** (*Coastal Eng* S0378383923001059) — numerical hindcast 의 ML 보정
- **XAI (Durap 2025a/b)** — explainable, feature engineering ([[swan-recent-research-2024-2026]] §2)

## D. Review / 종합

- **Ferdaus MM, Cooper NA, Schmidt AB, Pokhrel P, Ioup E, Abdelguerfi M, Simeonov J (2025)**, "A Comprehensive Review of Phase-Averaged and Phase-Resolving Wave Models for Coastal Modeling Applications", arxiv:**2511.21856** (verified fetch):
  - **SWAN** = "cornerstone third-generation spectral model" — "comprehensive shallow water physics (triads, breaking, friction)" + "fully implicit time integration for efficiency in steady-state cases" + flexible grid + open-source
  - phase-averaged = wave action balance 로 통계량(mean Hs), 개별 phase 미추적; regional/global forecast + climate 효과적
  - **ML 통합 = emerging trend**: "data-driven parameterizations and surrogate models may **supplement or replace** traditional physics-based formulations for specific processes" — 단 **물리모델은 training data 외 extrapolation 에 필수** (caveat)

## E. 분류 요약

| 분류 | 대표 | 아키텍처 | 가속/정확도 | 비고 |
|---|---|---|---|---|
| **A surrogate** | DELWAVE 2024 | CNN point | >100 wind/sec, Hs MAE 5-10cm | climate ensemble |
| | DeepONet 2026 | operator learning | Duck NC, radiation stress+Hs | **ADCIRC 결합** Dawson |
| | FNO / GNN | neural operator | 45-80× faster, RMSE 0.3-2cm | downscaling |
| **B forecast** | Crossformer/Swin-LSTM | transformer+LSTM | typhoon Hs 3h | SWAN=학습데이터 |
| **C hybrid** | PINO / physics-guided | physics loss | extrapolation 개선 | residual correction |
| **D review** | Ferdaus 2025 | — | — | ML=supplement/replace + caveat |

## F. 핵심 통찰

1. **SWAN = 고품질 학습데이터 생성기** (DELWAVE/DeepONet 모두 SWAN out 으로 학습) → ML 이 emulate 후 ensemble/coupled 가속.
2. **Operator learning (DeepONet/FNO)** 이 point-LSTM 보다 발전 — full field + 물리량(radiation stress) 예측, **SWAN+ADCIRC coupling 의 wave surrogate** (Dawson 그룹 2026)로 storm-surge 운영 직결.
3. **caveat (Ferdaus 2025)**: 물리모델은 extrapolation(미학습 extreme)에 여전히 필수 → hybrid/PINO 가 현실적 방향.
4. wave surrogate(DELWAVE/DeepONet) ↔ surge surrogate([[07-ml-emulators]] PACT/StormNet) **대칭 구조** — coupled wave-surge ML emulation 이 차세대.

## G. 한계

- A.3·B·C 의 정량값은 **WebSearch snippet abstract-level** (full-text paywall ScienceDirect/MDPI) → primary fetch 시 보정.
- arxiv 2604.06433(DeepONet)·2508.03315(PINO)는 preprint — peer-review 후 metric 변동 가능.
- DELWAVE/DeepONet 만 직접 fetch verified; 나머지 bibliographic 은 검색결과 기반.

## H. 연결

- [[07-ml-emulators]] — storm-surge ML emulator (PACT/StormNet, surge 측 대응)
- [[swan-recent-research-2024-2026]] — SWAN 최근 동향 (§2 ML 하이브리드 상위)
- [[swan-unstructured-time-step]] — SWAN+ADCIRC coupling (DeepONet surrogate 대상)
- [[swan-foundational-papers]] — SWAN 원논문
