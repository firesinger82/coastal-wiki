---
title: "Longshore Drift 이론 — radiation stress derivation + set-up + longshore current (Holthuijsen §7.4.2-3, Bowen 1969, Battjes 1974)"
topic: littoral-drift
canonical_source: self
citation_status: verified
verification_method: "Holthuijsen 2007 'Waves in Oceanic and Coastal Waters' (textbook/md/Waves-Holthuijsen2007.md, source_id: holthuijsen2007) §7.4.2 Wave momentum and radiation stress (line 8252-8755) + §7.4.3 Wave-induced set-up, set-down and currents (line 8759-8946) 직접 인용 — eq (7.4.1)~(7.4.27) 본문 인용 + Longuet-Higgins & Stewart 1962 set-down 유도 (Holthuijsen 인용 line 8859-8870) + Bowen et al. 1968 lab obs validation (Figure 7.22, line 8892). Longshore current 유도는 외부 paper Bowen (1969) J. Marine Res. 27:206-215 + Battjes (1974) IAHR — Holthuijsen body 의 longshore-current 언급 (line 8252-8254) + Battjes (1972b) 인용 (line 8946) cross-ref."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — Holthuijsen 본문 직접 인용 + Bowen/Battjes 는 외부 paper reference (PDF 미보유, formula 은 01-concept §6 의 textbook-cross-checked form)"
verification_date: 2026-05-24
related:
  - concepts/littoral-drift/01-concept.md
  - concepts/waves/02-theory.md
  - concepts/sediment-transport/02-theory.md
---

# Longshore Drift 이론 — radiation stress 유도부터 longshore current 까지

> [`01-concept.md`](01-concept.md) 의 §2 (radiation stress 정의) + §6 (longshore current 식) 의 equation-level 유도. 모든 식은 Holthuijsen 2007 (textbook/md/Waves-Holthuijsen2007.md) 의 원본 번호 인용.

## 1. Wave momentum — 출발점 (Holthuijsen §7.4.2)

> "Waves transport not just energy; they also transport momentum. Such momentum transport is equivalent to a stress and horizontal variations in this stress act as forces on the water" (Holthuijsen line 8252)

수평면 단위면적당 $x$-방향 momentum 의 깊이 적분 (Holthuijsen eq 7.4.1, line 8281):

$$q_x = \int_{-d}^{\eta} \rho u_x \, dz \cdot \Delta x \Delta y$$

단위면적당 + 시간 평균 (Holthuijsen eq 7.4.2, line 8283):

$$Q_x = \overline{\int_{-d}^{\eta} \rho u_x \, dz}$$

→ 선형 파동 이론에서 $\overline{u_x} = 0$ 이지만 surface elevation $\eta$ 의 변동이 적분 상한을 흔들어 **non-zero 시간평균 momentum** 생성. 핵심 통찰.

## 2. Radiation stress (Holthuijsen §7.4.2)

### 2.1 정의 — momentum flux tensor

수파 가 운반하는 momentum flux 와 wave-induced pressure 의 깊이적분이 결합한 stress. $x$-방향 momentum 의 $x$-방향 flux:

$$S_{xx} = \overline{\int_{-d}^{\eta} (\rho u_x^2 + p_{\text{wave}}) \, dz}$$

(Holthuijsen line 5619, 8254-8350; eq 7.4.9 로 일반화).

### 2.2 일반 표현 (선형 파동)

선형 파동에서 wave energy $E = \frac{1}{8}\rho g H^2$, group-to-phase 속도비 $n = c_g/c$ 일 때:

| 성분 | 표현 | 물리 의미 |
|---|---|---|
| $S_{xx}$ | $E\left(2n - \frac{1}{2}\right)$ (1D 진행파) | $x$-momentum 의 $x$-flux |
| $S_{xy} = S_{yx}$ | $E\, n \cos\theta\sin\theta$ | $x$-momentum 의 $y$-flux (shear) |
| $S_{yy}$ | $E\left(n - \frac{1}{2}\right)$ | $y$-momentum 의 $y$-flux |

