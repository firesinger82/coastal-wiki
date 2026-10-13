---
title: "SWAN swantech Ch 2.3.5-2.3.8 — Vegetation/Sea ice/Bragg/Gen1·2 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf Ch 2 §2.3.5 Vegetation (p.44-47) + §2.3.6 Sea ice (p.47-49) + §2.3.7 Bragg scattering (p.48-50) + §2.3.8 First/Second-gen (p.50-52). Primary refs: Dalrymple 1984, Mendez-Losada 2004, Jacobsen 2019, Benit-Reniers 2022, Sand 1982, Collins-Rogers 2017, Meylan 2014·2018, Doble 2015, Rogers 2019·2021a·2021b, Yu 2019, Liu 2020, Ardhuin-Herbers 2002, Ardhuin 2003, Holthuijsen-de Boer 1988, Pierson-Moskowitz 1964, Shore Protection Manual 1973, Cavaleri-Malanotte-Rizzoli 1981, Snyder 1981."
citation_status: verified
verification_method: "swantech PDF 52–60쪽(인쇄 44–52쪽)의 식 (2.108)–(2.130)을 대조했다. 인쇄식과 동치 전사 및 구현 차이를 구분했다. 2026-10-13 R2 최종 결론과 이번 추가·수정 줄을 원문 대조했다." # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — Eq 2.108-2.130 verbatim + 4 sea ice methods + Bragg theory"
verification_date: 2026-06-01
last_source_check: 2026-10-13 (recovery 대조 반영)
related:
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/source-analysis/swan-bragg-scattering.md
---

# swantech Ch 2.3.5-2.3.8 verified verbatim

> swantech.pdf p.44-52 직접 read. SWAN 의 추가 source/sink: vegetation/ice/Bragg/gen1·2. Eq 2.108-2.130 + 30+ references.

## 1. §2.3.5 Wave damping due to vegetation (p.44-47)

### 1.1 Triad noncollinear extension — Benit-Reniers 2022 (Eq 2.108)

DCTA extension (collinear → noncollinear) via Sand 1982 transfer function:

$$S_{\text{nl3}}(\sigma_1, \theta_1) = \lambda c_{g,1} \frac{\sin(-\beta) \tilde{k}^{2-p}}{\tilde{\sigma}^2 d^2} \times \int_0^{2\pi} \int_0^{\infty} \left(\frac{\tanh \bar{k}d}{\bar{k}d}\right)^4 \left[\frac{G(\Delta\theta_{23})}{G(0)}\right]^2 E(\sigma_3, \theta_3) [c_{g,2} k_2^p E(\sigma_2, \theta_2) - c_{g,1} k_1^p E(\sigma_1, \theta_1)] d\sigma_2 d\theta_2 \quad \text{(2.108)}$$

(2.108)은 (2.107)과 같은 작용 밀도 정규화이다. 에너지 원천항으로 표시할 때는 $\sigma_1$을 곱한다. (swantech PDF 52쪽 / 인쇄 44쪽; `src/swancom4.ftn:4768` `DS2DD = FRINTF * SIG2 * DDIR`)

- $G(\Delta\theta_{nm})$ = Sand 1982 transfer function
- $\Delta\theta_{nm} = \theta_n - \theta_m$
- LTA/DCTA 계산 조건: **$Ur \ge 0.1$** (Ursell number)
- **41.45 since** revised formulation

### 1.2 Vegetation damping — Dalrymple 1984 cylinder approach (Eq 2.109)

> "A popular method of expressing the wave dissipation due to vegetation is the **cylinder approach** as suggested by **Dalrymple et al. (1984)**."

Energy losses = vegetation 의 fluid 에 작용한 force (Morison equation type). Plant motion + inertial + friction 무시.

$$\varepsilon_v = \frac{2}{3\pi} \rho C_D b_v N_v \left(\frac{gk}{2\sigma}\right)^3 \frac{\sinh^3 k\alpha h + 3 \sinh k\alpha h}{3k \cosh^3 kh} H^3 \quad \text{(2.109)}$$

- $\rho$ = water density
- $C_D$ = drag coefficient
- $b_v$ = stem diameter
- $N_v$ = plants per square meter
- $\alpha h$ = vegetation height
- $h$ = water depth
- $H$ = wave height

### 1.3 Mendez-Losada 2004 irregular wave 수정 (Eq 2.110-2.113)

$$\langle \varepsilon_v \rangle = \frac{1}{2\sqrt{\pi}} \rho \tilde{C}_D b_v N_v \left(\frac{gk}{2\sigma}\right)^3 \frac{\sinh^3 k\alpha h + 3 \sinh k\alpha h}{3k \cosh^3 kh} H_{\text{rms}}^3 \quad \text{(2.110)}$$

- $\tilde{C}_D$ = bulk drag (wave height 의존) — **유일 calibration parameter**
- $H_{\text{rms}}^2 = 8 E_{\text{tot}}$

**SWAN spectral 확장 (Eq 2.111)**:

$$S_{\text{ds,veg}}(\sigma, \theta) = \frac{D_{\text{tot}}}{E_{\text{tot}}} E(\sigma, \theta) \quad \text{(2.111)}$$

**Final expression (Eq 2.113)**:

문서 인쇄식 (swantech PDF 53쪽 / 인쇄 45쪽):

$$S_{\text{ds,veg}} = -\sqrt{\frac{2}{\pi}} g^2 \tilde{C}_D b_v N_v \left(\frac{\tilde{k}}{\tilde{\sigma}}\right)^3 \frac{\sinh^3 \tilde{k}\alpha h + 3 \sinh \tilde{k}\alpha h}{3k \cosh^3 \tilde{k}h} \sqrt{E_{\text{tot}}} E(\sigma, \theta) \quad \text{(2.113)}$$

