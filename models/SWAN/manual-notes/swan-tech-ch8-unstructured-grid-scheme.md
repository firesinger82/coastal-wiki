---
title: "SWAN swantech Ch 8.1-8.3 Unstructured grid description + numerical method (vertex-based BSBT/N-scheme + crest sweeping) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 8 §8.1 Description of an unstructured grid + §8.2 grid generation + §8.3 Numerical method, doc p.135-142 (Eq 8.1-8.16). References: Zijlema 2009·2010, Shewchuk 1996 (Triangle), Struijs 1994 (N-scheme)."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 8 §8.1-8.3 직접 read via pdftotext (식 번호 context-verified: Euler relation 8.1-8.3·angle 8.4·F lumping 8.5·implicit Euler 8.6·base vectors 8.7-8.10·propagation expand 8.11-8.14·base vec 8.15·vertex update 8.16) + website_markdown node84-92.md LaTeX alt-text. Ch 8은 chapter-local 번호 → website=PDF 일치(offset 0)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 8.1-8.16 + C≈2V/φ>143°/3-sweep 120° verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/source-analysis/swan-unstructured-time-step.md
  - models/SWAN/source-analysis/swan-grid-readers.md
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch8-unstructured-ops.md
---

# swantech Ch 8.1-8.3 Unstructured grid + numerical method — verified verbatim

> swantech.pdf (v41.51) Ch 8 §8.1-8.3 직접 read. **비구조(삼각) 격자 SWAN** — nested 대안, 국소 refinement. Grid 정의/조건 + **vertex-based BSBT(=N-scheme) 이산화** + crest-ordering sweeping. 소스 구현 [[swan-unstructured-time-step]] (SwanCompUnstruc) + [[swan-grid-readers]]. Zijlema(2009·2010).
>
> **식 번호 주의**: Ch 8은 chapter-local → **website = PDF 일치 (offset 0)**.

## 0. 도입

심해→천해 wind wave 의 다양한 공간스케일 → **flexible grid** 로 국소 refinement (estuary/fjord 강한 bathymetry 변화). Nested 대안(복잡 프로그래밍·계산비 ↑ 회피). 비구조 격자: 국소 refinement(adaptive/fixed) + coastline/island 유연 생성. 점당 CPU 비용은 높으나 격자점 수 감소로 상쇄. **구조격자 four-direction Gauss-Seidel + 완전 implicit 시간(§3.3)을 비구조에 적용 → 임의 time step 안정.**

## 1. §8.1.1 Definitions

- **structured**: quadrilateral (rectilinear/curvilinear), 내부 vertex 당 항상 **4 cell**
- **unstructured**: 제약 해제. 보통 삼각형 또는 삼각+사각(hybrid). **SWAN 은 삼각형(cell)만** — 변 = **face**

## 2. §8.1.2 Cell/vertex/face 관계 (Eq 8.1-8.3)

삼각 mesh: cell $C$, boundary face $E_b$, internal face $E_i$:
$$E_b + 2E_i = 3C \quad \text{(8.1)}$$
총 face $E = E_i + E_b$. Vertex $V$, hole(island) $H$ → **Euler 관계**:
$$C + V - E = 1 - H \quad \text{(8.2)}$$
$E_b \ll E_i$, $H$ 무시 시:
$$C \approx 2V,\quad E \approx 3V \quad \text{(8.3)}$$
> **cell 이 vertex 의 약 2배** → action 을 **vertex 에 저장**이 unknown 최소(주어진 격자서) → 물리과정(생성·소산·재분배) 평가 계산시간 대폭 절약.

## 3. §8.1.3 Grid 조건 (Eq 8.4)

badly-shaped 회피:
- **내부 vertex 당 cell 수: 최소 4, 최대 10**
- 삼각형 내각 제한 (face tangent $\vec{a},\vec{b}$):
$$\cos\phi = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|} \quad \text{(8.4)}$$
> **$\cos\phi < -0.8$ (즉 $\phi > 143°$) 금지** (안전).

## 4. §8.2 Grid generation (서술)

coarse→fine refinement. 최적 격자 = bathymetry/wave 급변역 고해상도. **Triangle (Shewchuk 1996)** — free 2D Delaunay triangulator (Matlab/Python interface), acute 삼각형만. Refinement 기준:
- **$h$-refinement**: wavelength/grid size 비 크게 유지 (천수서 wavelength↓ → cell↓). $h$ = 수심
- **topographic length scale**: $\Delta h/h < 1$ ($\Delta h$ = 삼각형 max-min 수심차, $h$ = 평균). 큰 $\Delta h/h$ = steep bottom → 세분 필요
- **min area constraint** 병행 (너무 작은 삼각형 방지). 반복 refinement.

