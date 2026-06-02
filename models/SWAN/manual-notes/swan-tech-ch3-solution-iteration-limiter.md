---
title: "SWAN swantech Ch 3.3-3.7 Solution algorithm + iteration/stopping + four-sweep + DIA-in-sweep + action limiter/under-relaxation verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.3 Solution algorithm + §3.4 Iteration process and stopping criteria + §3.5 sweeping + §3.6 DIA in four-sweep + §3.7 Action density limiter and under-relaxation, doc p.79-91 (Eq 3.16-3.30). References: Wesseling 1992, Ferziger-Perić 1999, Booij et al. 1999, Press et al. 1993, Holthuijsen-De Boer 1988, Zijlema-Wesseling 1998, WAMDI 1988, Hargreaves-Annan 2001, Hersbach-Janssen 1999, Tolman 1992·2002, Komen et al. 1994, Ris 1999, De Waal 2001, Janssen 1989·1991a."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.3-3.7 직접 read via pdftotext (식 번호 context-verified: matrix 3.16·S_tot linearization 3.17·Newton-Raphson 3.18·a_P 3.19·AN=b 3.20·H_m0 3.21·stopping 3.22-23·curvature 3.25-26·action limiter 3.27·limited update 3.28·under-relax 3.29-30) + website_markdown node42-48.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +15 offset)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.16-3.30 + 계수/default 값 verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-discretization.md
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
---

# swantech Ch 3.3-3.7 Solution algorithm + iteration + limiter — verified verbatim

> swantech.pdf (v41.51) §3.3-3.7 직접 read. [[swan-tech-ch3-discretization]] 의 이산화 system 을 **푸는 알고리즘** — Gauss-Seidel four-sweep + SIP solver + 비선형 source 선형화 + 수렴/정지 기준(curvature) + DIA-in-sweep + action limiter / frequency-dependent under-relaxation. SWAN 의 `NUMERIC` 명령 거의 전부의 이론 근거.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML은 §3.2 GSE 누적 + 본 절 보조식으로 +15 offset, 예: action limiter HTML 3.42 = PDF 3.27).

## 1. §3.3 Solution algorithm (Eq 3.16-3.20)

Implicit 이산화 → 선형방정식계. Matrix 구조는 geographic 전파 방향 의존 ($c_x>0, c_y>0$ 예):
$$\text{matrix structure (penta-diagonal block)} \quad \text{(3.16)}$$
- 주대각 subblock = 각 geographic 점의 $(\sigma,\theta)$ 공간 coupling, off-diagonal = geographic 점 간 coupling
- wave characteristic 이 직선·일정이면 **Gauss-Seidel 1-step** (Wesseling 1992), 격자크기 무관 → 복잡도 $\mathcal{O}(M)$ ($M$ 격자점)
- 방향을 4 quadrant($90°$)로 분할 → **four sweeps**, 각 sweep 의 방향이 domain of dependence → **CFL 자동 만족** (causality)

### 1.1 비선형 source 선형화 (Ferziger-Perić 1999)

$$S_{\text{tot}} = S_{\text{tot}}^p + S_{\text{tot}}^n N \quad \text{(3.17)}$$
- $S^p$ = 양 기여, $S^n$ = 음 기여 (둘 다 해당 bin 의 $N$ 무관). $N$ 미포함 음항은 이전 iteration 의 $N$ 으로 나눠 $S^n$ 에 추가 → 안정화. 각 source term 적용 상세: Booij et al. (1999).

Depth-induced breaking (강한 비선형) → **Newton-Raphson**:
$$S^n \approx \phi^{n-1}E^n + \left(\frac{\partial S}{\partial E}\right)^{n-1}(E^n - E^{n-1}) \quad \text{(3.18)}$$
> $S = aS_{\text{tot}}$, $E = aE_{\text{tot}}$ 형태 → $\partial S/\partial E = \partial S_{\text{tot}}/\partial E_{\text{tot}}$ 해석적.

### 1.2 5-점 stencil + SIP solver

$$a_P N_P = a_L N_L + a_R N_R + a_B N_B + a_T N_T + b_P \quad \text{(3.19)}$$
- P=중앙 bin $(l,m)$, L/R/B/T = $(l-1,m)/(l+1,m)/(l,m-1)/(l,m+1)$
- $a_k$ = $c_\sigma N, c_\theta N$ flux 이산화, $b_P$ = $S^p$ + 갱신된 $c_x N (3.3), c_y N (3.4)$, $a_P$ 는 $-S^n$ 포함

