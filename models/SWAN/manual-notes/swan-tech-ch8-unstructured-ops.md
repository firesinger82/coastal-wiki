---
title: "SWAN swantech Ch 8.4-8.7 Unstructured — interpolation + wave-induced force + diffusion-like terms + action conservation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 8 §8.4 Interpolation at user-defined locations + §8.5 Computation of wave-induced force + §8.6 Calculation of diffusion-like terms + §8.7 Conservation of action, doc p.143-147 (Eq 8.17-8.45)."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 8 §8.4-8.7 직접 read via pdftotext (식 번호 context-verified: linear interp 8.17·Green-Gauss 8.18·∇φ 8.22-24·area 8.26·shape function 8.27-29·radiation stress 8.30-34·CV gradient 8.35-38·diffusion 8.39·action conservation 8.40-45) + website_markdown node93-96.md LaTeX alt-text. Ch 8은 chapter-local 번호 → website=PDF 일치(offset 0).; 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
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

> swantech.pdf (v41.51) Ch 8 §8.4-8.7 직접 read. [swan-tech-ch8-unstructured-grid-scheme](swan-tech-ch8-unstructured-grid-scheme.md) (§8.1-8.3 격자+scheme)의 **보조 연산** — 사용자위치 보간(Green-Gauss) + wave force(centroid dual) + diffusion-like 항(GSE/diffraction) + action 보존 증명.
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
$$\begin{pmatrix}1&x_1&y_1\\1&x_2&y_2\\1&x_3&y_3\end{pmatrix}\begin{pmatrix}a_0^1&a_0^2&a_0^3\\a_x^1&a_x^2&a_x^3\\a_y^1&a_y^2&a_y^3\end{pmatrix}=I \quad \text{(8.29)}$$

(swantech PDF 152쪽 / 인쇄 144쪽; R1:TN-211)

## 2. §8.5 Wave-induced force (Eq 8.30-8.38)

Radiation stress (§3.11 Eq 3.59-61 과 동일, [swan-tech-ch3-qc-curvilinear](swan-tech-ch3-qc-curvilinear.md)):
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
- **GSE 완화**는 §3.2.1의 무번호 확산항을 사용한다. ([swan-tech-ch3-discretization](swan-tech-ch3-discretization.md); swantech PDF 82쪽 / 인쇄 74쪽; `online_doc/swantech/node38.html:467–478`의 HTML 식 (3.13)) [10-13 전수 검증 정정]
- **회절 매개변수**는 §2.5.4의 식 (2.138)이다. ([swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md); swantech PDF 64쪽 / 인쇄 56쪽; `online_doc/swantech/node29.html:126–133`의 HTML 식 (2.180)) [10-13 전수 검증 정정]

GSE는 현재 절점의 확산 텐서를 둘러싼 모든 셀에 공통 적용한다. 회절처럼 셀 중심에서 계수를 다시 평균하지 않는다. (`src/SwanGSECorr.ftn90:200,238` `dgx0 = dxx*dac2dx + dxy*dac2dy`; `dgx1 = dxx*dac2dx + dxy*dac2dy`; R1:TN-218)

비정렬 GSE는 현재 갱신 중인 `ac2`를 사용한다. 정렬 S&L의 이전 시간 `AC1` 보정과 다르다. 경계 절점에는 보정을 적용하지 않는다. (`src/SwanGSECorr.ftn90:127` `if ( vert(ivert)%atti(VMARKER) == 1 ) return`; `src/SwanGSECorr.ftn90:181` `dac2dx = 0.5*( ac2(id,is,v(1))*(ycugrd(v(2))-ycugrd(v(3))) + &`; R1:TC-008)

## 4. §8.7 Conservation of action (Eq 8.40-8.45)

(8.40)–(8.45)가 보이는 것은 지정한 무원천 조건에서의 작용 플럭스 보존이다. (swantech PDF 155쪽 / 인쇄 147쪽; R1:TN-224)

