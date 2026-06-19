---
title: "Delft3D-FLOW User Manual — 물리·수치 심화 (Ch 9 지배방정식·난류·heat·파-흐름 + Ch 10 ADI/이산화)"
model: Delft3D
doc: Delft3D-FLOW_User_Manual.pdf
canonical_source: manual
citation_status: verified
verification_method: "Delft3D-FLOW_User_Manual.pdf (v4.07.01, Rev 80907, 3 May 2026, 757p) pdftotext -layout 직접 추출 후 전체 TOC + Ch 9 Conceptual description(p.163-260)·Ch 10 Numerical aspects(p.261-306) 페이지 인용. 인용: 연속·운동량 식 9.3/9.7/9.8 (p.175-176), 정수압 9.11-9.16 (p.176-177), 상태방정식 9.39-9.47 (p.185), 난류 9.98/9.115/9.127-9.138 (p.205-210), bed shear 9.53-9.60 (p.188-189), 파-흐름 GLM 9.169-9.207 (p.216-225), heat balance 9.213/9.257 (p.229,239), ADI 10.1-10.13 (p.261-267), Forester filter 10.59-10.60 (p.280) 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
  - models/Delft3D/manual-notes/delft3d-flow-user-manual.md
---

# Delft3D-FLOW User Manual — 물리·수치 심화 (Ch 9·10)

> Delft3D-FLOW 매뉴얼 757p 중 이론 핵심인 **Ch 9 Conceptual description (p.163-260)** 과 **Ch 10 Numerical aspects (p.261-306)** 의 지배방정식·process 식·수치 스킴을 페이지 인용으로 정리. 입력 reference·MDF 구조는 [[delft3d-flow-user-manual]] 참조. source-analysis 대응은 본문 §끝 매핑표.

## 1. 문서 정체 + 이론/수치 장 TOC

| 항목 | 값 |
|---|---|
| 제목 | Delft3D-FLOW — Hydro-Morphodynamics, User Manual |
| Version / Revision | 4.07.01 / 80907 |
| 날짜 / 발행 | 3 May 2026 / Deltares |
| 페이지 | 757 (DRAFT 워터마크) |

본 노트가 다루는 **물리·수치 장** (TOC p.v-xi 직접 인용):

| 장 | 제목 | 페이지 |
|---|---|---:|
| **9** | **Conceptual description** | 163 |
| 9.3 | Governing equations (Hydrodynamic 9.3.1 / Transport 9.3.2 / Intake-outfall 9.3.3 / Equation of state 9.3.4) | 166 |
| 9.4 | Boundary conditions (Flow 9.4.1 / Transport 9.4.2) | 186 |
| 9.5 | Turbulence (AEM 9.5.1 / k-L 9.5.2 / k-ε 9.5.3 / Low-Re 9.5.4) | 201 |
| 9.6 | Secondary flow (σ-model only) | 212 |
| 9.7 | Wave-current interaction (radiation stress / Stokes / streaming / wave turb / bed shear) | 216 |
| 9.8 | Heat flux models (5 모델) | 228 |
| 9.9 | Tide generating forces | 241 |
| 9.10-9.11 | Hydraulic structures / Flow resistance (bedforms·trachytopes·vegetation) | 245-246 |
| **10** | **Numerical aspects of Delft3D-FLOW** | 261 |
| 10.1-10.3 | Staggered grid / σ·Z-grid / model boundaries | 261-263 |
| 10.4 | Time integration 3D SWE (ADI 10.4.1 / time-step 10.4.5) | 264 |
| 10.5 | Spatial discretization (horiz·vert advection / viscosity) | 270 |
| 10.6 | Transport eq solution (Cyclic 10.6.1 / Van Leer-2 10.6.2 / Forester 10.6.4) | 275 |
| 10.7 | Turbulence model 수치구현 | 281 |
| 10.8 | Drying and flooding | 281 |
| 10.10 | Artificial vertical mixing (σ-coord) | 300 |
| **11** | Sediment transport and morphology | 307 |
| **12** | Fixed layers in Z-model | 388 |
| App A/B | Files / Special features (B.12 Non-hydrostatic solver, p.621) | 428/505 |

