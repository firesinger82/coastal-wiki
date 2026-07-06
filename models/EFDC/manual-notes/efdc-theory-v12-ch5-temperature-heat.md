---
title: "EFDC+ Theory v12 Ch 5 TEMPERATURE AND HEAT TRANSFER — Surface/Bed Heat Exchange + COARE 3.6 + Ice Formation/Melt deep note"
topic: efdc-theory-v12-ch5-temperature-heat
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf 본문 pp.59-71 (Ch 5 전체, 물리 PDF p.72-84) 직접 추출 — 식 (5.1)~(5.33) + Table 5.1 (light attenuation Paulson-Simpson/Kraus-Businger/Jerlov) + Table 5.2 (evaporation IEAVAP 0-10) 인용. 소스 교차검증: EFDCPlus_Stable(12.4, sha 3ed76b6) EFDC/Transport/mod_heat.f90 (Rosati-Miyakoda:60-61·COARE ISTOPT(2)==2:691·EQUILIBRIUM_TEMPERATURE:1551·freezing TF=-0.0545*SAL:1181)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — PDF Read pages 72-84 직접 + mod_heat.f90 grep 교차검증"
verification_date: 2026-07-04
related:
  - models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md
  - models/EFDC/manual-notes/efdc-theory-doc-v12.md
  - models/EFDC/source-analysis/
  - concepts/sst/04-code-and-tools.md
---

# EFDC+ Theory v12 Ch 5 TEMPERATURE AND HEAT TRANSFER — 식 level deep 노트

