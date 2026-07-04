---
title: "EFDC+ Theory v12 Ch 6 SEDIMENT TRANSPORT — 식 level cross-walk (Original SedTran non-cohesive/cohesive/consolidation + SEDZLJ 매핑)"
topic: efdc-theory-v12-ch6-sediment
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf 본문 pp.72-95 (§6.1-§6.4.1, 물리 PDF p.85-108) 직접 추출 — 식 (6.1)~(6.110) + Fig 6.1-6.4 캡션 인용. §6.4 SEDZLJ 상세식(6.111~)은 source-analysis [[efdc_sedzlj]] 에 소스 직접 read 로 기커버 → 본 노트는 이론↔소스↔legacy(2003) cross-walk. primary sources: Hamrick 1992/Tetra Tech 2007b · van Rijn 1984 · Smith-McLean 1977 · Garcia-Parker 1991 · Krone/Partheniades · Mehta et al. 1989 · Hwang-Mehta 1989 · Ziegler-Nisbet 1994 · Jones-Lick 2000."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — PDF Read pages 85-108 직접 + source-analysis/legacy cross-ref"
verification_date: 2026-07-04
related:
  - models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md
  - models/EFDC/manual-notes/efdc-theory-v12-ch5-temperature-heat.md
  - models/EFDC/manual-notes/efdc-sediment-theory-2003.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
  - concepts/sediment-transport/02-theory.md
---

# EFDC+ Theory v12 Ch 6 SEDIMENT TRANSPORT — 식 level cross-walk

> 출처: [`EFDC_Theory_Document_Ver_12.pdf`](../raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf) Chapter 6 (문서 pp.72-120, 본 노트는 §6.1-§6.4.1 = pp.72-95, 물리 PDF p.85-108), DSI LLC.
> **cross-walk 3축**: (a) 이론식 (본 노트) ↔ (b) 소스 [[efdc_sedzlj]](SEDZLJ branch 직접 read) + [[efdc_sediment]](Original SedTran dispatch) ↔ (c) legacy [[efdc-sediment-theory-2003]](Tetra Tech 2002/2003 Hamrick reference).
> Theory Ch-series: [[efdc-theory-v12-ch2-hydrodynamics]](수력)·[[efdc-theory-v12-ch5-temperature-heat]](온도) 에 이은 **Ch 6 유사이동**.

## 0. §6.1 두 모듈 (p.72)

EFDC+ 는 유사이동 **2 옵션**:

1. **EFDC (Original) Sediment Transport** — Hamrick's work (Tetra Tech 2007b). cohesive/non-cohesive **별도 계산 프로세스** (Fig 6.1). 각 class 사용자정의 상수 erosion rate.
2. **SEDZLJ** — SNL-EFDC 유래 (Jones-Lick 2000; Thanh et al. 2008; Ziegler-Lick 1988/1986). 응집성 무관 **통합 처리** (Fig 6.2). SEDFlume 측정 site-specific erosion rate → 공간변동.

**공통**: 수관 부유이동은 동일 방식(§6.2). 차이는 (1) cohesive vs non-cohesive 처리 (2) 수관-bed 질량교환. 둘 다 hydro 모듈과 동적 결합 → geomorphic feedback. (소스 dispatch: Card C36 `NSEDFLUME` = 0 Original / 98·99 SEDZLJ, [[efdc_sedzlj]] §Dispatch.)

## 1. §6.2 Suspended Sediment Transport (pp.72-76) — 공통 프레임

### 1.1 §6.2.1 Governing Equations (pp.72-74)

generic transport Eq 3.1 의 유사 형태 (수평 물리확산항 생략 — 수치확산 작음). curvilinear-sigma (Eq 6.1):

$$\frac{\partial}{\partial t}(m_x m_y HC_j) + \frac{\partial}{\partial x}(m_y HuC_j) + \frac{\partial}{\partial y}(m_x HvC_j) + \frac{\partial}{\partial z}(m_x m_y wC_j) - \frac{\partial}{\partial z}(m_x m_y w_{s,j}C_j) = \frac{\partial}{\partial z}\left(\frac{m_x m_y}{H}A_b\frac{\partial}{\partial z}C_j\right) + S_{s,j}^E + S_{s,j}^I \quad (6.1)$$

$C_j$ = class $j$ 농도 (g/m³), $w_{s,j}$ = 침강속도, $A_b$ = 연직 eddy diffusivity, $S^E/S^I$ = external(point/non-point load)/internal(reactive decay·floc 형성/파괴 시 class간 교환) source-sink. 연직 BC (Eq 6.2-6.3):