> Ch 11 (sediment) 의 식은 별도 source-analysis 노트 영역 — [[../source-analysis/sediment/delft3d_sediment]] 와 [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) 로 위임. 본 노트는 hydrodynamic core 집중.

## 2. 모델 정체·가정 (§9.3.1, p.173)

Delft3D-FLOW 은 **비압축 Navier-Stokes 를 shallow water + Boussinesq 가정** 하에 푼다. 연직 운동량식에서 **연직 가속을 무시 → 정수압(hydrostatic pressure) 식**. 3D 모델에서 연직속도는 연속식에서 계산 (§9.3.1, p.173).

- 수평: orthogonal **curvilinear** 좌표 — Cartesian (ξ, η) 또는 spherical (λ, ϕ). Spherical 은 curvilinear 의 특수경우 $\sqrt{G_{\xi\xi}}=R\cos\phi,\ \sqrt{G_{\eta\eta}}=R$, $R=6378.137$ km WGS84 (식 9.1, p.173).
- 연직: **σ-grid (σ-model)** 또는 **Cartesian Z-grid (Z-model)**. 본 장 식은 σ-coord 기준; Z-coord 차이는 Ch 12 (p.173). cf. [[../source-analysis/delft3d_sigma_z]].

**σ 정의** (식 9.2, p.174): $\sigma = \dfrac{z-\zeta}{d+\zeta} = \dfrac{z-\zeta}{H}$, 바닥 $\sigma=-1$, 자유표면 $\sigma=0$. $H=d+\zeta$ (total depth). σ-grid 는 Phillips(1957) 도입, 층 수가 수심 무관 일정 (p.174). Z-grid 는 강한 성층·급경사 지형에서 isopycnal 과 평행해 인공혼합 저감 (p.174); 바닥은 staircase 표현.

## 3. 지배방정식 (§9.3.1, σ-grid)

### 연속식 (depth-averaged, 식 9.3, p.175)

$$\frac{\partial\zeta}{\partial t}+\frac{1}{\sqrt{G_{\xi\xi}G_{\eta\eta}}}\frac{\partial\big[(d+\zeta)U\sqrt{G_{\eta\eta}}\big]}{\partial\xi}+\frac{1}{\sqrt{G_{\xi\xi}G_{\eta\eta}}}\frac{\partial\big[(d+\zeta)V\sqrt{G_{\xi\xi}}\big]}{\partial\eta}=(d+\zeta)Q$$

$U,V$ = depth-averaged velocity (식 9.4-9.5). $Q=\int_{-1}^{0}(q_{in}-q_{out})d\sigma+P-E$ (강수 $P$·증발 $E$·소스/싱크, 식 9.6, p.175). 발전소 취수는 sink 로 모델링.

### 수평 운동량식 (식 9.7-9.8, p.176)

ξ-방향 (η-방향은 대칭):

$$\frac{\partial u}{\partial t}+\frac{u}{\sqrt{G_{\xi\xi}}}\frac{\partial u}{\partial\xi}+\frac{v}{\sqrt{G_{\eta\eta}}}\frac{\partial u}{\partial\eta}+\frac{\omega}{d+\zeta}\frac{\partial u}{\partial\sigma}-\frac{v^2}{\sqrt{G_{\xi\xi}G_{\eta\eta}}}\frac{\partial\sqrt{G_{\eta\eta}}}{\partial\xi}+\frac{uv}{\sqrt{G_{\xi\xi}G_{\eta\eta}}}\frac{\partial\sqrt{G_{\xi\xi}}}{\partial\eta}-fv=-\frac{1}{\rho_0\sqrt{G_{\xi\xi}}}P_\xi+F_\xi+\frac{1}{(d+\zeta)^2}\frac{\partial}{\partial\sigma}\Big(\nu_V\frac{\partial u}{\partial\sigma}\Big)+M_\xi$$

