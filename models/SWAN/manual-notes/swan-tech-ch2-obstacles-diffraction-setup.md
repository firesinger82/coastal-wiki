---
title: "SWAN swantech Ch 2.5 Obstacles + 2.5.4 Diffraction + 2.6 Wave-induced set-up verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §2.5 Modelling of obstacles (doc p.52-56, Eq 2.131-2.144) + §2.6 Wave-induced set-up (doc p.57, Eq 2.145-2.147). References: Booij 1993, Goda 1967, Seelig 1979, d'Angremond 1996, Van der Meer 2005, Holthuijsen et al. 2003, Dingemans 1987."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §2.5-2.6 직접 read via pdftotext (식 번호 context-verified) + website_markdown node25-30.md LaTeX alt-text. 식 번호는 PDF 번호 체계 (online HTML은 2.171-2.187로 +40 offset; 본 노트는 PDF 번호 2.131-2.147 사용)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 2.131-2.147 + 계수 verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-governing-equations.md
  - models/SWAN/manual-notes/swan-quasi-coherent.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
---

# swantech Ch 2.5 Obstacles + 2.5.4 Diffraction + 2.6 Set-up — verified verbatim

> swantech.pdf (v41.51) §2.5-2.6 직접 read. Sub-grid line obstacle (breakwater/dam) 의 transmission·reflection·freeboard·diffraction + wave-induced set-up. §2.7 Quasi-coherent 는 [[swan-quasi-coherent]] 별도.
>
> **식 번호 주의**: online HTML은 같은 내용에 2.171-2.187 부여(중간 식 누적 +40 offset). 본 노트는 **PDF 번호 2.131-2.147** 사용 (context-verified). 괄호에 [HTML n] 병기.

## 0. Obstacle 개념 (§2.5)

Sub-grid 접근 — obstacle 이 grid size 대비 narrow. (넓으면 bathymetric feature 로.) 3가지 영향:
- 통과/월파 시 파고 감소 (transmission)
- 반사 (reflection)
- 끝단 회절 (diffraction)

> Short-crested 파에선 diffraction 영향 작음 — tip 에서 1-2 파장 이내 제외 (Booij 1993). 입사 directional spectrum 이 너무 narrow 하지 않으면 obstacle 주변 파 합리적 표현. 수치 구현은 §3.12 ([[swan-documentation-stack]] 참조).

## 1. Transmission (§2.5.1, Eq 2.131-2.135)

투과계수 $K_t$ = downwave Hs / upwave Hs ($0 \le K_t \le 1$). 2 식 선택.

### 1.1 Goda et al. (1967) — closed-surface dam 월파

$$K_t = \begin{cases} 1, & \frac{F}{H_i} < -\beta - \alpha \\ 0.5\left[1 - \sin\left(\frac{\pi}{2\alpha}\left(\frac{F}{H_i}+\beta\right)\right)\right], & -\beta-\alpha \le \frac{F}{H_i} \le \alpha-\beta \\ 0, & \frac{F}{H_i} > \alpha-\beta \end{cases} \quad \text{(2.131) [HTML 2.171]}$$

- $F = h - d$ = freeboard (dam crest level $h$ − mean water level $d$, 둘 다 reference 기준)
- $H_i$ = upwave 입사 (유의)파고
- $\alpha, \beta$ = dam 형상 의존 (Seelig 1979), **Table 2.1**:

| case | $\alpha$ | $\beta$ |
|---|---|---|
| vertical thin wall | 1.8 | 0.1 |
| caisson | 2.2 | 0.4 |
| dam with slope 1:3/2 | 2.6 | 0.15 |

> Wave flume 실험 기반 → 엄밀히는 normal incidence. 방향 무의존 가정, 주파수 불변(에너지 스케일만 변, 형상 불변), slope 1:0.7(55°)보다 완만해야 유효.

### 1.2 d'Angremond et al. (1996) — impermeable rough low-crested dam

$$K_t = -0.4\frac{F}{H_i} + 0.64\left(\frac{B_k}{H_i}\right)^{-0.31}(1 - e^{-0.5\xi_p}) \quad \text{(2.132) [HTML 2.172]}$$
- $B_k$ = crest width, $\xi_p \equiv \tan\alpha/\sqrt{H_i/L_{0p}}$ = breaker parameter, $L_{0p} = gT_p^2/2\pi$ (deep water 파장), $\alpha$ = breakwater slope
- 제약: $0.075 \le K_t \le 0.9$ **(2.133) [HTML 2.173]**