인쇄식의 분모에는 평균 표시가 빠졌다. 구현식의 분모는 $3\widetilde k\cosh^3(\widetilde kh)$이다. (`src/swancom2.ftn:859` `C = 3.*KMESPC*(COSH(KD))**3`)
평균 주파수는 문서에서 $m_0/m_{-1}$이다. 구현은 $m_1/m_0$ 평균 주파수를 사용한다. (`src/swancom1.ftn:6024` `SMEBRK = SIGM01`; swantech PDF 53쪽 / 인쇄 45쪽의 (2.46) 인용)

### 1.4 다층 vegetation (Eq 2.114-2.116)

$$S_{\text{ds,veg}} = \sum_{i=1}^{I} S_{\text{ds,veg},i} \quad \text{(2.114)}$$

각 layer $i$ 의 식:

문서 인쇄식 (swantech PDF 53쪽 / 인쇄 45쪽):

$$S_{\text{ds,veg},i} = -\sqrt{\frac{2}{\pi}} g^2 \tilde{C}_{D,i} b_{v,i} N_{v,i} \left(\frac{\tilde{k}}{\tilde{\sigma}}\right)^3 \sqrt{E_{\text{tot}}} \frac{(\sinh^3 \tilde{k}\alpha_i h - \sinh^3 \tilde{k}\alpha_{i-1}h) + 3(\sinh \tilde{k}\alpha_i h - \sinh \tilde{k}\alpha_{i-1}h)}{3k \cosh^3 \tilde{k}h} E(\sigma, \theta) \quad \text{(2.115)}$$

구현식의 분모는 $3\widetilde k\cosh^3(\widetilde kh)$이다. (`src/swancom2.ftn:859` `C = 3.*KMESPC*(COSH(KD))**3`)

문서 인쇄식은 $\sum_{i=1}^{I}\alpha_i\le1$이다. $\alpha_i$를 누적 층 경계로 정의하면 올바른 조건은 $0=\alpha_0\le\cdots\le\alpha_I\le1$이다. 층 두께 비율의 합과 구별한다. (swantech PDF 54쪽 / 인쇄 46쪽, (2.116); `src/swancom2.ftn:873` `KVEGH = KVEGH + KMESPC * LAYH(IL)`)

**Figure 2.3**: 2-layer schematic (S_veg,1 + S_veg,2 with C̃_D,1·b_v,1·N_v,1 + C̃_D,2·b_v,2·N_v,2). Mangrove tree 처럼 vertical variation.

**Horizontal variation**: $V_f = \tilde{C}_D b_v N_v$ 의 spatial control — $\tilde{C}_D = 1, b_v = 1$ 설정 시 $V_f = N_v$ (User cmd 직접 control).

### 1.5 Jacobsen 2019 alternative — frequency-dependent (canopy)

$$\delta_v = 2\Gamma S_u \sqrt{\frac{2 m_{u,0}}{\pi}}$$

with velocity spectrum:

$$S_u = \left(\frac{\sigma \cosh k(z+h)}{\sinh kh}\right)^2 S_\eta$$

$\Gamma = \frac{1}{2} \rho C_D b_v N_v \alpha_u^3$ ($\alpha_u$ = velocity reduction factor).

Depth-integrated frequency-dependent dissipation:

$$S_{\text{ds,veg}} = -\frac{1}{\rho g} \int_{-h}^{-h+h_v} \delta_v dz$$

(Simpson rule integration, $h_v$ = canopy height).

## 2. §2.3.6 Wave damping due to sea ice (p.47-49)

### 2.1 General formulation

> "A direct dissipation of wave energy occurs due to the presence of sea ice... using empirical formula. The temporal exponential decay rate of energy is"

$$D_{\text{ice}} = S_{\text{ice}}/E = -2 c_g k_i$$

- $k_i$ (1/m) = linear exponential **attenuation rate of wave amplitude** ($a(x) = H_0 \exp(-k_i x)$)
- Factor 2 = amplitude → energy decay
- $c_g$ = spatial → temporal decay

### 2.2 R19 method — Rogers 2019 polynomial (since 41.31)

> "This is a parameterization described in **Collins and Rogers (2017)** and is similar to the **'IC4M2' method implemented in WAVEWATCH III**. That method, in turn, is a generalization of the formula proposed by **Meylan et al. (2014)**."

$$k_i(f) = c_0 + c_1 f + c_2 f^2 + c_3 f^3 + c_4 f^4 + c_5 f^5 + c_6 f^6$$

$f$의 단위는 Hz이다. (`src/swancom2.ftn:1546` `FREQ = SPCSIG(IS) / PI2`)

- 7 user-defined polynomial coefficients
- $c_2$ units = s²/m
- **Default R19**: $c_2 = 1.06 \times 10^{-3}$ s²/m, $c_4 = 2.3 \times 10^{-2}$ s⁴/m (Meylan 2014 fit, **Antarctic MIZ pancake ice 10-25 m diameter**)
- 다른 calibration: Rogers 2021a (thinner ice): $c_2 = 0.208 \times 10^{-3}$, $c_4 = 5.18 \times 10^{-2}$
- Rogers 2018 (pancake/frazil): $c_2 = 0.284 \times 10^{-3}$, $c_4 = 1.53 \times 10^{-2}$

### 2.3 3 ice-thickness dependent methods (since 41.41)

#### D15 — Doble 2015

$$k_i = C_{hf,D} f^{2.13} h_{\text{ice}}$$

- Default $C_{hf,D} = 0.1$ (Weddell Sea Antarctic MIZ pancake ice)

