---
title: "Storm Surge ML Emulators — surrogate models for hydrodynamic storm-surge prediction"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "arxiv:2605.09036 직접 fetch (WebFetch 2026-05-26) — abstract + 메타데이터 (authors, 제출일 2026-05-09, 카테고리 cs.LG) 직접 인용. 본문 §2 의 architecture 디테일·peak-aware loss·결과·한계는 전부 abstract 인용 기반. 정량 RMSE/MAE 수치, training hindcast 모델 (ADCIRC/Delft3D/etc.), CMIP6 5개 model 구체명, US Northeast 정점 좌표/개수 등은 abstract 미명시 — full PDF read 후 보강 가능. §3-4 의 본 위키 cross-ref 와 한국 적용 검토는 자체 분석."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-26
verification_by: "Claude Opus 4.7 (1M context) — arxiv abs 페이지 직접 fetch + author/date/category/abstract 직접 인용"
verification_date: 2026-05-26
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - concepts/storm-surge/04-code-and-tools.md
  - concepts/storm-surge/05-examples.md
  - models/ADCIRC/source-analysis/storm-surge/
---

# Storm Surge ML Emulators

> 본 §는 full hydrodynamic 모델 (ADCIRC, Delft3D, SCHISM 등) 의 계산비용 한계를 ML/surrogate 로 우회하는 storm-surge prediction 접근법 정리. 실시간 위험 평가·대규모 ensemble·기후 시나리오 평가에 사용.

## 1. 왜 ML emulator 인가

기존 full hydrodynamic 모델은 정확도는 높지만 계산비용이 큼:

