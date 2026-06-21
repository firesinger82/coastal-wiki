---
title: "처오름대 (Swash Zone) — 정의·process·runup·sediment + 전이 연구"
topic: swash-zone
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "**§4 전이연구 3건 = full PDF 직접 read (2026-06-18, pdftotext) 후 verified** — 1909.11279(Stringari-Power 2019, Univ Newcastle, 7 호주 사빈, highlights/abstract+본문 line 75/177 확인: 40%·landward 10%·IG 50%·extreme 20%/>97%·Iribarren 상관)·2504.18467(Wisconsin-Madison+Delaware, Snell+Ryrie1983 JFM129:193+Antuono2010 JFM658:166, O.H.Hinsdale Directional Wave Basin W1-12 정규/W13-15 불규칙)·2305.03811(Davidson-Brenner-Pujara, Wisconsin-Madison, 입자관성+진입 timing). **실제 읽은 highlights/abstract/명시 실험설정만 인용 — 페이지·식 번호 임의 인용 금지**.\n**§1-3 textbook page 보강 (2026-06-18, grep+Read 로 page 본문 직접 확인 후 인용)**: §1 swash zone=foreshore 정의(alternately wet/dry)·surf/breaker zone 경계 = [coastal-eng-intro-wijetunge] PAGE-12 + [coastal-processes-with-eng-apps] PAGE-7. §2 uprush/backwash·run-up/run-down zone(다음 처오르는 파 만남=swash-swash) = [coastal-structures-design] PAGE-16. §2 sediment uprush/backwash 비대칭(upper foreshore 공극 침투→backwash 운반능↓→퇴적) = [coastal-processes-with-eng-apps] PAGE-18. §2/§3 Ru2% 설계 정의·Rayleigh 분포 = [coastal-structures-design] PAGE-20~21, run-up front velocity 15%/30-40% = PAGE-22. §3 ξ breaker/surf-similarity 명칭·기호 = [coastal-eng-intro-wijetunge] PAGE-27 nomenclature.\n**잔존 source-needed** (보유 page 미수록): IG band 주기 수치, bore collapse 의 NLSW dam-break 형식해, Iribarren $\\xi$ 수식 형태·임계값, IG 변조의 반사성 의존 정량 — Holthuijsen 2007 Ch 11·Masselink-Puleo 2006 review 필요. coastal-processes-with-eng-apps 추출 md 는 PDF p.1-35(Ch 1-3)만 보유 → §5.6 Swash Zone Dynamics(book p.114) 본문 인용 불가."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - concepts/swash-zone/04-code-and-tools.md
  - concepts/waves/04-code-and-tools.md
  - concepts/littoral-drift/01-concept.md
  - concepts/sediment-transport/01-concept.md
---

# 처오름대 (Swash Zone)

> ⚠ citation_status: **partially-verified**. §1 정의·§2 uprush/backwash·runup·§3 Ru2% = 교과서 page 인용 verified. IG band 수치·bore collapse NLSW·Iribarren 수식·IG 변조 정량은 source-needed(Holthuijsen/Masselink 미보유 page).

## 1. 정의

**Swash zone** = 쇄파된 파(bore)가 해빈 사면을 **밀려 올라갔다(uprush) 중력으로 되돌아 내려오는(backwash)** 운동으로 인해 **주기적으로 물에 잠겼다 노출되는 천이대**. 교과서 용어로는 **전빈(foreshore)** 과 동일 — "해빈 중 파가 오르내릴 때 번갈아 젖었다 마르는(alternately wet or dry as the waves rush up and down) 부분으로, 저조 정선에서 고조 시 wave uprush 한계(= shoreline)까지 뻗는다"([coastal-eng-intro-wijetunge] PAGE-12). 동일한 정의가 Dean & Dalrymple 도 "전빈, 즉 swash zone 은 파가 단면의 가파른 부분을 쓸어올릴 때 번갈아 젖었다 마르는 영역"([coastal-processes-with-eng-apps] PAGE-7). shoreline 이 시간에 따라 이동(time-varying wet/dry boundary)하는 영역.

