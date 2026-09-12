---
title: "XBeach 유동 solver — 운동량 잔차·선박 압력수두·비정수압 보정·연속식 연결"
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
source_correction_date: 2026-09-12
source_correction_by: "Codex"
source_correction_scope: "`ph`의 선박 귀속, 운동량 잔차 부호, 실제 2차 보정 호출과 강우 소비를 정정"
source_correction_human_approval: not-issued
---

> **2026-09-12 AI 출처 정정**: `ph`의 선박 귀속, 운동량 잔차 부호, 실제 2차 보정 호출과 강우 소비를 정정. 기존 `verification_*`는 이전 검증 이력이며 이번 정정의 새 사람 승인이 아니다. [원문 구간·SHA와 연결 판정](../../../_staging/total-read/model-audit/XBeach/connectivity/runtime-20260912/evidence.json)을 따르며 원본 솔버는 수정하지 않았다.

# XBeach NLSWE flow solver (flow_timestep / flow_secondorder)

> `flow_timestep.F90`(1102, subroutine `flow`) + `flow_secondorder.F90`(1063) 직접 read. XBeach 의 **깊이평균 비선형 천수방정식(NLSWE) 흐름 solver** — surfbeat(wave-averaged GLM 흐름 + wave force) · nonh(wave-resolving + non-hydrostatic 압력) 모드가 공유([[xbeach_mode_dispatch]]). bed friction 계수 자체는 [[xbeach_bed_friction]], 본 노트는 **운동량·연속 방정식 solver**.

## 1. Explicit Euler 운동량과 압력수두

아래는 배열 첨자를 생략한 **AI 전사·축약식**이다. 소스의 `dudt`는 속도에 더하는 가속도가 아니라, 갱신에서 **빼는 잔차**다. (`flow_timestep.F90:563-580`)

```text
dudt = ududx + vdudy - viscu + g*dzsdx
       + taubx/(rho*hu) + Fvegu/(rho*hu)
       - lwave*Fx/(rho*hum) - fc*vu
       - rhoa*Cd*windsu*sqrt(windsu²+windnv²)/(rho*hum)
dudt = clamp(dudt, -maxfacg*g, maxfacg*g)
uu = uu - dt*dudt
```

따라서 u의 Coriolis 속도 증분은 `+dt*fc*vu` 방향이다. v 잔차의 Coriolis 항은 `+fc*uv`이며 `vv -= dt*dvdt`로 갱신한다. 두 식은 각각 `wetu==1`, `wetv==1`에서 적용되고 건조점 속도는 0이 된다. (`flow_timestep.F90:563-580, 597-616`)

`dzsdx/dzsdy`는 `zs+ph`의 격자 방향 경사다. 여기서 **`ph`는 선박에 의한 압력수두 [m]**다. `shipwave`는 선박 위치·방향을 보간하고 선박 격자의 압력수두를 `s%ph`로 사상한다. 이 호출은 `ships==1`일 때 `flow`보다 먼저 실행된다. nonh의 압력은 별도의 `s%pres`와 국소 보정량 `dp`로 계산한다. (`variables.def:256`; `ship.F90:287-337, 365-373`; `libxbeach.F90:293-310`; `flow_timestep.F90:131-149`; [[xbeach_nonh]])

## 2. Bed friction — Ruessink et al. 2001 (flow_timestep.F90:535-556) ★

```fortran
taubx = cfu*par%rho*ueu*sqrt((1.16*urms)**2 + vmageu**2)    ! Ruessink 2001
```
- **파 궤도속도 `urms` 포함**(계수 1.16) — surfzone 에서 파동 orbital motion 이 평균류 bed shear 를 증폭(순수 평균류 friction 과 결정적 차이). `cfu` = bed friction 계수([[xbeach_bed_friction]]). `ueu`=GLM u, `vmageu`=속도 크기.
- cap: `|taubx| ≤ 100·g·ρ·hu`(과대 friction 방지, :543).

## 3. Eddy viscosity (flow_timestep.F90:365-530)

- `par%viscosity==0` 이면 skip(계산 절감).
- background(user `nuh` 또는 **Smagorinsky**) + **breaking-induced** viscosity: `where(s%breaking/=0)` 롤러/쇄파 난류로 `nuh` 증가(:379-403) — 쇄파역 momentum 혼합·longshore current 형성. `nuhv` factor 로 d²v/dx² 상호작용 증가.

