---
title: "처오름대 이론 — NLSW swash 해·Iribarren scaling·runup 매개변수화·uprush/backwash 비대칭"
topic: swash-zone
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "**교과서 page 직접 확인 인용분 = verified**: (1) surf similarity(Battjes 1974) ζ=tanβ/√(H0/L0)·Dean number D=Hb/(wT)·Froude F=w/√(gHb) → coastal-processes-with-eng-apps p.26 §3.3.1 Eq(3.1)-(3.3) 본문 read 확인. (2) wave run-up R_u2% 설계파라미터·run-up 속도 Eq(2) u2%=c_u2%√(g(R_u2%−zA))·flow thickness Eq(3)·front velocity Eq(4)·계수 c_h2%=0.20(1:3,1:4)/0.30(1:6)·c_u2%=1.4-1.5·front-velocity 분포(15%/30-40%/75%) → coastal-structures-design p.20-23 §2.3 본문 read 확인. **NLSW swash 해(Shen-Meyer 1963·Antuono 2010 JFM)·Hunt 1959·Stockdon 2006 runup 식·breaker-type ξ 임계값은 본 위키 md 교과서에 본문 부재 → 문헌 cross-ref(01 §4.2·04)로만 표기, 임의 page/식 인용 안 함**. Wijetunge book pp.49-59 run-up 본문은 추출 md 에 미수록(index entry 만 존재) → 인용 안 함."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/swash-zone/01-concept.md
  - concepts/swash-zone/04-code-and-tools.md
  - concepts/waves/04-code-and-tools.md
  - concepts/littoral-drift/01-concept.md
---

# 처오름대 이론 (Swash Zone Theory)

> [[01-concept]] §1-3 의 정성 정의(uprush/backwash·bore collapse·Iribarren 체계)를 **정량 식**으로 보강. 본 노트는 (1) NLSW swash 해, (2) Iribarren(surf similarity) scaling, (3) runup 매개변수화, (4) uprush/backwash 비대칭 시간규모로 구성.

---

## 1. 비선형 천수(NLSW) swash 해

### 1.1 지배방정식

분산을 무시한 **비선형 천수방정식(non-linear shallow-water equations, NLSW)** 이 swash/surf 의 1차 모델. 1차원 cross-shore ($x$ = 해안 직각, 상향 양):

$$
\partial_t h + \partial_x(hu) = 0,\qquad
\partial_t(hu) + \partial_x\!\left(hu^2 + \tfrac{1}{2}gh^2\right) = -gh\,\partial_x z_b - \tau_b/\rho
$$

여기서 $h$ = 수심, $u$ = 수심평균 유속, $z_b$ = 바닥고, $\tau_b$ = 바닥마찰. shoreline 은 $h\to 0$ 의 이동 경계(moving wet/dry boundary)로 나타나며, swash 동역학의 핵심은 이 경계의 비정상 거동이다. (NLSW 의 swash 적용·dam-break 유사성은 [[04-code-and-tools]] §"NLSW" 행 참조.)

### 1.2 해석해 (문헌 cross-ref)

평탄 사면 위 NLSW 의 고전 swash 해는 다음 계열로 이어진다 — 본 위키 md 교과서에는 본문이 없어 **문헌 인용으로만** 표기(임의 식 번호 인용 금지):

- **Shen & Meyer (1963)** — bore collapse 후 사면 위 swash lens 의 운동을 NLSW 의 단순 탄도(ballistic) 해로 기술. 무마찰 한계에서 shoreline 입자는 초기 속도 $u_0$ 로 사면을 오르내리며, 수직 runup 한계가 $u_0^2/(2g)$ 형태로 scaling.
- **Antuono (2010, *J. Fluid Mech.* 658:166)** — cross-shore NLSW 의 정칙(regular) 해. [[01-concept]] §4.2 의 경사입사 bore 논문(arxiv:2504.18467)이 이 해를 **forward-moving characteristic 변수 $\alpha$** + Snell 굴절과 결합해 weakly-2D(longshore) swash 로 확장(Ryrie 1983, *JFM* 129:193 의 약2차원 forcing 위에).

> 이 해들의 공통 함의: swash 의 1차 거동은 분산 없이 **특성곡선(characteristics)** 으로 닫히며, runup 한계는 bore collapse 시점의 운동에너지(즉 입사파 진폭·사면)로 결정된다 → 아래 §2 Iribarren scaling 의 이론적 근거.

---

## 2. Iribarren 수(surf similarity)와 swash 체계

### 2.1 정의

