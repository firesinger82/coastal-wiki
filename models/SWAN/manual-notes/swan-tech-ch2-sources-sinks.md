---
title: "SWAN swantech Ch 2.3 Sources and sinks — §2.3.1 general + §2.3.2 Wind input (S_in) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf Ch 2 §2.3.1 General concepts (p.13-19) + §2.3.2 Input by wind (p.19-21). Primary references: Phillips 1957·1960, Miles 1957, Hasselmann 1960·1962·1963·1973·1974·1985, Cavaleri-Malanotte-Rizzoli 1981, Snyder 1981, Komen 1984·1994, Janssen 1989·1991, Battjes-Janssen 1978, Eldeberky-Battjes 1995, WAMDI 1988, Wu 1982, Zijlema 2012, Van Vledder-Bottema 2003."
citation_status: verified
verification_method: "raw PDF p.13-21 (PDF page 21-29) 직접 read. Eq 2.27-2.37 LaTeX verbatim + 30+ references."
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — Eq 2.27-2.37 + references verbatim"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-wind-formulations-implementation.md
  - models/SWAN/source-analysis/swan-whitecapping.md
  - models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md
---

# swantech Ch 2.3 §2.3.1-2.3.2 verified verbatim

> swantech.pdf p.13-21 직접 read. SWAN의 모든 6 source/sink term의 **표준 식 + 30+ reference**. 본 위키 [[swan-tech-ch2-governing-equations]] §2.2.2 의 RHS S_tot 정의.

## 1. §2.3.1 General concepts — 6 processes (p.14-19)

**S_tot 분해 (Eq 2.27)**:

$$\boxed{S_{\text{tot}} = S_{\text{in}} + S_{\text{nl3}} + S_{\text{nl4}} + S_{\text{ds,w}} + S_{\text{ds,b}} + S_{\text{ds,br}}} \quad \text{(2.27)}$$

| 항 | 의미 |
|---|---|
| $S_{\text{in}}$ | Wind input (wave growth) |
| $S_{\text{nl3}}$ | Triad nonlinear (3-wave, shallow water) |
| $S_{\text{nl4}}$ | Quadruplet nonlinear (4-wave, deep/intermediate) |
| $S_{\text{ds,w}}$ | Whitecapping dissipation |
| $S_{\text{ds,b}}$ | Bottom friction dissipation |
| $S_{\text{ds,br}}$ | Depth-induced wave breaking |

### 1.1 Wind input (p.14)

> "Transfer of wind energy to the waves is described with a **resonance mechanism (Phillips, 1957)** and a **feed-back mechanism (Miles, 1957)**."

2가지 mechanism:
- **Resonance** (Phillips 1957): wind-induced pressure 의 harmonic 이 free surface harmonic 과 phase 일치 → linear in time growth
- **Feedback** (Miles 1957): wave-induced pressure 가 wave growth에 비례하여 over/under-pressure → exponential in time

**Linear + Exponential combination (Eq 2.28)**:

$$S_{\text{in}}(\sigma, \theta) = A + B E(\sigma, \theta) \quad \text{(2.28)}$$

- $A$ = linear term (Cavaleri-Malanotte-Rizzoli 1981 + Tolman 1992a Pierson-Moskowitz filter)
- $B$ = exponential coefficient (2 옵션):
  - **WAM Cycle 3**: Snyder 1981 (rescaled in $U_*$ by Komen 1984)
  - **WAM Cycle 4**: Janssen 1991a (BL + roughness, iterative Mastenbroek 1993)

### 1.2 Whitecapping dissipation S_ds,w (p.15)

> "Whitecapping is primarily controlled by the steepness of the waves. In presently operating third-generation wave models, the whitecapping formulations are based on a **pulse-based model (Hasselmann, 1974)**, as adapted by the **WAMDI group (1988)**:"

**Eq 2.29**:

$$S_{\text{ds,w}}(\sigma, \theta) = -\Gamma \tilde{\sigma} \frac{k}{\tilde{k}} E(\sigma, \theta) \quad \text{(2.29)}$$

- $\Gamma$ = steepness dependent coefficient (Komen 1984 closure)
- $\tilde{\sigma}, \tilde{k}$ = mean frequency + mean wave number
- 2 $\Gamma$ 값: WAM Cycle 3 (Komen 1984) + WAM Cycle 4 (Janssen 1991a 기반)