- 한국 ADCIRC hindcast typical: 1 storm event = 1-12 시간 wall-clock (64-256 cores MPI) — [`04-code-and-tools.md §7`](04-code-and-tools.md#7-운영-예제--한국-태풍-hindcast-워크플로)
- 100-1000 ensemble (CMIP6 forcing 시나리오, return period 계산, real-time 다중 track 평가) → 수 천 core-hour
- early warning timeline (수 분-수 시간) 에 부적합한 경우 다수

ML/surrogate model 은 학습 후 forward pass 가 수 초 단위 — ensemble·기후 예측·실시간 경보 후보. 단, **학습에 의존하는 full-physics hindcast 데이터셋** 이 전제 (보통 ADCIRC 등 high-fidelity 모델로 미리 만든 시뮬레이션 결과).

## 2. PACT (Liu et al. 2026) — peak-aware cross-attention graph transformer

### 2.1 기본 정보 (verified arxiv 2026-05-26 fetch)

| 항목 | 값 |
|---|---|
| arxiv ID | **2605.09036v1** |
| 제목 | "PACT: Peak-Aware Cross-Attention Graph Transformers for Efficient Storm-Surge Emulation" |
| 저자 | Zesheng Liu, Doyup Kwon, Ning Lin, Maryam Rahnemoonfar |
| 제출일 | 2026-05-09 |
| arxiv 카테고리 | cs.LG (Machine Learning) |
| URL | <https://arxiv.org/abs/2605.09036> |
| 소속 | abstract 페이지 미명시 (full paper 에 명시 추정) |

### 2.2 모델 아키텍처 (abstract 직접)

PACT 는 station-level surge prediction 을 위한 pipeline:

1. **Patch-as-graph encoding** — atmospheric forcing field 의 각 patch 를 graph 로 표현
2. **GraphSAGE** spatial encoding — graph node 의 spatial structure 추출
3. **Learned station query + cross-attention** — uniform pooling 대신 station 별 query 를 학습, forcing graph node 들로부터 정보 aggregation
4. **Transformer encoder** — forcing history 의 시간축 dependency 모델링
5. **Horizon-query decoder** — lead time 별 forecast 생성 (shared temporal memory 로부터)

→ 핵심 차별점: GNN baseline 대비 *station-specific cross-attention* 으로 spatial pooling 을 학습.

### 2.3 Peak-aware learning strategy

극값 (peak surge) 예측 정확도 향상이 핵심 contribution. 3 가지 기법 조합:

- **Auxiliary peak-aware head** — main forecaster 외 가벼운 별도 head 가 peak signal 강조
- **Tail-focused loss** — peak-dominated sample (distribution tail) 에 가중치 부여
- **Horizon-wise slope regularizer** — multi-step 예측의 변화율 일관성 강제 (시간축으로 coherent trajectory)

→ ML emulator 의 보편적 약점인 *extreme event under-prediction* 을 학습 단계에서 보강.

### 2.4 검증 + 결과 (abstract 직접)

- 영역: **US Northeast coast 다수 tide-gauge 정점** (구체 station 좌표·개수 abstract 미명시)
- baseline: "strong spatio-temporal graph neural network" (구체 architecture abstract 미명시)
- forcing: reanalysis + **CMIP6 datasets (5개)** (구체 model name abstract 미명시)
- 지표: **RMSE + MAE 양쪽 baseline 대비 개선**
- 극값 진단: reanalysis + 대부분 CMIP6 에서 **peak fidelity + tail preservation 개선**
- 계산 효율: **1 시즌 (winter) surge trajectory ≈ 3.5 초** (학습 후, 1년 데이터 기준)

### 2.5 한계 (저자 명시)

- **reanalysis → climate-model (CMIP6) transfer gap** — reanalysis 로 학습 후 CMIP6 forcing 으로 inference 시 markedly degrade
- CMIP6 family 끼리는 transfer 비교적 양호 ("transfers well within the CMIP6 family")
- → **persistent reanalysis-GCM gap** 이 ML surrogate generalization 의 핵심 장애로 진단

### 2.6 본 위키 미보강 (full PDF read 시 보강 가능)

abstract 만으로는 확인 불가:

- **Training hindcast 의 hydrodynamic 모델** — ADCIRC? Delft3D? SCHISM? (abstract 미명시)
- 구체 RMSE/MAE 수치 (abstract 는 "outperforms baseline" 으로만 정성)
- baseline GNN architecture 명세
- US Northeast 구체 station (좌표·개수·기간)
- CMIP6 5개 model 구체명
- code/data 공개 여부
- training data window, batch size, 학습 시간 등 hyperparameter

→ full paper PDF (<https://arxiv.org/pdf/2605.09036v1>) read 후 본 §2 update 권장.

## 3. 본 위키 storm-surge 자료와의 관계

| 본 위키 자료 | PACT 와의 접점 |
|---|---|
| [`01-concept.md`](01-concept.md) §3 인자 | PACT 의 input atmospheric forcing = §3 의 wind·pressure (IB) 인자와 동등 |
| [`02-theory.md`](02-theory.md) Pugh §6 + ADCIRC GWCE | PACT 는 GWCE 풀이가 아니라 input→output mapping 학습 — physics layer 우회 |
| [`04-code-and-tools.md §1-2`](04-code-and-tools.md) ADCIRC NWS 모드 | PACT 학습 hindcast 가 ADCIRC NWS=12/13/20 출력이면 직접 데이터 파이프라인 가능 (full paper 확인 필요) |
| [`04-code-and-tools.md §8`](04-code-and-tools.md#8-검증-metrics) RMSE/skill | PACT 사용 RMSE/MAE = 본 위키 검증 metric 동일 계열 (Willmott skill score 는 PACT 미사용) |
| [`05-examples.md`](05-examples.md) Maemi·Hinnamnor·Bolaven | PACT 한국 적용 시 검증 case 후보 (단 PACT 자체는 US Northeast 학습) |

## 4. 한국 적용 검토 (탐색 단계, 미실증)

PACT 는 US Northeast 학습/검증. 한국 적용 시 고려사항:

1. **학습 데이터 부재** — 한국 ADCIRC hindcast (KMOU·KIOST 보유, 학회 발표 기준) 활용 가능성. [`04-code-and-tools §7`](04-code-and-tools.md#7-운영-예제--한국-태풍-hindcast-워크플로) 워크플로 결과인 maxele.63 + station-level fort.61 시계열을 학습 셋으로 가공 필요. 한국 학습 셋 표준 데이터 없음 (2026-05-26 기준).
2. **정점** — KHOA 13정점 ([`04-code-and-tools §4.3`](04-code-and-tools.md#43-한국-13-정점-코드)) 후보. 단 KHOA OpenAPI archive 한계 (~1년) — 학습용 long-term observation 은 KHOA Annual Report 등 별도 archive 인용 필요 ([`04-code-and-tools §4.1`](04-code-and-tools.md#41-실시간-조위-관측)).
3. **태풍 typology 차이** — US Northeast 는 extratropical + hurricane 혼재 (winter season trajectory 인용), 한국은 typhoon (서태평양 GAHM) — physics regime 차이로 직접 transfer 효과 unknown.
4. **CMIP6 transfer gap** — PACT 가 명시한 reanalysis→CMIP6 degradation 은 한국 ensemble 평가에도 동일 issue 예상.

→ 한국 ML emulator 별도 학습 후보 (한국 ADCIRC hindcast → PACT 류 fine-tune) 가 현실적 적용 경로.

## 5. 추가 검토 후보 (placeholder — 향후 채워나갈 영역)

본 §는 ML emulator 입문점. 본 위키 추가 ML surge 논문 미트리아지 (2026-05-26 기준). 향후 cataloged 될 후보 카테고리:

- LSTM / sequence model station-level surge (Tiggeloven et al., 미확인)
- Neural operator (DeepONet, FNO) for shallow-water
- PINN (physics-informed) for SWE
- ensemble downscaling surrogate (GCM → local surge)
- Storm-track conditioned emulator (GAHM 입력 → ML surge)

추적: `research/watchlist/` 에 ML emulator author + arxiv cs.LG ∩ physics.ao-ph 카테고리 등록 후보 (현재 미생성).

## 6. 연결

- [`01-concept.md`](01-concept.md) — storm-surge 5 인자
- [`02-theory.md`](02-theory.md) — Pugh §6 + ADCIRC GWCE 식 (PACT 는 풀이 우회)
- [`04-code-and-tools.md`](04-code-and-tools.md) — full hydrodynamic 모델 + KHOA 관측 (PACT 학습 데이터 원천 후보)
- [`05-examples.md`](05-examples.md) — Maemi·Hinnamnor·Bolaven case (한국 검증 후보)
- 외부:
  - PACT arxiv abs: <https://arxiv.org/abs/2605.09036>
  - PACT PDF: <https://arxiv.org/pdf/2605.09036v1>
