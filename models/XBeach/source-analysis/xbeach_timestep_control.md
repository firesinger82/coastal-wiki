---
title: "XBeach time step 제어(timestep.F90) — CFL adaptive dt = CFL·min(dsu,dnv)/√(g·max(hh)) + output time snapping + timestep_init/compute_dt"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/timestep.F90 (764) 직접 read — compute_dt(416) CFL dt=CFL·min(dsu,dnv)/sqrt(g·max(hh)) + tnext snapping(n=ceiling) + timestep_init(123)/outputtimes_update(346) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — CFL adaptive dt verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
---

# XBeach time step 제어 (timestep.F90)

> `timestep.F90`(764) 직접 read. **adaptive time step(dt) 산출** — Courant(CFL) 조건으로 매 step dt 조정. [[xbeach_flow_solver]]/[[xbeach_wave_action_balance]] 의 explicit Euler 안정 보장.

## 1. CFL adaptive dt (compute_dt, :416) ★

```fortran
par%dt = par%CFL * min(min(dsu), min(dnv)) / sqrt(max(hh)·par%g)
```
- **shallow-water CFL**: `dt ≤ CFL·Δx/√(gh)` — 격자간격(dsu/dnv) / 최대 파속 √(g·h_max). `par%CFL`(~0.7) 안전계수.
- 가장 얕지 않고 **가장 깊은(빠른) 점**이 dt 제한(전 domain 최소 dt). ISDYNSTP(dynamic) 시 매 step 재계산.

## 2. Output time snapping (:430)

다음 출력시각 `tnext` 를 넘지 않게 dt 조정: `n = ceiling((tnext−t)/dt); dt = (tnext−t)/n` — 출력 시점에 정확히 도달(균등 분할). `outputtimes_update`(:346)가 출력 시각 관리.

## 3. timestep_init (:123)

simulation 시작 시 시간격자 초기화(tpar): 출력 간격(tintg/tintm/tintp), 시작/종료(tstop), morphology 시작(morstart). `dtref`(참조 dt)·`maxdtfac`(dt 변화 제한).

## 4. 모드별

- explicit 모드(surfbeat/nonh) 모두 CFL 제한. nonh 는 파 해상 위해 작은 dt(파속+동압력). morphology 는 `morfac`([[xbeach_morphology]])로 형상시간 가속(dt_morph = morfac·dt).

## 5. 연결

- [[xbeach_flow_solver]] — DDELT/dt explicit Euler 안정(CFL)
- [[xbeach_mode_dispatch]] — 모드별 timestep 차이
- [[xbeach_morphology]] — morfac 형상시간 가속
