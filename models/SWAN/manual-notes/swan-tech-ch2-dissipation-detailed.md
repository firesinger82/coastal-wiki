---
title: "SWAN swantech Ch 2.3.3 Dissipation of wave energy (S_ds) — whitecapping + bottom friction + depth breaking verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.3.3 Dissipation of wave energy, doc p.21-29 (Eq 2.43-2.74). Primary references: Hasselmann 1974, WAMDI 1988, Komen 1984, Günther 1992, Janssen 1991a·1991b·1992, Pierson-Moskowitz 1964, Rogers 2003, Alves-Banner 2003, Van der Westhuysen 2007·2012, Yan 1987, Plant 1982, Snyder 1981, Resio 2004, Rogers 2012, Zieger 2015, Ardhuin 2010, Hasselmann 1973 (JONSWAP), Bouws-Komen 1983, Zijlema 2012, Collins 1972, Madsen 1988, Jonsson 1966·1980, Battjes-Janssen 1978, Eldeberky-Battjes 1995, Battjes-Stive 1985, Kaminsky-Kraus 1993, Thornton-Guza 1983."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §2.3.3 직접 read via pdftotext + website_markdown node16.md LaTeX alt-text cross-check. 식 번호는 PDF 번호 체계 (website HTML은 중간 식을 추가 번호 매겨 +1 offset; 본 노트는 기존 노트와 일관되게 PDF 번호 사용). Eq 2.43-2.74 context-verified."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.43-2.74 + coefficient values verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-sources-sinks.md
  - models/SWAN/manual-notes/swan-tech-ch2-nonlinear-detailed.md
  - models/SWAN/source-analysis/swan-whitecapping.md
  - models/SWAN/source-analysis/swan-st6-babanin-implementation.md
---

# swantech Ch 2.3.3 Dissipation of wave energy (S_ds) — verified verbatim

> swantech.pdf (v41.51) §2.3.3 직접 read. [[swan-tech-ch2-sources-sinks]] §2.3.1 의 brief 식(Eq 2.29-2.31)을 **상세 식 + tunable 계수값**으로 확장. 3 dissipation 메커니즘: whitecapping(2.43-2.58) + bottom friction(2.59-2.63) + depth-induced breaking(2.64-2.74).
>
> **식 번호 주의**: PDF(v41.51)와 online HTML이 같은 41.51이지만 HTML이 중간 식을 추가 번호 매겨 dissipation 구간에서 **HTML = PDF + 1**. 본 노트는 기존 노트([[swan-tech-ch2-sources-sinks]] 등)와 일관되게 **PDF 번호** 사용. 괄호 안에 [HTML n] 병기.

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
> $S_{\text{ds,non-break}}$ 는 Eq 2.43(Komen 1984 설정)을 background dissipation 으로 사용.

### Yan (1987) wind input (saturation model 과 짝)

강풍($u_*/c>0.1$)에서 성장률이 $u_*/c$ 에 quadratic (Plant 1982), 약풍에서 linear (Snyder 1981). Yan(1987) analytical fit:

$$\beta_{\text{fit}} = D\left(\frac{u_*}{c}\right)^2\cos^2(\theta-\alpha) + E\left(\frac{u_*}{c}\right)\cos(\theta-\alpha) + F\cos(\theta-\alpha) + H \quad \text{(2.54) [HTML 2.55]}$$

2 제약: $\beta_{\text{fit}}\approx\beta_{\text{Snyder}}$ for $U_5/c\approx1$ (즉 $u_*/c\approx0.036$) **(2.55)**, $\lim_{u_*/c\to\infty}\beta_{\text{fit}}=\beta_{\text{Plant}}$ **(2.56)**.

계수값 (Yan 원값과 다소 상이 — PM 1964 fetch range 에서 더 나은 fetch-limited 결과):
$$D = 4.0\times10^{-2},\quad E = 5.52\times10^{-3},\quad F = 5.2\times10^{-5},\quad H = -3.02\times10^{-4}$$

지수 $p_0$ — whitecapping(2.49)과 wind(2.54)의 frequency scaling 일치 요구 (Resio 2004): 강풍 $p_0=4$, 약풍 $p_0=2$. $u_*/c=0.1$ 중심 smooth transition:

$$p_0(\sigma) = 3 + \tanh\left[w\left(\frac{u_*}{c}-0.1\right)\right] \quad \text{(2.57) [HTML 2.58]}$$
> $w = 26$ (SWAN). 강풍 천수($p_0=4$)에선 추가 무차원 인자 $\tanh(kh)^{-1/2}$ 가 Eq 2.49 에 필요.

## 3. Whitecapping — opposing current dissipation (Eq 2.58)

역류(군속도 접근 → wave blocking, steepness-induced breaking). Ris-Holthuijsen(1996): SWAN 과소예측 → Hs 과대예측. Van der Westhuysen(2012) saturation-based 추가 dissipation, relative Doppler shifting rate $c_\sigma/\sigma$ (Eq 2.13) 비례:

$$S_{\text{wc,curr}}(\sigma,\theta) = -C''_{\text{ds}}\max\left[\frac{c_\sigma(\sigma,\theta)}{\sigma},0\right]\left(\frac{B(k)}{B_r}\right)^{p/2}E(\sigma,\theta) \quad \text{(2.58) [HTML 2.59]}$$
> $C''_{\text{ds}}=0.8$, $B_r=1.75\times10^{-3}$, $p=p_0$ (Eq 2.57).

