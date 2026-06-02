---
title: "SWAN swantech Ch 8.4-8.7 Unstructured — interpolation + wave-induced force + diffusion-like terms + action conservation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 8 §8.4 Interpolation at user-defined locations + §8.5 Computation of wave-induced force + §8.6 Calculation of diffusion-like terms + §8.7 Conservation of action, doc p.143-147 (Eq 8.17-8.45)."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 8 §8.4-8.7 직접 read via pdftotext (식 번호 context-verified: linear interp 8.17·Green-Gauss 8.18·∇φ 8.22-24·area 8.26·shape function 8.27-29·radiation stress 8.30-34·CV gradient 8.35-38·diffusion 8.39·action conservation 8.40-45) + website_markdown node93-96.md LaTeX alt-text. Ch 8은 chapter-local 번호 → website=PDF 일치(offset 0)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 8.17-8.45 + centroid dual/Green-Gauss verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch8-unstructured-grid-scheme.md
  - models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/source-analysis/swan-unstructured-time-step.md
---

# swantech Ch 8.4-8.7 Unstructured ops — verified verbatim

> swantech.pdf (v41.51) Ch 8 §8.4-8.7 직접 read. [[swan-tech-ch8-unstructured-grid-scheme]] (§8.1-8.3 격자+scheme)의 **보조 연산** — 사용자위치 보간(Green-Gauss) + wave force(centroid dual) + diffusion-like 항(GSE/diffraction) + action 보존 증명.
>
> **식 번호 주의**: Ch 8은 chapter-local → **website = PDF 일치 (offset 0)**.

## 1. §8.4 Interpolation at user-defined locations (Eq 8.17-8.29)

모든 양이 vertex 위치 → user 위치엔 보간. Cell $i$ vertex 1,2,3 (반시계), edge 12/23/31. $\varphi_j = \varphi(\vec{x}_j)$.

### 1.1 Green-Gauss reconstruction

선형보간 ($\vec{x}_0$ cell 내, $\varphi_0$):
$$\varphi(\vec{x}) = \varphi_0 + \nabla\varphi\cdot(\vec{x}-\vec{x}_0) \quad \text{(8.17)}$$
$\nabla\varphi$ = cell 내 상수, **Green-Gauss**:
$$\nabla\varphi \approx \frac{1}{A_i}\int_{\triangle i}\nabla\varphi\,d\Omega = \frac{1}{A_i}\oint_{\partial\triangle i}\varphi\vec{n}\,d\Gamma \approx \frac{1}{A_i}\sum_e\varphi_e\vec{n}_e \quad \text{(8.18)}$$
- $A_i$ = cell 면적, $e\in\{12,23,31\}$. Edge 값 = 평균: $\varphi_{12} = \tfrac{1}{2}(\varphi_1+\varphi_2)$ 등 **(8.19)**
- outward normal (edge 를 시계 90° 회전): $\vec{n}_{12} = R\vec{t}_{12}$, $R = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $\vec{t}_{12} = \vec{x}_2-\vec{x}_1$ **(8.20)**
- 항등식: $\vec{n}_{12} + \vec{n}_{23} + \vec{n}_{31} = 0$ **(8.21)**

결과:
$$\nabla\varphi = \frac{1}{2A_i}[\vec{n}_{12}(\varphi_1-\varphi_3) + \vec{n}_{31}(\varphi_1-\varphi_2)] = -\frac{1}{2A_i}[\varphi_1\vec{n}_{23} + \varphi_2\vec{n}_{31} + \varphi_3\vec{n}_{12}] \quad \text{(8.22)}$$
$$\frac{\partial\varphi}{\partial x} = \frac{1}{2A_i}[\varphi_1(y_2-y_3) + \varphi_2(y_3-y_1) + \varphi_3(y_1-y_2)] \quad \text{(8.23)}$$
$$\frac{\partial\varphi}{\partial y} = \frac{1}{2A_i}[\varphi_1(x_3-x_2) + \varphi_2(x_1-x_3) + \varphi_3(x_2-x_1)] \quad \text{(8.24)}$$
면적 $A_i = |\vec{t}_{12}\cdot\vec{n}_{13}|/2$, $\vec{n}_{13} = R\vec{t}_{13} = (y_3-y_1, x_1-x_3)^T$ **(8.25)**:
$$A_i = \frac{1}{2}|(x_2-x_1)(y_3-y_1) - (x_3-x_1)(y_2-y_1)| \quad \text{(8.26)}$$

