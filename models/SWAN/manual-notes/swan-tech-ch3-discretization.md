---
title: "SWAN swantech Ch 3.2 Discretization — BSBT/SORDUP/Stelling-Leendertse + GSE + hybrid spectral + 음에너지 제거 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.2 Discretization, doc p.70-78 (Eq 3.1-3.15). References: Whitham 1974, Holthuijsen 2007, Rogers et al. 2002, Gear 1971, Stelling-Leendertse 1992, Booij-Holthuijsen 1987, WISE Group 2007, Tolman 1991."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.2 직접 read via pdftotext (식 번호 context-verified) + website_markdown node37-41.md LaTeX alt-text. 식 번호는 PDF 번호 체계 (online HTML은 GSE 계수·refraction 예시식을 추가 번호 매겨 hybrid scheme부터 +6 offset; 본 노트는 PDF 번호 사용). Eq 3.1-3.15 context-verified, GSE 계수/refraction 예시식은 PDF 무번호.; 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
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

> swantech.pdf (v41.51) §3.2 직접 read. [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) 의 action balance (Eq 2.18-2.19)를 **유한차분 이산화** — geographic 3 schemes (BSBT/SORDUP/Stelling-Leendertse) + GSE correction + spectral hybrid scheme + 음에너지 conservative elimination.
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
$$\left(\frac{10(c_x N)_i - 15(c_x N)_{i-1} + 6(c_x N)_{i-2} - (c_x N)_{i-3}}{12\Delta x}\right)^n_{j,l,m} + \left(\frac{(c_x N)_{i+1}-(c_x N)_{i-1}}{4\Delta x}\right)^{n-1}_{j,l,m} \quad \text{(3.9)}$$
(y 동일 **(3.10)**)
> 2차 시간·공간·unconditionally stable·causality·flux conservative(경험적). Diffusion 이 BSBT·SORDUP보다 **현저히 작음**. **boundary·obstacle 인접 3격자에선 BSBT로 회귀.** 단 무조건 안정이어도 **실용적 시간 제약**: Courant ≫ 1 시 wiggle 발생(저확산이라 억제 불가), 최대 허용 Courant ≈ 10 (fastest wave 기준, subjective, Rogers 2002).

## 2. Garden-Sprinkler Effect (GSE) correction (Eq 3.11-3.13)

S&L 의 확산이 매우 작아 장거리 전파 시 GSE 출현 (coarse spectral resolution, Booij-Holthuijsen 1987). Anisotropic diffusion 항 명시 추가 (spectral resolution + propagation time 의존). 본 위키 [swan-gse-correction](../source-analysis/swan-gse-correction.md) (SwanGSECorr.ftn90).

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

$$c_\sigma N\big\vert_{i,j,l+1/2,m}=\begin{cases}(1-0.5\mu)c_\sigma N\big\vert_{i,j,l,m}+0.5\mu c_\sigma N\big\vert_{i,j,l+1,m},&\text{if shifting to higher frequencies}\\(1-0.5\mu)c_\sigma N\big\vert_{i,j,l+1,m}+0.5\mu c_\sigma N\big\vert_{i,j,l,m},&\text{if shifting to lower frequencies}\end{cases} \quad \text{(3.14)}$$

(swantech PDF 84쪽 / 인쇄 76쪽; R1:TN-058)

$$c_\theta N\big\vert_{i,j,l,m+1/2}=\begin{cases}(1-0.5\nu)c_\theta N\big\vert_{i,j,l,m}+0.5\nu c_\theta N\big\vert_{i,j,l,m+1},&\text{if counter-clockwise}\\(1-0.5\nu)c_\theta N\big\vert_{i,j,l,m+1}+0.5\nu c_\theta N\big\vert_{i,j,l,m},&\text{if clockwise}\end{cases} \quad \text{(3.15)}$$

(swantech PDF 84쪽 / 인쇄 76쪽; R1:TN-059)

