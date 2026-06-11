---
title: "Storm Surge ML Emulators — surrogate models for hydrodynamic storm-surge prediction"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "arxiv:2605.09036 직접 fetch (WebFetch 2026-05-26) — abstract + 메타데이터 (authors, 제출일 2026-05-09, 카테고리 cs.LG) 직접 인용. 본문 §2 의 architecture 디테일·peak-aware loss·결과·한계는 전부 abstract 인용 기반. 정량 RMSE/MAE 수치, training hindcast 모델 (ADCIRC/Delft3D/etc.), CMIP6 5개 model 구체명, US Northeast 정점 좌표/개수 등은 abstract 미명시 — full PDF read 후 보강 가능. §3 추가 (2026-05-26): arxiv:2604.20688v2 (Nader·Giaremis·Dawson·Kaiser·Mohammadiporshokooh·Kaiser 2026, 제출일 2026-04-22 v1 / 2026-04-23 v2, 카테고리 cs.LG/cs.AI, 51p) abstract 직접 fetch — GCN+GAT+LSTM bias-correction architecture · US Gulf Coast 학습 · Hurricane Idalia (2023) test · RMSE 감소율 (48h >70% / 72h >50%) verbatim 인용. §4 cross-ref 표 + §5 한국 적용 검토 (StormNet bias-correction 접근이 한국 우선) 자체 분석 [2026-06-11 재번호 후 현 §5 관계표·§6 한국적용]. **§2.6~2.16 추가 (2026-05-28)**: arxiv:2605.09036v1 **full PDF 41p 직접 fetch** (curl + Read tool) — Table 1 5 CMIP6 모델 (AWI-CM-1-1-MR / CNRM-CM6-1 / EC-Earth3 / MPI-ESM1-2-HR / MRI-ESM2-0) + Table 2 4-station RMSE/MAE (Battery 0.0337/0.0246 / Boston 0.0274/0.0203 / Lewes 0.0276/0.0208 / CBBT 0.0306/0.0235) + Table 3 5% peak (PACT vs ST-GNN ~53% reduction) + Table 4 inference 3.4-3.6s vs ADCIRC 4.5-7h + Table 7/8 cross-dataset (NCEP→GCM 0.14-0.18m vs GCM↔GCM 0.04-0.09m reanalysis-GCM gap) + Appendix A ST-GNN baseline + Appendix C peak-aware ablation. ADCIRC 모델 + TPXO9 + 4 station 좌표 + 학습 config (4×H100 batch 256 lr 0.005 300 epochs Adam wd 10^-5) + GraphSAGE + cross-attention + Transformer + horizon-query + dual-head + L_PeakAware (eq 35) verbatim 인용. Charbonnier slope loss + ρ=0.05 tail fraction 등 hyperparameter 명시. ✅ 기존 §2.6 미보강 6개 항목 모두 해소 (code/data 공개 1건만 ⚠ — corresponding author 요청 필요). **§4 추가 (2026-06-11)**: arxiv:2603.25978v1 (Pachev·Arora·Zhao·Valseth, 2026-03-26) **abstract 직접 인용** (inbox markdown) — 전지구 학습 데이터셋(ADCIRC peak surge 15,000+ landfalling synthetic storm) + CV architecture peak emulator + location-invariance + dataset/model 공개. verbatim 2 인용. CV backbone 구체·basin 분포(서태평양 typhoon 포함 여부)·정량 RMSE·location-invariance 구현은 abstract 미명시 — full PDF read 후 §4 보강. 섹션 재번호 동반: 기존 §4→§5(관계표)·§5→§6(한국적용)·§6→§7(후보)·§7→§8(연결)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-26
verification_by: "Claude Opus 4.7 (1M context) — arxiv abs 페이지 직접 fetch + author/date/category/abstract 직접 인용 (PACT + StormNet) + PACT full PDF 41p read (2026-05-28)"
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

### 2.6 본 위키 미보강 항목 — ✅ 모두 해소 (2026-05-28 full PDF 41p read)

abstract 만으로 불가했던 항목들이 PDF §2-7 + Appendix A-E 직접 인용으로 해소:

