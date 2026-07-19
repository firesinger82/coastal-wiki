---
title: "Storm Surge ML Emulators — surrogate models for hydrodynamic storm-surge prediction"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "arxiv:2605.09036 직접 fetch (WebFetch 2026-05-26) — abstract + 메타데이터 (authors, 제출일 2026-05-09, 카테고리 cs.LG) 직접 인용. 본문 §2 의 architecture 디테일·peak-aware loss·결과·한계는 전부 abstract 인용 기반. 정량 RMSE/MAE 수치, training hindcast 모델 (ADCIRC/Delft3D/etc.), CMIP6 5개 model 구체명, US Northeast 정점 좌표/개수 등은 abstract 미명시 — full PDF read 후 보강 가능. §3 추가 (2026-05-26): arxiv:2604.20688v2 (Nader·Giaremis·Dawson·Kaiser·Mohammadiporshokooh·Kaiser 2026, 제출일 2026-04-22 v1 / 2026-04-23 v2, 카테고리 cs.LG/cs.AI, 51p) abstract 직접 fetch — GCN+GAT+LSTM bias-correction architecture · US Gulf Coast 학습 · Hurricane Idalia (2023) test · RMSE 감소율 (48h >70% / 72h >50%) verbatim 인용. §4 cross-ref 표 + §5 한국 적용 검토 (StormNet bias-correction 접근이 한국 우선) 자체 분석 [2026-06-11 재번호 후 현 §5 관계표·§6 한국적용]. **§2.6~2.16 추가 (2026-05-28)**: arxiv:2605.09036v1 **full PDF 41p 직접 fetch** (curl + Read tool) — Table 1 5 CMIP6 모델 (AWI-CM-1-1-MR / CNRM-CM6-1 / EC-Earth3 / MPI-ESM1-2-HR / MRI-ESM2-0) + Table 2 4-station RMSE/MAE (Battery 0.0337/0.0246 / Boston 0.0274/0.0203 / Lewes 0.0276/0.0208 / CBBT 0.0306/0.0235) + Table 3 5% peak (PACT vs ST-GNN ~53% reduction) + Table 4 inference 3.4-3.6s vs ADCIRC 4.5-7h + Table 7/8 cross-dataset (NCEP→GCM 0.14-0.18m vs GCM↔GCM 0.04-0.09m reanalysis-GCM gap) + Appendix A ST-GNN baseline + Appendix C peak-aware ablation. ADCIRC 모델 + TPXO9 + 4 station 좌표 + 학습 config (4×H100 batch 256 lr 0.005 300 epochs Adam wd 10^-5) + GraphSAGE + cross-attention + Transformer + horizon-query + dual-head + L_PeakAware (eq 35) verbatim 인용. Charbonnier slope loss + ρ=0.05 tail fraction 등 hyperparameter 명시. ✅ 기존 §2.6 미보강 6개 항목 모두 해소 (code/data 공개 1건만 ⚠ — corresponding author 요청 필요). **§4 추가 (2026-06-11) → full PDF 격상 (2026-06-12)**: arxiv:2603.25978v1 (Pachev·Arora·Zhao·Valseth, 2026-03-26 [cs.CE]) — 초판 abstract-level 후 **full PDF 직접 read(pdftotext, /tmp/globalLI.txt)** 로 §4.1-4.7 verified 격상. 확정: 6 IBTrACS basin(NA/EP/NI/SI/**WP**/SP — 서태평양 한국 basin 포함) / STORM×IBTrACS→ADCIRC symmetric Holland / NOAA STOFS-2D-Global mesh(12.8M node) / storm packing 15000→3000 / landfall-중심 2.5°×2.5° 128×128 grid(location-invariance 기제) / 41 입력채널(13 pres+13 wind×2+bathy+landmask) / **UNet-5** encoder-decoder C0=64 / Table 3 basin별 RMSE(WP global 연안0.34·전점0.27m) / 실태풍 NA 67 hurricane per-point ADCIRC0.22 vs UNet0.37m / code github UT-CHG/adcirc-rom + DesignSafe 공개. 섹션 재번호 동반: 기존 §4→§5(관계표)·§5→§6(한국적용)·§6→§7(후보)·§7→§8(연결). **§3 full PDF 격상 (2026-06-16)**: arxiv:2604.20688v2 **full PDF 20p 직접 fetch**(curl + pdftotext -layout, /tmp/stormnet.txt) — §3.5 미보강 7항목 전부 해소. Table 1 13 TC(학습 11 / Ian 2022 val / Idalia 2023 test) + Table 3 16 Gulf Coast gauge(NOAA-NOS/TCOON, node 8 Grand Isle LA 최다연결 9) + 그래프 구성(edge iff ρij>0.8 AND dij<500km, Pearson 상관 + haversine, weighted adj=ρij) + offset eq1(modeled−observed, 3σ outlier 제거, MinMax 누설방지 분리) + 아키텍처 MLP→GCN+GAT→2×LSTM(Fig 3) + 학습 config(Adam 200ep lr 3e-5 wd 5e-7 batch 20 past-window 42-48h, single A100) + Idalia 결과(median RMSE 18-72h ~0.08-0.09m 포화, 48h-ahead 미보정 ADCIRC 대비 Cedar Key 60%/Apalachicola 65%/Galveston 73% 감소, peak Cedar Key 35%/29%) + Table 5 ablation(MLP+GAT+GCN+LSTM 0.084 best, GAT+LSTM 0.097>GCN+LSTM 0.131) verbatim. **정직 재구성: 헤드라인 >70%/>50% 는 미보정 ADCIRC 대비, 기존 LSTM baseline[77] 대비로는 36h ~11-12%·>24h window ~10% 만 우위(24h 이하 동등, full timeseries 평균은 LSTM 이 근소 우위) — 주 이점은 짧은 학습시간**. 코드/데이터 공개 repo 명시 없음(데이터 CERA Historical Storm Archive). Gulf Coast 한정(WP 미학습)."
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