해빈/구조물 사면의 쇄파·처오름 체계를 지배하는 무차원수는 **surf similarity parameter (Iribarren 수)**, Battjes (1974) 정의:

$$
\zeta \equiv \frac{\tan\beta}{\sqrt{H_0/L_0}}
$$

여기서 $\tan\beta$ = 해빈 경사, $H_0$·$L_0$ = 심해 파고·파장 ((coastal-processes-with-eng-apps, p.26 §3.3.1 Eq.(3.2))). 같은 page 에서 함께 제시되는 인접 무차원 해빈 파라미터:

| 파라미터 | 식 | 출처 |
|---|---|---|
| Dean number | $D \equiv \dfrac{H_b}{wT}$ | Eq.(3.1) |
| **surf similarity (Iribarren)** | $\zeta \equiv \dfrac{\tan\beta}{\sqrt{H_0/L_0}}$ | Eq.(3.2), Battjes 1974 |
| Froude number | $F = \dfrac{w}{\sqrt{gH_b}}$ | Eq.(3.3) |

(($H_b$ = 쇄파파고, $T$ = 주기, $w$ = 표사 침강속도 — coastal-processes-with-eng-apps, p.26 §3.3.1))

> 교과서는 세 파라미터 중 surf similarity 가 "단일 해빈 경사를 식별해야 하므로(beach face 경사인지, 쇄파선까지의 평균경사인지) 해빈 간 비교가 어렵다"는 실무적 한계를 명시한다 ((coastal-processes-with-eng-apps, p.26 §3.3.1)). → swash 연구에서 $\tan\beta$ 정의(beach-face vs 평균)에 따라 $\zeta$ 가 달라지는 점에 유의.

### 2.2 reflective vs dissipative (정성)

$\zeta$ 가 클수록(가파른 경사·긴 주기·작은 파형경사) 사면이 **반사성(reflective)** — 입사파가 사면에서 강하게 반사, plunging/surging breaker, swash 진폭 큼. 작을수록 **소산성(dissipative)** — spilling breaker, 넓은 surf zone, swash 가 infragravity(IG) 변조에 지배. 이 체계 의존성은 [[01-concept]] §4.1 bore-bore capture 가 "steeper/more reflective 일수록 극단 shoreline 최대치 구동 확률 ↑" (Stringari & Power 2019) 와 직접 부합.

> 주의: surf similarity 의 spilling/plunging/surging **임계값**(예: Battjes 의 $\zeta<0.5$ spilling 등)은 본 위키 md 교과서 본문에 수치가 부재 → 본 노트에서 임계값을 단언하지 않음(source-needed). 정성 경향만 기술.

---

## 3. runup 매개변수화

### 3.1 설계 파라미터 $R_{u2\%}$

연안구조물(제방) 설계의 처오름 핵심 파라미터는 **up-rushing wave 의 2% 가 초과하는 사면상 처오름 수위 $R_{u2\%}$** ((coastal-structures-design, p.20 §2.3)). run-up 수위가 Rayleigh 분포를 따른다고 가정하면 $R_{u2\%}$ 를 알 때 전체 처오름 수위 분포가 결정된다 ((coastal-structures-design, p.21 §2.3)). (구체 $R_{u2\%}$ 산정식은 교과서가 EurOtop Manual 2007 로 위임하고 재수록하지 않음 — 본 노트도 EurOtop 식을 임의로 옮겨 적지 않음.)

### 3.2 run-up 속도·flow thickness

설계상 처오름 수위뿐 아니라 **처오름 유속(front velocity)** 과 흐름 두께가 필요하며(잔디 사면 손상의 지배 인자 = front velocity), 불규칙파 2% 값으로:

$$
u_{2\%} = c_{u2\%}\sqrt{g\,(R_{u2\%} - z_A)}\qquad\text{(Eq. 2)}
$$
$$
h_{2\%} = c_{h2\%}\,(R_{u2\%} - z_A)\qquad\text{(Eq. 3)}
$$

여기서 $z_A$ = 사면 위 위치(처오름대 내, swl 기준), $c_{u2\%}$·$c_{h2\%}$ = 계수 ((coastal-structures-design, p.21 §2.3 Eq.(2)-(3))). 권장 계수값 ((coastal-structures-design, p.21-22 §2.3)):

- $c_{h2\%} = 0.20$ (사면 1:3·1:4), $0.30$ (1:6), 보간으로 1:5 → $0.25$ — EurOtop 의 $c_{h2\%}=0.055\cot\alpha$ 보다 이 절차를 권장.
- $c_{u2\%} = 1.4$–$1.5$ (1:3 ~ 1:6 사면).