### 1.2 Shape function 대안 (Eq 8.27-8.29)

$$\varphi(\vec{x}) = \sum_k\varphi_k\lambda_k(\vec{x}) = \varphi_1\lambda_1 + \varphi_2\lambda_2 + \varphi_3\lambda_3 \quad \text{(8.27)}$$
linear shape function ($\lambda_k$ cell당 선형, $\lambda_k(\vec{x}_j) = \delta_{kj}$):
$$\lambda_k(\vec{x}) = a_0^k + a_x^k x + a_y^k y \quad \text{(8.28)}$$
계수 $a$:
$$\begin{pmatrix}1&x_1&y_1\\1&x_2&y_2\\1&x_3&y_3\end{pmatrix}\begin{pmatrix}a_0^k\\a_x^k\\a_y^k\end{pmatrix} = I \quad \text{(8.29)}$$

## 2. §8.5 Wave-induced force (Eq 8.30-8.38)

Radiation stress (§3.11 Eq 3.59-61 과 동일, [[swan-tech-ch3-qc-curvilinear]]):
$$S_{xx} = \rho g\int[n\cos^2\theta + n - \tfrac{1}{2}]E\,d\sigma d\theta \quad \text{(8.30)}$$
$$S_{xy} = S_{yx} = \rho g\int n\sin\theta\cos\theta\,E\,d\sigma d\theta \quad \text{(8.31)}$$
$$S_{yy} = \rho g\int[n\sin^2\theta + n - \tfrac{1}{2}]E\,d\sigma d\theta \quad \text{(8.32)}$$
($n$ = $c_g/c$ 비). Force:
$$F_x = -\frac{\partial S_{xx}}{\partial x} - \frac{\partial S_{xy}}{\partial y} \quad \text{(8.33)},\qquad F_y = -\frac{\partial S_{yx}}{\partial x} - \frac{\partial S_{yy}}{\partial y} \quad \text{(8.34)}$$

### 2.1 Centroid dual control volume (Eq 8.35-8.38)

내부 vertex force → **centroid dual CV** (vertex 둘러싼 centroid 연결, 전 도메인 채움·비중첩). $\varphi$ = $S_{xx}/S_{xy}/S_{yy}$:
$$\nabla\varphi \approx \frac{1}{A_{\text{CV}}}\sum_e\varphi_e\vec{n}_e \quad \text{(8.35)}$$
- edge 값 = centroid dual edge 평균 $(\varphi_0+\varphi_1)/2$ 등. 삼각형 내 radiation stress = vertex 평균
$$\frac{\partial\varphi}{\partial x} = \frac{1}{2A_{\text{CV}}}\sum_{i=0}^{n-1}(\varphi_i+\varphi_{i+1})(y_{i+1}-y_i) \quad \text{(8.36)}$$
$$\frac{\partial\varphi}{\partial y} = \frac{1}{2A_{\text{CV}}}\sum_{i=0}^{n-1}(\varphi_i+\varphi_{i+1})(x_i-x_{i+1}) \quad \text{(8.37)}$$
($n$ = 둘러싼 cell 수, $\varphi_n=\varphi_0$ 등 cyclic)
$$A_{\text{CV}} = \frac{1}{2}\sum_{i=0}^{n-1}(x_i y_{i+1} - x_{i+1}y_i) \quad \text{(8.38)}$$
> (8.36)이 §3.8.5 (refraction limiter)의 비구조 gradient (Eq 3.85 대체용 Green-Gauss "Eq 8.36")로 참조됨.

## 3. §8.6 Diffusion-like terms (Eq 8.39)

비구조서 필요한 diffusion-like 항:
$$\nabla\cdot(\kappa\nabla\varphi) \quad \text{(8.39)}$$
($\kappa$ = space-varying diffusion coeff tensor, $\varphi$ = vertex scalar). SWAN 적용:
- **GSE 완화** (§3.2 Eq 3.13 [[swan-tech-ch3-discretization]])
- **diffraction parameter** (§2.5.4 Eq 2.141 [[swan-tech-ch2-obstacles-diffraction-setup]], 본문 "2.181" HTML)