**Atmospheric forcing**: NCEP/NCAR Reanalysis (Kalnay 1996, 1979-2014) + 5 CMIP6 GCMs (ScenarioMIP SSP5-8.5, historical 1979-2014 + future 2070-2100):

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

## 3. StormNet (Nader, Dawson et al. 2026) — GNN-LSTM bias correction (verified, full PDF read 2026-06-16)

### 3.1 기본 정보

| 항목 | 값 |
|---|---|
| arxiv ID | **2604.20688v2** (v1: 2026-04-22, v2: 2026-04-23) |
| 제목 | "StormNet: Improving storm surge predictions with a GNN-based spatio-temporal offset forecasting model" |
| 저자 | Noujoud Nader, Stefanos Giaremis, **Clint Dawson**, Carola Kaiser, Karame Mohammadiporshokooh, Hartmut Kaiser |
| arxiv 카테고리 | cs.LG (primary), cs.AI (secondary) |
| Keywords | Storm Surge Modeling, Bias Correction, Graph Neural Networks, Graph Convolution Networks |
| URL | <https://arxiv.org/abs/2604.20688> |
| 소속 | **Dawson = UT Austin ADCIRC 핵심 개발자** — 저자 권위. CERA(Coastal Emergency Risk Assessment) 플랫폼 통합 지향 |
| 코드/데이터 | 공개 repo 명시 없음. 데이터 = **CERA Historical Storm Archive** (refs [56,61]) |

### 3.2 모델 아키텍처 (PDF §2.5, Fig 3)

StormNet 은 **station-level bias correction** 을 위한 spatio-temporal GNN. ADCIRC 출력을 fully replace 가 아니라 post-process — physics-based forecast 의 잔차 (offset) 를 학습. 3 phase pipeline:

1. **MLP** (lightweight) — 각 station 의 historical offset 입력 전처리
2. **GCN** (graph convolution) — 그래프 구조 따라 이웃 station 정보 aggregation, broad spatial correlation
3. **GAT** (graph attention) — attention 으로 이웃별 중요도 adaptive weighting (storm 중 가장 relevant 한 inter-station 관계 강조)
4. **2× LSTM** — 시간축 dependency, time-series 예측
5. 최종 출력: predicted offset $\hat{o}_i(t)$ → ADCIRC forecast 에 더해 보정 (residual correction)

→ PACT (§2) 와 차이: PACT 는 atmospheric forcing → surge 의 **direct emulator**. StormNet 은 ADCIRC 위에 얹는 **post-processor (bias corrector)** — physics layer 보존. GCN(general spatial) + GAT(adaptive local) 의 **상보 조합**이 핵심 설계.

### 3.3 데이터 + 그래프 구성 (PDF §2.2-2.3)

**Offset 정의 (eq 1)**: $o_i(t) = x_i^{\text{modeled}}(t) - x_i(t)$ — station $i$ 의 ADCIRC 예측치 − 관측치 (hourly). ±3σ 밖 outlier 제거. MinMax scaling 을 train/val/test 별도 적용 (training 속성 기준 → data leakage 방지).

**TC 데이터 (Table 1)**: 13 historical Gulf Coast TC. 학습 11 + **Ian (2022, H5) = validation + Idalia (2023, H4) = test**:

| 학습 TC | Cat | 비고 |
|---|---|---|
| Charley(2004)·Dennis(2005)·Eta(2020)·Helene(2024) | H4 | |
| Wilma(2005)·Michael(2018)·Milton(2024) | H5 | |
| Hermine(2016)·Debby(2024) | H1 | |
| Debby(2012)·Fred(2021) | TS | |

