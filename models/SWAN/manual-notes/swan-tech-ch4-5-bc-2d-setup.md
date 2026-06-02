---
title: "SWAN swantech Ch 4 Wave BC/IC + Ch 5 Implementation of 2D wave setup (Poisson finite-volume curvilinear) verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 4 Wave boundary and initial conditions (doc p.117-118) + Ch 5 Implementation of 2D wave setup §5.1-5.2 (doc p.119-126, Eq 5.1-5.25). References: Pierson-Moskowitz 1964, Hasselmann et al. 1973 (JONSWAP), Kahma-Calkoen 1992, Dingemans 1997, Wesseling 2001, Botta-Ellenbroek 1985."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 4-5 직접 read via pdftotext (식 번호 context-verified: equilibrium 5.1·Poisson 5.2·BC 5.3·problem def 5.4·Neumann 5.5·Dirichlet 5.6·covariant/contravariant 5.7-5.12·FV integration 5.13-5.14·base vector approx 5.15-5.16·integration path 5.17-5.22·Neumann half-cell 5.23-5.24·matrix system 5.25) + website_markdown node64-77.md LaTeX alt-text. Ch 5/6은 chapter-local 번호라 website=PDF 일치 (offset 없음)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 5.1-5.25 + 9-point stencil/NWKARR=9/MXC×MYC verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-qc-curvilinear.md
  - models/SWAN/manual-notes/swan-tech-ch2-obstacles-diffraction-setup.md
  - models/SWAN/manual-notes/swan-tech-ch6-iterative-solvers.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
---

# swantech Ch 4 BC/IC + Ch 5 2D wave setup — verified verbatim

> swantech.pdf (v41.51) Ch 4-5 직접 read. **파 경계/초기조건** (Ch 4, 무방정식) + **2D wave setup 의 Poisson 식 finite-volume 곡선격자 해법** (Ch 5, Eq 5.1-5.25). [[swan-tech-ch2-obstacles-diffraction-setup]] §6 의 1D set-up (Eq 2.145-2.147)을 2D 수치로 확장.
>
> **식 번호 주의**: Ch 5/6은 chapter-local 번호 → **website = PDF 일치** (Ch 2/3 같은 offset 없음).

## A. Ch 4 — Wave boundary and initial conditions (무방정식)

### A.1 Wave BC (up-wave 경계)

2D spectrum 지정, 3 옵션:
- **1D parametric spectrum + directional distribution**: Pierson-Moskowitz(1964) / **JONSWAP**(Hasselmann 1973) / Gaussian
- **1D discrete spectrum + directional dist** (측정 기반)
- **2D discrete spectrum** (다른 SWAN run 또는 WAM/WAVEWATCH III)

### A.2 Frequency/directional 경계

- **주파수 경계**: 최저·최고 이산주파수서 **fully absorbing** (에너지 자유 전파 → 일부 경우 total energy 미보존). 단 high-freq cut-off 위에 **diagnostic tail $f^{-m}$ ($m=4$ 또는 $5$)** 추가 (고주파 nonlinear 상호작용 + integral parameter 계산용)
- **방향 경계**: closed circular 시 불필요. 경제성 위해 pre-defined directional sector 옵션 (경계 fully absorbing, refraction 으로 action 제거 가능)

### A.3 Geographic 경계

- **land**: 무파 생성 + 입사 에너지 전부 흡수 (무문제)
- **water**: 관측 있으면 입력. 없으면 무파 입사 + 자유 유출 가정 (오차 → 관심영역서 멀리 배치 필수)

### A.4 Initial conditions

- **Nonstationary default**: local wind 으로 **Kahma-Calkoen(1992) deep-water growth curve** ($H_s$·peak freq 는 PM 1964 cut-off), fetch = 평균 spatial step, shape = JONSWAP + $\cos^2\theta$ (local wind 방향 중심)
- **Stationary first guess**: SWAN 2nd-generation mode
- 이전 stationary/nonstationary 계산 결과로 초기상태 가능

## B. Ch 5 — Implementation of 2D wave setup

### B.1 §5.1 지배식 (Eq 5.1-5.3)

Wave setup = 해안 근접 narrow zone, quasi-stationary. Wave-induced force ↔ setup gradient 평형:
$$gd\left(\frac{\partial\zeta}{\partial x} + \frac{\partial\zeta}{\partial y}\right) + F_x + F_y = 0 \quad \text{(5.1)}$$
($\zeta$=setup, $d$=수심, $F_i$=단위질량당 wave-induced force)

식 수 1개로 축소: Dingemans(1997) — wave-driven current 는 force 의 divergence-free 부분, setup 은 rotation-free 부분. (5.1)의 divergence → **elliptic Poisson 식**:
$$\frac{\partial}{\partial x}\left(gd\frac{\partial\zeta}{\partial x}\right) + \frac{\partial}{\partial y}\left(gd\frac{\partial\zeta}{\partial y}\right) + \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} = 0 \quad \text{(5.2)}$$

