---
title: "SWAN 최근 연구동향 2023-2026 — ST6 보급·ML 하이브리드·data assimilation·TC coupling·기후 downscaling"
topic: swan
canonical_source: external
external_source: "SWAN 2023-2026 응용연구 survey. 정량 인용분 4편은 출판본 전문 직독(2026-07-19): JMSE 14(5):435 / Frontiers Mar. Sci. 2023:1298727 / JMSE 13(6):1196 / JMSE 13(9):1612. 나머지 항목은 서지 수준 포인터."
citation_status: verified
has_source_needed: true
verification_method: "★2026-07-19 전면 재검증. **오픈액세스 4편 전문 직독**(MDPI·Frontiers 는 결제벽 아님 — Cloudflare 봇차단이었고 reader 프록시로 전문 수신; 2026-06-02 판의 'paywall' 진단은 오진). DOI 6건 Crossref API 실조회로 실재·제목 일치 확인(jmse14050435·jmse13091612·jmse13061196·jmse13081450·fmars.2023.1298727·2021MS002493). ★2026-06-02 판의 정량 서술 중 **JMSE 14(5):435 항목은 논문 결론과 반대**였음 — 본문 §1.1 정정 기록 참조. 전문 미확보 항목(ScienceDirect·Ocean Dynamics·USGS 등)은 §6 에 서지 포인터로만 격리하고 정량 단언 제거."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-02
verification_by: "Claude Fable 5 — 오픈액세스 전문 직독 + Crossref DOI 대조"
verification_date: 2026-07-19
related:
  - models/SWAN/web-refs/swan-foundational-papers.md
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
---

# SWAN 최근 연구동향 2023-2026

> SWAN 의 코드/이론은 [[swan-documentation-stack]] (v41.51)에 고정; 본 노트는 **응용·결합·calibration 연구동향**. 원논문은 [[swan-foundational-papers]].
> **§1~§4 = 출판본 전문 직독 verified. §6 = 서지 포인터만(정량 단언 없음).**

## 1. ST6 physics 보급 + calibration (vs Komen default)

swantech §2.3.3 의 ST6([[swan-tech-ch2-dissipation-detailed]] §4).

### 1.1 ★한국 연안 1년 민감도 실험 — ST6 는 **기본설정에서 Komen 에 졌다** (verified, 전문 직독)

**"A Study on Enhancing the Accuracy of Wave Prediction Models Through SWAN Sensitivity Experiments: Focusing on Wind Input and Whitecapping Dissipation"**, *JMSE* **14**(5), 435 (2026). doi:`10.3390/jmse14050435`

- 설정: **2021년 1년 전기간**, 한국 전 연안(KMA 파랑부이 55 + 해양관측부이 36 등 — 동해·남해 도서·서해 포함), 시간간격 10분. **강제풍 = JMA-MSM 5 km**.
- 전 케이스 전파고 상관 **R ≈ 0.91**.
- **고파(Hs > 2 m) 기본설정 결과** (Table 6):

| 케이스 | 조합 | RMSE (Hs>2m) | Bias |
|---|---|---:|---:|
| **K-5** | Komen whitecapping + **Zijlema** drag | **0.42 m** ← 기본설정 최우수 | 0.03 |
| **S-7** | **ST6 기본** | **0.52 m** | 0.19 |

- ST6 기본이 뒤진 사유(저자): 기본 파라미터가 **JMA-MSM 풍장 특성과 정합되지 않음**. `U10,proxy` 를 28·32·35 로 바꾼 민감도(S-1~S-3)는 평균정확도 유의차 없음 → **풍입력 편차 보정이 선결**.
- **CDFAC(시변 drag 계수 스케일링) 풍편차 보정 후**(Table 7): ST6 **0.52 → 0.35 m**(bias 0.19→0.16), Komen 은 **0.42 → 0.39 m** 로 소폭. → **ST6+CDFAC(0.35) 가 최종 최우수**, 단 **보정을 붙였을 때만**.
- **파고대별 역전**(§5.3): **Hs < 1.0 m 에서는 KOMEN 이 우세**(정상해황 최적화 이력), Hs 1.0~1.2 m 부터 ST6 우위 전환, **2.0 m 초과 시 Komen RMSE 급상승**.
- ⚠ **저자 자신의 한계 공시(§5.2.3)**: CDFAC 는 **hindcast mode** — 2021 관측에서 유도한 계수를 **같은 2021 기간에 적용**한 **순환검증(circular validation)**. 저자는 이를 "운영 예보성능이 아니라 **풍입력 오차가 통제됐을 때의 잠재정확도(Potential Accuracy)**"로 해석할 것을 명시. 운영 적용엔 split-sample 교차검증 필요.
- ★**JMA-MSM 편차 구조 진단**(§5.2.1): 서해·남해 정점에서 MSM 풍속 **양의 편차** — **리아스 해안 + 다도해**의 불규칙한 국지 조도를 **5 km 해상도가 못 풀어** 해면을 실제보다 매끄럽게 인식 → 풍속 과대 → 천해 굴절·저면마찰과 결합해 파랑오차 증폭. CDFAC 는 이 구조적 편차를 전역 스케일링으로 상쇄.

