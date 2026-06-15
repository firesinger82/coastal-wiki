---
title: "처오름대 (Swash Zone) — 정의·process·runup·sediment + 전이 연구"
topic: swash-zone
canonical_source: self
citation_status: source-needed
verification_method: "신규 토픽 (2026-06-15) — research/inbox promote 3건(arxiv:1909.11279 bore-bore capture / 2504.18467 oblique bore swash / 2305.03811 beaching debris) abstract 직접 인용 + swash zone 정의·process 는 publicly-known coastal engineering canonical (Holthuijsen 2007 Ch 11·Dean & Dalrymple·Masselink-Puleo 2006 review 일반지식). 정량 claim·교과서 페이지 인용은 full read 후 verified 승격 TODO."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
related:
  - concepts/swash-zone/04-code-and-tools.md
  - concepts/waves/04-code-and-tools.md
  - concepts/littoral-drift/01-concept.md
  - concepts/sediment-transport/01-concept.md
---

# 처오름대 (Swash Zone)

> ⚠ citation_status: **source-needed**. 정의·process 골격은 publicly-known canonical, 정량·세부는 abstract/추후 교과서 인용 대기.

## 1. 정의

**Swash zone** = 쇄파된 파(bore)가 해빈 사면을 **밀려 올라갔다(uprush) 중력으로 되돌아 내려오는(backwash)** 운동으로 인해 **주기적으로 물에 잠겼다 노출되는 천이대**. surf zone 의 landward 경계 ~ 최대 runup 한계 사이. shoreline 이 시간에 따라 이동(time-varying wet/dry boundary)하는 영역.

- 상류 경계: surf zone(쇄파대) — bore 가 swash 로 collapse
- 하류 경계: 최대 처오름선(runup limit) ~ dry beach
- 시간 규모: incident wave(~수 초~10초) + **infragravity(IG, 수십 초~수 분)** 중첩

## 2. 주요 process

| process | 내용 |
|---|---|
| **Uprush / backwash** | bore collapse → 얇은 sheet flow 상류 이동(uprush, 감속) → 중력 backwash(가속). 비대칭 시간구조 |
| **Bore collapse** | surf zone bore 가 shoreline 에서 무너지며 swash lens 형성 (NLSW dam-break 유사) |
| **Swash-swash interaction** | 선행 backwash 와 후속 uprush 충돌 / 빠른 bore 가 느린 bore 포획(**bore-bore capture**, §4.1) |
| **Infragravity 변조** | 반사 IG wave 가 swash 진폭·주기 변조 — 반사성(steep) 해빈서 우세 |
| **Sediment transport** | uprush(상류 퇴적 경향) vs backwash(하류 침식) 비대칭 → 해빈 경사·berm 형성, swash-zone 표사 |
| **Runup** | 처오름 수직 한계. 설계·범람(R2% = 2% 초과확률 runup)에 핵심 — [`concepts/waves`](../waves/04-code-and-tools.md) + storm-surge 범람 wave setup |

## 3. 지배 파라미터

- **Iribarren 수** $\xi = \tan\beta / \sqrt{H/L_0}$ (surf similarity) — swash 체계(반사/소산성)·bore-bore capture 확률 지배(§4.1)
- 해빈 경사 $\tan\beta$, 입사파 $H$·주기, 입자 관성(표사·debris)

## 4. 전이된 연구 (research/inbox promote, source-needed)

### 4.1 Bore-bore capture (Stringari·Power 2019)

arxiv:[1909.11279](https://arxiv.org/abs/1909.11279). 빠른 bore 가 surf/swash 에서 느린 bore 를 **포획**하는 현상을 최초 정량화 — 호주 7개 micro-tidal 사빈 wave tracking. 발생가능 조건서 **포획확률 ~40%**, 최가능 위치 = nearshore 의 landward 10%(time-varying surf-swash extent). amplitude/frequency dispersion + bore-IG 상호작용이 구동. **극단 shoreline 최대치의 >97% 가 bore-bore capture 가 직접 구동** — 반사성(steep, 높은 Iribarren)일수록 확률↑. 기존 runup 예측모델 미반영 현상.

### 4.2 경사 입사 bore 의 swash flow (Sung et al. 2025)

arxiv:[2504.18467](https://arxiv.org/abs/2504.18467). 비선형 천수방정식(NLSW)의 **새 해** — 작은 접근각 $\theta$ 에서 Snell 굴절 적용("small-$\theta$, constant-$\alpha$" 해). Ryrie(1983) weakly 2D NLSW(cross-shore 가 alongshore 를 forcing) + Antuono(2010) cross-shore 해 + 특성곡선법. 대형 wave basin 15 케이스(법선·경사입사) 검증 — 시간평균 alongshore 유속 예측 정확 → **alongshore transport 예측 개선**.

### 4.3 Bore-driven swash 의 부유 debris beaching (Davidson·Brenner·Pujara 2023)

arxiv:[2305.03811](https://arxiv.org/abs/2305.03811). 부유 해양 debris 의 swash beaching 단순모델 + 실험 검증. 해빈 = debris sink(marine debris mass balance 에 beaching 필수). 지배 파라미터 = **입자 관성 + swash 진입 시점·유속**. 표사뿐 아니라 부유물 transport 로 swash 확장.

## 5. 연결

- [`04-code-and-tools.md`](04-code-and-tools.md) — swash 수치모델(NLSW·Boussinesq·SWASH·XBeach·VOF)
- [`concepts/waves/04-code-and-tools.md`](../waves/04-code-and-tools.md) — 위상해상 모델 + §5.1 위상평균/위상해상 리뷰
- [`concepts/littoral-drift/`](../littoral-drift/) — alongshore transport(§4.2 직결)
- [`concepts/sediment-transport/`](../sediment-transport/) — bed-load/suspended(§4.3 + §10.1 Green-Naghdi DG swash)
- [`concepts/storm-surge/`](../storm-surge/) — 범람 시 runup·wave setup
