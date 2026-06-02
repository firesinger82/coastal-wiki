---
title: "SWAN swantech Ch 2.7 Quasi-Coherent (QC) modelling — Wigner distribution + Weyl evolution + QC approximation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.7 Quasi-coherent modelling (§2.7.1 Wigner distribution + §2.7.2 Evolution equation + §2.7.3 QC approximation), doc p.58-68 (Eq 2.146-2.155). References: Wigner 1932, Weyl 1931, Bremmer 1973, McDonald 1988, Cohen 2012, Bastiaans 1979, Smit-Janssen 2013, Smit et al. 2015a·2015b, Akrish et al. 2020."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §2.7 직접 read via pdftotext (식 번호 context-verified: covariance Γ 2.146·Wigner W 2.147·dispersive wave 2.148·dispersion 2.149·Weyl operator 2.150·phase-space evolution 2.151·Moyal product 2.152·Smit-Janssen2013 central result 2.153·QC form 2.154·S_qc 2.155) + website_markdown node31-34.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +42 offset: HTML 2.188-2.230가 PDF 2.146-2.155에 대응; Weyl/BCH/Taylor 중간 유도식은 PDF 무번호)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.146-2.155 + length scales(ε/μ/β/L_c) verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/source-analysis/swan-quasi-coherent.md
  - models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
---

# swantech Ch 2.7 Quasi-Coherent (QC) modelling — verified verbatim

> swantech.pdf (v41.51) §2.7 직접 read. **통계적 inhomogeneous 파동장**(refractive focusing·diffraction·current scattering)의 이론 — **Wigner distribution + Weyl 형식론 진화식 + QC 근사** (Smit-Janssen 2013, Akrish 2020). [[swan-tech-ch3-qc-curvilinear]] §3.9 구현 + [[swan-quasi-coherent]] (SwanQCM) 의 **이론 근거**.
>
> **식 번호 주의**: §2.7도 PDF↔HTML offset (HTML 2.188-2.230 = PDF 2.146-2.155; HTML이 Weyl/BCH/Taylor 유도단계까지 번호). 본 노트 **PDF 번호** 채택, 중간 유도식은 무번호.

## 0. 도입

Action balance(Eq 2.16, [[swan-tech-ch2-governing-equations]])는 **Gaussian + quasi-homogeneous** 가정. **QC 모델**(Smit 2015a/b, Akrish 2020)은 **통계적 inhomogeneous** 파동장의 생성·전파 허용. 핵심 = **Wigner distribution + 진화식**. 개념은 stat/quantum mech/optics 에서 widely 채택 (Wigner 1932, Bremmer 1973, McDonald 1988, Cohen 2012).

## 1. §2.7.1 Wigner distribution (Eq 2.146-2.147)

Variance density spectrum 의 확장 — **non-collinear 파성분 cross-correlation 포함** (homogeneous statistics 이탈).

### 1.1 Homogeneous 복습

Gaussian zero-mean $\eta(\vec{x})$, Fourier $\hat{\eta}(\vec{k})$ (PDF 무번호). Homogeneous(통계적 독립) 시 auto-covariance $R(\vec{\xi}) = \langle\eta(\vec{x})\eta^\star(\vec{x}+\vec{\xi})\rangle$ 의 Fourier = variance density $E(\vec{k})$ (PDF 무번호). 총 variance $\langle\eta\eta^\star\rangle = R(\vec{0}) = \int E(\vec{k})\,d\vec{k}$, $E(\vec{k})\ge0$ → 1차 통계 완전 정의.

### 1.2 Inhomogeneous → Wigner

Medium 변화(depth·current)가 correlation length 대비 빠르면 두 파성분 correlate (refractive focusing·diffraction·current scattering, many wavelength 상관). Cross-correlation 으로 wave interference 기술 → 빠른 wave statistics 변화 (Smit-Janssen 2013).

