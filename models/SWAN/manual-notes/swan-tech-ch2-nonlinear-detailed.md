---
title: "SWAN swantech Ch 2.3.4 Nonlinear wave-wave interactions (S_nl) — quadruplets DIA/WRT + triads FTIM/SPB/LTA/DCTA verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.3.4 Nonlinear wave-wave interactions, doc p.29-50 (Eq 2.75-2.108). Quadruplets: Hasselmann 1985 (DIA), Tolman 1993, Van Vledder 2000·2006, WAMDI 1988, Komen 1994, Hasselmann 1962·1963, Webb 1978, Tracy-Resio 1982, Resio-Perrie 1991, Herterich-Hasselmann 1980, Benoit 2005. Triads: Freilich-Guza 1984, Eldeberky 1996, Eldeberky-Battjes 1995, Herbers-Burton 1997, Madsen-Sørensen 1993, Becq-Girard 1999, Holloway 1980, Salmon 2016, Doering-Bowen 1995, De Wit 2022, Bredmose 2005, Akrish 2024, Booij 2009, Zijlema 2022, Benit-Reniers 2022, Sand 1982, Peregrine 1967, Reniers-Zijlema 2022."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §2.3.4 직접 read via pdftotext (context-verified 식 번호) + website_markdown node18.md/node19.md LaTeX alt-text. 식 번호는 PDF 번호 체계. 주의: 본 섹션 PDF↔HTML offset 가변 (quadruplets +1, triads bispectrum 유도부 +1→+15). Quadruplets 2.75-2.89 = HTML−1 (context-verified). Triads 핵심 named 식(FTIM 2.100·SPB 2.101·LTA 2.102·ext-LTA 2.103·biphase 2.104·Ursell 2.105·DCTA 2.106·DCTA-rev 2.107·noncollinear 2.108) PDF 본문 직접 검증. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.75-2.108 PDF context-검증, 계수값 verbatim"
verification_date: 2026-06-02
last_source_check: 2026-10-13 (recovery 대조 반영)
related:
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/source-analysis/swan-xnl4-exact-quadruplet.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
---

# swantech Ch 2.3.4 Nonlinear wave-wave interactions (S_nl) — verified verbatim

> swantech.pdf (v41.51) §2.3.4 직접 read. [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) §2.3.1 의 brief nonlinear 서술을 **DIA/WRT 정확 식 + 41.51 신설 triad 체계(FTIM·QuadWave)** 로 확장. Quadruplets(deep, 2.75-2.89) + Triads(shallow, 2.90-2.108).
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

문서 인쇄식 (swantech PDF 37쪽 / 인쇄 29쪽):

$$\begin{pmatrix}\delta S^*_{\text{nl4}}(\sigma,\theta)\\ \delta S^*_{\text{nl4}}(\sigma^+,\theta^+)\\ \delta S^*_{\text{nl4}}(\sigma^-,\theta^-)\end{pmatrix} = \begin{pmatrix}2\\-1\\-1\end{pmatrix} C_{\text{nl4}}(2\pi)^2 g^{-4}\left(\frac{\sigma}{2\pi}\right)^{11}\times$$
$$\left[E^2(\sigma,\theta)\left\{\frac{E(\sigma^+,\theta^+)}{(1+\lambda)^4} + \frac{E(\sigma^-,\theta^-)}{(1-\lambda)^4}\right\} - 2\frac{E(\sigma,\theta)E(\sigma^+,\theta^+)E(\sigma^-,\theta^-)}{(1-\lambda^2)^4}\right] \quad \text{(2.77) [HTML 2.78]}$$

부호 정정식:

$$\begin{pmatrix}\delta S^*_{\text{nl4}}(\sigma,\theta)\\ \delta S^*_{\text{nl4}}(\sigma^+,\theta^+)\\ \delta S^*_{\text{nl4}}(\sigma^-,\theta^-)\end{pmatrix} = \begin{pmatrix}-2\\1\\1\end{pmatrix} C_{\text{nl4}}(2\pi)^2 g^{-4}\left(\frac{\sigma}{2\pi}\right)^{11}\times$$
$$\left[E^2(\sigma,\theta)\left\{\frac{E(\sigma^+,\theta^+)}{(1+\lambda)^4} + \frac{E(\sigma^-,\theta^-)}{(1-\lambda)^4}\right\} - 2\frac{E(\sigma,\theta)E(\sigma^+,\theta^+)E(\sigma^-,\theta^-)}{(1-\lambda^2)^4}\right] \quad \text{(2.77) [HTML 2.78]}$$

인쇄식의 벡터는 $(2,-1,-1)^T$이다. 같은 대괄호를 유지한 코드의 벡터는 $(-2,1,1)^T$이다. (`src/swancom4.ftn:1524` `SFNL(I,ID) = - 2. * ( SA1(I,J) + SA2(I,J) )`)
- $C_{\text{nl4}} = 3\times10^7$ (default). 기하급수 주파수 분포(SWAN)에서 variance/momentum/action 보존.
- $E(\sigma^\pm,\theta^\pm)$ = 주변 4 bin bi-linear 보간 (또는 nearest-bin weight=1 옵션).

### 천수 scaling (WAMDI 1988)

$$S_{\text{nl4}}^{\text{finite depth}} = R(k_p d)\,S_{\text{nl4}}^{\text{deep water}} \quad \text{(2.78) [HTML 2.79]}$$

$$R(k_p d) = 1 + \frac{C_{sh1}}{k_p d}(1 - C_{sh2}k_p d)e^{C_{sh3}k_p d} \quad \text{(2.79) [HTML 2.80]}$$
- $C_{sh1}=5.5,\ C_{sh2}=5/6,\ C_{sh3}=-5/4$ (WAMDI 1988)

CSH2의 실행 기본값은 0.833이다. (`src/swanmain.ftn:1456` `PQUAD(4) = 0.833`; swanuse PDF 73쪽 / 인쇄 65쪽의 `0.833333`)
- 하한은 파수 $k_p$가 아니라 무차원 $k_pd=.5$이다. (`src/swancom4.ftn:1410` `X = MAX ( 0.75 * DEP2(KCGRD(1)) * KMESPC , 0.5 )`; swantech PDF 39쪽 / 인쇄 31쪽)

## A.2 XNL / WRT — Webb-Resio-Tracy (Van Vledder)

