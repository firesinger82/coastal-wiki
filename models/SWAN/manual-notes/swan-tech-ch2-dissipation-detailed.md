---
title: "SWAN swantech Ch 2.3.3 Dissipation of wave energy (S_ds) — whitecapping + bottom friction + depth breaking verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.3.3 Dissipation of wave energy, doc p.21-29 (Eq 2.43-2.74). Primary references: Hasselmann 1974, WAMDI 1988, Komen 1984, Günther 1992, Janssen 1991a·1991b·1992, Pierson-Moskowitz 1964, Rogers 2003, Alves-Banner 2003, Van der Westhuysen 2007·2012, Yan 1987, Plant 1982, Snyder 1981, Resio 2004, Rogers 2012, Zieger 2015, Ardhuin 2010, Hasselmann 1973 (JONSWAP), Bouws-Komen 1983, Zijlema 2012, Collins 1972, Madsen 1988, Jonsson 1966·1980, Battjes-Janssen 1978, Eldeberky-Battjes 1995, Battjes-Stive 1985, Kaminsky-Kraus 1993, Thornton-Guza 1983."
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 60줄을 R2·R5·R7 최종 보고서, 현재 코드, 웹 HTML, swantech·swanuse의 인용 쪽과 대조했다. 소산 구간의 HTML 식 번호는 PDF 번호보다 1 크다. PDF 35쪽 이미지로 (2.67)의 인쇄 괄호를 확인했다." # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.43-2.74 + coefficient values verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
last_source_check: 2026-10-13 (recovery 대조 반영)
related:
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/manual-notes/swan-tech-ch2-nonlinear-detailed.md
  - models/SWAN/source-analysis/swan-whitecapping.md
  - models/SWAN/source-analysis/swan-st6-babanin-implementation.md
---

# swantech Ch 2.3.3 Dissipation of wave energy (S_ds) — verified verbatim

> swantech.pdf (v41.51) §2.3.3 직접 read. [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) §2.3.1 의 brief 식(Eq 2.29-2.31)을 **상세 식 + tunable 계수값**으로 확장. 3 dissipation 메커니즘: whitecapping(2.43-2.58) + bottom friction(2.59-2.63) + depth-induced breaking(2.64-2.74).
>
> **식 번호 주의**: PDF(v41.51)와 online HTML이 같은 41.51이지만 HTML이 중간 식을 추가 번호 매겨 dissipation 구간에서 **HTML = PDF + 1**. 본 노트는 기존 노트([swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) 등)와 일관되게 **PDF 번호** 사용. 괄호 안에 [HTML n] 병기.

## 1. Whitecapping — Komen et al. (1984) formulation (Eq 2.43-2.48)

Hasselmann (1974) pulse-based model, wave number 재정식화(유한수심 적용 가능, WAMDI 1988):

$$\boxed{S_{\text{ds,w}}(\sigma,\theta) = -\Gamma\,\tilde{\sigma}\,\frac{k}{\tilde{k}}\,E(\sigma,\theta)} \quad \text{(2.43) [HTML 2.44]}$$

Steepness 의존 계수 $\Gamma$ — WAMDI(1988)를 Günther(1992)가 Janssen(1991a) 기반으로 adapt:

$$\Gamma = \Gamma_{\text{KJ}} = C_{\text{ds}}\left((1-\delta) + \delta\frac{k}{\tilde{k}}\right)\left(\frac{\tilde{s}}{\tilde{s}_{\text{PM}}}\right)^p \quad \text{(2.44) [HTML 2.45]}$$

- $\delta=0$ → WAMDI(1988) 식으로 환원
- $\tilde{s}_{\text{PM}} = \sqrt{3.02\times10^{-3}}$ = Pierson-Moskowitz(1964) overall steepness
- overall wave steepness: $\tilde{s} = \tilde{k}\sqrt{E_{\text{tot}}}$ **(2.45) [HTML 2.46]**

Mean 양 (WAMDI 1988):

$$\tilde{\sigma} = \left(E_{\text{tot}}^{-1}\int_0^{2\pi}\int_0^\infty \frac{1}{\sigma}E\,d\sigma d\theta\right)^{-1} \quad \text{(2.46) [HTML 2.47]}$$

$$\tilde{k} = \left(E_{\text{tot}}^{-1}\int_0^{2\pi}\int_0^\infty \frac{1}{\sqrt{k}}E\,d\sigma d\theta\right)^{-2} \quad \text{(2.47) [HTML 2.48]}$$

$$E_{\text{tot}} = \int_0^{2\pi}\int_0^\infty E(\sigma,\theta)\,d\sigma d\theta \quad \text{(2.48) [HTML 2.49]}$$

### 계수값 (2 set — wind input 식에 의존)

| Set | $C_{\text{ds}}$ | $\delta$ | $p$ | 출처 |
|---|---|---|---|---|
| **WAM Cycle 3** (Komen 1984 wind) | $2.36\times10^{-5}$ | 0 | 4 | Komen 1984, WAMDI 1988 |
| **WAM Cycle 4** (Janssen 1991a wind) | $4.10\times10^{-5}$ | 0.5 | 4 | Janssen 1992, Günther 1992, Komen 1994 |

