---
title: "SWAN swantech Ch 3.2 Discretization — BSBT/SORDUP/Stelling-Leendertse + GSE + hybrid spectral + 음에너지 제거 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.2 Discretization, doc p.70-78 (Eq 3.1-3.15). References: Whitham 1974, Holthuijsen 2007, Rogers et al. 2002, Gear 1971, Stelling-Leendertse 1992, Booij-Holthuijsen 1987, WISE Group 2007, Tolman 1991."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.2 직접 read via pdftotext (식 번호 context-verified) + website_markdown node37-41.md LaTeX alt-text. 식 번호는 PDF 번호 체계 (online HTML은 GSE 계수·refraction 예시식을 추가 번호 매겨 hybrid scheme부터 +6 offset; 본 노트는 PDF 번호 사용). Eq 3.1-3.15 context-verified, GSE 계수/refraction 예시식은 PDF 무번호."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.1-3.15 + 계수 verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/source-analysis/swan-gse-correction.md
  - models/SWAN/source-analysis/swan-action-balance.md
---

# swantech Ch 3.2 Discretization — verified verbatim

> swantech.pdf (v41.51) §3.2 직접 read. [[swan-tech-ch2-governing-equations]] 의 action balance (Eq 2.18-2.19)를 **유한차분 이산화** — geographic 3 schemes (BSBT/SORDUP/Stelling-Leendertse) + GSE correction + spectral hybrid scheme + 음에너지 conservative elimination.
>
> **식 번호 주의**: Ch 3도 PDF↔online HTML offset (Eq 3.1-3.10 일치, hybrid scheme부터 HTML이 GSE 계수·refraction 예시식 추가번호 → +6). 본 노트는 **PDF 번호** 사용, GSE 계수식·refraction 예시식은 PDF 무번호.

## §3.1 설계 원칙 (node36, 서술)

SWAN 1993 (Holthuijsen·Booij·Ris, Booij 1999) 수치 설계 원칙:
- **nearshore + oceanic** 모두 (deep+shallow process, **flexible mesh curvilinear·triangular, 격자 20 m ~ 100 km** — 해저 세부 ~ hurricane wind). Cartesian/spherical 좌표
- 이산화는 **simple·robust·accurate·economical** → **finite difference + method of lines** (시간적분 ↔ 공간이산화 독립 선택)
- **fully implicit 시간적분** → Von Neumann 안정 (임의 time step). **sweeping algorithm** (causality rule 준수)
- limiter: action density limiter·frequency-dependent under-relaxation·refraction limiter·Patankar (이하 §3.7-3.8)

## 0. 시간 + 4D 이산화 (Eq 3.1-3.2)

Action balance (Eq 2.19) homogeneous part:
$$\frac{\partial N}{\partial t} + \frac{\partial c_x N}{\partial x} + \frac{\partial c_y N}{\partial y} + \frac{\partial c_\sigma N}{\partial \sigma} + \frac{\partial c_\theta N}{\partial \theta} \quad \text{(3.1)}$$

- 직사각 격자 ($\Delta x, \Delta y$ 일정), spectral bin ($\Delta\theta$ 일정 + $\Delta\sigma/\sigma$ 일정 → **logarithmic 주파수 분포**)
- counters: $1\le i\le M_x$, $1\le j\le M_y$, $1\le l\le M_\sigma$, $1\le m\le M_\theta$. 모든 변수($k, c_g, u$, 전파속도)는 $(i,j,l,m)$ 점에 위치
- **implicit Euler** 시간 이산화:

$$\frac{N^n - N^{n-1}}{\Delta t}\Big|_{i,j,l,m} + \frac{[c_x N]_{i+1/2}-[c_x N]_{i-1/2}}{\Delta x}\Big|^n + \frac{[c_y N]_{j+1/2}-[c_y N]_{j-1/2}}{\Delta y}\Big|^n + \frac{[c_\sigma N]_{l+1/2}-[c_\sigma N]_{l-1/2}}{\Delta\sigma}\Big|^n + \frac{[c_\theta N]_{m+1/2}-[c_\theta N]_{m-1/2}}{\Delta\theta}\Big|^n \quad \text{(3.2)}$$
> stationary 계산 시 첫 항 제거, $n$ = iteration level. 반정수 = bin 경계.

