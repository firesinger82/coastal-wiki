---
title: "SWAN swantech Ch 2.3.4 Nonlinear wave-wave interactions (S_nl) — quadruplets DIA/WRT + triads FTIM/SPB/LTA/DCTA verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.3.4 Nonlinear wave-wave interactions, doc p.29-50 (Eq 2.75-2.108). Quadruplets: Hasselmann 1985 (DIA), Tolman 1993, Van Vledder 2000·2006, WAMDI 1988, Komen 1994, Hasselmann 1962·1963, Webb 1978, Tracy-Resio 1982, Resio-Perrie 1991, Herterich-Hasselmann 1980, Benoit 2005. Triads: Freilich-Guza 1984, Eldeberky 1996, Eldeberky-Battjes 1995, Herbers-Burton 1997, Madsen-Sørensen 1993, Becq-Girard 1999, Holloway 1980, Salmon 2016, Doering-Bowen 1995, De Wit 2022, Bredmose 2005, Akrish 2024, Booij 2009, Zijlema 2022, Benit-Reniers 2022, Sand 1982, Peregrine 1967, Reniers-Zijlema 2022."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §2.3.4 직접 read via pdftotext (context-verified 식 번호) + website_markdown node18.md/node19.md LaTeX alt-text. 식 번호는 PDF 번호 체계. 주의: 본 섹션 PDF↔HTML offset 가변 (quadruplets +1, triads bispectrum 유도부 +1→+15). Quadruplets 2.75-2.89 = HTML−1 (context-verified). Triads 핵심 named 식(FTIM 2.100·SPB 2.101·LTA 2.102·ext-LTA 2.103·biphase 2.104·Ursell 2.105·DCTA 2.106·DCTA-rev 2.107·noncollinear 2.108) PDF 본문 직접 검증."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.75-2.108 PDF context-검증, 계수값 verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
---

# swantech Ch 2.3.4 Nonlinear wave-wave interactions (S_nl) — verified verbatim

> swantech.pdf (v41.51) §2.3.4 직접 read. [[swan-tech-ch2-sources-sinks]] §2.3.1 의 brief nonlinear 서술을 **DIA/WRT 정확 식 + 41.51 신설 triad 체계(FTIM·QuadWave)** 로 확장. Quadruplets(deep, 2.75-2.89) + Triads(shallow, 2.90-2.108).
>
> **식 번호 주의**: PDF↔online HTML offset 이 본 섹션에서 **가변**. Quadruplets는 HTML=PDF+1, triads bispectrum 유도부는 offset +1→+15 로 증가 (HTML이 중간 유도식을 추가 번호). 본 노트는 **PDF 번호** 사용, named 식은 PDF 본문 직접 검증.

---

# A. Quadruplets — deep/intermediate water (Eq 2.75-2.89)

2 방법: **DIA** (crude Boltzmann 근사, SWAN 표준) + **XNL/WRT** (Van Vledder 정확 적분).

## A.1 DIA — Hasselmann et al. (1985)

Tolman(1993 personal comm)이 약간 수정한 소스 구현. 2 quadruplet 구성, 주파수:

$$\sigma_1 = \sigma_2 = \sigma,\quad \sigma_3 = \sigma(1+\lambda) = \sigma^+,\quad \sigma_4 = \sigma(1-\lambda) = \sigma^- \quad \text{(2.75) [HTML 2.76]}$$
- $\lambda = 0.25$ (default). Resonance 만족 위해 1st quadruplet: $\theta_3 = -11.48°$, $\theta_4 = 33.56°$. 2nd quadruplet = mirror: $\theta_3 = \theta^+ = 11.48°$, $\theta_4 = \theta^- = -33.56°$ (임의 $\lambda$: Van Vledder 2000).

$$S_{\text{nl4}}(\sigma,\theta) = S^*_{\text{nl4}}(\sigma,\theta) + S^{**}_{\text{nl4}}(\sigma,\theta) \quad \text{(2.76) [HTML 2.77]}$$
($S^*$ = 1st quadruplet, $S^{**}$ = 2nd = mirror)

세 frequency-direction bin 에서 variance 변화율:

$$\begin{pmatrix}\delta S^*_{\text{nl4}}(\sigma,\theta)\\ \delta S^*_{\text{nl4}}(\sigma^+,\theta^+)\\ \delta S^*_{\text{nl4}}(\sigma^-,\theta^-)\end{pmatrix} = \begin{pmatrix}2\\-1\\-1\end{pmatrix} C_{\text{nl4}}(2\pi)^2 g^{-4}\left(\frac{\sigma}{2\pi}\right)^{11}\times$$
$$\left[E^2(\sigma,\theta)\left\{\frac{E(\sigma^+,\theta^+)}{(1+\lambda)^4} + \frac{E(\sigma^-,\theta^-)}{(1-\lambda)^4}\right\} - 2\frac{E(\sigma,\theta)E(\sigma^+,\theta^+)E(\sigma^-,\theta^-)}{(1-\lambda^2)^4}\right] \quad \text{(2.77) [HTML 2.78]}$$
- $C_{\text{nl4}} = 3\times10^7$ (default). 기하급수 주파수 분포(SWAN)에서 variance/momentum/action 보존.
- $E(\sigma^\pm,\theta^\pm)$ = 주변 4 bin bi-linear 보간 (또는 nearest-bin weight=1 옵션).

### 천수 scaling (WAMDI 1988)

$$S_{\text{nl4}}^{\text{finite depth}} = R(k_p d)\,S_{\text{nl4}}^{\text{deep water}} \quad \text{(2.78) [HTML 2.79]}$$

$$R(k_p d) = 1 + \frac{C_{sh1}}{k_p d}(1 - C_{sh2}k_p d)e^{C_{sh3}k_p d} \quad \text{(2.79) [HTML 2.80]}$$
- $C_{sh1}=5.5,\ C_{sh2}=5/6,\ C_{sh3}=-5/4$ (WAMDI 1988)
- $k_p\to0$ 발산 → lower limit $k_p=0.5$ → max $R=4.43$. Robustness 위해 $k_p = 0.75\tilde{k}$ (Komen 1994).

## A.2 XNL / WRT — Webb-Resio-Tracy (Van Vledder)

6차원 Boltzmann (Hasselmann 1962·1963 + Webb 1978, Tracy-Resio 1982, Resio-Perrie 1991). 상세: Van Vledder(2006), 개관 Benoit(2005). 본 위키 [[swan-xnl4-exact-quadruplet]] (mod_xnl4v5.ftn90).

Resonance 조건:
$$\vec{k}_1+\vec{k}_2 = \vec{k}_3+\vec{k}_4,\quad \sigma_1+\sigma_2 = \sigma_3+\sigma_4 \quad \text{(2.80) [HTML 2.81]}$$

action density $N_1$ 변화율 (전체 quadruplet 적분):
$$\frac{\partial N_1}{\partial t} = \int\!\!\int\!\!\int G(\vec{k}_1,\vec{k}_2,\vec{k}_3,\vec{k}_4)\,\delta(\cdots)\,\delta(\sigma_1+\sigma_2-\sigma_3-\sigma_4)\times[N_1 N_3(N_4-N_2)+N_2 N_4(N_3-N_1)]\,d\vec{k}_2 d\vec{k}_3 d\vec{k}_4 \quad \text{(2.81) [HTML 2.82]}$$
- $G$ = coupling coefficient (명시식 Herterich-Hasselmann 1980)

WRT 핵심: $(\vec{k}_1,\vec{k}_3)$ 별 적분 공간 + locus 따라 $(s,n)$ 좌표:
$$\frac{\partial N_1}{\partial t} = 2\int T(\vec{k}_1,\vec{k}_3)\,d\vec{k}_3 \quad \text{(2.82) [HTML 2.83]}$$

$T$ 함수 (2.83 [HTML 2.84]), $\theta$ 영역 함수 (2.84 [HTML 2.85]), closed locus 선적분으로 변환 (2.85 [HTML 2.86]). Jacobian:
$$J = |\vec{c}_{g,2} - \vec{c}_{g,4}|^{-1} \quad \text{(2.86) [HTML 2.87]}$$

이산화 (locus 보통 40 조각):
$$T(\vec{k}_1,\vec{k}_3) \approx \sum_{i=1}^{n_s} G(s_i)J(s_i)P(s_i)\,\Delta s_i \quad \text{(2.87) [HTML 2.88]}$$