> 출처: [`EFDC_Theory_Document_Ver_12.pdf`](../raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf) Chapter 5 (문서 pp.59-71, 물리 PDF p.72-84), DSI LLC.
> 소스 교차검증: [`mod_heat.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/Transport/mod_heat.f90) (EFDC+ Stable = 12.4, sha `3ed76b6`).
> 본 노트는 [[efdc-theory-doc-v12]] Ch 별 깊이 노트 시리즈 — [[efdc-theory-v12-ch2-hydrodynamics]](수력) 에 이은 **Ch 5 온도/열전달**. equation level + primary source + 소스 라인 인용.

## 0. Ch 5 구조 + 기본 방정식

Ch 5 는 curvilinear-sigma 좌표의 **generic transport equation (Eq 3.1)** 을 온도(T)에 적용한 것으로, 이류·난류혼합·수평확산은 수력 모듈이 제공하고, 이 장은 **열원/열침(sources/sinks)** 을 정의한다 (p.59). 열원: surface heat exchange · short wave radiation absorption · bottom heat exchange · inflow/outflow BC. 개념도 Fig 5.1 (atmosphere–water column–bed 3층, epilimnion/thermocline/hypolimnion).

| § | 주제 | 식 | primary source |
|---|---|---|---|
| 5.1 | Surface Heat Exchange (3 방법) | 5.1–5.12 | Rosati-Miyakoda 1988 / Fairall(COARE) / Brady 1969 |
| 5.2 | Short Wave Radiation (1/2-band + WQ-linked) | 5.13–5.17 | Beer's law / Paulson-Simpson 1977 / Jerlov 1968 |
| 5.3 | Bed Heat Exchange | 5.18–5.20 | — |
| 5.4 | Ice Formation and Melt (6 sub) | 5.21–5.30 | W2 (Wells-Cole 2000) |
| 5.5 | Water Volume Evaporative Losses | 5.31–5.33 | Edinger et al. 1974 |

## 1. §5.1 Surface Heat Exchange (pp.60-62)

수면(z=1) 경계조건 (Eq 5.1):

$$-\frac{\rho c_p A_b}{H}\frac{\partial T}{\partial z} = H_L + H_E + H_C \quad (5.1)$$

- $H_L$ = long wave back radiation flux (W/m²), $H_E$ = latent heat flux, $H_C$ = sensible heat flux. $A_b$ = vertical eddy diffusivity, $H$ = water depth.

수면 열교환 **3 방법**: (1) Full Heat Balance, (2) COARE 3.6 bulk algorithm, (3) Equilibrium Temperature. 소스에서 `ISTOPT(2)` 스위치로 선택 (mod_heat.f90: `==2` COARE:691, `==4` external equilibrium:850).

### 1.1 §5.1.1 Full Heat Balance (p.60) — Rosati-Miyakoda 1988 / Hamrick 1992

$$H_L = \varepsilon\sigma(T_s+273.15)^4(0.39-0.05\sqrt{e_a})(1+B_c C) + 4\varepsilon\sigma(T_s+273.15)^3(T_s-T_a) \quad (5.2)$$
$$H_E = c_e\rho_a L_E W_s (e_s-e_a)\frac{0.622}{P_a} \quad (5.3)$$
$$H_C = c_h\rho_a c_{pa} W_s (T_s-T_a) \quad (5.4)$$

| 상수 | 값 |
|---|---|
| $\varepsilon$ emissivity | 0.97 |
| $\sigma$ Stefan-Boltzmann | $5.67\times10^{-8}$ W/m²/K⁴ |
| $B_c$ empirical | 0.8 |
| $C$ cloud fraction | 0 (청천)–1 (전운) |
| $\rho_a$ atmos density | 1.2 kg/m³ |
| $c_{pa}$ air specific heat | 1005 J/kg/K |
| $L_E$ latent heat evap | $2.501\times10^6$ J/kg |

$e_s$ = 수면온도 포화증기압, $e_a$ = 실제증기압 (mb), $P_a$ = 대기압, $c_e,c_h$ = turbulent exchange coeff, $W_s$ = 풍속. **소스 근거**: mod_heat.f90:60-61 주석 "The heat flux terms are derived from a paper by Rosati and Miyakoda (1988) 'A General Circulation Model for Upper Ocean'". full heat balance (non-legacy) 는 ice 모듈과 완전 연동 (p.61).

> ⚠ **disclosed-gap (cloud sign, code≠manual, 2026-07-04)**: 소스 [`mod_heat.f90:648`](../source-analysis/efdc_heat_temperature.md)([[efdc_heat_temperature]] §1.1)는 구름인자를 **`(1-0.8·CLOUDT)`** 로 구현하나, 위 Eq 5.2 인쇄본은 `(1+B_cC)`. 구름↑ → 순 장파 냉각↓ 가 물리적으로 옳으므로 **소스 `(1-0.8C)` 가 표준(Rosati-Miyakoda 1988 원형)**, 매뉴얼 `(1+B_cC)` 는 부호 오식으로 판단(`1-B_cC` 여야 함). 실행값은 소스 기준.

### 1.2 §5.1.2 COARE 3.6 Bulk Algorithm (p.61) — EFDC+ 12.1부터 신규

Coupled Ocean–Atmosphere Response Experiment v3.6 (Fairall et al. 1996, 2003) — **Monin-Obukhov similarity theory (MOST)** 기반 near-surface flux. bulk 변수로 sensible/latent flux + stress 추정.

$$\overline{w'x'} = c_x^{1/2}c_d^{1/2}S\Delta X = C_x S\Delta X \quad (5.5)$$

$x$ = 풍속성분/수증기 비습 등, $c_x$ = bulk transfer coeff, $S$ = 평균풍속, $\Delta X$ = air-sea 평균차. Reynolds 평균으로:

$$H_C = \rho_a c_{pa}\overline{w'T'} = \rho_a c_{pa} C_h S(T_s-\theta) \quad (5.6)$$
$$H_E = \rho_a L_e\overline{w'q'} = \rho_a L_e C_e S(q_s-q) \quad (5.7)$$

$\theta$ = potential temperature, $q$ = 수증기 mixing ratio, $q_s$ = 계면값. 수면조도 = **Charnock 식 + smooth flow limit** (Eq 5.8):

$$z_0 = \frac{\alpha u_*^2}{g} + \frac{0.11\nu}{u_*} \quad (5.8)$$

$u_*$ = friction velocity, $\nu$ = kinematic viscosity. **소스**: mod_heat.f90:691 `ISTOPT(2)==2 → COARE 3.6`, 입력변환 :704-737 (CDCOARE·EVACOARE evap rate m/s).

### 1.3 §5.1.3 Equilibrium Temperature (p.62) — CE-QUAL-W2 (Wells-Cole 2000) / Brady 1969

순 수면열교환률을 equilibrium temperature $T_e$ (net flux=0 인 온도) 로 선형화 (Eq 5.9):

$$H_n = -K_{aw}(T_s-T_e) \quad (5.9)$$

7개 열교환 과정을 $K_{aw}$ + $T_e$ 에 집약. Brady et al. 1969 근사식 (**English units**, EFDC+ 내부 SI↔English 변환):

$$T_e = \frac{I_{sw}}{23 + f(W)(\beta+0.255)} + T_d \quad (5.10)$$
$$K = 23 + (\beta_w+0.225)\,17 W_2 \quad (5.11)$$
$$\beta_w = 0.255 - 0.0085 T_w - 0.000204 T_w^2 \quad (5.12)$$

$\beta = 0.255-0.0085T^*+0.000204T^{*2}$, $T^*=0.5(T_s+T_d)$, $T_d$ = dew point (°F), $W_2$ = 2 m 풍속 (mph). **소스 교차검증** (mod_heat.f90 `SUBROUTINE EQUILIBRIUM_TEMPERATURE`:1551) — `BETA=0.255-8.5E-3*TSTAR+2.04E-4*TSTAR**2`:1583, `TSTAR=(ET+TDEW_F)*0.5`:1582, `CSHE=15.7+(0.26+BETA)*FW`:1585, ETP 반복해 (`do J` 루프 :1587-1594) → 매뉴얼 "iterative/approximate technique (Brady et al. 1969)" 실장 확인. 코드 계수(15.7·0.26)는 매뉴얼 제시형(23·0.255)의 대체 Edinger/Brady 표현이며 English↔SI 변환 상수(`W_M2_TO_BTU_FT2_DAY=7.60796` 등 :33-37) 동반. equilibrium module 도 ice 모듈과 완전 연동.

## 2. §5.2 Short Wave Radiation (pp.63-65)

수면 도달 단파복사 (Eq 5.13) — 수관 shading + ice + emergent shoot 감쇠:

$$I_{sw} = I_0 S_f \min\{\exp[-K_{e,me}(H_{rps}-H)],1\}\min\{\exp[-K_{e,ice}H_{ice}],1\} \quad (5.13)$$

$I_0$ = 측정 태양복사, $S_f$ = 수관/지형 shading factor, $H_{ice}$ = 얼음두께, $K_{e,ice}$/$K_{e,me}$ = ice/emergent shoot 소광계수, $H_{rps}$ = rooted plant shoot 높이.

### 2.1 §5.2.1 One-band (p.63) — Beer's Law

$$I(z) = I_{sw}\exp(-\zeta z) \quad (5.14)$$

$\zeta$ = light extinction coefficient (1/m), $z$ = 수심.

### 2.2 §5.2.2 Two-band (p.64) — legacy EFDC

fast/slow 2 감쇠계수 (상부 5 m 적색광 급감 + 10 m 이하 청록광 완감):

$$I(z) = I_{sw}[R\exp(z\zeta_f)+(1-R)\exp(z\zeta_s)] \quad (5.15)$$

**Table 5.1** (Paulson-Simpson 1977 adapted) — 관측 fit 계수:

| Author | Water Type | R | ζ_f (1/m) | ζ_s (1/m) |
|---|---|---|---|---|
| Paulson-Simpson 1977 | Run 1 | 0.74 | 0.588 | 0.063 |
| | Composite | 0.62 | 0.667 | 0.050 |
| Kraus-Businger 1994 | Very Clear Water | 0.4 | 0.200 | 0.025 |
| Jerlov 1968 | Type I | 0.58 | 2.857 | 0.043 |
| | Type I (upper 50 m) | 0.68 | 0.833 | 0.036 |
| | Type IA | 0.62 | 1.667 | 0.050 |
| | Type IB | 0.67 | 1.000 | 0.059 |
| | Type II | 0.77 | 0.667 | 0.071 |
| | Type III | 0.78 | 0.714 | 0.127 |

### 2.3 §5.2.3 Water Quality Linked (pp.64-65)

Full Heat / Equilibrium Temperature 옵션용 — 상층에 항상 고정비율 β 흡수 (Eq 5.16):

$$I(z) = (1-\beta)I_{sw}\exp(-K_e z) \quad (5.16)$$

**총 소광계수** — rooted plant 포함 (Eq 5.17):

$$K_{ess} = K_{e,b} + K_{e,TSS}TSS + K_{e,POC}POC + K_{e,DOC}DOC + K_{e,Chl}\sum Chl + K_{e,MAC}MAC \quad (5.17)$$

$K_{e,b}$ = 배경, TSS = 유사모듈 총부유물, POC/DOC = 수질모듈 유기탄소, Chl = 조류 chlorophyll-a, MAC = 고정생물/식물 shoot. **모듈 결합 단계**: (a) 수력+온도만 → $K_{e,b}$; (b) +TSS → $K_{e,b}+K_{e,TSS}$; (c) full WQ → 전항 (§5.2.3.1, p.65).

## 3. §5.3 Bed Heat Exchange (p.66)

저면-수관 열교환 (deep lake/reservoir 온도개선, 통상 무시 가능) (Eq 5.18-5.20):

$$H_b = -(K_{b,v}U + K_{b,c})(T_w-T_b) \quad (5.18)$$
$$U = \sqrt{u_1^2+v_1^2} \quad (5.19)$$
$$\frac{\delta(D_B T_b)}{\delta t} = -(K_{b,v}U+K_{b,c})(T_b-T_w) \quad (5.20)$$

$K_{b,v}$ = convective (W·s/m³/°C), $K_{b,c}$ = conductive (W/m²/°C, 통상 0.3, 표면계수 대비 ~2 order 작음), $D_B$ = bed thermal thickness (m, calibration; 클수록 $T_b$ 느리게 변화). 코드는 양변을 $\rho c_p$ 로 나눠 $K_{b,c}$ 단위 m/s·$K_{b,v}$ 무차원화. 연평균 기온이 $T_b$ 초기추정치로 양호.

## 4. §5.4 Ice Formation and Melt (pp.67-69) — W2 (Wells-Cole 2000)

EFDC+ ice 모듈 = W2 기반 **coupled heat** 접근. ice **동역학(block/chunk 이동)은 미구현**. (한국 겨울 결빙 해역/저수지 적용 관련.)

### 4.1 §5.4.1 Heat Balance (p.67)

water-to-ice-air 열수지 (Eq 5.21):

$$\rho_i L_f\frac{dh}{dt} = h_{ai}(T_i-T_e) - h_{wi}(T_w-T_m) \quad (5.21)$$

$\rho_i$ = ice density, $L_f$ = 융해잠열, $h_{ai}$ = ice-to-air 계수, $h_{wi}$ = water-to-ice (through melt layer) 계수, $T_m$ = melt temp. 초기 결빙두께 — 음(-)의 수면온도를 등가 얼음두께로 변환 (Eq 5.22):

$$\theta_0 = -\frac{T_{wn}\rho_w c_{pw}h}{\rho_i L_f} \quad (5.22)$$

$T_{wn}$ = local temporary negative water temperature, $h$ = 층두께. **소스**: mod_heat.f90 supercooled 상태 `TFS=TF-0.01`:1188, frazil ice growth `ISICE==4`:1190 (`FRAZILICE` 축적 :1197).

### 4.2 §5.4.2 Ice Surface Temperature (p.68)

$$T_s^n = \frac{\theta^{n-1}}{K_i}[H_{sn}^n+H_{an}^n-H_{br}(T_s^n)-H_c(T_s^n)] \quad (5.23)$$
$$H_{sn}+H_{an}-H_{br}-H_e-H_c+q_i = \rho_i L_f\frac{d\theta_{ai}}{dt},\quad T_s=0°C \quad (5.24)$$
$$q_i = K_i\frac{T_f-T_s(t)}{\theta(t)} \quad (5.25)$$

$K_i$ = 얼음 열전도도 (W/m/°C), $T_f$ = 결빙점, $q_i$ = 얼음통과 heat flux, $H_{sn}/H_{an}$ = 입사 단파/장파, $H_{sr}/H_{ar}$ = 반사 단파/장파, $H_{br}$ = 수면 back radiation.

### 4.3 §5.4.3 Freezing Temperature (p.68) — TDS 의존

$$T_f = \begin{cases} -0.0545\,TDS, & TDS<35\ ppt \\ -0.3146-0.0417\,TDS-0.000166\,TDS^2, & TDS>35\ ppt \end{cases} \quad (5.26)$$

**소스 정합 확인** (mod_heat.f90:1180-1184): `SAL<35 → TF=-0.0545*SAL`, `else TF=-0.31462-0.04177*SAL-0.000166*SAL*SAL`. (매뉴얼 반올림형 -0.3146/-0.0417 vs 소스 -0.31462/-0.04177 — 동일식.) `ISTRAN(1)==0` (염분 미모의) 시 `TF=0`.

### 4.4 §5.4.4–5.4.6 Ice Melt / Growth (p.69)

Air/water 계면 melt (Eq 5.27): $\rho_i c_{pi}\frac{T_s(t)}{2}\theta(t) = \rho_i L_f\Delta\theta_{ai}$. Bottom growth/melt (Eq 5.28-5.29):

$$q_i - q_{iw} = \rho_i L_f\frac{d\theta_{iw}}{dt} \quad (5.28)$$
$$\Delta\theta_{iw}^n = \frac{1}{\rho_i L_f}\left[K_i\frac{T_f-T_s^n}{\theta^{n-1}} - h_{wi}(T_w^n-T_f)\right] \quad (5.29)$$

얼음 저면 태양복사 (Eq 5.30) — albedo·surface absorption·감쇠:

$$H_{ps} = H_s(1-\alpha_i)(1-\beta_i)\exp[-\gamma_i\theta(t)] \quad (5.30)$$

$\alpha_i$ = ice albedo, $\beta_i$ = 얼음표면 흡수분율, $\gamma_i$ = ice extinction coeff.

## 5. §5.5 Water Volume Evaporative Losses (pp.70-71)

증발에 의한 수량 손실 (Full Heat/Equilibrium 은 flux 만, 수량손실은 선택). 수심변화 (Eq 5.31):

$$\Delta z = E\Delta t = \frac{H_E}{\rho L_E}\Delta t \quad (5.31)$$

증발잠열 flux — Edinger et al. 1974 (Eq 5.32-5.33):

$$H_E = f(W)(e_s-e_a) \quad (5.32)$$
$$f(W) = a + bW + cW^2 \quad (5.33)$$

**Table 5.2** — Evaporation methods (`IEAVAP` 스위치, wind coeff a/b/c):

| IEAVAP | Approach | Usage | a | b | c |
|--:|---|---|--:|--:|--:|
| 0 | Do Not Include Evaporation | — | | | |
| 1 | Use Evaporation from ASER | Measured/Externally Est. | | | |
| 2 | EFDC Original | | | | |
| 3 | Ward 1980 | Cooling Lake | 0.0 | 3.534 | 0.0 |
| 4 | Harbeck Jr 1964 | Cooling Lake | 0.0 | 3.818 | 0.0 |
| 5 | Brady et al. 1969 | Cooling Pond | 6.442 | 0.0 | 0.322 |
| 6 | Anderson et al. 1954 | Large Lake | 0.0 | 2.403 | 0.0 |
| 7 | Webster-Sherman 1995 | Lakes | 2.717 | 2.743 | 0.0 |
| 8 | Fulford-Sturm 1984 | Rivers | 8.359 | 2.090 | 0.0 |
| 9 | Gulliver-Stefan 1984 | Streams | 7.732 | 1.672 | 0.0 |
| 10 | Edinger et al. 1974 | Lakes/Rivers | 6.9 | 0.0 | 0.345 |

## 6. 소스 매핑 요약

| 매뉴얼 § | 소스 (mod_heat.f90, 12.4 sha 3ed76b6) |
|---|---|
| §5.1.1 Full Heat Balance | Rosati-Miyakoda 주석 :60-61 |
| §5.1.2 COARE 3.6 | `ISTOPT(2)==2` :691, 입력변환 :704-737 |
| §5.1.3 Equilibrium Temp | `SUBROUTINE EQUILIBRIUM_TEMPERATURE` :1551-1603 (BETA:1583·CSHE:1585·반복해 J-loop:1587) |
| §5.3 Bed Heat | `4.43E-14 = 1/rhob/cpb·5.67e-8` 주석 :968,992 |
| §5.4.3 Freezing Temp | `TF=-0.0545*SAL` :1181 (매뉴얼 Eq 5.26 정합) |
| §5.4.1 Ice (frazil) | `ISICE==4` frazil transport :1190, `FRAZILICE` :1197 |
| 단위변환 (W2 English) | `MPS_TO_MPH`·`W_M2_TO_BTU_FT2_DAY` 등 :33-37 |

## 7. 관련

- [[efdc-theory-v12-ch2-hydrodynamics]] — Ch 2 수력 (generic transport Eq 3.1 이 온도의 상위 방정식)
- [[efdc-theory-doc-v12]] — Theory v12 전체 개요·Ch 구조
- `concepts/sst/04-code-and-tools.md` — 해수면온도 모델링 도메인 관점 (COARE bulk flux cross-model: [[roms_bulk_flux_coare]] ROMS COARE 3.0 와 대조)
- **Primary sources**: Rosati-Miyakoda 1988 (JPO 18:1601) · Fairall et al. 1996/2003 (COARE) · Brady-Graves-Geyer 1969 · Wells-Cole 2000 (CE-QUAL-W2) · Paulson-Simpson 1977 · Jerlov 1968 · Edinger et al. 1974.