## 1. Geographic 이산화 — 3 schemes (Eq 3.3-3.13)

1차 upwind 은 fully monotone (spurious oscillation 없음)이나 numerically diffusive. 2 대안 (2차 SORDUP·Stelling-Leendertse)이 ocean/shelf 용 구현.

### 1.1 First-order upwind (BSBT)

Flux upwind 근사 ($c_x>0$ 예):
$$c_x N|_{i+1/2,j,l,m} = \begin{cases} c_x N|_{i,j,l,m}, & c_x|_{i,j,l,m} \ge 0 \\ c_x N|_{i+1,j,l,m}, & c_x|_{i,j,l,m} < 0 \end{cases} \quad \text{(3.3)}$$
(y 방향 동일 **(3.4)**)

First sweep ($c_x>0, c_y>0$) scheme:
$$\left(\frac{(c_x N)_i - (c_x N)_{i-1}}{\Delta x}\right)^n_{j,l,m} \quad \text{(3.5)},\qquad \left(\frac{(c_y N)_j - (c_y N)_{j-1}}{\Delta y}\right)^n_{i,l,m} \quad \text{(3.6)}$$

> **BSBT** = first-order Backward Space Backward Time (3.2+3.3+3.4). stationary·nonstationary 모두 가능. Unconditionally stable·monotone·compact 이나 cross-diffusion 최적 아님. Method of characteristics 유도 → **semi-Lagrangian** (energy flux 가 wave characteristic 따라 일정, Whitham 1974 pg.245 Eq 11.61 + Holthuijsen 2007 pg.200). **Flux conservative** (급변 해저 shoaling 필수). 상류점만으로 결정 → causality 보존.

### 1.2 SORDUP (stationary default)

2차 BDF (Gear 1971), $x,y$ 도함수 대체:
$$\left(\frac{3(c_x N)_i - 4(c_x N)_{i-1} + (c_x N)_{i-2}}{2\Delta x}\right)^n_{j,l,m} \quad \text{(3.7)}$$
(y 동일 **(3.8)**, Rogers 2002)
> 2차 공간 정확(1차 시간, 무관)·flux conservative(경험적)·**not monotone**. Causality 보존, BSBT보다 diffusion ↓, 비용 큰 차이 없음. **open/land boundary·obstacle 인접 2격자에선 BSBT로 회귀.**

### 1.3 Stelling-Leendertse (nonstationary default)

Cyclic scheme (Stelling-Leendertse 1992):
$$\left(\frac{10(c_x N)_i - 15(c_x N)_{i-1} + 6(c_x N)_{i-2} - (c_x N)_{i-3}}{6\Delta x}\right)^n_{j,l,m} + \left(\frac{(c_x N)_{i+1}-(c_x N)_{i-1}}{4\Delta x}\right)^{n-1}_{j,l,m} \quad \text{(3.9)}$$
(y 동일 **(3.10)**)
> 2차 시간·공간·unconditionally stable·causality·flux conservative(경험적). Diffusion 이 BSBT·SORDUP보다 **현저히 작음**. **boundary·obstacle 인접 3격자에선 BSBT로 회귀.** 단 무조건 안정이어도 **실용적 시간 제약**: Courant ≫ 1 시 wiggle 발생(저확산이라 억제 불가), 최대 허용 Courant ≈ 10 (fastest wave 기준, subjective, Rogers 2002).

## 2. Garden-Sprinkler Effect (GSE) correction (Eq 3.11-3.13)

S&L 의 확산이 매우 작아 장거리 전파 시 GSE 출현 (coarse spectral resolution, Booij-Holthuijsen 1987). Anisotropic diffusion 항 명시 추가 (spectral resolution + propagation time 의존). 본 위키 [[swan-gse-correction]] (SwanGSECorr.ftn90).

