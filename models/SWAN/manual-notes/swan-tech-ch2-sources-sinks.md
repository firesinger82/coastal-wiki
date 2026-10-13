---
title: "SWAN swantech Ch 2.3 Sources and sinks — §2.3.1 general + §2.3.2 Wind input (S_in) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf Ch 2 §2.3.1 General concepts (p.13-19) + §2.3.2 Input by wind (p.19-21). Primary references: Phillips 1957·1960, Miles 1957, Hasselmann 1960·1962·1963·1973·1974·1985, Cavaleri-Malanotte-Rizzoli 1981, Snyder 1981, Komen 1984·1994, Janssen 1989·1991, Battjes-Janssen 1978, Eldeberky-Battjes 1995, WAMDI 1988, Wu 1982, Zijlema 2012, Van Vledder-Bottema 2003."
citation_status: verified
verification_method: "raw PDF p.13-21 (PDF page 21-29) 직접 read. Eq 2.27-2.37 LaTeX verbatim + 30+ references. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — Eq 2.27-2.37 + references verbatim"
verification_date: 2026-06-01
last_source_check: 2026-10-13 (recovery 대조 반영)
related:
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-wind-formulations-implementation.md
  - models/SWAN/source-analysis/swan-whitecapping.md
  - models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md
---

# swantech Ch 2.3 §2.3.1-2.3.2 verified verbatim

> swantech PDF 21–29쪽 / 인쇄 13–21쪽의 원천항 개요와 바람 입력을 정리한다. 식 (2.27)은 천해의 기본 과정 6개를 분해한다. 식생·해빙·불규칙 해저 산란은 같은 문서의 별도 절에서 설명한다. [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md)은 작용 평형식의 우변을 정리한다. [10-13 전수 검증 정정]

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
- 본 위키 [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md) (mod_xnl4v5.ftn90)

**DIA (Discrete Interaction Approximation)** — Hasselmann 1985:
- SWAN 표준
- Quite successful for developing wave spectrum (Komen 1994)
- 단일 방향 파랑에서 거의 0이라는 설명은 실제 4파 상호작용 계수에 관한 것이다. 이를 DIA의 고정 계수 $C_{nl4}$가 0이라는 뜻으로 옮기지 않는다. (swantech PDF 26쪽 / 인쇄 18쪽)
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

**Zijlema 2012 (Eq 2.35)** — FIT 선택 경로. 이 코드의 기본 항력은 Wu이다. (`src/swanmain.ftn:1109` `IDRAG  = 1`; swanuse PDF 66쪽 / 인쇄 58쪽, PDF 69쪽 / 인쇄 61쪽)

$$C_D(U_{10}) = (0.55 + 2.97 \tilde{U} - 1.49 \tilde{U}^2) \times 10^{-3}, \quad \tilde{U} = U_{10}/U_{\text{ref}}, \quad U_{\text{ref}} = 31.5 \text{ m/s} \quad \text{(2.35)}$$

→ **High wind (15-30 m/s) C_D 10-30% 감소**, hurricane (>30 m/s) **30% 감소**. Wu 1982 가 high wind 에서 overestimate 한다는 최근 연구 반영.

### 2.4 Linear growth A (Cavaleri-Malanotte-Rizzoli 1981 + Tolman 1992a filter)

$$A = \frac{1.5 \times 10^{-3}}{2\pi g^2} (U_* \max[0, \cos(\theta - \theta_w)])^4 H \quad \text{(2.36)}$$

with PM filter:

$$H = \exp\left\{-\left(\frac{\sigma}{\sigma_{\text{PM}}^*}\right)^{-4}\right\}, \quad \sigma_{\text{PM}}^* = \frac{0.13 g}{28 U_*} \cdot 2\pi$$

인쇄식은 그대로 인용한다. AGROW 미선택 시 계수는 0이다. (`src/swanmain.ftn:1484` `PWIND(31) = 0.`)
구현 필터는 $g/(28U_*)$를 사용한다. (`src/swancom3.ftn:1749` `FPM =  GRAV / ( 28.0 * UFRIC )`)
(2.36)의 필터 외에 하한과 고주파 감소를 적용한다. (`src/swancom3.ftn:1762` `ARGU = MIN (2., FPM / SIGMA)`; `src/swancom3.ftn:1776–1778`의 `FREQ1 .GT. 1.`·`FREQ1**(-3)`)

