---
title: "SWAN Scientific/Technical Ch 2 Governing equations — §2.1-2.2 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Scientific/Technical Documentation, Cycle III 41.51, Delft 1993-2026) Ch 2 Governing equations, §2.1 Spectral description (p.7-10) + §2.2 Propagation of wave energy (p.10-12). Primary refs: Whitham 1974, Mei 1983, Komen et al. 1994, Holthuijsen 2007, Zijlema 2021."
citation_status: verified
verification_method: "raw PDF `models/SWAN/raw/manuals/pdfs/swantech.pdf` 직접 read (p.7-12 = PDF page 15-19). Eq 2.1-2.17 LaTeX verbatim 인용. Figure 2.1 Holthuijsen 2007 reproduction 명시."
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — Eq 2.1-2.17 verbatim + Whitham/Mei/Komen/Holthuijsen citations"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
  - models/SWAN/source-analysis/swan-propagation-implementation.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
---

# SWAN swantech Ch 2 Governing equations — §2.1-2.2 verified verbatim

> **swantech.pdf p.7-12** (Ch 2 Governing equations §2.1 Spectral description of wind waves + §2.2 Propagation of wave energy) verbatim 직접 인용. SWAN 의 모든 verified 식의 **1차 출처**. 본 위키 기존 [[swan-action-balance]] 와 보완.

## 1. §2.1 Spectral description of wind waves (p.7-10)

### 1.1 Random-phase model (Eq 2.1)

> "Wind generated waves have irregular wave heights and periods, caused by the irregular nature of wind."

Random-phase model — sea surface = sum of harmonic waves, statistically independent:

$$\eta(t) = \sum_{i} a_i \cos(\sigma_i t + \alpha_i) \quad \text{(2.1)}$$

- $\eta$ = sea surface elevation
- $a_i$ = random amplitude of $i$-th wave (Rayleigh distributed)
- $\sigma_i$ = relative radian frequency (ambient current 존재 시)
- $\alpha_i$ = random phase (uniform 0 ~ 2π)
- Reference: **Holthuijsen 2007**

### 1.2 Dispersion relation + Doppler shift (Eq 2.2-2.3)

Ambient current 가 vertical uniform 가정 시 absolute radian frequency:

$$\omega = \sigma + \vec{k} \cdot \vec{u} \quad \text{(2.2)}$$

→ Doppler shift. $\vec{k} = (k_x, k_y)$ wave number vector.

Linear dispersion (relative frequency):

$$\sigma = \sqrt{g|\vec{k}| \tanh(|\vec{k}| d)} \quad \text{(2.3)}$$

- $g$ = 중력가속도
- $d$ = water depth

### 1.3 Variance density spectrum (Eq 2.4-2.6)

Auto-covariance Fourier 변환으로 정의:

$$E'(f) = \int_{-\infty}^{+\infty} C(\tau) e^{-2\pi i f \tau} d\tau \quad \text{(2.4)}$$

$$C(\tau) = \langle \eta(t) \eta(t+\tau) \rangle \quad \text{(2.5)}$$

- $f = \sigma/2\pi$ (Hz)
- $\langle \cdot \rangle$ = ensemble average
- $\tau$ = time lag

Stationary wave 조건에서 one-sided spectrum:

$$E(f) = 2E'(f) \text{ for } f \ge 0, \quad E(f) = 0 \text{ for } f < 0 \quad \text{(2.6)}$$

### 1.4 Total variance + energy (Eq 2.7-2.8)

$$\langle \eta^2 \rangle = C(0) = \int_0^{+\infty} E(f) df \quad \text{(2.7)}$$

→ $E(f)$ 가 variance density (m²/Hz).

$$E_{\text{tot}} = \frac{1}{2} \rho_w g \langle \eta^2 \rangle \quad \text{(2.8)}$$

→ 표면적당 wave 전체 energy. "variance" 와 "energy density" 용어를 본 문서에서 **혼용** (단, **Zijlema 2021** 참조 — 정확 구분).

### 1.5 2D directional spectrum (Eq 2.9)

Wave 문제 대부분 frequency-direction 동시 분포 필요:

$$E(f) = \int_0^{2\pi} E(f, \theta) d\theta \quad \text{(2.9)}$$

$E(f, \theta)$ = SWAN 의 표준 directional spectrum. **Figure 2.1**: North Sea local breeze + storm 의 1D vs 2D 비교 (Holthuijsen (2007) 재인쇄, Cambridge UP 허가).

### 1.6 Integral wave parameters (Eq 2.10-2.12)

$n$-th moment:

$$m_n = \int_0^{\infty} f^n E(f) df \quad \text{(2.10)}$$

$m_0 = \langle \eta^2 \rangle$. Significant wave height:

$$H_s = 4\sqrt{m_0} \quad \text{(2.11)}$$

Wave periods (3가지):

$$T_{m01} = \frac{m_0}{m_1}, \quad T_{m02} = \sqrt{\frac{m_0}{m_2}}, \quad T_{m-10} = \frac{m_{-1}}{m_0} \quad \text{(2.12)}$$

