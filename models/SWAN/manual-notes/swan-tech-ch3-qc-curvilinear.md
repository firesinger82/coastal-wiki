---
title: "SWAN swantech Ch 3.9 QC approximation impl + 3.10 curvilinear governing + 3.11 force in curvilinear verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.9 Implementation of QC approximation + §3.10 Governing equations in curvilinear co-ordinates + §3.11 Computation of force in curvilinear co-ordinates, doc p.102-108 (Eq 3.44-3.69). References: Smit et al. 2015a·2015b, Smit-Janssen 2016, Akrish et al. 2020."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.9-3.11 직접 read via pdftotext (식 번호 context-verified: W eq 3.44·S_qc convolution 3.45·curvilinear coords 3.46-47·Taylor 3.50-51·partial deriv 3.52-54·propagation 3.55·D coeff 3.56·stability 3.57·action conservation 3.58·radiation stress 3.59-61·n 3.62·force 3.63-64·ξη transform 3.65-69) + website_markdown node55-57.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +43 offset; Tukey window·ΔΣ/Δc_g/Δu·[D] 보조식은 PDF 무번호)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.44-3.69 + Tukey γ=0.2 + Δq=2Δk verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
  - models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md
---

# swantech Ch 3.9 QC impl + 3.10-3.11 curvilinear — verified verbatim

> swantech.pdf (v41.51) §3.9-3.11 직접 read. **QC scattering 의 수치 구현** (Wigner W 의 σθ↔k 변환 + convolution) + **곡선좌표 governing/force** (Taylor 기반 편미분 + radiation stress force). §3.9 는 [[swan-quasi-coherent]] (SwanQCM.ftn90)과 보완.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML +43 offset; QC 보조식·[D]·ΔΣ 등은 PDF 무번호).

## 1. §3.9 QC approximation 구현 (Eq 3.44-3.45)

§2.7 phase-space 식(Eq 2.225-2.230)은 $(\vec{x},\vec{k})$ 공간, SWAN 은 $(\sigma,\theta)$. 전략: **$(\sigma,\theta)$서 Wigner 정의 → $\vec{k}$ 변환 → phase space서 scattering → $(\sigma,\theta)$ 역변환** (Smit 2015a / Akrish 2020 은 $\vec{k}$ 고수).

$$\frac{\partial W}{\partial t} + \nabla_{\vec{x}}\cdot[(\vec{c}_g + \vec{u})W] = J^{-1}S_{\text{qc}} \quad \text{(3.44)}$$
- $W(\vec{x},t;\sigma,\theta)$ = Wigner 분포, $J = |\vec{c}_g|/|\vec{k}|$ = Jacobian. $S_{\text{qc}}$ 평가 전 $W(\vec{x},t;\vec{k}) = J\,W(\vec{x},t;\sigma,\theta)$ 필요
- **W 는 action density 의 cross-correlation 확장** → ambient current 시 보존. Moment 계산엔 $\sigma W$ 적분 ($\iint W\,d\sigma d\theta > 0$이나 **$W$ 는 음수 가능** → §3.2.4 conservative elimination 적용 금지)

이슈: cross-variance 의 dispersion 비순응(같은 $\sigma$ 의 $\vec{k}_1,\vec{k}_2$ 가 $\sigma(|(\vec{k}_1+\vec{k}_2)/2|)\ne\sigma$ 에 기여 → mapping/aliasing error, 작아 수용 Smit 2015b App C). Refraction·Doppler 는 transport 항 아닌 $S_{\text{qc}}$ 에 포함 (stiffness 회피 + Jacobian 매핑오차 회피). **Depth-breaking(Smit 2015b)·triad(Smit-Janssen 2016) QC 는 미포함 (진행 중)**.

좌변은 §3.2-3.3 (구조격자) / §8.3 (비구조) 통상 이산화. **shoaling 해소 위해 최소 2차 정확도 권장 → SORDUP/Stelling-Leendertse** ($W$ 가 전파 중 급속 narrow/broaden).

### 1.1 3 grid + convolution (Eq 3.45)