$$-\frac{A_b}{H}\frac{\partial}{\partial z}C_j - w_{s,j}C_j = J_{o,j}\ \ \text{at}\ z=0; \qquad -\frac{A_b}{H}\frac{\partial}{\partial z}C_j - w_{s,j}C_j = 0\ \ \text{at}\ z=1 \quad (6.2,6.3)$$

$J_{o,j}$ = 수관-bed 순교환 flux (수관 방향 양). (cf. concept: [[concepts/sediment-transport/02-theory]] §3 Rouse.)

### 1.2 §6.2.2 Numerical Solution (pp.74-76) — fractional step 4단계

salinity 이동식과 동일 high-order upwind (Hamrick 1992), **fractional step** (Eq 6.4-6.12):

| step | 식 | 내용 |
|---|---|---|
| 1 advection+ext src | 6.4 | **MPDATA** anti-diffusive (Smolarkiewicz-Clark 1986) + optional FCT (Smolarkiewicz-Grabowski 1990) — [[efdc_transport_scheme]] CALTRAN_AD 대응 |
| 2 settling | 6.5-6.8 | fully implicit upwind, **top layer(k=KC)→bottom(k=1) march-down** + optional 층간 anti-diffusion |
| 3 bed exchange | 6.9-6.11 | resuspension/deposition. non-cohesive $J_0^{***}=w_s(C_{eq}-C_1^{***})$ (6.10) / cohesive deposition $J_0^{***}=-P_d w_s C_1^{***}$ (6.11). flux limiter $L_o$ (6.9) = top bed layer 만 1 step 완전 재부유 |
| 4 vertical diffusion | 6.12 | implicit, bed·수면 zero diffusive flux |

## 2. §6.3 EFDC (Original) Sediment Transport Module (pp.77-95)

Fig 6.3 개념도 (bottom shear τbx/τby → erosion/bedload/suspended load → settling/deposition/consolidation). non-cohesive·cohesive 별도 프로세스.

### 2.1 §6.3.1 Non-Cohesive Sediment (pp.77-88)

#### (a) Settling velocity — van Rijn 1984 piecewise (Eq 6.13-6.18)

$$w_{soj} = \sqrt{g'd_j}\begin{cases} R_{dj}/18, & d\le100\,\mu m \\ \frac{10}{R_{dj}}(\sqrt{1+0.01R_{dj}^2}-1), & 100<d_j\le1000\,\mu m \\ 1.1, & d_j>1000\,\mu m \end{cases} \quad (6.14)$$

reduced gravity $g'=g(\rho_{sj}/\rho_w-1)$ (6.15), grain densimetric Reynolds $R_{dj}=d_j\sqrt{g'd_j}/\nu$ (6.16). hindered settling $w_{sj}=(1-\sum C_i/\rho_{si})^n w_{soj}$ (6.17, $n$=2-4 van Rijn 1984), 선형근사 (6.18, ≤200,000 mg/l 5% 이내; <25,000 mg/l 무보정도 5% 이내).

#### (b) Critical Shields + transport mode (Eq 6.19-6.23)

$$\theta_{csj}=\frac{\tau_{csj}}{g'd_j}=\frac{u_{*csj}^2}{g'd_j}=f(R_{dj}) \quad (6.19)$$

van Rijn 1984 5-구간 numerical (Eq 6.20): $0.24(R_{dj}^{2/3})^{-1}$ / $0.14(\cdot)^{-0.64}$ / $0.04(\cdot)^{-0.1}$ / $0.013(\cdot)^{0.29}$ / $0.055$. transport mode by bed shear velocity $u_*=\sqrt{\tau_b}$ (6.21): $u_*<u_{*csj}$ 무이동(deposit) / $u_{*csj}<u_*<w_{soj}$ **bedload** (6.23) / $u_*>w_{soj}$ **suspended**. (임계 130 μm — Fig 6.4 교점.)

#### (c) Bedload — general Φ + 5 formulation (Eq 6.24-6.35)

