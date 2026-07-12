---
title: "XBeach NLSWE flow solver (flow_timestep.F90 + flow_secondorder.F90) — 깊이평균 운동량 explicit Euler(advection+g∂(zs+ph)+Ruessink2001 bed friction+wave force Fx+Coriolis+veg) + MacCormack 2nd-order + continuity"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/flow_timestep.F90 (1102) + flow_secondorder.F90 (1063) 직접 read — subroutine flow: advection(181-341) + viscosity Smagorinsky/breaking(365-530) + bed friction Ruessink2001(535-556) + explicit Euler momentum(559-593, g·dzsdx+taubx+Fvegu−lwave·Fx−fc·vu) + continuity. flow_secondorder MacCormack advUV/advW/con file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — NLSWE 운동량·friction·2nd-order·continuity verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
  - models/XBeach/source-analysis/xbeach_bed_friction.md
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/XBeach/source-analysis/xbeach_vegetation.md
---

# XBeach NLSWE flow solver (flow_timestep / flow_secondorder)

> `flow_timestep.F90`(1102, subroutine `flow`) + `flow_secondorder.F90`(1063) 직접 read. XBeach 의 **깊이평균 비선형 천수방정식(NLSWE) 흐름 solver** — surfbeat(wave-averaged GLM 흐름 + wave force) · nonh(wave-resolving + non-hydrostatic 압력) 모드가 공유([[xbeach_mode_dispatch]]). bed friction 계수 자체는 [[xbeach_bed_friction]], 본 노트는 **운동량·연속 방정식 solver**.

## 1. Explicit Euler 운동량 (flow_timestep.F90:559-593) ★

u-방향 가속도(GLM/Eulerian velocity uu):
```fortran
dudt = -advection_u
       - par%g*s%dzsdx(i,j)                         ! 압력경사 g·∂(zs+ph)/∂x
       - s%taubx(i,j)/(par%rho*s%hu(i,j))           ! bed friction
       - s%Fvegu(i,j)/(par%rho*s%hu(i,j))           ! 식생 항력
       + par%lwave*s%Fx(i,j)/(par%rho*s%hum(i,j))   ! wave force (radiation stress)
       - fc*s%vu(i,j)                               ! Coriolis
uu = uu + dt*dudt   ; |dudt| ≤ par%maxfacg*par%g    ! robustness clamp
```
- **압력경사** `dzsdx = ∂(zs + ph)/∂s`(:139) — `zs` 수위 + **`ph` 비정수압 pressure head**(nonh 모드 결합, hydrostatic 시 ph=0).
- **wave force** `Fx/Fy` = wave action balance 의 radiation stress 경사(`lwave` 토글) — surfbeat 의 흐름 구동원.
- **Coriolis** `fc = 2·wearth·sin(lat)`(:118).
- `dudt` 를 `±maxfacg·g` 로 clamp(급격 가속 억제, dry/shock 안정).

## 2. Bed friction — Ruessink et al. 2001 (flow_timestep.F90:535-556) ★

```fortran
taubx = cfu*par%rho*ueu*sqrt((1.16*urms)**2 + vmageu**2)    ! Ruessink 2001
```
- **파 궤도속도 `urms` 포함**(계수 1.16) — surfzone 에서 파동 orbital motion 이 평균류 bed shear 를 증폭(순수 평균류 friction 과 결정적 차이). `cfu` = bed friction 계수([[xbeach_bed_friction]]). `ueu`=GLM u, `vmageu`=속도 크기.
- cap: `|taubx| ≤ 100·g·ρ·hu`(과대 friction 방지, :543).

## 3. Eddy viscosity (flow_timestep.F90:365-530)

- `par%viscosity==0` 이면 skip(계산 절감).
- background(user `nuh` 또는 **Smagorinsky**) + **breaking-induced** viscosity: `where(s%breaking/=0)` 롤러/쇄파 난류로 `nuh` 증가(:379-403) — 쇄파역 momentum 혼합·longshore current 형성. `nuhv` factor 로 d²v/dx² 상호작용 증가.

## 4. 2nd-order MacCormack (flow_secondorder.F90)

기본 1차 upwind advection 에 **MacCormack predictor-corrector 2차 보정**:
- `flow_secondorder_advUV`(:85) — U/V advection 2차 보정(upwind difference `delta2`).
- `flow_secondorder_advW`(:390) — W(연직속도) 보정(nonh 전용).
- `flow_secondorder_con`(:686) — 연속방정식 2차 보정.
- `par%secorder` 토글. 수치확산 감소(파/front sharpness 보존).

## 5. Continuity + 수위 update

연속방정식 `∂zs/∂t = -∇·(h·u)` 로 수위 `zs` 갱신(`dzsdt`, flux divergence). `wetz` mask(wetting-drying), `hu/hv` = u/v-point 수심, `hum/hvm` = 운동량 수심. boundary 에서 `uu` 외삽(:585-589).

**마스크 산정(2026-07-12 보강)**: wet/dry 마스크는 본 파일이 아닌 `wetcells.F90 compute_wetcells` 에서 매 스텝 산정 — `hh>eps+numeps`→`wetz=1`(:108-111), `wetu` 는 `hu`·`hum` **둘 다** `>eps+numeps` 요구(:75-77, "correct advection term" 주석), `wete` 는 `hh+delta·H>eps .or. wetz==1`(:117). 임계 `eps` 기본 **0.005 m**(params.F90:1398, 허용 0.001-0.1). 초기화는 `zs>zb+eps`(initialize.F90:1062-1071). 형태학 갱신 후에는 morphevolution.F90:3202-3208 이 **`wetz` 만** 재판정 + dry 셀 `zs=zb+eps`·`hh=eps` 클램프 — `wetu/wetv/wete` 는 그 자리에서 재산정되지 않고 다음 스텝 `compute_wetcells` 에서 갱신(범위 한정 = 2026-07-12 Codex 재검증).

## 6. 모드별 차이

| 모드 | 흐름 | 압력 |
|---|---|---|
| **stationary/surfbeat** | wave-averaged GLM 흐름 + `Fx`(radiation stress) | hydrostatic(ph=0) |
| **nonh** | wave-resolving + `Fx` 없음(파 직접 해상) | + `ph` 비정수압([[xbeach_nonh]] 후속) |

→ 동일 `flow` solver 가 압력항 `ph`·wave force `Fx` 유무로 모드 분기.

## 7. 연결

- [[xbeach_mode_dispatch]] — surfbeat/nonh/stationary 가 이 flow solver 공유
- [[xbeach_bed_friction]] — `cfu` 계수 산출(본 노트는 taubx 적용)
- [[xbeach_vegetation]] — `Fvegu` 식생 항력 항
- [[xbeach_morphology]] — `taubx` bed shear → sediment transport(transus)
- wave action balance(`Fx` radiation stress 공급) / nonh(`ph` 압력) — 후속 노트
- Ruessink et al. 2001 (wave-orbital bed friction) / Smagorinsky 1963 (eddy viscosity)
