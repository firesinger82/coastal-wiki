---
title: "XBeach wave action balance (wave_instationary.F90 + wave_stationary_directions.F90) — surfbeat 파작용 N=E/σ x·y·θ 전파 + Roelvink/Baldock 쇄파 dissipation + roller energy balance → radiation stress Fx/Fy"
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
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "stationary와 surfbeat single_dir의 활성 공유 루틴·callType·방향 격자를 정정"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: stationary와 surfbeat single_dir의 활성 공유 루틴·callType·방향 격자를 정정. 위 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인을 뜻하지 않는다. [원문 구간·SHA와 재사용 근거](../../../_staging/total-read/model-audit/XBeach/connectivity/corrections-20260912/evidence.json)에 결속했다.

# XBeach wave action balance (surfbeat wave driver)

> 활성 surfbeat 에너지 전파는 `wave_instationary.F90`, 조건부 정상 방향 계산은 `wave_stationary_directions.F90`에 연결된다 (`wave_timestep.F90:75-114`). XBeach **surfbeat(instationary) 모드의 핵심 파동 solver** — short-wave 에너지의 파작용(action) 평형방정식을 풀어 쇄파 dissipation·roller 를 거쳐 **radiation stress `Fx/Fy`** 산출 → [[xbeach_flow_solver]] 흐름 구동. boundary spectrum→bound wave 는 [[xbeach_wave_boundary]], 본 노트는 **내부 파작용 전파·쇄파·roller**.

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

## 5. 활성 정상 계산과 구형 파일

현재 `wave_timestep`은 stationary에서 `wave_stationary_directions(s,par,0)`을 호출한다. 이때 `callType=0`은 `s%ntheta`를 사용한다. surfbeat의 `single_dir` 경로도 같은 루틴을 `callType=1`로 호출하지만, 이때는 `s%ntheta_s`로 평균 방향을 계산한다. 호출은 `wavint` 간격 조건과 새 stationary 경계 조건으로 제어하며, surfbeat single_dir에는 `t==dt` 조건도 있다. (`wave_timestep.F90:75-114`; `wave_stationary_directions.F90:33-49, 71-76`)

`wave_directions.F90`와 `wave_stationary.F90`는 현재 조사한 빌드 목록에 포함되지 않는다. 두 파일을 읽은 이전 검증 이력은 보존하되 현재 solver로 귀속하지 않는다. ([[xbeach-build-mode-connectivity]]; 상세는 [[xbeach_wave_stationary]])

## 6. 모드별 활성 wave 호출

| 모드 | 호출 | 조건 |
|---|---|---|
| stationary | `wave_dispersion(...,0)` → `wave_stationary_directions(...,0)` | `wavint` 또는 새 경계 조건에 따른 정상 계산 |
| surfbeat, `single_dir==1` | 평균장 갱신 → 조건부 `wave_dispersion(...,1)`과 `wave_stationary_directions(...,1)` | 정상 방향 계산 (`wavint` 조건, 새 경계 조건 또는 `t==dt`); 이후 에너지 전파는 별도 실행 |
| surfbeat | `wave_dispersion(...,0 또는 2)` → `wave_instationary` | 매 파랑 스텝의 에너지 전파; WCI 조건에 따라 분산 계산 인수 선택 |

위 표는 `wave_timestep.F90:75-114`의 stationary/surfbeat 분기다. nonh의 수력 계산은 [[xbeach_mode_dispatch]]와 [[xbeach_nonh]]를 따른다.

## 7. 연결

- [[xbeach_flow_solver]] — Fx/Fy radiation stress → 흐름 운동량(wave→current)
- [[xbeach_mode_dispatch]] — surfbeat/stationary/nonh 모드 분기
- [[xbeach_wave_boundary]] — boundary spectrum→bound wave(본 solver 의 offshore 입력)
- [[xbeach_vegetation]] — Dveg 식생 wave dissipation
- Roelvink 1993 / Baldock 1998 (쇄파) / Svendsen 1984 (roller) / Holthuijsen action balance