3 이산 grid: $\vec{k}$ (간섭 해소, user $(\sigma,\theta)$ domain 변환), $\vec{x}'$ (coherent region), $\vec{q}$ (medium wavenumber).
- $\Delta k$ = incident $N(\vec{k})$ 표준편차, **coherent length $L_c = 2\pi/\Delta k$** (Smit 2015a)
- $D_{\vec{x}'}$ = 변길이 $\frac{1}{2}L_c$ 정사각, $(M+1)^2$ 점
- $q_{\max} = \pi/\Delta x'$, user 또는 $q_{\max} = \alpha|\vec{k}_p|$ ($\alpha$=0.5/1/2)
- $\Delta q = 2\Delta k$ (보간오차 회피) → $N = q_{\max}/\Delta k$, $M = N$ (1:1 매핑, 무보간)

$$S_{\text{qc}}(x,y,k_x,k_y) = -\mathrm{i}\sum_{q_x}\sum_{q_y}\left[\Delta\hat{\sigma} + \vec{k}\cdot\Delta\hat{\vec{u}} - \frac{\mathrm{i}}{2}(\Delta\hat{c_g}\cdots)\nabla_{\vec{x}}\right]W(x,y,k_x-\tfrac{q_x}{2},k_y-\tfrac{q_y}{2}) + \text{c.c.} \quad \text{(3.45)}$$
- $\Delta\hat{\sigma}, \Delta\hat{c_g}, \Delta\hat{\vec{u}}$ = DFT (window $\mathcal{W}$ taper 후 차분, PDF 무번호)
- **Tukey window** $\mathcal{W}(z)$ (PDF 무번호): $\ell = L_c/2$, taper $\gamma$ **hardcoded $\gamma=0.2$**
- $\nabla_{\vec{x}}W$ = 구조격자 2차 중심차분 / 비구조 Green-Gauss (Eq 8.35)

## 2. §3.10 Curvilinear governing (Eq 3.46-3.58)

곡선격자 좌표 $x_{i,j}$ **(3.46)**, $y_{i,j}$ **(3.47)** ($i=1..M, j=1..N$). Four-sweep 불변 (first sweep: $(i-1,j),(i,j-1)$ → $(i,j)$), 2D Taylor 전개로 근사.

이웃 격자 차 (3.48-3.49):
$$\Delta x_1 = x_{i,j}-x_{i-1,j},\ \Delta y_1 = y_{i,j}-y_{i-1,j},\ \Delta F_1 = F_{i,j}-F_{i-1,j} \quad \text{(3.48)}$$
$$\Delta x_2 = x_{i,j}-x_{i,j-1},\ \Delta y_2 = y_{i,j}-y_{i,j-1},\ \Delta F_2 = F_{i,j}-F_{i,j-1} \quad \text{(3.49)}$$

2D Taylor: $\Delta F_1 = \frac{\partial F}{\partial x}\Delta x_1 + \frac{\partial F}{\partial y}\Delta y_1$ **(3.50)**, $\Delta F_2 = \cdots$ **(3.51)** → 편미분:
$$\frac{\partial F}{\partial x} \approx \frac{\Delta y_2\Delta F_1 - \Delta y_1\Delta F_2}{[D]} \quad \text{(3.52)},\qquad \frac{\partial F}{\partial y} \approx \frac{\Delta x_1\Delta F_2 - \Delta x_2\Delta F_1}{[D]} \quad \text{(3.53)}$$
$$[D] = \Delta y_2\Delta x_1 - \Delta y_1\Delta x_2 \quad \text{(3.54)}$$

완전 propagation 항 (시간미분 포함, σθ 임시 무시):
$$\left(\frac{1}{\Delta t} + (D_{x,1}+D_{x,2})c_{x,i,j}^+ + (D_{y,1}+D_{y,2})c_{y,i,j}^+\right)N_{i,j}^+ - \frac{N_{i,j}^-}{\Delta t} - D_{x,1}(c_x N)_{i-1,j}^+ - \cdots = S_{i,j}^+ \quad \text{(3.55)}$$
$$D_{x,1} = \frac{\Delta y_2}{[D]},\ D_{y,1} = -\frac{\Delta x_2}{[D]},\ D_{x,2} = -\frac{\Delta y_1}{[D]},\ D_{y,2} = \frac{\Delta x_1}{[D]} \quad \text{(3.56)}$$
> $+$ = 신 time level $t$, $-$ = 구 $t-\Delta t$. Stationary: $1/\Delta t \to 0$.

**Sweep 판정 안정조건** (전파방향이 $(i-1,j),(i,j-1)$ 연결선 사이):
$$D_{x,1}c_x + D_{y,1}c_y \ge 0 \quad\text{and}\quad D_{x,2}c_x + D_{y,2}c_y \ge 0 \quad \text{(3.57)}$$
> 이 기준으로 SWAN 이 spectral direction 의 sweep 소속 판정. 2nd sweep: $\Delta x_1 = x_{i,j}-x_{i,j-1}$, $\Delta x_2 = x_{i,j}-x_{i+1,j}$ 등 (3·4 sweep 유사, 식 불변).

**Action 보존** (삼각형 $(i,j),(i-1,j),(i,j-1)$, stationary·source=0 시 3 flux 균형):
$$[c_x N]_{i,j}^+(\Delta y_2-\Delta y_1) + \cdots + [c_y N]_{i,j}^+(\Delta x_1-\Delta x_2) + \cdots = 0 \quad \text{(3.58)}$$

## 3. §3.11 Force in curvilinear (Eq 3.59-3.69)

FORCE = wave-driven stress (N/m², radiation stress 미분). Radiation stress tensor:
$$S_{xx} = \rho g\int\left[n\cos^2\theta + n - \tfrac{1}{2}\right]E\,d\sigma d\theta \quad \text{(3.59)}$$
$$S_{xy} = S_{yx} = \rho g\int n\sin\theta\cos\theta\,E\,d\sigma d\theta \quad \text{(3.60)}$$
$$S_{yy} = \rho g\int\left[n\sin^2\theta + n - \tfrac{1}{2}\right]E\,d\sigma d\theta \quad \text{(3.61)}$$
$$n = \frac{c_g k}{\omega} \quad \text{(3.62)}$$
> $n$ = 군속도/위상속도 비. ([[swan-tech-ch2-obstacles-diffraction-setup]] §5 set-up 의 $S_{xx}$ Eq 2.146 과 동일 정의.)

Force:
$$F_x = -\frac{\partial S_{xx}}{\partial x} - \frac{\partial S_{xy}}{\partial y} \quad \text{(3.63)},\qquad F_y = -\frac{\partial S_{yx}}{\partial x} - \frac{\partial S_{yy}}{\partial y} \quad \text{(3.64)}$$

곡선좌표 $\xi,\eta$ → physical 변환 (tensor 성분 $f$):
$$\frac{\partial f}{\partial\xi} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial\xi} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial\xi} \quad \text{(3.65)},\quad \frac{\partial f}{\partial\eta} = \cdots \quad \text{(3.66)}$$
$$\frac{\partial f}{\partial x} = \cdots \quad \text{(3.67)},\quad \frac{\partial f}{\partial y} = \cdots \quad \text{(3.68)}$$
수치근사 (2차 중심): $\frac{\partial f}{\partial\xi} \approx \frac{f_{\xi+1,\eta}-f_{\xi-1,\eta}}{2}$, $\frac{\partial f}{\partial\eta} \approx \frac{f_{\xi,\eta+1}-f_{\xi,\eta-1}}{2}$ **(3.69)**
> $x,y$ 미분도 동일 사용. 경계선 one-sided 근사.