경계조건 (open boundary + shoreline(depth=0)):
$$F_n + gd\frac{\partial\zeta}{\partial n} = 0 \quad \text{(5.3)}$$
($n$=외향 법선). 전 경계점 이 BC 면 unknown 상수 남음 → **최대수심 경계점서 $\zeta=0$ 고정**. 2nd type (Dirichlet $\zeta$ given): nested model 용 (대모델 setup → nested 외경계).
> 매 iteration 후 setup 재계산 → 수심에 더함 (wave field 에 setup 효과 반영). 출력량 `SETUP`.

### B.2 §5.2.1 Problem definition (Eq 5.4-5.6)

$$\frac{\partial}{\partial x_k}\left(F_k + gd\frac{\partial\zeta}{\partial x_k}\right) = 0 \quad \text{(5.4)}$$
- **Neumann** (beach 항상): $F_n + gd\frac{\partial\zeta}{\partial n} = 0$ at boundary **(5.5)** (setup 가산상수 자유도)
- **Dirichlet**: $\zeta$ = given at boundary **(5.6)**
- **boundary-fitted, vertex-centered finite volume method**. 이하 $k \equiv gd$.

### B.3 Discretization (Eq 5.7-5.22) — 곡선격자 finite volume

물리영역 → $(\xi^1,\xi^2)$ 직사각 computational domain (dry 점 포함). 변환 관계 (summation convention):
$$\frac{\partial\varphi}{\partial x^\beta} = \frac{1}{\sqrt{g}}\frac{\partial}{\partial\xi^\gamma}(\sqrt{g}\,a^{(\gamma)}_\beta\varphi) \quad \text{(5.7)}$$
- contravariant base vector $\vec{a}^{(\alpha)} = \nabla\xi^\alpha$ **(5.8)**, Jacobian $\sqrt{g} = a^1_{(1)}a^2_{(2)} - a^2_{(1)}a^1_{(2)}$ **(5.9)**, covariant $\vec{a}_{(\alpha)} = \partial\vec{x}/\partial\xi^\alpha$ **(5.10)**
- contravariant ← covariant: $\sqrt{g}\vec{a}^{(1)} = (a^2_{(2)}, -a^1_{(2)})^T$ **(5.11)**, $\sqrt{g}\vec{a}^{(2)} = (-a^2_{(1)}, a^1_{(1)})^T$ **(5.12)**

(5.7)을 (5.5)에 적용:
$$\frac{1}{\sqrt{g}}\frac{\partial}{\partial\xi^\alpha}(\sqrt{g}\,\vec{a}^{(\alpha)}\cdot(k\nabla\zeta + \vec{F})) = 0 \quad \text{(5.13)}$$
> $\nabla\zeta$ 는 Cartesian $\vec{x}$ 미분 (ξ 아님).

Cell $\Omega$ (-1,0),(0,-1),(1,0),(0,1) 적분 (finite volume):
$$\int_{\Omega_\xi}\frac{\partial}{\partial\xi^\alpha}(\sqrt{g}\vec{a}^{(\alpha)}\cdot(k\nabla\zeta+\vec{F}))d\Omega_\xi \approx \sqrt{g}\vec{a}^{(1)}\cdot(k\nabla\zeta+F)|^{(1,0)}_{(-1,0)} + \sqrt{g}\vec{a}^{(2)}\cdot(k\nabla\zeta+\vec{F})|^{(0,1)}_{(0,-1)} \quad \text{(5.14)}$$
- 4 cell integration point (1,0),(0,1),(-1,0),(0,-1). Covariant base 중심차분: $\vec{a}_{(2)}|_{(0,1)} = \vec{x}_{(0,2)}-\vec{x}_{(0,0)}$ **(5.15)**, $\vec{a}_{(1)}|_{(1,0)} = \vec{x}_{(2,0)}-\vec{x}_{(0,0)}$ **(5.16)** (computational step=1)

**$\nabla\zeta$ 특별처리** (Cartesian 미분이나 모든 미분이 ξ 방향) → **integration path method** (Wesseling 2001): $\xi^1,\xi^2$ 2 독립방향 적분:
$$(\vec{x}_{2,0}-\vec{x}_{0,0})\nabla\zeta|_{(1,0)} = \zeta_{2,0}-\zeta_{0,0} \quad \text{(5.17)}$$
$$\tfrac{1}{2}((\vec{x}_{2,2}-\vec{x}_{2,-2})+(\vec{x}_{0,2}-\vec{x}_{0,-2}))\nabla\zeta|_{(1,0)} = \tfrac{1}{2}((\zeta_{2,2}-\zeta_{2,-2})+(\zeta_{0,2}-\zeta_{0,-2})) \quad \text{(5.18)}$$
선형계 해 → $\nabla\zeta|_{(1,0)}$ 를 이웃 $\zeta$ 로 (5.19), 계수 $\vec{c}^1, \vec{c}^2, C, \vec{c}_{(\alpha)}$ (5.20-5.22). (5.14)+(5.19) = 이산식 1행.