$B_k \ge 10H_i$ 일 때 (wide crest):
$$K_t = -0.35\frac{F}{H_i} + 0.51\left(\frac{B_k}{H_i}\right)^{-0.65}(1 - e^{-0.41\xi_p}) \quad \text{(2.134) [HTML 2.174]}$$
- 제약: $0.05 \le K_t \le -0.006\frac{B_k}{H_i} + 0.93$ **(2.135) [HTML 2.175]**

> (2.132)/(2.134)는 $B_k = 10H_i$ 에서 불연속. Van der Meer(2005) 실용: $B_k<8H_i$ → (2.132), $B_k>12H_i$ → (2.134), 사이는 선형보간.

## 2. Reflection (§2.5.2)

Quay/breakwater 반사. obstacle 성격(smooth surface vs rubble-mound)에 따라 reflected field 산란 정도 상이. SWAN 은 반사를 여러 방향 wave component 로 diffuse 가능. (식 없음 — 정성 서술.)

## 3. Freeboard-dependent reflection & transmission (§2.5.3, Eq 2.136-2.137)

Obstacle flooding 시 relative freeboard $F/H_s$ 함수로 변화. Fixed 계수를 $\tanh$ 로 스케일:

$$R = \left[1 + \tanh\left(\frac{2}{\gamma_R}\frac{F}{H_s}\right)\right]\frac{R_0}{2} \quad \text{(2.136) [HTML 2.176]}$$

$$T = \left[1 + \tanh\left(-\frac{2}{\gamma_T}\frac{F}{H_s}\right)\right]\frac{T_0}{2} \quad \text{(2.137) [HTML 2.177]}$$
- $R_0, T_0$ = fixed 반사/투과 계수, $\gamma_R, \gamma_T$ = relative freeboard 범위 (계수가 min↔max 사이 변하는 위치와 일치)

> **Quay 옵션**: obstacle line 양측 수심 차 (quay 측이 얕음). 깊은→얕은(quay): 위 식. 얕은→깊은: $R=0, T=1$.

## 4. Diffraction (§2.5.4, Eq 2.138-2.144)

Phase-decoupled refraction-diffraction 근사 (Holthuijsen et al. 2003) — 2D 스펙트럼 개별 component 의 directional turning rate. Mild-slope 식 기반, phase 정보 생략(quasi-homogeneous 가정). (inhomogeneous diffraction 통계는 §2.7 [[swan-quasi-coherent]].)

무전류 ($c_\sigma=0$) 기본 전파속도:
$$c_{x,0} = \frac{\partial\omega}{\partial k}\cos\theta,\quad c_{y,0} = \frac{\partial\omega}{\partial k}\sin\theta,\quad c_{\theta,0} = -\frac{1}{k}\frac{\partial\omega}{\partial h}\frac{\partial h}{\partial n} \quad \text{(2.138) [HTML 2.178]}$$
($n$ = wave ray 수직)

Eikonal:
$$K^2 = k^2(1+\delta) \quad \text{(2.139) [HTML 2.179]}$$

Diffraction parameter:
$$\delta = \frac{\nabla(cc_g\nabla\sqrt{E})}{cc_g\sqrt{E}} \quad \text{(2.140) [HTML 2.180]}$$
($E(x,y)$ = total energy $\sim H_s^2$)

Diffraction 보정 전파속도:
$$c_x = c_{x,0}\overline{\delta},\quad c_y = c_{y,0}\overline{\delta},\quad c_\theta = c_{\theta,0}\overline{\delta} + \cdots\left(\frac{\partial\overline{\delta}}{\partial x}c_{y,0} - \frac{\partial\overline{\delta}}{\partial y}c_{x,0}\right) \quad \text{(2.141) [HTML 2.181]}$$

$$\overline{\delta} = \sqrt{1+\delta} \quad \text{(2.142) [HTML 2.182]}$$

### Smoothing (수치 안정화)

초기 계산서 $\sim2\Delta x$ 진동이 $\delta$ gradient 교란 → convolution filter:
$$E_{i,j}^n = E_{i,j}^{n-1} - 0.2[E_{i-1,j}+E_{i,j-1}-4E_{i,j}+E_{i+1,j}+E_{i,j+1}]^{n-1} \quad \text{(2.143) [HTML 2.183]}$$
($n$ = convolution iteration)