- 곡선격자 변환이 도입한 **curvature term** ($\propto v^2\partial\sqrt{G_{\eta\eta}}/\partial\xi$ 등) (p.176).
- 밀도변동은 baroclinic pressure term 빼고 무시(Boussinesq). $P_\xi,P_\eta$=압력경사, $F_\xi,F_\eta$=수평 Reynolds stress 불균형, $M_\xi,M_\eta$=외부 momentum source/sink(구조물·discharge·파응력) (p.176).
- $\nu_V$ = 식 9.20 연직 eddy viscosity.

### 연직속도 (식 9.9, p.176)

$\omega$ = adapting σ-coord 의 연직속도 (iso-σ 면 기준 상대속도), 연속식에서 계산. 물리 연직속도 $w$ (Cartesian) 는 모델 식에 안 들어가고 후처리용으로만 식 9.10 으로 환산 (p.176).

### 정수압 가정 (σ-grid, 식 9.11-9.16, p.176-177)

$$\frac{\partial P}{\partial\sigma}=-g\rho H \quad\Rightarrow\quad P=P_{atm}+gH\int_\sigma^0\rho\,d\sigma'$$

- **상수밀도** 압력경사 (식 9.13): $\frac{1}{\rho_0\sqrt{G_{\xi\xi}}}P_\xi=\frac{g}{\sqrt{G_{\xi\xi}}}\frac{\partial\zeta}{\partial\xi}+\frac{1}{\rho_0\sqrt{G_{\xi\xi}}}\frac{\partial P_{atm}}{\partial\xi}$ — barotropic(자유표면경사) + 대기압경사. 대기압은 storm surge 시 peak wind 에서 외력 지배 (p.177).
- **비균질밀도** (식 9.15-9.16, Leibniz rule): barotropic + **baroclinic** $g\frac{d+\zeta}{\rho_0\sqrt{G_{\xi\xi}}}\int_\sigma^0\big(\frac{\partial\rho}{\partial\xi}+\frac{\partial\rho}{\partial\sigma}\frac{\partial\sigma}{\partial\xi}\big)d\sigma'$. σ 변환이 수평경사에 연직미분 도입 → 급경사 지형에서 인공흐름; baroclinic term 수치처리는 §10.10 (p.177, Stelling & Van Kester 1994).

### Coriolis / Reynolds stress (p.177-178)

- $f=2\Omega\sin\phi$ (지리위도). curvilinear grid 는 공간변화 Coriolis 지정 (p.178).
- $F_\xi,F_\eta$ = eddy viscosity 개념 (Rodi 1984). 3D 천수류는 an-isotropic: $\nu_H\gg\nu_V$ (식 9.21-9.27, p.180).

## 4. Eddy viscosity 합성 (§9.3.1 Reynold's stresses, p.178-179)

**수평** (식 9.19): $\nu_H=\nu_{SGS}+\nu_V+\nu_H^{back}$ — sub-grid scale(HLES) + 3D-turbulence + 사용자배경. **연직** (식 9.20): $\nu_V=\nu_{mol}+\max(\nu_{3D},\nu_V^{back})$, $\nu_{3D}$ 는 연직 closure(§9.5)에서 계산 (p.179).

Table 9.2 (p.178) eddy viscosity 옵션:

| 모델 | $\nu_{SGS}$ | $\nu_H^{back}$ | $\nu_{3D}$ | $\nu_V^{back}$ |
|---|---|---|---|---|
| 2D, no HLES | - | 2D-turb + dispersion coef | - | - |
| 2D, with HLES | HLES 계산 | 3D-turb + dispersion | - | - |
| 3D, no HLES | - | 2D-turb | 연직 turb model | background |
| 3D, with HLES | HLES 계산 | - | 연직 turb model | background |

> ⚠ $\nu_V^{back}$ 하한은 **운동량식(9.7/9.8)에만** 적용, 연직 turbulence 식(9.115/9.127/9.128)엔 미적용 (p.179 remark).

전단응력 형식 (식 9.21-9.25 partial-slip rough wall, explicit→안정조건 발생 / 식 9.26-9.27 Laplace operator coarse grid, p.180).