$$\frac{\partial N(\vec{k}_1)}{\partial t} \approx \sum T(\vec{k}_1,\vec{k}_3)\,\Delta k_{i_{k3}}\Delta\theta_{i_{\theta3}} \quad \text{(2.88) [HTML 2.89]}$$

> **비용**: DIA 대비 $10^3$~$10^4$ 배 — 고도로 idealized test case 한정. 권장: max freq ≈ 6×peak, ~40 주파수(증분 1.07), 방향 ~10°.

### BQF 파일 + depth rescale

적분 공간(loci·계수·Jacobian)을 초기화 시 precompute → binary "xnl4v5_*xxxxx*.bqf" (xxxxx=수심, 99999=deep). 최근접 수심 $d_N$ 의 BQF 사용 후 DIA scaling(2.79) 재조정:

$$S_{\text{nl4}}^d = S_{\text{nl4}}^{d_N}\frac{R(k_p d)}{R(k_p d_N)} \quad \text{(2.89) [HTML 2.90]}$$

---

# B. Triads — shallow water (Eq 2.90-2.108)

> **41.51 대폭 확장**: 이전엔 LTA/SPB/DCTA 만. 41.51 부터 quadratic 이론 전개 + FTIM 신설 + 4 interaction coefficient + QuadWave(Akrish 2024). 2 방법: **quadratic formulation** (FTIM·SPB·LTA) + **DCTA** ($k^{-4/3}$ tail heuristic).

## B.1 Quadratic 이론 framework (Eldeberky 1996, Herbers-Burton 1997)

1D 자유표면 (Freilich-Guza 1984, Eldeberky 1996, Akrish 2024):
$$\eta(x,t) = \sum_{p=-\infty}^\infty A_p(x)\exp[\mathrm{i}(\omega_p t - \psi_p(x))]$$
($d\psi_p/dx = k_p$, $\omega_p^2 = gk_p\tanh(k_p d)$). 진폭 evolution (Madsen-Sørensen 1993, Eldeberky 1996):
$$\frac{dA_p}{dx} = -S_p A_p - \mathrm{i}\sum_m R_{(m,p-m)}A_m A_{p-m}\exp[-\mathrm{i}(\psi_m+\psi_{p-m}-\psi_p)]$$
($S_p$=shoaling, $R_{(m,p-m)}$=interaction coeff, real·대칭). 복소진폭 $C_p = A_p\exp(-\mathrm{i}\psi_p)$ 도입 →

$$\frac{dC_p}{dx} = -\mathrm{i}k_p C_p - \mathrm{i}\sum_{m=1}^{p-1}R_{(m,p-m)}C_m C_{p-m} - 2\mathrm{i}\sum_{m=1}^\infty R_{(p+m,-m)}C^*_m C_{p+m} \quad \text{(2.90) [HTML 2.94]}$$

2차 moment $E_p = \langle C_p C^*_p\rangle$ (이산 spectral energy), 3차 = bispectrum $B_{m,p-m} = \langle C_m C_{p-m}C^*_p\rangle$ (Hasselmann 1963). Spectrum evolution:
$$\frac{dE_p}{dx} = 2\sum_{m=1}^{p-1}R_{(m,p-m)}\text{Im}(B_{m,p-m}) - 4\sum_{m=1}^\infty R_{(p+m,-m)}\text{Im}(B_{m,p}) \quad \text{[HTML 2.99]}$$

Bispectrum evolution → trispectrum $T_{m,n,p-m-n}$ (4차 moment) → **closure 2가지**:
- **quasi-Gaussian** (quasi-normal, $c_4=0$, Eldeberky 1996): $\Psi = \Delta k$
- **Holloway (1980)**: $c_4 \propto B_{m,p-m}$, $\Psi = \Delta k - \mathrm{i}K$ ($K>0$ relaxation)

정상상태 bispectrum:
$$B_{m,p-m} = \frac{2}{\Psi}[R_{(m,p-m)}E_m E_{p-m} - R_{(p,-m)}E_m E_p - R_{(m-p,p)}E_{p-m}E_p] \quad \text{[HTML 2.107]}$$
> 국소 스펙트럼만 의존 (weak nonlinearity + 작은 bed slope, Herbers-Burton 1997). $B_{l,k} = |B_{l,k}|\exp(-\mathrm{i}\beta_{l,k})$, $\beta$=biphase.