6차원 Boltzmann (Hasselmann 1962·1963 + Webb 1978, Tracy-Resio 1982, Resio-Perrie 1991). 상세: Van Vledder(2006), 개관 Benoit(2005). 본 위키 [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md) (mod_xnl4v5.ftn90).

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

문서 인쇄식 (swantech PDF 40쪽 / 인쇄 32쪽):

$$\frac{\partial N(\vec{k}_1)}{\partial t} \approx \sum T(\vec{k}_1,\vec{k}_3)\,\Delta k_{i_{k3}}\Delta\theta_{i_{\theta3}} \quad \text{(2.88) [HTML 2.89]}$$

(2.88)의 보완식에는 앞의 대칭 계수 2와 극좌표 면적 인자 $k_3$를 모두 적는다. (`src/mod_xnl4v5.ftn90:7667` `t13 = 2.*t13`; `src/mod_xnl4v5.ftn90:7677` `xnl(ik1,ia1) = xnl(ik1,ia1) + t13*q_k(ik3)*q_delta*q_dk(ik3)`)

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
- SPB의 문서 설명은 국소 첨두파수이다. 구현은 해당 삼중항의 최소 파수에 .95를 곱한다. 기본 절편은 0이다. (swantech PDF 47쪽 / 인쇄 39쪽; `src/swancom4.ftn:3519` `KM = MIN(K1,K2,K3)`; `src/swancom4.ftn:3520` `KB = PTRIAD(6)*KM + PTRIAD(7)`)

## B.4 LTA — Lumped Triad Approximation (Eldeberky 1996, Eq 2.102)

FTIM(2.100) 단순화 (DTA Eldeberky-Battjes 1995의 적응판). 4 가정: ① 세 interaction coeff 동일, ② sum/diff → self-self only ($\Delta f\to$ effective bandwidth $\delta f$), ③ $\delta f/|\Delta k| \propto c_p$, ④ 저→고 harmonic 만.

$$S^+_{\text{nl3}}(f_p) = c_p R^2_{(p/2,p/2)}\max[0,\,E^2(f_{p/2}) - 2E(f_{p/2})E(f_p)]\sin(-\beta_{p/2,p/2})$$
$$S^-_{\text{nl3}}(f_p) = c_{2p}R^2_{(p,p)}\max[0,\,E^2(f_p) - 2E(f_p)E(f_{2p})]\sin(-\beta_{p,p})$$
($S^-(f_p) = S^+(f_{2p})$, 가정①)

$$S_{\text{nl3}}(f_p) = \alpha_{\text{LTA}}c_{g,p}[S^+_{\text{nl3}}(f_p) - 2S^-_{\text{nl3}}(f_p)] \quad \text{(2.102)}$$
> swantech PDF 48쪽 / 인쇄 40쪽은 원래 LTA의 $f_p<2.5\widetilde f$를 설명한다.

현재 `TRIAD LTA` 기본값은 주파수 절단을 끈다. 이전 수치형 LTA 경로의 기본 절단은 2.5이다. 3배 주파수 상호작용도 `TRIAD LTA`에서 계산한다. (`src/swanpre1.ftn:3351` `CALL INREAL ('CUTFR', PTRIAD(2), 'STA', -1.)`; swanuse PDF 75쪽 / 인쇄 67쪽)

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

Bredmose·QuadWave의 전달함수 전개 (swantech PDF 50쪽 / 인쇄 42쪽, PDF 51쪽 / 인쇄 43쪽):

$$N_{(m,p-m)}=-\frac{g}{2\sigma_m\sigma_{p-m}}[\sigma_{mp}^2k_mk_{p-m}+\sigma_pk_{mp}(k_m\sigma_{p-m}+k_{p-m}\sigma_m)]-\frac{\sigma_{mp}^2}{2g}(\sigma_m\sigma_{p-m}-\sigma_p^2)$$

$$H_{mp}=(\sigma_p^2-\sigma_{mp}^2)/(k_p-k_{mp})$$

$$k_{mp}=k_m+k_{p-m}$$

$$\sigma_{mp}^2=gk_{mp}\tanh(k_{mp}d)$$

`src/swancom4.ftn:3163` `WLM2 = GRAV * KLM * TANH(KLM*DEP)`; `src/swancom4.ftn:3174` `S = ( W1*W1 - WLM2 ) / ( K1 - KLM )`.

## B.7 DCTA — Distributed Collinear Triad Approximation (Booij et al. 2009, Eq 2.106-2.108)

quadruplet 유추 heuristic — 모든 super harmonic 생성 + $k^{-4/3}$ universal tail. 원식 (Booij 2009):
$$S_{nl3}(\sigma_1)=\lambda\sin(-\beta)\widetilde k^{1-p}d^{-2}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]N_3[\sigma_2c_{g,2}k_2^pN_2-\sigma_1c_{g,1}k_1^pN_1]d\sigma_2 \quad \text{(2.106)}$$

(swantech PDF 51쪽 / 인쇄 43쪽)
- quasi-resonance $\sigma_3 = |\sigma_2-\sigma_1|$ (주파수 일치, 파수 불일치). $\lambda$=calibration, $\tilde{k}=\tilde{\sigma}/\sqrt{gd}$ ($\tilde{\sigma}$=Eq 2.66 mean), $p=4/3$ shape, $\overline{k}=(k_1+k_2+k_3)/3$. $\tanh(\overline{k}d)/\overline{k}d$ 가 파수 증가 시 resonance mismatch 반영.

**Zijlema(2022) energy-flux 보존형** (개선, 41.45 구현):
$$S_{nl3}(\sigma_1)=\lambda c_{g,1}\sin(-\beta)\widetilde k^{2-p}(\widetilde\sigma^2d^2)^{-1}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]^4E_3[c_{g,2}k_2^pE_2-c_{g,1}k_1^pE_1]d\sigma_2 \quad \text{(2.107)}$$

(swantech PDF 51쪽 / 인쇄 43쪽)

**Noncollinear 확장 (Benit-Reniers 2022, Eq 2.108)** — 각도차 기반 transfer reduction:
$$S_{nl3}(\sigma_1,\theta_1)=\lambda c_{g,1}\sin(-\beta)\widetilde k^{2-p}(\widetilde\sigma^2d^2)^{-1}\int_0^{2\pi}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]^4[G(\Delta\theta_{23})/G(0)]^2 E_3[c_{g,2}k_2^pE_2-c_{g,1}k_1^pE_1]d\sigma_2d\theta_2 \quad \text{(2.108)}$$