**16 gauge stations (Table 3)** — Gulf Coast FL→AL→LA→TX, NOAA-NOS + TCOON 기관. 선정 기준: 모든 storm 에서 obs+modeled 데이터 결측 적은 station (결측 많으면 제외). 예: Cedar Key FL(node 3, landfall 직접 타격 max ~2.5m), Apalachicola FL(node 4, ~1.0m), Grand Isle LA(node 8, **최다연결 9**), Galveston Bay Entrance TX(node 12, landfall 원거리).

**그래프 (undirected, eq)**: node = gauge station, node feature = 관측 수위 시계열 $x_i$. **edge iff $\rho_{ij} > \rho_{\min}$ AND $d_{ij} < d_{\max}$** ($\rho_{\min}=0.8$, $d_{\max}=500$ km). $\rho_{ij}$ = 두 관측 수위 시계열의 Pearson 상관, $d_{ij}$ = haversine 대권거리. weighted adjacency $A_{ij}=\rho_{ij}$. → **물리적 의미**: 강한 수위상관 + 지리근접 station 끼리 연결. 임계값은 disconnected station 안 생기는 최저값.

### 3.4 Idalia (2023) 결과 (PDF §3.1)

- prediction window 6/9/12/15/18/24/36/48/72h 평가. median RMSE 는 18h 까지 증가 후 **18-72h 에서 ~0.08-0.09m 로 포화** (window 늘려도 안 커짐) — 긴 horizon 운영예보(OFS, 통상 ≥3일)에 유망.
- **48h-ahead, 미보정 ADCIRC 대비 RMSE 감소** (3 대표 정점): Cedar Key 60% / Apalachicola 65% / Galveston Bay Entrance **73%**. **72h-ahead**: 50% / 52% / 59%.
- **peak surge**: Cedar Key 최대관측수위 지점 forecasting error 를 48h 35% / 72h 29% 감소.
- TCOON(텍사스) station 이 NOAA-NOS 보다 RMSE 낮음 — Idalia 의 텍사스 영향 미미 (easy case) 때문.

### 3.5 LSTM baseline 비교 + ablation (PDF §3.2, Table 4-5)

**vs 기존 sequential LSTM 방법 [77]** (graph 없이 station 간 상호작용 미모델링):

| window | StormNet vs LSTM |
|---|---|
| 24h | 거의 동등 |
| full timeseries (전 station 평균) | LSTM 이 오히려 근소 우위 (각자 8/16 station 우세) |
| 36h (full) | StormNet 11/16 station 우세, 평균 RMSE **~11% 낮음** |
| 36h (landfall 전후 2일) | StormNet 13/16 station 우세, **~12% 낮음** |
| >24h window 종합 | StormNet **~10% 낮은 RMSE** |

**Ablation (Table 5, 24h window, 전 station RMSE m)**:

| 구성 | RMSE |
|---|---|
| GCN+LSTM | 0.131 |
| GAT+LSTM | 0.097 |
| GCN+GAT+LSTM | 0.087 |
| MLP+GAT+LSTM / MLP+GCN+LSTM | 0.088 |
| **MLP+GAT+GCN+LSTM (full StormNet)** | **0.084** |

→ GAT 단독이 GCN 단독보다 우수, GCN+GAT 조합으로 GAT 대비 11% 추가 감소, MLP 추가로 최종 3% 더. full 구성 최적.

### 3.6 정직한 평가 + 한계 (PDF §4)

- **헤드라인 ">70%/>50%" 는 미보정 ADCIRC 대비** 수치 — 기존 LSTM bias-correction 방법 대비로는 **>24h window 에서 ~10%, 24h 이하 동등** (full timeseries 평균은 LSTM 이 근소 우위). 저자 자체 결론도 "similar accuracy ... for short prediction windows ... but lower RMSE by 10% for windows greater than 24 h". **StormNet 의 실질 차별화 = 짧은 학습시간**(real-time 운영 적합).
- **구조적 한계** (PDF §4): (a) **obs+modeled 데이터 모두 있는 gauged 좌표에만** 적용 가능 — ungauged 위치 불가, (b) station 별 comparable 학습량 필요, (c) physics 는 그래프 구성에만 들어가고 **학습 과정엔 미반영**, (d) future work = ungauged 위치 bias 추정.
- Gulf Coast 한정. **WP(서태평양) 미학습** — 한국 직접적용 불가 (intro 가 Western North Pacific TC DB 를 언급하나 본 연구 학습셋은 Gulf Coast).
- 본 위키 한국 적용: §6.5 — 한국 ADCIRC 운영체계가 있다면 **진입장벽 최저 ML 접근**(full emulator 학습셋 불필요, 기존 ADCIRC 출력 + KHOA 관측만으로 residual 학습). 단 gauged 좌표 제약 = KHOA 정점에 한정.