## 4. 실제 실행되는 2차 보정

| 루틴 | 현재 호출 조건과 위치 |
|---|---|
| `flow_secondorder_advUV` | `secorder==1`, `flow_timestep.F90:645-652` |
| `flow_secondorder_huhv` | `secorder==1`, 유량 계산 전 수심 보정, `flow_timestep.F90:706-719` |
| `flow_secondorder_advW` | nonh의 세 predictor에서 `secorder==1`, `nonh.F90:1234-1262, 1844-1883, 2858-2935` |
| `flow_secondorder_con` | 정의는 `flow_secondorder.F90:686-824`에 있지만 `flow_timestep.F90:754-759`의 호출은 주석 처리됨 |

따라서 `secorder=1`을 연속식 MacCormack 보정까지 실행한다는 뜻으로 읽으면 안 된다. 해당 호출 주석은 감쇠 때문에 제거했다고 기록한다. nonh에서는 압력 predictor → 조건부 U/V 2차 보정 → 압력 corrector 순서로 실행한다. (`flow_timestep.F90:635-658`)

## 5. Continuity + 수위 update

연속식은 격자 유량 발산에 `-infil + rainfallrate`를 더해 `zs += dt*dzsdt`로 갱신한다. 수평 유량 경계 적용 뒤, `rainfall==1`이면 강우를 갱신하고 연속식이 즉시 소비한다. (`flow_timestep.F90:724-751`; [[xbeach_tide_forcing]]) `wetz` mask(wetting-drying), `hu/hv` = u/v-point 수심, `hum/hvm` = 운동량 수심. boundary 에서 `uu` 외삽(:585-589).

**마스크 산정(2026-07-12 보강)**: wet/dry 마스크는 본 파일이 아닌 `wetcells.F90 compute_wetcells` 에서 매 스텝 산정 — `hh>eps+numeps`→`wetz=1`(:108-111), `wetu` 는 `hu`·`hum` **둘 다** `>eps+numeps` 요구(:75-77, "correct advection term" 주석), `wete` 는 `hh+delta·H>eps .or. wetz==1`(:117). 임계 `eps` 기본 **0.005 m**(params.F90:1398, 허용 0.001-0.1). 초기화는 `zs>zb+eps`(initialize.F90:1062-1071). 형태학 갱신 후에는 morphevolution.F90:3202-3208 이 **`wetz` 만** 재판정 + dry 셀 `zs=zb+eps`·`hh=eps` 클램프 — `wetu/wetv/wete` 는 그 자리에서 재산정되지 않고 다음 스텝 `compute_wetcells` 에서 갱신(범위 한정 = 2026-07-12 Codex 재검증).

## 6. 모드와 외력의 구분

`flow`의 nonh 압력 호출 조건은 `wavemodel==WAVEMODEL_NONH`다. 이때 `nonh_cor(...,0)`와 `nonh_cor(...,1)`이 예측·보정을 수행한다. 선박 압력수두 `ph`의 공급 조건은 별도 `ships==1`이다. `ph`를 기준으로 stationary/surfbeat와 nonh를 구분할 수 없다. (`flow_timestep.F90:635-658`; `libxbeach.F90:293-310`)

`swave`의 nonh 기본값은 0이지만 입력으로 1도 허용하며, 운동량의 `Fx/Fy`에는 `lwave`가 곱해진다. 따라서 모드 이름만으로 모든 구성에서 파력항이 없다고 단정하지 않는다. (`params.F90:98-109`; `flow_timestep.F90:563-612`)

## 7. 연결

- [[xbeach_mode_dispatch]] — surfbeat/nonh/stationary 가 이 flow solver 공유
- [[xbeach_bed_friction]] — `cfu` 계수 산출(본 노트는 taubx 적용)
- [[xbeach_vegetation]] — `Fvegu` 식생 항력 항
- [[xbeach_morphology]] — `taubx` bed shear → sediment transport(transus)
- [[xbeach_wave_action_balance]] — 파력 공급; [[xbeach_nonh]] — `pres/dp` 압력 보정
- Ruessink et al. 2001 (wave-orbital bed friction) / Smagorinsky 1963 (eddy viscosity)
