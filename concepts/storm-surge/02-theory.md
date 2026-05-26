---
title: "Storm Surge 이론 — shallow water + IB + wind stress + tide-surge interaction (Pugh Ch 6-7)"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "Pugh 'Tides, Surges and Mean Sea-Level' Ch 6 (textbook/md/sea-level.md p.184-230) 직접 인용 — §6:1 Weather effects, §6:3 Atmospheric pressure (eq. 6:5), §6:4 Wind stress, §6:5 Numerical modelling, §7:8 Tide-surge interaction. ADCIRC Theory (Luettich & Westerink 2004) GWCE form. textbook/md/sea-level.md line 7370 ('one millibar will produce a decrease in sea-level of one centimetre') + line 7374 (Proudman shelf model amplification) 직접 인용. §3.4 추가 (2026-05-26): arXiv:2605.03933v1 (Sathia & Giometto 2026, 제출일 2026-05-05, 카테고리 physics.flu-dyn) abstract 직접 fetch (WebFetch 2026-05-26) — 새 PBL height scaling 두 식 u_*/β (neutral) + u_*/√(βN) (stable) + 평균 2.5% relative error verbatim 인용. ADCIRC GAHM BL Vmax 환산 cross-ref 와 한국 태풍 적용 검토는 자체 분석."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-26
verification_by: "Claude Opus 4.7 (1M context) — Pugh 본문 직접 인용 + ADCIRC theory 매핑 + §3.4 arxiv abs 직접 fetch"
verification_date: 2026-05-26
related:
  - concepts/storm-surge/01-concept.md
  - concepts/tides/02-theory.md
  - models/ADCIRC/raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf
---

# Storm Surge 이론 — Pugh §6-7 정형

> 본 §는 [`01-concept.md`](01-concept.md) 의 5 인자 정성 설명을 equation level 로 정형화. 모든 식은 Pugh 1987 (textbook/md/sea-level.md) 의 원본 번호 인용.

## 1. 출발점 — shallow water equations

지구 회전 효과 포함된 shallow-water momentum + continuity (Pugh §3:5, eq. 3:23-3:25 + §6:5 numerical modelling 인용):

$$
\frac{\partial \bar{u}}{\partial t} - f\bar{v} = -g \frac{\partial \eta}{\partial x} - \frac{1}{\rho}\frac{\partial P_A}{\partial x} + \frac{\tau_{wx}}{\rho H} - \frac{\tau_{bx}}{\rho H}
$$

$$
\frac{\partial \bar{v}}{\partial t} + f\bar{u} = -g \frac{\partial \eta}{\partial y} - \frac{1}{\rho}\frac{\partial P_A}{\partial y} + \frac{\tau_{wy}}{\rho H} - \frac{\tau_{by}}{\rho H}
$$

$$
\frac{\partial \eta}{\partial t} + \frac{\partial (H\bar{u})}{\partial x} + \frac{\partial (H\bar{v})}{\partial y} = 0
$$

기호:
- $\eta$ = sea surface elevation (storm surge + tide)
- $\bar{u}, \bar{v}$ = depth-averaged velocity (m/s)
- $f = 2\Omega \sin\phi$ = Coriolis parameter
- $P_A$ = 대기압 (Pa)
- $\tau_w$ = surface wind stress
- $\tau_b$ = bottom stress
- $H = h + \eta$ = total depth (수심 + 표고)
- $\rho \approx 1025$ kg/m³ (해수 밀도)

ADCIRC 는 위 식의 unstructured finite-element 형 (GWCE = Generalized Wave Continuity Equation form) 풀이. Source: `models/ADCIRC/raw/source_code/adcirc/src/momentum_eqn.F` 및 theory PDF §3.1.

## 2. Inverse Barometer Effect (Pugh §6:3)

### 2.1 정적 응답 (no currents 평형)

평형 가정 시 momentum 식의 시간 미분·관성 항 0 → pressure gradient = sea-level slope (Pugh eq. 6:3-6:5):