단측 variance density: $E(f_p) = 2\langle C_p C^*_p\rangle/\Delta f_p = 2E_p/\Delta f_p$.

## B.2 FTIM — Full Triad Interaction Model (Eq 2.100)

quasi-Gaussian closure 기반. 모든 collinear sum/difference 상호작용, energy flux $c_g E$ 보존 ($\alpha$ calibration × $c_g$):

$$S_{\text{nl3}}(f_p) = 2\alpha_{\text{FTIM}}c_{g,p}\left[\sum_{m=1}^{p-1}R_{(m,p-m)}\frac{\Delta f_m}{|k_{p-m}+k_m-k_p|}Q(f_m,f_{p-m})\sin(-\beta_{m,p-m})\right.$$
$$\left. - 2\sum_{m=1}^\infty R_{(p+m,-m)}\frac{\Delta f_m}{|k_p+k_m-k_{p+m}|}Q(f_m,f_p)\sin(-\beta_{m,p})\right] \quad \text{(2.100)}$$
- $Q(f_m,f_{p-m}) = R_{(m,p-m)}E(f_m)E(f_{p-m}) - R_{(p,-m)}E(f_m)E(f_p) - R_{(m-p,p)}E(f_{p-m})E(f_p)$
- **SWAN 41.51 구현**. $\alpha_{\text{FTIM}} = \mathcal{O}(1)$. $Q<0$ → subharmonic (biphase 180° mismatch, 절댓값 무시 처리).

## B.3 SPB — Stochastic Parametric Boussinesq (Becq-Girard et al. 1999, Eq 2.101)

Holloway(1980) closure 기반:
$$S_{\text{nl3}}(f_p) = 2\alpha_{\text{SPB}}K c_{g,p}\left[\sum_{m=1}^{p-1}R_{(m,p-m)}\frac{\Delta f_m}{\Delta k_{m,p-m}^2 + K^2}Q(f_m,f_{p-m}) - 2\sum_{m=1}^\infty R_{(p+m,-m)}\frac{\Delta f_m}{\Delta k_{m,p}^2+K^2}Q(f_m,f_p)\right] \quad \text{(2.101)}$$
- $\Delta k_{m,p-m} = k_{p-m}+k_m-k_p$, $\alpha_{\text{SPB}} = \mathcal{O}(1)$.
- $K$ 튜닝: Becq-Girard 1999 $K = 0.95k_{\text{op}} - 0.75$ ($k_{\text{op}}$=offshore peak). **Salmon(2016)**: 실 적용서 $k_{\text{op}}$ 정의 곤란 + $K<0$ 방지 → $K = 0.95k_{\text{peak}}$ (local peak, **SWAN 구현**).

## B.4 LTA — Lumped Triad Approximation (Eldeberky 1996, Eq 2.102)

FTIM(2.100) 단순화 (DTA Eldeberky-Battjes 1995의 적응판). 4 가정: ① 세 interaction coeff 동일, ② sum/diff → self-self only ($\Delta f\to$ effective bandwidth $\delta f$), ③ $\delta f/|\Delta k| \propto c_p$, ④ 저→고 harmonic 만.

$$S^+_{\text{nl3}}(f_p) = c_p R^2_{(p/2,p/2)}\max[0,\,E^2(f_{p/2}) - 2E(f_{p/2})E(f_p)]\sin(-\beta_{p/2,p/2})$$
$$S^-_{\text{nl3}}(f_p) = c_{2p}R^2_{(p,p)}\max[0,\,E^2(f_p) - 2E(f_p)E(f_{2p})]\sin(-\beta_{p,p})$$
($S^-(f_p) = S^+(f_{2p})$, 가정①)

$$S_{\text{nl3}}(f_p) = \alpha_{\text{LTA}}c_{g,p}[S^+_{\text{nl3}}(f_p) - 2S^-_{\text{nl3}}(f_p)] \quad \text{(2.102)}$$
> 2nd(가능시 4th·8th) higher harmonic 생성. surf zone 밖에서 persistent → $f_p < 2.5\tilde{f}$ 만 계산.

### Extended LTA (41.51, Eq 2.103)