## 5. §8.3.1 Discretization procedure (Eq 8.5-8.16)

Eq 2.16 의 time-deriv + geographic propagation 외 전부를 $F(\vec{x},\sigma,\theta)$ 로 묶음:
$$\frac{\partial N}{\partial t} + \nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] = F \quad \text{(8.5)}$$
($\vec{c}_{\vec{x}} = \vec{c}_g + \vec{u}$). 삼각 mesh (hybrid 도 가능). **Vertex-based**: action $N$ 을 vertex 에 저장, 각 vertex 서 (8.5) 풂 (boundary vertex 값 고정).

**1차 implicit Euler**:
$$\frac{N^n - N^{n-1}}{\Delta t} + \nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N^n] = F^n \quad \text{(8.6)}$$
> **CFL 무제약** (explicit spectral 모델과 달리), time step 은 정확도만 제한. 대형 계 → **point-by-point multi-directional Gauss-Seidel** (iteration 중 신규 vertex 값 활용, **locally implicit globally explicit** → 대형 행렬 불필요 + 임의 time step 안정).

### 5.1 Vector calculus (Eq 8.7-8.10)

Vertex 1서 local $\vec{\xi}=(\xi,\eta)$ → Cartesian $\vec{x}=(x,y)$ 매핑. 접선 base vector:
$$\vec{e}_{(1)} = \frac{\partial\vec{x}}{\partial\xi},\quad \vec{e}_{(2)} = \frac{\partial\vec{x}}{\partial\eta} \quad \text{(8.7)}$$
법선 (등ξ/η면):
$$\vec{e}^{(1)} = \text{grad}\,\xi,\quad \vec{e}^{(2)} = \text{grad}\,\eta \quad \text{(8.8)}$$
reciprocal: $\vec{e}_{(\alpha)}\cdot\vec{e}^{(\beta)} = \delta_\alpha^\beta$ **(8.9)**. Cramer:
$$\vec{e}^{(1)} = \frac{1}{D}(e^2_{(2)}, -e^1_{(2)})^\top,\ \vec{e}^{(2)} = \frac{1}{D}(\cdots, e^1_{(1)})^\top,\ D = e^2_{(2)}e^1_{(1)} - e^2_{(1)}e^1_{(2)} \quad \text{(8.10)}$$

### 5.2 Propagation 이산화 (Eq 8.11-8.16)

$$\nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] = \frac{\partial c_x N}{\partial x} + \frac{\partial c_y N}{\partial y} \quad \text{(8.11)}$$
chain rule:
$$\nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] = e^{(1)}_1\frac{\partial c_x N}{\partial\xi} + e^{(2)}_1\frac{\partial c_x N}{\partial\eta} + e^{(1)}_2\frac{\partial c_y N}{\partial\xi} + e^{(2)}_2\frac{\partial c_y N}{\partial\eta} \quad \text{(8.12)}$$
**1차 one-sided 차분** (vertex 1,2,3 의 $N_1,N_2,N_3$, $\Delta\xi=\Delta\eta=1$): $\frac{\partial c_x N}{\partial\xi} \approx \frac{c_x N_1 - c_x N_2}{\Delta\xi}$ 등 **(8.13)** → (8.12) 대입:
$$\nabla_{\vec{x}}\cdot[\vec{c}_{\vec{x}}N] \approx c_x N|_2^1 e^{(1)}_1 + c_x N|_3^1 e^{(2)}_1 + c_y N|_2^1 e^{(1)}_2 + c_y N|_3^1 e^{(2)}_2 \quad \text{(8.14)}$$
base vector: $\vec{e}_{(1)} = \vec{x}_1 - \vec{x}_2$, $\vec{e}_{(2)} = \vec{x}_1 - \vec{x}_3$ **(8.15)**.

> 최저차 정확·**action 보존**(§8.7). **BSBT upwind 3 이유**: ① compact (1 삼각형만) ② characteristic 따라 전파 강제 (multidimensional·최소 cross-diffusion) ③ monotone ($N>0$ 보장). **정삼각 격자(대각선이 characteristic 정렬)서 N(arrow) scheme(fluctuation splitting)과 동일** (Struijs 1994 pp.63-64) — multidimensional·1차·monotone·conservative·narrow stencil·characteristic 일치(§3.2.1) 공유(완전 동일은 아님).

