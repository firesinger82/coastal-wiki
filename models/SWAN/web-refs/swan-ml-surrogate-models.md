---
title: "SWAN ML/surrogate 모델 — DELWAVE·DeepONet·FNO·GNN emulator + transformer/LSTM forecasting (2020-2026)"
topic: swan
canonical_source: external
external_source: "WebSearch + arxiv/GMD/저널 landing-page fetch (2026-06-02) → 핵심 3편 full-PDF 격상 (2026-07-03). 핵심 직접확인: DELWAVE 1.0 (Mlakar 2024 GMD 17:4705-4725 open-access, PDF 21p full read), DeepONet SWAN surrogate (Cai et al. 2026 arxiv:2604.06433 Dawson 그룹, PDF 46p full read), review (Ferdaus et al. 2025 arxiv:2511.21856, PDF 38p full read)."
citation_status: verified
verification_method: "full-PDF 직접 read(2026-07-03, 사용자 지시 'surrogate full-PDF 격상 우선'): ① DELWAVE gmd-17-4705-2024.pdf 전 21p — 아키텍처(Fig 4-7)·입력텐서(Eq 2-10)·ablation(Table 1)·storm precision/recall(Fig 13)·기후신호(§5.3) 본문 확인. ② DeepONet arxiv 2604.06433v1 전 46p — operator 정식화(Eq 2-6)·hyperparam(Table 1 Optuna)·1-D/2-D/DUCK 결과(Table 2-7)·0.04s vs 30s 가속(§5.3)·radiation stress 부록(Eq A.2-A.7) 확인. ③ Ferdaus arxiv 2511.21856v1 전 38p — Table 1-8·모델선택 가이드(§3.8)·critical analysis(DIA/whitecapping/γ)·HPC 벤치(§6)·ML(§3.10·§7.6) 확인, 구버전 노트의 'SWAN=cornerstone' 인용은 phase-averaged 클래스 지칭으로 정정. ④ 추가 arXiv 2편(2026-07-03 2차): FNO CoastalTwin 2110.07100 전 6p(NEMO SSH surrogate 로 분류 정정, 45× 실체 확인)·PINO 2508.03315 전 13p(위상해상 HOSM 재구성으로 분류 정정, physics-in-loss·SSP·실시간 확인) — arXiv 가용분 소진. WebSearch snippet(abstract-level) 잔존: A.3 GNN/CNN·B forecasting·C physics-guided — 전부 paywall, 정량값 snippet 기반(원문 확인 시 보정)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-02 (초판) / 2026-07-03 (full-PDF 격상)
verification_by: "Claude Opus 4.8 (1M context) — full-PDF read(DELWAVE 21p/DeepONet 46p/Ferdaus 38p) + WebSearch"
verification_date: 2026-07-03
related:
  - models/SWAN/web-refs/swan-recent-research-2024-2026.md
  - concepts/storm-surge/07-ml-emulators.md
  - models/SWAN/manual-notes/swan-unstructured-time-step.md
  - models/SWAN/web-refs/swan-foundational-papers.md
---

# SWAN ML/surrogate 모델 (2020-2026)

> WebSearch+fetch survey (2026-06-02). SWAN 의 **ML 대체/가속** 연구 — (A) surrogate/emulator (SWAN 대체) (B) forecasting (SWAN 데이터 시계열) (C) hybrid/physics-guided (D) downscaling. storm-surge 의 [[07-ml-emulators]] (PACT/StormNet, surge)와 wave 측 대응. ⚠ 직접확인(DELWAVE/DeepONet/review) 외 정량값은 abstract-level.

## A. Surrogate / emulator (SWAN 직접 대체)

### A.1 DELWAVE 1.0 — CNN point emulator ★ (verified, PDF 21p full read 2026-07-03)