## 4. ST6 source term package (서술, Rogers 2012 / Zieger 2015)

ST6 ("Babanin et al. physics") — 비공식 NRL SWAN 2008 도입(Rogers 2012), WW3 2010 도입(Zieger 2015). WW3 공개판(v4/5) 문서가 SWAN ST6 변경의 적절한 문서. SWAN-WW3 3가지 차이:

1. **SSWELL ZIEGER** (non-breaking dissipation): WW3 v5 의 steepness 의존 계수 미구현 → SWAN 은 ST6 WW3 v4 따름 (Zieger 2015 Eq 23 vs 28).
2. **SSWELL ARDHUIN** (Ardhuin 2010 non-breaking): SWAN ST6 에서 사용 가능 (WW3/ST6엔 없고 WW3/ST4의 것).
3. **Wind speed scaling**: $U=28u_*$ (Komen 1984) → $U=S_{ws}u_*$ ($S_{ws}$ free param). $S_{ws}>28$ (SWAN $S_{ws}=32$) → tail level 개선, mean square slope 과대예측 보정 ($a_1,a_2$ 재튜닝 필요).

기타: linear wind(Cavaleri-Malanotte-Rizzoli 1981) 변경, viscous stress 계산 변경, water viscosity dissipation 추가. 본 위키 [[swan-st6-babanin-implementation]].

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

Eldeberky-Battjes(1995) spectral 확장:

$$S_{\text{ds,br}}(\sigma,\theta) = \frac{D_{\text{tot}}}{E_{\text{tot}}}E(\sigma,\theta) = -\frac{\alpha_{\text{BJ}}Q_b\tilde{\sigma}}{\beta^2\pi}E(\sigma,\theta) \quad \text{(2.68) [HTML 2.69]}$$

$H_{\max} = \gamma d$ ($d$ = total depth incl. set-up). Breaker parameter $\gamma$:
- BJ(1978) 원본: $\gamma=0.8$ (Miche criterion)
- **Battjes-Stive(1985): 0.6-0.83, 평균 0.73 (SWAN default)**
- Kaminsky-Kraus(1993): 0.6-1.59, 평균 0.79
- 출처군: Galvin 1972, Arcilla-Lemos 1990, Nelson 1987·1994

### 6.2 Thornton-Guza (1983) alternative

BJ 와 달리 surf zone 에서도 Rayleigh 분포 유지 가정(모든 파 breaking):

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
| 2.43-2.48 Komen whitecapping | `WCAPPING KOMEN [cds2] [stpm] [delta] [pwtail]` | [[swan-whitecapping]] |
| 2.49-2.58 saturation + Yan | `WCAPPING AB` (Alves-Banner / Van der Westhuysen) | [[swan-whitecapping]] |
| 2.58 opposing current | `WCAPPING ... CUR [cdsv]` | (없음) |
| ST6 (§4) | `GEN3 ST6 ...` + `SSWELL ZIEGER/ARDHUIN` | [[swan-st6-babanin-implementation]] |
| 2.59-2.63 bottom friction | `FRICTION JONSWAP/COLLINS/MADSEN` | (없음) |
| 2.64-2.68 BJ breaking | `BREAKING CONSTANT 1.0 0.73` (α=1, γ=0.73) | (없음) |
| 2.69-2.74 Thornton-Guza | `BREAKING ... ` (대안) | (없음) |

## 8. 버전 history (§2.3.3 관련)

- **40.91A**: whitecapping $\delta=0\to1$ default (Rogers 2003 저주파 개선)
- **41.01**: bottom friction JONSWAP $C_{\text{JON}}=0.038$ 통일 (Zijlema 2012 wind drag와 결합)
- 2008(NRL)/2010(WW3): ST6 도입 (Rogers 2012, Zieger 2015)

## 9. 한계

- Yan(2.54) β_fit 의 directional cos 거듭제곱(첫 항 quadratic): PDF pdftotext 레이아웃 garble로 표준 Yan(1987)/Van der Westhuysen(2007) 형($\cos^2$)으로 렌더 — 원 PDF 식 이미지 직접 대조 권장.
- $Q_b$ (2.67) 중간 case 의 transcendental 형: PDF text 추출이 부분 garble — 함수 구조는 정확하나 정밀 대조 시 PDF p.25 figure 확인.
- ST6(§4)는 식 미인용(WW3 문서 참조) — [[swan-st6-babanin-implementation]] source-analysis 가 canonical.

## 10. 연결

- [[swan-tech-ch2-sources-sinks]] — §2.3.1 brief(Eq 2.29-2.31) + §2.3.2 wind input
- [[swan-tech-ch2-nonlinear-detailed]] — §2.3.4 quadruplets + triads (Eq 2.75-2.108)
- [[swan-whitecapping]] — source-analysis
- [[swan-st6-babanin-implementation]] — ST6 (Yan 1987 wind + saturation whitecapping)
- [[swan-tech-ch2-governing-equations]] — §2.1-2.2 (Eq 2.16 RHS S_tot)