- $\theta_w$ = wind direction
- $\sigma_{\text{PM}}^*$ = fully developed Pierson-Moskowitz 1964 peak frequency (friction velocity 기준)
- **Tolman 1992a 의 10^{-5}** → **10^{-3} 오타** (Tolman personal comm 1995 footnote)

### 2.5 Exponential growth B — 2 옵션

#### Option 1: Komen 1984 (WAM Cycle 3)

기본 GEN3 바람·백파 조합은 WESTH이다. Komen과 FIT는 선택 가능한 경로이다. (`src/swanpre1.ftn:453` `INTEGER, SAVE :: LWINDM = 5`; `src/swanmain.ftn:1112` `IWCAP  = 7`; swanuse PDF 69쪽 / 인쇄 61쪽)

$$B = \max\left[0, 0.25 \frac{\rho_a}{\rho_w} \left(28 \frac{U_*}{c_{\text{ph}}} \cos(\theta - \theta_w) - 1\right)\right] \sigma \quad \text{(2.37)}$$

- $c_{\text{ph}}$ = phase speed
- $\rho_a/\rho_w$ = air/water density 비

#### Option 2: Janssen 1989·1991a (WAM Cycle 4)

quasi-linear wind-wave theory + BL + roughness length. Iterative Mastenbroek 1993.

## 3. SWAN 옵션 매핑 (User cmd)

| Tech 식 | User cmd | 본 위키 |
|---|---|---|
| Eq 2.28·2.32–2.37 S_in | `WIND` + `GEN1/GEN2/GEN3` | [swan-wind-formulations-implementation](../source-analysis/swan-wind-formulations-implementation.md) (swantech PDF 22·27–28쪽 / 인쇄 14·19–20쪽) [10-13 전수 검증 정정]
| Eq 2.29 whitecapping | `WCAPPING KOMEN` / `WCAPPING AB`; Janssen 조합은 `GEN3 JANSSEN` | [swan-whitecapping](../source-analysis/swan-whitecapping.md) (swanuse PDF 66·71쪽 / 인쇄 58·63쪽) [10-13 전수 검증 정정]
| Eq 2.30 bottom friction | `FRICTION` (JONSWAP / Collins / Madsen) | (없음) |
| Eq 2.31 breaking | `BREAKING CONSTANT 1.0 0.73` | (없음) |
| S_nl4 exact (Eq 별도) | `QUADRUPL 51` / `QUADRUPL 52` / `QUADRUPL 53` | [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md) |
| S_nl4 DIA | `QUADRUPL` (default Hasselmann 1985) | [swan-source-terms-implementation](../source-analysis/wave/swan-source-terms-implementation.md) |
| S_nl3 triad | `TRIAD LTA/SPB/FTIM/DCTA` | (없음) |
| Multiple DIA | `QUADRUPL 4`와 별도 `MDIA` 명령 | (없음, Hashimoto 2002) |

상수 쇄파 기본값의 명시 예는 `BREAKING CONSTANT 1.0 0.73`이다. 첫 수치는 $\alpha_{BJ}$이다. 둘째 수치는 $\gamma$이다. (`src/swanpre1.ftn:2380` `CALL INREAL ('ALPHA', PSURF(1), 'STA', 1.0)`; `src/swanpre1.ftn:2381` `CALL INREAL ('GAMMA', PSURF(2), 'STA', 0.73)`)
XNL은 `QUADRUPL 51`·`52`·`53`으로 지정한다. Multiple DIA는 `QUADRUPL 4`와 별도 `MDIA` 명령으로 지정한다. (`src/swanpre1.ftn:3294`의 정수 `IQUAD`; `src/swanpre1.ftn:3152` `IF (KEYWIS('MDIA')) THEN`)

## 4. SWAN 41.x 기본값 변경 history

- 41.01의 FIT 항력 기본값은 41.45 공개 커밋 `2980d1a`(2023-02-27)에서 Wu로 바뀌었다. (`2980d1a:src/swanmain.ftn:1096` `IDRAG  = 1`; `src/swanmain.ftn:1109` `IDRAG  = 1`; `website/modifications/modifications.htm:538`)
- 배포판 41.51과 파일 내부 변경 번호 41.80을 구별한다. (`src/swanmain.ftn:965` `VERNUM = 41.51`; [swan-bragg-scattering](../source-analysis/swan-bragg-scattering.md))
- **41.85** (2019-01): IEM surfbeat ([swan-surfbeat-iem](../source-analysis/swan-surfbeat-iem.md))
- **41.90** (2021-06): QCM ([swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md))