- **Mlakar P, Ricchi A, Carniel S, Bonaldo D, Ličer M (2024)**, "DELWAVE 1.0: deep learning surrogate model of surface wave climate in the Adriatic Basin", *Geosci. Model Dev.* **17**, 4705-4725. doi:10.5194/gmd-17-4705-2024 (open-access CC-BY 4.0, model description paper, published 2024-06-17)
- **Abstract (verbatim)**: "We propose a new point-prediction model, the **DEep Learning WAVe Emulating model (DELWAVE)**, which successfully emulates the behaviour of a numerical surface ocean wave model (Simulating WAves Nearshore, SWAN) at a **sparse set of locations**, thus enabling numerically cheap large-ensemble prediction over synoptic to climate timescales."
- **타깃 SWAN 구성 (§2.2)**: 비정상 action balance (Booij 1999 Eq 1 인용), 직교 곡선격자 북부 ~2 km → 남동 8-10 km, Otranto 해협 개방경계 calm 처리, **25 log 주파수 0.05-0.5 Hz × 36 방향**, Δt=360 s. 강제력 = COSMO-CLM 0.0715°(~8 km, 224×230, CMCC-CM GCM, 6-hourly) CTR 1971-2000 / **SCE RCP8.5 2071-2100** (SLR +0.70 m 균일 반영, Antonioli 2017). Adriatic **6 정점**: AA(Acqua Alta)·GD(Grado)·OB·OB2·OB3·MB(Monopoli). 학습=CTR(80/20 train/valid), 시험=SCE.
- **입력 텐서 (§3.1, Eq 2-10)**: `[11, 4, 90, 89]` = 11 time step(현재+선행 10; 심해분산 c_f=(gλ/2π)^½·λ≈40 m로 swell 이 분지 종단 1-1.5 d 횡단 → 반올림 10) × 4 필드(u·v 바람 + **Gaussian location encoding**(sparse 행렬, ς²=20 ≈ 0.45°, Eq 4-5) + **linear grid encoding**(Eq 7 — convolution 의 병진 불변성을 깨서 **fetch(바람패턴↔타깃 상대위치)** 를 학습 가능케 함)).
- **구조 (§3.2, Fig 4-7)**: ① atmospheric encoder — per-input(Conv2d k3 f64 SiLU+MaxPool+residual) → **joint encoder(시간步 간 가중치 공유** 3×블록; 동일 바람패턴 검출기 재사용+과적합 억제) → output(1×1 conv f256, 步별 256-d 기상 descriptor) ② temporal collapse(Conv1d ×2 → 단일 256-d) ③ regression(dropout 0.2+Linear256+SiLU skip ×3 → Linear 3출력 **SWH·MWP·MWD**).
- **학습 (§3.3)**: loss=RMSE(Eq 6), ln(SWH+1) 변환+표준화, **random importance sampling**(격배치 교대; 전체 표본 중 Hs>2 m 는 5% 뿐 → 꼬리 보강, SWH 오분류 2× 벌점), Adam lr 1e-3·wd 1e-6 2일(Vega cluster) + lr 1e-5 600 epoch 재학습 = **총 ~2.5일 학습, 추론 >100 wind field/s**.
- **Temporal ablation (§4, Table 1)**: DELWAVE₂/₄/₈/₁₁/₁₆ 비교 → **DELWAVE₁₁ 최적**(9케이스 중 4 최저 RMS), 11步 초과는 diminishing returns.
- **성능 (§5.1, 2071-2100 SWAN 대비)**: **Hs MAE 5-10 cm**(Hs<1 m 에서 <5 cm, >3 m 에서 10-15 cm) / **방향 MAE 10-25°**(지배풍향 bin 최소, 0°/360° 구분 인공오차) / **주기 MAE 0.2 s**(<6 s 구간 <0.25 s; AA 는 >8 s 에서 ~1 s — **Scirocco 원거리 swell**: AA 파장(場)이 남아드리아 비국지 바람으로 결정되는 구조 한계, wave power P=ρg²Hs²T_m-1,0/64π(Eq 13) 분석으로 저에너지 랜덤 해면에 오차 집중 확인 → 실무 영향 제한).
- **Storm 분석 (§5.2, Boccotti 2000 기준: Hs>1.5·평균, <10 h 병합, <12 h 폐기)**: 전체 storm **precision=recall 0.97-0.98**(AA/OB/MB); **연최대(annual maxima)만은 0.83-0.93** — peak Hs 미세오차가 연최대 순위를 뒤바꾸는 전파효과(§5.2 해석), storm 자체 분류 실패 아님.
- **기후신호 (§5.3)**: 99th percentile **≤5% 계통적 과소** 외 기후통계 일치. **surrogate 노이즈 ≪ SCE-CTR 기후변화 신호** — Bora(NE) 약화·Scirocco(SE) 강화 방향성(Bonaldo 2020) DELWAVE 가 재현.
- **한계·전망 (§6)**: 학습 정점 밖 위치 예측 불가(Gaussian encoding 일반화 = open question), physics-informed ML·지중해 확장 후속. 코드 <https://github.com/petermlakar/DELWAVE> (zenodo 10.5281/zenodo.10990866, 전처리 데이터 10.5281/zenodo.7816888).
- **의의**: numerically cheap **large-ensemble climate projection** (point prediction). SWAN 의 climate downscaling 가속.

