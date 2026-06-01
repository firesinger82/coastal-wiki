---
title: "SWAN swantech Ch 2.3.5-2.3.8 — Vegetation/Sea ice/Bragg/Gen1·2 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf Ch 2 §2.3.5 Vegetation (p.44-47) + §2.3.6 Sea ice (p.47-49) + §2.3.7 Bragg scattering (p.48-50) + §2.3.8 First/Second-gen (p.50-52). Primary refs: Dalrymple 1984, Mendez-Losada 2004, Jacobsen 2019, Benit-Reniers 2022, Sand 1982, Collins-Rogers 2017, Meylan 2014·2018, Doble 2015, Rogers 2019·2021a·2021b, Yu 2019, Liu 2020, Ardhuin-Herbers 2002, Ardhuin 2003, Holthuijsen-de Boer 1988, Pierson-Moskowitz 1964, Shore Protection Manual 1973, Cavaleri-Malanotte-Rizzoli 1981, Snyder 1981."
citation_status: verified
verification_method: "raw PDF p.44-52 (PDF page 52-60) 직접 read. Eq 2.108-2.130 LaTeX verbatim."
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — Eq 2.108-2.130 verbatim + 4 sea ice methods + Bragg theory"
verification_date: 2026-06-01
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

$$S_{\text{ds,veg}} = -\sqrt{\frac{2}{\pi}} g^2 \tilde{C}_D b_v N_v \left(\frac{\tilde{k}}{\tilde{\sigma}}\right)^3 \frac{\sinh^3 \tilde{k}\alpha h + 3 \sinh \tilde{k}\alpha h}{3k \cosh^3 \tilde{k}h} \sqrt{E_{\text{tot}}} E(\sigma, \theta) \quad \text{(2.113)}$$

### 1.4 다층 vegetation (Eq 2.114-2.116)

$$S_{\text{ds,veg}} = \sum_{i=1}^{I} S_{\text{ds,veg},i} \quad \text{(2.114)}$$

각 layer $i$ 의 식:

$$S_{\text{ds,veg},i} = -\sqrt{\frac{2}{\pi}} g^2 \tilde{C}_{D,i} b_{v,i} N_{v,i} \left(\frac{\tilde{k}}{\tilde{\sigma}}\right)^3 \sqrt{E_{\text{tot}}} \frac{(\sinh^3 \tilde{k}\alpha_i h - \sinh^3 \tilde{k}\alpha_{i-1}h) + 3(\sinh \tilde{k}\alpha_i h - \sinh \tilde{k}\alpha_{i-1}h)}{3k \cosh^3 \tilde{k}h} E(\sigma, \theta) \quad \text{(2.115)}$$

조건: $\sum_{i=1}^{I} \alpha_i \le 1$ (emergent/submergent layers, Eq 2.116)

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
- $A, BE$ = linear/exponential wind growth ([[swan-tech-ch2-sources-sinks]] §2 Eq 2.32)
- Modified for shallow water (Booij-Holthuijsen personal comm 1996)

### 4.2 Linear growth A (Eq 2.119-2.122)

Cavaleri-Malanotte-Rizzoli 1981 + Holthuijsen-de Boer 1988 + Holthuijsen 1996 adaptation:

$$A = \begin{cases}
\frac{\beta_1}{2\pi g^2} C_{\text{drag}}^2 \left(\frac{\rho_a}{\rho_w}\right)^2 (U_{10} \max[0, \cos(\theta - \theta_w)])^4, & \sigma \ge 0.7 \sigma_{\text{PM,d}} \\
0, & \sigma < 0.7 \sigma_{\text{PM,d}}
\end{cases} \quad \text{(2.119)}$$

- $\beta_1 = 188$
- $C_{\text{drag}} = 0.0012$
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

$$S_{\text{tot}} = \begin{cases}
\frac{\alpha k^{-3}}{2 c_g} \exp\left\{-\frac{5}{4}\left(\frac{\sigma}{\sigma_{\text{PM,d}}}\right)^{-4}\right\} \frac{2}{\pi} \cos^2(\theta - \theta_w), & |\theta - \theta_w| < \pi/2 \\
0, & |\theta - \theta_w| \ge \pi/2
\end{cases} \quad \text{(2.126)}$$

### 4.6 1st-gen vs 2nd-gen — scale factor α

**1st-generation (Eq 2.127)**: constant

$$\alpha = 0.0081$$

**2nd-generation (Eq 2.128-2.130)**: depends on wind sea + dimensionless depth

$$\alpha = \max\left[(0.0081 + (0.013 - 0.0081) e^{-\tilde{d}}), 0.0023 \tilde{E}_{\text{tot,sea}}^{-0.223}\right] \quad \text{(2.128)}$$

$$\tilde{E}_{\text{tot,sea}} = \frac{g^2 E_{\text{tot,sea}}}{U_{10}^4} \quad \text{(2.129)}$$

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
| 41.80 | 2021-09 | **Bragg scattering** ([[swan-bragg-scattering]]) |
| 41.85 | 2019-01 | **IEM surfbeat** ([[swan-surfbeat-iem]]) |
| 41.90 | 2021-06 | **QCM** ([[swan-quasi-coherent]]) |
| 41.91 | 2022-02 | QC surf breaking |
| 41.95 | 2022-07 | VTK output ([[swan-vtk-output]]) |

## 8. User cmd 매핑

| Tech 식 | User cmd | 본 위키 |
|---|---|---|
| Eq 2.109-2.116 vegetation | `VEGETATION` (p.68) | (없음 신설 후보) |
| Eq 2.117 Bragg | `BRAGG` (p.71) | [[swan-bragg-scattering]] |
| Sea ice 4 methods | `SICE` (p.70) | (없음 신설 후보) |
| 1st/2nd gen | `GEN1` (p.57) / `GEN2` (p.58) | (없음) |
| 3rd gen | `GEN3` (p.58) — default | [[swan-tech-ch2-sources-sinks]] |

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

- §2.3.3 dissipation (Komen 1984 deep) + §2.3.4 Nonlinear (DIA 정확 식) 미커버 — 다음
- §2.4 current Eq 별도 (Eq 2.16 LHS의 c_g + u 통합 표현)
- §2.5 obstacles deep (Transmission/Reflection/Freeboard/Diffraction) 별도
- §2.6 Wave-induced set-up + §2.7 QCM 별도
- 30+ reference 의 DOI 별도

## 11. 연결

- [[swan-tech-ch2-sources-sinks]] — §2.3.1-2.3.2 wind input/whitecapping/bottom friction/breaking/triad/quadruplet
- [[swan-tech-ch2-governing-equations]] — §2.1-2.2 governing
- [[swan-bragg-scattering]] — §2.3.7 Bragg implementation
- [[swan-surfbeat-iem]] — User cmd SURFBEAT (별도 module, swantech 미수록)
- [[swan-quasi-coherent]] — §2.7 QCM (별도)
- [[swan-documentation-stack]] — 4 PDFs TOC