- $\theta$ = wave incidence angle (해안 normal 과 wave ray 사이 각)
- shallow water ($kd \to 0$): $n \to 1$ → $S_{xx} \to \frac{3}{2}E$, $S_{xy} \to E\cos\theta\sin\theta$
- deep water ($kd \to \infty$): $n \to 0.5$ → $S_{xx} \to \frac{1}{2}E$, $S_{xy} \to \frac{1}{2}E\cos\theta\sin\theta$

상세 유도는 Holthuijsen Note 7C (line 8349+). 원 paper 는 Longuet-Higgins & Stewart (1962, 1963, 1964).

### 2.3 핵심 — $S_{xy}$ 가 longshore drift driver

$S_{xy}$ component (off-diagonal) 가 surf zone 에서 alongshore force 를 만들어 **longshore current** 생성. 이 부분이 [`01-concept.md §2`](01-concept.md) 의 식 $S_{xy} = E n \cos\theta \sin\theta$ 의 출처.

## 3. Wave-induced set-down / set-up (Holthuijsen §7.4.3)

### 3.1 momentum balance

수평 momentum 보존:

$$\frac{\partial S_{xx}}{\partial x} = -\rho g (d + \eta) \frac{\partial \eta}{\partial x}$$

(Holthuijsen eq 7.4.21, line 8859; $\eta$ = mean water surface, $d$ = still water depth)

### 3.2 Set-down (dissipation 없음, 1D normal 입사)

shoaling 만 있을 때 (Holthuijsen eq 7.4.22, line 8865-8872):

$$\overline{\eta} = -\frac{a^2 k}{2 \sinh(2kd)} \quad \text{(set-down, no dissipation)}$$

- $a = H/2$ = amplitude
- $k$ = wavenumber
- $d$ = local water depth

매우 얕은 물 ($\sinh(2kd) \approx 2kd$) 에서 (Holthuijsen eq 7.4.23, line 8880-8884):

$$\overline{\eta} \approx -\frac{1}{16} \frac{H^2}{d}$$

→ $H^2/d$ 비례, **음수** (해수면 하강).

### 3.3 Incipient breaking 조건

breaking 시작점 (incipient breaking): $H_{br}/d_{br} \approx 0.8$. 이 시점의 set-down (Holthuijsen line 8888):

$$\overline{\eta}_{br} \approx -\frac{1}{16} \frac{H_{br}^2}{d_{br}}$$

→ 보통 local depth 의 **4-5%** 하강.

### 3.4 Set-up (dissipation 있음, surf zone 내)

breaking 후 surf zone 에서 $dS_{xx}/dx < 0$ → 부호 반전 → mean water 상승.

$H = \gamma (d + \eta)$ (constant ratio 가정, $\gamma$ = breaker index) 로 (Holthuijsen eq 7.4.24, line 8915):

$$\frac{d\overline{\eta}}{dx} = -K \frac{dd}{dx}, \quad K = \frac{\frac{3}{8}\gamma^2}{1 + \frac{3}{8}\gamma^2}$$

incipient breaking 부터 적분 → mean waterline 의 set-up (Holthuijsen eq 7.4.26, line 8910-8920):

$$\overline{\eta}_{\text{waterline}} = \frac{5}{16} \gamma H_{br}$$

$\gamma$ 가 0.5-1.5 범위일 때 (Holthuijsen eq 7.4.27, line 8920-8925):

$$0.15 H_{br} < \overline{\eta}_{\text{waterline}} < 0.45 H_{br}$$

→ breaker 높이의 **15-45%** 가 waterline 에서의 mean sea-level 상승.

### 3.5 검증 — Bowen et al. 1968 실험실

Holthuijsen Figure 7.22 (line 8892) — Bowen, Inman & Simmons (1968) 실험실 관측 (1:12 beach slope, $\gamma = 1.2$) 이 위 식 (7.4.22, 7.4.25) 와 매우 일치. set-down 4-5% + set-up 15-45% 의 정량 확인.

## 4. Longshore current (Bowen 1969, Battjes 1974)

### 4.1 Driver — alongshore momentum balance

$S_{xy}$ component 가 cross-shore 방향으로 변하면 alongshore force 발생:

$$F_y = -\frac{\partial S_{xy}}{\partial x}$$

surf zone 에서 wave 가 breaking → $S_{xy}$ 가 cross-shore 로 단조 감소 → $F_y > 0$ → alongshore current 생성.

이 force 와 bottom friction 의 균형 (정상상태) → longshore current $v_l$ 평형값.

### 4.2 Bowen (1969) — 무차원 단순 유도

Bowen, A.J. (1969) "The generation of longshore currents on a plane beach" *J. Marine Res.* 27:206-215.

가정:
- plane beach, slope $\tan\beta$ = const
- breaker line 에서 $H_{br} = \gamma d_{br}$ (saturated)
- linear bottom friction $\tau_b = \rho c_f v_l$
- mixing 무시

breaker line ($d = d_{br}$) 에서의 평형값:

$$v_l = \frac{5\pi}{16} \frac{\tan\beta}{c_f} \sqrt{g h_{br}} \, \sin\theta_b \cos\theta_b$$

([`01-concept.md §6`](01-concept.md#6-longshore-current--battjes-1974-bowen-1969) 의 식과 동일).

- $\tan\beta$ = beach slope
- $c_f$ = bed friction coefficient
- $h_{br}$ = breaker depth ($\approx H_{br}/\gamma$)
- $\theta_b$ = breaker angle

### 4.3 Battjes (1974) — quadratic friction + mixing 확장

Battjes, J.A. (1974) "A computational model for the longshore current" IAHR.

확장:
- **Quadratic bottom friction**: $\tau_b = \rho c_f v_l |v_l|$ (실제 turbulent)
- **Horizontal mixing**: 측면 momentum exchange (eddy viscosity $\nu_t$)
- → cross-shore profile $v_l(x)$ 산출 가능 (breaker line peak + offshore/onshore decay)

profile 의 maximum 은 Bowen (1969) 의 단순 식과 같은 차수 ($v_l \sim O(1)$ m/s for typical 한국 조건), mixing 으로 분포가 부드러워짐.

Holthuijsen body 도 Battjes (1972b, 1974) 를 surf zone current literature 로 인용 (line 8946, 9062).

### 4.4 한국 typical 값

[`01-concept.md §6`](01-concept.md#6-longshore-current--battjes-1974-bowen-1969) 의 예제:
- $H_{br} = 1$ m, $\theta_b = 10°$, $\tan\beta = 0.05$, $c_f = 0.01$
- 이론값 $v_l \approx 2.6$ m/s, 실측 typical $0.5$-$1.5$ m/s
- 괴리는 (a) friction 의 비선형성 (Battjes 1974 quadratic) + (b) mixing + (c) wave 의 직선이 아닌 sinusoidal incidence 분산 때문

## 5. 에너지 → $S_{xy}$ → current 의 인과 chain

위 §1-§4 를 한 줄로:

$$\underbrace{\frac{1}{8}\rho g H^2}_{E\ \text{wave energy}} \xrightarrow{\text{group transport}} \underbrace{E n \cos\theta \sin\theta}_{S_{xy}\ \text{radiation stress}} \xrightarrow{\partial/\partial x\ \text{in surf zone}} \underbrace{-\partial S_{xy}/\partial x}_{F_y\ \text{alongshore force}} \xrightarrow{\text{friction balance}} \underbrace{v_l}_{\text{longshore current}} \xrightarrow{\text{sediment entrainment}} \underbrace{Q_l}_{\text{longshore drift}}$$

마지막 단계 ($v_l \to Q_l$, CERC formula) 는 [`01-concept.md §3`](01-concept.md#3-cerc-formula-1984-shore-protection-manual) 의 정형.

## 6. 시각 정리 — 1D beach cross-section

```
  ┌─ deep water ──┬── shoaling ──┬─ surf zone ─┐
  │   no set-down │ set-down ↓    │ set-up ↑    │ beach
  │   S_xy const  │ S_xy growing  │ S_xy ↓→ F_y │
  │               │               │ longshore   │
  └───────────────┴───────────────┴─────────────┘
       breaker line: H_br = γ·d_br (γ ≈ 0.8)
```

(Holthuijsen Figure 7.22 schematic + §7.4.3 narrative 참조)

## 7. 인용 정형

본 §의 핵심 인용 (source_id: holthuijsen2007 = Holthuijsen 2007):

- Wave momentum 정의 $Q_x = \overline{\int \rho u_x dz}$ — Holthuijsen eq 7.4.1, 7.4.2 (line 8281-8285)
- Radiation stress $S_{ij}$ general — Holthuijsen §7.4.2 (line 8254-8755)
- Shallow water $n=1$ vs deep $n=0.5$ — Holthuijsen eq 7.4.9 + Note 7C
- momentum balance $\partial S_{xx}/\partial x = -\rho g (d+\eta) \partial \eta /\partial x$ — Holthuijsen eq 7.4.21 (line 8859)
- Set-down $\overline{\eta} = -a^2 k / [2 \sinh(2kd)]$ — Holthuijsen eq 7.4.22 (line 8865)
- Set-down 매우 얕은 물 $-H^2/(16d)$ — Holthuijsen eq 7.4.23 (line 8880)
- Set-up at waterline $(5/16)\gamma H_{br}$ — Holthuijsen eq 7.4.26 (line 8910)
- Set-up range 0.15-0.45 $H_{br}$ — Holthuijsen eq 7.4.27 (line 8920)
- Bowen et al. 1968 lab validation — Holthuijsen Figure 7.22 (line 8892)
- Longshore current 식 $v_l = (5\pi/16)(\tan\beta/c_f)\sqrt{gh_b}\sin\theta_b\cos\theta_b$ — Bowen (1969) J. Marine Res. 27:206-215 ([`01-concept.md §6`](01-concept.md#6-longshore-current--battjes-1974-bowen-1969))
- Quadratic friction + mixing 확장 — Battjes (1974) IAHR ([`01-concept.md §6`](01-concept.md#6-longshore-current--battjes-1974-bowen-1969))

## 8. 관련 문헌

### Textbook (PDF 보유)
- **Holthuijsen, L.H.** (2007) *Waves in Oceanic and Coastal Waters* Cambridge University Press, Ch 7 §7.4.2-3 (source_id: holthuijsen2007)

### 외부 paper (PDF 미보유 — formula form 만 cross-check)
- **Longuet-Higgins, M.S. & Stewart, R.W.** (1962) "Radiation stress and mass transport in gravity waves" *J. Fluid Mech.* 13:481-504
- **Longuet-Higgins, M.S. & Stewart, R.W.** (1964) "Radiation stresses in water waves: a physical discussion, with applications" *Deep-Sea Res.* 11:529-562
- **Bowen, A.J., Inman, D.L., & Simmons, V.P.** (1968) "Wave 'set-down' and set-up" *J. Geophys. Res.* 73:2569-2577 (Holthuijsen Figure 7.22 의 lab 검증 source)
- **Bowen, A.J.** (1969) "The generation of longshore currents on a plane beach" *J. Marine Res.* 27:206-215
- **Battjes, J.A.** (1972b) "Radiation stresses in short-crested waves" *J. Marine Res.* 30:56-64
- **Battjes, J.A.** (1974) "A computational model for the longshore current" — IAHR

## 9. 연결

- [`01-concept.md`](01-concept.md) — 정의·CERC·Komar-Inman·Sediment Budget·한국 사례
- [`03-analysis-methods.md`](03-analysis-methods.md) (예정) — beach profile survey + tracer + RTK GPS
- [`04-code-and-tools.md`](04-code-and-tools.md) (예정) — XBeach surf module + GENESIS
- [`05-examples.md`](05-examples.md) (예정) — 한국 해변 case study
- [`concepts/waves/02-theory.md`](../waves/02-theory.md) — wave-induced momentum 의 일반 이론
- [`concepts/sediment-transport/02-theory.md`](../sediment-transport/02-theory.md) (예정) — bedload / suspended 의 일반 이론
- [`models/XBeach/source-analysis/`](../../models/XBeach/source-analysis/) — surf module 소스코드 분석 (별도 commit a9618df^ promote)