### A.2 DeepONet — operator-learning surrogate (ADCIRC 결합 동기) ★ (verified, PDF 46p full read 2026-07-03)

- **Cai S, Dutta S, Loveland M, Valseth E, Rivera-Casillas P, Trahan C, Dawson C (2026)**, "Operator Learning for Surrogate Modeling of Wave-Induced Forces from Sea Surface Waves", arxiv:**2604.06433**v1 (2026-04-07, physics.comp-ph). **Oden Institute UT Austin(Dawson) + 미 육군 ERDC**(Loveland·Rivera-Casillas·Trahan) + NMBU/Simula(Valseth). DOE DE-SC0022211 + ERDC BAA W912HZ-23-2-0013 지원, TACC Frontera 계산.
- **동기 (§1-2)**: wave-induced surge 성분이 storm 총수위의 **10-30%**(Causio et al. 인용). SWAN+ADCIRC·SCHISM+WWM3 coupling 에서 **radiation stress gradient 가 ADCIRC GWCE/운동량식의 추가 강제항** — 매 coupling step 마다 고차원 spectral 문제(SWAN)를 푸는 비용 → wave 를 순환모델보다 **coarse temporal 로 돌리는 관행**을 DeepONet 으로 대체.
- **정식화 (Eq 2-6)**: SWAN 정상상태 solution operator 𝒢_S: (N_bnd, U₁₀) ↦ N(σ,θ,x,y) 를 학습. **branch** 입력 u=[Uₓ, U_y, H_bnd, cos θ_bnd, sin θ_bnd](시나리오 강제력), **trunk** 입력 (x,y)(임의 좌표) → q̂(x)=Σᵢ₌₁ᵖ bᵢ(u)tᵢ(x). 시나리오당 공간좌표 **~5%만 표집** 학습. **이산화 불변** — 학습 mesh 에 없는 위치도 예측 가능(CNN/LSTM 대비 핵심 이점).
- **Hyperparam (Table 1, Optuna 100 trial×3000 epoch, 1-D 케이스로 1회만)**: Hsig 모델 lr 1e-3·batch 256·p=20·branch 4층×16(elu)·trunk 5층×96(ReLU) / Forces 모델 lr 1e-4·batch 64·p=30·branch 4층×128(LeakyReLU)·trunk 5층×96(tanh).
- **QC**: SWAN 수렴판정(relative change+curvature, wet 격자점 99.5%) 미달·50 iteration 초과 시나리오는 데이터셋 제외.
- **3 케이스 결과 (전부 JONSWAP 경계, 70-15-15 분할)**:

| 케이스 | 도메인·시나리오 | Hsig RLE | x-force RLE | y-force RLE |
|---|---|---|---|---|
| **1-D** | 40 m→0/38 km 균일사면, 2401건(풍속 11-17·±7°·H 0.6-1.2 m·Tp 3.5 s) | 0.1-0.4% (max **0.72%**) | 대다수 <5% (max **6.41%**) | — |
| **2-D** | 38×40 km 평면사면, 1650/344/345(풍속 14-20·방향 -70~75°·H 0.4-1.0 m) | 0.2-0.6% (max **1.23%**) | 1.5-3% (max **8.78%**) | 2.5-4% (max **8.74%**; 풍향 0° 케이스는 SWAN y-force 자체가 수치노이즈라 제외) |
| **DUCK** | FRF Duck NC 실지형(**ONR Test Bed F71** + DELILAH 실측 연계), 3840→2688/576/576(풍속 1-8 m/s·nautical 0-315°·H 1.6-2.6 m·Tp 10.718 s·수위 +0.11 m·측면경계 Hs 1.63 m/10.5 s/88°/22°) | 대다수 <1% (max **1.91%**) | 2-5% (max **10.98%**) | 대다수 <3.5% (max **6.88%**) |

- **오차 국재화 (§5.2)**: 최대오차는 일관되게 **surf-zone(천수화·쇄파 급경사역)과 외해 경계** — 물리적 감도가 큰 곳에 정합(무작위 아님). DeepONet 은 SWAN 출력의 고주파 radiation-stress "spike"(소규모 지형·이산화 인공물 유래)를 **스무딩**(spectral bias) — 저자들은 이것이 오히려 **고주파 수치노이즈에 민감한 순환모델에 더 안정적인 강제력**일 수 있다고 논증.
- **가속 (§5.3)**: 시나리오당 **~0.04 s vs SWAN ~30 s ≈ 3 orders of magnitude** — 대규모 ensemble·운영 wave-current coupling 직결.
- **한계 (§5.4)**: bulk 량(Hsig·force gradient)만, **full action density spectrum 미예측**; 균일 바람장 한정. 코드 <https://github.com/ShukaiC/NeuralOperator-CoastalWaves> (출판 시), 데이터 DesignSafe.
- **위키 정합**: 부록 radiation stress 식(Eq A.4-A.6 S_xx/S_yy/S_xy, Hsig=4√∬E A.7)은 swantech Eq 3.59-61·swanuse Appendix A 정의([[../manual-notes/swan-tech-ch3-qc-curvilinear]]·[[../manual-notes/swan-output-variable-definitions]])와 동일.
- **의의**: **Clint Dawson 그룹(ADCIRC)** — SWAN+ADCIRC coupling([[swan-unstructured-time-step]] Casey Dietrich 41.20)의 **wave 측 surrogate**. Surge 측 PACT([[07-ml-emulators]])와 대칭. Coupled wall-clock 절감 (wave 를 coarse temporal 대신 DeepONet).

### A.3 FNO / GNN / CNN surrogate (일부 full-PDF 격상 2026-07-03)

- **FNO CoastalTwin — Jiang et al. 2021** (arxiv:2110.07100, FDL: PNNL·DLR·MIT·IBM·NASA·USGS, 6p 워크숍) ★PDF: ⚠ **분류 정정 — SWAN 아닌 NEMO(순환모델) SSH surrogate**. NW유럽 7 km 520×292, 강제력 MSLP·U10·V10(ERA5 downscaled)+GEBCO(특수 log 스케일링 B′=(ln(B+50)−ln50)/ln100), 2020년 전체 @5 min, 11개월 학습/4월 시험. FNO(linear 20ch + Fourier층 5개(20ch·40 modes)+linear)가 UNet 을 4케이스 전부 압도 — **MSE 0.0011 vs 0.0025, 1-SSIM 0.2283 vs 0.4178**(Table 1, Case 1) — ★구판의 "CORR 0.91 vs 0.75"는 **원문 부재 수치라 삭제**(2026-07-19 전문 재대조: CORR 은 §2.3 에 지표로 정의되고 Fig 3 공간상관 *지도*로만 제시, 수치 표 없음). **45× = 1개월 에뮬 ~2 min vs NEMO ~1.5 hr(단일 2.6 GHz 코어)** — GPU 병렬화 시 추가 가속 여지 명시. 약점 = **육지 마스크 경계 부근 열화**(佛-西 동측·영국 연안, coastal modeling 공통 이슈로 지목). 플랫폼 CoastalTwin(gitlab, 출판 시 공개).
- **GNN + polynomial regression 초해상** — ★**2026-07-19 서지 오귀속 정정 + 전문 확보 verified**: **Kuehn J, Abadie S, Delpey M, Roeber V (2024)**, "Super-resolution on unstructured coastal wave computations with graph neural networks and polynomial regressions", *Coastal Engineering* **194**, 104619, doi:10.1016/j.coastaleng.2024.104619. **OA 전문**(HAL hal-04704696). 
  - ⚠ 구판이 붙인 PII `S1463500323000963` 은 **전혀 다른 논문** — Zhu X, Wu K, Huang W (2023), "Deep learning approach for downscaling of significant wave height data from wave models", *Ocean Modelling* **185**, 102257 (**CNN 초해상**이며 GNN·ridge regression 미등장). 즉 *수치는 맞고 서지가 틀린* 형태(swan-recent-research 건과 정반대 방향의 같은 계열 실패).
  - 정량(원문 대조): RMSE **0.3~2 cm** — 단 이는 **polynomial regression(PR)** 값. 가속은 **30~80배**(Table 6: PR 81/62/30, GN 70/55/28) — "80×"는 Region 1·PR 단일 최량치.
  - ★원문 highlight: "**Polynomial regressions outperform graph neural networks in most cases**" — 우열 방향이 구판에 누락돼 있었음.
