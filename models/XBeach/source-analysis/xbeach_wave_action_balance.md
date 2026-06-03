---
title: "XBeach wave action balance (wave_instationary.F90 + wave_directions.F90) — surfbeat 파작용 N=E/σ x·y·θ 전파 + Roelvink/Baldock 쇄파 dissipation + roller energy balance → radiation stress Fx/Fy"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_instationary.F90 (479) + wave_directions.F90 (400) 직접 read — action N=ee/sigt advecxho/yho/thetaho(199-208), gammax limiter(241), dissipation roelvink/baldock/janssen_battjes(254-257), roller rr 평형(drr=2g·BR·rr/c, 250-330+) file:line 인용. 쇄파 모듈 roelvink_module."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — action balance·쇄파·roller·radiation stress verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
  - models/XBeach/source-analysis/wave/xbeach_wave_boundary.md
  - models/XBeach/source-analysis/xbeach_single_dir.md
---

# XBeach wave action balance (surfbeat wave driver)

> `wave_instationary.F90`(479) + `wave_directions.F90`(400) 직접 read. XBeach **surfbeat(instationary) 모드의 핵심 파동 solver** — short-wave 에너지의 파작용(action) 평형방정식을 풀어 쇄파 dissipation·roller 를 거쳐 **radiation stress `Fx/Fy`** 산출 → [[xbeach_flow_solver]] 흐름 구동. boundary spectrum→bound wave 는 [[xbeach_wave_boundary]], 본 노트는 **내부 파작용 전파·쇄파·roller**.

## 1. Wave action balance (wave_instationary.F90:193-218) ★

방향분해(ntheta bins) short-wave 에너지 `ee(x,y,θ)` 를 **파작용 N = E/σ** 로 변환해 전파:
```fortran
s%ee(:,:,itheta) = s%ee/s%sigt                    ! E → N = E/σ (action)
call advecxho(s%ee, s%cgx, xadvec, ...)            ! ∂(cgx·N)/∂x  (x 전파, group velocity)
call advecyho(s%ee, s%cgy, yadvec, ...)            ! ∂(cgy·N)/∂y  (y 전파)
if(refraction==1) advecthetaho(s%ee, s%ctheta, ...)! ∂(cθ·N)/∂θ   (방향 refraction)
s%ee = s%ee - dt*(xadvec + yadvec + thetaadvec)    ! Euler step
s%ee = max(s%ee*s%sigt, 0.d0)                      ! N → E
```
- **파작용 방정식**: `∂N/∂t + ∂(c_gx N)/∂x + ∂(c_gy N)/∂y + ∂(c_θ N)/∂θ = −D/σ`. N=E/σ 가 (흐름 존재 시) 보존량(wci wave-current interaction).
- `cgx/cgy` = group velocity 성분, `ctheta` = 방향 refraction 속도(수심·흐름 경사, `compute_wave_direction_velocities`). `advecxho/yho/thetaho` = higher-order(par%scheme) upwind advection.
- **gammax limiter**(:241): `H ≤ gammax·h` 초과 시 `ee /= (H/(gammax·h))²` (얕은 물 파고 상한, 수치 안정).

## 2. 쇄파 dissipation D (wave_instationary.F90:251-257)

```fortran
select case(par%break)
  case(BREAK_ROELVINK1,BREAK_ROELVINK2): call roelvink(par,s)   ! Roelvink 1993 (Qb 기반)
  case(BREAK_BALDOCK):                   call baldock(par,s)    ! Baldock 1998
  case(...):                             janssen_battjes        ! Janssen-Battjes
end select
```
- **Roelvink**: `Qb`(쇄파 비율) 기반 dissipation `D`, breaker delay 위해 `Qb` advect(`advecqx/qy`, cgxm=c·cos(θmean−α)). **Baldock**: 확률적 쇄파(deep-applicable). `gamma`(파고/수심 쇄파 지표)·`alpha`·`n` 파라미터.
- 추가 dissipation: **bed friction `Df`** + **vegetation `Dveg`**([[xbeach_vegetation]]).
- 방향 분배: `dder = ee·D/E`(roller 로 가는 분), `dd = dder + ee·(Df+Dveg)/E`(전체). `ee -= dt·dd`.

## 3. Roller energy balance (wave_instationary.F90:300-340) ★

쇄파 후 surface roller 에너지 `rr(x,y,θ)`:
```fortran
call advecxho(s%rr, s%cx, ...); advecyho(s%rr, s%cy, ...); advecthetaho(s%rr, s%ctheta, ...)  ! roller 전파 (위상속도 c)
drr = 2*par%g*s%BR*max(rr,0)/sqrt(cx²+cy²)         ! roller dissipation (slope BR)
s%rr = s%rr + dt*(dder − drr)                       ! source=쇄파 dder, sink=drr
```
- roller 는 **위상속도 c**(group 아님)로 전파. `BR` = roller slope(β, ~0.1) → dissipation `2g·β·E_r/c`. roller 가 쇄파 운동량을 surfzone 안쪽으로 지연 전달(wave setup·undertow 정확도 향상, Svendsen 1984).
- `par%roller==1` 시 활성.

## 4. Radiation stress → Fx/Fy

`ee + rr`(파+roller 에너지)로 radiation stress tensor `Sxx/Sxy/Syy` → **wave force `Fx/Fy`**(공간경사) → [[xbeach_flow_solver]] §1 의 `lwave·Fx/(ρ·hum)` 운동량 항. surfbeat 의 wave→current 구동(longshore current·setup·undertow).

## 5. Stationary 모드 (wave_directions.F90, 400)

`wave_directions` = **stationary 모드**의 방향 분해 solver(ntheta_s bins). 반복(`iter`/`itermax`, Herr/thetaerr 수렴)으로 정상상태 파작용·방향(thetamean) 해. instationary 와 달리 시간전진 없이 정상 평형. [[xbeach_single_dir]](single-directional)·[[xbeach_mode_dispatch]] 와 연계.

## 6. 모드별 wave solver

| 모드 | solver | 특징 |
|---|---|---|
| **surfbeat(instat)** | `wave_instationary` | 시간전진 파작용+roller, wave-group 변조→bound long wave(infragravity) |
| **stationary** | `wave_directions` | 반복 정상상태, 평균 wave forcing |
| **nonh** | (파 직접 해상) | action balance 미사용([[xbeach_flow_solver]] §6) |

## 7. 연결

- [[xbeach_flow_solver]] — Fx/Fy radiation stress → 흐름 운동량(wave→current)
- [[xbeach_mode_dispatch]] — surfbeat/stationary/nonh 모드 분기
- [[xbeach_wave_boundary]] — boundary spectrum→bound wave(본 solver 의 offshore 입력)
- [[xbeach_vegetation]] — Dveg 식생 wave dissipation
- Roelvink 1993 / Baldock 1998 (쇄파) / Svendsen 1984 (roller) / Holthuijsen action balance