## 5. 난류 closure (§9.5, p.201-211)

4 옵션 모두 Kolmogorov(1942)-Prandtl(1945) eddy viscosity 개념: $\nu_{3D}=c'_\mu L\sqrt{k}$ (식 9.98, p.205), $c'_\mu=c_\mu^{1/4}$, **$c_\mu=0.09$** (Rodi 1984). cf. [[../source-analysis/delft3d_turbulence]].

| § | 모델 | k | L | 식 |
|---|---|---|---|---|
| 9.5.1 | AEM (algebraic) | 대수식 | Bakhmetev(1932) $L=\kappa(z+d)\sqrt{1-\frac{z+d}{H}}$ | 9.99, p.205 |
| 9.5.2 | k-L | transport eq | 대수 (Bakhmetev) | 9.115, p.207 |
| 9.5.3 | **k-ε** | transport eq | $L=c_D\frac{k\sqrt{k}}{\varepsilon}$ | 9.126-9.135, p.209 |

$\kappa\approx0.41$ (Von Kármán). AEM 은 $\nu_{3D}=\max(\nu_{ALG},\nu_{PML})$ (식 9.114).

### k-ε 모델 (식 9.127-9.138, p.209-210)

$$\frac{\partial k}{\partial t}+\text{(advection)}=\frac{1}{(d+\zeta)^2}\frac{\partial}{\partial\sigma}\Big(D_k\frac{\partial k}{\partial\sigma}\Big)+P_k+P_{kw}+B_k-\varepsilon$$
$$\frac{\partial\varepsilon}{\partial t}+\text{(advection)}=\frac{1}{(d+\zeta)^2}\frac{\partial}{\partial\sigma}\Big(D_\varepsilon\frac{\partial\varepsilon}{\partial\sigma}\Big)+P_\varepsilon+P_{\varepsilon w}+B_\varepsilon-c_{2\varepsilon}\frac{\varepsilon^2}{k}$$

- 확산계수 (식 9.129): $D_k=\frac{\nu_{mol}}{\sigma_{mol}}+\frac{\nu_{3D}}{\sigma_k}$, $D_\varepsilon=\frac{\nu_{3D}}{\sigma_\varepsilon}$.
- 생성/부력 (식 9.130-9.131): $P_\varepsilon=c_{1\varepsilon}\frac{\varepsilon}{k}P_k$, $B_\varepsilon=c_{1\varepsilon}\frac{\varepsilon}{k}(1-c_{3\varepsilon})B_k$.
- **상수 (Rodi 1984)** (식 9.132-9.134): $c_{1\varepsilon}=1.44$, $c_{2\varepsilon}=1.92$, $c_{3\varepsilon}=$ {0.0 불안정성층, 1.0 안정성층} — 안정성층에서 buoyancy flux off (p.210).
- 연직 eddy viscosity (식 9.135): $\nu_{3D}=c_\mu\frac{k^2}{\varepsilon}$, $c_\mu=c_D c'_\mu$.
- **바닥 ε BC** (식 9.137): $\varepsilon|_{\sigma=-1}=\frac{u_{*b}^3}{\kappa z_0}$; **표면** (식 9.138): $\varepsilon|_{\sigma=0}=\frac{u_{*s}^3}{\frac{1}{2}\kappa\Delta z_s}$, 무풍시 표면 ε=0 (p.210).
- ⚠ 3D k-ε 상수는 depth-averaged 와 달라 **2D 에서는 k-ε 사용 불가** (p.210).

## 6. 바닥 전단응력 / 조도 (§9.4.1.1, p.188-189)

바닥 momentum BC (식 9.51-9.52): $\frac{\nu_V}{H}\frac{\partial u}{\partial\sigma}\big|_{\sigma=-1}=\frac{1}{\rho_0}\tau_{b\xi}$.

**2D** (식 9.53): $\vec\tau_b=\frac{\rho_0 g\vec U|\vec U|}{C_{2D}^2}$. **3D** (식 9.57): $\vec\tau_{b3D}=\frac{g\rho_0\vec u_b|\vec u_b|}{C_{3D}^2}$ (최하층 속도 기준).