### B.4 BC 처리 (Eq 5.23-5.24)

- **Dirichlet**: 해당 행 = 0, 대각 = 1, BC 값을 RHS 에. (간단)
- **Neumann**: half-cell 적분 (Fig 5.2):
$$\int_{\Omega_\xi}\frac{\partial}{\partial\xi^\alpha}(\cdots)d\Omega_\xi \simeq \tfrac{1}{2}\sqrt{g}\vec{a}^{(1)}\cdot(k\nabla\zeta+\vec{F})|\cdots + \sqrt{g}\vec{a}^{(2)}\cdot(k\nabla\zeta+\vec{F})|^{(0,1)}_{(0,0)} \quad \text{(5.23)}$$
> 경계점 (0,0) 항 소멸 (Neumann). 경계서 $\nabla\zeta$ 평가 → one-sided integration path (5.24). Virtual cell (경계 cell 좌표 외삽)로 $\vec{a}_{(\alpha)}$ 확보.

### B.5 Dry points

- dry 점 자체: 행 + RHS = 0
- **wet-dry 인접**: wet (0,0) + dry (2,0) → (1,0)서 Neumann 가정 (기여 0). $\zeta_{(2,0)}$ 포함식엔 one-sided. Dry 행에 둘러싸인 wet 점은 $\nabla\zeta$ 정보 부족($\partial\zeta/\partial\xi^2$ 불가) → $\nabla\zeta = 0$.

### B.6 Matrix 구축 + §5.2.2 solver

- Integration point loop (점 (0,1) in $(i,j)$ = 점 (0,-1) in $(i-1,j)$ → 2 set만), **distribution** (계수 × factor → matrix).
- 행렬계:
$$Ax = f \quad \text{(5.25)}$$
- $A$ = discrete Poisson 연산자, $x$ = setup 근사, $f$ = BC + wave force. **direct addressing (dry 포함) → 차원 고정 $MXC\times MYC$**. **9-point stencil → 행당 9 비영 (diagonal 저장, NWKARR=9)**. Dry 행: 대각만 1, $x=f=0$.
- **Matrix 성질**: 내부 대칭 ($a_{i,j}=a_{j,i}$)이나 BC/dry 로 **비대칭** (Dirichlet known 미제거 + dry interface 대칭화 불명). 전 경계 Neumann → **singular** (해가 상수 자유도). Gauss elimination 시 bend 채워짐 → $2\times MXC+2$ vector 메모리 (큰 $MXC$ 부적합) → **iterative method**.
- **Solver**: 1D = trapezoidal rule. **2D = modified SOR (Botta-Ellenbroek 1985)** ([[swan-tech-ch6-iterative-solvers]]). BC: open boundary + shoreline 직전 격자 = wave force ↔ hydrostatic pressure gradient 평형, 최심 경계점 = setup 0. **Shoreline 은 setup 따라 이동**. Rectilinear·curvilinear 모두.

## C. SWAN 옵션 매핑

| Tech (PDF) | User cmd | 비고 |
|---|---|---|
| Ch 4 BC | `BOUNDSPEC` (JONSWAP/PM/Gauss/file) + `BOUNDNEST` | 2D spectrum 3 옵션 |
| Ch 4 IC | `INITIAL DEFAULT/ZERO/PAR/HOTSTART` | Kahma-Calkoen 1992 default |
| 5.1-5.25 2D setup | `SETUP` | Poisson FV, modified SOR |
| diagnostic tail | `QUANTITY ... PWTAIL` | $f^{-4}$ 또는 $f^{-5}$ |

## D. 한계

- (5.14)·(5.19)·(5.22)·(5.23)·(5.24): ASCII/truncated 다행식 → 구조 전사 (정밀식 swantech.pdf p.122-124).
- PDF 5.24 는 grep서 무번호로 보이나 website 5.24 (Neumann one-sided) 존재 — 본 노트 (5.24)로 표기 (경계 §B.4).
- §5.2.2 The iterative solver (node77)는 SOR 참조만 (상세는 Ch 6 [[swan-tech-ch6-iterative-solvers]]).

## E. 연결

- [[swan-tech-ch2-obstacles-diffraction-setup]] — §2.6 1D set-up (Eq 2.145-2.147, 2D 의 출발식)
- [[swan-tech-ch3-qc-curvilinear]] — §3.10 곡선좌표 (covariant/contravariant 공유)
- [[swan-tech-ch6-iterative-solvers]] — Ch 6 SIP/SOR (5.25 solver)
- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3 SIP (action balance solver, 동일 기법)