**Alternative formulations**:
- Rogers 2003 (Komen 1984 calibration)
- Van Vledder-Hurdle 2002 (mean spectral steepness)
- **Van der Westhuysen 2007** (Alves-Banner 2003 기반, wave group hydrodynamics, mean spectral 의존성 제거 — Yan 1987 wind input 와 함께 사용)

### 1.3 Bottom friction S_ds,b (p.16) — JONSWAP

> "For continental shelf seas with sandy bottoms, the dominant mechanism appears to be **bottom friction (Bertotti and Cavaleri, 1994)** which can generally be expressed as"

**Eq 2.30**:

$$S_{\text{ds,b}} = -C_b \frac{\sigma^2}{g^2 \sinh^2 kd} E(\sigma, \theta) \quad \text{(2.30)}$$

- $C_b$ = bottom friction coefficient

SWAN 3 옵션 implementation:
- **JONSWAP** (Hasselmann 1973): empirical constant
- **Collins 1972**: nonlinear drag law (Hasselmann-Collins 1968 단순화)
- **Madsen 1988**: eddy viscosity model

> "The effect of a mean current on the wave energy dissipation due to bottom friction is not taken into account in SWAN" (Tolman 1992b — roughness length 이 mean current 보다 영향 큼)

### 1.4 Depth-induced breaking S_ds,br (p.17) — Battjes-Janssen + spectral

> "In contrast to this, the total dissipation (i.e. integrated over the spectral space) due to this type of wave breaking can be well modelled with the **dissipation of a bore applied to the breaking waves in a random field (Battjes and Janssen, 1978; Thornton and Guza, 1983)**."

**Eldeberky-Battjes 1995** → spectral version (uni-modal spectra shape depth-induced breaking insensitive).

**Eq 2.31**:

$$S_{\text{ds,br}}(\sigma, \theta) = \frac{D_{\text{tot}}}{E_{\text{tot}}} E(\sigma, \theta) \quad \text{(2.31)}$$

- $E_{\text{tot}}$ = total wave energy
- $D_{\text{tot}} < 0$ = total dissipation rate (Battjes-Janssen 1978)
- Breaker parameter: $\gamma = H_{\max}/d$
- Default constant: **γ = 0.73** (Battjes-Stive 1985 mean)
- Variable γ: Nelson 1987 + Ruessink 2003 (both in SWAN)

### 1.5 Nonlinear wave-wave interactions (p.17-19)

> "The basic properties of wave-wave interactions were discovered during the fundamental research of **Phillips (1960) and Hasselmann (1960, 1962, 1963a,b)**."

#### Quadruplet (deep + intermediate water)

> "transfer wave energy from the spectral peak to lower frequencies (peak down-shift) and to higher frequencies (where the energy is dissipated by whitecapping)"

**Exact Boltzmann integral**:
- Algorithm: **WRT (Webb-Tracy-Resio)** developed by Resio 2001
- Reprogrammed: **XNL** by Van Vledder (Van Vledder-Bottema 2003)
- 본 위키 [[swan-xnl4-exact-quadruplet]] (mod_xnl4v5.ftn90)

**DIA (Discrete Interaction Approximation)** — Hasselmann 1985:
- SWAN 표준
- Quite successful for developing wave spectrum (Komen 1994)
- 한계: uni-directional waves (DIA coefficient ≈ 0) + finite-depth (Hasselmann-Hasselmann 1981 JONSWAP scaling)
- **Multiple DIA**: Hashimoto 2002 (up to 6 wave number configurations 으로 정확도 ↑)

#### Triad (shallow water)

> "In very shallow water, triad wave interactions become important for shoaling waves. It transfers energy to higher and lower frequencies, resulting in super and sub harmonics (Eldeberky 1996; Herbers-Burton 1997; Becq-Girard 1999)"

SWAN 의 4 triad 옵션:
1. **LTA (Lumped Triad Approximation)** — Eldeberky 1996, collinear directional uncoupled
2. **SPB (Stochastic Parametric Boussinesq)** — Becq-Girard 1999, all collinear interactions + closure hypothesis Holloway 1980
3. **FTIM (Full Triad Interaction Model)** — alternative to SPB, quasi-Gaussian + Eldeberky 1996 biphase
4. **DCTA (Distributed Collinear Triad Approximation)** — Booij 2009, k^{-4/3} high-frequency tail equilibrium

## 2. §2.3.2 Input by wind (p.19-21)