(swantech PDF 52쪽 / 인쇄 44쪽)
> (2.107)–(2.108)의 $S$는 코드의 작용 밀도 변화율로 읽는다. 에너지 원천항으로 표시할 때는 $\sigma_1$을 곱한다. (`src/swancom4.ftn:4386` `STRI = BETA * CG * ( SAP(ID,IS) - SAN(ID,IS) )`; `src/swancom4.ftn:4390` `IMATRA(ID,IS) = IMATRA(ID,IS) + STRI`)
>
> LTA·DCTA triad 는 **$Ur \ge 0.1$ 에서만** 계산.

## C. SWAN 옵션 매핑 (User cmd)

| Tech 식 (PDF) | User cmd | 본 위키 |
|---|---|---|
| 2.75-2.79 DIA quadruplet | `QUADRUPL` (default Hasselmann 1985) | [swan-source-terms-implementation](../source-analysis/wave/swan-source-terms-implementation.md) |
| 2.80-2.89 WRT/XNL exact | `QUADRUPL ... iquad=51/52/53` | [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md) |
| 2.100 FTIM | `TRIAD FTIM` (41.51) | (없음) |
| 2.101 SPB | `TRIAD SPB` | (없음) |
| 2.102 LTA / 2.103 ext-LTA | `TRIAD LTA` | (없음) |
| 2.106-2.107 DCTA | `TRIAD DCTA` | (없음) |
| 2.108 noncollinear DCTA | `TRIAD DCTA ... ` (Benit-Reniers) | (없음) |
| interaction coeff (B.6) | `TRIAD ... ` (Freilich/MadsenSørensen/Bredmose/QuadWave) | (없음) |

## D. 버전 history (§2.3.4)

- DIA: SWAN 초기부터 (Hasselmann 1985, Tolman 1993 수정)
- WRT/XNL: Van Vledder(2006) — [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md)
- **41.45**: DCTA Zijlema(2022) energy-flux 보존형(2.107) + De Wit(2022) biphase + Benit-Reniers noncollinear(2.108)
- **41.51**: FTIM(2.100) 신설 + extended LTA(2.103) + 4 interaction coeff(QuadWave/Akrish 2024)

## E. 원문 대조

- DCTA (2.107)–(2.108)는 같은 작용 밀도 정규화이다. (swantech PDF 51–52쪽 / 인쇄 43–44쪽)
- Bredmose·QuadWave의 분모는 $H_{mp}$이다. (swantech PDF 50–51쪽 / 인쇄 42–43쪽; `src/swancom4.ftn:3174` `S = ( W1*W1 - WLM2 ) / ( K1 - KLM )`)

## F. 연결