전파방향(wave ray) 따라:
$$D_{ss} = \frac{\Delta c_g^2 T}{12}\quad\text{(PDF 무번호)}$$
crest 따라(수직):
$$D_{nn} = \frac{c_g^2 \Delta\theta^2 T}{12}\quad\text{(PDF 무번호)}$$
- $\Delta c_g$ = 인접 주파수 군속도 차, $T$ = **wave age** (storm 생성 후 경과시간)

Cartesian 변환 (PDF 무번호): $D_{xx}=D_{ss}\cos^2\theta + D_{nn}\sin^2\theta$, $D_{yy}=D_{ss}\sin^2\theta + D_{nn}\cos^2\theta$, $D_{xy}=(D_{ss}-D_{nn})\cos\theta\sin\theta$. Eq 3.1 에 추가되는 항: $-D_{xx}\partial_{xx}N - 2D_{xy}\partial_{xy}N - D_{yy}\partial_{yy}N$ (PDF 무번호), 시간레벨 $n-1$ 2차 중심차분 (explicit, 빠름·조건부 안정).

**안정조건** (Rogers 2002):
$$Q = \frac{\max(D_{xx},D_{yy},D_{xy})\Delta t}{\min(\Delta x,\Delta y)^2} \le \frac{1}{2} \quad \text{(3.11)}$$
> GSE correction 으로 무조건 안정 advection → 조건부 안정 advection-diffusion. 실험상 $Q\le0.48$ 에서 불안정 없음. Ocean 은 $D_{nn}$ 지배:

$$Q = \frac{c_g^2 T\Delta t\Delta\theta^2}{12\Delta x^2} \quad \text{(3.12)}$$

상수 wave age $\overline{T}$ 근사 ($\overline{L}=c_g\overline{T}$ travel distance, $\mu=c_g\Delta t/\Delta x$ Courant):
$$Q = \frac{\overline{L}\mu\Delta\theta^2}{12\Delta x} \quad \text{(3.13)}$$
> Ocean: $\mu\approx1/2$, $\Delta\theta\sim10°$, $\overline{L}/\Delta x\sim200$ → $Q\le1/4$ 안정. **Shelf(regional)**: $\mu=\mathcal{O}(1)$ 이나 GSE 작음 → diffusion 사용 말 것. **Small(local)**: $\mu=\mathcal{O}(10\text{-}100)$, 보통 stationary + SORDUP(GSE 없음)/BSBT 사용.

## 3. Spectral 이산화 — hybrid central/upwind (Eq 3.14-3.15)

Spectral flux 는 1차 upwind 부적합 (blocking 주파수 근처 매우 diffusive). 중심차분은 unphysical oscillation. → **hybrid central/upwind** (parameter $\mu,\nu\in[0,1]$, 0=upwind / 1=central):

$$c_\sigma N|_{i,j,l+1/2,m} = \begin{cases}(1-\mu)\cdots & \text{shifting to higher frequencies} \\ \cdots & \text{shifting to lower frequencies}\end{cases} \quad \text{(3.14)}$$

$$c_\theta N|_{i,j,l,m+1/2} = \begin{cases}(1-\nu)\cdots & \text{counter-clockwise} \\ \cdots & \text{clockwise}\end{cases} \quad \text{(3.15)}$$

> Flux conservative (급변 해저 적합). **$\nu=1$ (central)** 은 flux conservative 이나 **pointwise 비보존** + checkerboard 문제. **$\nu=0$ (upwind)** 은 pointwise conservation (각 directional bin flux 일정) + causality 보존. 실용: 항상 $0\le\nu<1$.
>
> **SWAN 표준 $\nu=1/2$** — upwind보다 diffusion ↓이나 작은 wiggle 가능. 3 연속 전파속도 동부호일 때 asymmetric 근사 (refraction 예시식 PDF 무번호); zero-crossing(방향 불명)에선 central($\nu=0$ 처리). $\nu=1/2$ 는 downstream bin 이 에너지 받아 causality 위반 + pointwise 비보존이나, blocking 밖 broad spectrum에선 영향 미미.