## 4. Global Location-Invariant Peak Surge (Pachev, Valseth et al. 2026) — 전지구 UNet emulator

### 4.1 기본 정보 (verified — full PDF read 2026-06-12)

| 항목 | 값 |
|---|---|
| arxiv ID | **2603.25978v1** [cs.CE] (2026-03-26) |
| 제목 | "Global Location-Invariant Peak Storm Surge Prediction" |
| 저자·소속 | Benjamin Pachev (UMass Amherst), Prateek Arora (UC Berkeley), Jinpai Zhao (UT Austin Oden Inst.), **Eirik Valseth** (Norwegian Univ Life Sciences + Simula, Oslo) |
| 코드 | <https://github.com/UT-CHG/adcirc-rom> (UT Computational Hydraulics Group) |
| 데이터·모델 | DesignSafe 플랫폼 공개 |
| URL | <https://arxiv.org/abs/2603.25978> |

### 4.2 PACT(§2)·StormNet(§3) 대비 — 3 ML surge 패러다임

| 축 | PACT (§2) | StormNet (§3) | Global LI (§4) |
|---|---|---|---|
| 예측 대상 | full surge time series (direct emulate) | ADCIRC offset (bias correction) | **peak surge only** (maxele 128×128 장) |
| 아키텍처 | graph transformer (cross-attention) | GCN+GAT+LSTM | **UNet-5** (fully-conv encoder-decoder) |
| 지리 범위 | US Northeast + CMIP6 downscale | US Gulf Coast | **global 6 basin (15,000+ storm, WP 포함)** |
| 핵심 강점 | peak-aware loss + CMIP6 적용 (단 reanalysis→GCM gap §2.12) | real-time post-process | **location-invariance — 미보유 지역 일반화** |
| 학습 원천 | ADCIRC/reanalysis | ADCIRC hindcast | **ADCIRC synthetic storm suite (STORM×IBTrACS)** |

→ 세 패러다임 상보적: direct emulator(PACT) / bias corrector(StormNet) / **global peak-surge generalizer(Global LI)**. 한국처럼 표준 surrogate 학습셋이 없는 지역(§6)에 **직접 transfer 가능성** = 가장 주목할 후보 (서태평양 WP basin 포함 확정 — §4.3).

### 4.3 데이터셋 — 전지구 ADCIRC synthetic suite (PDF §2)

- **STORM × IBTrACS** synthetic TC track → ADCIRC(symmetric Holland) 변환. >15,000 landfalling moderate-severe TC.
- **6 IBTrACS ocean basin 전부**: NA(North Atlantic)·EP(East Pacific)·NI(North Indian)·SI(South Indian)·**WP(West Pacific)**·SP(South Pacific). → **★서태평양(WP) 포함 = 한국·일본 태풍 basin 학습됨** (§4.7·§6.6 직결).
- 메시: NOAA **STOFS-2D-Global** (12.8M nodes / 24.9M triangular elements) 단일 전지구 메시.
- **Storm packing**: basin당 1 cyclone 씩 multi-storm run (ADCIRC symmetric-Holland multi-storm 지원하도록 codebase 수정) → 15,000 run 을 **3,000 run** 으로 절감. basin간 peak surge 간섭 없음 검증.

### 4.4 입력 특징 + location-invariance 메커니즘 (PDF §3.1)

- maxele 를 **storm landfall 위치 중심 regular lat-lon grid** 로 보간 → **이것이 location-invariance 핵심**: 절대 지리좌표가 아니라 landfall-상대 윈도를 학습("geographic region 을 model architecture 에 implicit encode", PDF p.5).
- 윈도 **2.5°×2.5°, 128×128** 해상도. Holland forcing 3시간 간격 −24h~+12h = **13 시각**.
- **41 입력 채널** = 39 기상(13 pressure + 13 wind-x + 13 wind-y) + 1 bathymetry + 1 land mask. 출력 = 128×128 maxele 장.

### 4.5 아키텍처 — UNet-5 (PDF §3.2)

- **UNet-5** (5단 encoder/decoder), fully-convolutional encoder-decoder + skip connection. f_θ: ℝ^(41×128×128) → ℝ^(128×128) (ζ̂ = maxele).
- Encoder 5단: 각 (3×3 conv ×2 + ReLU) → 2×2 maxpool, base width C0=64, 단계마다 채널 2배·공간 1/2.
- Decoder 5단: 2×2 transposed conv 업샘플 + skip concat + (3×3 conv ×2). skip 으로 surge 극대점 국소정보 보존.