- ✅ Training hydrodynamic 모델 → **ADCIRC** (§2.7)
- ✅ RMSE/MAE 수치 → §2.10 Table 2 (4 stations) + §2.11 Table 3 (5% peak)
- ✅ baseline GNN architecture → §2.9 **ST-GNN** (GraphSAGE + global pooling + LSTM, Appendix A Fig A1)
- ✅ US Northeast 4 정점 → §2.7 (CBBT VA + Lewes DE + Battery NY + Boston MA)
- ✅ CMIP6 5 모델 구체명 → §2.7 Table 1 (AWI-CM-1-1-MR / CNRM-CM6-1 / EC-Earth3 / MPI-ESM1-2-HR / MRI-ESM2-0)
- ✅ Training config + 시간 → §2.13 (4×H100, batch 256, 300 epochs, lr=0.005, Adam wd=10⁻⁵)
- ⚠ code/data 공개 여부 — PDF Acknowledgments + Appendix 어느 곳에도 GitHub repo / data DOI 명시 없음. corresponding author maryam@lehigh.edu 요청 필요

### 2.7 Datasets (PDF §2 Table 1) — verified

**Atmospheric forcing**: NCEP/NCAR Reanalysis (Kalnay 1996, 1979-2014) + 5 CMIP6 GCMs (ScenarioMIP SSP5-8.5, historical 1979-2014 + future 2070-2099):

| # | Model | Horizontal resolution | Reference |
|---|---|---|---|
| 1 | **AWI-CM-1-1-MR** | 1.9° × 1.2° | Semmler 2020 |
| 2 | **CNRM-CM6-1** | 1.4° × 1.4° | Volodin & Gritsun 2018 |
| 3 | **EC-Earth3** | 0.7° × 0.7° | Massonnet 2020 |
| 4 | **MPI-ESM1-2-HR** | 0.9° × 0.9° | Gutjahr 2019 |
| 5 | **MRI-ESM2-0** | 1.1° × 1.1° | Yukimoto 2019 |
| NCEP-NCAR | 1.9° × 1.875° | Kalnay 1996 |

선정 기준 (PDF §2.1): 역사-미래 mean surface temp 변화 representative + TC environmental field 재현 + ETC frequency 정합 (Priestley 2020, Gore 2023).

**Hydrodynamic ground truth**: ADCIRC (Luettich 1992) finite element unstructured mesh, ~1 km nearshore → ~100 km open ocean (Marsooli & Lin 2018), TPXO9-Atlas 8 tidal constituents (Egbert & Erofeeva 2002). Winter Nov 1-Mar 31 simulation. Residual surge: $\eta_t^{\text{surge}} = \eta_t^{wl} - \eta_t^{\text{tide}}$ (eq 1).

**4 US Northeast tide-gauge stations** (Figure 1b):

| Station | 약 좌표 | 비고 |
|---|---|---|
| CBBT (Chesapeake Bay Bridge Tunnel), VA | ~36.5°N, 76°W | Mid-Atlantic |
| Lewes, DE | ~38.8°N, 75°W | Delaware Bay |
| The Battery, NY | ~40.7°N, 74°W | NYC harbor — ETC dominated (Catalano & Broccoli 2018: 88/100 largest events) |
| Boston, MA | ~42.3°N, 71°W | 91/100 largest events ETC-driven |

### 2.8 Graph + node features (PDF §2.3-2.4)

