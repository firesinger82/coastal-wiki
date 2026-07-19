---
title: "Storm Surge 이론 — shallow water + IB + wind stress + tide-surge interaction (Pugh Ch 6-7)"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "Pugh 'Tides, Surges and Mean Sea-Level' Ch 6 (textbook/md/sea-level.md p.184-230) 직접 인용 — §6:1 Weather effects, §6:3 Atmospheric pressure (eq. 6:5), §6:4 Wind stress, §6:5 Numerical modelling, §7:8 Tide-surge interaction. ADCIRC Theory (Luettich & Westerink 2004) GWCE form. textbook/md/sea-level.md line 7370 ('one millibar will produce a decrease in sea-level of one centimetre') + line 7374 (Proudman shelf model amplification) 직접 인용. §3.4 추가 (2026-05-26): arXiv:2605.03933v1 (Sathia & Giometto 2026, 제출일 2026-05-05, 카테고리 physics.flu-dyn) abstract 직접 fetch (WebFetch 2026-05-26) — 새 PBL height scaling 두 식 u_*/β (neutral) + u_*/√(βN) (stable) + 평균 2.5% relative error verbatim 인용. ADCIRC GAHM BL Vmax 환산 cross-ref 와 한국 태풍 적용 검토는 자체 분석. **§3.4.4~3.4.8 추가 (2026-05-28)**: arXiv:2605.03933v1 **full PDF 34p 직접 fetch** (curl + Read tool) — derivation eq 5-32 (Pollard 1973 P73 응용 + slab model + Ri_b closure) + LES setup Appendix A (256×256×512 grid, Bou-Zeid Smagorinsky, CFL=0.075) + Table A1 216 stratified sims + Appendix B 16 neutral/mild (Set A C_R=0.58, avg 6% error / R²=0.99 / RMSE=6.92m) + parity plot stable C_S=1.2 (R²=0.99 / bias=1.04m / RMSE=23.5m) + characteristic heights (v_max 65-85% / inflow peak 6-20% of h) + eq 41-43 R-scaling h~R^((1-n)/2) + eq 44 K_m~R^(-2n) + combined formula B1 p=4 (vs ABL p=2). Wind engineering / coastal resilience 응용 명시. 비교 expressions 구체화 (Meng 1995 / Kepert 2001 / Pollard 1973 / Sous 2013 / Zilitinkevich 2007 외 closure model papers)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-26
verification_by: "Claude Opus 4.7 (1M context) — Pugh 본문 직접 인용 + ADCIRC theory 매핑 + §3.4 arxiv abs 직접 fetch + §3.4.4~3.4.8 PDF 34p full read (2026-05-28)"
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

★**2026-07-19 출처 정정**: 구판은 아래 표와 `C_D×10³ = 0.51 + 0.080·U₁₀` 식을 **"Pugh §6:4 + Garratt 1977"** 로 귀속했으나, **교재 원문(sea-level.md) 전문 grep 결과 "Garratt" 0건**이며 표·식 모두 교재에 없다. Pugh 가 제시하는 유일한 drag 식은 아래 Smith & Banke 다.

**Pugh §6:4:2 원문 (sea-level.md:7454-7456) — 실제 교재 식**:

$$10^3 C_D = 0.63 + 0.066\, W_{10} \qquad (2.5\ \mathrm{m/s} < W_{10} < 21\ \mathrm{m/s})$$

> "Acceptable values for C_D (**Smith and Banke, 1975**) are given by …" — 교재는 drag 가 풍속 제곱보다 약간 빠르게 증가하며, 이는 파고 증가에 따른 표면조도 증가로 설명된다고 서술. ⚠**적용범위 상한 21 m/s** — 태풍역(30 m/s+) 적용은 외삽임에 유의.

구판 표(5→0.8-1.0 … 50→3.0-3.5)는 위 식에서 역산된 값으로 보이나(U=5→0.91, 10→1.31, 30→2.91) **교재 미수록이므로 삭제**. `0.51 + 0.080·U₁₀` 형태는 통상 인용되는 Garratt 형과도 달라 **원전 미확인** `[source-needed]` (Garratt 1977, *Mon. Wea. Rev.* 105:915-929 — DOI 실재 확인, AMS 결제벽으로 본문 미확보).