> SWAN 은 mean(peak) period 를 구조적으로 10-20% 과소예측 (Rogers 2003 hindcast 확인). $\delta$ 를 0→1 로 조정하면 저주파 에너지 예측 개선 → **버전 40.91A 부터 $\delta=1$ 이 default**. 단 $C_{\text{ds}}$ 재튜닝 없이 $\delta$ 만 바꾸면 PM(1964) 파고 이론 한계 초과 가능.

## 2. Whitecapping — saturation-based model + Yan wind (Eq 2.49-2.57)

Van der Westhuysen(2007) 대안 — Alves-Banner(2003) wave-group 기반 적응(mean spectral steepness/wavenumber 의존성 제거, sea-swell·천수 적용 가능):

$$S_{\text{ds,break}}(\sigma,\theta) = -C'_{\text{ds}}\left(\frac{B(k)}{B_r}\right)^{p/2}(\tanh kh)^{(2-p_0)/4}\sqrt{gk}\,E(\sigma,\theta) \quad \text{(2.49) [HTML 2.50]}$$

방위각 적분 saturation:

$$B(k) = \int_0^{2\pi} c_g k^3 E(\sigma,\theta)\,d\theta \quad \text{(2.50) [HTML 2.51]}$$

- $B_r = 1.75\times10^{-3}$ (threshold saturation), $C'_{\text{ds}} = 5.0\times10^{-5}$
- $B(k) > B_r$ → breaking, $p = p_0$; $B(k)\le B_r$ → no breaking, residual ($p=0$)
- smooth transition (Alves-Banner 2003):

$$p = \frac{p_0}{2} + \frac{p_0}{2}\tanh\left[10\left(\sqrt{\frac{B(k)}{B_r}}-1\right)\right] \quad \text{(2.51) [HTML 2.52]}$$
> SWAN 에선 단순히 $p = p_0$ 로 설정.

Breaking/non-breaking 분리 (Van der Westhuysen 2007):

$$S_{\text{ds,w}}(\sigma,\theta) = f_{\text{br}}(\sigma)S_{\text{ds,break}} + [1-f_{\text{br}}(\sigma)]S_{\text{ds,non-break}} \quad \text{(2.52) [HTML 2.53]}$$

$$f_{\text{br}}(\sigma) = \frac{1}{2} + \frac{1}{2}\tanh\left[10\left(\sqrt{\frac{B(k)}{B_r}}-1\right)\right] \quad \text{(2.53) [HTML 2.54]}$$
> WESTH의 비쇄파 배경 소산은 Komen 형태를 사용한다. 이 경로의 $C_{ds}$는 $3.00\,10^{-5}$이다. (`src/swancom2.ftn:2545` `PWCAP1  = 3.00E-5`)

### Yan (1987) wind input (saturation model 과 짝)

강풍($u_*/c>0.1$)에서 성장률이 $u_*/c$ 에 quadratic (Plant 1982), 약풍에서 linear (Snyder 1981). Yan(1987) analytical fit:

$$\beta_{fit}=D(u_*/c)^2\cos(\theta-\alpha)+E(u_*/c)\cos(\theta-\alpha)+F\cos(\theta-\alpha)+H \quad \text{(2.54) [HTML 2.55]}$$

첫 항의 방향 인자는 $\cos(\theta-\alpha)$이다. $\cos^2$가 아니다. (swantech PDF 32쪽 / 인쇄 24쪽; `src/swancom3.ftn:2876` `SWINEB = TEMP3 * COSDIF - COF4`)

2 제약: $\beta_{\text{fit}}\approx\beta_{\text{Snyder}}$ for $U_5/c\approx1$ (즉 $u_*/c\approx0.036$) **(2.55)**, $\lim_{u_*/c\to\infty}\beta_{\text{fit}}=\beta_{\text{Plant}}$ **(2.56)**.

계수값 (Yan 원값과 다소 상이 — PM 1964 fetch range 에서 더 나은 fetch-limited 결과):
$$D = 4.0\times10^{-2},\quad E = 5.52\times10^{-3},\quad F = 5.2\times10^{-5},\quad H = -3.02\times10^{-4}$$

지수 $p_0$ — whitecapping(2.49)과 wind(2.54)의 frequency scaling 일치 요구 (Resio 2004): 강풍 $p_0=4$, 약풍 $p_0=2$. $u_*/c=0.1$ 중심 smooth transition:

$$p_0(\sigma) = 3 + \tanh\left[w\left(\frac{u_*}{c}-0.1\right)\right] \quad \text{(2.57) [HTML 2.58]}$$
> $w = 26$ (SWAN). 강풍 천수($p_0=4$)에선 추가 무차원 인자 $\tanh(kh)^{-1/2}$ 가 Eq 2.49 에 필요.

문서 인용은 $w=26$을 유지한다. 코드 재현용 식에는 $w=25.76$을 적는다. (`src/swancom2.ftn:2583` `P = 3. + TANH( 25.76 * (UFRIC*KWAVE(IS,1)/SPCSIG(IS)-0.1) )`; swantech PDF 32쪽 / 인쇄 24쪽)

## 3. Whitecapping — opposing current dissipation (Eq 2.58)

역류(군속도 접근 → wave blocking, steepness-induced breaking). Ris-Holthuijsen(1996): SWAN 과소예측 → Hs 과대예측. Van der Westhuysen(2012) saturation-based 추가 dissipation, relative Doppler shifting rate $c_\sigma/\sigma$ (Eq 2.13) 비례:

$$S_{\text{wc,curr}}(\sigma,\theta) = -C''_{\text{ds}}\max\left[\frac{c_\sigma(\sigma,\theta)}{\sigma},0\right]\left(\frac{B(k)}{B_r}\right)^{p/2}E(\sigma,\theta) \quad \text{(2.58) [HTML 2.59]}$$
> $C''_{\text{ds}}=0.8$, $B_r=1.75\times10^{-3}$, $p=p_0$ (Eq 2.57).

## 4. ST6 source term package (서술, Rogers 2012 / Zieger 2015)

ST6 ("Babanin et al. physics") — 비공식 NRL SWAN 2008 도입(Rogers 2012), WW3 2010 도입(Zieger 2015). WW3 공개판(v4/5) 문서가 SWAN ST6 변경의 적절한 문서. SWAN-WW3 3가지 차이:

1. **SSWELL ZIEGER** (non-breaking dissipation): WW3 v5 의 steepness 의존 계수 미구현 → SWAN 은 ST6 WW3 v4 따름 (Zieger 2015 Eq 23 vs 28).
2. **SSWELL ARDHUIN** (Ardhuin 2010 non-breaking): SWAN ST6 에서 사용 가능 (WW3/ST6엔 없고 WW3/ST4의 것).
3. **Wind speed scaling**: $U=28u_*$ (Komen 1984) → $U=S_{ws}u_*$ ($S_{ws}$ free param). $S_{ws}>28$ (SWAN $S_{ws}=32$) → tail level 개선, mean square slope 과대예측 보정 ($a_1,a_2$ 재튜닝 필요).

기타: linear wind(Cavaleri-Malanotte-Rizzoli 1981) 변경, viscous stress 계산 변경, water viscosity dissipation 추가. 본 위키 [swan-st6-babanin-implementation](../source-analysis/swan-st6-babanin-implementation.md).

## 5. Bottom friction (Eq 2.59-2.63)

3 모델 공통형:

$$S_{\text{ds,b}} = -C_b\frac{\sigma^2}{g^2\sinh^2 kd}E(\sigma,\theta) \quad \text{(2.59) [HTML 2.60]}$$

$$U_{\text{rms}}^2 = \int_0^{2\pi}\int_0^\infty \frac{\sigma^2}{\sinh^2 kd}E(\sigma,\theta)\,d\sigma d\theta \quad \text{(2.60) [HTML 2.61]}$$

| 모델 | $C_b$ | 값/출처 |
|---|---|---|
| **JONSWAP** (Hasselmann 1973) | $C_{\text{JON}}$ (상수) | $0.038$ m²s⁻³ (swell) / $0.067$ (wind-sea, Bouws-Komen 1983). **41.01 부터 0.038 통일** (Zijlema 2012 의 2차 다항 wind drag Eq 2.35 사용 시 swell/wind-sea 무관) |
| **Collins (1972)** | $C_b = C_f g U_{\text{rms}}$ | $C_f = 0.015$ |
| **Madsen (1988)** | $C_b = f_w\frac{g}{\sqrt{2}}U_{\text{rms}}$ **(2.61)** | $f_w$ = Jonsson(1966) |

Madsen friction factor (Jonsson 1966, Madsen 1988):

$$\frac{1}{4\sqrt{f_w}} + \log_{10}\left(\frac{1}{4\sqrt{f_w}}\right) = m_f + \log_{10}\left(\frac{a_b}{K_N}\right) \quad \text{(2.62) [HTML 2.63]}$$
- $m_f = -0.08$ (Jonsson-Carlsen 1976), $K_N$ = bottom roughness length scale
- near-bottom excursion amplitude: $a_b^2 = 2\int_0^{2\pi}\int_0^\infty \frac{1}{\sinh^2 kd}E\,d\sigma d\theta$ **(2.63) [HTML 2.64]**
- $a_b/K_N < 1.57$ → $f_w = 0.30$ (Jonsson 1980)

## 6. Depth-induced wave breaking (Eq 2.64-2.74)

### 6.1 Battjes-Janssen (1978) bore model (default)

$$D_{\text{tot}} = -\frac{1}{4}\alpha_{\text{BJ}}Q_b\left(\frac{\tilde{\sigma}}{2\pi}\right)H_{\max}^2 = -\alpha_{\text{BJ}}Q_b\tilde{\sigma}\frac{H_{\max}^2}{8\pi} \quad \text{(2.64) [HTML 2.65]}$$
- $\alpha_{\text{BJ}} = 1$ (SWAN), $Q_b$ = breaking fraction:

$$\frac{1-Q_b}{\ln Q_b} = -8\frac{E_{\text{tot}}}{H_{\max}^2} \quad \text{(2.65) [HTML 2.66]}$$

mean frequency (breaking 용, 위 §2.3.3 의 것과 다름):
$$\tilde{\sigma} = E_{\text{tot}}^{-1}\int_0^{2\pi}\int_0^\infty \sigma E(\sigma,\theta)\,d\sigma d\theta \quad \text{(2.66) [HTML 2.67]}$$

$Q_b$ cases ($\beta = H_{\text{rms}}/H_{\max}$):

$$Q_b = \begin{cases} 0, & \beta \le 0.2 \\ Q_0 - \beta^2\dfrac{Q_0-\exp((Q_0-1)/\beta^2)}{\beta^2-\exp((Q_0-1)/\beta^2)}, & 0.2 < \beta < 1 \\ 1, & \beta \ge 1 \end{cases} \quad \text{(2.67) [HTML 2.68]}$$
> $\beta\le0.5$ → $Q_0=0$; $0.5<\beta\le1$ → $Q_0=(2\beta-1)^2$.