#### M18 — Meylan 2018 "Model with Order 3 Power Law"

$$k_i = C_{hf,M} h_{\text{ice}}^1 f^3$$

- $C_{hf,M}$ = viscosity parameter
- Default 0.059 (Rogers 2021a broken floes Antarctic MIZ)
- 이전 calibrations: Liu 2020 broken floes Antarctic $C_{hf,M} = 0.00751$ / pancake-frazil Beaufort $C_{hf,M} = 0.0351$

#### R21B — Rogers 2021b (Yu 2019 Reynolds non-dimensionalization)

$$k_i = C_{hf} h_{\text{ice}}^{n/2-1} f^n$$

- Default $n = 4.5$, $C_{hf} = 2.9$ (Rogers 2021b)

### 2.4 Source term scaling — areal ice fraction

$0 \le a_{\text{ice}} \le 1$ areal ice fraction.

**Wind input reduction**:

$$S_{\text{in}} \leftarrow (1 - a_{\text{ice}}) S_{\text{in}}$$

GEN1/2에서는 $E>E_{lim}$인 완화 소산도 같은 인자로 줄어든다. 완화의 양의 우변과 대각을 함께 줄이므로 포화 목표값은 유지한다. (`src/swancom3.ftn:505–507`의 `SWIND_EXP`·`SWIND_IMP`에 대한 `FACTOR_ON_SIN` 곱)

→ open water fraction. **User cmd `SET [icewind]`** 로 reduce/disable 가능.

**Ice source scaling**:

$$S_{\text{ice}} \leftarrow a_{\text{ice}} S_{\text{ice}}$$

→ **Nonlinear interactions NOT scaled** (Rogers 2016 discussion).

### 2.5 한계 (verbatim)

- "reflection and scattering by sea ice is not represented"
- "floe size distribution is not represented"

## 3. §2.3.7 Bragg scattering (p.49-50)

### 3.1 Theory — Ardhuin-Herbers 2002

> "**Ardhuin and Herbers (2002)** developed a theory for the Bragg scattering of surface waves and proposed a source term that can be implemented in spectral wave models. This source term describes the lowest order resonant interaction between **a triad of two wave components with the same frequency but different wave number vectors** $\vec{k}$ and $\vec{k}'$ (and thus the associated directions $\theta$ and $\theta'$), and a bottom component that has the difference wave number $\vec{l} = \vec{k} - \vec{k}'$."

**Eq 2.117**:

$$\boxed{S_{\text{bragg}}(\sigma, \theta) = \chi \int_0^{2\pi} \cos^2(\theta - \theta') F^B(\vec{l}) \left[E(\sigma, \theta') - E(\sigma, \theta)\right] d\theta'} \quad \text{(2.117)}$$

with coupling coefficient:

$$\chi = \frac{2\pi \sigma^2 k^3}{c_g \sinh^2(2kd)}$$

- $F^B$ = bed elevation spectrum (small-scale variability)
- $k = |\vec{k}|$
- $(\sigma, \theta)$-space formulation (Ardhuin-Herbers 2002 와 차이 — 본 SWAN 식이 (σ,θ) 공간)

### 3.2 2 옵션 — bottom spectrum input

**Option 1**: detailed bottom topography input
- Bilinear fit → large-scale (d(x), refraction-resolved) + remainder (small-scale F^B)
- Fourier transform $\vec{x} \to \vec{k}$ → F^B

**Option 2**: precomputed bottom spectrum $F^B(\vec{k})$ external
- 모든 computational grid point 공통

### 3.3 Cutoff

> "For evaluating the Bragg scattering, an upper limit to the bathymetric variability is imposed. The cutoff $(k/l)_{\max}$, displaying the ratio between surface and bed elevation wave numbers with $l = |\vec{l}|$, **is set to 5 (Ardhuin and Herbers, 2002)**."

→ **Forward scattering 확산** + **Backward scattering 감쇠** (Ardhuin 2003).

## 4. §2.3.8 First/Second-generation model formulations (p.50-52)

### 4.1 Holthuijsen-de Boer 1988 relaxation model (Eq 2.118)

$$S_{\text{tot}} = \begin{cases}
S_{\text{in}} = A + BE, & \text{if } E < E_{\text{lim}} \text{ and } |\theta - \theta_w| < \pi/2 \\
S_{\text{ds,w}} = (E_{\text{lim}} - E)/\tau, & \text{if } E > E_{\text{lim}} \text{ and } |\theta - \theta_w| < \pi/2 \\
0, & \text{if } E > E_{\text{lim}} \text{ and } |\theta - \theta_w| > \pi/2
\end{cases} \quad \text{(2.118)}$$

- $E_{\text{lim}}$ = saturated spectrum
- $\tau$ = time scale
- $\theta_w$ = wind direction
- $A, BE$ = linear/exponential wind growth ([swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) §2 Eq 2.32)
- Modified for shallow water (Booij-Holthuijsen personal comm 1996)

### 4.2 Linear growth A (Eq 2.119-2.122)

Cavaleri-Malanotte-Rizzoli 1981 + Holthuijsen-de Boer 1988 + Holthuijsen 1996 adaptation:

$$A = \begin{cases}
\frac{\beta_1}{2g^2} C_{\text{drag}}^2 \left(\frac{\rho_a}{\rho_w}\right)^2 (U_{10} \max[0, \cos(\theta - \theta_w)])^4, & \sigma \ge 0.7 \sigma_{\text{PM,d}} \\
0, & \sigma < 0.7 \sigma_{\text{PM,d}}
\end{cases} \quad \text{(2.119)}$$