> ★**2026-06-02 판 정정 기록**: 구판은 이 논문을 "한국 **동해안 겨울폭풍파**, **ST6 default 가 최우수**: ME 0.052 / RMSE 0.342 / SI 0.129 / R 0.964"로 요약했으나 **전 항목이 원문과 불일치** — ⓐ대상은 동해안 한정·겨울 한정이 아니라 **전 연안 1년**, ⓑ ST6 기본은 **최우수가 아니라 열위**(0.52 vs K-5 0.42), ⓒ 인용 4수치(0.052/0.342/0.129/0.964)는 **원문에 존재하지 않음**(원문 R≈0.91). 검색 스니펫 기반 서술의 위험을 보여주는 사례로 기록 보존.

### 1.2 whitecapping 계수 최적화 일반법 (verified, 전문 직독)

**"A general method to determine the optimal whitecapping dissipation coefficient in the SWAN model"**, *Frontiers in Marine Science* (2023). doi:`10.3389/fmars.2023.1298727`

- 문제의식: `Cds` 를 관행적으로 **시행착오(trial and error)** 로 정하는 실태.
- 이론 결과: **최적 `Cds` 는 적용 풍장과 일대일 대응**. 고품질 풍장 조건에서는 **도메인·기간과 무관하게 최적 `Cds` 가 좁은 범위**에 수렴.
- 실험: 남중국해(SCS)에서 풍입력 2종(**ST6·YAN**) × whitecapping 3종(**KOMEN·JANSSEN·WST**). 각 whitecapping 스킴별 최적 `Cds` 범위 도출 — **최적범위 값이 SWAN 기본 `Cds` 를 일관되게 상회**. 멕시코만·지중해로 이식해 적용성 검증.
- → §1.1 의 한국 사례(ST6 기본이 MSM 풍장과 부정합)와 **같은 진단**: 계수 기본값은 풍장에 종속적이며 무조건 이식 불가.

### 1.3 기타

- **Liu Q et al. (2021)**, "Global Wave Hindcasts Using the Observation-Based Source Terms (ST6): Description and Validation", *JAMES*. doi:`10.1029/2021MS002493` — ST6 전지구 hindcast 검증. (Crossref 서지 확인, 전문 미독)

## 2. ML/DL 하이브리드 SWH 예측 (SWAN 데이터 학습)

> **상세는 [[swan-ml-surrogate-models]] 별도** (surrogate DELWAVE/DeepONet/FNO/GNN + forecasting transformer/LSTM + hybrid PINO + review).

### 2.1 태풍 시 단기예측 — LSTM vs RF (verified, 전문 직독)

**"Machine Learning-Based Short-Term Forecasting of Significant Wave Height During Typhoons Using SWAN Data: Pearl River Estuary"**, *JMSE* **13**(9), 1612 (2025). doi:`10.3390/jmse13091612`

- 학습데이터: **SWAN 모의 출력**, **역사 태풍 87개**. 독립시험용 **대표 태풍 10개** 유보.
- **3시간 예보**: **LSTM > RF** — 평균 RMSE 낮고 R² 높음, 특히 **고동적 조건의 파랑 peak 포착**에서 우위.
- ★**6시간 예보에서 역전 부분 발생**: 양 모델 정확도 저하, **안정 시나리오에서는 RF 가 근소 우위**, 복잡한 파랑 발달에서는 LSTM 이 더 반응적. (구판의 "LSTM > RF" 단순 서술은 3h 한정)
- 인근 3개 정점 일반화 시험: 양 모델(특히 LSTM) 학습지점 밖에서도 예측력 유지.
- 저자 제시 개선방향: 풍장 예측인자 통합, 모델 갱신 전략, 앙상블 기상자료.

### 2.2 기타 (서지 포인터, 정량 미검증)

- "Enhancing significant wave height prediction based on numerical SWAN and Crossformer models with adaptive decomposition", *Expert Systems with Applications* (2025). [S0957417425021426] — SWAN + Crossformer.
- Self-Attention ConvLSTM 기반 regional SWH 예측 / Durap (2025a/2025b) XAI 하이브리드.
- 동향: SWAN 이 **고품질 학습 데이터 생성기** 역할(특히 태풍·극한), DL 이 단기 forecast 가속·peak 보정.

## 3. Data assimilation (서지 포인터, 정량 미검증)

- "Estimating Coastal Winds by Assimilating High-Frequency Radar Spectrum Data in SWAN" (PMC8659604) — HF radar spectrum → SWAN wind 추정.
- "Application of SWAN model for wave forecasting in the southern Baltic Sea supplemented with measurement and satellite data", *Environmental Modelling & Software* (2023). [S1364815223000105]
- 동향: wide-area(위성) + local(HF radar/buoy) assimilation 으로 wind/wave BC 개선.