추가 triad: $p/3, 2p/3, p$ ($S^{++}$) 및 $p, 2p, 3p$ ($S^{--}$):
$$S_{\text{nl3}}(f_p) = \alpha_{\text{LTA+}}c_{g,p}[S^+_{\text{nl3}}(f_p) - 2S^-_{\text{nl3}}(f_p) + S^{++}_{\text{nl3}}(f_p) - 2S^{--}_{\text{nl3}}(f_p)] \quad \text{(2.103)}$$

## B.5 Biphase parametrization (Eq 2.104-2.105)

$-\pi/2 \le \beta_{l,k} \le 0$. Eldeberky(1996): spectral Ursell 만 의존:
$$\beta = -\frac{\pi}{2} + \frac{\pi}{2}\tanh\left(\frac{m}{Ur}\right) \quad \text{(2.104)}$$

$$Ur = \frac{gH_{m0}}{8\sqrt{2}}\left(\frac{T_{m01}}{\pi d}\right)^2 \quad \text{(2.105)}$$
- $m$ tunable. Eldeberky-Battjes(1995) $m=0.2$ → 불안정(고주파 인위 증폭). **Doering-Bowen(1995) $m=0.63$** (robust).
- **De Wit(2022)**: SWASH 기반 (local bed slope + peak period 의존), biphase 양수 허용(recurrence) — **41.45 구현**.

## B.6 Interaction coefficients $R_{(m,p-m)}$ (4종, 41.51, PDF 무번호 display 식)

> PDF(v41.51)에서 아래 4식은 (2.105)~(2.106) 사이 **무번호 display 식** (HTML은 2.129-2.136 부여). 저자로 인용.

| 출처 | 비고 |
|---|---|
| **Freilich-Guza (1984)** | $R_{(m,p-m)} = -\dfrac{3}{4}\dfrac{\sigma_p}{d\sqrt{gd}}$ (Peregrine 1967 Boussinesq 기반, $\sigma_p=2\pi f_p$) |
| **Madsen-Sørensen (1993)** | improved dispersion Boussinesq, $B=1/15$. 초기 SWAN LTA 용 (Eldeberky 1996) |
| **Bredmose et al. (2005)** | $R = N_{(m,p-m)}/H_{mp}$ — 2nd order Stokes 정확 일치. $H_{mp} = (\sigma_p^2-\sigma_{mp}^2)/(k_p-k_{mp})$, $k_{mp}=k_m+k_{p-m}$ |
| **QuadWave / Akrish (2024)** | $R = W_{(m,p-m)}N_{(m,p-m)}/H_{mp}$, weight $W = \exp[-(\chi/\alpha_3)^{\alpha_2}]$, $\chi = |k_{mp}|d(|k_{mp}|/|k_p|)^{\alpha_1}$. **SWAN: $\alpha_1=1, \alpha_2=0.4, \alpha_3=5.5$** (원 $\alpha_2=1.4$는 고주파 과다) |

> 개관: Akrish(2024). 4식 모두 **SWAN 41.51 구현**.

## B.7 DCTA — Distributed Collinear Triad Approximation (Booij et al. 2009, Eq 2.106-2.108)

quadruplet 유추 heuristic — 모든 super harmonic 생성 + $k^{-4/3}$ universal tail. 원식 (Booij 2009):
$$S_{\text{nl3}}(\sigma_1) = \lambda\frac{\sin(-\beta)\tilde{k}^{1-p}}{\cdots}\int\frac{\tanh(\overline{k}d)}{\overline{k}d}[\sigma_2 c_{g,2}k_2^p N(\sigma_2) - \sigma_1 c_{g,1}k_1^p N(\sigma_1)]\,d\sigma_2 \quad \text{(2.106)}$$
- quasi-resonance $\sigma_3 = |\sigma_2-\sigma_1|$ (주파수 일치, 파수 불일치). $\lambda$=calibration, $\tilde{k}=\tilde{\sigma}/\sqrt{gd}$ ($\tilde{\sigma}$=Eq 2.66 mean), $p=4/3$ shape, $\overline{k}=(k_1+k_2+k_3)/3$. $\tanh(\overline{k}d)/\overline{k}d$ 가 파수 증가 시 resonance mismatch 반영.