- $\beta_1 = 188$
- 문서의 $C_{drag}$는 0.0012이다. 코드 재현에는 0.00123을 쓴다. (swantech PDF 58쪽 / 인쇄 50쪽; `src/swanmain.ftn:1468` `PWIND(11) = 0.00123`)
- $\sigma_{\text{PM,d}}$ = depth-dependent PM frequency (Shore Protection Manual 1973):

$$\sigma_{\text{PM,d}} = \frac{\sigma_{\text{PM}}}{\tanh(0.833 \tilde{d}^{0.375})} \quad \text{(2.120)}$$

Dimensionless depth:

$$\tilde{d} = \frac{gd}{U_{10}^2} \quad \text{(2.121)}$$

Pierson-Moskowitz 1964 peak frequency:

$$\sigma_{\text{PM}} = \frac{0.13 g}{U_{10}} \cdot 2\pi \quad \text{(2.122)}$$

### 4.3 Exponential growth B (Eq 2.123) — Snyder 1981 rescaled

$$B = \max\left[0, \beta_2 \frac{5}{2\pi} \frac{\rho_a}{\rho_w}\left(\frac{U_{10}}{\sigma/k} \cos(\theta - \theta_w) - \beta_3\right)\right] \sigma \quad \text{(2.123)}$$

- $\beta_2 = 0.59$, $\beta_3 = 0.12$

### 4.4 Decay (relaxation model)

$$S_{\text{ds,w}}(\sigma, \theta) = \frac{E_{\text{lim}}(\sigma, \theta) - E(\sigma, \theta)}{\tau(\sigma)} \quad \text{(2.124)}$$

Time scale:

$$\tau(\sigma) = \beta_4 \left(\frac{2\pi}{\sigma}\right)^2 \frac{g}{U_{10} \cos(\theta - \theta_w)} \quad \text{(2.125)}$$

- $\beta_4 = 250$

### 4.5 Saturated spectrum (Eq 2.126)

Adapted Pierson-Moskowitz, $\cos^2$ directional distribution at $\theta_w$:

문서 인쇄식 (swantech PDF 59쪽 / 인쇄 51쪽):

$$S_{\text{tot}} = \begin{cases}
\frac{\alpha k^{-3}}{2 c_g} \exp\left\{-\frac{5}{4}\left(\frac{\sigma}{\sigma_{\text{PM,d}}}\right)^{-4}\right\} \frac{2}{\pi} \cos^2(\theta - \theta_w), & |\theta - \theta_w| < \pi/2 \\
0, & |\theta - \theta_w| \ge \pi/2
\end{cases} \quad \text{(2.126)}$$

좌변은 원천항 $S_{tot}$이 아니라 포화 스펙트럼 $E_{lim}$이다. 코드의 결과도 포화 작용 밀도 `ALIMW`이다. (`src/swancom3.ftn:435` `ALIMW(ID,IS) = ALIM1D * DIRDIS`)

### 4.6 1st-gen vs 2nd-gen — scale factor α

**1st-generation (Eq 2.127)** 문서 인쇄값:

$$\alpha = 0.0081$$

GEN1에도 천해 $\alpha$ 보정이 적용된다. (`src/swancom3.ftn:408` `ALPM = MIN ( 0.155 , MAX ( ALPMD , ALPM ) )`)

**2nd-generation (Eq 2.128-2.130)**: depends on wind sea + dimensionless depth

$$\alpha = \max\left[(0.0081 + (0.013 - 0.0081) e^{-\tilde{d}}), 0.0023 \tilde{E}_{\text{tot,sea}}^{-0.223}\right] \quad \text{(2.128)}$$

$$\tilde{E}_{\text{tot,sea}} = \frac{g^2 E_{\text{tot,sea}}}{U_{10}^4} \quad \text{(2.129)}$$

GEN2의 기본 설정에서 무차원 에너지는 $[10^{-25},.0036]$으로 제한한다. (`src/swancom3.ftn:396` `EDML = MIN ( PWIND(10) , (GRAV**2 * ETOTW) / WIND10**4 )`; `src/swancom3.ftn:397` `EDML = MAX ( 1.E-25 , EDML )`; `src/swanmain.ftn:1467` `PWIND(10) = 0.0036`; `src/swanpre1.ftn:2857`의 `EDMLPM` 입력) [10-13 전수 검증 정정]

$$E_{\text{tot,sea}} = \int_{\theta_w - \pi/2}^{\theta_w + \pi/2} \int_{0.7 \sigma_{\text{PM,d}}}^{\infty} E(\sigma, \theta) d\sigma d\theta \quad \text{(2.130)}$$

- Maximum $\alpha = 0.155$ (wind sea overshoot)
- Deep water Pierson-Moskowitz 1964: $\alpha = 0.0081$

## 5. §2.4 Ambient current on waves (p.52, brief)

> "**Longuet-Higgins and Stewart (1960, 1961, 1962)** founded the theoretical description of wave-current interactions."

- Yu 1952, Hedges 1985, Lia 1989 — observations
- Strong opposite current → wave steepness + height ↑ → current-induced whitecapping + reflection
- Blocking frequency → nonlinear transfer to higher/lower freq (Ris 1997)
- **Action density N = E/σ conserved** (Eq 2.16의 핵심) — SWAN action balance 채택 이유

## 6. §2.5 Modelling of obstacles (p.52, intro)

> "SWAN can estimate wave transmission through a (line-)structure such as a breakwater (dam). It is assumed that the obstacle is **narrow compared to the grid size** (sub-grid approach). If reality the width is large, the feature preferably is to be modeled as a bathymetric feature."

→ §2.5.1-2.5.4 deep 별도 (Transmission/Reflection/Freeboard/Diffraction).