filter 폭 (표준편차):
$$\varepsilon_x \approx \frac{1}{2}\sqrt{3n}\,\Delta x \quad \text{(2.144) [HTML 2.184]}$$
> $n=6$ 최적 (공간해상도 파장의 1/5~1/10) → $\varepsilon_x \approx 2\Delta x$. $y$ 동일. Smoothing 은 **$\delta$ 계산에만** 적용 (다른 계산엔 미적용).

### Diffraction 사용 금지 조건 (4 동시충족 시)

① obstacle/coastline 이 down-wave view 상당 부분 가림, ② 거리 짧음(수 파장 미만), ③ 반사가 coherent, ④ 반사계수 유의. → harbour·반사 breakwater 정면·cliff wall 부적합. 흡수/반사 해안(만·라군·피요르드) + 간헐 obstacle(barrier island·breakwater·headland)엔 적합.

## 5. Wave-induced set-up (§2.6, Eq 2.145-2.147)

### 5.1 1D

연직적분 momentum balance (wave force = radiation stress gradient vs hydrostatic pressure gradient; 해안 평행 성분은 wave-induced current 만 유발, set-up 무):

$$\frac{dS_{xx}}{dx} + \rho g H\frac{d\overline{\eta}}{dx} = 0 \quad \text{(2.145) [HTML 2.185]}$$
($d$ = total depth incl. set-up, $\eta$ = mean surface elevation incl. set-up)

$$S_{xx} = \rho g\int\left[n\cos^2\theta + n - \frac{1}{2}\right]E\,d\sigma d\theta \quad \text{(2.146) [HTML 2.186]}$$
(radiation stress tensor)

### 5.2 2D (Dingemans et al. 1987)

Wave-induced current 는 force 의 divergence-free 부분, set-up 은 rotation-free 부분 주도. Momentum balance 의 divergence 고려 + acceleration divergence 무시:

$$\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} - \frac{\partial}{\partial x}\left(\rho g H\frac{\partial\overline{\eta}}{\partial x}\right) - \frac{\partial}{\partial y}\left(\rho g H\frac{\partial\overline{\eta}}{\partial y}\right) = 0 \quad \text{(2.147) [HTML 2.187]}$$

> **Open coast 한정** (외부 무제한 급수 — 연안·하구). Closed basin(호수)엔 부적합.

## 6. SWAN 옵션 매핑 (User cmd)

| Tech 식 (PDF) | User cmd | 비고 |
|---|---|---|
| 2.131 Goda transmission | `OBSTACLE TRANSM ... DAM` (Goda) | Seelig 1979 α,β |
| 2.132-2.135 d'Angremond | `OBSTACLE DAM ...` | low-crested, Van der Meer 2005 보간 |
| 2.136-2.137 freeboard R/T | `OBSTACLE ... FREEBOARD [gammat] [gammar] QUAY` | quay 옵션 |
| reflection | `OBSTACLE REFL [reflc] [RDIFF]` | diffuse 반사 |
| 2.138-2.144 diffraction | `DIFFRAC [idiffr] [smpar] [smnum]` | Holthuijsen 2003, $n$=smnum |
| 2.145-2.147 set-up | `SETUP` | open coast only |

## 7. 한계

- (2.141) $c_\theta$ diffraction-보정항·(2.106-style) 분모: pdftotext garble로 "$\cdots$" 처리 — PDF p.55 또는 Holthuijsen(2003) 원논문.
- §2.5.2 Reflection 은 식 없는 정성 서술 — 수치 구현(diffuse 각도 분배)은 §3.12 / source-analysis 별도.
- §2.4 ambient current (Longuet-Higgins-Stewart, $N=E/\sigma$ 보존)은 [[swan-tech-ch2-vegetation-ice-bragg-gen12]] §2.4 brief 참조.
- §2.7 Quasi-coherent → [[swan-quasi-coherent]].

## 8. 연결

- [[swan-tech-ch2-governing-equations]] — §2.1-2.2 (action balance, 전파속도 $c_x,c_y,c_\theta,c_\sigma$ 정의)
- [[swan-quasi-coherent]] — §2.7 QC (inhomogeneous diffraction 통계)
- [[swan-documentation-stack]] — 4 PDFs TOC, §3.12 numerical obstacle
- [[swan-tech-ch2-vegetation-ice-bragg-gen12]] — §2.3.5-8 + §2.4 ambient current