## 4. 음에너지 conservative elimination (Tolman 1991, §3.2.4 — PDF 무번호 식)

Hybrid scheme ($\mu,\nu\ne0$)은 wiggle 발생 가능. 에너지 함유부에선 background level 위라 음수 안 되지만, **spectrum flank**(저주파 ~0.03 Hz 또는 spread 가장자리, zero-energy bin 인접)에서 음에너지 발생. Broad spectrum 은 평활 → 음에너지 작음. **Conservative elimination** (Tolman 1991): sweep 내 각 주파수의 음에너지 제거 + 해당 directional sector 양에너지를 상수배해 에너지 보존.

주파수 $f$, sweep 방향범위 $[\theta_1,\theta_2]$ (아래 식들은 **PDF 무번호** display 식 — HTML은 3.27-3.30 부여):
$$E(f,\theta) = E^+(f,\theta) + E^-(f,\theta)\quad(E^+>0, E^-<0)$$
$$E_{\text{tot}}(f) = \int_{\theta_1}^{\theta_2}E(f,\theta)\,d\theta,\qquad E^p_{\text{tot}}(f) = \int_{\theta_1}^{\theta_2}E^+(f,\theta)\,d\theta$$
$$\alpha(f) = \frac{E_{\text{tot}}(f)}{E^p_{\text{tot}}(f)} \le 1$$
> $E^-=0$ 설정 + 양에너지 $\times\alpha(f)$ → 주파수별 총에너지 보존.
>
> **Strict elimination** (예외): directional resolution 이 spreading 대비 coarse(spreading $<10°$ 를 $10°$ bin 분산) → 음에너지 합 > 양에너지 → $\alpha<0$ → 보존 무의미 → 음에너지만 제거, 양에너지 유지. (이 경우 hybrid scheme 자체 부정확하므로 악화 아님.) **전형적 field case: 95%+ conservative, 5% 미만 strict (허용).**

## 5. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §3.2) | User cmd | 비고 |
|---|---|---|
| 3.3-3.6 BSBT | `PROP BSBT` | first-order, semi-Lagrangian, robust |
| 3.7-3.8 SORDUP | `PROP SORDUP` (또는 default stationary) | 2차 BDF, boundary 인접 2격자 BSBT |
| 3.9-3.10 Stelling-Leendertse | `PROP SL` (default nonstationary) | cyclic, Courant ≤ 10, boundary 3격자 BSBT |
| 3.11-3.13 GSE | `GSE [waveage]` | S&L 장거리 swell 시, $\overline{T}$ wave age |
| 3.14-3.15 hybrid spectral | `NUMERIC ... [cdd] [css]` | $\nu, \mu$ central/upwind blend (default 0.5) |
| §3.2.4 음에너지 제거 | (internal, Tolman 1991) | conservative + strict |

## 6. 한계

- GSE 계수식(D_ss·D_nn·D_xx 등)·refraction 예시식(3.22-3.26 HTML)·중심차분 보조식: **PDF 무번호** display 식 → 본 노트 무번호 인용 (HTML은 별도 번호 부여).
- hybrid scheme(3.14-3.15)의 cases 본문: pdftotext + HTML alt-text 모두 truncated("$\cdots$") → 정밀 식은 swantech.pdf p.76-77 직접 또는 SwanCompUnstruc/source-analysis.
- §3.2.1 도입 paragraph(numerical diffusion 관점, node39)는 정성 서술 — 본 노트 §1 intro에 요약.

## 7. 연결

- [[swan-tech-ch2-governing-equations]] — Eq 2.18-2.19 action balance (이산화 대상)
- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3-3.7 solution algorithm + sweeping + stopping + action limiter
- [[swan-gse-correction]] — SwanGSECorr.ftn90 (GSE D_ss/D_nn 구현)
- [[swan-action-balance]] — action balance source-analysis
- [[swan-unstructured-time-step]] — §8.3 multidimensional BSBT (unstructured)