$$\frac{q_B}{\rho_s d\sqrt{g'd}}=\Phi(\theta,\theta_{cs}); \quad \theta=\frac{\tau_b}{g'd_j}=\frac{u_*^2}{g'd_j} \quad (6.24,6.25)$$

일반형 $\Phi=\phi(\theta-\theta_{cs})^\alpha(\sqrt\theta-\gamma\sqrt{\theta_{cs}})^\beta$ (6.26), $\phi=0.053/(R_d^{1/5}\theta_{cs}^{2.1})$ (6.27, van Rijn 1984). α/β/γ 사용자정의 → **5 공식**: van Rijn 1984 (6.28) · Engelund-Hansen 1967 (6.29) · **Meyer-Peter-Müller 1948** (6.30) · Bagnold 1956 (6.31) · Wu et al. 2000 (6.32). [riverine Ackers-White/Laursen/Yang 은 (6.25) 부적합 → 미포함.] bedload flux 벡터화 (6.33) + upwind cell-face (6.34) + bed 순제거율 $J_b$ (6.35, 4면 compass).

#### (d) Suspended load — Rouse equilibrium concentration (Eq 6.36-6.71)

near-bed 평형농도 개념. Eq 6.36-6.48 로 Rouse 프로파일 유도: Rouse number $R=w_s/(u_*\kappa)$ (6.45), $C=(z_{eq}/z)^R C_{eq}-J_o/w_s$ (6.48), 순 flux $J_o=w_s(C_{eq}-C_{ne})$ (6.49), 층평균 $J_o=w_s(\bar C_{eq}-\bar C)$ (6.51). depth-avg 2D 확장 (6.55-6.63).

**평형농도 $C_{eq}=C_{eq}(d,\rho_s,\rho_w,w_s,u_*,\nu)$ (6.64)** — 3 옵션 (Garcia-Parker 1991 리뷰):
- **Smith-McLean 1977** (6.65): $C_{eq}=\rho_s\frac{0.65\gamma_o T}{1+\gamma_o T}$, $\gamma_o=2.4\times10^{-3}$, $T=(\tau_b-\tau_{cs})/\tau_{cs}$ (6.66)
- **van Rijn 1984** (6.67): $C_{eq}=0.015\rho_s\frac{d}{z_{eq}^*}T^{3/2}R_d^{-1/5}$
- **Garcia-Parker 1991** (6.68-6.71): $C_{jeq}=\rho_s\frac{A(\lambda Z_j)^5}{1+3.33A(\lambda Z_j)^5}$, $A=1.3\times10^{-7}$ — **straining $\lambda$ + hiding $F_H$ factor** 로 **armoring**(multi-class) 표현. 단일 class 시 λ=F_H=1.

### 2.2 §6.3.2 Cohesive Sediments (pp.88-92)

#### (a) Settling — floc, 4 옵션 (Eq 6.72-6.82)

응집(flocculation) 반영. 일반형 $w_{se}=w_{se}(d,C,du/dz,q)$ (6.72):
- **Opt1 Hwang-Mehta 1989** (6.73): $w_s=aC^n/(C^2+b^2)^m$ — Lake Okeechobee, 저농도↓·고농도↓ 포물선
- **Opt2 Shrestha-Orlob 1996** (6.74-6.76): $cw_s=C^\alpha\exp(-4.21+0.147G)$, 연직전단 $G$
- **Opt3 Ziegler-Nisbet 1994** (6.77-6.80): $w_s=a d_f^b$, floc diameter $d_f=\sqrt{\alpha_f/(C\sqrt{\tau_{xz}^2+\tau_{yz}^2})}$
- **Opt4 generalized** (6.81-6.82): $C'=\tau C$ 3-구간 power-law

#### (b) Deposition — Krone (Eq 6.83)

$$J_o^d=\begin{cases} -w_s C_d\left(\frac{\tau_{cd}-\tau_b}{\tau_{cd}}\right)=-w_s P_d C_d, & \tau_b<\tau_{cd} \\ 0, & \tau_b\ge\tau_{cd} \end{cases} \quad (6.83)$$

deposition 확률 $P_d=(\tau_{cd}-\tau_b)/\tau_{cd}$ (Krone/Partheniades 계열, [[efdc_sedzlj]] §2.1 Gessler-Krone 대응). $\tau_{cd}$ = 침적 임계응력 (0.06-1.1 N/m², calibration).

#### (c) Erosion — surface/mass, Partheniades-type (Eq 6.84-6.90)

mass erosion(τb>depth-varying 강도 τs, 급속) vs surface erosion(점진). surface (Eq 6.84-6.85):

$$J_o^r=w_r C_r=\frac{dm_e}{dt}\left(\frac{\tau_b-\tau_{ce}}{\tau_{ce}}\right)^\alpha\ \text{or}\ \frac{dm_e}{dt}\exp\left(-\beta\left(\frac{\tau_b-\tau_{ce}}{\tau_{ce}}\right)^\gamma\right),\quad \tau_b\ge\tau_{ce} \quad (6.84,6.85)$$

(6.84 consolidated bed / 6.85 soft partially-consolidated). 임계 $\tau_{ce}$ 3 옵션: **Opt1 Hwang-Mehta 1989** $\tau_{ce}=a(\rho_b-\rho_l)^b+c$ (6.87, a=0.883·b=0.2·c=0.05·ρ_l=1.065) / **Opt2-3 Sanford-Maa 2001** void-ratio $\tau_{ce}=\tau_{ci}(1+\varepsilon_r)/(1+\varepsilon_b)$ (6.88-6.89) / **Opt4** $\tau_{ce}=\tau_{ci}$ (6.90).

### 2.3 §6.3.3 Consolidation of Mixed Beds (pp.92-95, Eq 6.91-6.110)

cohesive+non-cohesive 혼합 bed 압밀. pore water 분배 (6.91-6.92), void ratio $\varepsilon=\phi/(1-\phi)$ (6.89), 혼합 void ratio = 체적가중평균 (6.96/6.101). Gibson-type 유효응력 압밀: 비배출 $q$ (6.102), $\lambda=-\frac{1}{f_{sc}}\frac{\partial}{\partial\varepsilon}(\sigma/g\rho_w)$ (6.107) constitutive, tri-diagonal 해 → 층두께 갱신 (6.108-6.110). non-cohesive 분획 비압축 가정.

## 3. §6.4 SEDZLJ — source-analysis 매핑 (pp.95-120)

§6.4 이론(6.111~ Eq)의 상세는 **소스 직접 read** 로 [[efdc_sedzlj]] 에 기커버 (7 sub-routine 2019 lines). 본 노트는 이론식↔소스 대응만:

| Theory v12 §6.4 | source-analysis [[efdc_sedzlj]] | 핵심 |
|---|---|---|
| §6.4.1 Background (p.95) | §Scope | hindcast erosion/deposition 비유일성 → SEDFlume 직접측정 동기 |
| §6.4.2 Bed Shear Stress (p.97) | §3 `s_shear.f90` | Christoffersen-Jonsson 1985 wave-current (Eq 3.8/3.10/4.11/4.12/4.23/4.25) |
| §6.4.3 Erosion Rate (p.98) | §2.6 `s_sedzlj.f90` | Sedflume `NSEDFLUME=1` log-linear vs `98` power-law A·τ^N |
| §6.4.4 Suspended Load (p.104) | §2.1-2.3 | Gessler 1965 / Krone deposition probability |
| §6.4.5 Bedload (p.105) | §5 `s_bedload.f90` | Van Rijn 1981 (Eq 20a/20b/21) |
| §6.4.6 Bed Armoring (p.107) | §2.4-2.8 | active layer TACT + layer reconstitution |
| (bed slope) | §4 `s_slope.f90` | Lick 2009 Eq 3.36 SH_SCALE |

> **Original vs SEDZLJ 알고리즘 대비** (theory-doc-v12 §4.1 후보 `efdc-sedzlj-vs-sedtran-comparison` 부분충족): Original = van Rijn 1984 평형농도(Rouse) + class별 상수 erosion / SEDZLJ = SEDFlume 직접측정 erosion rate + 통합 multi-class active-layer. 공통 = Eq 6.1 부유이동 + van Rijn bedload 계열.

## 4. Ch 6 소스/legacy 매핑 요약

| 매뉴얼 § | 이론식 | 소스/legacy |
|---|---|---|
| §6.2 부유이동 (공통) | 6.1-6.12 | [[efdc_transport_scheme]] CALTRAN/CALTRAN_AD (MPDATA) |
| §6.3.1 non-cohesive | 6.13-6.71 | Original SedTran ([[efdc_sediment]]), legacy [[efdc-sediment-theory-2003]] §6 |
| §6.3.2 cohesive | 6.72-6.90 | Krone/Partheniades — legacy 2003 §7, SEDZLJ Gessler-Krone [[efdc_sedzlj]] §2.1 |
| §6.3.3 consolidation | 6.91-6.110 | 혼합 bed 압밀 (Gibson) |
| §6.4 SEDZLJ | 6.111~ | [[efdc_sedzlj]] 소스 직접 (Card C36 NSEDFLUME) |

## 5. 관련

- [[efdc_sedzlj]] — SEDZLJ branch 소스 직접 read (본 노트가 이론↔소스 매핑한 대상)
- [[efdc-sediment-theory-2003]] — Tetra Tech 2002/2003 Hamrick legacy reference (§6.3 Original 의 원전)
- [[efdc-theory-v12-ch2-hydrodynamics]] · [[efdc-theory-v12-ch5-temperature-heat]] — Theory Ch-series 연속
- `concepts/sediment-transport/02-theory.md` — Shields/Rouse/settling 도메인 관점 (Soulsby 1997 cross)
- **Primary sources**: Hamrick 1992 / Tetra Tech 2007b · van Rijn 1984 · Smith-McLean 1977 · Garcia-Parker 1991 · Meyer-Peter-Müller 1948 · Krone / Partheniades · Mehta et al. 1989 · Hwang-Mehta 1989 · Shrestha-Orlob 1996 · Ziegler-Nisbet 1994 · Sanford-Maa 2001 · Jones-Lick 2000 · Ziegler-Lick 1988/1986.