$$\rho g \frac{\partial \eta}{\partial x} = -\frac{\partial P_A}{\partial x}$$

적분 → IB 식 (Pugh eq. 6:5, p.194):

$$\boxed{\eta_{IB} = -\frac{\Delta P_A}{\rho g}}$$

수치 결과 (Pugh, p.194 직접 인용):

> "An increase in atmospheric pressure of one millibar will produce a decrease in sea-level of one centimetre. This response of sea-level is called the inverted barometer effect." (Pugh §6:3)

> "During a typical year extratropical atmospheric pressures may vary between values of 980 mb and 1030 mb. Compared with a Standard Atmosphere of 1013 mb, this implies a range of static sea levels between +0.33 m and -0.17 m." (Pugh §6:3)

### 2.2 한국 적용 — 태풍 IB surge

| 태풍 (한국) | 중심기압 (mb) | IB 정적 surge (m) | 분류 |
|---|---:|---:|---|
| Maemi 2003 | 950 | +0.63 | extratropical 보다 큼 |
| Hinnamnor 2022 | 920 | +0.93 | extreme tropical |
| typical 가을 태풍 | 970-980 | +0.33~+0.43 | average |

배경기압 1013 mb 기준. ADCIRC 의 `PRBCKGRND = 1013.0 mb` constant (`models/ADCIRC/raw/source_code/adcirc/src/constants.F90:54`).

### 2.3 동적 응답 — Proudman shelf model amplification

대기압 변동이 빠르게 움직일 때 (예: 빠른 태풍) 정적 IB 보다 큰 동적 응답 가능 (Pugh §6:3, p.197 인용):

> "A simple but elegant theoretical model of the response may be derived from the hydrodynamic equations for a shelf of constant depth (Proudman, 1953)." (Pugh §6:3)

대기압 disturbance 가 속도 $C_A$ 로 이동 시 amplification:

$$A = \frac{1}{1 - C_A^2/(gD)}$$

- $C_A^2/(gD) = 1$ 시 이론적 무한 amplification (resonance — 실제는 friction 으로 damped)

수치 예 (Pugh §6:3 인용):

> "The amplification factor for a disturbance moving at 20 km per hour over water of 50 m depth is 1.07, but if the depth falls to 25 m the factor increases to 1.14. The resonant condition for a disturbance travelling at a speed of 20 km per hour requires a very shallow depth of 3.0 m." (Pugh §6:3)

→ 한국 서해 (수심 20-50m) 가 동해 (1000m+) 보다 동적 amplification 가능성 큼. 단, 한국 태풍은 보통 25-40 km/h 이동.

## 3. Wind Stress (Pugh §6:4)

### 3.1 Bulk parameterization

표층 wind stress:

$$\tau_w = \rho_a C_D U_{10}^2$$

- $\rho_a \approx 1.2$ kg/m³
- $U_{10}$ = 10 m altitude 풍속 (m/s)
- $C_D$ = drag coefficient

$C_D$ 의 풍속 의존성 (Pugh §6:4 + Garratt 1977):

| $U_{10}$ (m/s) | $C_D \times 10^3$ | 비고 |
|---:|---:|---|
| 5 | 0.8-1.0 | light winds |
| 10 | 1.2-1.4 | typical |
| 20 | 1.8-2.0 | strong wind |
| 30 | 2.5-3.0 | hurricane/typhoon |
| 50 | 3.0-3.5 | extreme (saturate 가능) |

Garratt 1977 fit:

$$C_D \times 10^3 = 0.51 + 0.080 \cdot U_{10}$$ (m/s)

ADCIRC 는 Garratt 또는 Powell 2003 등 옵션 (`fort.15` `IM` parameter).

### 3.2 Wind set-up — shallow water

momentum (정상상태, no Coriolis) 식 → wind setup gradient:

$$\frac{\partial \eta}{\partial x} = \frac{\tau_w}{\rho g H} - \frac{\tau_b}{\rho g H}$$

장구간 평균·bottom stress 무시 시:

$$\boxed{\Delta \eta_{wind} \approx \frac{\rho_a C_D U^2 \cdot L}{\rho g H}}$$

- $L$ = wind fetch (km)
- $H$ = 평균수심

**한국 서해 적용** ($U = 30$ m/s 태풍, $L = 200$ km, $H = 30$ m):

$$\Delta\eta_{wind} = \frac{1.2 \times 2.5\times10^{-3} \times 900 \times 200000}{1025 \times 9.81 \times 30} = \frac{540{,}000}{301{,}702} \approx \mathbf{1.79 \text{ m}}$$

→ 서해 천해에서 wind set-up 만 +1.8 m 가능. IB +0.6 m + wave setup +1 m + tide spring high → 큰 flood 위험.

**동해 적용** ($U = 30$ m/s, $L = 200$ km, $H = 1000$ m):

$$\Delta\eta_{wind} = \frac{540{,}000}{10{,}056{,}717} \approx 0.054 \text{ m} = 5.4 \text{ cm}$$

→ 동해는 wind set-up 30 배 작음. 동해 storm surge 는 주로 IB + Coriolis 효과.

### 3.3 ADCIRC 의 wind input

`fort.15` 의 `NWS` 파라미터로 wind input source 결정:

| NWS | source | 비고 |
|---|---|---|
| 0 | no meteo | 조석만 |
| 12 | OWI ASCII | bulk wind/pressure 분리 |
| 13 | OWI NetCDF | 동일, NetCDF |
| 14 | GRIB2 | 직접 |
| 19 | AHM (Asymmetric Holland Model) | parametric TC, single B per record |
| 20 | GAHM (Generalized AHM) | quadrant-dependent B, BL Vmax — **권장 modern** |
| 29 | AHM + OWI | hybrid (vortex + background) |
| 30 | GAHM + OWI | 동일, GAHM 사용 |

상세 분석 — `_staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge.md (at commit a9618df^)` (source-code level, NWS 모든 모드 + Holland B + ATCF Best Track + IB suppression `NOIVB`).

### 3.4 Hurricane PBL height scaling — Sathia & Giometto 2026 (arXiv:2605.03933)

§3.1 bulk drag 는 surface (10 m) wind 기준 $\tau_w = \rho_a C_d U_{10}^2$. 그러나 hurricane wind profile 은 surface 부터 PBL top 까지 빠르게 변하며, **PBL height** $h_{BL}$ 가 wind drag · momentum exchange 의 scale 을 결정한다. ADCIRC AHM/GAHM (§3.3, NWS=19/20) 의 BL Vmax → 10-m surface wind 환산도 PBL 의 vertical structure 가정에 의존한다.

#### 3.4.1 새 scaling 공식 — Sathia & Giometto 2026

저자 주장 (verbatim, arXiv:2605.03933v1 abstract):

> "Existing models rely on a height scale derived with the assumption of a constant eddy viscosity, a strong simplification that limits physical accuracy."

저자 제안 (hurricane outside the eyewall):

| 성층 | PBL height scaling |
|---|---|
| **Neutral stratification** | $h_{BL} \sim u_\star / \beta$ |
| **Stable stratification** | $h_{BL} \sim u_\star / \sqrt{\beta N}$ |

기호 (verbatim):

- $u_\star$ = friction velocity (m/s)
- $\beta$ = **absolute fluid vorticity** (planetary $f$ + relative vorticity; hurricane core 에서 크게 증가)
- $N$ = Brunt-Väisälä frequency of the background stratification ($s^{-1}$)

저자 의의 (verbatim):

> "These scalings are analogous to those used in the literature for neutrally and stably stratified turbulent atmospheric boundary layers."

→ ABL (atmospheric boundary layer) scaling 의 hurricane outside-eyewall 적용. constant eddy viscosity 가정 회피.

#### 3.4.2 Validation 정확도 (verbatim)

저자 보고 (arXiv:2605.03933v1 abstract):