**3 step**: ① 각 cell 내 $\nabla\varphi$ (Eq 8.23-8.24) ② centroid 의 $\kappa$ 곱 ③ CV 내 $\kappa\nabla\varphi$ gradient (Eq 8.36-8.37).

## 4. §8.7 Conservation of action (Eq 8.40-8.45)

(8.16) 이산화가 **energy 보존** 증명 (stationary, $F=0$). (8.16)서:
$$\vec{e}^{(1)}\cdot(\vec{c}_{\vec{x}}N)_1 + \vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_1 = \vec{e}^{(1)}\cdot(\vec{c}_{\vec{x}}N)_2 + \vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_3 \quad \text{(8.40)}$$
한편 divergence theorem:
$$\nabla\cdot(\vec{c}_{\vec{x}}N) = \frac{1}{\Omega}\oint\vec{c}_{\vec{x}}N\cdot\vec{n}\,d\Gamma \quad \text{(8.41)}$$
edge 평균:
$$\nabla\cdot(\vec{c}_{\vec{x}}N) \approx \frac{1}{2\Omega}[((\vec{c}_{\vec{x}}N)_1+(\vec{c}_{\vec{x}}N)_2)\cdot\vec{n}_{12} + ((\vec{c}_{\vec{x}}N)_2+(\vec{c}_{\vec{x}}N)_3)\cdot\vec{n}_{23} + ((\vec{c}_{\vec{x}}N)_3+(\vec{c}_{\vec{x}}N)_1)\cdot\vec{n}_{31}] \quad \text{(8.42)}$$
항등식 $\vec{n}_{23} = -\vec{n}_{12} - \vec{n}_{31}$ **(8.43)**, $\vec{n}_{12} = -\vec{e}^{(2)}$, $\vec{n}_{31} = -\vec{e}^{(1)}$ **(8.44)**:
$$\nabla\cdot(\vec{c}_{\vec{x}}N) \approx \frac{1}{2\Omega}[\vec{e}^{(1)}\cdot((\vec{c}_{\vec{x}}N)_1-(\vec{c}_{\vec{x}}N)_2)\cdots - \vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_3] = 0 \quad \text{(8.45)}$$
> stationary·무source 시 divergence = 0 → **energy flux vector divergence-free** → 삼각형 face 수직 flux 의 closed 적분 = 0 (source-free, compact BSBT). **Face $\vec{e}_{(1)}, \vec{e}_{(2)}$ 사이 wave characteristic 따라 energy flux 일정** → **BSBT = characteristic 일치 semi-Lagrangian** (비균일 수심·current 에도 성립).

## 5. SWAN 옵션 매핑

| Tech (PDF §8) | User cmd | 비고 |
|---|---|---|
| §8.4 interpolation | `POINTS`/`CURVE` 출력 | Green-Gauss / shape function |
| §8.5 force | `FORCE` 출력 | centroid dual |
| §8.6 diffusion | `GSE`/`DIFFRAC` (비구조) | Green-Gauss gradient |
| §8.7 (이론) | — | action 보존 증명 |

## 6. 한계

- (8.22)·(8.29)·(8.42)·(8.45): 다행/matrix/truncated 식 → 구조 전사 (정밀식 swantech.pdf p.143-147).
- §8.6 diffraction 참조식 "2.181"(HTML)은 본 위키 PDF Eq 2.141 ([[swan-tech-ch2-obstacles-diffraction-setup]]).
- 소스 구현은 [[swan-unstructured-time-step]].

## 7. 연결

- [[swan-tech-ch8-unstructured-grid-scheme]] — §8.1-8.3 (격자+BSBT scheme, 8.16 보존 대상)
- [[swan-tech-ch3-qc-curvilinear]] — §3.11 force (8.30-34 와 동일 radiation stress)
- [[swan-tech-ch3-discretization]] — §3.2 GSE (8.6 diffusion 적용처) Eq 3.13
- [[swan-tech-ch2-obstacles-diffraction-setup]] — §2.5.4 diffraction (8.6 적용처) Eq 2.141
- [[swan-unstructured-time-step]] — SwanCompUnstruc.ftn90 구현