- 입력: 3 forcing graphs at $t-12h$, $t-6h$, $t$ (6h grid, eq 2)
- 타겟: 6-step hourly surge $\mathbf{y}_t \in \mathbb{R}^6$ from $t$ to $t+5h$ (eq 3)
- Graph: 4-neighbor lat-lon grid (eq 5), permutation equivariant
- Node features (eq 6): $\mathbf{x}_{t,i} = [\text{lat}_i, \text{lon}_i, u_{t,i}, v_{t,i}, p'_{t,i}] \in \mathbb{R}^5$
- **Pressure spatial mean centering**: $p'_{t,i} = p_{t,i} - \bar{p}_t$, $\bar{p}_t = (1/|V|)\sum_i p_{t,i}$ (eq 7-8). focus on spatial gradients

### 2.9 ST-GNN baseline (Appendix A Fig A1)

비교 baseline: GraphSAGE encoder per snapshot + global pooling → concat 3 timesteps → LSTM → Linear → 6-step output. 즉 **uniform spatial pooling + recurrent temporal**. PACT 와 핵심 차이:

- ST-GNN: 모든 station 에 같은 pooled forcing token
- PACT: **station-specific cross-attention query** → station 별 forcing 의 different 부분에 attention

### 2.10 Overall results (Table 2 — NCEP Past-Only, meters)

| Method | Loss | Battery RMSE/MAE | Boston RMSE/MAE | Lewes RMSE/MAE | CBBT RMSE/MAE |
|---|---|---|---|---|---|
| Simple GNN (0h) | MSE | 0.0659 / 0.0480 | 0.0495 / 0.0354 | 0.0655 / 0.0511 | 0.0631 / 0.0473 |
| ST-GNN (12h) | MSE | 0.0536 / 0.0384 | 0.0426 / 0.0310 | 0.0447 / 0.0341 | 0.0469 / 0.0348 |
| PACT Base | MSE | 0.0349 / 0.0253 | 0.0282 / 0.0209 | 0.0279 / 0.0210 | 0.0309 / 0.0237 |
| **PACT Best** | **Peak-Aware** | **0.0337 / 0.0246** | **0.0274 / 0.0203** | **0.0276 / 0.0208** | **0.0306 / 0.0235** |

PACT vs ST-GNN: RMSE **34-38% 감소**, MAE **32-38% 감소**. Peak-aware loss 추가로 추가 ~0.0012m RMSE 개선.

### 2.11 Peak-event performance (Table 3 — 5% peak time, meters)

PACT Best vs ST-GNN (12h) at Battery:

| Metric | ST-GNN | PACT Best | 개선 |
|---|---|---|---|
| Peak RMSE | 0.1022 | **0.0479** | -53% |
| Peak MAE | 0.0796 | **0.0358** | -55% |
| Peak Mean Signed | -0.0620 | **-0.0139** | underprediction 78% 감소 |
| Peak Max Abs | 0.3537 | **0.2101** | -41% |

**핵심**: ST-GNN 은 peak underprediction (negative signed error magnitude 큼). PACT peak-aware loss 가 systematic 부호 bias 보정. 1% / 10% peak threshold 도 같은 패턴 (Appendix D Tables D1, D2).

### 2.12 Cross-dataset transfer — reanalysis-GCM gap (Tables 7, 8)

Past-Only RMSE (Battery, train→eval, meters):

| Train\Eval | NCEP | AWI | CNRM | EC_EARTH | MPI | MRI |
|---|---|---|---|---|---|---|
| **NCEP→**  | / | **0.1616** | **0.1789** | **0.1425** | **0.1595** | **0.1779** |
| AWI→ | 0.0534 | / | 0.0543 | 0.0548 | 0.0425 | 0.0519 |
| CNRM→ | 0.0510 | 0.0868 | / | 0.1147 | 0.0886 | 0.0609 |
| EC_EARTH→ | 0.0575 | 0.0472 | 0.0722 | / | 0.0492 | 0.0632 |
| MPI→ | 0.0814 | 0.0419 | 0.0689 | 0.0591 | / | 0.0565 |
| MRI→ | 0.0630 | 0.0481 | 0.0440 | 0.0761 | 0.0509 | / |

**핵심 발견** (PDF §6.2):

- NCEP→GCM: **0.14-0.18 m RMSE** (in-data NCEP 0.0337 대비 4-5배 증가)
- GCM↔GCM: 0.04-0.09 m (in-data 와 comparable)
- **asymmetric**: GCM→NCEP transfer 는 0.05-0.08 m (양호) — reanalysis-GCM gap 이 **harder-to-easier 방향** 으로만 큰 영향
- 원인: NCEP 은 data assimilation 으로 observed atmospheric state 제약 vs GCM 은 free-running, 자체 climatology + ETC frequency 다름 (Priestley 2020: CMIP6 weak cyclones zonally + bomb cyclone underestimate)
- EC_EARTH 가장 어려운 target (highest-res 0.7° → finer-scale gradients 가 lower-res training 에서 학습 안됨)

향후 robustness 방향 (PDF §6.2 권고): (a) multi-source training across multiple GCMs, (b) lightweight domain adaptation / calibration when deploying.

### 2.13 Training config + computational efficiency (PDF §4.3 + Table 4)

- Hardware: **4× NVIDIA H100 GPUs**, Intel Xeon Platinum 8468 host
- Optimization: **batch 256, Adam wd=10⁻⁵, lr=0.005, 300 epochs**, linear warmup 5 epochs + cosine decay (min lr 10⁻⁶)
- ADCIRC ground truth: Princeton Della cluster (AMD EPYC 9654 + Intel Cascade Lake, 64-128 CPU cores)

**Runtime (Table 4, 1 station × 1 year)**:

| Dataset | Training (sec) | Inference (sec) | ADCIRC (hours) |
|---|---|---|---|
| NCEP | 621 | 3.60 | 4.5-7 |
| AWI | 2294 | 3.46 | 4.5-7 |
| CNRM | 1214 | 3.40 | 4.5-7 |
| EC_EARTH | 4452 | 3.54 | 4.5-7 |
| MPI | 2292 | 3.50 | 4.5-7 |
| MRI | 1531 | 3.45 | 4.5-7 |

→ **1년 winter season trajectory ≈ 3.4-3.6 초** (학습 후) vs ADCIRC **4.5-7 시간** = **~5,000-7,000배 가속**. 학습 비용 (621-4452 초) 은 1 회성 — multi-year/station/scenario ensemble 시 amortize.

### 2.14 Architecture detail (PDF §3, eq 9-35)

PACT 4 stage (Figure 2):

1. **Spatial Graph Encoding (GraphSAGE, Hamilton 2017)**: $L$ layer 메시지 전달 — $\mathbf{m}_i^{(\ell)} = \text{AGG}\{\mathbf{h}_j^{(\ell-1)}: j \in \mathcal{N}(i)\}$, $\mathbf{h}_i^{(\ell)} = \phi(\mathbf{W}^{(\ell)}[\mathbf{h}_i^{(\ell-1)} \| \mathbf{m}_i^{(\ell)}] + \mathbf{b}^{(\ell)})$ (eq 9). AGG = mean, $\phi$ = LeakyReLU, dropout. **3개 입력 시간에 shared weights**

2. **Station-Conditioned Cross-Attention Readout** (Fig 3): 학습 가능한 station query $\mathbf{Q}_s = \tilde{\mathbf{q}}_s^\top$, $\tilde{\mathbf{q}}_s = \mathbf{q}_{\text{base}} + \psi(\mathbf{s})$ (eq 13). $\mathbf{s}$ = NOAA station metadata (lat, lon, elevation). multi-head attention (Vaswani 2017). 출력 $\mathbf{z}_{s,\tau} = \text{Attn}(\mathbf{Q}_s, \mathbf{K}_\tau, \mathbf{V}_\tau)$ (eq 12)

3. **Temporal Transformer Encoder**: 3 station-conditioned tokens + temporal embeddings (eq 18-21). multi-head self-attention + FFN + residual + layer norm

4. **Horizon-Conditioned Decoder**: learned horizon queries $\{\mathbf{q}_h\}_{h=0}^5$, $\mathbf{c}_h = \text{Attn}(\mathbf{q}_h, \mathbf{H}, \mathbf{H})$ (eq 22). 각 lead time 별 dedicated query

5. **Peak-Aware Auxiliary Head** (§3.5):
   - Dual prediction: $\hat{y}_h^{\text{base}} = f_{\text{base}}(\mathbf{c}_h)$, $r_h^{\text{tail}} = f_{\text{tail}}(\mathbf{c}_h)$ (eq 24)
   - Bounded tail: $\tilde{r}_h^{\text{tail}} = c \tanh(r_h^{\text{tail}}/c)$ (eq 25)
   - Gated combination: $\hat{y}_h = \hat{y}_h^{\text{base}} + g \cdot \alpha \cdot \tilde{r}_h^{\text{tail}}$ (eq 26), gate $g = \sigma(f_{\text{gate}}(\bar{\mathbf{c}}))$ (eq 27)

### 2.15 Peak-Aware Loss (PDF §3.5.2, eq 28-35)

$$\mathcal{L}_{\text{PeakAware}} = \mathcal{L}_{\text{mse}} + \lambda_{\text{tail}} \mathcal{L}_{\text{tail}} + \lambda_{\text{slope}} \mathcal{L}_{\text{slope}}$$

- $\mathcal{L}_{\text{mse}}$: 표준 MSE (eq 28)
- $\mathcal{L}_{\text{tail}}$: MSE 를 peak-dominated samples ($p_b \geq \tau_{\text{tail}}$, $\tau_{\text{tail}}$ = 95%-tile) 위에서만 (eq 30-31), $\rho = 0.05$
- $\mathcal{L}_{\text{slope}}$: Charbonnier loss $\rho(x) = \sqrt{x^2 + \epsilon^2}$ ($\epsilon = 0.001$, Barron 2019) over slope errors $e_{b,h} = \Delta\hat{y}_{b,h} - \Delta y_{b,h}$ (eq 33-34)

**Ablation (Appendix C Table C1, Battery)**:

| Variant | Overall RMSE | 5% Peak RMSE | 5% Peak Max Abs |
|---|---|---|---|
| MSE | 0.0349 | 0.0532 | 0.2346 |
| +Tail | 0.0345 | 0.0477 | **0.1834** |
| +Slope | 0.0340 | 0.0510 | 0.2582 |
| +Tail+Slope | **0.0337** | **0.0479** | 0.2101 |

→ Tail term primary for peak-RMSE/MAE, Slope term primary for 1% peak max abs (Pareto-optimal combined).

### 2.16 한계 (저자 명시 + 본 위키 검토)

PDF 명시:

- **Reanalysis-GCM gap** (§6.2): NCEP-trained 모델 → GCM forcing 시 RMSE 4-5배 증가. 운영 deployment 시 source-target distribution match 중요
- ETC 중심: TC 만 다루는 paper 대비 ETC + TC 양쪽 cover. 하지만 4 정점 모두 US Northeast — global generalization 미입증
- Lead time 6h 단기 (t to t+5h). longer-lead surge forecasting 별도

본 위키:

- 한국 적용 시 KOOS-EJS / WRF-ROMS hindcast 결합 가능성 — §6 한국 적용 검토 참조
- code/data 공개 미확인 (corresponding author 요청 또는 후속 publication 추적)

## 3. StormNet (Nader, Dawson et al. 2026) — GNN-LSTM bias correction

### 3.1 기본 정보 (verified arxiv 2026-05-26 fetch)

| 항목 | 값 |
|---|---|
| arxiv ID | **2604.20688v2** (v1: 2026-04-22, v2: 2026-04-23) |
| 제목 | "StormNet: Improving storm surge predictions with a GNN-based spatio-temporal offset forecasting model" |
| 저자 | Noujoud Nader, Stefanos Giaremis, **Clint Dawson**, Carola Kaiser, Karame Mohammadiporshokooh, Hartmut Kaiser |
| arxiv 카테고리 | cs.LG (primary), cs.AI (secondary) |
| Comments | 51 pages, 9 figures, 5 tables |
| URL | <https://arxiv.org/abs/2604.20688> |
| 소속 | abstract 페이지 미명시 (**Dawson = UT Austin ADCIRC 핵심 개발자** — 저자 권위) |

### 3.2 모델 아키텍처 (abstract 직접)

StormNet 은 **station-level bias correction** 을 위한 spatio-temporal GNN. ADCIRC 출력을 fully replace 가 아니라 post-process — physics-based forecast 의 잔차 (offset) 를 학습:

- **Graph convolutional (GCN)** — water-level gauge station 사이 spatial dependency 추출
- **Graph attention (GAT)** — station 간 attention weights 학습 (위치별 영향력 differential)
- **LSTM** — 시간축 dependency 모델링 (storm 진행 중 시계열 패턴)
- 최종 출력: ADCIRC forecast 에 더할 offset (= residual correction)

→ PACT (§2) 와 차이: PACT 는 atmospheric forcing → surge 의 **direct emulator**. StormNet 은 ADCIRC 위에 얹는 **post-processor (bias corrector)** — physics layer 보존.

### 3.3 학습 + 검증 (abstract 직접)

| 항목 | 값 |
|---|---|
| Training | US Gulf Coast 과거 hurricane 데이터 (구체 hurricane list abstract 미명시) |
| Test case | **Hurricane Idalia (2023)** |
| Baseline | Sequential LSTM (graph 없는 sequence-only — StormNet 의 자체 ablation) |
| Metric | RMSE (root mean square error) |

### 3.4 결과 (abstract 직접 verbatim)

> "Results demonstrate that StormNet can effectively reduce the root mean square error (RMSE) in water-level predictions by more than 70% for 48-hour forecasts and above 50% for 72-hour forecasts, as well as outperform a sequential LSTM baseline, particularly for longer prediction horizons."

| Forecast horizon | RMSE 감소율 |
|---|---|
| **48-hour** | **>70%** |
| **72-hour** | **>50%** |

→ 긴 시간 horizon 일수록 LSTM baseline 대비 우수 (graph spatial info 효과).

추가 abstract 인용:

> "The model also exhibits low training time, enhancing its applicability in real-time operational forecasting systems."

### 3.5 본 위키 미보강 (full PDF read 시 보강 가능)

abstract 만으로는 확인 불가 (51 pages full paper 에 명시 추정):

- training hurricane list (US Gulf Coast 어떤 storms, 몇 개)
- gauge station 좌표·개수·기간
- StormNet 의 정확한 graph 구성 (node = station? edge weight = distance? bathymetry? 정점간 hydrodynamic distance?)
- ADCIRC 의 어떤 version·grid·NWS mode 입력 사용
- Hurricane Idalia (2023) test 의 정량 station-by-station 결과
- GAT attention weights 의 해석 (어느 station 이 어디 영향)
- code/data 공개 여부

→ full paper PDF (<https://arxiv.org/pdf/2604.20688v2>) read 후 본 §3 update 권장.

## 4. Global Location-Invariant Peak Surge (Pachev, Valseth et al. 2026) — 전지구 CV emulator

### 4.1 기본 정보 (inbox markdown abstract-level, 수집 2026-06-06)

| 항목 | 값 |
|---|---|
| arxiv ID | **2603.25978v1** (2026-03-26) |
| 제목 | "Global Location-Invariant Peak Storm Surge Prediction" |
| 저자 | Benjamin Pachev, Prateek Arora, Jinpai Zhao, **Eirik Valseth** |
| seed (inbox 메타) | ADCIRC |
| URL | <https://arxiv.org/abs/2603.25978> |
| 소속 | abstract 미명시 (저자 Pachev·Valseth = ADCIRC 계열 surrogate 연구 — abstract 가 ADCIRC 출력 학습 명시) |

### 4.2 핵심 기여 (abstract 직접)

기존 surrogate 데이터셋의 **지리적 편중** (대부분 CONUS·중국 한정) 을 정면으로 겨냥. 두 산출물(데이터셋·모델) + 공개:

1. **전지구 학습 데이터셋** — ADCIRC peak surge 출력, 전세계에 분포한 **15,000+ landfalling synthetic storm**. abstract verbatim:
   > "the largest dataset of its kind ever assembled, and is unique in its global scope."
2. **CV 기반 ML 모델** — computer vision architecture 기반 peak surge 모델, 전지구 데이터셋 학습. abstract verbatim:
   > "can accurately predict maximum storm surge in disparate geographical regions - including those for which few or no surrogate models exist."
3. dataset·model 모두 **공개** ("publicly available").

→ 핵심 novelty = **location-invariance**: 학습 지역 밖에서 무력해지는 기존 emulator 의 한계를, 전지구 데이터로 일반화하여 돌파.

### 4.3 PACT(§2)·StormNet(§3) 대비 — 3 ML surge 패러다임

| 축 | PACT (§2) | StormNet (§3) | Global LI (§4) |
|---|---|---|---|
| 예측 대상 | full surge time series (direct emulate) | ADCIRC offset (bias correction) | **peak surge only** (maxele 류 — abstract 추론) |
| 아키텍처 | graph transformer (cross-attention) | GCN+GAT+LSTM | **computer vision architecture** (backbone abstract 미상세) |
| 지리 범위 | US Northeast + CMIP6 downscale | US Gulf Coast | **global (15,000+ storm 전세계)** |
| 핵심 강점 | peak-aware loss + CMIP6 적용 (단 reanalysis→GCM gap §2.12) | real-time post-process | **location-invariance — 미보유 지역 일반화** |
| 학습 원천 | ADCIRC/reanalysis | ADCIRC hindcast | **ADCIRC synthetic storm suite** |

→ 세 패러다임 상보적: direct emulator(PACT) / bias corrector(StormNet) / **global peak-surge generalizer(Global LI)**. 한국처럼 표준 surrogate 학습셋이 없는 지역(§6)에 **직접 transfer 가능성** = 가장 주목할 후보 (단 서태평양 basin 포함 여부 확인 전제 — §4.4).

### 4.4 본 위키 미보강 (full PDF read 시 보강 가능)

abstract 만으로 확인 불가 (정량·구조는 본문 명시 추정):

- CV architecture 구체 (CNN backbone·U-Net·입력 raster 종류 wind/pressure field·해상도)
- 15,000 synthetic storm 의 **basin 분포** (서태평양 typhoon 포함 여부 — **한국 적용 직결**)
- location-invariance 구현 메커니즘 (좌표 인코딩·정규화·도메인 일반화 기법)
- peak surge 정확도 정량 (RMSE/MAE, 지역별 break-down)
- 동아시아/한국 검증 결과 유무
- 공개 dataset·model URL (논문 본문)

→ full PDF (<https://arxiv.org/pdf/2603.25978v1>) read 후 §4 update 권장. 특히 **서태평양 basin 포함 시 한국 적용 1순위 후보** (§6.6).

## 5. 본 위키 storm-surge 자료와의 관계

| 본 위키 자료 | PACT (§2) 와의 접점 | StormNet (§3) 와의 접점 |
|---|---|---|
| [`01-concept.md`](01-concept.md) §3 인자 | input atmospheric forcing = §3 wind·pressure 인자 동등 | ADCIRC 출력의 offset 학습 — input = §3 인자 + ADCIRC forecast |
| [`02-theory.md`](02-theory.md) Pugh §6 + ADCIRC GWCE | GWCE 풀이 우회 (direct mapping) | GWCE 풀이 (ADCIRC) 의 **잔차만 학습** — physics layer 보존 |
| [`04-code-and-tools.md §1-2`](04-code-and-tools.md) ADCIRC NWS 모드 | 학습 hindcast 가 ADCIRC NWS=12/13/20 출력이면 pipeline (full paper 확인) | ADCIRC NWS 모드 출력 (water-level 시계열) 을 **직접 입력** — pipeline 자연 |
| [`04-code-and-tools.md §8`](04-code-and-tools.md#8-검증-metrics) RMSE/skill | RMSE/MAE 사용 = 본 위키 동일 metric 계열 | RMSE 사용 — 본 위키 동일 metric |
| [`05-examples.md`](05-examples.md) Maemi·Hinnamnor·Bolaven | 한국 적용 시 검증 case (단 US Northeast 학습) | 한국 적용 시 같음 (US Gulf Coast 학습 → 한국 transfer gap 예상) |

→ **Global LI (§4)** 는 PACT 와 같은 direct-emulator 계열(ADCIRC 출력 학습)이나, peak surge 만 산출하고 **전지구 학습**이라는 점에서 위 "transfer gap" 을 설계상 회피 — 본 위키 한국 case([`05-examples.md`](05-examples.md))에 학습 없이 적용 가능성이 가장 높은 후보(서태평양 basin 포함 전제, §4.4).

## 6. 한국 적용 검토 (탐색 단계, 미실증)

PACT·StormNet·Global LI 모두 한국 미학습. 한국 적용 시 공통 고려사항:

1. **학습 데이터 부재** — 한국 ADCIRC hindcast (KMOU·KIOST 보유, 학회 발표 기준) 활용 가능성. [`04-code-and-tools §7`](04-code-and-tools.md#7-운영-예제--한국-태풍-hindcast-워크플로) 워크플로 결과인 maxele.63 + station-level fort.61 시계열을 학습 셋으로 가공 필요. 한국 학습 셋 표준 데이터 없음 (2026-05-26 기준).
2. **정점** — KHOA 13정점 ([`04-code-and-tools §4.3`](04-code-and-tools.md#43-한국-13-정점-코드)) 후보. 단 KHOA OpenAPI archive 한계 (~1년) — 학습용 long-term observation 은 KHOA Annual Report 등 별도 archive 인용 필요 ([`04-code-and-tools §4.1`](04-code-and-tools.md#41-실시간-조위-관측)).
3. **태풍 typology 차이** — US Northeast/Gulf Coast 는 hurricane (Atlantic basin), 한국은 typhoon (서태평양 basin, GAHM 권장) — physics regime 차이로 직접 transfer 효과 unknown.
4. **PACT 의 CMIP6 transfer gap** — climate downscaling 적용 시 reanalysis→CMIP6 degradation. 한국 ensemble 평가에도 동일 issue 예상.
5. **StormNet 의 bias correction 접근** — 한국 ADCIRC 자체 운영체계 (KMOU 등) 가 있다면 StormNet 류 post-processor 가 **가장 진입장벽 낮은 ML 접근**: full emulator 학습 데이터 불필요, **기존 ADCIRC 출력 + KHOA 관측 만으로 residual 학습 가능**. PACT 류 direct emulator 보다 한국 적용 우선 검토 후보.
6. **Global LI (§4) 의 zero-shot transfer 가능성** — 전지구 학습 + location-invariance 설계상, 한국 학습셋 **구축 없이** 곧바로 한국 peak surge 추정 시도 가능 (학습 데이터 부재 1번 항목을 우회). 단 두 전제: (a) 15,000 storm 에 **서태평양 typhoon basin 포함** 여부 (§4.4 — 본문 확인 필요), (b) peak surge 만 산출 → 시계열·총수위 침수예측엔 부족. 공개 model 이므로 한국 좌표 inference 만으로 즉시 sanity check 가능 = **실증 진입장벽 최저**.

→ 한국 적용 경로 우선순위 (현실적): **Global LI zero-shot sanity check (즉시, 공개 model inference — basin 포함 전제)** → **StormNet 류 bias correction (단기, ADCIRC 운영체계 위에 얹기)** → PACT 류 direct emulator (장기, 한국 학습 hindcast 셋 구축 후).

## 7. 추가 검토 후보 (placeholder — 향후 채워나갈 영역)

본 §는 ML emulator 입문점. 향후 cataloged 될 후보 카테고리 (Global LI §4 = 전지구 peak emulator 항목 catalog 됨, 2026-06-11):

- LSTM / sequence model station-level surge (StormNet baseline 류, Tiggeloven et al. 미확인)
- Neural operator (DeepONet, FNO) for shallow-water — inbox `operator-learning-for-surrogate-modeling-of-wave-induced-for` (2604.06433) 등 미트리아지
- 데이터 기반 limited-area surge model — inbox `flo--a-data-driven-limited-area-storm-surge-model` (2601.02090) 미트리아지
- 효율적 regional surrogate 학습 (진화 landscape·기후) — inbox `an-efficient-regional-storm-surge-surrogate` (2511.07269) 미트리아지
- PINN (physics-informed) for SWE
- ensemble downscaling surrogate (GCM → local surge)
- Storm-track conditioned emulator (GAHM 입력 → ML surge)

추적: `research/watchlist/` 에 ML emulator author + arxiv cs.LG ∩ physics.ao-ph 카테고리 등록 후보. 현재 [[../../research/watchlist/repo-myroms-roms]] · [[../../research/watchlist/repo-noaa-emc-ww3]] 등 model repo 위주 — `topic-ml-storm-surge-emulators.md` 신설은 [[reference-next-session-candidates]] 우선순위 3 옵션.

## 8. 연결

- [`01-concept.md`](01-concept.md) — storm-surge 5 인자
- [`02-theory.md`](02-theory.md) — Pugh §6 + ADCIRC GWCE 식 (PACT 는 풀이 우회, StormNet 은 잔차만 학습)
- [`04-code-and-tools.md`](04-code-and-tools.md) — full hydrodynamic 모델 + KHOA 관측 (PACT/StormNet/Global LI 학습 데이터 원천 후보)
- [`05-examples.md`](05-examples.md) — Maemi·Hinnamnor·Bolaven case (한국 검증 후보; Global LI zero-shot transfer 1순위 §6.6)
- 외부:
  - PACT arxiv abs: <https://arxiv.org/abs/2605.09036>
  - PACT PDF: <https://arxiv.org/pdf/2605.09036v1>
  - StormNet arxiv abs: <https://arxiv.org/abs/2604.20688>
  - StormNet PDF: <https://arxiv.org/pdf/2604.20688v2>
  - Global LI arxiv abs: <https://arxiv.org/abs/2603.25978>
  - Global LI PDF: <https://arxiv.org/pdf/2603.25978v1>