$a=\exp[(Q_0-1)/\beta^2]$는 코드 및 Newton 유도와 맞는 정정식이다. 인쇄식의 괄호 오류를 고쳤다. (swantech PDF 35쪽 / 인쇄 27쪽; `src/swancom2.ftn:1762` `Z = EXP((QO-1.)/B2)`)

Eldeberky-Battjes(1995) spectral 확장:

$$S_{\text{ds,br}}(\sigma,\theta) = \frac{D_{\text{tot}}}{E_{\text{tot}}}E(\sigma,\theta) = -\frac{\alpha_{\text{BJ}}Q_b\tilde{\sigma}}{\beta^2\pi}E(\sigma,\theta) \quad \text{(2.68) [HTML 2.69]}$$

$H_{\max} = \gamma d$ ($d$ = total depth incl. set-up). Breaker parameter $\gamma$:
- BJ(1978) 원본: $\gamma=0.8$ (Miche criterion)
- **Battjes-Stive(1985): 0.6-0.83, 평균 0.73 (SWAN default)**
- Kaminsky-Kraus(1993): 0.6-1.59, 평균 0.79
- 출처군: Galvin 1972, Arcilla-Lemos 1990, Nelson 1987·1994

### 6.2 Thornton-Guza (1983) alternative

BJ와 달리 surf zone에서도 Rayleigh 분포를 유지한다고 가정한다. 매뉴얼의 `all waves will break`는 큰 파만이 아니라 전체 파고 범위에서 쇄파를 고려한다는 설명이다. 실제 쇄파 분포는 $p_b(H)=W(H)p(H)$이다. 이 설명을 $Q_b=1$이라는 무조건적 주장으로 읽지 않는다. (swantech PDF 36쪽 / 인쇄 28쪽, (2.71)–(2.72))

$$D_{\text{tot}} = -\frac{B^3\tilde{\sigma}}{8\pi d}\int_0^\infty H^3 p_b(H)\,dH \quad \text{(2.69) [HTML 2.70]}$$

$$p(H) = \frac{2H}{H_{\text{rms}}^2}\exp\left(-\left(\frac{H}{H_{\text{rms}}}\right)^2\right) \quad \text{(2.70) [HTML 2.71]}$$

$$p_b(H) = W(H)\,p(H) \quad \text{(2.71) [HTML 2.72]}$$

weighting (TG 1983, fraction 이 파고 독립):
$$W(H) = Q_b = \left(\frac{H_{\text{rms}}}{\gamma d}\right)^n \quad \text{(2.72) [HTML 2.73]}$$
> $n=4$ (calibration), $\gamma$ = breaker index (BJ 의 것과 다름!).

$$\int_0^\infty H^3 p_b(H)\,dH = Q_b\int_0^\infty H^3 p(H)\,dH = \frac{3}{4}\sqrt{\pi}\,Q_b H_{\text{rms}}^3 \quad \text{(2.73) [HTML 2.74]}$$

$$D_{\text{tot}} = -\frac{3B^3\tilde{\sigma}}{32\sqrt{\pi}\,d}\,Q_b H_{\text{rms}}^3 \quad \text{(2.74) [HTML 2.75]}$$

## 7. SWAN 옵션 매핑 (User cmd)

| Tech 식 (PDF) | User cmd | 본 위키 |
|---|---|---|
| 2.43-2.48 Komen whitecapping | `WCAPPING KOMEN [cds2] [stpm] [powst] [delta] [powk]` (swanuse PDF 71쪽 / 인쇄 63쪽; `src/swanpre1.ftn:2468–2472`) | [swan-whitecapping](../source-analysis/swan-whitecapping.md) [10-13 전수 검증 정정] |
| 2.49-2.58 saturation + Yan | `WCAPPING AB` (Alves-Banner / Van der Westhuysen) | [swan-whitecapping](../source-analysis/swan-whitecapping.md) |
| 2.58 opposing current | `WCAPPING ... CUR [cdsv]` | (없음) |
| ST6 (§4) | `GEN3 ST6 ...` + `SSWELL ZIEGER/ARDHUIN` | [swan-st6-babanin-implementation](../source-analysis/swan-st6-babanin-implementation.md) |
| 2.59-2.63 bottom friction | `FRICTION JONSWAP/COLLINS/MADSEN` | (없음) |
| 2.64-2.68 BJ breaking | `BREAKING CONSTANT 1.0 0.73` (α=1, γ=0.73) | (없음) |
| 2.69-2.74 Thornton-Guza | `BREAKING ... ` (대안) | (없음) |

## 8. 버전 history (§2.3.3 관련)

- **40.91A**: whitecapping $\delta=0\to1$ default (Rogers 2003 저주파 개선)
- **41.01**: bottom friction JONSWAP $C_{\text{JON}}=0.038$ 통일 (Zijlema 2012 wind drag와 결합)
- 2008(NRL)/2010(WW3): ST6 도입 (Rogers 2012, Zieger 2015)

## 9. 식의 정정과 정규화