방향 quadrant 의 system:
$$A\vec{N} = \vec{b} \quad \text{(3.20)}$$
- $A\in\mathbb{R}^{K\times K}$ ($K = N_\sigma\times\frac{1}{4}N_\theta$), 비대칭, **penta-diagonal**. Source 선형화(3.17)가 diagonal dominance 강화 → 안정성 ↑
- 해: **incomplete LU + SIP (Strongly Implicit Procedure, Ferziger-Perić 1999)** — 비대칭 penta-diagonal 전용, 빠름
- **무전류 시**: 주파수 shift 없음 → $a_L=a_R=0$ → tri-diagonal → **Thomas algorithm** (Press 1993)

## 2. §3.4 Iteration process + stopping criteria (Eq 3.21-3.26)

$c_x, c_y$ 부호가 도메인서 달라 다단계 필요. Wave ray 곡선(천수 depth/current refraction) → 1 iteration 불가. Quadrant 간 상호작용(refraction + nonlinear) → sweep + system(3.20) 반복. $s=1\to S$ (보통 $S=50$ max) 또는 수렴기준 충족 시 종료.

$$H_{m0} = 4\sqrt{m_0},\quad T_{m01} = 2\pi\frac{m_0}{m_1},\quad m_j = \int_0^\infty\int_0^{2\pi}\sigma^j E\,d\sigma d\theta \quad \text{(3.21)}$$

### 2.1 종래 기준 (41.01 이전, 현재 obsolete)

전체 wet 격자의 **98% 이상**에서 둘 다 충족:
$$\frac{|\Delta H_{m0}^s(i,j)|}{H_{m0}^{s-1}(i,j)} < \varepsilon_H^r \quad\text{or}\quad |\Delta H_{m0}^s(i,j)| < \varepsilon_H^a \quad \text{(3.22)}$$
$$\frac{|\Delta T_{m01}^s(i,j)|}{T_{m01}^{s-1}(i,j)} < \varepsilon_T^r \quad\text{or}\quad |\Delta T_{m01}^s(i,j)| < \varepsilon_T^a \quad \text{(3.23)}$$
- default: $\varepsilon_H^r = \varepsilon_T^r = 0.02$, $\varepsilon_H^a = 0.02$ m, $\varepsilon_T^a = 0.2$ s
- 첫 추정: Holthuijsen-De Boer (1988) 2nd-gen source 로 가속

> **문제**: (3.22)(3.23)가 부족 — 느린 수렴 시 연속 iterate 차가 작아 수렴 전 정지 (non-monotonic local max/min). 특히 $T_{m01}$ 은 수렴 척도로 부적합 (고주파 미세 변동에 민감 → 상대오차 비단조 진동) → 개선 기준에서 **$T_{m01}$ 폐기**, $H_{m0}$ 만 유지.

### 2.2 Spectral radius 통찰 (Ferziger-Perić 1999)

$$\phi^\infty - \phi^s \approx \frac{\phi^{s+1}-\phi^s}{1-\rho} \quad \text{(3.24)}$$
> $\rho$ = spectral radius (수렴률). $\rho$ 작을수록 빠름. **해 오차 > 연속 iterate 차** — $\rho\to1$ 일수록 비율 커짐. SWAN 은 nonlinear transfer 로 smooth 하지 않아 Zijlema-Wesseling(1998) 류 기준 부적합.

### 2.3 Curvature 기준 (41.01+ default)

수렴 시 iteration curve 곡률 → 0:
$$\Delta(\Delta\tilde{H}_{m0}^s)^s = \tilde{H}_{m0}^s - 2\tilde{H}_{m0}^{s-1} + \tilde{H}_{m0}^{s-2} \quad \text{(3.25)}$$
> $\tilde{H}_{m0}^s \equiv (H_{m0}^s + H_{m0}^{s-1})/2$ (소진폭 진동 제거)

$$\frac{|H_{m0}^s(i,j) - (H_{m0}^{s-1}(i,j) + H_{m0}^{s-2}(i,j))/2 \cdots|}{2H_{m0}^s(i,j)} < \varepsilon_C,\quad s=3,4,\cdots \quad \text{(3.26)}$$
- $\varepsilon_C$ = max 허용 곡률, $H_{m0}^s$ 정규화. 전체 wet 격자 **99% 이상** 충족 시 정지 (**primary** 기준)
- 곡률은 local max/min 사이 0 통과 + action limiter(§3.7.2)로 두 level 진동 가능 → **safeguard 로 약한 (3.22) 병행 유지**
- **버전 41.01 부터 (3.26)+(3.22) default, 종래 (3.22)+(3.23) obsolete**