## 7. SWAN 41.x version 변화 (요약)

| Version | Year | 추가 |
|---|---|---|
| 41.31 | — | **R19 sea ice** (Rogers 2019 polynomial) |
| 41.41 | — | **D15, M18, R21B** sea ice (thickness 의존) + **GitLab hosting** |
| 41.45 | — | DCTA noncollinear (Benit-Reniers 2022) |
| 내부 변경 번호 41.80 | 2021-09 | **Bragg scattering** ([swan-bragg-scattering](../source-analysis/swan-bragg-scattering.md)); `src/SwanBraggScat.ftn90:38` `!   41.80, September 2021: New module` [10-13 전수 검증 보완] |
| 내부 변경 번호 41.85 | 2019-01 | **IEM surfbeat** ([swan-surfbeat-iem](../source-analysis/swan-surfbeat-iem.md)); `src/SwanIEM.ftn90:38` `!   41.85, January 2019: New module` [10-13 전수 검증 정정] |
| 내부 변경 번호 41.90 | 2021-06 | **QCM** ([swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md)); `src/SwanQCM.ftn90:38` `!   41.90, June 2021: New module` [10-13 전수 검증 정정] |
| 41.91 | 2022-02 | QC surf breaking |
| 내부 변경 번호 41.95 | 2022-07 | VTK output ([swan-vtk-output](../source-analysis/swan-vtk-output.md)); `src/SwanVTKWriteHeader.ftn90:36` `!   41.95, July 2022: New subroutine` [10-13 전수 검증 정정] |

배포판 41.51과 파일 내부 변경 번호 41.80을 구별한다. 내부 번호만으로 배포판의 출시 순서를 만들지 않는다. (`src/swanmain.ftn:965` `VERNUM = 41.51`)

## 8. User cmd 매핑

| Tech 식 | User cmd | 본 위키 |
|---|---|---|
| Eq 2.109-2.116 vegetation | `VEGETATION` (p.68) | (없음 신설 후보) |
| Eq 2.117 Bragg | `BRAGG` (p.71) | [swan-bragg-scattering](../source-analysis/swan-bragg-scattering.md) |
| Sea ice 4 methods | `SICE` (p.70) | (없음 신설 후보) |
| 1st/2nd gen | `GEN1` (p.57) / `GEN2` (p.58) | (없음) |
| 3rd gen | `GEN3` (p.58) — default | [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) |

## 9. 핵심 references (Ch 2.3.5-2.3.8)

### Vegetation
- Dalrymple 1984 (cylinder approach)
- Mendez-Losada 2004 (irregular wave + H_rms)
- Jacobsen 2019 (canopy frequency-dependent)
- Benit-Reniers 2022 (DCTA noncollinear, 41.45)
- Sand 1982 (transfer function G(Δθ))

### Sea ice
- Collins-Rogers 2017 (R19 base, IC4M2 WW3)
- Meylan 2014, 2018 (R19 polynomial fit + M18 power law)
- Doble 2015 (D15 empirical)
- Rogers 2018, 2019, 2021a, 2021b (R19/R21B)
- Yu 2019 (Reynolds non-dim)
- Liu 2020 (M18 calibrations)
- Rogers 2016 (nonlinear not scaled)

### Bragg
- Ardhuin-Herbers 2002 (theory + (k/l)_max=5 cutoff)
- Ardhuin 2003 (directional spreading)

### 1st/2nd gen
- Holthuijsen-de Boer 1988 (relaxation framework)
- Holthuijsen 1996 (modifications)
- Cavaleri-Malanotte-Rizzoli 1981 (linear A)
- Snyder 1981 (exponential B)
- Pierson-Moskowitz 1964 (PM spectrum)
- Shore Protection Manual 1973 (depth-dep PM)

### Ambient current
- Longuet-Higgins-Stewart 1960·1961·1962 (theory)
- Yu 1952, Hedges 1985, Lia 1989, Ris 1997

## 10. 한계

- [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) — §2.3.3 소산
- [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) — §2.3.4 비선형 상호작용
- §2.4 current Eq 별도 (Eq 2.16 LHS의 c_g + u 통합 표현)
- §2.5 obstacles deep (Transmission/Reflection/Freeboard/Diffraction) 별도
- §2.6 Wave-induced set-up + §2.7 QCM 별도
- 30+ reference 의 DOI 별도

## 11. 연결