> "The formulae are backed by analytical derivation and validated against velocity profiles from large-eddy simulations and field observations. They are predictive to within 2.5% relative error on average and yield a good collapse of the simulated and observational velocity profiles away from the surface."

요약:

- 검증 자료: LES (large-eddy simulations) + field observations
- 평균 상대오차: **2.5%** (eyewall 외부)
- 적용 범위: "away from the surface" 영역에서 velocity profile collapse

#### 3.4.3 본 위키 적용 — ADCIRC GAHM 와의 연결

ADCIRC GAHM (§3.3, NWS=20) 의 wind profile 환산 단계:

- **GAHM 출력**: cyclone boundary layer 평균 Vmax (Holland 1980 + quadrant-dependent B)
- **ADCIRC 입력**: 10-m surface wind ($\tau_w$ 계산용)
- **환산**: BL Vmax → 10-m wind reduction factor — **PBL 의 vertical structure 가정 필요**
  - 현재 일반적: Powell et al. 2003 reduction factor ~0.85 (`models/ADCIRC/raw/manuals/`)
  - reduction factor 의 height-dependence 는 $h_{BL}$ 가정에 의존

따라서 Sathia & Giometto (2026) 의 새 $h_{BL}$ scaling 의 의의:

1. **GAHM-derived BL Vmax → 10-m wind 환산의 height-dependent reduction factor 개선 후보** — 현재 constant eddy viscosity 기반 가정을 $u_\star/\beta$ (neutral) 또는 $u_\star/\sqrt{\beta N}$ (stable) 로 대체
2. 한국 태풍 (Maemi 2003, Hinnamnor 2022 — `05-examples.md` §1·§2; Bolaven 2012 — `05-examples.md` §3) 의 **eyewall 외부 surge response** 정확화
3. ADCIRC 의 wind input 단계 (`fort.22` AHM/GAHM record) 후속 개선 — paper 가 최근 (2026-05-05 제출) 이라 직접 적용 사례 아직 없음

#### 3.4.4 한계 (verified 범위 명시)

본 §3.4 는 **arXiv:2605.03933v1 abstract 직접 인용** 수준. 다음은 abstract 미명시이며 full PDF read 후 보강 가능:

- analytical derivation 의 정식 length scale 유도 단계
- LES setup (격자, $Re_\tau$, 모델 풍속 범위, 강제 hurricane)
- 비교한 기존 expressions 의 구체명 (Garratt 1992? Zilitinkevich 1972? Rotunno & Bryan 2012?)
- eyewall **내부** 적용 가능성 — abstract 는 명시적으로 "outside the eyewall" 만
- coastal resilience / wind engineering 적용 구체 사례

ADCIRC source code 변경은 아직 없음 — paper 의 reduction factor 통합은 후속 연구 가능성.

## 4. Tide-Surge Interaction (Pugh §7:8)

### 4.1 비선형 결합 원인

천해에서 두 신호 (tide + surge) 가 비선형 결합. 3 가지 원천 (Pugh §7:8):

**(1) Bottom friction quadratic term**:

$$\tau_b = \rho C_f u |u|$$

tide-only velocity $u_t$ + surge velocity $u_s$ 일 때:

$$|u_t + u_s|(u_t + u_s) \neq u_t |u_t| + u_s |u_s|$$

→ tide 와 surge 가 결합해서 추가 dissipation term 발생.

**(2) Total depth modulation**:

shallow water wind-setup 식 $\Delta\eta \propto 1/H$. tide phase 따라 $H = h + \eta_t$ 변동:
- spring high tide ($H$ 큼) → wind setup 작음
- spring low tide ($H$ 작음) → wind setup 큼

**(3) Advection term**:

$$\bar{u} \frac{\partial \bar{u}}{\partial x}$$ 의 비선형 결합

### 4.2 한국 서해 특수성

- 큰 tide range (인천 +5 m spring tide range) + 천해 (20-50m) → tide-surge interaction 강함
- Lingling 2019, Bolaven 2012 등 서해 태풍 시 관측 surge 가 단순 IB+wind+tide 합산보다 작거나 큰 phase-dependent 변동