## 5. 핵심 references (Ch 2.3 인용 30+)

### Wind input
- Phillips 1957 (resonance), Miles 1957 (feedback)
- Snyder 1981, Komen 1984
- Janssen 1989, 1991a (WAM Cycle 4)
- Cavaleri-Malanotte-Rizzoli 1981 (linear A)
- Tolman 1992a (PM filter)
- Wu 1982 ($C_D$), Zijlema 2012 (Eq 2.35 FIT 선택)
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

## 6. 원천항 상세 연결

- [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) — §2.3.3 소산
- [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) — §2.3.4 4파·3파
- [swan-tech-ch2-vegetation-ice-bragg-gen12](swan-tech-ch2-vegetation-ice-bragg-gen12.md) — §2.3.5–2.3.8 식생·얼음·Bragg·GEN1/2

## 7. 연결

- [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) — §2.1-2.2 (Eq 2.16 의 RHS S_tot 의 정의)
- [swan-documentation-stack](swan-documentation-stack.md) — 4 PDFs TOC
- [swan-wind-formulations-implementation](../source-analysis/swan-wind-formulations-implementation.md) — Eq 2.32-2.37 implementation
- [swan-whitecapping](../source-analysis/swan-whitecapping.md) — Eq 2.29 implementation
- [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md) — exact S_nl4 via Van Vledder XNL
- [swan-source-terms-implementation](../source-analysis/wave/swan-source-terms-implementation.md) — DIA implementation
- [swan-st6-babanin-implementation](../source-analysis/swan-st6-babanin-implementation.md) — ST6 바람 입력은 `SWIND_DBYB`이다. ST6 백파는 `CALC_SDS`이다. Yan 입력과 Van der Westhuysen 백파의 조합은 WESTH이다. (swantech PDF 33쪽 / 인쇄 25쪽; swanuse PDF 69쪽 / 인쇄 61쪽) `src/swancom1.ftn:7489`는 `CALL SWIND_DBYB`이다. `src/swancom2.ftn:2859`는 `CALL CALC_SDS`이다. [10-13 전수 검증 보완]
- [swan-bragg-scattering](../source-analysis/swan-bragg-scattering.md) — Bragg (§2.3.7)
- [swan-quasi-coherent](../source-analysis/swan-quasi-coherent.md) — QCM (§2.7, scattering 별도)


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-036 | 전체 원천항과 바람 입력 · swantech PDF 28쪽 / 인쇄 20쪽, (2.36) | swantech PDF 28쪽 / 인쇄 20쪽, (2.36) $A={1.5\times10^{-3}\over2\pi g^2}(U_*\max[0,\cos(\theta-\theta_w)])^4H$, $H=\exp\{-(\sigma/\sigma_{PM}^*)^{-4}\}$, $\sigma_{PM}^*={0.13g\over28U_*}2\pi$. | `src/swancom3.ftn:1749` `FPM =  GRAV / ( 28.0 * UFRIC )`; `src/swancom3.ftn:1750` `TEMP1 = PWIND(31) / ( GRAV**2 * 2. * PI )`; `src/swancom3.ftn:1763` `FILTER = EXP ( - ARGU**4 )`; `src/swancom3.ftn:1772` `TEMP3  = ( UFRIC *  MAX( 0. , COSDIF))**4`; `src/swancom3.ftn:1773` `SWINEA = MAX( 0. , TEMP2 * TEMP3 * FILTER )` | C | $A$의 계수·방향 의존성은 `AGROW` 설정 시 같다. 구현의 필터 주파수는 문서 값의 $1/(0.13\,2\pi)$배이다. `src/swancom3.ftn:1611`–1613 주석도 (g/(28U_*))를 명시한다. 해석: 코드가 채택한 필터 주파수의 변경을 문서가 적지 않았다. 추가 절단은 SS-502이다. |
| R2:SS-038 | 전체 원천항과 바람 입력 · swantech PDF 29쪽 / 인쇄 21쪽, (2.38) | swantech PDF 29쪽 / 인쇄 21쪽, (2.38) $B=\beta(\rho_a/\rho_w)(U_*/c_{ph})^2\max[0,\cos(\theta-\theta_w)]^2\sigma$. | `src/swancom3.ftn:2326` `ZALP   = 0.011`; `src/swancom3.ftn:2609` `XFAC2  = ( UFRIC / CW1 + ZALP )**2`; `src/swancom3.ftn:2619` `SWINEB = RHOAW * BETA * XFAC2 * COS2 * SIGMA` | C | 코드가 ((U_*/c_{ph}+0.011)^2)를 사용한다. 같은 보정은 파랑 응력 계산의 2388–2389행에도 있다. |
| R2:SS-039 | 전체 원천항과 바람 입력 · swantech PDF 29쪽 / 인쇄 21쪽, (2.39) | swantech PDF 29쪽 / 인쇄 21쪽, (2.39) $\beta=(1.2/\kappa^2)\lambda\ln^4\lambda$, $\lambda\le1$; $\lambda=gz_e e^r/c_{ph}^2$, $r=\kappa c/\lvert U_*\cos(\theta-\theta_w)\rvert$. 본문은 $\lambda>1$이면 $\beta=0$, $\kappa=0.41$로 정한다. | `src/swancom3.ftn:2324` `BETAMX = 1.2`; `src/swancom3.ftn:2325` `F1     = BETAMX / XKAPPA**2`; `src/swancom3.ftn:2611` `IF ( COS1 .GT. 0.01 ) THEN`; `src/swancom3.ftn:2612` `ZARG = XKAPPA / ( (UFRIC / CW1 + ZALP ) * COS1 )`; `src/swancom3.ftn:2614` `IF ( ZLOG .LT. 0. ) BETA = F1 * EXP (ZLOG) * ZLOG**4`; `src/swanmain.ftn:1476` `PWIND(15) = 0.41` | C | 로그 공간의 Miles 함수는 같다. $r$의 분모에는 `ZALP` 보정이 있다. 코드는 `COS1>0.01`에서만 성장률을 계산한다. $\lambda=1$에서 두 표현은 모두 0이다. |
| R2:SS-201 | 전체 원천항과 바람 입력 · swantech PDF 28쪽 / 인쇄 20쪽, 본문 `Since version 41.01, the SWAN model employs the drag formulation as given by Eq. (2.35).` | swantech PDF 28쪽 / 인쇄 20쪽, 본문 `Since version 41.01, the SWAN model employs the drag formulation as given by Eq. (2.35).` | `src/swanmain.ftn:1109` `IDRAG  = 1`; `src/swanpre1.ftn:3048` `CALL INKEYW ('STA','WU')`; `src/swanpre1.ftn:3052` `IDRAG = 2`는 `FIT` 선택 안에 있다 | C | swantech PDF 28쪽 / 인쇄 20쪽은 FIT 식을 사용한다고 적지만 그 문장에는 기본값이라는 한정이 없다. 현재 기본값 Wu는 swanuse PDF 66쪽 / 인쇄 58쪽·swanuse PDF 69쪽 / 인쇄 61쪽과 코드가 일치한다. FIT도 선택 가능한 구현으로 남는다. 따라서 C의 범위는 swantech PDF 28쪽 / 인쇄 20쪽에 현재 선택·기본값 설명이 빠진 점이다. `2980d1a`(2023-02-27)는 `IDRAG`를 2에서 1로 바꿨다. 공개 41.51 `7ee8981`도 1이다. 이 이력만으로 현재 매뉴얼의 해당 문장을 기본값 오기로 단정하지 않는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-701 | 노트 · manual-notes/swan-tech-ch2-sources-sinks.md:151 | `manual-notes/swan-tech-ch2-sources-sinks.md:151` `(default 현행)`; 171 `Komen 1984 (WAM Cycle 3, default)`. | `src/swanmain.ftn:1109` `IDRAG  = 1`; `src/swanpre1.ftn:453` `INTEGER, SAVE :: LWINDM = 5`; `src/swanmain.ftn:1112` `IWCAP  = 7` | B | 이 코드의 기본 항력은 Wu이다. 기본 GEN3 바람·백파 조합은 WESTH이다. Komen과 FIT는 선택 가능한 경로이다. [10-13 결론 검증 보완] |
| R2:SS-702 | 노트 · manual-notes/swan-tech-ch2-sources-sinks.md:159 | `manual-notes/swan-tech-ch2-sources-sinks.md:159`의 $1.5\,10^{-3}$; 163의 $\sigma_{PM}^*=.13g\,2\pi/(28U_*)$. | `src/swanmain.ftn:1484` `PWIND(31) = 0.`; `src/swancom3.ftn:1749` `FPM = GRAV / ( 28.0 * UFRIC )` | C | 인쇄식은 그대로 인용한다. 구현 설명에는 AGROW 미선택 시 계수 0을 적는다. 구현 필터는 $g/(28U_*)$를 사용한다고 적는다. 고주파 절단도 별도로 적는다. |
| R2:SS-703 | 노트 · manual-notes/swan-tech-ch2-sources-sinks.md:274 | `manual-notes/swan-tech-ch2-sources-sinks.md:274` `ST6 (Yan 1987 + Van der Westhuysen 2007) physics package`; `manual-notes/swan-tech-ch2-dissipation-detailed.md:208`의 같은 ST6 연결 설명. | `src/swanpre1.ftn:2985`–2986 `based on work of` / `Donelan, Babanin, Tsagareli and others`; `src/swancom1.ftn:7489` `CALL SWIND_DBYB`; `src/swancom2.ftn:2859` `CALL CALC_SDS` | B | Yan 입력과 Van der Westhuysen 백파의 조합은 WESTH이다. ST6 바람 입력은 `SWIND_DBYB`이다. ST6 백파는 `CALC_SDS`이다. [10-13 결론 검증 보완] [10-13 전수 검증 보완]
| R2:SS-704 | 노트 · manual-notes/swan-tech-ch2-sources-sinks.md:122 | `manual-notes/swan-tech-ch2-sources-sinks.md:122` `uni-directional waves (DIA coefficient ≈ 0)`. | — | B | 단일 방향 파랑에서 거의 0이라는 설명은 실제 4파 상호작용 계수에 관한 것이다. 이를 DIA의 고정 계수 $C_{nl4}$가 0이라는 뜻으로 옮기지 않는다. |
| R2:SS-705 | 노트 · manual-notes/swan-tech-ch2-sources-sinks.md:189 | `manual-notes/swan-tech-ch2-sources-sinks.md:189` `BREAKING CON 0.73`. | `src/swanpre1.ftn:2380` `CALL INREAL ('ALPHA', PSURF(1), 'STA', 1.0)`; `src/swanpre1.ftn:2381` `CALL INREAL ('GAMMA', PSURF(2), 'STA', 0.73)` | B | 상수 쇄파 기본값의 명시 예는 `BREAKING CONSTANT 1.0 0.73`이다. 첫 수치는 $\alpha_{BJ}$이다. 둘째 수치는 $\gamma$이다. [10-13 결론 검증 보완] |
| R7:H-538 | FIT·JONSWAP 기본값 | `website/modifications/modifications.htm:538` `For computing wind drag the second order polynomial fit as described in this article is the default instead of the well-known Wu (1982) parameterization. At the same time the value of the Jonswap bottom friction is set to 0.038 m²/s³. This is default irrespective of swell and wind-sea conditions.` | `src/swanmain.ftn:1109` `IDRAG  = 1                                                          42.00 41.49 41.33`; 이력: `122b595:src/swanmain.ftn:1096` `IDRAG  = 1                                                          42.00 41.49 41.33`; `122b595:src/swanmain.ftn:1383` `PBOT(3)   = 0.038                                                   41.49`; `2980d1a:src/swanmain.ftn:1096` `IDRAG  = 1                                                          42.00 41.49 41.33`; 변경·대조 커밋: `2980d1a 2023-02-27 initial release (v 41.45)`; `git show 2980d1a -- src/swanmain.ftn`의 변경은 `IDRAG  = 2`에서 `IDRAG  = 1`이다. `src/swanmain.ftn:1396` `PBOT(3)   = 0.038` | A 판 차이 | 41.01의 FIT 항력 기본값은 41.45 공개 커밋 `2980d1a`(2023-02-27)에서 Wu로 바뀌었다. JONSWAP 바닥 마찰 기본값 0.038은 현재도 유지된다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