3 조도식 (식 9.54-9.56, 9.60, p.188-189):

| 식 | 공식 | 입력 |
|---|---|---|
| Chézy | $C_{2D}=$ Chézy 계수 [m$^{1/2}$/s] | C 직접 |
| Manning | $C_{2D}=\frac{\sqrt[6]{H}}{n}$ | n [m$^{-1/3}$s] |
| White-Colebrook | $C_{2D}=18\log_{10}\frac{12H}{k_s}$ | $k_s$ Nikuradse [m] |
| 3D (z₀) | $C_{3D}=\frac{\sqrt g}{\kappa}\ln\big(1+\frac{\Delta z_b}{2z_0}\big)$ | $z_0$ user |

> 입력 reference(GUI 기본값 Manning 0.04 / White-Colebrook 10.0 / Chézy 65.0, 기본 Chézy)는 [[delft3d-flow-user-manual]] §4.5.7 참조 (p.61-66).

## 7. 상태방정식 (§9.3.4, p.185)

$\rho=f(s,t)$, **Eckart 또는 UNESCO** 선택. GUI 불가 → MDF `DenFrm = #Eckart#` / `#UNESCO#`(기본) 직접 편집 (p.185).

- **Eckart** (식 9.39-9.42, 범위 0<t<40°C, 0<s<40 ppt): $\rho=\frac{1000 P_0}{\lambda+\alpha_0 P_0}$, $\lambda=1779.5+11.25t-0.0745t^2-(3.80+0.01t)s$, $\alpha_0=0.6980$, $P_0=5890+38t-0.375t^2+3s$. **단점**: 담수 4°C 최대밀도 미재현 (p.185).
- **UNESCO** (식 9.43-9.47 EOS80, 범위 0<t<40°C, 0.5<s<43 ppt): $\rho=\rho_0+As+Bs^{3/2}+Cs^2$, $C=4.8314\cdot10^{-4}$. 467 데이터점, 표준오차 $3.6\cdot10^{-3}$ kg/m³ (Millero & Poisson 1981). **기본·권장** — 4°C 최대밀도 정확, thermal stratification 용 (p.185-186).

## 8. 경계조건 (§9.4, p.186-201)

- 닫힌경계 = 자연경계, 법선속도 0. 열린경계 = 인공 water-water, 반사 최소화 (p.186).
- **약반사 BC** (Verboom & Slob 1984, Engquist-Majda): Riemann invariant $R=U\pm2\sqrt{gH}$ (식 9.70). 선형화 (식 9.71): 지정신호 $f(t)=U+\zeta\sqrt{g/d}$, $2\sqrt{gd}$ 는 수심장에서 계산 (p.192).
- 5 BC type (p.192): Water level $\zeta=F_\zeta(t)+\delta_{atm}$ / Velocity $U=F_U(t)$ / Discharge $Q=F_Q(t)$ / Neumann $\partial\zeta/\partial\vec n=f(t)$ / Riemann $U\pm\zeta\sqrt{g/d}=F_R(t)$.
- Barotropic forcing 근사 (p.192): 자유표면경사(geostrophic) + tidal + 기상(wind set-up) + 파(wave set-up) 선형중첩.
- **Transport BC** (§9.4.2): 열린경계 Thatcher-Harleman 조건(§9.4.2.2, p.199) — 유출후 재유입 시 return time 동안 점진 복원.

## 9. 파-흐름 상호작용 (§9.7, p.216-227)

Delft3D-FLOW 은 **GLM (Generalised Lagrangian Mean, Andrews & McIntyre 1978) 정식화** 로 풀고 wave-current interaction 포함 (p.217).