### 2.1 Wave growth (Eq 2.32-2.37)

$$S_{\text{in}}(\sigma, \theta) = A + B E(\sigma, \theta) \quad \text{(2.32)}$$

### 2.2 Friction velocity from U_10 (WAM Cycle 3)

$$U_*^2 = C_D U_{10}^2 \quad \text{(2.33)}$$

### 2.3 Drag coefficient C_D — 3 옵션

**Wu 1982 (Eq 2.34)** — piecewise:

$$C_D(U_{10}) = \begin{cases} 1.2875 \times 10^{-3}, & U_{10} < 7.5 \text{ m/s} \\ (0.8 + 0.065 U_{10}) \times 10^{-3}, & U_{10} \ge 7.5 \text{ m/s} \end{cases} \quad \text{(2.34)}$$

**Zijlema 2012 (Eq 2.35)** — **since SWAN 41.01** (default 현행):

$$C_D(U_{10}) = (0.55 + 2.97 \tilde{U} - 1.49 \tilde{U}^2) \times 10^{-3}, \quad \tilde{U} = U_{10}/U_{\text{ref}}, \quad U_{\text{ref}} = 31.5 \text{ m/s} \quad \text{(2.35)}$$

→ **High wind (15-30 m/s) C_D 10-30% 감소**, hurricane (>30 m/s) **30% 감소**. Wu 1982 가 high wind 에서 overestimate 한다는 최근 연구 반영.

### 2.4 Linear growth A (Cavaleri-Malanotte-Rizzoli 1981 + Tolman 1992a filter)

$$A = \frac{1.5 \times 10^{-3}}{2\pi g^2} (U_* \max[0, \cos(\theta - \theta_w)])^4 H \quad \text{(2.36)}$$

with PM filter:

$$H = \exp\left\{-\left(\frac{\sigma}{\sigma_{\text{PM}}^*}\right)^{-4}\right\}, \quad \sigma_{\text{PM}}^* = \frac{0.13 g}{28 U_*} \cdot 2\pi$$

- $\theta_w$ = wind direction
- $\sigma_{\text{PM}}^*$ = fully developed Pierson-Moskowitz 1964 peak frequency (friction velocity 기준)
- **Tolman 1992a 의 10^{-5}** → **10^{-3} 오타** (Tolman personal comm 1995 footnote)

### 2.5 Exponential growth B — 2 옵션

#### Option 1: Komen 1984 (WAM Cycle 3, default)

$$B = \max\left[0, 0.25 \frac{\rho_a}{\rho_w} \left(28 \frac{U_*}{c_{\text{ph}}} \cos(\theta - \theta_w) - 1\right)\right] \sigma \quad \text{(2.37)}$$

- $c_{\text{ph}}$ = phase speed
- $\rho_a/\rho_w$ = air/water density 비

#### Option 2: Janssen 1989·1991a (WAM Cycle 4)

quasi-linear wind-wave theory + BL + roughness length. Iterative Mastenbroek 1993.

## 3. SWAN 옵션 매핑 (User cmd)

| Tech 식 | User cmd | 본 위키 |
|---|---|---|
| Eq 2.28-2.37 S_in | `WIND` + `GEN1/GEN2/GEN3` | [[swan-wind-formulations-implementation]] |
| Eq 2.29 whitecapping | `WCAPPING` (Komen / Janssen / Van der Westhuysen) | [[swan-whitecapping]] |
| Eq 2.30 bottom friction | `FRICTION` (JONSWAP / Collins / Madsen) | (없음) |
| Eq 2.31 breaking | `BREAKING CON 0.73` (default γ Battjes-Stive) | (없음) |
| S_nl4 exact (Eq 별도) | `QUADRUPL XNL` | [[swan-xnl4-exact-quadruplet]] |
| S_nl4 DIA | `QUADRUPL` (default Hasselmann 1985) | [[swan-source-terms-implementation]] |
| S_nl3 triad | `TRIAD LTA/SPB/FTIM/DCTA` | (없음) |
| Multiple DIA | `QUADRUPL MDIA 6` | (없음, Hashimoto 2002) |

## 4. SWAN 41.x 기본값 변경 history

- **41.01** (2014?): C_D Zijlema 2012 (Eq 2.35) **default 채택**
- **41.80** (2021-09): Bragg scattering 추가 ([[swan-bragg-scattering]])
- **41.85** (2019-01): IEM surfbeat ([[swan-surfbeat-iem]])
- **41.90** (2021-06): QCM ([[swan-quasi-coherent]])