- **CNN regional wind-wave surrogate** — 서지 확정(2026-07-19 Crossref): **Huang et al. (2022)**, *Applied Ocean Research* **126**, 103287, doi:10.1016/j.apor.2022.103287 — 본문 abstract-level(Elsevier 결제벽) `[source-needed]`.
- **PINO — Ehlers·Stender·Hoffmann 2025** (arxiv:2508.03315, TU Hamburg·TU Berlin·Imperial, 13p) ★PDF: ⚠ **분류 정정 — SWAN surrogate 아닌 위상해상(phase-resolved) 파면 재구성 = 데이터 동화 문제**(HOSM/포텐셜류 영역). 희소 계측(부이 5기 case A / X-band 레이더 snapshot+교정부이 1기 case B)에서 η̃·Φ̃ˢ 시공간 전장 복원 — **ground truth 파면 없이 학습**: 자유표면 경계조건(Zakharov form Eq 1-2) 잔차를 loss 에 내장(ℒ_sensor+ℒ_phy,1+ℒ_phy,2+0.25ℒ_reg, HOSM 4차 Taylor 로 Φˢ·W 근사, Fourier 미분+Tukey 창). 아키텍처 = FNO 기반 3층·128 modes·latent 32(부이)/64(레이더), AdamW·RTX3090. HOSM 합성검증(JONSWAP TMA γ=3.3, L_p 100-200 m, ε 0.02-0.13, 1953 m×100 s): **SSP 0.1035(부이)/0.1341(레이더)**, 복원 **0.014 s/샘플 = 실시간**, 지도학습 FNO 대비 **학습데이터 ⅓**. 레이더는 tilt·shadowing 변조 명시 모델링(Eq 8-9), 고 ε 일수록 shadowing 정보손실로 오차↑(물리적 원인, 기법 한계 아님). 한계 = **1D+t 장파봉 한정**(2D+t 후속). DFG rogue-wave 과제, ChatGPT 문법교정 공개.

### A.4 Wave hydrodynamics surrogate on evolving landscapes ★ (verified, PDF read 2026-06-12)

- **Gharehtoragh & Johnson 2026** (arxiv:2510.12986, **Purdue Univ**) — TC 앙상블 × **진화하는 landscape**(제방·해벽 유무·SLR·지반침하·식생손실 시나리오)에서 **SWAN** 의 유의파고 Hs 를 대체하는 deep-learning surrogate.
- **아키텍처**: CNN(여러 convolutional + pooling + dropout + ReLU) → multiple dense layers. 입력 특징 = landscape 형태요소 + TC 인자 + **surge surrogate 출력을 입력 feature 로 사용**(surge→wave 결합).
- **정량**: SWAN 대비 surrogate 예측이 grid cell·landscape 의 **~89%** 에서 two-sided equivalence test 통과, 평균 **RMSE 0.05–0.06 m**.
- **응용**: 제방·floodwall **wave overtopping** 기여를 저비용 산출 → budget-constrained probabilistic flood risk 계획.
- 동일 **Johnson group 의 surge 측 regional surrogate**(arxiv:2511.07269, [[../../../concepts/storm-surge/07-ml-emulators]] §7.4)와 **wave↔surge 대칭 + surge→wave 입력 연쇄** = 차세대 **coupled ML emulation** 의 구체 사례.