Vertex 1 갱신 (삼각형 △123, $N_2^n, N_3^n$ 주어짐):
$$\left[\frac{1}{\Delta t} + c_{x,1}(e^{(1)}_1 + e^{(2)}_1) + c_{y,1}(e^{(1)}_2 + e^{(2)}_2)\right]N_1^n = \frac{N_1^{n-1}}{\Delta t} + (c_{x,2}e^{(1)}_1 + c_{y,2}e^{(1)}_2)N_2^n + (c_{x,3}e^{(2)}_1 + c_{y,3}e^{(2)}_2)N_3^n + F^n \quad \text{(8.16)}$$
> Face $\vec{e}_{(1)},\vec{e}_{(2)}$ 사이 방향($\theta_1$~$\theta_2$ shaded sector) = (8.16)의 **domain of dependence**. Characteristic 가 이 sector 내 → **CFL 안정 무관**(causality). $F^n$ 은 sector 내 implicit 이산화 (spectral 근사·source 선형화 §3.3). 모든 둘러싼 cell 처리 시 vertex 1 갱신 완료. Refraction·nonlinear 로 sector 간 shift → 반복 수렴.

## 6. §8.3.2 Sweeping algorithm

각 vertex 는 다음 진행 전 geographic 갱신 필요 (upwave vertex 2,3 갱신 후만 → causality). 구조격자는 four-sweep natural ordering. **비구조는 distinct direction 없음** → vertex 를 번호순(랜덤) 정렬하면 최신해 미활용.

**Crest ordering** 제안: vertex 를 **main wave direction 수직(wave crest 따라)** 정렬 — main dir = 경계 입사 wave energy 또는 wind 방향. **격자 원점 거리 오름차순** 정렬. Characteristic 따라 갱신 → random 보다 빠른 수렴 (직선 ray 적합, 곡선 ray(섬 주변)는 비효율 → 실효 Gauss-Seidel 아님).

**M sweep** (4 불필요), 각 sweep = $2\pi/M$ 방향범위. 예: **3 sweep × 120°** (1st = dominant, 2nd = +120°, 3rd = -120°) → 3 vertex ordering → 타 방향 전파도 커버. sweep ↑ → 방향간격 ↓ → iteration ↓ (단 계산량 ↑). **3 sweep 이 좋은 절충**.

알고리즘: sweep 별 미갱신 vertex list (sweep 방향 따라 원점거리 오름차순) 순회. 2 upwave face 가 처리가능 wave 방향 enclose. Vertex 둘러싼 모든 cell 처리 시 갱신. Sweep 완료 = 전 vertex geographic 갱신. Iteration 완료 = 전 sweep 수행(전 vertex geographic+spectral 갱신). **curvature stopping(§3.4)** 까지 반복.

## 7. SWAN 옵션 매핑

| Tech (PDF §8) | User cmd | 비고 |
|---|---|---|
| §8.1 grid | `CGRID UNSTRUCTURED` + `READGRID UNSTRUCTURED ADCIRC/TRIANGLE/EASYMESH` | [[swan-grid-readers]] |
| §8.3 vertex BSBT | (internal, 임의 time step) | N-scheme 유사 |
| §8.3.2 sweeps | `NUMERIC ... ` (sweep 수) | crest ordering, 3 권장 |

## 8. 한계

- (8.13)·(8.16): 다행/truncated 식 → 구조 전사 (정밀식 swantech.pdf p.139-141).
- §8.4-8.7 (interpolation·force·diffusion·action conservation, Eq 8.17-8.45) → [[swan-tech-ch8-unstructured-ops]] (다음).
- 소스 구현(vertex loop·sweep·contributor) 상세는 [[swan-unstructured-time-step]] (SwanCompUnstruc.ftn90).

## 9. 연결

- [[swan-unstructured-time-step]] — SwanCompUnstruc.ftn90 (vertex sweep 구현, Casey Dietrich 41.20)
- [[swan-grid-readers]] — ADCIRC/Triangle/Easymesh reader
- [[swan-tech-ch3-discretization]] — §3.2 구조격자 BSBT (semi-Lagrangian 공유)
- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3 four-sweep + source 선형화 (8.16 의 F^n)
- [[swan-tech-ch8-unstructured-ops]] — §8.4-8.7 (interpolation·force·diffusion·action conservation)