### 1.7 SWAN 사용 변수

> "In SWAN, the energy density spectrum $E(\sigma, \theta)$ is generally used. On a larger scale the spectral energy density function $E(\sigma, \theta)$ becomes a function of space and time, that is, $E(\vec{x}, t; \sigma, \theta)$ and wave dynamics should be considered to determine the evolution of the spectrum in space and time."

→ SWAN 의 dependent variable = **$E(\vec{x}, t; \sigma, \theta)$**.

## 2. §2.2 Propagation of wave energy (p.10-12)

### 2.1 §2.2.1 Wave kinematics — Whitham 1974, Mei 1983 (Eq 2.13-2.15)

> "Using the linear wave theory and the conservation of wave crests, the wave propagation velocities in spatial space within Cartesian framework and spectral space can be obtained from the kinematics of a wave train (Whitham, 1974; Mei, 1983)"

Propagation velocity 3개 (geographical 2 + spectral 2 = 4 component):

$$
\begin{aligned}
\frac{d\vec{x}}{dt} &= (c_x, c_y) = \vec{c}_g + \vec{u} = \frac{1}{2}\left(1 + \frac{2|\vec{k}|d}{\sinh(2|\vec{k}|d)}\right) \frac{\sigma \vec{k}}{|\vec{k}|^2} + \vec{u} \\
\frac{d\sigma}{dt} &= c_\sigma = \frac{\partial \sigma}{\partial d}\left(\frac{\partial d}{\partial t} + \vec{u} \cdot \nabla_{\vec{x}} d\right) - c_g \vec{k} \cdot \frac{\partial \vec{u}}{\partial s} \\
\frac{d\theta}{dt} &= c_\theta = -\frac{1}{k}\left(\frac{\partial \sigma}{\partial d} \frac{\partial d}{\partial m} + \vec{k} \cdot \frac{\partial \vec{u}}{\partial m}\right)
\end{aligned} \quad \text{(2.13)}
$$

- $c_x, c_y$ = spatial propagation velocities
- $c_\sigma$ = spectral propagation in $\sigma$ space (depth + current 변화로 인한 frequency shift)
- $c_\theta$ = spectral propagation in $\theta$ space (depth + current induced refraction)
- $\vec{u} = (u_x, u_y)$ = ambient current
- $s$ = wave propagation direction의 공간 좌표
- $m$ = $s$ 의 수직 좌표
- 주의: $c_\theta$ 는 **diffraction 효과 미포함** (§2.5.4 별도 처리)

Wave number magnitude + direction:

$$\vec{k} = (k_x, k_y) = (|\vec{k}|\cos\theta, |\vec{k}|\sin\theta) \quad \text{(2.14)}$$

Total derivative operator:

$$\frac{d}{dt} = \frac{\partial}{\partial t} + (\vec{c}_g + \vec{u}) \cdot \nabla_{\vec{x}} \quad \text{(2.15)}$$

### 2.2 §2.2.2 Spectral action balance equation (Eq 2.16-2.17)

**핵심 정의**:
> "The action density is defined as $N = E/\sigma$ and is **conserved during propagation** along its wave characteristic in the presence of ambient current, whereas energy density $E$ is not (**Whitman, 1974**). Wave action is said to be **adiabatic invariant**."

**핵심 식 (Eq 2.16)** — Mei 1983 + **Komen et al. 1994**:

$$\boxed{\frac{\partial N}{\partial t} + \nabla_{\vec{x}} \cdot \left[(\vec{c}_g + \vec{u}) N\right] + \frac{\partial c_\sigma N}{\partial \sigma} + \frac{\partial c_\theta N}{\partial \theta} = \frac{S_{\text{tot}}}{\sigma}} \quad \text{(2.16)}$$

**LHS 항 해석**:
1. $\partial N/\partial t$ — kinematic part (local change)
2. $\nabla_{\vec{x}} \cdot [(\vec{c}_g + \vec{u})N]$ — **2D geographical propagation** (shoaling 포함, $\vec{c}_g = \partial\sigma/\partial\vec{k}$ from $\sigma^2 = g|\vec{k}|\tanh(|\vec{k}|d)$)
3. $\partial c_\sigma N/\partial \sigma$ — **σ-shifting** (depth + mean current 변화)
4. $\partial c_\theta N/\partial \theta$ — **depth + current induced refraction**

**RHS**: $S_{\text{tot}}$ = non-conservative source/sink — energy density $E(\sigma, \theta)$ 단위 (not action). §2.3 deep.

### 2.3 Deep water no current (Eq 2.17)

$\sigma = \omega$, $N = E/\sigma$ 단순화:

$$\frac{\partial E}{\partial t} + \nabla_{\vec{x}} \cdot (\vec{c}_g E) = S_{\text{tot}} \quad \text{(2.17)}$$

→ **wave packet ray equation** along wave ray. Source/sink 없으면 energy conserved.

## 2b. §2.4 The influence of ambient current on waves (node24, 서술)