### 3.3 front velocity 분포·최대치

Van der Meer (2011) 의 개별 처오름파 분석 결과(매끈한 제방 사면) ((coastal-structures-design, p.22 §2.3)):

- 처오름은 평균적으로 **최대 처오름 수위의 15%** 위치에서 시작하며, 그때 front velocity 가 이미 최대 front velocity 에 근접.
- front velocity 는 **최대 처오름 수위의 75% 위치까지 거의 일정**하게 유지(쇄파·충격이 up-rushing water 를 가속하기 때문).
- 실제 최대 front velocity 는 **최대 처오름 수위의 30–40%** 위치에서 도달.
- Eq.(2) 의 제곱근 형태는 "특정 위치의 최대유속"에는 맞으나 **front velocity 와는 다름**.

최대 front velocity 대 최대 처오름의 관계 추세(Fig. 5) ((coastal-structures-design, p.23 §2.3 Eq.(4))):

$$
\frac{u_{\max}}{\sqrt{g H_s}} = c_u \,\frac{R_{u,\max}}{H_s}
$$

$c_u$ 는 확률변수(평균 $\mu(c_u)=1.0$, 정규분포, 변동계수 CoV $=0.25$) ((coastal-structures-design, p.23 §2.3)).

> 이 분포(15%-시작·30-40%-최대·75%-까지 일정)는 §4 uprush 가속/감속 비대칭의 사면-구조물 측 정량 근거.

### 3.4 Hunt(1959)·Stockdon(2006) (문헌 cross-ref)

자연 해빈의 runup 매개변수화 표준 — 본 위키 md 교과서에 본문 부재로 **문헌 인용만**(임의 page/식 금지):

- **Hunt (1959)** — runup 이 Iribarren 수에 선형 비례하는 고전 scaling $R/H \sim \zeta$ (반사성 영역). §2 surf similarity 와 §3.3 의 $R_{u,\max}/H_s$ 추세선이 같은 계열.
- **Stockdon et al. (2006)** — 광범위 현장자료 기반 $R_{2\%}$ 매개변수화: setup + swash(incident + IG) 합성, $\zeta$ 와 $(H_0 L_0)^{1/2}$·$\tan\beta$ 로 표현. dissipative 극한에서 IG swash 가 지배(§2.2·[[01-concept]] §4.1 와 정합).

> 위 두 식의 계수는 본 노트에서 단언하지 않음(교과서 본문 미보유). 필요 시 원논문 full-read 후 별도 verified 승격.

---

## 4. swash 시간규모·uprush/backwash 비대칭

[[01-concept]] §2 의 정성 비대칭을 시간규모로 정리:

- **시간규모**: incident swash(~수 초–10초, 입사파 주기) + **infragravity swash(수십 초–수 분)** 중첩. 반사성 해빈은 incident, 소산성 해빈은 IG 가 swash 진폭·주기를 지배(§2.2).
- **uprush(처오름)**: bore collapse 직후 얇은 sheet flow 가 사면을 오름. front velocity 가 초기(처오름 한계의 15%)부터 거의 최대에 근접하고 한계의 75%까지 일정(§3.3) → uprush 는 쇄파 충격으로 **가속 출발 후 거의 일정 속도** 단계를 가짐.
- **backwash(되돌이)**: 중력에 의한 가속 하강. uprush 와 달리 사면 마찰·삼투(percolation)·중력의 순효과로 시간구조가 비대칭.
- **공학적 함의**: front velocity 가 잔디·armour 손상의 지배 인자(§3.2). swash 표사 비대칭(uprush 퇴적 / backwash 침식)은 해빈 경사·berm 형성을 좌우([[01-concept]] §2).

---

## 5. 연결

- [[01-concept]] — §4.1 bore-bore capture(Stringari-Power 2019)·§4.2 경사입사 NLSW 해(Antuono/Ryrie)·§4.3 debris beaching
- [[04-code-and-tools]] — NLSW·Boussinesq/Green-Naghdi·SWASH·XBeach 의 swash-handling(wetting-drying·breaking·runup)
- [`concepts/waves/04-code-and-tools.md`](../waves/04-code-and-tools.md) — 위상해상 모델
- [`concepts/littoral-drift/`](../littoral-drift/) — alongshore transport(§1.2 weakly-2D 해 직결)
- `models/SWASH/` — 비정수압 위상해상 모델(runup source-analysis [[swash-wetting-drying-runup]])