ADCIRC 의 처리: shallow water 비선형 항 모두 포함, tide forcing + storm vortex 같은 grid 에서 결합 계산 — separation 없는 통합.

## 5. Numerical Modelling (Pugh §6:5)

### 5.1 ADCIRC Generalized Wave Continuity Equation (GWCE)

Luettich & Westerink (2004) eq. 17:

$$\frac{\partial^2 \eta}{\partial t^2} + \tau_0 \frac{\partial \eta}{\partial t} + \nabla \cdot \mathbf{J} - U_{x0}\frac{\partial \eta}{\partial t}\frac{\partial h}{\partial x} - U_{y0}\frac{\partial \eta}{\partial t}\frac{\partial h}{\partial y} = 0$$

여기서 $\mathbf{J}$ 는 continuity + momentum 합성 flux. $\tau_0$ = numerical weighting parameter (사용자 입력, 일반 $\tau_0 = 0.01$).

장점: noise 줄이고 numerical efficiency.

### 5.2 Finite element grid

ADCIRC 의 unstructured triangular grid → 한국 연안 같은 복잡 지형 효율적 표현. 한국 적용 예:
- HSOFS (Hurricane Surge On the Fly System) — 미국 형태, 한국 유사 grid 작업 가능
- 한국 서해 mesh — `models/ADCIRC/raw/source_code/adcirc-testsuite/` 안 예제 (testsuite 16GB, .gitignore 됨, 별도 clone)

## 6. Surge envelope vs water level

본 분석에서 storm surge 는 **maximum surge envelope** $\max_t \eta_{surge}(x, y, t)$ 가 주된 관심사 (특정 시점 elevation 보다는 storm 전체 영향의 spatial pattern).

ADCIRC outputs:
- `fort.63` = elevation time series (한 정점)
- `fort.74` = wind velocity
- `maxele.63` = **maximum elevation envelope** — surge map 생성에 핵심
- `maxvel.63` = max velocity envelope

## 7. 인용 정형

본 §의 핵심 식:
- IB: $\eta_{IB} = -\Delta P_A / (\rho g)$ — (Pugh eq. 6:5, p.194)
- 1 mb = 1 cm: textbook/md/sea-level.md line 7370 직접
- Proudman amplification: $A = 1/(1 - C_A^2/gD)$ — Pugh §6:3 p.197
- Wind stress: $\tau_w = \rho_a C_D U^2$ — Pugh §6:4 + Garratt 1977
- Wind setup: $\Delta\eta \propto U^2 L / H$
- Tide-surge interaction 3 sources — Pugh §7:8

## 8. 관련 문헌

- Pugh, D.T. (1987) "Tides, Surges and Mean Sea-Level" — Ch 6-7 directly cited
- Proudman, J. (1953) "Dynamical Oceanography" — shelf shallow water model
- Luettich, R.A. & Westerink, J.J. (2004) ADCIRC Theory v44 — GWCE
- Garratt, J.R. (1977) "Review of drag coefficients" — $C_D(U)$ formula
- Powell, M.D., Vickery, P.J., Reinhold, T.A. (2003) "Reduced drag coefficient for high wind speeds in tropical cyclones" Nature 422:279-283 — extreme wind $C_D$ saturation

## 9. 연결

- [`01-concept.md`](01-concept.md) — 5 인자 정성 정리
- [`03-analysis-methods.md`](03-analysis-methods.md) (예정) — tide-surge separation algorithm, joint probability
- [`04-code-and-tools.md`](04-code-and-tools.md) (예정) — ADCIRC NWS 운영
- [`concepts/tides/02-theory.md`](../tides/02-theory.md) §8.6 — SLR + storm surge baseline
- [`models/ADCIRC/source-analysis/storm-surge/`](../../models/ADCIRC/source-analysis/storm-surge/) — 7개 NWS source-code 분석 (promote 완료 commit a9618df)