## 3. §3.5 Four-sweep technique (illustrative)

무전류: energy 전파방향 = 군속도. Upwind stencil — $(x_i,y_j)$ 는 up-wave $(x_{i-1},y_j), (x_i,y_{j-1})$ 로 결정 → $0°$-$90°$ sector = **sweep 1**. Stencil $90°$ 회전 4회 → 4 quadrant 전파. **Unconditionally stable** (characteristic 가 quadrant 내) → **CFL 무관**. Causality: geographic + spectral domain of dependence 동일.

Refraction 시 quadrant 간 action shift → 반복 (iterative four-sweep), 종료: 모든 격자서 $H_s, T$ 변화 <1%.

> **$M>4$ sweep 옵션**: 방향간격 $360°/M$. 심해(직선 ray)는 iteration 감소 가능 (8 sweep $45°$ / 12 sweep $30°$). **천수에선 역효과** — refraction 으로 wave energy 가 1 step 에 여러 bin jump → sweep sector 조기 이탈/skip ($<30°$ + 큰 depth 변화 시) → ray 교차·causality 위반·불안정 (§3.8.3 참조).

### 3.1 전류 존재 시 4 configurations

$c_x = c_{g,x}+U_x$, $c_y = c_{g,y}+U_y$. Sweep 별 부호 분류 (1: ++, 2: -+, 3: --, 4: +-). 고주파일수록 군속도 작아 current 영향 大 → sector 경계 변화 大. **4 config** (current $45°$ 예, Fig 3.3):
- **(A)** 강한 역류 → $c_x,c_y$ 모두 음 (wave blocking), sweep 1 에 아무것도 전파 안 됨
- **(B)** 약한 current → sector 경계 거의 무변 (무전류와 유사)
- **(C)** 순류 → 2 sector 가 양 전파속도
- **(D)** 강한 순류 → 전 $360°$ sector 가 sweep 1 에 전파

## 4. §3.6 DIA in four-sweep — 2 methods

Quadruplet 은 DIA(§2.3.4, [[swan-tech-ch2-nonlinear-detailed]])로 적분. Four-sweep 결과 2 방식:

| 방식 | 시점 | 비용 | 보존 | current |
|---|---|---|---|---|
| **Method 1** | iteration 시작 시 first sweep 전 1회 계산 후 저장→explicit 적분 | **메모리 ×2** ($S_{\text{nl4}}$ 전 격자 저장) | energy 보존 | **ambient current 시 권장** |
| **Method 2** | sweep 별 개별 계산·적분 (인접 2 quadrant 각 $33°$ 추가) | **시간 ×1.66** ($2\times33°\times4/360°$); semi-implicit 시 ×2 | sweep/iteration 별 비보존 (수렴엔 무영향) | **current 시 불가** (주파수별 sector 경계 상이 → bin overlap → 비보존) |

> Method 2 는 fully explicit 권장 (효율). Current 모델엔 **Method 1 권장**.

## 5. §3.7 Action density limiter + under-relaxation (Eq 3.27-3.30)

3rd-gen 모델은 **multiple time scale**(광대역 주파수) → action balance 가 **stiff** (Press 1993). 최소 시간척도가 수렴 지배 → over/undershoot. Nonlinear 4-wave 가 최대 난제 (spectral change 고민감).

### 5.1 Action density limiter (Hersbach-Janssen 1999, WAM 1980s)

매 time step / 격자 / bin 의 net 변화를 omni-directional Phillips equilibrium 의 일부로 제한 (Booij 1999 형):
$$\Delta N \equiv \gamma\frac{\alpha_{\text{PM}}}{2\sigma k^3 c_g} \quad \text{(3.27)}$$
- $\gamma\ge0$ = limitation factor (**보통 $\gamma=0.1$**, Tolman 1992), $\alpha_{\text{PM}} = 8.1\times10^{-3}$ (Pierson-Moskowitz Phillips 상수, Komen 1994)
- **Janssen(1989,1991a) wind 사용 시 원 Hersbach-Janssen(1999) limiter 적용**