두 점 $\vec{x}\pm\vec{\xi}/2$ 의 covariance:
$$\Gamma(\vec{x},\vec{\xi}) = \left\langle\eta\Bigl(\vec{x}+\frac{\vec{\xi}}{2}\Bigr)\eta^\star\Bigl(\vec{x}-\frac{\vec{\xi}}{2}\Bigr)\right\rangle \quad \text{(2.146)}$$

phase space $(\vec{x},\vec{k})$ 의 **Wigner distribution**:
$$W(\vec{x},\vec{k}) = \frac{1}{4\pi^2}\int\Gamma(\vec{x},\vec{\xi})\,e^{-\mathrm{i}\vec{k}\cdot\vec{\xi}}\,d\vec{\xi} \quad \text{(2.147)}$$
- $\Gamma(\vec{x},\vec{\xi}) = \Gamma^\star(\vec{x},-\vec{\xi})$ → **$W$ real-valued**. Bastiaans(1979) 형: $\hat{\Gamma}(\vec{k},\vec{u})$ ($\vec{k}$=평균, $\vec{u}=\vec{k}_1-\vec{k}_2$ 차) 통해 spectrum 표현 (PDF 무번호)
- **W 가 완전한 2차 통계(cross-variance 포함) 기술**. 국소 variance $m_0(\vec{x}) = \langle\eta\eta^\star\rangle(\vec{x}) = \int W(\vec{x},\vec{k})\,d\vec{k} \ge 0$ (PDF 무번호)
- **W 는 음수 가능 → quasi-distribution** (marginal 은 존재하나 엄밀한 joint distribution 아님)

## 2. §2.7.2 Evolution equation (Eq 2.148-2.152)

**Weyl symbol calculus** (Weyl 1931, McDonald 1988, Cohen 2012): phase space 의 ordinary function(symbol) ↔ physical space 의 operator(kernel). Fourier 도함수 ↔ $\mathrm{i}\vec{k}$ ($-\mathrm{i}\nabla_{\vec{\xi}}\leftrightarrow\vec{k}$, $\mathrm{i}\nabla_{\vec{k}}\leftrightarrow\vec{\xi}$).

dispersive wave 식 (Bremmer 1973):
$$\frac{\partial\eta}{\partial t} = -\mathrm{i}\Omega(\vec{x},-\mathrm{i}\nabla_{\vec{x}})\,\eta \quad \text{(2.148)}$$
- $\Omega$ = dispersion $\omega(\vec{x},\vec{k})$ 의 linear pseudo-differential operator:
$$\omega(\vec{x},\vec{k}) = \sqrt{g|\vec{k}|\tanh(|\vec{k}|d)} + \vec{k}\cdot\vec{u} \quad \text{(2.149)}$$
(slowly varying medium linear wave)

**Weyl rule**: operator ↔ phase-space function. $\hat{\omega}(\vec{q},\vec{p})$ Fourier (PDF 2.150) + Taylor 전개. $\Gamma$ 의 Weyl symbol = Wigner $W$. $\partial\Gamma/\partial t$ → $\partial W/\partial t$ phase-space 식:
$$\frac{\partial W}{\partial t}(\vec{x},\vec{k}) = -\mathrm{i}\,\omega(\vec{x}+\tfrac{\mathrm{i}}{2}\nabla_{\vec{k}}, \vec{k}-\tfrac{\mathrm{i}}{2}\nabla_{\vec{x}})\,W(\vec{x},\vec{k}) + \text{c.c.} \quad \text{(2.151)}$$
> Fourier 공간 $\hat{\Gamma}(\vec{k},\vec{u})$ 경유 유도도 동일 (Smit-Janssen 2013).