정상·$F=0$ 조건에서 (8.16)은 다음 식이다.
$$\vec{e}^{(1)}\cdot(\vec{c}_{\vec{x}}N)_1 + \vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_1 = \vec{e}^{(1)}\cdot(\vec{c}_{\vec{x}}N)_2 + \vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_3 \quad \text{(8.40)}$$
한편 divergence theorem:
$$\nabla\cdot(\vec{c}_{\vec{x}}N) = \frac{1}{\Omega}\oint\vec{c}_{\vec{x}}N\cdot\vec{n}\,d\Gamma \quad \text{(8.41)}$$
edge 평균:
$$\nabla\cdot(\vec{c}_{\vec{x}}N) \approx \frac{1}{2\Omega}[((\vec{c}_{\vec{x}}N)_1+(\vec{c}_{\vec{x}}N)_2)\cdot\vec{n}_{12} + ((\vec{c}_{\vec{x}}N)_2+(\vec{c}_{\vec{x}}N)_3)\cdot\vec{n}_{23} + ((\vec{c}_{\vec{x}}N)_3+(\vec{c}_{\vec{x}}N)_1)\cdot\vec{n}_{31}] \quad \text{(8.42)}$$
항등식 $\vec{n}_{23} = -\vec{n}_{12} - \vec{n}_{31}$ **(8.43)**. 반시계 셀에서 올바른 관계는 $\vec n_{12}=D\vec e^{(2)},\ \vec n_{31}=D\vec e^{(1)},\ D=2\Omega$이다. 법선은 길이, 역기저는 길이 역수이다. 문서 식 (8.44)는 부호와 면적 계수를 빠뜨렸다. (swantech PDF 155쪽 / 인쇄 147쪽; `src/SwanGridCell.ftn90:170` `rdet = 1./(dy2*dx1 - dy1*dx2)`; R1:TN-222)
$$\nabla\cdot(\vec{c}_{\vec{x}}N) \approx \vec{e}^{(1)}\cdot(\vec{c}_{\vec{x}}N)_1+\vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_1-\vec{e}^{(1)}\cdot(\vec{c}_{\vec{x}}N)_2-\vec{e}^{(2)}\cdot(\vec{c}_{\vec{x}}N)_3 = 0 \quad \text{(8.45)}$$

(8.44)를 수정하여 (8.42)에 대입하면 대괄호만 남는다. (8.45)의 $1/(2\Omega)$는 중복이다. 정상 무원천 국소 잔차가 0이라는 결론은 유지된다. (swantech PDF 155쪽 / 인쇄 147쪽; R1:TN-223)
> 흐름이 있을 때 스펙트럼 수송을 포함한 $F$를 0으로 두는 조건 없이 전체 에너지 플럭스 보존으로 확장할 수 없다. (swantech PDF 155쪽 / 인쇄 147쪽; `src/SwanTranspX.ftn90:130–131`의 `ac2`; R1:TN-224)

## 5. SWAN 옵션 매핑

| Tech (PDF §8) | User cmd | 비고 |
|---|---|---|
| §8.4 interpolation | `POINTS`/`CURVE` 출력 | Green-Gauss / shape function |
| §8.5 force | `FORCE` 출력 | centroid dual |
| §8.6 diffusion | `GSE`/`DIFFRAC` (비구조) | Green-Gauss gradient |
| §8.7 (이론) | — | action 보존 증명 |

## 6. 한계

- 셀 내부 선형 플럭스 또는 셀 평균 발산에 적용하는 보존성 증명이다. (swantech PDF 155쪽 / 인쇄 147쪽, 식 (8.41)·(8.42); R1:TN-220)
- §8.6의 HTML 링크 표시는 "2.181"이다. 링크 대상 `eq3-44`는 HTML 식 (2.180)과 PDF 식 (2.138)에 해당한다. (`online_doc/swantech/node95.html:76`; `online_doc/swantech/node29.html:126–133`; swantech PDF 64쪽 / 인쇄 56쪽; [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md)) [10-13 전수 검증 정정]
- 소스 구현은 [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md).

## 7. 연결