## B. Forecasting (SWAN/WW3 데이터 → 시계열 DL)

- **Crossformer + SWAN** adaptive decomposition Hs (*Expert Systems with Applications* 2025, S0957417425021426) — [[swan-recent-research-2024-2026]] §2
- **LSTM > Random Forest — 단 3h 한정** (Pearl River, 87 typhoon SWAN, *JMSE* 13(9):1612, doi:10.3390/jmse13091612) — ✅**전문 직독 verified 2026-07-19**: 3h 예보는 LSTM 이 RMSE↓·R²↑(특히 peak 포착), ★**6h 에서는 안정 시나리오 한정 RF 가 근소 우위**·LSTM 은 복잡 발달에 더 반응적. 대표 태풍 10개 독립시험 유보, 인근 3정점 일반화 유지. 상세 [[swan-recent-research-2024-2026]] §2.1
- ⚠ **Swin transformer-LSTM**(중국 연변해, 재분석 구동)·**Self-Attention ConvLSTM** regional Hs — ★**저자·연도·저널·DOI 전무 = 식별 불가 항목**(2026-07-19 감사 적발). 절대규칙 #1(무출처 단언 금지) 저촉이므로 **서지 확정 전까지 인용 금지** `[source-needed]`.
- **SWRL Net** (*Weather and Forecasting* 35(6), 2020) — spectral residual DL 로 short-term wave forecast 개선 (numerical 위 residual correction)
- **ANN port wave forecast** (WW3 기반, *Ocean Eng* S0029801822008496)

## C. Hybrid / physics-guided

- **Physics-guided DL** skillful wind-wave (PMC11616684) — 물리 제약 결합
- **WW3 + ML hindcast 개선** (*Coastal Eng* S0378383923001059) — numerical hindcast 의 ML 보정
- **XAI (Durap 2025a/b)** — explainable, feature engineering ([[swan-recent-research-2024-2026]] §2)

## D. Review / 종합 (verified, PDF 38p full read 2026-07-03)