- 상류 경계: surf zone(쇄파대) — bore 가 swash 로 collapse. surf/breaker zone = "shoreline 에서 쇄파 시작 외측 경계까지의 천해 띠"([coastal-eng-intro-wijetunge] PAGE-12)
- 하류 경계: 최대 처오름선(runup limit) ~ dry beach
- 시간 규모: incident wave(~수 초~10초) + **infragravity(IG, 수십 초~수 분)** 중첩 (IG band 정량 수치 source-needed)

## 2. 주요 process

| process | 내용 |
|---|---|
| **Uprush / backwash** | bore collapse → 얇은 sheet flow 상류 이동(uprush, 감속) → 중력 backwash(가속). 비대칭 시간구조. 사면 상의 동등 표현: "파가 사면을 올라간 뒤(run up) 다시 흘러내려(rush down) **다음 처오르는 파를 만날 때까지** 내려오는 run-up/run-down zone"([coastal-structures-design] PAGE-16) |
| **Bore collapse** | surf zone bore 가 shoreline 에서 무너지며 swash lens 형성 (NLSW dam-break 유사) — *NLSW dam-break 형식해는 source-needed* |
| **Swash-swash interaction** | 선행 backwash 와 후속 uprush 충돌 / 빠른 bore 가 느린 bore 포획(**bore-bore capture**, §4.1). 사면 상 직접 관찰: 흘러내리는 물이 "다음 처오르는 파를 만난다"([coastal-structures-design] PAGE-16) |
| **Infragravity 변조** | 반사 IG wave 가 swash 진폭·주기 변조 — 반사성(steep) 해빈서 우세 *(정량·반사성 의존 = source-needed)* |
| **Sediment transport** | uprush(상류 퇴적 경향) vs backwash(하류 침식) 비대칭 → 해빈 경사·berm 형성, swash-zone 표사. 기구: "상부 전빈(upper foreshore)·wave uprush 한계는 공극률이 높아 uprush 물이 모래로 스며들어 사면을 통해 backwash 로 빠져나간다 → backwash 의 부피 손실로 모래를 외해로 운반하는 능력이 떨어져 해빈면(beach face) 퇴적 기구가 된다"([coastal-processes-with-eng-apps] PAGE-18) |
| **Runup** | 처오름 수직 한계. 설계·범람(Ru2%)에 핵심. **Ru2% = 사면에서 처오르는 파의 2%가 초과하는 처오름 수위**(wave run-up 의 공학 설계 파라미터)([coastal-structures-design] PAGE-20). run-up front velocity 는 max run-up level 의 약 15% 지점에서 시작해 30–40% 지점에서 최대([coastal-structures-design] PAGE-22). [`concepts/waves`](../waves/04-code-and-tools.md) + storm-surge 범람 wave setup |

## 3. 지배 파라미터

- **Iribarren 수(surf similarity / breaker parameter $\xi$)** $\xi = \tan\beta / \sqrt{H/L_0}$ — swash 체계(반사/소산성)·bore-bore capture 확률 지배(§4.1). Wijetunge 도 $\xi$ 를 "breaker parameter (surf similarity parameter)"로 명명·기호 사용([coastal-eng-intro-wijetunge] PAGE-27 nomenclature). *수식 형태·임계값 자체는 보유 page 에 미수록 → source-needed*
- **Ru2%** — 처오름 수위 설계 파라미터(사면서 2% 초과). Rayleigh 분포 가정 시 Ru2% 로 전체 처오름 수위 분포 산출([coastal-structures-design] PAGE-20~21)
- 해빈 경사 $\tan\beta$, 입사파 $H$·주기, 입자 관성(표사·debris)

## 4. 전이된 연구 (full PDF 직접 read 2026-06-18, verified)