- $\vec u^L=\vec u^E+\vec u^S$ (식 9.171): GLM = Eulerian + **Stokes drift**. 모든 transport 는 GLM 속도로, 결과파일엔 Eulerian 속도 (p.217).
- **Radiation stress forcing** (§9.7.1): 파유도력 $F_i=-\partial S_{ij}/\partial x_j$ (식 9.170). Dingemans(1987) — divergence-free 부분은 흐름 못 일으켜 무시; 잔여는 dissipation 관련 $F_i=\frac{Dk_i}{\omega}$ (식 9.173, p.217).
- **Stokes drift·mass flux** (§9.7.2), **streaming** (§9.7.3), **wave-induced turbulence** $P_{kw},P_{\varepsilon w}$ (§9.7.4, 식 9.191 $P_{\varepsilon w}=c_{1\varepsilon}P_{kw}$, $c_{1\varepsilon}=1.44$, p.221).
- **파에 의한 bed shear 증강** (§9.7.5, p.222-225): wave friction factor Swart(1974) (식 9.205): $f_w=0.00251\exp(5.21(A/k_s)^{-0.19})$ if $A/k_s>\pi/2$, else 0.3; $A=u_{orb}/\omega$ (식 9.206). 8 wave/current boundary-layer 모델 (Table 9.5, p.225): FR84·MS90·HT91·GM79·DS88·BK67·CJ85·OY88·VR04. 유효 bed shear 는 Stokes drift 보정 (식 9.207).

## 10. Heat flux 모델 (§9.8, p.228-240)

열수지 (식 9.213, p.229): $Q_{tot}=Q_{sn}+Q_{an}-Q_{br}-Q_{ev}-Q_{co}$ (net solar + net atmospheric − back radiation − evaporative − convective). cf. [[../source-analysis/delft3d_heat]].

5 모델 (p.228-240):

| # | 모델 | 처방 입력 | 계산 항 |
|---|---|---|---|
| 1 | Heat flux 1 | clear-sky 단파 $Q_{sc}$ | $Q_{an},Q_{br},Q_{ev},Q_{co}$ (Table 9.7) |
| 2 | Heat flux 2 (Octavio 1977) | net $(Q_{sn}+Q_{an})$ measured | $Q_{br},Q_{ev},Q_{co}$ (Table 9.8) |
| 3 | **Excess temperature** (Sweers 1976) | $T_{back}$ | $Q_{tot}=-\lambda(T_s-T_{back})$ (식 9.257-9.258) |
| 4 | Murakami (1985, Japan) | net solar $Q_{sn}$ | $Q_{eb},Q_{ev},Q_{co}$, depth 흡수 (Table 9.9) |
| 5 | Ocean (Gill 1982·Lane 1989, North Sea) | cloud cover % | $Q_{eb},Q_{ev},Q_{co}$ + free convection (Table 9.10) |

Excess model 교환계수 (식 9.258): $\lambda=4.48+0.049T_s+f(U_{10})(1.12+0.018T_s+0.00158T_s^2)$.

## 11. 수치 — Ch 10 (p.261-306)

### Staggered grid (§10.1, p.261)

유한차분, orthogonal curvilinear. 변수배치 = **Arakawa C-grid** (staggered): 수위(압력)점은 연속셀 중심, 속도성분은 셀면에 수직. 장점: BC 단순·수위 공간진동 방지(Stelling 1984) (p.261).

### ADI 시간적분 (§10.4, p.264-267)

명시적 적분은 wave CFL 제약 (식 10.1, p.265): $\text{CFL}_{wave}=2\Delta t\sqrt{gH}\sqrt{\frac{1}{\Delta x^2}+\frac{1}{\Delta y^2}}<1$ → 수초 time-step 강제. 따라서 implicit 필요 (Crank-Nicholson 은 large band matrix 비경제, p.265).

**ADI (Leendertse 1967)** — 1 time-step 을 **2 stage(각 ½Δt)** 분할, 양 stage 공간 2차 정확 (p.266). cf. [[../source-analysis/delft3d_adi_solver]].