- [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) — §2.3.1 brief nonlinear 서술
- [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) — §2.3.3 (Eq 2.43-2.74)
- [swan-tech-ch2-vegetation-ice-bragg-gen12](swan-tech-ch2-vegetation-ice-bragg-gen12.md) — §2.3.5-8 (Eq 2.109+, noncollinear DCTA 2.108 직전 연결)
- [swan-xnl4-exact-quadruplet](../source-analysis/swan-xnl4-exact-quadruplet.md) — WRT/XNL source-analysis (mod_xnl4v5.ftn90)
- [swan-source-terms-implementation](../source-analysis/wave/swan-source-terms-implementation.md) — DIA implementation


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md) · [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-077 | 4파 상호작용 · swantech PDF 37쪽 / 인쇄 29쪽, (2.77) | swantech PDF 37쪽 / 인쇄 29쪽, (2.77) $(\delta S_0,\delta S_+,\delta S_-)^T=(2,-1,-1)^T C_{nl4}(2\pi)^2g^{-4}(\sigma/2\pi)^{11}[E_0^2\{E_+/(1+\lambda)^4+E_-/(1-\lambda)^4\}-2E_0E_+E_-/(1-\lambda^2)^4]$. | `src/swancom4.ftn:251` `DAL1 = 1. / (1.+PQUAD(1))**4`; `src/swancom4.ftn:253` `DAL3 = 2.*DAL1*DAL2`; `src/swancom4.ftn:1480` `SA1A = E00 * ( EP1 * DAL1 + EM1 * DAL2 ) * PQUAD(2)`; `src/swancom4.ftn:1481` `SA1B = SA1A - EP1 * EM1 * DAL3 * PQUAD(2)`; `src/swancom4.ftn:1485` `SA1 (IS,ID) = FACTOR * SA1B`; `src/swancom4.ftn:1524` 의 `- 2.`; 1525–1532의 양의 이웃 기여 | B | 문서와 코드의 대괄호 안은 같은 부호이다. 교환 벡터는 코드에서 $(-2,+1,+1)$이다. 문서는 벡터 전체의 부호를 반대로 인쇄했다. `UE=2πσN`을 세 번 곱하고 출력에서 `2πσ`로 나누므로 문서의 $(2π)^2$는 맞다. `src/swanmain.ftn:1454` `PQUAD(2) = 3.E7`은 기본 계수와 같다. |
| R2:SS-215 | 4파 상호작용 · swantech PDF 39쪽 / 인쇄 31쪽, 무번호 | swantech PDF 39쪽 / 인쇄 31쪽, 무번호 $C_{sh1}=5.5,C_{sh2}=5/6,C_{sh3}=-5/4$; 본문 `a lower limit of kp = 0.5`, $R_{max}=4.43$, $k_p=.75\widetilde k$. | `src/swanmain.ftn:1455` `PQUAD(3) = 5.5`; `src/swanmain.ftn:1456` `PQUAD(4) = 0.833`; `src/swanmain.ftn:1457` `PQUAD(5) = -1.25`; `src/swancom4.ftn:1410`의 `X = MAX ( 0.75 * DEP2(KCGRD(1)) * KMESPC , 0.5 )` | B | 하한의 대상은 파수 $k_p$가 아니라 무차원 수심 $k_pd$이다. DIA 상수 `.833`은 $5/6$을 세 자리로 반올림한 값이다. XNL의 2815행은 `5./6.`을 사용한다. 두 구현의 마지막 자릿수는 같지 않다. |
| R2:SS-231 | 3파 상호작용의 유도식 · swantech PDF 42쪽 / 인쇄 34쪽, 무번호 | swantech PDF 42쪽 / 인쇄 34쪽, 무번호 $\eta(x,t)=\sum_{p=-\infty}^\infty A_p(x)\exp[i(\omega_pt-\psi_p(x))]$; $d\psi_p/dx=k_p$; $\omega_p^2=gk_p\tanh(k_pd)$; $A_{-p}=A_p^*,\omega_{-p}=-\omega_p,\psi_{-p}=-\psi_p$. | `src/swancom4.ftn:4324` `E(:) = AC2(ID,:,KCGRD(1)) * SPCSIG(:)`; 5154행은 `ED(:) = ED(:) * 2. * PI * SPCSIG(:)`를 사용한다 | H | 수면의 복소 진폭 표현은 통계 원천항의 유도 출발점이다. 이 루틴들은 시간별 수면이나 위상을 복원하지 않는다. 분산 관계는 전달계수의 파수 입력에도 적용한다. |
| R2:SS-232 | 3파 상호작용의 유도식 · swantech PDF 42쪽 / 인쇄 34쪽, 무번호 | swantech PDF 42쪽 / 인쇄 34쪽, 무번호 $dA_p/dx=-S_pA_p-i\sum_{m=-\infty}^\infty R_{(m,p-m)}A_mA_{p-m}\exp[-i(\psi_m+\psi_{p-m}-\psi_p)]$; $R_{(l,k)}=R_{(k,l)}$; $C_p=A_p\exp[-i\psi_p]$. | `src/swancom4.ftn:3048` 이하 `TCOEF`; `src/swancom4.ftn:5288` `STRI = 2.*CSUM(ID,IS) - 4.*CDIF(ID,IS)` | H | 코드는 유도 후의 통계 원천항을 계산한다. 복소 진폭의 공간 미분 방정식을 따로 풀지 않는다. |
| R2:SS-090 | 3파 상호작용의 유도식 · swantech PDF 43쪽 / 인쇄 35쪽, (2.90) | swantech PDF 43쪽 / 인쇄 35쪽, (2.90) $dC_p/dx=-ik_pC_p-i\sum_{m=-\infty}^\infty R_{(m,p-m)}C_mC_{p-m}$. | `src/swancom4.ftn:5288` `STRI = 2.*CSUM(ID,IS) - 4.*CDIF(ID,IS)` | H | 문서는 이 식에서 (2.92)를 유도한다. 코드는 폐쇄 후의 에너지 전달량을 계산한다. |
| R2:SS-091 | 3파 상호작용의 유도식 · swantech PDF 43쪽 / 인쇄 35쪽, (2.91) | swantech PDF 43쪽 / 인쇄 35쪽, (2.91) $dC_p/dx=-ik_pC_p-i\sum_{m=1}^{p-1}R_{(m,p-m)}C_mC_{p-m}-2i\sum_{m=1}^\infty R_{(p+m,-m)}C_m^*C_{p+m}$. | `src/swancom4.ftn:5219`의 `CSUM`; `src/swancom4.ftn:5273` 의 `CDIF`; `src/swancom4.ftn:5288` 의 `2.`·`4.` | H | 합 상호작용과 차 상호작용의 유도식이다. 최종 통계식의 상대 계수 1 대 2가 코드에 남는다. |
| R2:SS-233 | 3파 상호작용의 유도식 · swantech PDF 43쪽 / 인쇄 35쪽, 무번호 | swantech PDF 43쪽 / 인쇄 35쪽, 무번호 $E_p=\langle C_pC_p^*\rangle$; $B_{m,p-m}=\langle C_mC_{p-m}C_p^*\rangle$; $dE_p/dx=\langle C_p^*dC_p/dx\rangle+\langle C_pdC_p^*/dx\rangle$. | `src/swancom4.ftn:5205`–5207의 `EE1`·`EE2`·`EE3`는 에너지 곱이다 | H | 모멘트의 정의와 곱 미분 규칙이다. 코드는 개별 복소 진폭의 앙상블을 생성하지 않는다. |
| R2:SS-234 | 3파 상호작용의 유도식 · swantech PDF 43쪽 / 인쇄 35쪽, 무번호 | swantech PDF 43쪽 / 인쇄 35쪽, 무번호 $dB_{m,p-m}/dx=\langle C_{p-m}C_p^*dC_m/dx\rangle+\langle C_mC_p^*dC_{p-m}/dx\rangle+\langle C_mC_{p-m}dC_p^*/dx\rangle$. | `src/swancom4.ftn:5217` `STRI = CC1*EE1 - CC2*EE2 - CC3*EE3` | H | 세 복소 진폭의 곱 미분이다. 코드가 사용하는 세 에너지 곱의 유도 근거이다. |
| R2:SS-235 | 3파 상호작용의 유도식 · swantech PDF 44쪽 / 인쇄 36쪽, 무번호 | swantech PDF 44쪽 / 인쇄 36쪽, 무번호 $dB_{m,p-m}/dx=-i\Delta kB_{m,p-m}+i\sum_{n=-\infty}^{\infty}[R_{(n,p-n)}T_{m,p-m,n}-R_{(n,p-m-n)}T_{m,n,p-m-n}-R_{(n,m-n)}T_{n,m-n,p-m}]$; $\Delta k=k_{p-m}+k_m-k_p$; $T_{m,n,p-m-n}=\langle C_mC_nC_{p-m-n}C_p^*\rangle$. | `src/swancom4.ftn:3496` `DK = K3 + K2 - K1` | H | 4차 모멘트 방정식은 폐쇄 이전의 유도식이다. 파수 불일치 $\Delta k$는 코드에서 직접 계산한다. [10-13 결론 검증 정정] |
| R2:SS-093 | 3파 상호작용의 유도식 · swantech PDF 44쪽 / 인쇄 36쪽, (2.93) | swantech PDF 44쪽 / 인쇄 36쪽, (2.93) $T_{m,n,p-m-n}=E_mE_n\delta_{np}+E_nE_p\delta_{mp}+E_mE_p\delta_{n(-m)}+c_4$. | `src/swancom4.ftn:5205`–5207의 에너지 곱; 5217의 세 항 | H | 준 Gaussian 또는 Holloway 폐쇄를 선택하기 위한 통계 항등식이다. $T$나 $c_4$ 자체는 상태 변수로 적분하지 않는다. |
| R2:SS-236 | 3파 상호작용의 유도식 · swantech PDF 44쪽 / 인쇄 36쪽, 무번호 | swantech PDF 44쪽 / 인쇄 36쪽, 무번호 $c_4=0$이면 $dB_{m,p-m}/dx=-i\Delta kB_{m,p-m}+2i[R_{(m,p-m)}E_mE_{p-m}-R_{(p,-m)}E_mE_p-R_{(m-p,p)}E_{p-m}E_p]$; Holloway는 $dB_{m,p-m}/dx=-i\Delta kB_{m,p-m}+2i[R_{(m,p-m)}E_mE_{p-m}-R_{(p,-m)}E_mE_p-R_{(m-p,p)}E_{p-m}E_p]-KB_{m,p-m}$, $K>0$이다. 통합식 $dB_{m,p-m}/dx=-i\Psi B_{m,p-m}+2i[R_{(m,p-m)}E_mE_{p-m}-R_{(p,-m)}E_mE_p-R_{(m-p,p)}E_{p-m}E_p]$. | `src/swancom4.ftn:3517` `IF ( ITRIAD.EQ.2 ) THEN`; `src/swancom4.ftn:3521` `FT = KB * DF / (DK*DK + KB*KB)`; `src/swancom4.ftn:3525` `FT = DF / MAX(ABS(DK),0.1*K1)` | H | SPB와 FTIM의 대수적 폐쇄를 유도한다. 코드는 시간·공간 의존 $B$ 방정식을 적분하지 않는다. [10-13 결론 검증 정정] |
| R2:SS-094 | 3파 상호작용의 유도식 · swantech PDF 45쪽 / 인쇄 37쪽, (2.94) | swantech PDF 45쪽 / 인쇄 37쪽, (2.94) $\Psi=\Delta k$. | `src/swancom4.ftn:3525` `FT = DF / MAX(ABS(DK),0.1*K1)` | H | 준 Gaussian 유도식의 정의이다. 최종 FTIM의 분모 제한은 SS-100에서 판정한다. |
| R2:SS-095 | 3파 상호작용의 유도식 · swantech PDF 45쪽 / 인쇄 37쪽, (2.95) | swantech PDF 45쪽 / 인쇄 37쪽, (2.95) $\Psi=\Delta k-iK$. | `src/swancom4.ftn:3521` `FT = KB * DF / (DK*DK + KB*KB)` | H | Holloway 유도식의 정의이다. 코드는 $1/\Psi$의 허수 부분을 실수 연산으로 계산한다. |
| R2:SS-100 | 3파 상호작용의 계산식과 계수 · swantech PDF 46쪽 / 인쇄 38쪽, (2.100) | swantech PDF 46쪽 / 인쇄 38쪽, (2.100) $S_{nl3}(f_p)=2\alpha_{FTIM}c_{g,p}[\sum_{m=1}^{p-1}R_{(m,p-m)}\Delta f_mQ_{m,p-m}\sin(-\beta_{m,p-m})/\lvert\Delta k_{m,p-m}\rvert-2\sum_{m=1}^{\infty}R_{(p+m,-m)}\Delta f_mQ_{m,p}\sin(-\beta_{m,p})/\lvert\Delta k_{m,p}\rvert]$. | `src/swancom4.ftn:3525` `FT = DF / MAX(ABS(DK),0.1*K1)`; `src/swancom4.ftn:3528` 의 `PTRIAD(1)*FT*CG1*RINT`; 3600의 같은 제한; 5288의 합 | C | 코드는 $\lvert\Delta k\rvert$에 $0.1k_1$ 하한을 둔다. 큰 공명 증폭을 제한한다. 전달계수·군속도·2 대 4의 계수는 같다. |
| R2:SS-219 | 3파 상호작용의 계산식과 계수 · swantech PDF 47쪽 / 인쇄 39쪽, 무번호 원래 | swantech PDF 47쪽 / 인쇄 39쪽, 무번호 원래 $K=.95k_{op}-.75$; SWAN $K=.95k_{peak}$; 원문 `This is implemented in SWAN.` | `src/swancom4.ftn:3519` `KM = MIN(K1,K2,K3)`; `src/swancom4.ftn:3520` `KB = PTRIAD(6)*KM + PTRIAD(7)`; `src/swanpre1.ftn:3376`의 기본 `0.95`; 3377의 기본 `0.0` | C | 코드가 사용하는 파수는 국소 스펙트럼의 첨두 파수가 아니다. 상호작용하는 세 성분의 최소 파수이다. `src/swanmain.ftn:1442`–1448의 주석은 음의 절편을 제거한 이유를 명시한다. |
| R2:SS-220 | 3파 상호작용의 계산식과 계수 · swantech PDF 48쪽 / 인쇄 40쪽, 무번호 | swantech PDF 48쪽 / 인쇄 40쪽, 무번호 $f_p<2.5\widetilde f$에서만 LTA 계산. | `src/swanpre1.ftn:3351` `CALL INREAL ('CUTFR', PTRIAD(2), 'STA', -1.)`; 3419의 구형 기본 `2.5`; `src/swancom4.ftn:3956`의 `ITRIAD.EQ.1` 및 `.NOT.PTRIAD(2).NE.-1.` 분기 | C | 최신 LTA 기본값은 주파수 상한을 사용하지 않는다. `2.5`는 구형 LTA 기본값이다. C는 swantech PDF 48–49쪽 / 인쇄 40–41쪽에 현재 확장 LTA 기본값 `CUTFR=-1`의 전 주파수 처리가 없는 점이다. 원래 LTA 설명의 2.5를 모든 LTA 선택에 적용하지 않는다. [10-13 결론 검증 보완] |
| R2:SS-106 | 3파 상호작용의 계산식과 계수 · swantech PDF 51쪽 / 인쇄 43쪽, (2.106) | swantech PDF 51쪽 / 인쇄 43쪽, (2.106) $S_{nl3}(\sigma_1)=\lambda\sin(-\beta)\widetilde k^{1-p}d^{-2}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]N_3[\sigma_2c_{g,2}k_2^pN_2-\sigma_1c_{g,1}k_1^pN_1]d\sigma_2$. | `src/swancom4.ftn:3694`의 `FT**4`; `src/swancom4.ftn:4324` 의 `E(:) = AC2(ID,:,KCGRD(1)) * SPCSIG(:)` | H | 문서는 이 식을 `original expression`으로 소개한다. 이어서 41.45부터 개정식 (2.107)을 구현했다고 명시한다. |
| R2:SS-107 | 3파 상호작용의 계산식과 계수 · swantech PDF 51쪽 / 인쇄 43쪽, (2.107) | swantech PDF 51쪽 / 인쇄 43쪽, (2.107) $S_{nl3}(\sigma_1)=\lambda c_{g,1}\sin(-\beta)\widetilde k^{2-p}(\widetilde\sigma^2d^2)^{-1}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]^4E_3[c_{g,2}k_2^pE_2-c_{g,1}k_1^pE_1]d\sigma_2$. | `src/swancom4.ftn:4317` `BETA = PTRIAD(1) / FT2 * SINBPH * KM**(2.-P)`; `src/swancom4.ftn:3694–3695` 의 `FT**4 * CG1 * K1**P`·성분 2; `src/swancom4.ftn:4386` `STRI = BETA * CG * ( SAP(ID,IS) - SAN(ID,IS) )`; `src/swancom4.ftn:4390` `IMATRA(ID,IS) = IMATRA(ID,IS) + STRI` | F | 이 식의 좌변은 코드에서 작용 밀도 원천항 $S_N$이다. $[E(\sigma)]=L^2T$를 넣으면 우변 차원도 $L^2T=[\partial_tN]$이다. 2.27의 에너지 원천항과는 $S_E=\sigma S_N$ 관계이다. 따라서 코드에 추가 $1/\sigma$가 없다는 이유만으로 결함이라고 판정하지 않는다. |
| R2:SS-108 | 3파 상호작용의 계산식과 계수 · swantech PDF 52쪽 / 인쇄 44쪽, (2.108) | swantech PDF 52쪽 / 인쇄 44쪽, (2.108) $S_{nl3}(\sigma_1,\theta_1)=\lambda c_{g,1}\sin(-\beta)\widetilde k^{2-p}(\widetilde\sigma^2d^2)^{-1}\int_0^{2\pi}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]^4[G(\Delta\theta_{23})/G(0)]^2 E_3[c_{g,2}k_2^pE_2-c_{g,1}k_1^pE_1]d\sigma_2d\theta_2$. | `src/swancom4.ftn:4757`의 `SANDN(COS23)`; `src/swancom4.ftn:4761` `FT2 = FT * FT`; `src/swancom4.ftn:4765–4766` 의 `QTL2(J,1) * FT2 * E3 * E1`·성분 2; `src/swancom4.ftn:4768` `DS2DD = FRINTF * SIG2 * DDIR`; 4795의 우변 가산 | F | (2.107)과 같은 작용 밀도 정규화이다. 각도 함수의 제곱과 두 적분 측도는 일치한다. 문서에 없는 작은 에너지 절단은 SS-520이다. |
| R2:SS-222 | 3파 상호작용의 계산식과 계수 · swantech PDF 49–51쪽 / 인쇄 41–43쪽 | swantech PDF 49–51쪽 / 인쇄 41–43쪽, $m=.63$의 안정성·관측 일치, 원래 QuadWave $\alpha_2=1.4$가 고주파 에너지를 과대평가한다는 설명. | `src/swancom4.ftn:3093`–3094 주석 `note: original value of 1.4 yields too much` / `energy in high-frequency part` | H | 문서의 $m=.63$과 QuadWave 계수 선택은 관측·안정성·고주파 에너지에 관한 보정 근거이다. 코드 주석도 원래 값 1.4의 고주파 과대평가를 설명한다. 독립 실행식의 구현 누락이 아니므로 H이다. [10-13 결론 검증 정정] |
| R2:SS-518 | LTA의 방향 적분, 양의 source 제한, 3배 주파수 상호작용 | swantech PDF 48–49쪽 / 인쇄 40–41쪽은 LTA·확장 LTA와 3배 주파수 기여를 설명한다. swanuse PDF 75쪽 / 인쇄 67쪽은 `LTA`가 확장 LTA를 활성화한다고 적는다. 부록 C 139/131은 `DINT` 입력을 제시한다. | `src/swancom4.ftn:3968`의 `PTRIAD(8)`; `src/swancom4.ftn:4030` 의 `MAX(0.,FT*`; `src/swancom4.ftn:4080` 의 `SA(ID,IS) - 2.`; `src/swancom4.ftn:4085` 의 `SA3(ID,IS)`; `src/swanpre1.ftn:3352`의 `DINT`; `src/swanpre1.ftn:3352` `CALL INREAL ('DINT' , PTRIAD(8), 'STA',60.0)` | C | 3배 주파수 상호작용은 swantech (2.103)과 사용자 매뉴얼에 있다. C는 방향 적분의 기본 폭 60도와 음수 제거 순서가 해당 식에 없는 점이다. 코드는 $\sin(-\beta)$를 포함한 `FT`까지 곱한 뒤 `MAX(0.,...)`를 적용한다. (2.102)는 그 인자를 양수 부분 연산 밖에 적는다. 음의 이중 위상각에서는 두 순서의 결과가 같다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-519 | FTIM/SPB의 방향 평균 곱과 이산 합·차 상호작용 | swanuse 부록 C 139/131은 FTIM·SPB의 `DINT` 입력을 제시한다. | `src/swancom1.ftn:7552` `IF ( ICUR .EQ. 0 .OR. ITER .GT. 1 ) THEN`; `src/swancom4.ftn:5205`–5207의 대칭 평균; `src/swancom4.ftn:5217` 의 `CC1*EE1 - CC2*EE2 - CC3*EE3`; `src/swancom4.ftn:5288` `STRI = 2.*CSUM(ID,IS) - 4.*CDIF(ID,IS)`; `src/swanpre1.ftn:3378`·3390·3409·3412의 기본값은 `-1.`이다 | C | 방향 적분 옵션은 방향별 스펙트럼과 방향 평균 스펙트럼의 곱을 대칭화한다. FTIM/SPB의 `DINT=-1` 기본값은 전 방향이다. 음의 결과는 작용 밀도로 나눈 상대 감쇠율로 조립한다. 연속식 (2.99)의 별도 물리 계수라고 해석하지 않는다. 흐름이 있는 첫 반복에는 3파 계산을 건너뛴다. C는 swantech PDF 46–47쪽 / 인쇄 38–39쪽에 방향 평균 곱의 대칭화와 흐름이 있는 첫 반복의 호출 예외가 없는 점이다. 방향 적분 옵션 자체는 부록에 있다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-520 | DCTA 비공선 3파 경로의 작은 에너지 절단과 Sand 전달함수의 내부 계산 | swantech PDF 52쪽 / 인쇄 44쪽, (2.108) $S_{nl3}(\sigma_1,\theta_1)=\lambda c_{g,1}\sin(-\beta)\widetilde k^{2-p}(\widetilde\sigma^2d^2)^{-1}\int_0^{2\pi}\int_0^\infty[\tanh(\bar kd)/(\bar kd)]^4[G(\Delta\theta_{23})/G(0)]^2 E_3[c_{g,2}k_2^pE_2-c_{g,1}k_1^pE_1]d\sigma_2d\theta_2$. | `src/swancom4.ftn:4622`의 `1.E-4 * ETOT`; 4691의 벡터 차 크기 `K12 = SQRT(K1*K1 + K2*K2 - 2. * K1 * K2 * COS12)`; `src/swancom4.ftn:4747` 의 `ETRSH` 비교; `src/swancom4.ftn:4757` 의 `SANDN` 호출; `src/swancom4.ftn:4919` 의 `(GHC-FACC+C)/(GH1-FAC1+C)` | C | (2.108)은 비공선 적분을 적지만 에너지 절단과 $G$의 내부 식은 적지 않는다. 비공선 선택은 방향을 바꾸는 삼중항을 보간한다. 입력 parser는 이 선택을 DCTA에 한정한다. [10-13 결론 검증 정정] |
| R2:SS-521 | De Wit 이중 위상각의 표 보간·Ursell 배율·범위 제한·공간 평균 | swanuse PDF 76쪽 / 인쇄 68쪽은 `DEWIT [lpar]`와 `[lpar]=0`일 때 평균화하지 않는 조건을 설명한다. | `src/swancom4.ftn:5620` `DDDS = -1. * ( DDDX * COSDIR + DDDY * SINDIR )`; `src/swancom4.ftn:5682–5685` 의 `PLBIP` 보간; `src/swancom4.ftn:5690` `BIP = RSGN * BIP * PI/6.`; `src/swancom1.ftn:5928`의 `SQRT(TANH`; `src/swancom1.ftn:5930` 의 `MAX`·`MIN` | C | 문서는 De Wit의 국소 경사·첨두주기 의존성을 소개한다. 실제 식은 표의 이중 선형 보간이다. 표 범위 밖에서는 끝값을 쓴다. 이중 위상각을 $[-\pi/2,\pi/2]$로 제한한다. Saprykina 경로는 별도 계산이다. C는 swantech PDF 49쪽 / 인쇄 41쪽에 표 보간·끝값·Ursell 배율·범위 제한의 계산 세부가 없는 점이다. 공간 평균 옵션의 존재는 swanuse에 있다. [10-13 결론 검증 보완] |
| R2:SS-713 | 노트 · manual-notes/swan-tech-ch2-nonlinear-detailed.md:43 | `manual-notes/swan-tech-ch2-nonlinear-detailed.md:43`의 `\begin{pmatrix}2\\-1\\-1\end{pmatrix}`. | `src/swancom4.ftn:1524`의 `SFNL(I,ID) = - 2. * ( SA1(I,J) + SA2(I,J) )` | B | 인쇄식의 벡터는 $(2,-1,-1)^T$이다. 같은 대괄호를 유지한 코드의 벡터는 $(-2,1,1)^T$이다. 노트에는 인쇄식과 부호 정정식을 나란히 적는다. |
| R2:SS-714 | 노트 · manual-notes/swan-tech-ch2-nonlinear-detailed.md:54 | `manual-notes/swan-tech-ch2-nonlinear-detailed.md:54` `lower limit $k_p=0.5$`; 76의 (2.88). | `src/swancom4.ftn:1410`의 `MAX (0.75 * DEP2(KCGRD(1)) * KMESPC , 0.5)`; `src/mod_xnl4v5.ftn90:7677`의 $k_3$ 적분 가중 | B | 하한은 파수 $k_p$가 아니라 무차원 $k_pd=.5$이다. (2.88)의 보완식에는 앞의 대칭 계수 2와 극좌표 면적 인자 $k_3$를 모두 적는다. |
| R2:SS-715 | 노트 · manual-notes/swan-tech-ch2-nonlinear-detailed.md:129 | `manual-notes/swan-tech-ch2-nonlinear-detailed.md:129` `local peak, **SWAN 구현**`. | `src/swancom4.ftn:3519`–3520의 `KM = MIN(K1,K2,K3)` 및 `KB = PTRIAD(6)*KM + PTRIAD(7)` | C | SPB의 문서 설명은 국소 첨두파수이다. 구현은 해당 삼중항의 최소 파수에 .95를 곱한다. 기본 절편은 0이다. [10-13 결론 검증 보완] |
| R2:SS-716 | 노트 · manual-notes/swan-tech-ch2-nonlinear-detailed.md:140 | `manual-notes/swan-tech-ch2-nonlinear-detailed.md:140` `$f_p < 2.5\tilde{f}$ 만 계산`; 192 `TRIAD ELTA`. | `src/swanpre1.ftn:3351` `CALL INREAL ('CUTFR', PTRIAD(2), 'STA', -1.)`; `src/swanpre1.ftn:3341` 의 `KEYWIS('LTA')` | C | 현재 `TRIAD LTA` 기본값은 주파수 절단을 끈다. 이전 수치형 LTA 경로의 기본 절단은 2.5이다. 3배 주파수 상호작용도 `TRIAD LTA`에서 계산한다. 별도 `TRIAD ELTA` 명령으로 소개하지 않는다. [10-13 결론 검증 보완] |
| R2:SS-717 | 노트 · manual-notes/swan-tech-ch2-nonlinear-detailed.md:172 | `manual-notes/swan-tech-ch2-nonlinear-detailed.md:172`·176·179의 `\cdots`; 207 `pdftotext garble`. | — | C | 생략한 DCTA 인자와 전달함수 전개를 이 보고서의 식으로 채운다. (2.107)–(2.108)의 $S$는 코드의 작용 밀도 변화율로 읽는다고 명시한다. 에너지 원천항으로 표시할 때는 $\sigma_1$을 곱한다. |
| R5:PN-024 | CSH2 | swanuse PDF 73쪽 / 인쇄 65쪽 `0.833333` | `src/swanmain.ftn:1456` `PQUAD(4) = 0.833` | B | CSH2의 실행 기본값은 0.833이다. |
| R7:H-112 | SPB | `website/modifications/modifications.htm:112` `An alternative for triad wave-wave interactions is added. This alternative is the Stochastic Parametric model based on the Boussinesq-type wave equations (SPB) of Becq-Girard et al. (1999).` | `src/swancom1.ftn:7560` `ELSEIF (ITRIAD.EQ.2 .OR. ITRIAD.EQ.3) THEN                     42.15`; 이력: `122b595:src/swancom1.ftn:7482` `CALL SWSPB (AC2   , DEP2  , CGO   , SPCSIG,`; 변경·대조 커밋: `7ee8981 2024-09-02 initial release (v 41.51)`; `src/swanpre1.ftn:3366–3374` `ELSE IF ( KEYWIS('SPB') ) THEN`에서 `ITRIAD = 2`; `src/swancom1.ftn:7560–7562`은 SPB·FTIM에 `CALL SWFTIM`을 사용한다 | H 현재 반영된 이력 기록 | 41.01의 SPB 추가 이력은 현재 선택자 ITRIAD=2에 반영되어 있다. 41.51 공개 커밋은 SPB 계산 호출을 SWSPB에서 SWFTIM으로 바꾸었다. 기능 추가 이력 자체는 H로 기록한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R7:H-501 | SPB 계산 비용 | `website/modifications/modifications.htm:501` `The complexity of computing triads using the SPB method (Becq-Girard et al, 1999) is greatly improved, leading to lower computing times.` | `src/swancom1.ftn:7562` `CALL SWFTIM ( AC2   , SPCSIG,` | H 코드 대조 대상 아님 | SPB 계산 시간 개선을 알리는 배포 기록이다. 현재 SPB는 SWFTIM 경로를 사용한다. 원문은 시간 개선의 측정 사례나 배수를 제시하지 않는다. [10-13 결론 검증 정정] |
| R7:H-529 | triad 개선 안내 | `website/modifications/modifications.htm:529` `Implementation of triads has been improved:` | `src/swanpre1.ftn:3350` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)`; 이력: `122b595:src/swanpre1.ftn:3295` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.8)`; `122b595:src/swanpre1.ftn:3321` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.90)`; `7ee8981:src/swanpre1.ftn:3350` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)`; `7ee8981:src/swanpre1.ftn:3375` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.90)`; 변경·대조 커밋: `7ee8981 2024-09-02 initial release (v 41.51)` | A 판 차이 | 41.10에 기록한 LTA 계수 0.8은 41.45 코드에도 있다. 41.51 공개 커밋 `7ee8981`(2024-09-02)은 LTA 계수를 1.0으로 바꾸었다. SPB 계수 0.9는 유지되었다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R7:H-531 | LTA 0.8·SPB 0.9 | `website/modifications/modifications.htm:531` `coefficient [trfac] is set to 0.8 in case of LTA and 0.9 in case of SPB` | `src/swanpre1.ftn:3350` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)`; 이력: `122b595:src/swanpre1.ftn:3295` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.8)`; `122b595:src/swanpre1.ftn:3321` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.90)`; `7ee8981:src/swanpre1.ftn:3350` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)`; `7ee8981:src/swanpre1.ftn:3375` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.90)`; 변경·대조 커밋: `7ee8981 2024-09-02 initial release (v 41.51)` | A 판 차이 | 41.10에 기록한 LTA 계수 0.8은 41.45 코드에도 있다. 41.51 공개 커밋 `7ee8981`(2024-09-02)은 LTA 계수를 1.0으로 바꾸었다. SPB 계수 0.9는 유지되었다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R7:H-532 | SPB 코드 구조·문서 개선 | `website/modifications/modifications.htm:532` `implementation SPB more structured and documented`; 해당 실행문 없음 | — | H 코드 대조 대상 아님 | 가독성·문서화 평가이다. 실행 결과의 명제가 아니다. |
| R7:H-583 | triad 보존성·안정성 | `website/modifications/modifications.htm:583` `The numerical implementation of triads is improved. It is energy-conservative and more stable.` | `src/swancom4.ftn:4030` `SA(ID,IS) = MAX(0., FT * ( EDM * (EM - E0) - ED0 * EM ))   41.44` | H 코드 대조 대상 아님 | 40.51의 triad 수치 구현을 energy-conservative와 more stable로 평가한 이력이다. 인용한 현재 SA 식만으로 구판 대비 보존 오차나 안정성 개선량을 정하지 않는다. [10-13 결론 검증 정정] |
| R7:S-056 | 구판 LTA 기본값과 현재 전달계수 | `website/settings/settings.htm:92` `<td style="border: 1px solid black;">consistent collinear LTA</td>` | `src/swanpre1.ftn:3350` `CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)`; 이력 대조: `122b595 2023-02-28 initial release (v 41.45)`; `122b595:src/swanpre1.ftn:3295` `          CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 0.8)`; `122b595:src/swanpre1.ftn:3296` `          CALL INREAL ('CUTFR', PTRIAD(2), 'STA', 2.5)`; `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/swanpre1.ftn:3350` `          CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)`; `7ee8981:src/swanpre1.ftn:3351` `          CALL INREAL ('CUTFR', PTRIAD(2), 'STA', -1.)`; `43e9bbb:src/swanpre1.ftn:3350` `          CALL INREAL ('TRFAC', PTRIAD(1), 'STA', 1.0)` | A 확정 (7ee8981 2024-09-02) | 41.45의 LTA 생략값 TRFAC=0.8·CUTFR=2.5는 41.51 공개 커밋 `7ee8981`(2024-09-02)에서 TRFAC=1.0·CUTFR=-1로 바뀌었다. 구판 설정 파일에 명시한 값을 현재 생략값으로 설명하지 않는다. [10-13 git 이력 판정] [10-13 결론 검증 보완] |