> 3편 모두 arxiv full PDF 직접 추출(pdftotext)·확인. 인용 수준 = highlights/abstract + 명시 방법·실험설정·embedded 참조(실제 읽은 범위만).

### 4.1 Bore-bore capture (Stringari & Power 2019)

arxiv:[1909.11279](https://arxiv.org/abs/1909.11279) (C. E. Stringari, H. E. Power, **University of Newcastle**, Australia, 32p). 빠른 bore 가 surf/swash 에서 느린 bore 를 **포획(capture)**하는 현상을 정량화 — **호주 7개 sandy·micro-tidal·wave-dominated 사빈** 비디오 데이터(p.1 highlights·abstract, p.본문 line 75/177):
- 포획 가능 조건의 사빈에서 **포획확률 ≈40%** — 최가능 위치 = nearshore 의 **landward 10%**(time-varying surf-swash extent).
- 포획은 **IG(infragravity) 에너지 우세 조건에서만 일어나는 것이 아님** (IG 우세 시 ≈50%) — amplitude/frequency dispersion 도 기여.
- 포획이 **극단 shoreline 최대치를 유발하는 경우는 포획 사례의 ≈20%**에 불과하나, **극단 최대치의 >97%는 bore-bore capture 가 직접 구동**.
- 극단 최대치 구동 확률은 **Iribarren 수·beach morphodynamic state 와 직접 상관 — steeper/more reflective 일수록 ↑**. 기존 runup 예측모델 미반영 현상.

### 4.2 경사 입사 bore 의 swash flow (Wisconsin-Madison·Delaware 그룹 2025)

arxiv:[2504.18467](https://arxiv.org/abs/2504.18467) (Univ Wisconsin-Madison + Univ Delaware CACR, 31p). 비선형 천수방정식(NLSW)의 **새 해** — 작은 접근각 $\theta$ 에서 **Snell 굴절 적용**("small-$\theta$, constant-$\alpha$" 해, abstract p.1):
- **Ryrie (1983, JFM 129:193)** weakly-2D NLSW(cross-shore 가 alongshore 를 forcing) + **Antuono (2010, JFM 658:166)** cross-shore 해 + **특성곡선법**(forward-moving characteristic variable $\alpha$).
- 검증: **O.H. Hinsdale Directional Wave Basin** 대형실험 — 정규파 12케이스(W1-12, 법선·경사입사 wall-reflection 법) + 불규칙파 3케이스(W13-15, 각 10반복), in-situ 센서 수심·유속.
- Snell 굴절 + constant-$\alpha$ 가정이 잘 성립, 시간평균 alongshore 유속 예측 정확 → **alongshore (longshore) transport 예측 개선** 함의.

### 4.3 Bore-driven swash 의 부유 debris beaching (Davidson, Brenner & Pujara 2023)

arxiv:[2305.03811](https://arxiv.org/abs/2305.03811) (B. Davidson, J. Brenner, N. Pujara, **Univ Wisconsin-Madison**, 22p). 부유 해양 debris 의 swash beaching 단순모델 + 실험 검증 (abstract p.1):
- 해빈 = debris sink — marine debris mass balance 에 beaching 필수.
- 지배 파라미터 = **입자 관성(inertia) + swash zone 진입 시점·유속**.
- 표사뿐 아니라 부유물(buoyant) transport 로 swash 동역학 확장.

## 5. 연결

- [`04-code-and-tools.md`](04-code-and-tools.md) — swash 수치모델(NLSW·Boussinesq·SWASH·XBeach·VOF)
- [`concepts/waves/04-code-and-tools.md`](../waves/04-code-and-tools.md) — 위상해상 모델 + §5.1 위상평균/위상해상 리뷰
- [`concepts/littoral-drift/`](../littoral-drift/) — alongshore transport(§4.2 직결)
- [`concepts/sediment-transport/`](../sediment-transport/) — bed-load/suspended(§4.3 + §10.1 Green-Naghdi DG swash)
- [`concepts/storm-surge/`](../storm-surge/) — 범람 시 runup·wave setup