- [swan-tech-ch8-unstructured-grid-scheme](swan-tech-ch8-unstructured-grid-scheme.md) — §8.1-8.3 (격자+BSBT scheme, 8.16 보존 대상)
- [swan-tech-ch3-qc-curvilinear](swan-tech-ch3-qc-curvilinear.md) — §3.11 force (8.30-34 와 동일 radiation stress)
- [swan-tech-ch3-discretization](swan-tech-ch3-discretization.md) — §3.2.1 GSE 확산항은 swantech PDF 82쪽 / 인쇄 74쪽의 무번호 식이다. HTML 식 번호는 (3.13)이다. [10-13 전수 검증 정정]
- [swan-tech-ch2-obstacles-diffraction-setup](swan-tech-ch2-obstacles-diffraction-setup.md) — §2.5.4 회절 매개변수는 swantech PDF 64쪽 / 인쇄 56쪽의 식 (2.138)이다. [10-13 전수 검증 정정]
- [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) — SwanCompUnstruc.ftn90 구현

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론). 아래 결론 문장은 R1의 AI 해석이다. [10-13 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-211 | 문서 식 (8.27)·(8.28)·(8.29) | swantech PDF 152쪽 / 인쇄 144쪽, (8.27): $\varphi(\vec x)=\sum_k\varphi_k\lambda_k(\vec x)$; $\lambda_k(\vec x_j)=\delta_{kj}$; (8.28): $\lambda_k=a_0^k+a_x^kx+a_y^ky$; (8.29): $\begin{pmatrix}1&x_1&y_1\\1&x_2&y_2\\1&x_3&y_3\end{pmatrix}\begin{pmatrix}a_0^1&a_0^2&a_0^3\\a_x^1&a_x^2&a_x^3\\a_y^1&a_y^2&a_y^3\end{pmatrix}=I$. | `src/SwanInterpolatePoint.ftn90:220,244` `phic = ( phi1 + phi2 + phi3 ) / 3.`; `foutp = phic + xgrs*(x - xc) + ygrs*(y - yc)` | F 표기 차이 | 해석: 코드는 $3\times3$ 연립식을 별도로 풀지 않는다. $\lambda_k=1/3+\nabla\lambda_k\cdot(\vec x-\vec x_c)$를 대입하면 (8.17)과 같아진다. 따라서 별도 미구현 보간법으로 분류하지 않는다. |
| R1:TN-218 | 문서 식 (8.39) | swantech PDF 154쪽 / 인쇄 146쪽, (8.39)의 GSE 적용도 “$\kappa$ as given in the centroid”. | `src/SwanGSECorr.ftn90:140,143–144,200,238` `dcg = 0.5 * abs(cgo(is+1,1)-cgo(is-1,1))`; `dss = dcg**2*WAVAGE/12.`; `dnn = (cgo(is,1)*DDIR)**2 * WAVAGE/12.`; `dgx0 = dxx*dac2dx + dxy*dac2dy`; `dgx1 = dxx*dac2dx + dxy*dac2dy` | C 문서 누락 | GSE는 현재 절점의 확산 텐서를 둘러싼 모든 셀에 공통 적용한다. 회절처럼 셀 중심에서 계수를 다시 평균하지 않는다. 문서는 이 경로 차이를 적지 않는다. |
| R1:TN-220 | 문서 식 (8.41)·(8.42) | swantech PDF 155쪽 / 인쇄 147쪽, (8.41): $\nabla\cdot\vec F=\Omega^{-1}\oint\vec F\cdot\vec n\,d\Gamma$; (8.42): $\nabla\cdot\vec F\approx[(\vec F_1+\vec F_2)\cdot\vec n_{12}+(\vec F_2+\vec F_3)\cdot\vec n_{23}+(\vec F_3+\vec F_1)\cdot\vec n_{31}]/(2\Omega)$. | — | H 코드 대조 대상 아님 | 셀 내부 선형 플럭스 또는 셀 평균 발산에 적용하는 보존성 증명이다. 임의 공간함수의 점별 발산과 경계 적분이 항상 같다는 식으로 사용하지 않는다. |
| R1:TN-222 | 문서 식 (8.44) | swantech PDF 155쪽 / 인쇄 147쪽, (8.44): $\vec n_{12}=-\vec e^{(2)},\ \vec n_{31}=-\vec e^{(1)}$. | `src/SwanGridCell.ftn90:170,177–180` `rdet = 1./(dy2*dx1 - dy1*dx2)`; `cell(icell)%geom(j)%rdx1 =  dy2*rdet`; `cell(icell)%geom(j)%rdy2 =  dx1*rdet` | B 문서 오기 | 해석: (8.15)의 기저와 반시계 꼭짓점에서 올바른 관계는 $\vec n_{12}=D\vec e^{(2)},\ \vec n_{31}=D\vec e^{(1)},\ D=2\Omega$이다. 법선은 길이, 역기저는 길이 역수이다. 문서 식은 부호와 면적 계수를 빠뜨렸다. |
| R1:TN-223 | 문서 식 (8.45) | swantech PDF 155쪽 / 인쇄 147쪽, (8.45): $\nabla\cdot\vec F\approx[\vec e^{(1)}\cdot\vec F_1+\vec e^{(2)}\cdot\vec F_1-\vec e^{(1)}\cdot\vec F_2-\vec e^{(2)}\cdot\vec F_3]/(2\Omega)=0$. | `src/SwanTranspX.ftn90:128` `asum = (rdx(1)+rdx(2))*cax(id,is,1) + (rdy(1)+rdy(2))*cay(id,is,1)`; `src/SwanTranspX.ftn90:135–136` `amat(id,is,1) = amat(id,is,1) + asum`; `rhs (id,is  ) = rhs (id,is  ) + rsum` | B 문서 오기 | 해석: (8.44)를 수정하여 (8.42)에 대입하면 대괄호만 남는다. (8.45)의 $1/(2\Omega)$는 중복이다. 정상 무원천 국소 잔차가 0이라는 결론은 유지된다. [10-13 전수 검증 정정] |
| R1:TN-224 | 작용 플럭스와 에너지 플럭스 | swantech PDF 155쪽 / 인쇄 147쪽: “energy flux vector is divergence free”; “also holds for non-uniform depth and ambient current”. | — | B 문서 오기 | 해석: (8.40)–(8.45)가 보이는 것은 지정한 무원천 조건에서의 작용 플럭스 보존이다. 흐름이 있을 때 스펙트럼 수송을 포함한 $F$를 0으로 두는 조건 없이 전체 에너지 플럭스 보존으로 확장할 수 없다. |
| R1:TC-008 | 비정렬 GSE의 시간 수준과 경계점 | — | `src/SwanGSECorr.ftn90:127,181,271` `if ( vert(ivert)%atti(VMARKER) == 1 ) return`; `dac2dx = 0.5*( ac2(id,is,v(1))*(ycugrd(v(2))-ycugrd(v(3))) + &`; `rhs  (id,is  ) = rhs  (id,is  ) + dgxdx + dgydy` | C 문서 누락 | 비정렬 GSE는 현재 갱신 중인 `ac2`를 사용한다. 정렬 S&L의 이전 시간 `AC1` 보정과 다르다. 경계 절점에는 보정을 적용하지 않는다. |
| R1:TC-014 | 보간 위치의 예외값·경계 각도 허용량 | — | `src/SwanInterpolatePoint.ftn90:132,141–143,181–187,210` `if ( EQREAL(finp(ivert),excval) ) return`; `foutp = finp(ivert)`; `eps = PI/360.`; `eps = 0.`; `if ( th > th1-eps .and. th <= th2+eps ) then` | C 문서 누락 | 같은 절점이면 직접 복사한다. 셀 꼭짓점에 예외값이 있으면 선형 보간을 하지 않는다. 경계 검색은 $0.5^\circ$ 허용량을 사용한다. |
| R1:TC-015 | 비정렬 힘의 건조·경계·퇴화 제어체적 처리 | — | `src/SwanComputeForce.ftn90:156,203–208,230,280–283` `fx = 0.`; `fy = 0.`; `if ( vert(ivert)%atti(VMARKER) == 1 ) cycle vertexloop`; `if ( dep2(v(1)) <= DEPMIN .or. dep2(v(2)) <= DEPMIN .or. dep2(v(3)) <= DEPMIN ) cycle vertexloop`; `if ( area <= 0d0 ) then` | C 문서 누락 | 경계 절점과 건조 셀을 접한 절점의 힘은 초기값 0을 유지한다. 비양수 면적에는 오류 수준 2를 보고하고 해당 절점을 건너뛴다. |