- **Ferdaus MM, Cooper NA, Schmidt AB, Pokhrel P, Ioup E, Abdelguerfi M, Simeonov J (2025)**, "A Comprehensive Review of Phase-Averaged and Phase-Resolving Wave Models for Coastal Modeling Applications", arxiv:**2511.21856**v1 (2025-11-26, physics.ao-ph, **38p**). Univ. of New Orleans + **미 해군 NRL Stennis**(계약 N00173-20-2-C007). ⚠ provenance: 저자들이 **Writefull(생성형 AI) 영어교정 사용을 명시 공개**(내용 책임은 저자).
- **범위**: phase-averaged 5종(SWAN·WAVEWATCH III·WAM·MIKE 21 SW·TOMAWAC) vs phase-resolving(FUNWAVE-TVD·SWASH·COULWAVE·NHWAVE·BOSZ) — 정식화(§4 WABE Eq 8-11·source term Eq 12-17·Boussinesq Eq 18-21·비정수압 Eq 23-25)·수치기법(§4.5-4.9)·정량검증(§5 Table 6-7)·HPC(§6 Table 8)·모델선택 가이드(§3.8).
- **인용 정정 (full read)**: 초판 노트의 "SWAN = cornerstone" 은 부정확 — 원문 §3.5 는 "**Phase-averaged spectral wave models** are the cornerstone of operational wave forecasting"(클래스 지칭). SWAN 개별 서술(§3.5.1)은 "third-generation... specifically designed for coastal regions, estuaries, and lakes... comprehensive representation of shallow-water physics... **fully implicit** time integration... particularly efficient for **steady-state** simulations".
- **SWAN 위치 (Table 2·4, §3.8)**: 상대비용 **baseline 1.0**(100 km²·500 m·24 h 기준) — phase-resolving 은 **10-200×**. 격자 0.1-5 km·Δt 10-60 min·적용수심 h<200 m·OpenMP+제한적 MPI. 강점=천해물리(triads·breaking·friction)+유연 격자+오픈소스 대형 커뮤니티 / 한계=**회절 표현 제한·대규모 시간의존 문제에서 implicit solver 느림·외해 부적합**. 권고영역: 10 km² 미만~10³ km² 연안, coastal engineering design 1순위.
- **정량 팩트 (SWAN 관련)**: ST6 가 hurricane 조건 유의파고 오차 **15-25% 감소**(선행 파라미터화 대비) / 비구조 격자 = 구조 대비 비용 **5-10× 절감** / SWAN 확장성 = DD 로 **9,000+ core**(Dietrich et al. 2012 인용) 단 소도메인에서 20 thread 초과 시 역효과(Rautenbach 2021) / 운영 SWH RMSE 전형 **0.3-0.5 m**(개방해 우수·복잡연안 저하) / **SWAN+ADCIRC 로 Hurricane Michael(Cat-5) surge+파랑 동시재현**(Vijayan 2023, Table 7).
- **Critical analysis (리뷰 자체의 비판적 논점 — 위키 SWAN source-analysis 와 정합)**:
  - **DIA**: 임의 선정 4-6 quadruplet 으로 full Boltzmann 근사(O(N_f⁷)→O(N_f³)) — **오차 미정량·체계적 평가법 부재**, bimodal/급변 바람에서 부정확.
  - **Whitecapping C_ds**: 지역·바람산품별 시행착오 튜닝 관행 → **바람장 오차를 흡수하는 보상관계** — TC 최강역에서 유의파고 **2-3 m+ 과소**, ST6 로 감소했으나 미해결.
  - **Battjes-Janssen γ**: 통상 0.73 고정이나 관측상 **0.4-1.2 변동**(경사·입사조건) — 보편성 없는 튜닝 파라미터.
- **HPC (§6, Table 8)**: WAM6-GPU v1.0 = 8×A100 으로 7일 전지구 0.1° 예보 실시간(**37×** vs dual-socket CPU) / GPU 스펙트럴 모델 일반 20-50× / FUNWAVE-TVD GPU 50-100×.
- **ML 통합 (§3.10·§7.6, verbatim 유지)**: "data-driven parameterizations and surrogate models may **supplement or replace** traditional physics-based formulations for specific processes" — 단 **"physics-based models will remain essential for extrapolation beyond training data"**(§3.10). §7.6: 신뢰성 근본질문(특히 극한사상 외삽) 미해결 → **hybrid(물리+ML)가 최선 경로**.

## E. 분류 요약

| 분류 | 대표 | 아키텍처 | 가속/정확도 | 비고 |
|---|---|---|---|---|
| **A surrogate** | DELWAVE 2024 ★PDF | CNN point (3-block, [11,4,90,89] 텐서) | 학습 2.5d, >100 wind/s, Hs MAE 5-10cm, storm P/R 0.97 | climate ensemble, 99%ile ≤5% 과소 |
| | DeepONet 2026 ★PDF | operator learning (branch×trunk) | **0.04s vs 30s ≈10³×**, Hsig RLE <2%·forces <11% (DUCK) | **ADCIRC 결합** Dawson, 이산화 불변 |
| | Johnson wave 2026 ★PDF | CNN + surge입력 연쇄 | RMSE 0.05-0.06m, 89% 등가통과 | landscape 진화 (A.4) |
| | FNO CoastalTwin ★PDF | neural operator | 45×(2min vs 1.5hr), MSE 0.0011 | ⚠NEMO SSH(파랑 아님), 육지마스크 열화 |
| | GNN / CNN | — | 80×, RMSE 0.3-2cm | downscaling (abstract-level, paywall) |
| **B forecast** | Crossformer/Swin-LSTM | transformer+LSTM | typhoon Hs 3h | SWAN=학습데이터 (abstract-level) |
| **C hybrid** | PINO ★PDF / physics-guided | physics-in-loss FNO | SSP 0.10-0.13, 0.014s/샘플, GT 불요 | ⚠위상해상 HOSM 재구성(SWAN 아님), 1D+t 한정 |
| **D review** | Ferdaus 2025 ★PDF | — (38p, 5+5 모델 비교) | SWAN=baseline 1.0, ST6 15-25%↓, DIA/C_ds/γ 비판 | ML=supplement/replace + caveat |