**Moyal product** (Cohen 2012, BCH identity로 Weyl operator 단순화 — 중간 유도식 PDF 무번호):
$$\frac{\partial W}{\partial t}(\vec{x},\vec{k}) = -\mathrm{i}\,\omega\Bigl(\vec{x},\vec{k}; \tfrac{\mathrm{i}}{2}(\overleftarrow{\nabla}_{\vec{k}}\cdot\overrightarrow{\nabla}_{\vec{x}} - \overleftarrow{\nabla}_{\vec{x}}\cdot\overrightarrow{\nabla}_{\vec{k}})\Bigr)\,W + \text{c.c.} \quad \text{(2.152)}$$
- 좌/우향 화살표 = symbol 좌측($\omega$)/우측($W$) 작용. **non-commutative** (Weyl ordering으로 정확 transport 식 회복, WKB ansatz)
- **가장 일반적 phase-space 식** (inhomogeneous 파동장)이나 **infinite series** (exponential 전개) → 수치 불가능 → 근사 필요(§2.7.3)

## 3. §2.7.3 QC approximation (Eq 2.153-2.155)

### 3.1 Length scales

- $L$ = 특성 wavelength, $L_m$ = medium 변화 스케일, $L_s$ = 2차 통계 변화 스케일, $L_c$ = correlation(coherent) 길이
- $\epsilon = L/L_m \ll 1$ (medium 느린 변화, Eq 2.149 가정)
- $\mu = L/L_s \ll 1$ (통계가 $\mathcal{O}(100\text{-}1000)$ wavelength 거리서 약변)
- **$\beta = L_c/L_m$** = 근사의 key. **$L_c = 2\pi/\Delta k$** ($\Delta k$=spectrum 폭 = 입사장 표준편차). Narrow-band → 큰 $L_c$, directional spread → 작은 coherent radius
- 2 case: **(i) $\beta\ll1$** (medium 변화보다 짧게 de-correlate), **(ii) $\beta=\mathcal{O}(1)$** (coherent radius 내 seabed/current 급변)

### 3.2 최저차 (β≪1) → action balance

exponential 전개 truncate ($\mathcal{O}(\beta^2,\mu^2)$ 무시) → **친숙한 action balance** (PDF 무번호, HTML 2.220):
$$\frac{\partial W}{\partial t} + \nabla_{\vec{k}}\omega\cdot\nabla_{\vec{x}}W - \nabla_{\vec{x}}\omega\cdot\nabla_{\vec{k}}W = 0$$
> $\nabla_{\vec{k}}\omega = c_g = \mathcal{O}(1)$. β≪1 한정 (β=O(1)서 무효).

### 3.3 β=O(1) 확장 → QC (Smit-Janssen 2013 central result)

Moyal product 의 convolution 재정식 ($\hat{\omega}(\vec{q},\vec{k})$, μ≪1 유지) → **중심 결과**:
$$\frac{\partial W}{\partial t}(\vec{x},\vec{k}) = -\mathrm{i}\int\hat{\omega}(\vec{q},\vec{k})\,e^{\mathrm{i}\vec{q}\cdot\vec{x}}\Bigl(\cdots - \tfrac{\mathrm{i}}{2}\vec{q}\cdot\overrightarrow{\nabla}_{\vec{x}}\Bigr)W(\vec{x},\vec{k}-\tfrac{\vec{q}}{2})\,d\vec{q} + \text{c.c.} \quad \text{(2.153)}$$
> **$\hat{\omega}$ 와 $W$ 의 convolution. Smit-Janssen(2013) 핵심 결과 (그들 Eq 15; Akrish 2020 Eq 2.19 mean current 포함).** μ≪1 → **(1차) Quasi-Coherent(QC) 근사**.

수치 적합 형으로 recast:
$$\boxed{\frac{\partial W}{\partial t} + \nabla_{\vec{k}}\omega\cdot\nabla_{\vec{x}}W = S_{\text{qc}}} \quad \text{(2.154)}$$
- **$S_{\text{qc}}$ = scattering source** (refraction + Doppler shift + wave interference 의 inhomogeneous 생성·전파)

### 3.4 S_qc 도출