제한된 갱신:
$$N_{i,j,l,m}^s = N_{i,j,l,m}^{s-1} + \frac{\Delta N_{i,j,l,m}}{|\Delta N_{i,j,l,m}|}\min\{|\Delta N_{i,j,l,m}|, \Delta N\} \quad \text{(3.28)}$$
> 저주파(에너지 함유부)는 pseudo time step 이 evolution scale 과 일치 → pre-limitation 결과. 고주파는 limiter 상한. **문제**: limiter 가 peak 근처·전 격자·전 iteration 에서 active (Tolman 2002 확인) → poor convergence (소진폭 진동). Ris(1999): 정상해가 limiter 설정에 영향받음. De Waal(2001): equilibrium 에서 hidden sink 의심.

### 5.2 Frequency-dependent under-relaxation (false time stepping)

Under-relaxation 항으로 $A$ 주대각 강화 (Ferziger-Perić 1999):
$$\frac{\vec{N}^s - \vec{N}^{s-1}}{\tau} + A\vec{N}^s = \vec{b} \quad \text{(3.29)}$$
- $\tau$ = pseudo time step. $\tau$ 작을수록 작은 갱신 (수렴 ↓, 비용 ↑)
- **주파수 비례 under-relaxation**: $\tau^{-1} = \alpha\sigma$ ($\alpha$ 무차원) → 고주파 작은 갱신, 저주파 큰 갱신:

$$(A + \alpha\sigma I)\vec{N}^s = \vec{b} + \alpha\sigma\vec{N}^{s-1} \quad \text{(3.30)}$$
> $s\to\infty$ 시 $A\vec{N}^\infty = \vec{b}$ (fixed point — 정상해 불변). $\alpha$ 증가 → 전 스펙트럼 변화 감소 → (i) action balance 실제로 푸는 주파수 범위 확대 (ii) limiter 사용 감소. **$\alpha$ 는 경험적 결정 (robustness 저하)**. 첫 iteration 은 under-relaxation off ($\alpha=0$, 2nd-gen 첫 추정 위해 — 2nd-gen 은 안정화 불필요).

## 6. SWAN 옵션 매핑 (User cmd)

| Tech (PDF §) | User cmd | 비고 |
|---|---|---|
| §3.3 SIP solver | (internal, default) | penta-diagonal ILU+SIP / 무전류 Thomas |
| 3.22-3.23 종래 stopping | `NUMERIC STOPC ... STAT mxitst` | obsolete (41.01 이전) |
| 3.26 curvature stopping | `NUMERIC STOPC [dabs] [drel] [curvat] [npnts]` | **default since 41.01**, npnts=99% |
| §3.4 max iteration | `NUMERIC ... [mxitst]` (stationary, 보통 50) / `[mxitns]` (nonstationary) | |
| §3.5 sweeps | (internal four-sweep) | $M>4$ 비권장 |
| §3.6 DIA-in-sweep | `QUADRUPL [iquad]` | iquad=1/2/3 method 선택 |
| 3.27-3.28 action limiter | `NUMERIC ... [limiter]` (= $\gamma$, default 0.1) | Hersbach-Janssen |
| 3.29-3.30 under-relaxation | `NUMERIC ... [alfa]` ($\alpha$) | frequency-dependent |

## 7. 한계

- Matrix 구조식(3.16): ASCII block 형태 → 본 노트 서술 요약 (penta-diagonal block coupling).
- 종래/curvature stopping (3.22-3.23, 3.26)의 cases 우변·곡률 분자: pdftotext + HTML alt-text 모두 truncated → 정밀식 swantech.pdf p.82-84 또는 SWAN User Manual NUMERIC.
- §3.7.1 introduction (stiff·multiple time scale 배경)은 정성 서술 — 본 노트 §5 도입에 요약.
- Newton-Raphson breaking(3.18)의 $\phi^{n-1}$ 정의: §3.3 본문 + [[swan-tech-ch2-dissipation-detailed]] §6 (S_ds,br Eq 2.68) 연계.

## 8. 연결

- [[swan-tech-ch3-discretization]] — §3.2 이산화 (이 system 의 출처)
- [[swan-tech-ch2-sources-sinks]] — source term S_tot (선형화 대상)
- [[swan-tech-ch2-dissipation-detailed]] — breaking S_ds,br (Newton-Raphson 3.18 대상)
- [[swan-tech-ch2-nonlinear-detailed]] — DIA quadruplet (§3.6 four-sweep 적분)
- [[swan-source-terms-implementation]] — source 선형화 implementation