## F. 핵심 통찰

1. **SWAN = 고품질 학습데이터 생성기** (DELWAVE/DeepONet 모두 SWAN out 으로 학습) → ML 이 emulate 후 ensemble/coupled 가속.
2. **Operator learning (DeepONet/FNO)** 이 point-LSTM 보다 발전 — full field + 물리량(radiation stress) 예측 + **이산화 불변**(미학습 좌표 예측), **SWAN+ADCIRC coupling 의 wave surrogate** (Dawson 그룹 2026, **0.04 s vs 30 s ≈ 10³×**)로 storm-surge 운영 직결. DeepONet 의 고주파 스무딩은 순환모델 강제력으로 오히려 안정적일 수 있음(A.2 §5.2).
3. **caveat (Ferdaus 2025)**: 물리모델은 extrapolation(미학습 extreme)에 여전히 필수 → hybrid/PINO 가 현실적 방향.
4. wave surrogate(DELWAVE/DeepONet) ↔ surge surrogate([[07-ml-emulators]] PACT/StormNet) **대칭 구조** — coupled wave-surge ML emulation 이 차세대.

## G. 한계

- **full-PDF verified (2026-07-03)**: A.1 DELWAVE(21p)·A.2 DeepONet(46p)·A.3 FNO CoastalTwin(6p)·A.3 PINO(13p)·A.4 Johnson wave(2026-06-12)·D Ferdaus(38p) — 본문 수치·식·표 직접 확인. **arXiv 가용분 전부 소진**.
- ⚠ full read 로 **분류 정정 2건**: FNO CoastalTwin = NEMO SSH surrogate(파랑 아님), PINO = 위상해상 HOSM 파면 재구성(SWAN surrogate 아님) — 본 노트에는 인접영역 참고로 유지하되 SWAN 직접 대체 사례 아님을 명시.
- 잔여 abstract-level 현황 (★2026-07-19 재판정 — 구판 "전부 paywall" 은 **부분 오진**):
  - **실제 결제벽**(Elsevier): GNN downscaling(*Ocean Modelling*)·CNN regional(*Coastal Eng/Applied Ocean Res*)·Crossformer(*Expert Systems with Applications*)·ANN port(*Ocean Eng*)·WW3+ML(*Coastal Eng*) → 원문 조달 시 보정 `[source-needed]`
  - ⚠ **오픈액세스인데 paywall 로 분류돼 있던 것**: *JMSE*(MDPI)는 결제벽이 아니라 Cloudflare 봇차단 — reader 프록시로 전문 수신 가능. **JMSE 13:1612 는 2026-07-19 전문 직독 완료**(위 B절 정정 반영). MDPI·Frontiers 계열 잔여 항목은 동일 방법으로 승격 가능.
  - 핵심 SWAN surrogate 계보(DELWAVE·DeepONet·Johnson)는 full-PDF 로 완결 — 잔여는 주변부.
- arxiv 2604.06433(DeepONet)·2511.21856(Ferdaus)·2508.03315(PINO)는 preprint — peer-review 후 metric 변동 가능. Ferdaus(Writefull)·PINO(ChatGPT 3.5) 생성형 AI 교정 사용 공개.

## H. 연결

- [[07-ml-emulators]] — storm-surge ML emulator (PACT/StormNet, surge 측 대응)
- [[swan-recent-research-2024-2026]] — SWAN 최근 동향 (§2 ML 하이브리드 상위)
- [[swan-unstructured-time-step]] — SWAN+ADCIRC coupling (DeepONet surrogate 대상)
- [[swan-foundational-papers]] — SWAN 원논문