$\hat{\omega}(\vec{q},\vec{k})$ = $\omega(\vec{x}',\vec{k})$ Fourier (PDF 2.225 region), $W(\vec{x},\vec{k}-\vec{q}/2)$ = $\Gamma$ Fourier (PDF 무번호). Triple integral → shifted Dirac delta → **$\omega(\vec{x}',\vec{k})$ 가 $|\vec{x}'|\le|\vec{\xi}|/2$ compact support** → $\Gamma(\vec{\xi})=0$ for $|\vec{\xi}|>L_c$ → **국소 통계는 $\vec{x}$ 주변 반경 $L_c/2$ medium 만 영향**.

$\omega(\vec{x}+\vec{\xi}/2,\vec{k}) = \omega(\vec{x},\vec{k}) + \Delta\omega(\vec{x}+\vec{\xi}/2,\vec{k})$ 분리(Akrish 2020) → $\Delta\omega$ 항만 $S_{\text{qc}}$ 기여. 최종 (PDF 무번호 + 2.155):
$$S_{\text{qc}} = -\mathrm{i}\int\Delta\hat{\omega}(\vec{x},\vec{q},\vec{k})\Bigl(\cdots\Bigr)W(\vec{x},\vec{k}-\tfrac{\vec{q}}{2})\,d\vec{q} + \mathrm{i}\int\Delta\hat{\omega}(\vec{x},\vec{q},\vec{k})\Bigl(\cdots\Bigr)W(\vec{x},\vec{k}+\tfrac{\vec{q}}{2})\,d\vec{q} \quad \text{(2.155)}$$
> $\Delta\hat{\omega}(\vec{x},\vec{q},\vec{k})$ = $\vec{x}$ 주변 변길이 $L_c/2$ 정사각서 계산. **$S_{\text{qc}}$ 는 $\vec{q}$ 적분 (ξ 아님).** 진화식은 (2.154), scattering term 은 (2.155).

## 4. SWAN 연결 + 구현

| Tech (PDF §2.7) | 구현 | 비고 |
|---|---|---|
| 2.147 Wigner W | [[swan-quasi-coherent]] SwanQCM | W = N_0 + W_c 분리 |
| 2.154 QC 진화식 | §3.9 ([[swan-tech-ch3-qc-curvilinear]]) Eq 3.44 | $J^{-1}S_{qc}$ |
| 2.155 S_qc | §3.9 Eq 3.45 convolution (Tukey γ=0.2, Δq=2Δk, L_c=2π/Δk) | $\vec{q}$ 적분 |
| User cmd | `SCAT` (since 41.90) | harbor/breakwater 회절 |

## 5. 한계

- §2.7.2 Weyl/BCH/Taylor 유도식(HTML 2.204-2.216)·§2.7.3 도출(HTML 2.221-2.228): **PDF 무번호** → 본 노트 핵심 milestone(2.146-2.155)만 PDF 번호 전사.
- (2.151)·(2.152)·(2.153)·(2.155)의 연산자/convolution 세부: alt-text truncated("$\cdots$") → 정밀식 swantech.pdf p.60-68 또는 **Smit-Janssen 2013 (JPO 43(8):1741-1758, doi:10.1175/JPO-D-13-046.1; ⚠ JFM 아님) / Akrish 2020 (JFM 891:A2) 원논문** ([[swan-foundational-papers]]).
- **[[swan-tech-ch3-qc-curvilinear]] §3.9 노트의 "Eq 2.225-2.230" 은 HTML 번호** — 본 PDF 기준은 2.150-2.155 (cross-ref 보정 필요).

## 6. 연결

- [[swan-quasi-coherent]] — SwanQCM.ftn90 (Wigner W 구현, 41.90 Akrish-Smit-Zijlema)
- [[swan-tech-ch3-qc-curvilinear]] — §3.9 QC 수치 구현 (Eq 3.44-3.45, 본 이론의 적용)
- [[swan-tech-ch2-governing-equations]] — action balance(Eq 2.16, QC 가 일반화하는 quasi-homogeneous 식)
- [[swan-tech-ch2-obstacles-diffraction-setup]] — §2.5.4 phase-decoupled diffraction (QC 의 비통계 대안)