- [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) — §2.3.1-2.3.2 wind input/whitecapping/bottom friction/breaking/triad/quadruplet
- [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) — §2.1-2.2 governing
- [swan-bragg-scattering](../source-analysis/swan-bragg-scattering.md) — §2.3.7 Bragg implementation
- [swan-surfbeat-iem](../source-analysis/swan-surfbeat-iem.md) — User cmd SURFBEAT (별도 module, swantech 미수록)
- [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) — §2.7 QCM (별도)
- [swan-documentation-stack](swan-documentation-stack.md) — 4 PDFs TOC


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md). 표의 결론은 R2의 AI 해석이다. 기존 노트 인용의 줄 번호는 이번 반영 전 HEAD 기준이다. [10-13 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-109 | 식생 감쇠 · swantech PDF 52쪽 / 인쇄 44쪽, (2.109) | swantech PDF 52쪽 / 인쇄 44쪽, (2.109) $\varepsilon_v=\frac{2}{3\pi}\rho C_Db_vN_v(gk/(2\sigma))^3[\sinh^3(k\alpha h)+3\sinh(k\alpha h)]H^3/[3k\cosh^3(kh)]$. | `src/swancom2.ftn:860`의 `SQRT(ETOT)`는 불규칙파의 통계량이다 | H | 규칙파 이론을 불규칙파 식 (2.110)으로 바꾸는 출발식이다. 코드는 개별 파고 $H$에 대한 규칙파 소산을 별도로 계산하지 않는다. |
| R2:SS-112 | 식생 감쇠 · swantech PDF 53쪽 / 인쇄 45쪽, (2.112) | swantech PDF 53쪽 / 인쇄 45쪽, (2.112) $D_{tot}=-\widetilde C_Db_vN_v(g\widetilde k/(2\widetilde\sigma))^3[\sinh^3(\widetilde k\alpha h)+3\sinh(\widetilde k\alpha h)]H_{rms}^3/[2g\sqrt\pi\,3k\cosh^3(\widetilde kh)]$. | `src/swancom2.ftn:859` `C = 3.*KMESPC*(COSH(KD))**3` | B | 분모의 단독 $k$에도 평균 표시가 필요하다. 코드는 분모에 $\widetilde k$를 사용한다. 평균 주파수의 별도 차이는 SS-270이다. |
| R2:SS-113 | 식생 감쇠 · swantech PDF 53쪽 / 인쇄 45쪽, (2.113) | swantech PDF 53쪽 / 인쇄 45쪽, (2.113) $S_{ds,veg}=-\sqrt{2/\pi}g^2\widetilde C_Db_vN_v(\widetilde k/\widetilde\sigma)^3[\sinh^3(\widetilde k\alpha h)+3\sinh(\widetilde k\alpha h)]\sqrt{E_{tot}}E/[3k\cosh^3(\widetilde kh)]$. | `src/swancom2.ftn:859`의 `3.*KMESPC`; `src/swancom2.ftn:860` `SVEG1 = SQRT(2./PI)*GRAV**2 * (KMESPC/SMEBRK)**3 * SQRT(ETOT)/C` | B | (2.112)와 같은 분모의 평균 표시 누락이다. 나머지 계수·제곱근·차수는 같다. |
| R2:SS-115 | 식생 감쇠 · swantech PDF 53쪽 / 인쇄 45쪽, (2.115) | swantech PDF 53쪽 / 인쇄 45쪽, (2.115) $S_{ds,veg,i}=-\sqrt{2/\pi}g^2\widetilde C_{D,i}b_{v,i}N_{v,i}(\widetilde k/\widetilde\sigma)^3\sqrt{E_{tot}}\{[\sinh^3(\widetilde k\alpha_ih)-\sinh^3(\widetilde k\alpha_{i-1}h)]+3[\sinh(\widetilde k\alpha_ih)-\sinh(\widetilde k\alpha_{i-1}h)]\}E/[3k\cosh^3(\widetilde kh)]$. | `src/swancom2.ftn:873` `KVEGH = KVEGH + KMESPC * LAYH(IL)`; `src/swancom2.ftn:879` `A = C - A`; `src/swancom2.ftn:880` `B = D - B`; `src/swancom2.ftn:859` 의 `3.*KMESPC` | B | 층 경계의 쌍곡함수 차이는 일치한다. 분모의 $k$에는 평균 표시가 빠졌다. |
| R2:SS-116 | 식생 감쇠 · swantech PDF 54쪽 / 인쇄 46쪽, (2.116) | swantech PDF 54쪽 / 인쇄 46쪽, (2.116) $\sum_{i=1}^{I}\alpha_i\le1$. | `src/swancom2.ftn:897` `SLAYH1 = SLAYH1 + LAYH(IL)`; `src/swancom2.ftn:902` `LAYPRT = DEP2(KCGRD(1)) - SLAYH2`; 914의 누적 경계 | B | (2.115)와 그림 2.3의 $\alpha_i h$는 바닥부터 잰 누적 경계 높이이다. 올바른 제한은 $0=\alpha_0\le\alpha_1\le\cdots\le\alpha_I\le1$ 또는 $\sum_i(\alpha_i-\alpha_{i-1})\le1$이다. 인쇄식은 층 두께 비율과 누적 높이 비율을 혼동한다. |
| R2:SS-270 | 식생 감쇠 · swantech PDF 53쪽 / 인쇄 45쪽, 원문 `the mean frequency ... and the mean wave number ... are given by Eqs. (2.46) and (2.47), respectively`. | swantech PDF 53쪽 / 인쇄 45쪽, 원문 `the mean frequency ... and the mean wave number ... are given by Eqs. (2.46) and (2.47), respectively`. | `src/swancom1.ftn:6024` `SMEBRK = SIGM01`; `src/swancom1.ftn:7365` 의 `CALL SVEG (DEP2   ,IMATDA   ,ETOT   ,SMEBRK    ,`; `src/swancom2.ftn:860`의 `(KMESPC/SMEBRK)**3` | C | 구현은 $m_1/m_0$ 평균 주파수를 사용한다. 문서가 지목한 (2.46)은 $m_0/m_{-1}$이다. 파수 평균은 (2.47)과 같다. |
| R2:SS-274 | 식생 감쇠 · swantech PDF 54쪽 / 인쇄 46쪽, 무번호 | swantech PDF 54쪽 / 인쇄 46쪽, 무번호 $m_{u,0}=\int_0^\infty S_u\,df$. | `src/swancom2.ftn:979` `MU = MU + FDD(IS) * SPCSIG(IS)**2 * AC2(ID,IS,KCGRD(1))`; `src/swancom2.ftn:986` `MU = MU * DDIR * FRINTF` | B | 바로 앞에서 $S_\eta=E(\sigma)$로 정의했으므로 적분 측도는 $d\sigma$여야 한다. 코드는 $N\sigma^2d\log\sigma=E(\sigma)d\sigma$를 적분한다. $df$를 쓰려면 $S_u(f)=2\pi S_u(\sigma)$로 바꿔야 한다. |
| R2:SS-287 | 얼음 감쇠와 Bragg 산란 · swantech PDF 55–56쪽 / 인쇄 47–48쪽, R19의 다른 보정값 | swantech PDF 55–56쪽 / 인쇄 47–48쪽, R19의 다른 보정값 $(c_2,c_4)=(.208\,10^{-3},5.18\,10^{-2})$, $(.284\,10^{-3},1.53\,10^{-2})$; M18의 다른 $C_{hf,M}=.00751,.0351$; 적용 지역·얼음 종류. | `src/swanpre1.ftn:2645`·2647·2655의 사용자 계수 입력 | H | 문헌 사례의 보정값이다. 코드의 고정 기본값이라고 서술하지 않는다. |
| R2:SS-118 | 1·2세대 원천항 · swantech PDF 58쪽 / 인쇄 50쪽, (2.118) | swantech PDF 58쪽 / 인쇄 50쪽, (2.118) $S_{tot}=A+BE$ if $E<E_{lim}$ and $\lvert\theta-\theta_w\rvert<\pi/2$; $(E_{lim}-E)/\tau$ if $E>E_{lim}$ and $\lvert\theta-\theta_w\rvert<\pi/2$; $0$ if $E>E_{lim}$ and $\lvert\theta-\theta_w\rvert>\pi/2$. | `src/swancom3.ftn:437` `IF ( AC2CEN .LE. ALIMW(ID,IS) ) THEN`; `src/swancom3.ftn:438` `GROWW(ID,IS) = .TRUE.`; 488의 비성장 분기; `src/swancom3.ftn:493–494` 의 `COSDIF .LT. 0.`이면 `TAUINV = 0.` | C | 코드는 $E=E_{lim}$을 성장 분기에 포함한다. 문서는 등호인 경우를 적지 않는다. 갱신 후 포화값을 넘지 않게 제한하는 처리는 SS-528이다. |
| R2:SS-119 | 1·2세대 원천항 · swantech PDF 58쪽 / 인쇄 50쪽, (2.119) | swantech PDF 58쪽 / 인쇄 50쪽, (2.119) $A=\frac{\beta_1}{2\pi}\frac{\pi}{g^2}C_{drag}^2(\rho_a/\rho_w)^2(U_{10}\max[0,\cos(\theta-\theta_w)])^4$ for $\sigma\ge.7\sigma_{PM,d}$; 그 아래 $A=0$. 무번호 $\beta_1=188,C_{drag}=.0012$. | `src/swancom3.ftn:457` `FACTA = PWIND(1) * PI * PWIND(9)**2 * PWIND(11)**2 / GRAV**2`; 475의 주파수 조건; `src/swancom3.ftn:476–477` 의 `ADUM` 및 `/SIGTPI`; `src/swanmain.ftn:1459` `PWIND(1) = 188.0`; `src/swanmain.ftn:1468` `PWIND(11) = 0.00123`; `src/swanpre1.ftn:2822`의 `CALL INREAL ('CDRAG',  PWIND(11), 'UNC', 0.)`는 생략 시 초기값을 유지한다 | F | 식의 구조와 선형 성장의 절단 주파수는 같다. 코드 초기 항력계수는 `.00123`이다. swantech와 swanuse의 `.0012`는 유효숫자 두 자리로 반올림하면 대응한다. 이 차이만으로 문서 오기를 단정하지 않는다. 코드 재현에는 `.00123`을 쓴다. 인쇄 계수 `.0012`를 직접 대입한 결과와 수치적으로 같다는 뜻은 아니다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-121 | 1·2세대 원천항 · swantech PDF 59쪽 / 인쇄 51쪽, (2.121) | swantech PDF 59쪽 / 인쇄 51쪽, (2.121) $\widetilde d=gd/U_{10}^2$. | `src/swancom3.ftn:369` `DND = MIN( 50. , GRAV * DEP2(KCGRD(1)) / WIND10**2 )` | C | 코드는 무차원 수심을 50으로 제한한다. |
| R2:SS-126 | 1·2세대 원천항 · swantech PDF 59쪽 / 인쇄 51쪽, (2.126) | swantech PDF 59쪽 / 인쇄 51쪽, (2.126) $S_{tot}=\alpha k^{-3}\exp[-\frac54(\sigma/\sigma_{PM,d})^{-4}](2/\pi)\cos^2(\theta-\theta_w)/(2c_g)$ for $\lvert\theta-\theta_w\rvert<\pi/2$; 그 밖은 0. | `src/swancom3.ftn:416` `TEMP1 = ALPM / ( 2. * KWAVE(IS,1)**3 * CGO(IS,1) )`; `src/swancom3.ftn:419` `ALIM1D = TEMP1 * TEMP2 / SPCSIG(IS)`; `src/swancom3.ftn:432` `DIRDIS = (2./PI) * COSDIF**2`; `src/swancom3.ftn:435` `ALIMW(ID,IS) = ALIM1D * DIRDIS` | B | 좌변은 원천항 $S_{tot}$이 아니라 포화 스펙트럼 $E_{lim}$이다. 코드의 결과도 포화 작용 밀도 `ALIMW`이다. 지수 인자의 절단은 SS-528이다. |
| R2:SS-127 | 1·2세대 원천항 · swantech PDF 59쪽 / 인쇄 51쪽, (2.127) GEN1 | swantech PDF 59쪽 / 인쇄 51쪽, (2.127) GEN1 $\alpha=.0081$. | `src/swancom3.ftn:382` `ALPM = 0.0081`; `src/swancom3.ftn:407` `ALPMD = 0.0081 + ( 0.013 - 0.0081 ) * EXP ( -1. * DND )`; `src/swancom3.ftn:408` `ALPM = MIN ( 0.155 , MAX ( ALPMD , ALPM ) )` | C | 코드는 GEN1에도 천해 증가량을 적용한다. 382행의 `.0081`이 최종값은 아니다. |
| R2:SS-129 | 1·2세대 원천항 · swantech PDF 60쪽 / 인쇄 52쪽, (2.129) | swantech PDF 60쪽 / 인쇄 52쪽, (2.129) $\widetilde E_{tot,sea}=g^2E_{tot,sea}/U_{10}^4$. | `src/swancom3.ftn:396` `EDML = MIN ( PWIND(10) , (GRAV**2 * ETOTW) / WIND10**4 )`; `src/swancom3.ftn:397` `EDML = MAX ( 1.E-25 , EDML )`; `src/swanmain.ftn:1467` `PWIND(10) = 0.0036` | C | GEN2의 기본 설정에서 무차원 에너지는 $[10^{-25},.0036]$으로 제한한다. 상한의 존재와 기본값은 사용자 매뉴얼에 있다. C는 swantech (2.129)에 상·하한 처리가 없는 점으로 좁힌다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 전수 검증 정정] |
| R2:SS-522 | 식생의 깊은 물 절단·부분층·Jacobsen 적분 상수 | swantech PDF 53–55쪽 / 인쇄 45–47쪽은 잠긴 식생·층별 소산·Simpson 적분을 설명한다. swanuse PDF 77쪽 / 인쇄 69쪽는 층별 높이 입력과 Jacobsen의 층화 미구현을 명시한다. | `src/swancom2.ftn:858`의 `KD.GT.10.`; `src/swancom2.ftn:762` `NIP  = 20`; `src/swancom2.ftn:763` `ALFU = 1.`; `src/swancom2.ftn:970` 의 `EKZ = EXP(KZ)`; `src/swancom2.ftn:902` `LAYPRT = DEP2(KCGRD(1)) - SLAYH2` | C | Suzuki 경로는 평균 $kd>10$에서 종료한다. Jacobsen 경로는 $\alpha_u=1$과 20개 높이 구간을 사용한다. 개별 $kd\ge20$에서는 쌍곡함수 비를 지수함수로 계산한다. 층이 수면을 넘으면 잠긴 부분만 포함한다. C는 swantech 식생 절에 `KD.GT.10.`·개별 $kd\ge20$의 처리, `NIP=20`, `ALFU=1`이 없는 점이다. 잠긴 부분만 포함한다는 물리 조건과 Simpson 적분 자체는 문서에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-526 | GEN1/2의 얼음 배율은 성장과 완화 모두에 적용 | swantech PDF 58쪽 / 인쇄 50쪽, (2.118) $S_{tot}=A+BE$ if $E<E_{lim}$ and $\lvert\theta-\theta_w\rvert<\pi/2$; $(E_{lim}-E)/\tau$ if $E>E_{lim}$ and $\lvert\theta-\theta_w\rvert<\pi/2$; $0$ if $E>E_{lim}$ and $\lvert\theta-\theta_w\rvert>\pi/2$. | `src/swancom3.ftn:505`–507의 `SWIND_EXP`·`SWIND_IMP`에 대한 `FACTOR_ON_SIN` 곱 | C | 2.3.6은 바람 입력의 감소를 설명한다. GEN1/2에서는 $E>E_{lim}$인 완화 소산도 같은 인자로 줄어든다. 완화의 양의 우변과 대각을 함께 줄이므로 포화 목표값은 유지한다. |
| R2:SS-723 | 노트 · manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:64 | `manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:64`·72의 `3k \cosh^3`. | `src/swancom2.ftn:859` `C = 3.*KMESPC*(COSH(KD))**3` | B | 인쇄식의 분모에는 평균 표시가 빠졌다. 구현식의 분모는 $3\widetilde k\cosh^3(\widetilde kh)$이다. 평균 주파수는 문서의 $m_0/m_{-1}$과 코드의 $m_1/m_0$를 별도로 적는다. |
| R2:SS-724 | 노트 · manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:74 | `manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:74` `$\sum_{i=1}^{I} \alpha_i \le 1$`. | `src/swancom2.ftn:873` `KVEGH = KVEGH + KMESPC * LAYH(IL)` | B | $\alpha_i$를 누적 층 경계로 정의하면 올바른 조건은 $0=\alpha_0\le\cdots\le\alpha_I\le1$이다. 층 두께 비율의 합과 구별한다. |
| R2:SS-725 | 노트 · manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:217 | `manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:217` `\frac{\beta_1}{2\pi g^2}`. | `src/swancom3.ftn:457`의 `PWIND(1) * PI` | B | 노트는 분자의 $\pi$를 빠뜨렸다. 계수를 $\beta_1/(2g^2)$로 정정한다. 코드 기본 항력계수 .00123과 문서의 .0012도 구별한다. |
| R2:SS-726 | 노트 · manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:255 | `manual-notes/swan-tech-ch2-vegetation-ice-bragg-gen12.md:255` `S_{\text{tot}}`; 262 `1st-generation (Eq 2.127)**: constant`. | `src/swancom3.ftn:435` `ALIMW(ID,IS) = ALIM1D * DIRDIS`; 408의 천해 하한 | C | 문서 인용 옆에 포화 스펙트럼의 좌변 정정 $E_{lim}$을 적는다. GEN1에도 천해 $\alpha$ 보정이 적용된다고 적는다. GEN2 무차원 에너지의 코드 제한도 적는다. |
