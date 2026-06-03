---
title: "XBeach 쇄파 dissipation(roelvink.F90) — Roelvink1993(Qb=1−exp(−(H/γh)^n)) / Roelvink2 / Roelvink-Daly / Baldock1998 / Janssen-Battjes + Ruessink1998 spatial γ"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/roelvink.F90 (320) 직접 read — roelvink/baldock/janssen_battjes(1D/2D) public, Qb=1−exp(−(H/(γ·tanh(kh)/k))^n)(79-84/145-150), D=Qb·2·α·E·(σ/2π or 1/Trep)(97-110), Daly γ/γ2 threshold(88-92), Baldock Hb=tanh(γkh/0.88)(227), Ruessink1998 γ=0.76kh+0.29(221) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 쇄파 Qb·D 식 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
  - models/XBeach/source-analysis/xbeach_flow_solver.md
---

# XBeach 쇄파 dissipation (roelvink.F90)

> `roelvink.F90`(320) 직접 read. [[xbeach_wave_action_balance]] 의 파작용 평형에 들어가는 **wave breaking dissipation `D`** 의 정식. surfzone 파고 감쇠의 핵심. `par%break` 으로 선택. module `roelvink_module` (public: `roelvink`/`baldock`/`janssen_battjes`, 각 1D/2D).

## 1. Roelvink 1993 (BREAK_ROELVINK1/2) ★

**breaking 확률(fraction) Qb**:
```fortran
arg = -( H / (par%gamma*tanh(k·h)/k) )**par%n      ! wci: 수심 대신 γ·tanh(kh)/k
arg = -( H / (par%gamma*h) )**par%n                ! 일반: γ·h
Qb  = min(1 - exp(max(arg,-100)), 1)               ! 쇄파 비율 [0,1]
D   = Qb · 2·par%alpha · E · (σ/2π  or  1/Trep)     ! dissipation
```
- `gamma`(γ) = breaker index(~0.55), `n` = 지수(~10, 클수록 sharp 한 임계), `alpha`(α) = dissipation 계수(~1).
- **ROELVINK1**: `D = Qb·2α·E/Trep`. **ROELVINK2**: `D = ...·H/h`(수심 정규화, shallow 강화).
- `wci=1`(wave-current interaction): `1/Trep` 대신 `σ/2π`(국소 주파수).

## 2. Roelvink-Daly (BREAK_ROELVINK_DALY)

Qb 를 **임계 on/off + advection**: `H > γ·h → Qb=1`(쇄파 시작), `H < γ2·h → Qb=0`(쇄파 종료), 사이는 advected Qb 유지(breaker delay). 쇄파 영역의 hysteresis(시작/종료 다른 임계, Daly et al. 2012).

## 3. Baldock 1998 (BREAK_BALDOCK)

확률적 쇄파(deep-applicable): `Hb = tanh(γ·kh/0.88)·(0.88/k)`(쇄파 한계 파고), `R = Hb/H`, Qb·D 가 R 의 함수. 비-shallow(rip channel·deep) 에도 적용. **Ruessink et al. 1998 spatial γ**: `γ = 0.76·kh + 0.29`(수심·파수 의존, 상수 γ 대안).

## 4. Janssen-Battjes

Battjes-Janssen 1978 형식의 변형(janssen_battjes_1D/2D). bore-based dissipation.

## 5. 결합

- `D` → [[xbeach_wave_action_balance]] §2 의 파작용 sink + roller source(dder). 파고 감쇠 + roller 운동량 → wave force → [[xbeach_flow_solver]].
- `Qb` 는 [[xbeach_flow_solver]] 의 breaking-induced eddy viscosity(`s%breaking`) trigger 이기도.

## 6. 연결

- [[xbeach_wave_action_balance]] — D 가 들어가는 파작용 평형(+roller)
- [[xbeach_flow_solver]] — Qb breaking → eddy viscosity
- Roelvink 1993 / Daly et al. 2012 / Baldock et al. 1998 / Battjes-Janssen 1978 / Ruessink et al. 1998(spatial γ)
