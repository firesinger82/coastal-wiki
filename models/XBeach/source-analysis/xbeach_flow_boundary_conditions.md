---
title: "XBeach flow 경계조건(boundaryconditions.F90) — offshore front(abs_1d/abs_2d Van Dongeren1997 약반사 흡수-생성 Riemann/wall/nonh_1d) + tide(instant/velocity/hybrid) + lateral(wall/Neumann/abs) + discharge"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/boundaryconditions.F90 (2324) + params.F90(front/tide 상수 507-562) 직접 read — flow_bc(930) front 분기 FRONT_ABS_2D Van Dongeren1997 Riemann beta=u−2√(gh)(1222-1300) + wave_bc(9) + flow_lat_bc(LR_WALL/NEUMANN/ABS_1D 1500-) + discharge_boundary file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — front/tide/lateral BC + Van Dongeren 흡수-생성 verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_wave_boundary_generation.md
  - models/XBeach/source-analysis/xbeach_nonh.md
---

# XBeach flow 경계조건 (boundaryconditions.F90)

> `boundaryconditions.F90`(2324) 직접 read. XBeach **흐름 경계조건** — offshore front·lateral·discharge + tide. [[xbeach_wave_boundary_generation]] 이 생성한 incoming 파/bound-IG 시계열을 offshore 에서 **약반사(weakly-reflective) 흡수-생성** BC 로 부과(외향 반사파는 흡수, 입사파는 생성). [[xbeach_flow_solver]] 의 경계값 공급.

## 1. 4 public 루틴

| 루틴 | 역할 |
|---|---|
| `wave_bc`(:9) | wave 경계 forcing 적용(생성된 boun_U.bcf/nonh 시계열 → offshore 파) |
| `flow_bc`(:930) | tide + offshore **front** BC (§2-3) |
| `flow_lat_bc`(:1500) | lateral(좌우) BC (§4) |
| `discharge_boundary_h/v` | discharge(하천 유입) BC |

## 2. Offshore front BC (flow_bc, params.F90:507-511) ★

`par%front`:
| 값 | BC | 설명 |
|---|---|---|
| `FRONT_ABS_1D` | Ad's radiating(1D 흡수) | 1D 약반사 radiating |
| **`FRONT_ABS_2D`** | **Van Dongeren 1997 weakly-reflective** | 2D 흡수-생성(§3) ★ 표준 surfbeat |
| `FRONT_WAVEFLUME` | wave flume radiating | 수조 재현 |
| `FRONT_WALL` | 완전반사 벽 | reflective |
| `FRONT_NONH_1D` | non-hydrostatic 1D | [[xbeach_nonh]] 결합 BC |

## 3. FRONT_ABS_2D — Van Dongeren 1997 흡수-생성 (boundaryconditions.F90:1222-1300) ★★

**Riemann invariant** 기반 약반사 경계 — 외향(reflected) 파는 통과시켜 흡수, 입사(incoming) 파는 생성:
```fortran
beta = s%uu(1:2,:) - 2*sqrt(g*hum)                          ! Riemann invariant(외향 특성)
bn = -(uu - sqrt(g·hum))·dβ/dx + sqrt(g·hum)·dv/dy − cfu·|U|·uu/hum   ! β 진화(특성 전파)
thetai = atan(vi/ui)                                         ! 입사파 각
! 입사 long wave celerity: freewave=1 → √(gh), else → cg(bound)
uu(1,j) = (order-1)·ui + umean                              ! 생성: 입사(specified) + reflected(computed)
```
- `beta = u − 2√(gh)` = 외향 특성(outgoing Riemann). 경계에서 외향파는 자유 유출(흡수).
- **incoming** `ui/vi` = wave_boundary_generation 이 준 입사 단파+bound IG(specified). **reflected** = total − specified(흡수).
- `par%order`: 1=1차(short wave 만) / 2=2차(bound long wave 포함, surfbeat 표준).
- `par%freewave`: 입사 long wave 가 free(√(gh)) vs bound(cg, 파군속도)로 전파한다고 가정.
- → surfzone 에서 생성된 IG 가 외해로 깔끔히 빠져나가(반사 spurious 제거) + 외해 입사파 정확 생성. surfbeat IG 수지의 핵심.

## 4. Tide (flow_bc, params.F90:561) + lateral

### Tide type `par%tidetype`
- `TIDETYPE_INSTANT`: 전 domain 즉시 조위 적용. `TIDETYPE_VELOCITY`: 경계 유속으로 조석. `TIDETYPE_HYBRID`: 둘 조합(domain 내 wetz 연결 점진, :1114). `tide_boundary_timestep`(compute_tide_module)로 zs0 갱신.

### Lateral `flow_lat_bc` (LR_*, :1500-)
- `LR_WALL`(벽) / `LR_NEUMANN`(수위 gradient 0) / `LR_NEUMANN_V`(속도 Neumann) / `LR_NO_ADVEC` / `LR_ABS_1D`(lateral 흡수). 주로 longshore-uniform 가정 시 Neumann.
- back BC: `BACK_WALL` 등(:1395).

## 5. Discharge BC

`discharge_boundary_h/v` — 지정 위치 하천/유입 discharge(질량 소스). `velocity_Boundary`(boun_U.bcf)로 시변 유속/discharge.

## 6. 결합 chain

```
wave_boundary_generation(입사 단파+bound IG 시계열 boun_U.bcf)
  → wave_bc(읽어 offshore 파 forcing)
  → flow_bc FRONT_ABS_2D(Riemann: 입사 생성 + 외향 흡수) + tide
  → flow_solver(경계 uu/zs)
```

## 7. 연결

- [[xbeach_wave_boundary_generation]] — 입사 단파+bound IG 생성(abs_2d 가 부과하는 specified 파)
- [[xbeach_flow_solver]] — 경계 uu/vv/zs → NLSWE 흐름
- [[xbeach_nonh]] — FRONT_NONH_1D non-hydrostatic 경계
- compute_tide(readtide) — tide zs0
- Van Dongeren & Svendsen 1997 (weakly-reflective absorbing-generating BC)