## 4. Regional 응용 + 기후 downscaling

### 4.1 동중국해 15년 고해상 재현 (verified, 전문 직독)

**"Regional Wave Analysis in the East China Sea Based on the SWAN Model"**, *JMSE* **13**(6), 1196 (2025). doi:`10.3390/jmse13061196`

- 설정: **ERA5 풍장 + ETOPO1 수심**, **0.05° × 0.05°**, 영역 **25–35°N / 120–130°E**, 기간 **2009–2023**(15년).
- ★**스킴 비교 결론 — 천해에서는 Komen·Collins 조합이 최적**: whitecapping **Komen** + 저면마찰 **Collins** 조합이 위성 관측 대비 평균 **RMSE 0.374 m / 0.369 m**, whitecapping 대안 **Westhuysen** 및 저면마찰 대안 **Jonswap·Madsen** 보다 우수.
- 월평균 유의파고 **0–3 m**, **가을·겨울 > 봄·여름**, **북서→남동 증가** 경향. 쿠로시오 영향 언급.
- → §1.1 과 합쳐 보면 **"ST6/신형 스킴이 항상 우세"는 성립하지 않음** — 천해·중간파고대에서는 Komen 계열이 견고.

### 4.2 기타 (서지 포인터, 정량 미검증)

- "On the capability of SWAN model for South Atlantic Ocean wave simulation", *Ocean Dynamics* **75**:51 (2025).
- "Dynamically downscaled future wave projections ... main Hawaiian Islands" (USGS Science Data Catalog).
- "Assessing the impact of wave model calibration in the uncertainty of wave energy estimation", *Renewable Energy* (2023). [S0960148123006729]

## 5. Tropical cyclone wave-surge coupling

- **"Numeric Modeling of Sea Surface Wave Using WAVEWATCH-III and SWAN During Tropical Cyclones: An Overview"**, *JMSE* **13**(8), 1450 (2025). doi:`10.3390/jmse13081450` — Crossref 서지 확인(전문 미독).
- "An efficient early warning system for typhoon storm surge based on time-varying advisories by coupled ADCIRC and SWAN", *Ocean Dynamics* (2015) — 본 위키 [[swan-unstructured-time-step]] 결합과 연결.
- 동향: **unstructured SWAN+ADCIRC**(단일 mesh wave+surge), WW3(대양)→SWAN(연안) nesting, time-varying advisory 운영. ADCIRC `adcirc-swan-coupling`(PR #498 SWANTimeControl) 관련.

## 6. 핵심 동향 요약

| 동향 | 키워드 | 본 위키 연결 |
|---|---|---|
| ST6 보급 | 관측기반 source. ★**기본값 무조건 우위 아님** — 풍장 정합·파고대 의존 | [[swan-tech-ch2-dissipation-detailed]] §4 / [[swan-st6-babanin-implementation]] |
| 계수 보정 | `Cds` ↔ 풍장 일대일 대응, 기본값 상회 최적범위 존재 | §1.2 |
| ML 하이브리드 | LSTM/RF/Crossformer/ConvLSTM/XAI, SWAN=학습데이터 | [[swan-ml-surrogate-models]] |
| Data assimilation | HF radar·위성, wind/wave BC | (신규) |
| 기후 downscaling | ERA5+고해상, wave energy, projection | §4.1 |
| TC coupling | SWAN+ADCIRC unstructured, WW3 nesting | [[swan-unstructured-time-step]] / ADCIRC swan-coupling |
| wind drag | sea-state/WBLM, 고차 C_D, ★CDFAC 시변 스케일링 | [[swan-tech-ch2-sources-sinks]] (Zijlema 2012 C_D) |

## 7. 한계 (disclosed)

- **§2.2·§3·§4.2·§5 항목은 전문 미확보** — 서지 포인터일 뿐 **정량 단언 없음** `[source-needed]`. ScienceDirect(Elsevier)·Ocean Dynamics(Springer)는 실제 결제벽. 필요 시 원문 조달 후 개별 승격.
- 2026 상반기 논문 일부만 포착(2026-06 검색 기준).
- ★**방법론 교훈**: 구판은 MDPI·Frontiers 를 "paywall"로 오진해 전 노트를 `source-needed` 로 두었고, 그 사이 **검색 스니펫 기반 정량값이 원문과 반대로 기재**된 채 잔존했다(§1.1 정정 기록). **오픈액세스 여부를 먼저 판정하고, 정량값은 전문 확인 전까지 기재하지 않는다**가 옳은 순서.

## 8. 연결

- [[swan-foundational-papers]] — 원논문 (ST6 Rogers/Zieger, QC Smit-Janssen/Akrish 등)
- [[swan-documentation-stack]] — SWAN v41.51 공식 docs
- [[swan-tech-ch2-dissipation-detailed]] — ST6 물리 (§2.3.3 §4)
- [[swan-unstructured-time-step]] — SWAN+ADCIRC 결합 (TC coupling)