- 2D 벡터형 (식 10.7-10.8): Step1 $\frac{\vec U^{\ell+1/2}-\vec U^\ell}{\frac12\Delta t}+A_x\vec U^{\ell+1/2}+A_y\vec U^\ell+B\vec U^{\ell+1/2}=\vec d$ / Step2 대칭 (p.266).
- **Stage1** ($\ell\to\ell+\frac12$): V-momentum 먼저, 이어 U-momentum 이 연속식과 자유표면경사로 implicit 결합. **Stage2** ($\ell+\frac12\to\ell+1$): U 먼저, V 가 연속식과 결합 (p.266).
- barotropic pressure(수위경사) implicit stage 에선 advection·viscosity explicit, 반대 stage 에선 역 (p.266). 동일 subroutine 재사용, Coriolis 부호만 방향의존 (p.266).
- 운동량식 연속식 대입 → **수위 tri-diagonal system**, back-substitution 으로 속도 (p.266).
- bottom friction $B=\text{diag}(\lambda,\lambda,0)$ 는 안정성 위해 각 stage implicit (식 10.11, p.266).

3 수평 advection 스킴 (p.266): **WAQUA**(Stelling 1984) / **Cyclic**(Stelling & Leendertse 1992) — 둘 다 time-step 제약 없음 / **Flooding**(Stelling & Duinmeijer 2003, 2D rectilinear, hydraulic jump·bore, advection explicit→Courant 제약).

연직 exchange explicit 시 가혹한 제약 (식 10.12-10.13): $\Delta t\le\frac{(\Delta\sigma H)^2}{2\nu_V}$ 등 → 연직은 implicit 처리 (p.267).

### Transport eq 해법 (§10.6, p.275-280)

- **Cyclic method** (§10.6.1, 식 10.58, p.279): 계수 모두 양수($\alpha,\beta\le1$) → positive concentration 보존, wiggle 점진 제거.
- **Van Leer-2** (§10.6.2, p.278): monotone limiter.
- **Forester filter** (§10.6.4, p.279-280): 수평·연직 비물리 wiggle 제거. 연직 filter 적용조건 (식 10.59): local max/min + $Pe_{\Delta z}=\frac{|w|\Delta z}{D_V}\le2$, $\varepsilon=10^{-3}$, $D_{num}=\frac{\Delta z^2}{2\Delta t}$. 수평 max 100 step / 연직 max 1000 step. ⚠ 연직 Forester 는 salinity·temperature 만 평활, sediment 불영향 (p.280).

### 난류 수치구현 (§10.7, p.281)

eddy viscosity 는 항상 직전 ½ time-step 정보 기반. k·ε transport 는 **non-conservative form**, 1차 upwind. k·ε·$\nu_V$ 는 staggered grid 의 **층계면(셀중심)** 에 위치 → 생성·부력항 연직경사 정확 (p.281).

## 12. source-analysis 대응 (이론↔코드)

| Manual 이론 (page) | source-analysis 노트 |
|---|---|
| §9.3.1 σ/Z governing eq (p.173) | [[../source-analysis/delft3d_sigma_z]] |
| §9.5 난류 closure k-ε (p.205-210) | [[../source-analysis/delft3d_turbulence]] |
| §9.8 heat balance 5 모델 (p.229) | [[../source-analysis/delft3d_heat]] |
| §10.4 ADI 2-stage (p.266) | [[../source-analysis/delft3d_adi_solver]] |
| §10.8 drying/flooding (p.281-289) | [[../source-analysis/delft3d_drying_flooding]] |
| Ch 11 sediment·morphology (p.307) | [[../source-analysis/sediment/delft3d_sediment]] |

## 13. 관련 자료

- [[delft3d-flow-user-manual]] — TOC + MDF 입력 family 12 buckets (운영 reference)
- [[delft3d-manuals-overview]] — 53 PDFs 인덱스
- 외부: [Deltares OSS Delft3D](https://oss.deltares.nl/web/delft3d), [manuals download](https://content.oss.deltares.nl/delft3d4/)
- 주요 출처 논문: Stelling (1984)·Stelling & Van Kester (1994)·Leendertse (1967)·Rodi (1984)·Andrews & McIntyre (1978)·Swart (1974) (Ch 9·10 References, p.411-)