> Flux conservative (급변 해저 적합). **$\nu=1$ (central)** 은 flux conservative 이나 **pointwise 비보존** + checkerboard 문제. **$\nu=0$ (upwind)** 은 pointwise conservation (각 directional bin flux 일정) + causality 보존. 실용: 항상 $0\le\nu<1$.
>
> **SWAN 표준 $\nu=1/2$** — upwind보다 diffusion ↓이나 작은 wiggle 가능. 3 연속 전파속도 동부호일 때 asymmetric 근사 (refraction 예시식 PDF 무번호). 문서 기호로 중심차분은 $\nu=1$이다. 코드에서는 `PNUMS(6)=1-\nu`이다. 부호 전환 분기는 매개변수 값을 바꾸지 않고 중심차분 계수를 직접 조립한다. (swantech PDF 84–85쪽 / 인쇄 76–77쪽; `src/swancom5.ftn:3988` `PCD1 = PNH * C1`; R1:TN-059·TN-063)

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
- 식 (3.14)·(3.15)의 문서 매개변수와 코드 매개변수는 $\mu=1-\mathrm{PNUMS}(7)$, $\nu=1-\mathrm{PNUMS}(6)$로 대응한다. (swantech PDF 84쪽 / 인쇄 76쪽; `src/swancom5.ftn:3290–3292` `PNH = 1. / (2. * DS)`; `PN1 =  (1. - PNUMS(7) ) * PNH`; `PN2 =  (1. + PNUMS(7) ) * PNH`; R1:TN-058·TN-059)
- §3.2.1 도입 paragraph(numerical diffusion 관점, node39)는 정성 서술 — 본 노트 §1 intro에 요약.

## 7. 연결