## 4. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §) | User cmd | 비고 |
|---|---|---|
| 3.44-3.45 QC | `SCAT [...]` | Tukey γ=0.2 hardcoded, [[swan-quasi-coherent]] |
| §3.10 curvilinear | `CGRID CURVILINEAR` + `READGRID COORDINATES` | Taylor 기반 편미분 |
| 3.59-3.69 force | `FORCE` 출력 / `SETUP` 입력 | radiation stress F_x, F_y |

## 5. 한계

- §3.9 QC 보조식 (S_qc DFT ΔΣ/Δc_g/Δu, Tukey window full form): PDF 무번호 + alt-text truncated → 핵심값(γ=0.2, Δq=2Δk, L_c=2π/Δk)만 전사. 전체 알고리즘은 [[swan-quasi-coherent]] (SwanQCM 12 sub).
- 곡선 propagation(3.55)·action 보존(3.58): ASCII 다행식 → 구조 요약 (정밀식 swantech.pdf p.106-107).
- force ξη 변환(3.67-68): alt-text truncated → 구조만.

## 6. 연결

- [[swan-quasi-coherent]] — SwanQCM.ftn90 (QC source-analysis, §2.7+§3.9)
- [[swan-tech-ch3-discretization]] — §3.2 직교격자 이산화 (곡선격자 일반화 전)
- [[swan-tech-ch3-solution-iteration-limiter]] — four-sweep (곡선격자서 불변)
- [[swan-tech-ch2-obstacles-diffraction-setup]] — set-up $S_{xx}$ (force 와 동일 radiation stress)
- [[swan-tech-ch3-obstacles-spectral-ops]] — §3.12-3.16 (다음)