### 4.6 정량 결과 (PDF §4, Table 3)

**Holdout RMSE (m)** — global UNet 이 basin-specific local model 을 전 basin 에서 능가 (NA ~10%·NI ~28% 감소):

| basin | local(연안) | local(전점) | **global(연안)** | **global(전점)** |
|---|--:|--:|--:|--:|
| NA | 0.73 | 0.38 | 0.66 | 0.34 |
| EP | 0.26 | 0.19 | 0.23 | 0.18 |
| NI | 0.99 | 0.48 | 0.71 | 0.40 |
| SI | 0.74 | 0.49 | 0.64 | 0.48 |
| **WP** | 0.34 | 0.27 | **0.34** | **0.27** |
| SP | 0.49 | 0.31 | 0.38 | 0.28 |

→ **WP(한국 basin) global RMSE 연안 0.34m / 전점 0.27m**. 단 WP 는 global ≈ local (전지구 학습이 WP 정확도엔 추가이득 거의 없음 — NA·NI 처럼 자료부족 basin 이 더 큰 이득).

**실 태풍 검증 (PDF §4.2)**: NA 67 hurricane(2003-2023), NOAA 조위 30 storm/188 점. per-point RMSE **ADCIRC 0.22m vs UNet 0.37m**, storm-가중 **ADCIRC 0.48m vs UNet 0.52m** — ML 이 ADCIRC 에 근접하나 미달. Hurricane Hermine(2016) 예시.

### 4.7 한국 적용 함의 (본 위키 분석)