- [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) — Eq 2.18-2.19 action balance (이산화 대상)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3-3.7 solution algorithm + sweeping + stopping + action limiter
- [swan-gse-correction](../source-analysis/swan-gse-correction.md) — SwanGSECorr.ftn90 (GSE D_ss/D_nn 구현)
- [swan-action-balance](swan-action-balance.md) — 작용수지식과 원천항을 정리한 매뉴얼 노트이다. [10-13 전수 검증 정정]
- [swan-unstructured-time-step](../source-analysis/swan-unstructured-time-step.md) — §8.3 multidimensional BSBT (unstructured)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R1](../../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#5-차이-결론), [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R1:TN-044 | 문서 식 (3.9) | swantech PDF 81쪽 / 인쇄 73쪽, (3.9): $[10(c_xN)_i-15(c_xN)_{i-1}+6(c_xN)_{i-2}-(c_xN)_{i-3}]^n/(12\Delta x)+[(c_xN)_{i+1}-(c_xN)_{i-1}]^{n-1}/(4\Delta x)$. | `src/swancom5.ftn:2940` `FXY1 = 0.83333*(RDX(1)+RDX(2)) * CAX(ID,IS,1)`<br>`src/swancom5.ftn:2964–2965` `+(0.25*RDX(1)) * (CAX1(ID,IS,2) * AC1(ID,IS,IND2)` | C 문서 누락 | 식 구조와 부호는 같다. 코드는 $10/12$, $1/12$를 각각 `0.83333`, `0.08333`으로 절단한다. C는 swantech §3.2.1이 이 소수 계수 절단을 적지 않는 점이다. |
| R1:TN-045 | 문서 식 (3.10) | swantech PDF 81쪽 / 인쇄 73쪽, (3.10): $[10(c_yN)_j-15(c_yN)_{j-1}+6(c_yN)_{j-2}-(c_yN)_{j-3}]^n/(12\Delta y)+[(c_yN)_{j+1}-(c_yN)_{j-1}]^{n-1}/(4\Delta y)$. | `src/swancom5.ftn:2941` `&         + 0.83333*(RDY(1)+RDY(2)) * CAY(ID,IS,1)` | C 문서 누락 | 코드의 y 방향 식도 R1:TN-044와 같은 소수 계수 절단을 사용한다. C는 swantech §3.2.1의 이 절단값 누락이다. |
| R1:TN-055 | GSE 교차차분 | swantech PDF 82쪽 / 인쇄 74쪽, 번호 없음: $D_{xy}(N_{i,j}-N_{i-1,j}-N_{i,j-1}+N_{i-1,j-1})^{n-1}/(\Delta x\Delta y)$. | `src/swancom5.ftn:3003–3008` `!           old method`; `!           new method`; `D12AC = 0.25*(AC1(ID,IS,IND12) - AC1(ID,IS,IND11)`; `&                   -AC1(ID,IS,IND13) + AC1(ID,IS,IND10))` | B 문서 오기 | 해석: 활성 식은 네 대각 이웃의 중심 교차차분이다. 문서는 주석으로 남은 구식을 적는다. 구식도 해당 절점에서 2차 중심차분이 아니다. 의도 변경 주석이 있으므로 코드 결함으로 판정하지 않는다. |
| R1:TN-056 | 문서 식 (3.11)·(3.12)·(3.13) | swantech PDF 82–83쪽 / 인쇄 74–75쪽, (3.11): $Q=\max(D_{xx},D_{yy},D_{xy})\Delta t/\min(\Delta x,\Delta y)^2\le1/2$; (3.12): $Q=c_g^2T\Delta t\Delta\theta^2/(12\Delta x^2)$; (3.13): $Q=\bar L\mu\Delta\theta^2/(12\Delta x)$; $\bar L=c_g\bar T,\ \mu=c_g\Delta t/\Delta x$. | `src/swancom5.ftn:2916` `IF (WAVAGE.GT.0.) THEN` | H 코드 대조 대상 아님 | 문서는 안정성 추정과 실험 결과 $Q\le0.48$을 제시한다. 이 식들은 실행 중의 시간 간격 조절식으로 제시되지 않았다. |
| R1:TN-057 | GSE 안정성·규모별 권고 | swantech PDF 83쪽 / 인쇄 75쪽, §3.2.2 및 번호 없는 권고: $\mu\approx1/2,\ Q\le1/4,\ \Delta\theta\sim10^\circ,\ \bar L/\Delta x\sim200$; 지역 $\mu=\mathcal O(1)$; 국소 $\mathcal O(10-100)$. | `src/swanmain.ftn:1184` `WAVAGE = 0.` | H 코드 대조 대상 아님 | 적용 규모별 예시와 기법 선택 권고이다. GSE 보정은 기본으로 켜지지 않는다. |
| R1:TN-058 | 문서 식 (3.14) | swantech PDF 84쪽 / 인쇄 76쪽, (3.14): $c_\sigma N\big\vert_{i,j,l+1/2,m}=\begin{cases}(1-0.5\mu)c_\sigma N\big\vert_{i,j,l,m}+0.5\mu c_\sigma N\big\vert_{i,j,l+1,m},&\text{if shifting to higher frequencies}\\(1-0.5\mu)c_\sigma N\big\vert_{i,j,l+1,m}+0.5\mu c_\sigma N\big\vert_{i,j,l,m},&\text{if shifting to lower frequencies}\end{cases}$. | `src/swancom5.ftn:3290–3292` `PNH = 1. / (2. * DS)`; `PN1 =  (1. - PNUMS(7) ) * PNH`; `PN2 =  (1. + PNUMS(7) ) * PNH` | F 표기 차이 | 해석: $\mu=1-\mathrm{PNUMS}(7)$이면 풍상 계수 $(1+\mathrm{PNUMS}(7))/2=1-\mu/2$이다. 코드 기본 대입은 `src/swanmain.ftn:1234`의 `PNUMS(7)  = 0.5`이다. |
| R1:TN-059 | 문서 식 (3.15) | swantech PDF 84쪽 / 인쇄 76쪽, (3.15): $c_\theta N\big\vert_{i,j,l,m+1/2}=\begin{cases}(1-0.5\nu)c_\theta N\big\vert_{i,j,l,m}+0.5\nu c_\theta N\big\vert_{i,j,l,m+1},&\text{if counter-clockwise}\\(1-0.5\nu)c_\theta N\big\vert_{i,j,l,m+1}+0.5\nu c_\theta N\big\vert_{i,j,l,m},&\text{if clockwise}\end{cases}$. | `src/swancom5.ftn:3946–3948` `PNH = 1. / (2. * DD)`; `PN1 =  (1. - PNUMS(6) ) * PNH`; `PN2 =  (1. + PNUMS(6) ) * PNH` | F 표기 차이 | 해석: $\nu=1-\mathrm{PNUMS}(6)$이다. 기본 대입은 `src/swanmain.ftn:1232`의 `PNUMS(6)  = 0.5`이다. |
| R1:TN-063 | 부호 전환의 중심차분 | swantech PDF 85쪽 / 인쇄 77쪽: “central differences ($\nu=0$)”. | `src/swancom5.ftn:3988` `PCD1 = PNH * C1` | B 문서 오기 | 해석: 이 문장의 $\nu=0$은 (3.15)의 정의와 모순된다. 문서의 중심차분 값은 $\nu=1$이어야 한다. 코드의 `PNUMS(6)=0`과 혼동하면 안 된다. |
| R1:TN-066 | 음수 에너지의 사례 비율 | swantech PDF 87쪽 / 인쇄 79쪽: “over 95%”; “less than 5%”. | — | H 코드 대조 대상 아님 | 문서는 전형적 현장 사례의 발생 비율을 말한다. 허용 상한이나 정지 조건이 아니다. |
| R1:TC-018 | 선택적 방향 플럭스 제한기 SWFLXD | — | `src/swancom5.ftn:5308,5352–5362,5417` `XKAP = PNUMS(6)`; `RAP = (ACT2-ACT0+1.E-12)/(ACT0-ACT1+1.E-12)`; `FACT  = MIN( 2., 0.5*(1.+XKAP)*RAP + 0.5*(1.-XKAP) )`; `XLIMP = MAX( 0., MIN(2.*RAP,FACT) )`; `DFCOR = 0.5*(CAP*XLIMP*(ACT0-ACT1)-CAN*XLIMN*(ACT3-ACT2))` | C 문서 누락 | C는 swantech §3.2의 선형 혼합 플럭스 설명에 SWFLXD의 비선형 기울기 제한식이 없는 점이다. `IF ( IREFR.NE.0 ) THEN` 안의 `ELSE IF ( PROPFL.EQ.1 ) THEN`에서 호출한다. 비율의 분자와 분모에 각각 $10^{-12}$를 더한다. 방향 수송에 적용하는 선택 경로이다. |
| R1:TC-019 | 공간 stencil의 국소 차수 변경 | — | `src/swancom1.ftn:3099–3103,3134–3139` `IF (IC.LE.3) THEN`; `PROPSL = 0`; `IF (PROPSC.GT.1) PROPSL = 1`; `IF (COMPDA(KCGRD(IC),JDP2).LE.DEPMIN) PROPSL = 1`; `IF (COMPDA(KCGRD(IC),JDP1).LE.DEPMIN) PROPSL = 1` | C 문서 누락 | 고차 stencil의 영역 이탈·건조점에서 국소 BSBT로 바꾼다. 기본 세 점 자체가 없으면 공간 전파를 끄는 분기도 있다. 비정상 경로는 이전 시간 수심도 검사한다. |
| R1:TC-020 | 기법·시간 모드의 불일치 검사 | swanuse PDF 92쪽 / 인쇄 84쪽의 PROP 설명. | `src/swanmain.ftn:6564–6568` `IF (PROPSC.EQ.2 .AND. NSTATC.GT.0) THEN`; `CALL MSGERR (3, 'SORDUP scheme only in stationary run')`; `IF (PROPSC.EQ.3 .AND. NSTATC.EQ.0) THEN`; `CALL MSGERR (3, 'S&L scheme not in stationary run')` | C 문서 누락 | SORDUP의 정상 모드와 S&L의 비정상 모드 구분은 swanuse에도 있다. C는 swantech의 기법 설명에 모드 불일치 시 오류 수준 3을 보고하는 입력 검사 절차가 없는 점이다. 두 조건은 `IF (PROPSC.EQ.2 .AND. NSTATC.GT.0) THEN`과 `IF (PROPSC.EQ.3 .AND. NSTATC.EQ.0) THEN`이다. |
| R1:TC-021 | 정규 격자와 일치하는 스펙트럼 방향의 작은 이동 | — | `src/swanpre1.ftn:4709–4713` `IF (OPTG.EQ.1) THEN`; `IF (ABS(MODULO(SPCDIR(ID,1)-ALPC+0.25*PI ,0.5*PI)-0.25*PI)`; `.LT. 1.E-6) THEN`; `SPCDIR(ID,1) = OLDDIR + 2.E-6` | C 문서 누락 | 정규 격자 방향과 거의 일치하는 방향 bin을 $2\times10^{-6}$ rad 이동한다. 등간격 방향 격자의 초기 구성 뒤에 적용하는 예외이다. |
| R1:TC-022 | 명시 주파수 수송과 CFL에 따른 bin 제거 | swanuse PDF 141쪽 / 인쇄 133쪽의 `SIGEXpl [css] [cfl]`; `src/swancom1.ftn:5437–5461`의 호출 조건. | `src/swancom1.ftn:5451–5461` `ELSE IF ( INT(PNUMS(8)) .EQ. 2 ) THEN`; `CALL STRSSB`<br>`src/swancom5.ftn:3644,3670,3674,3726,3730` `CFLMAX = PNUMS(19)`; `IF ( CFLCEN .GT. CFLMAX ) THEN`; `ANYBLK(ID,IS) = .TRUE.`; `FSA  = ( FRGHT - FLEFT ) / DS`; `IMATRA(ID,IS) = IMATRA(ID,IS) - FSA` | C 문서 누락 | SIGEXpl 선택은 swanuse PDF 141 명령 도식에 있다. C는 swantech §3.2·§3.3에 CFL에 따른 bin 제거의 구현 조건이 없는 점이다. `PNUMS(19)=0.5*sqrt(2.)`가 기본 상한이다. `IF ( CFLCEN .GT. CFLMAX ) THEN`이면 ANYBLK를 켠다. SOLMT1은 해당 행의 대각을 1로, 우변과 방향 이웃 계수를 0으로 둔다. 이 의도된 제거와 R1:TC-023의 분모 결함 후보를 구분한다. |
| R1:TC-023 | 명시 주파수 CFL 분모의 기하학적 부호 | — | `src/swancom5.ftn:3656–3664` `CAXCEN = ABS ( CAX(ID,IS,1) )`; `CAYCEN = ABS ( CAY(ID,IS,1) )`; `TX     = RDX(1) * CAXCEN + RDX(2) * CAXCEN`; `TY     = RDY(1) * CAYCEN + RDY(2) * CAYCEN`; `CFLCEN = TS / MAX( 1.E-20 , ( TX + TY ) )` | E 코드 결함 후보 (중간) | STRSSB의 CFL 공간 분모는 속도에만 절댓값을 적용한다. 역기저의 부호가 다른 sweep에서는 공간 전달률이 상쇄될 수 있다. 호출 조건은 `IF ( (DYNDEP .OR. ICUR.EQ.1) .AND. ITFRE.NE.0 ) THEN` 안의 `ELSE IF ( INT(PNUMS(8)) .EQ. 2 ) THEN`이다. 이 E 중간 후보는 명시 주파수 경로에 한정한다. 기본 음해법에는 적용되지 않는다. |
| R1:TC-025 | 음수 제거 비율의 작은 분모 보호 | — | `src/swancom1.ftn:8303–8304` `IF ( ATOTP .LT. 1.E-15 ) ATOTP = 1.E-15`; `FACTOR = ATOT / ATOTP` | C 문서 누락 | `IF (NEGVAL) THEN` 안에서 양의 작용밀도 합이 $10^{-15}$보다 작으면 분모를 올린다. 이후 `IF ( FACTOR .GE. 0. ) THEN`인 경우 양의 밀도를 재조정한다. 이 작은 분모 조건에서는 R1:TN-064의 엄밀한 총량 보존 비율과 달라진다. C는 swantech §3.2.4의 보존적 제거식에 이 보호 조건이 없는 점이다. |
| R7:H-1331 | SORDUP 단순화·일관성 | `website/modifications/modifications.htm:1331` `The SORDUP scheme is made more simpler and more consistent.` | `src/swancom5.ftn:1360` `!  Further still, implementation of the upwind scheme in versions such as 40.41 and 40.51 used sweeping to                           40.59` | H 코드 대조 대상 아님 | 코드 구조의 품질 평가이다. 현행 중앙 차분은 R7:H-1223에서 판정한다. |