**Zijlema(2022) energy-flux 보존형** (개선, 41.45 구현):
$$S_{\text{nl3}}(\sigma_1) = \lambda c_{g,1}\frac{\sin(-\beta)\tilde{k}^{2-p}}{\tilde{\sigma}^2 d^2}\int\frac{\tanh\overline{k}d}{\cdots}[c_{g,2}k_2^p E(\sigma_2) - c_{g,1}k_1^p E(\sigma_1)]\,d\sigma_2 \quad \text{(2.107)}$$

**Noncollinear 확장 (Benit-Reniers 2022, Eq 2.108)** — 각도차 기반 transfer reduction:
$$S_{\text{nl3}}(\sigma_1,\theta_1) = \lambda c_{g,1}\frac{\sin(-\beta)\tilde{k}^{2-p}}{\tilde{\sigma}^2 d^2}\int_0^{2\pi}\int_0^\infty\frac{\tanh\overline{k}d}{\cdots}G(\Delta\theta_{nm})[\cdots]\,d\sigma_2 d\theta_2 \quad \text{(2.108)}$$
> $G(\Delta\theta_{nm})$ = Sand(1982) transfer function, $\Delta\theta_{nm}=\theta_n-\theta_m$. (이전 노트 [[swan-tech-ch2-vegetation-ice-bragg-gen12]]의 "Eq 2.108"이 바로 이 noncollinear DCTA — 동일 PDF 번호 일치 확인.)
>
> LTA·DCTA triad 는 **$Ur \ge 0.1$ 에서만** 계산.

## C. SWAN 옵션 매핑 (User cmd)

| Tech 식 (PDF) | User cmd | 본 위키 |
|---|---|---|
| 2.75-2.79 DIA quadruplet | `QUADRUPL` (default Hasselmann 1985) | [[swan-source-terms-implementation]] |
| 2.80-2.89 WRT/XNL exact | `QUADRUPL ... iquad=51/52/53` | [[swan-xnl4-exact-quadruplet]] |
| 2.100 FTIM | `TRIAD FTIM` (41.51) | (없음) |
| 2.101 SPB | `TRIAD SPB` | (없음) |
| 2.102 LTA / 2.103 ext-LTA | `TRIAD LTA` / `TRIAD ELTA` | (없음) |
| 2.106-2.107 DCTA | `TRIAD DCTA` | (없음) |
| 2.108 noncollinear DCTA | `TRIAD DCTA ... ` (Benit-Reniers) | (없음) |
| interaction coeff (B.6) | `TRIAD ... ` (Freilich/MadsenSørensen/Bredmose/QuadWave) | (없음) |

## D. 버전 history (§2.3.4)

- DIA: SWAN 초기부터 (Hasselmann 1985, Tolman 1993 수정)
- WRT/XNL: Van Vledder(2006) — [[swan-xnl4-exact-quadruplet]]
- **41.45**: DCTA Zijlema(2022) energy-flux 보존형(2.107) + De Wit(2022) biphase + Benit-Reniers noncollinear(2.108)
- **41.51**: FTIM(2.100) 신설 + extended LTA(2.103) + 4 interaction coeff(QuadWave/Akrish 2024)

## E. 한계

- Triads bispectrum 유도부(B.1, PDF 2.90-2.99): HTML offset 가변 구간 → 중간 유도식은 PDF 번호 미부여(또는 가변)로 본 노트는 named 결과식만 PDF 번호 인용, 유도식은 [HTML n] 또는 무번호.
- DCTA 식(2.106-2.108)의 적분 분모·$\tilde{k}$ 거듭제곱 일부: pdftotext garble로 "$\cdots$" 처리 — 정밀 식은 PDF p.49-50 또는 Booij(2009)/Zijlema(2022) 원논문.
- Bredmose/QuadWave $N_{(m,p-m)}$ 전개식 미인용 (PDF p.48 직접 또는 Bredmose 2005/Akrish 2024).

## F. 연결

- [[swan-tech-ch2-sources-sinks]] — §2.3.1 brief nonlinear 서술
- [[swan-tech-ch2-dissipation-detailed]] — §2.3.3 (Eq 2.43-2.74)
- [[swan-tech-ch2-vegetation-ice-bragg-gen12]] — §2.3.5-8 (Eq 2.109+, noncollinear DCTA 2.108 직전 연결)
- [[swan-xnl4-exact-quadruplet]] — WRT/XNL source-analysis (mod_xnl4v5.ftn90)
- [[swan-source-terms-implementation]] — DIA implementation