## 5. 핵심 references (Ch 2.3 인용 30+)

### Wind input
- Phillips 1957 (resonance), Miles 1957 (feedback)
- Snyder 1981, Komen 1984
- Janssen 1989, 1991a (WAM Cycle 4)
- Cavaleri-Malanotte-Rizzoli 1981 (linear A)
- Tolman 1992a (PM filter)
- Wu 1982 (C_D), Zijlema 2012 (Eq 2.35 default since 41.01)
- Pierson-Moskowitz 1964 (PM peak)
- Mastenbroek 1993 (iterative U_*)
- Yan 1987 (alternative wind input)

### Whitecapping
- Hasselmann 1974 (pulse-based)
- WAMDI 1988
- Komen 1984 (Γ closure)
- Young-Banner 1992, Banner-Young 1994 (cut-off frequency dependency)
- Rogers 2003, Van Vledder-Hurdle 2002 (alternative calibration)
- Alves-Banner 2003 (wave group hydrodynamics)
- Van der Westhuysen 2007 (Alves-Banner 적용)

### Bottom friction
- Hasselmann 1973 (JONSWAP)
- Putnam-Johnson 1949 (pioneering)
- Hasselmann-Collins 1968 → Collins 1972 (drag law)
- Madsen 1988 (eddy viscosity)
- Weber 1989, 1991
- Bertotti-Cavaleri 1994 (dominant mechanism)
- Luo-Monbaliu 1994 (no preference data)
- Tolman 1992b (no current effect)

### Breaking
- Battjes-Janssen 1978 (bore model)
- Thornton-Guza 1983
- Eldeberky-Battjes 1995 (spectral version)
- Battjes-Stive 1985 (γ=0.73 mean)
- Nelson 1987, Ruessink 2003 (variable γ)
- Battjes-Beji 1992, Vincent 1994, Arcilla 1994, Eldeberky-Battjes 1996 (lab obs)

### Nonlinear
- Phillips 1960, Hasselmann 1960·1962·1963a·1963b
- Hasselmann-Hasselmann 1981 (JONSWAP scaling)
- Hasselmann 1985 (DIA)
- Webb-Tracy-Resio (WRT, Resio 2001)
- Van Vledder-Bottema 2003 (XNL)
- Hashimoto 2002 (Multiple DIA 6 config)
- Young-Van Vledder 1993 (review)
- Beji-Battjes 1993, Arcilla 1994 (triad lab)
- Abreu 1992 (early triad attempt)
- Madsen-Sørensen 1993 (Boussinesq base)
- Eldeberky 1996 (LTA)
- Becq-Girard 1999 (SPB), Holloway 1980 (closure)
- Booij 2009 (DCTA)
- Komen et al. 1994 (book reference)

## 6. 한계

- §2.3 의 §2.3.3 Dissipation (deep treatment, Eq 2.38+) + §2.3.4 Nonlinear (DIA Eq 정확 식) 미커버 — 다음 chapter notes 예정
- §2.3.5 Vegetation + §2.3.6 Sea ice + §2.3.7 Bragg + §2.3.8 1st/2nd-gen — 다음
- Janssen 1991a quasi-linear theory 의 정확 식 미인용 (Eq 2.32 의 B option 2 = Janssen Cycle 4 식 별도)
- Van der Westhuysen 2007 alternative whitecapping 식 미인용
- 30+ reference 의 DOI/페이지 별도 cross-check 필요

## 7. 연결

- [[swan-tech-ch2-governing-equations]] — §2.1-2.2 (Eq 2.16 의 RHS S_tot 의 정의)
- [[swan-documentation-stack]] — 4 PDFs TOC
- [[swan-wind-formulations-implementation]] — Eq 2.32-2.37 implementation
- [[swan-whitecapping]] — Eq 2.29 implementation
- [[swan-xnl4-exact-quadruplet]] — exact S_nl4 via Van Vledder XNL
- [[swan-source-terms-implementation]] — DIA implementation
- [[swan-st6-babanin-implementation]] — ST6 (Yan 1987 + Van der Westhuysen 2007) physics package
- [[swan-bragg-scattering]] — Bragg (§2.3.7)
- [[swan-quasi-coherent]] — QCM (§2.7, scattering 별도)