- **WP basin 학습 확정** → §6.6 "한국 zero-shot 1순위" 전제 충족. 공개 code([adcirc-rom](https://github.com/UT-CHG/adcirc-rom)) + DesignSafe model 로 한국 좌표·태풍 landfall inference 즉시 sanity check 가능.
- 유의: (a) WP holdout RMSE 0.27–0.34m 는 **synthetic 자기검증**치 — 한국 실관측 검증 부재(실 태풍 검증은 NA 만). (b) **peak surge(maxele)만** → 시계열·총수위 침수예측엔 부족(§6.6 b). (c) landfall-중심 윈도라 한국 적용 시 한국 연안 bathymetry + 태풍 track 을 STOFS-2D-Global 메시 해상도로 표현해야 함.
- 미해결: 한국/동아시아 specific 검증, WP 의 한국 인근 landfall 밀도, datum/MSL 정합.

## 5. 본 위키 storm-surge 자료와의 관계

| 본 위키 자료 | PACT (§2) 와의 접점 | StormNet (§3) 와의 접점 |
|---|---|---|
| [`01-concept.md`](01-concept.md) §3 인자 | input atmospheric forcing = §3 wind·pressure 인자 동등 | ADCIRC 출력의 offset 학습 — input = §3 인자 + ADCIRC forecast |
| [`02-theory.md`](02-theory.md) Pugh §6 + ADCIRC GWCE | GWCE 풀이 우회 (direct mapping) | GWCE 풀이 (ADCIRC) 의 **잔차만 학습** — physics layer 보존 |
| [`04-code-and-tools.md §1-2`](04-code-and-tools.md) ADCIRC NWS 모드 | 학습 hindcast 가 ADCIRC NWS=12/13/20 출력이면 pipeline (full paper 확인) | ADCIRC NWS 모드 출력 (water-level 시계열) 을 **직접 입력** — pipeline 자연 |
| [`04-code-and-tools.md §8`](04-code-and-tools.md#8-검증-metrics) RMSE/skill | RMSE/MAE 사용 = 본 위키 동일 metric 계열 | RMSE 사용 — 본 위키 동일 metric |
| [`05-examples.md`](05-examples.md) Maemi·Hinnamnor·Bolaven | 한국 적용 시 검증 case (단 US Northeast 학습) | 한국 적용 시 같음 (US Gulf Coast 학습 → 한국 transfer gap 예상) |

→ **Global LI (§4)** 는 PACT 와 같은 direct-emulator 계열(ADCIRC 출력 학습)이나, peak surge 만 산출하고 **전지구 학습**이라는 점에서 위 "transfer gap" 을 설계상 회피 — 본 위키 한국 case([`05-examples.md`](05-examples.md))에 학습 없이 적용 가능성이 가장 높은 후보(서태평양 **WP basin 학습 포함 확정**, §4.3).

## 6. 한국 적용 검토 (탐색 단계, 미실증)

PACT·StormNet·Global LI 모두 한국 미학습. 한국 적용 시 공통 고려사항:

1. **학습 데이터 부재** — 한국 ADCIRC hindcast (KMOU·KIOST 보유, 학회 발표 기준) 활용 가능성. [`04-code-and-tools §7`](04-code-and-tools.md#7-운영-예제--한국-태풍-hindcast-워크플로) 워크플로 결과인 maxele.63 + station-level fort.61 시계열을 학습 셋으로 가공 필요. 한국 학습 셋 표준 데이터 없음 (2026-05-26 기준).
2. **정점** — KHOA 13정점 ([`04-code-and-tools §4.3`](04-code-and-tools.md#43-한국-13-정점-코드)) 후보. 단 KHOA OpenAPI archive 한계 (~1년) — 학습용 long-term observation 은 KHOA Annual Report 등 별도 archive 인용 필요 ([`04-code-and-tools §4.1`](04-code-and-tools.md#41-실시간-조위-관측)).
3. **태풍 typology 차이** — US Northeast/Gulf Coast 는 hurricane (Atlantic basin), 한국은 typhoon (서태평양 basin, GAHM 권장) — physics regime 차이로 직접 transfer 효과 unknown.
4. **PACT 의 CMIP6 transfer gap** — climate downscaling 적용 시 reanalysis→CMIP6 degradation. 한국 ensemble 평가에도 동일 issue 예상.
5. **StormNet 의 bias correction 접근** — 한국 ADCIRC 자체 운영체계 (KMOU 등) 가 있다면 StormNet 류 post-processor 가 **가장 진입장벽 낮은 ML 접근**: full emulator 학습 데이터 불필요, **기존 ADCIRC 출력 + KHOA 관측 만으로 residual 학습 가능**. PACT 류 direct emulator 보다 한국 적용 우선 검토 후보.
6. **Global LI (§4) 의 zero-shot transfer 가능성** — 전지구 학습 + location-invariance 설계상, 한국 학습셋 **구축 없이** 곧바로 한국 peak surge 추정 시도 가능 (학습 데이터 부재 1번 항목을 우회). **서태평양 WP basin 학습 포함 확정**(§4.3, holdout RMSE 연안 0.34m/전점 0.27m) + 공개 code·model(§4.1). 단 한계: (a) WP 정확도는 **synthetic 자기검증**치 — 한국 실관측 검증 부재(실태풍 검증은 NA 만, §4.6), (b) **peak surge(maxele)만** → 시계열·총수위 침수예측엔 부족. 그래도 한국 좌표 inference 만으로 즉시 sanity check 가능 = **실증 진입장벽 최저**.

→ 한국 적용 경로 우선순위 (현실적): **Global LI zero-shot sanity check (즉시, 공개 model inference — WP basin 포함 확정)** → **StormNet 류 bias correction (단기, ADCIRC 운영체계 위에 얹기)** → PACT 류 direct emulator (장기, 한국 학습 hindcast 셋 구축 후).

## 7. 추가 ML surge 모델 카탈로그

§2-4 가 deep-dive 3종(PACT·StormNet·Global LI)이라면, 본 §는 그 외 ML surge 모델 카탈로그.

### 7.1 DeepSurge (Rice·Balaguru·Leung et al. 2025, PNNL) — RNN 전역 surge + climate risk (verified, PDF read 2026-06-12)

arxiv:2506.13963 (2025-06-16). DeepSurge = **convolutional + recurrent** 신경망으로 **North Atlantic basin 임의 위치**의 peak surge 예측 (기존의 단일 bay/지점별 학습 한계 탈피 — "any given location" 일반화).

- 학습/검증: ADCIRC 출력. out-of-sample **R² 81.5% / MAE 0.25m**, ADCIRC 대비 **최대 96× 가속**. NOAA 조위 독립검증서 ADCIRC 와 comparable skill.
- risk: **RAFT**(Risk Analysis Framework for TCs, Xu 2024)로 **900,000 synthetic TC** 생성(기존 최대 규모) → DeepSurge 로 미국 연안 100년 surge risk + **TC 거동·해수면 변화(세기말)** 투영, inundation model 결합.
- PACT(§2) 와 대비: 둘 다 direct emulator 이나 DeepSurge 는 NA-wide 위치유연 RNN + 대규모 synthetic risk(900k), PACT 는 graph-transformer + CMIP6 downscale.

### 7.2 HURRI-GAN (Nader·Dawson et al. 2026) — TimeGAN 공간 bias 외삽 (verified, PDF read 2026-06-12)

arxiv:2603.06649 (2026-02-27). **TimeGAN**(time-series GAN)으로 ADCIRC 의 systemic bias 를 보정하되, 핵심 novelty = **water-level gauge station 밖 공간 위치로 bias correction 을 외삽**.

- StormNet(§3, 동일 Dawson/Kaiser 그룹)의 **시간축** offset 예측에 대한 **공간축 짝** — 둘 결합 시 full spatiotemporal bias correction. ADCIRC mesh 해상도/runtime 절감 동기(정확도 손실 없이).
- 결과: 외삽 target 위치서 low RMSE, ADCIRC 수위에 보정 적용 시 다수 test gauge 에서 예측 개선.
- 코드: <https://github.com/NoujoudNader/Extrapolation_GAN> · Zenodo doi:10.5281/zenodo.15634528.

### 7.3 Regional surge surrogate — 효율적 학습전략 (Liu·Johnson et al. 2025, Purdue) ★ (verified, PDF read 2026-06-12)

arxiv:2511.07269. **진화 landscape + climate 시나리오** 하 surge surrogate 학습. 핵심 기여 = **학습 효율화 전략** — 비싼 ADCIRC 시나리오 run 수를 줄이며 surrogate 정확도 유지:

- ★**헤드라인 결과(2026-07-19 원문 재대조로 보강)**: 3차원 동시 축약 — **격자점 80,000→5,000 · 입력특성 12→10 · storm 90→60** = 원본의 **약 5%** 로 **상관계수 0.94** 달성.
- 선별 기법은 축별로 다름: **격자점 = k-means**, **storm = k-medoids** + variance-based adaptive sampling(active learning). (구판은 k-medoids 만 기재)
- ⚠ **"90개 subset"은 이 논문의 산출물이 아님** — CHS-LA 연구(Nadal-Caraballo 2022)의 기존 **CMP2023 subset = 출발 baseline** 이며, 본 논문은 그 90 을 60 으로 더 줄인 것이다(구판 오귀속 정정).
- hazard curve 정량 = surrogate × JPM integral(Nadal-Caraballo 2022) 또는 surrogate 직접.
- **§A.4 wave surrogate(2510.12986)와 동일 Purdue Johnson group** — 다만 ⚠**"surge surrogate 출력 → wave surrogate 입력 연쇄(surge→wave coupled emulation)"는 본 논문에 근거가 없다**(2026-07-19 전문 재대조: 전문에서 "wave"는 선행연구 나열 중 1회뿐, 결합 emulation 논의 전무). 동일 그룹이라는 사실에서 나온 **위키 자체 추론**이므로 원문 인용과 구분 표기 — 검증 전 인용 금지 `[source-needed]`. [[../../models/SWAN/web-refs/swan-ml-surrogate-models]] §A.4.

### 7.4 FLO — data-driven LAM surge (Norwegian Met Institute 2026) ★ (verified, PDF read 2026-06-12)

arxiv:2601.02090 (Kristensen·Matuszak·Tedesco·Kullmann·Röhrs). **North/Norwegian/Barents Sea** data-driven storm surge model:

- **Anemoi framework**(ECMWF ML weather-forecasting 프레임워크) + **graph neural network(GNN)** 기반 **limited-area model(LAM)**.
- 자료·학습: **NORA(3km Norwegian Reanalysis) + NORA-Surge hindcast**(DA 미적용)는 **43년(1979-2022) 커버**이나 ★**학습·검증은 20년(1990-2009)**, **2010-2022 는 평가용 유보**(2026-07-19 원문 재대조 — 구판 "학습 43년"은 커버기간을 학습기간으로 오기). >90 유럽 연안 조위 gauge + NORA-Surge 검증, 수치모델과 comparable 정확도.
- 저자 솔직 평가: "forecast skill 큰 향상은 아니나, surge 예보를 **수치 → ML 기반으로 전환**하는 발판" = 향후 obs/DA 통합 유연성. StormNet/HURRI-GAN(post-process)과 달리 **GNN 직접 emulator**.

### 7.5 Tampa Bay CNN/RNN 비교 (Farhang Ghahfarokhi et al. 2024) — direct emulator architecture 비교 (verified, full PDF read 2026-06-18)

arxiv:2408.05797v1 (2024-08-11, Farhang Ghahfarokhi·Sonbolestan·Zamanizadeh, 9p). **CNN-LSTM / LSTM / 3D-CNN** 세 deep learning architecture 를 Tampa Bay surrogate surge 예측에서 비교.

- **데이터/정점**: **단일 정점 NOAA 8726520 St. Petersburg, FL**(Tampa Bay), 2011~2023 말 연속 관측. **train 2011-2020 / test 2021~end**(Hurricane Ian 2022 test 기간 포함). 입력 = wind + atmospheric pressure + 이전 sea level.
- **학습 config**: 3 모델 모두 Adam lr=0.001, **15 epochs**. CNN-LSTM=conv(공간)→flatten→LSTM(시간), 3D-CNN=2×Conv3D(64 filter)+batch norm.
- **결과 (Table 1)**: **CNN-LSTM 최우수** (test loss 0.010, R²=0.84). LSTM 은 train R²=0.88 최고지만 generalization 약함(test loss 0.014, test R²=0.77), 3D-CNN(test loss 0.011, R²=0.82)은 극한조건 불안정.
- **Hurricane Ian** case (Tampa Bay 에 −1.5 m **negative surge**) 에서 CNN-LSTM robustness 입증 — 음의 wind setup(역류 수위저하) case 를 명시 다룸.
- PACT(§2)·DeepSurge(§7.1) 와 관계: 동일 direct-emulator 계열이나 single-station(St. Petersburg) 한정 + architecture 비교가 초점 — location-invariance(§4)·peak-aware(§2) 같은 일반화 기법 미적용.
- 출처: <https://arxiv.org/abs/2408.05797>

### 7.6 Climate Adaptation-Aware Flood (Hassan·Karapetyan et al. 2025) — 연안 flood SLR·적응 시나리오 CNN (verified, full PDF read 2026-06-18)

arxiv:2510.26017v1 (2025-10-29, NYU Abu Dhabi Div. of Engineering, 57p). 연안도시 침수를 **변동 SLR projection + shoreline adaptation 시나리오** 조건부로 예측하는 CNN.

- **Abu Dhabi + San Francisco** 두 지역으로 geographical generalization 입증. flood depth map **MAE 를 SOTA 대비 평균 ~20% 감소** (abstract verbatim).
- **adaptation 분류 체계** (저자): protect(seawall·levee·storm barrier armoring) / accommodate(rising water) / retreat / avoid — 본 모델은 **방어구조물의 최적 공간배치**(어느 shoreline segment 를 fortify 할지) 시나리오를 조건 입력으로 받음 (예: Lower Manhattan 2.5 mile fortification 사례 언급).
- §2-4(surge emulator) 와 차이: surge time-series 가 아니라 **연안 flood depth map** (SLR·적응 시나리오 조건부) 산출 — 도시 planning/적응 의사결정 도구 지향. 한국 연안도시 적응계획(방조제·호안 segment 배치)에 개념적 전이가치.
- 출처: <https://arxiv.org/abs/2510.26017> · Project: <https://caspiannet.github.io/>

### 7.7 CLDNet — flood digital-twin SWE surrogate (Si·Chen et al. 2026) ⚠ surge 아님(하천 flood, 기법 전이용) (verified, full PDF read 2026-06-18)

arxiv:2605.13761v1 (2026-05-13, Si·Qiu·Sallam·Feinstein·He·Yan·Chen, 32p). Conditional **L**atent **D**ynamics **Net**work — **강우 구동 저차원 latent neural ODE** + 지형(고도·경사·Manning roughness) 조건부 **coordinate-based decoder** 로 임의 query 점의 depth·discharge 복원.

- Pointwise(meshless) decoding 으로 memory 가 grid 크기와 decouple → 불규칙 watershed native 처리, gauge 좌표 직접 query(raster snapping 불요).
- **검증 2종**: (a) **Texas synthetic 250,000-cell** 벤치마크 — regular-grid **VAE-ConvLSTM·FNO baseline 능가**(둘은 Cartesian grid 전제라 불규칙 watershed 부적용), (b) **Des Plaines River basin**(4,188,840 active cell) **114 real-rainfall Stage IV storm** 케이스 — 96h 전 basin 예측 **~29초**(2D SWE solver ~55분 대비 **~115× 가속**), **CSI ≈86%@0.5m** inundation threshold.
- ⚠ **연안 surge 아님** — 하천/강우(pluvial-fluvial) flood. 본 §에 수록 이유: latent neural ODE + 좌표 decoder + 불규칙 메시 native 라는 **SWE surrogate 기법**이 연안 inundation(maxele·총수위 침수도) emulation 으로 전이 가능. Global LI(§4)의 격자 maxele 산출 vs CLDNet 의 mesh-free 좌표 query 는 상보적 설계.
- 출처: <https://arxiv.org/abs/2605.13761>

### 7.8 미트리아지 / placeholder

- Neural operator (DeepONet/FNO) — `operator-learning` (2604.06433, [[../../models/SWAN/web-refs/swan-ml-surrogate-models]] §A.2 DeepONet 에 **verified**)
- LSTM / sequence model station-level surge (StormNet baseline 류, Tiggeloven et al. 미확인)
- PINN (physics-informed) for SWE / ensemble downscaling(GCM→local) / storm-track conditioned(GAHM→ML)

추적: `research/watchlist/` 에 ML emulator author + arxiv cs.LG ∩ physics.ao-ph 카테고리 등록 후보. 현재 [[../../research/watchlist/repo-myroms-roms]] · [[../../research/watchlist/repo-noaa-emc-ww3]] 등 model repo 위주 — `topic-ml-storm-surge-emulators.md` 신설은 향후 후보.

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