ADCIRC 의 wind drag 옵션(Garratt 식·Powell 2003 등)은 [`models/ADCIRC/`](../../models/ADCIRC/) canonical 참조 — ★`fort.15` `IM` 은 **drag 선택자가 아니라 모델 정식화(2DDI/3D) 선택자**이며 drag 는 `/metControl/ WindDragLimit` 계열이다(2026-07 정정 반영, [[../../models/ADCIRC/source-analysis/adcirc-3d-mode]]).

### 3.2 Wind set-up — shallow water

momentum (정상상태, no Coriolis) 식 → wind setup gradient:

$$\frac{\partial \eta}{\partial x} = \frac{\tau_w}{\rho g H} - \frac{\tau_b}{\rho g H}$$

장구간 평균·bottom stress 무시 시:

$$\boxed{\Delta \eta_{wind} \approx \frac{\rho_a C_D U^2 \cdot L}{\rho g H}}$$

- $L$ = wind fetch (km)
- $H$ = 평균수심

★**교재 자체의 worked example (Pugh §6:4:2, sea-level.md:7494)** — 아래 "한국 서해 적용"과 **완전히 동일한 조건**(200 km fetch · 수심 30 m, "대략 남부 북해의 규모")을 교재가 이미 풀어 두었다:

> "For a Strong Gale (Beaufort Force Nine, **22 m/s**) blowing over 200 km of water which has a depth of 30 m … the increase in level would be **0.85 m**. If the wind speed increased to Storm (Beaufort Force Eleven, **30 m/s**) the level of increase would be **1.60 m**."

**한국 서해 적용** ($U = 30$ m/s 태풍, $L = 200$ km, $H = 30$ m) — 교재값 **1.60 m** 를 기준으로 삼는다.

구판은 같은 조건에 $C_D = 2.5\times10^{-3}$ 를 넣어 **1.79 m** 를 제시했으나, 그 $C_D$ 는 위에서 삭제된 미출처 표에서 온 값이고 **교재 자신의 답(1.60 m)이 존재한다는 사실도 누락**돼 있었다(2026-07-19 정정). 교재 식(Smith & Banke)으로 30 m/s 를 대입하면 $C_D \approx 2.6\times10^{-3}$ 이나 이는 식의 적용범위(21 m/s) 밖 외삽이며, 교재가 어느 $C_D$ 로 1.60 m 를 얻었는지는 본문에 명시되지 않았다 `[source-needed]`.

→ 서해 천해에서 wind set-up 만 **+1.6 m 규모** 가능. IB + wave setup + 대조 만조가 겹치면 큰 범람 위험 (각 성분 정량은 해당 절 참조).

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

#### 3.4.4 Analytical derivation (PDF §2, full PDF 인용)

PDF §2.a Background + §2.b Derivation 직접 인용 (2026-05-28 full PDF fetch).

**Naive mixing-length argument**:

- Time-averaged linearized HBL eq (Kepert 2001, Sathia & Giometto 2025): $\alpha(V_g-v) = d\tau_{xz}/dz$ (eq 5), $\beta u = d\tau_{yz}/dz$ (eq 6)
- $\alpha = f + 2V_g/R$ (twice absolute angular velocity), $\beta = f + (1-n)V_g/R$ (absolute fluid vorticity, Smith & Montgomery 2020) — eq 7
- $K_m \sim u_* l_T$, mixing length $l_T = h$ (neutral) or $l_T = u_*/N$ (stable, Zilitinkevich 2007)
- **Naive 결과**: $h \sim u_*/I$ (neutral), $h \sim u_*/\sqrt{IN}$ (stable), where $I = \sqrt{\alpha\beta}$ (inertial freq, eq 10)
- 저자 결론: naive 식은 **LES와 inconsistent**

**제안된 식 (eq 11, 12)** — $I$ 가 아닌 $\beta$ 가 분모:

$$h = C_R\,\frac{u_*}{\beta}\,(\text{neutral}), \qquad h = C_S\,\frac{u_*}{\sqrt{\beta N}}\,(\text{stable})$$

**Stable case derivation (Pollard et al. 1973 응용)**:

1. Slab model 적분 with Leibniz rule (eq 15-17)
2. Surface drag $\tau_{xz}|_0 = C_D \bar{u}\sqrt{\bar{u}^2+\bar{v}^2}$, linearize → drop Rayleigh damping (eq 22)
3. Top stress zero (Haiden & Whiteman 2005, eq 23)
4. Solve $\tilde{u}=\tilde{v}=0$ IC → $h\bar{u}(t) = -\sqrt{\alpha/\beta}\,(C_D V_g^2/I)(1-\cos(It))$ (eq 26), $h(\bar{v}-V_g)(t) = -(C_D V_g^2/I)\sin(It)$ (eq 27)
5. Bulk Richardson closure $Ri_b = Ri_c$ (eq 28-29) → eq 30
6. Maximum at $It=\pi$ → eq 31, 사용 $C_D V_g^2 = u_*^2$ → **eq 32**

$R \to \infty$ 시 $\beta \to f$ → $u_*/\sqrt{fN}$ = stratified ABL 표준 (Pollard 1973, Zilitinkevich 2007). **Neutral case** 는 derivation 없이 LES + Sous et al. 2013 (rotating tank spin-down) empirical 영감.

#### 3.4.5 LES setup + Database (PDF §3 + Appendix A/B)

**LES setup** (Appendix A — verified):

- 도메인 $(2\pi \times 2\pi \times 2.5) \times 1000$ km, 격자 **256 × 256 × 512** (radial × tangential × vertical)
- Solver: Albertson & Parlange (1999a,b) base. Pseudo-spectral collocation (Orszag 1969, 1970) horizontal + 2nd-order centered FD vertical (staggered)
- SGS: **scale-dependent Lagrangian dynamic Smagorinsky** (Bou-Zeid et al. 2005)
- Time stepping: explicit 2nd-order Adams-Bashforth + fractional step (Chorin 1968, Kim & Moin 1985), CFL = 0.075
- Sponge layer 2000 m 위 (Rayleigh damping 0.01 s⁻¹)
- 3/2 dealiasing rule (Kravchenko & Moin 1997)
- $\theta_r = 300 + 0.005z$ K nudging (τ_r = 1 min, Chen et al. 2021a)
- 1.5 inertial periods $T_I = 2\pi/I$ 실행, 0.5 $T_I$ skip 후 1000 snapshots
- BC: lateral periodic, top free-lid, bottom wall-layer (Chester 2007a algebraic log-law)

**216 stratified simulations (Table A1)**:

| Param | Values | n |
|---|---|---|
| $V_g$ (m/s) | 30, 45, 60 | 3 |
| $n$ (radial gradient) | 0.25, 0.5 | 2 |
| $G_z$ (s⁻¹) | -0.02, -0.04 | 2 |
| $f$ (s⁻¹) | 5×10⁻⁵, 1×10⁻⁴ | 2 |
| $R$ (km) | 40, 80, 120 | 3 |
| $z_0$ (m) | 10⁻³, 10⁻², 10⁻¹ (ocean/intermediate/land) | 3 |
| **Total** | | **216** |

Database: NSF DesignSafe Data Depot (Sathia & Giometto 2026, DOI:10.17603/DS2-5TC9-XR68).

**16 추가 neutral + mildly stratified (Table B1)**: Set A (8 neutral runs, $G=45/60$, $R=30/35$, $n=0/0.25$) + Set B (8 with $N$ in geometric progression $10^{-4}$ → $10^{-2}$).

#### 3.4.6 Validation results (PDF §3 + Appendix B)

**Stable (eq 32)** — $C_S$ 결정:

- LES (216 runs): $C_S = 1.2$, average relative error $\sim 2.5\%$, **bias = 1.04 m, RMSE = 23.5 m, $R^2 = 0.99$** (Fig 5 parity plot)
- Observation fit (5 cases Table 1: Chen V25/V35/V45 + Bryan V40/V60): $C_S = 1.44$ (slightly higher)

**Neutral (eq 11)** — $C_R$ 결정 (Appendix B Set A 8 runs):

- $C_R = 0.58$, average error $6\%$, **bias = 2.93 m, RMSE = 6.92 m, $R^2 = 0.99$** (Fig B2)

**Combined formula (eq B1)** — neutral + stable transition:

$$\left(\frac{1}{h}\right)^p = \left(\frac{\beta}{C_R\,u_*}\right)^p + \left(\frac{\sqrt{\beta N}}{C_S\,u_*}\right)^p$$

- Zilitinkevich (2007) 은 ABL 에 $p=2$ 추천. 저자: HBL 은 **$p=4$ 더 좋음** ($f \ll N$ 이고 $\beta$ 가 $N$ 과 비교 가능한 magnitude)

**Characteristic heights (PDF §4)** — 다른 BL 길이 scale 도 $h$ 의 fraction:

| Quantity | Fraction of $h$ |
|---|---|
| Tangential velocity peak ($v_{max}$) | 65-85% ($\sim$80% 정점, Zhang 2011 정합) |
| Radial inflow peak | 6-20% (정점 $\sim$10%) |
| Inflow depth (first $u>0$) | 86-98% |
| Tangential depth (first $v<G$) | 108-111% |

#### 3.4.7 Scaling with radius (PDF §4)

$f$ 무시 + $N, n$ 상수 가정 + $G \sim R^{-n}$ (Bryan 2017b) 가정 시 (eq 41-43):

$$h \sim u_* \sqrt{R/G} \sim R^{(1-n)/2} \quad (\text{stable})$$

vs **neutral**: $h \sim u_*/\beta \sim R$ (linear).

Eddy viscosity 변화 (eq 44):

| Stratification | $K_m$ scaling |
|---|---|
| Stable | $K_m \sim u_*^2/N \sim G^2 \sim R^{-2n}$ (radial decrease, twice gradient wind 속도) |
| Neutral | $K_m \sim u_* h \sim G^2/\beta \sim R^{1-n}$ (radial increase) |

Stern & Nolan (2009), Zhang & Drennan (2012) 관측: $K_m$ near eyewall 크고 멀어질수록 감소 → **stratification scaling 과 정합** (neutral 식은 반대 부호라 inconsistent).

#### 3.4.8 한계 + 후속 (verified 범위 명시 — 2026-05-28 update)

기존 §3.4.4 한계 항목 (2026-05-26) 모두 PDF 본문 인용으로 해소:

- ✅ analytical derivation → §3.4.4 (Pollard 1973 응용)
- ✅ LES setup → §3.4.5 (216 sims, 256×256×512 grid, Bou-Zeid Smagorinsky)
- ✅ 비교한 expressions → Meng 1995, Kepert 2001, Sathia & Giometto 2025 (constant eddy viscosity $\sqrt{2K/I}$) / Zilitinkevich 2007 (ABL) / Pollard 1973 (P73 ocean mixed layer) / Sous 2013 (rotating tank) / 외 closure papers (Foster 2009, Nolan 2009, Kepert 2012, Gopalakrishnan 2013/2021, Zhang 2015/2017, Chen 2021-2023, Romdhani 2022, Matak & Momen 2023, Vickery 2009 wind engineering)
- ⚠ **eyewall 적용 가능성**: V45 (Chen 2021a) 의 nose feature 가 eyewall proximate regime 이지만, 본 derivation 가정 (avg vertical advection 무시 + 도메인 < R) 밖. 그럼에도 outer region collapse 가 양호하다는 partial evidence (PDF §3c 직접 인용): "the profile nevertheless collapses satisfactorily with the others, and the proposed scaling continues to perform well". eyewall **내부** 명시적 적용은 제외
- ✅ Wind engineering / coastal resilience 응용: turbulent inflow generators (tall building + wind turbine 풍하중), reduced-order surrogate model uncertainty 감소 (wind energy + coastal hazard analysis). NIST 자금 Grant 70NANB22H057, Anvil (Purdue) ATM180022

**ADCIRC 통합 후속** (위키 자체 분석):

- ADCIRC source code 의 reduction factor 가 새 $h \sim u_*/\sqrt{\beta N}$ scaling 기반으로 갱신 가능
- 한국 태풍 hindcast (Maemi 2003, Hinnamnor 2022 → `05-examples.md` §1·§2; Bolaven 2012 → §3) 의 eyewall 외 surge response 검증 case 후보
- Paper 가 신규 (2026-05 제출) — 코드 통합 사례 아직 없음. 향후 ADCIRC PR / NIFS KOOS workflow 채택 시 추적

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