> swantech §2.4 직접 read — action balance 채택의 **물리적 정당화**.

Ambient current(tidal·ocean·wind-generated·river·wave-generated)은 wave growth/decay 에 영향 (Yu 1952, Hedges 1985, Lia 1989). **강한 역류**서:
- wave steepness·height **급증**, **wave blocking** (current 가 군속도 접근) + current-induced **whitecapping·reflection**
- **blocking frequency**서 action 이 nonlinear wave-wave interaction 으로 고/저주파로 부분 전이 (Ris 1997)

이론적 기반: **Longuet-Higgins-Stewart (1960, 1961, 1962)**. **핵심**: current 존재 시 **action density 보존, energy density 비보존** (Eq 2.16의 $N=E/\sigma$ 이유) → SWAN 이 energy balance 아닌 **action balance** 채택. (Eq 2.16 §2.2 + [[swan-tech-ch3-refraction-limiter]] §3.8 current refraction.)

## 3. 핵심 references (Ch 2 인용)

- **Whitham 1974** — Linear and Nonlinear Waves (Wiley) — wave kinematics 원전, action density conservation 증명
- **Mei 1983** — The Applied Dynamics of Ocean Surface Waves (World Scientific) — Eq 2.13 + 2.16 derivation
- **Komen et al. 1994** — Dynamics and Modelling of Ocean Waves (Cambridge UP) — WAM 표준 reference, source term framework
- **Holthuijsen 2007** — Waves in Oceanic and Coastal Waters (Cambridge UP) — Eq 2.1 random-phase + Fig 2.1 (수업용 표준 교재)
- **Zijlema 2021** — variance vs energy density 정확 구분 (별도 paper)
- 1차 SWAN paper: [[swan-booij-1999-jgr-foundational]] (Booij·Ris·Holthuijsen 1999 JGR)

## 4. 본 위키 cross-references

### 4.1 [[swan-action-balance]] 와 보완

본 위키 기존 [[swan-action-balance]] = source-analysis level (구현). 본 노트 = theory level (Eq 2.16 verbatim). 두 노트는 상호 보완.

### 4.2 §2.1 의 implementation

- $E(\sigma, \theta) \to N = E/\sigma$ 변환: SWAN 내부 `ac2(MDC, MSC)` array
- $H_s = 4\sqrt{m_0}$ output: User cmd `BLOCK HSIGN`
- $T_{m01}, T_{m02}, T_{m-10}$: User cmd `BLOCK TMM10 TM01 TM02`

### 4.3 §2.2 의 implementation

- Eq 2.13 propagation velocities → `SwanPropvelX/SwanPropvelS` ([[swan-source-coverage-audit]])
- Eq 2.16 action balance → `SwanCompUnstruc` ([[swan-unstructured-time-step]]) + swancom1.ftn
- $c_\theta$ = depth/current refraction → [[swan-propagation-implementation]] + [[swan-gse-correction]] (GSE artifact 억제)
- $c_\sigma$ = σ-shifting → [[swan-propagation-implementation]] §σ space

### 4.4 §2.5.4 diffraction (별도) + §2.7 QCM (Wigner)

Eq 2.13 의 $c_\theta$ 는 diffraction 미포함. 회절 처리:
- 표준 mild-slope diffraction → [[swan-diffraction-obstacles]] (Holthuijsen 2003 후속)
- Wigner-based **quasi-coherent** → [[swan-quasi-coherent]] (Akrish-Smit-Zijlema 41.90)

## 5. 한계

- 본 노트는 **§2.1-2.2 만** verified (p.7-12, 6 페이지). §2.3 sources/sinks (S_in/S_ds/S_nl) + §2.4 current + §2.5 obstacles + §2.6 setup + §2.7 QCM은 별도 chapter notes 예정.
- 식 LaTeX 표기는 PDF verbatim 옮김 — display issue 시 PDF 원본 참조.
- $E(\vec{x}, t; \sigma, \theta)$ vs $N$ vs $E(f, \theta)$ 표기 차이 (frequency vs radian frequency) 별도 표 가치.
- §2.7 quasi-homogeneous 가정 (line p.9) 의 SWAN 적용 한계 별도.
- Komen et al. 1994 / Holthuijsen 2007 인용 페이지 별도.

## 6. 연결

- [[swan-action-balance]] — source-level action balance
- [[swan-documentation-stack]] — 4 PDFs TOC + §2.2.2 매핑
- [[swan-booij-1999-jgr-foundational]] — Booij 1999 JGR 원논문 (§1.4 reference)
- [[swan-propagation-implementation]] — Eq 2.13 implementation
- [[swan-unstructured-time-step]] — Eq 2.16 unstructured implementation
- [[swan-quasi-coherent]] — §2.7 Wigner 확장 (별도 chapter 노트)
- [[swan-diffraction-obstacles]] — §2.5.4 diffraction
- [[swan-gse-correction]] — Eq 2.13 $c_\theta$ refraction 의 GSE artifact 보정