- 첫 항의 방향 인자는 $\cos(\theta-\alpha)$이다. (swantech PDF 32쪽 / 인쇄 24쪽, (2.54))
- $a=\exp[(Q_0-1)/\beta^2]$는 인쇄식의 괄호 오류를 고친 정정식이다. (swantech PDF 35쪽 / 인쇄 27쪽, (2.67); `src/swancom2.ftn:1762` `Z = EXP((QO-1.)/B2)`)
- [swan-st6-babanin-implementation](../source-analysis/swan-st6-babanin-implementation.md) — ST6 백파·풍입력·너울 소산

## 10. 연결

- [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) — §2.3.1 brief(Eq 2.29-2.31) + §2.3.2 wind input
- [swan-tech-ch2-nonlinear-detailed](swan-tech-ch2-nonlinear-detailed.md) — §2.3.4 quadruplets + triads (Eq 2.75-2.108)
- [swan-whitecapping](../source-analysis/swan-whitecapping.md) — source-analysis
- [swan-st6-babanin-implementation](../source-analysis/swan-st6-babanin-implementation.md) — ST6는 Rogers 등의 별도 풍입력·백파 조합이다. Yan 풍입력과 Van der Westhuysen 백파 조합은 WESTH이다. (`src/swanpre1.ftn:2985–2986` `wind according to Rogers et al. (JTECH 2012) based on work of` / `Donelan, Babanin, Tsagareli and others`; swanuse PDF 69쪽 / 인쇄 61쪽)
- [swan-tech-ch2-governing-equations](swan-tech-ch2-governing-equations.md) — §2.1-2.2 — (2.16)의 우변은 $S_{tot}/\sigma$이다. (swantech PDF 19쪽 / 인쇄 11쪽) [10-13 전수 검증 정정]


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md) · [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-049 | 백파와 ST6 · swantech PDF 31쪽 / 인쇄 23쪽, (2.49) | swantech PDF 31쪽 / 인쇄 23쪽, (2.49) $S_{ds,break}=-C'_{ds}(B/B_r)^{p/2}(\tanh kh)^{(2-p_0)/4}\sqrt{gk}E$. | `src/swancom2.ftn:2587` `FAC1 = (B/BRKD)**(P/2.)`; `src/swancom2.ftn:2588` `FAC2 = SQRT(GRAV*KWAVE(IS,1))`; `src/swancom2.ftn:2590–2591` `WCAP(IS) = FBR * PWCAP(1) * FAC1 *` / `(FAC2/SPCSIG(IS))**(P/2.-1.) * FAC2 +` | F | 코드의 $(\sqrt{gk}/\sigma)^{p/2-1}$는 분산 관계 $\sigma^2=gk\tanh kh$에 의해 $(\tanh kh)^{(2-p)/4}$와 같다. SWAN은 문서가 명시한 $p=p_0$를 사용한다. |
| R2:SS-051 | 백파와 ST6 · swantech PDF 31쪽 / 인쇄 23쪽, (2.51) | swantech PDF 31쪽 / 인쇄 23쪽, (2.51) $p=p_0/2+(p_0/2)\tanh[10(\sqrt{B/B_r}-1)]$. 바로 뒤 원문 `In SWAN, however, p is simply set to p0 (see below).` | `src/swancom2.ftn:2583` `P = 3. + TANH( 25.76 * (UFRIC*KWAVE(IS,1)/SPCSIG(IS)-0.1) )` | H | 문서는 Alves–Banner의 이전 전이식을 설명한 뒤 SWAN에서 사용하지 않는다고 명시한다. 미구현 기능으로 해석하지 않는다. 무번호 $B>B_r\Rightarrow p=p_0$, $B\le B_r\Rightarrow p=0$도 이 이전 식의 설명이다. |
| R2:SS-055 | 백파와 ST6 · swantech PDF 32쪽 / 인쇄 24쪽, (2.55) | swantech PDF 32쪽 / 인쇄 24쪽, (2.55) $\beta_{fit}\approx\beta_{Snyder}$ for $U_5/c\approx1$ (or $u_*/c\approx0.036$). | `src/swancom3.ftn:2857`–2860의 맞춤 계수를 사용한다. 별도 Snyder 접합 방정식을 풀지 않는다 | H | 계수를 정하는 문헌의 맞춤 조건이다. 실행 중 적용하는 분기 조건이 아니다. |
| R2:SS-056 | 백파와 ST6 · swantech PDF 32쪽 / 인쇄 24쪽, (2.56) | swantech PDF 32쪽 / 인쇄 24쪽, (2.56) $\lim_{u_*/c\to\infty}\beta_{fit}=\beta_{Plant}$. | `src/swancom3.ftn:2870` `TEMP3  = ( COF1 * USTAC2 + COF2 * USTAC1 + COF3)` | H | 큰 $u_*/c$에서 2차 항이 지배한다는 맞춤 조건이다. 별도 극한 계산은 요구하지 않는다. |
| R2:SS-057 | 백파와 ST6 · swantech PDF 32쪽 / 인쇄 24쪽, (2.57) | swantech PDF 32쪽 / 인쇄 24쪽, (2.57) $p_0(\sigma)=3+\tanh[w(u_*/c-0.1)]$. 무번호 $w=26$, 강한 외력 $p_0=4$, 약한 외력 $p_0=2$, 천해 인자 $(\tanh kh)^{-1/2}$. | `src/swancom2.ftn:2583` `P = 3. + TANH( 25.76 * (UFRIC*KWAVE(IS,1)/SPCSIG(IS)-0.1) )` | F | 코드의 정확한 상수는 25.76이다. 문서의 26은 정수 단위로 반올림하면 대응하는 값이다. 이를 식의 오기로 단정하지 않고 표시 정밀도 차이로 분류한다. 문서 인용은 26을 유지한다. 코드 재현에는 25.76을 쓴다. $p_0=4$를 (2.49)에 넣으면 천해 지수는 $-1/2$이다. [10-13 결론 검증 정정] |
| R2:SS-204 | 백파와 ST6 · swantech PDF 30쪽 / 인쇄 22쪽, 무번호 Komen | swantech PDF 30쪽 / 인쇄 22쪽, 무번호 Komen $C_{ds}=2.36\times10^{-5},\delta=0,p=4$; Janssen $C_{ds}=4.10\times10^{-5},\delta=.5,p=4$; 본문 `δ is set to 1 as default since version 40.91A`. | `src/swanmain.ftn:1340` `PWCAP(1)  = 2.36E-5`; `src/swanmain.ftn:1342` `PWCAP(9)  = 2.`; `src/swanmain.ftn:1344` `PWCAP(10) = 1.`; `src/swanmain.ftn:1350` `PWCAP(3)  = 4.5`; `src/swanmain.ftn:1351` `PWCAP(4)  = 0.5`; `src/swanpre1.ftn:2918` `PWCAP(1)  = PWCAP(3) * (PWCAP(2) ** PWCAP(9))` | F | 문서는 Komen의 원래 보정값과 현재 기본값을 구분한다. Janssen의 실제 $4.5(3.02\times10^{-3})^2=4.10418\times10^{-5}$는 문서의 유효숫자 표현 $4.10\times10^{-5}$와 같다. |
| R2:SS-205 | 백파와 ST6 · swantech PDF 32쪽 / 인쇄 24쪽, 배경 소산 원문 `For this component, the parameter settings of Komen et al. (1984) are applied.` | swantech PDF 32쪽 / 인쇄 24쪽, 배경 소산 원문 `For this component, the parameter settings of Komen et al. (1984) are applied.` | `src/swancom2.ftn:2542` `! Note: use the default parameters of Komen et al. (1984) except Cds`; `src/swancom2.ftn:2543` `!       which is slightly larger`; `src/swancom2.ftn:2545` `PWCAP1  = 3.00E-5` | C | 배경 소산의 $C_{ds}$는 $2.36\times10^{-5}$가 아니라 $3.00\times10^{-5}$이다. 코드 주석이 의도적인 증가를 명시한다. [10-13 전수 검증 정정] |
| R2:SS-210 | 백파와 ST6 · swantech PDF 30쪽 / 인쇄 22쪽, 주기 과소예측 `10 to 20%`; 32/24, Yan 보정의 `better fetch-limited simulation results`; 33/25, (S_{ws}>28)의 `significant improvements to the tail level`. | swantech PDF 30쪽 / 인쇄 22쪽, 주기 과소예측 `10 to 20%`; 32/24, Yan 보정의 `better fetch-limited simulation results`; 33/25, (S_{ws}>28)의 `significant improvements to the tail level`. | — | H | 이 행은 문헌의 적용 결과와 성능 주장을 분류한다. 독립 실행식의 구현을 요구하는 항목이 아니므로 H이다. [10-13 결론 검증 정정] |
| R2:SS-067 | 바닥 마찰과 수심 쇄파 · swantech PDF 35쪽 / 인쇄 27쪽, (2.67) | swantech PDF 35쪽 / 인쇄 27쪽, (2.67) $Q_b=0$ for $\beta\le.2$; $Q_0-\beta^2[Q_0-\exp(Q_0-1)/\beta^2]/[\beta^2-\exp(Q_0-1)/\beta^2]$ for $0.2<\beta<1$; $Q_b=1$ for $\beta\ge1$. | `src/swancom2.ftn:1755` `IF ( B .LE. 0.2 ) THEN`; `src/swancom2.ftn:1756` `QBLOC = 0.0`; `src/swancom2.ftn:1757` `ELSE IF ( B .LT. 1.0 ) THEN`; `src/swancom2.ftn:1762` `Z  = EXP((QO-1.)/B2)`; `src/swancom2.ftn:1763` `QBLOC = QO - B2 * (QO-Z)/(B2-Z)`; `src/swancom2.ftn:1765` `QBLOC = 1.0` | B | 인쇄식은 `/β²`를 지수함수 밖에 놓았다. 코드와 (2.65)의 변형은 $\exp[(Q_0-1)/\beta^2]$를 요구한다. 예를 들어 $\beta=.5,Q_0=0$에서 인쇄식은 음의 $Q_b$를 낸다. |
| R2:SS-212 | 바닥 마찰과 수심 쇄파 · swantech PDF 35쪽 / 인쇄 27쪽, 무번호 | swantech PDF 35쪽 / 인쇄 27쪽, 무번호 $a_b/K_N<1.57\Rightarrow f_w=.30$. | `src/swancom2.ftn:360` `IF ( (ABRBOT / AKN ) .GT. 1.57 ) THEN`; `src/swancom2.ftn:383` `FW = 0.3` | C | 코드는 경계 $a_b/K_N=1.57$도 `.3` 분기에 포함한다. 문서는 그 경계의 처리와 거칠기 0의 대체값을 적지 않는다. |
| R2:SS-214 | 바닥 마찰과 수심 쇄파 · swantech PDF 36쪽 / 인쇄 28쪽 | swantech PDF 36쪽 / 인쇄 28쪽, $\gamma=.8$, 관측 범위 `.6–.83`와 `.6–1.59`, 평균 `.73`과 `.79`. | `src/swanpre1.ftn:2381` `CALL INREAL ('GAMMA', PSURF(2), 'STA', 0.73)` | H | 문헌의 관측·보정 범위를 설명한다. 모두를 코드 기본값으로 읽지 않는다. |
| R2:SS-507 | 바닥 마찰의 $kd<10$ 절단 | swantech PDF 35쪽 / 인쇄 27쪽, 무번호 $a_b/K_N<1.57\Rightarrow f_w=.30$. | `src/swancom2.ftn:519`의 `KD .LT. 10.`; `src/swancom2.ftn:355` `IF (.NOT. AKN.NE.0.) AKN = 0.001`; `src/swancom1.ftn:5833`–5835 `SINH_K_X_DEP_2(:) = SINH(MIN(30.,` / `KWAVE(:,1)*DEP2(KCGRD(1)))` / `)**2` | C | (2.59)–(2.63)에 없는 수치 범위 처리이다. |
| R2:SS-509 | Madsen 반복 분모가 정확한 Newton 미분과 다르다 | swantech PDF 34쪽 / 인쇄 26쪽 (2.62)의 $1/(4\sqrt{f_w})+\log_{10}[1/(4\sqrt{f_w})]=m_f+\log_{10}(a_b/K_N)$; | `src/swancom2.ftn:371` `DDUM = ( ADUM + LOG10(ADUM) - XDUM ) /`; `src/swancom2.ftn:372` `( 1.+ ( 1. / ADUM) )`; `src/swancom2.ftn:277` 의 `ADUM*log(10)` 수정 주석; `src/swancom2.ftn:368–381`의 초기값·반복·종료 조건 | C | 구현은 $a+\log_{10}a-b=0$을 풀면서 분모 $1+1/a$를 쓴다. 정확한 미분은 $1+1/(a\ln10)$이다. 277행은 `ADUM*log(10)`으로의 수정을 제안하지만 실제 372행은 `1.+(1./ADUM)`을 유지한다. 두 반복의 고정점은 같으므로 문서식의 근과 모순된다는 판정으로 확대하지 않는다. C는 swantech PDF 34–35쪽 / 인쇄 26–27쪽에 이 반복 분모·종료 조건이 없는 점이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-510 | 방향 분할 수 $K_\theta=\max(1,\mathrm{DSPR}/\theta_{crit})$로 쇄파율의 $\beta$를 나눈다 | swanuse 부록 C 138–139/130–131은 `DIRectionality [spread]`와 `FREQDep [power] [fmin] [fmax]` 옵션을 제시한다. | `src/swancom2.ftn:3326` `KTETA = MAX(1.,DSPR/((PSURF(15)/180.)*PI))`; `src/swancom2.ftn:1744` `B = B / SQRT(KTETA)`; `src/swancom2.ftn:2173` `FRFAC(IS) = FAC*SPCSIG(IS)**PP`; `src/swancom2.ftn:2177–2178` 의 `* DBLE(KTETA)` | C | 방향·주파수 의존 옵션의 존재는 사용자 매뉴얼 부록에 있다. C는 swantech PDF 35–36쪽 / 인쇄 27–28쪽 및 122–123/114–115에 `KTETA` 배율과 주파수 가중 정규화의 계산식이 없는 점이다. 인쇄한 BJ 식은 기본 `KTETA=1`과 주파수 가중 없음에 대응한다. 코드의 `FAC`는 적분 소산을 맞추는 정규화이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-511 | BJ 상대 소산의 포화 분기와 선행 조건 | swantech PDF 35쪽 / 인쇄 27쪽, (2.67) $Q_b=0$ for $\beta\le.2$; $Q_0-\beta^2[Q_0-\exp(Q_0-1)/\beta^2]/[\beta^2-\exp(Q_0-1)/\beta^2]$ for $0.2<\beta<1$; $Q_b=1$ for $\beta\ge1$. | `src/swancom2.ftn:2117`의 `WS = ( DBLE(PSURF(1)) / DBLE(PI)) * DBLE(FMEAN)`; `src/swancom2.ftn:2118` `SbrD = 0D0`; `src/swancom2.ftn:2110–2112`의 선행 조건; `src/swancom2.ftn:2122–2124`의 0 대입 | C | 강한 쇄파 구간에서 인쇄식의 단순 연장을 사용하지 않는다. BJ의 포화 처리는 `REAL(BB) .GT. 0. .AND. REAL(ABS(BB - DBLE(QB))) .GT. 0.`을 만족하고 `BB .LT. 1D0`이 거짓일 때 적용한다. `BB=QB=1`이면 `SURFA0`과 `SURFA1`을 0으로 둔다. [10-13 전수 검증 정정] |
| R2:SS-512 | 가변 쇄파지수와 특수 경로 | swantech PDF 25쪽 / 인쇄 17쪽·swantech PDF 36쪽 / 인쇄 28쪽은 가변 쇄파지수를 소개한다. swanuse PDF 73쪽 / 인쇄 65쪽는 BKD와 계수를 설명한다. 부록 C 138/130은 VAR·RUE·BKD·TG 선택을 나열한다. | `src/swancom2.ftn:3168` `BRCOEF = PSURF(4) + PSURF(7) * EXP ( -PSURF(8) / DDDS )`; 3200–3202의 선형식·제한; `src/swancom2.ftn:3238` `BRCOEF = FAC1 / TANH(FAC1/FAC2)`; `src/swancom1.ftn:5974` `BRCOEF = PSURF(4) - 0.3 * PSURF(5) * BIPH` | C | 가변 쇄파지수와 BKD의 존재는 매뉴얼에 있다. C는 swantech의 일반 설명에 인용한 각 수치식과 호출 예외가 빠진 점이다. BKD의 `FMEAN=SIGM_WAM`은 기본 `SMEBRK`와 다르다. `IGEN=4`에서는 첫 반복 이후 쇄파 조립을 0으로 만든다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-706 | 노트 · manual-notes/swan-tech-ch2-dissipation-detailed.md:84 | `manual-notes/swan-tech-ch2-dissipation-detailed.md:84`의 $D(u_*/c)^2\cos^2(\theta-\alpha)$; 199의 `표준 Yan(1987)/Van der Westhuysen(2007) 형` 재구성 설명. | `src/swancom3.ftn:2876` `SWINEB = TEMP3 * COSDIF - COF4` | B | 첫 항의 방향 인자는 $\cos(\theta-\alpha)$이다. $\cos^2$가 아니다. PDF 이미지에서 확인한 식을 쓰고 추정 재구성 표시를 제거한다. |
| R2:SS-707 | 노트 · manual-notes/swan-tech-ch2-dissipation-detailed.md:78 | `manual-notes/swan-tech-ch2-dissipation-detailed.md:78`의 `Komen 1984 설정` 배경 소산 설명; `source-analysis/swan-whitecapping.md:106` `Komen fallback`. | `src/swancom2.ftn:2545` `PWCAP1 = 3.00E-5` | C | WESTH의 비쇄파 배경 소산은 Komen 형태를 사용한다. 이 경로의 $C_{ds}$는 $3.00\,10^{-5}$이다. Komen 기본 $2.36\,10^{-5}$와 구별한다. |
| R2:SS-708 | 노트 · manual-notes/swan-tech-ch2-dissipation-detailed.md:94 | `manual-notes/swan-tech-ch2-dissipation-detailed.md:94`의 $w=26$. | `src/swancom2.ftn:2583`의 `25.76` | F | 노트의 $w=26$은 swantech PDF 32쪽 / 인쇄 24쪽의 인쇄값을 그대로 옮긴 것이다. 25.76을 정수 단위로 반올림하면 26이다. 전사 오기로 분류하지 않는다. 문서 인용은 $w=26$을 유지한다. 코드 재현용 식에는 $w=25.76$을 적는다. [10-13 결론 검증 정정] |
| R2:SS-709 | 노트 · manual-notes/swan-tech-ch2-dissipation-detailed.md:148 | `manual-notes/swan-tech-ch2-dissipation-detailed.md:148`의 `\exp((Q_0-1)/\beta^2)`; 200의 `PDF p.25`. | `src/swancom2.ftn:1762` `Z = EXP((QO-1.)/B2)` | B | $a=\exp[(Q_0-1)/\beta^2]$는 코드 및 Newton 유도와 맞는 정정식이다. 인쇄식의 괄호 오류를 고쳤다고 명시한다. 쪽 표시는 PDF 35쪽·인쇄 27쪽이다. |
| R2:SS-710 | 노트 · manual-notes/swan-tech-ch2-dissipation-detailed.md:163 | `manual-notes/swan-tech-ch2-dissipation-detailed.md:163` `모든 파 breaking`. | — | C | 노트의 `모든 파 breaking`은 매뉴얼의 표현을 옮긴 것이다. 전사 오기가 아니다. 이 문장은 큰 파만이 아니라 전체 파고 범위에서 쇄파를 고려한다는 설명으로 읽는다. 실제 쇄파 분포는 $p_b(H)=W(H)p(H)$이다. $Q_b=1$이라는 무조건적 주장으로 읽지 않도록 노트의 조건 설명을 보완한다. C의 범위는 이 노트의 확률 가중 설명이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R5:PN-182 | ST6와 WESTH 혼동 | `manual-notes/swan-tech-ch2-sources-sinks.md:274` `ST6 (Yan 1987 + Van der Westhuysen 2007)` | `src/swanpre1.ftn:2991` `IWCAP = 8` | B | Yan·Van der Westhuysen 조합은 WESTH다. ST6는 별도 Rogers 풍입력·백파 조합이다. |
| R7:H-749 | 쇄파율 근사 정확도 | `website/modifications/modifications.htm:749` `The numerical approximation of the fraction of breakers in the surfzone has changed (more accurate).`; 해당 실행문 없음 | — | H 코드 대조 대상 아님 | 변경식과 오차 기준을 적지 않은 정확도 평가이다. 구체 식을 현재 구현과 같다고 단정하지 않는다. |
| R7:S-012 | 복잡한 수심에서 가변 쇄파 권고 | `website/settings/settings.htm:151–159` `<td colspan=8 style="border: 1px solid white; padding: 0px;">Numerous studies have demonstrated the high degree of success of the constant breaker index <em>&gamma;</em><sub>BJ</sub> of` | — | H 코드 대조 대상 아님 | 상수 쇄파지수의 성공 사례와 가변 지수의 필요성은 적용성 주장이다. [10-13 결론 검증 보완] |
