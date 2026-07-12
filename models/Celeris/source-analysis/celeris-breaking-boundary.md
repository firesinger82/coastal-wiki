---
title: "Celeris-WebGPU 쇄파·경계·wet/dry — Pass_Breaking + BoundaryPass"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/{Pass_Breaking,BoundaryPass,Update_neardry}.wgsl + js/{Wave_Generator,Handler_BoundaryPass,Handler_PassBreaking}.js 직접 read. 라인 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 상위: [../README.md](../README.md) · 파이프라인 순서: [celeris-pipeline-graph.md](celeris-pipeline-graph.md) · 텍스처/ping-pong 인프라: [celeris-webgpu-infrastructure.md](celeris-webgpu-infrastructure.md)
> 비교: FUNWAVE 쇄파(`breaker.F`) → [../../FUNWAVE/source-analysis/funwave-physics-sources.md](../../FUNWAVE/source-analysis/funwave-physics-sources.md)

Celeris-WebGPU 파이프라인의 **6번 Breaking 패스**와 **7번 BoundaryPass**, 그리고 wet/dry 보조 패스(`Update_neardry`)를 다룬다. 세 패스 모두 임시 텍스처(`txtemp_*`)에 쓰고, JS가 canonical state로 복사한다(인프라 노트 참조).

---

## 1. 쇄파 모델 — eddy-viscosity (Kennedy 류)

`Pass_Breaking.wgsl`은 **Kennedy et al. eddy-viscosity 쇄파 모델**(소스 주석 명시, `shaders/Pass_Breaking.wgsl:98`)을 구현한다. FUNWAVE `breaker.F`의 점성형 쇄파(eddy-viscosity breaker)와 동일 계열이며, sub-grid Smagorinsky 점성을 더하는 자리도 마련돼 있으나 **현재 비활성**(`nu_Smag = 0.0`, `Pass_Breaking.wgsl:128-129`).

### 1.1 트리거 변수 — ∂η/∂t와 쇄파 "나이" t

- `detadt = textureLoad(dU_by_dt, idx, 0).x` (`:55`) — 자유수면 시간변화율 ∂η/∂t. Pass2/Pass3가 만든 `dU_by_dt` 텍스처의 x채널에서 읽음.
- `t_here` — 셀의 쇄파 시작 시각(breaking age 마커). `txBreaking.x`에서 읽고(`:58`), **지배 유향(dominant flow direction)의 상류 3셀** 중 최댓값과 max를 취해 전파시킨다(`:62-83`). |P|>|Q|이면 동/서, 아니면 남/북 이웃을 보고, 흐름 부호에 따라 상류측 3-cube를 선택(`:62-82`). 즉 쇄파 상태는 흐름 방향으로 advect된다.

### 1.2 임계 기준(criterion) — WGSL 그대로 전사

국소 수심 `h_here = eta_here - B_here`, `c_here = sqrt(g·h)` (`:92-94`). 기준 변수 3종(`:100-102`):

```wgsl
let T_star = globals.T_star_coef * sqrt(h_here/globals.g);   // 쇄파 지속 시간 스케일
let dzdt_I = globals.dzdt_I_coef * c_here;                    // 개시(initiation) 임계
let dzdt_F = globals.dzdt_F_coef * c_here;                    // 종료(final) 임계
```

**계수 기본값(2026-07-12 확인)**: `dzdt_I_coef=0.50`('start breaking parameter')·`dzdt_F_coef=0.15`('end')·`T_star_coef=5.0`('length of time until breaking becomes fully developed')·`delta_breaking=2.0`('eddy viscosity coefficient') — constants_load_calc.js:51-54.

쇄파 나이에 따라 임계 `dzdt_star`를 시간 보간(`:104-112`):

```wgsl
if(t_here <= globals.dt){                     dzdt_star = dzdt_I; }      // 새로 시작 → 높은 임계
else if (total_time - t_here <= T_star){
    dzdt_star = dzdt_I + (total_time - t_here)/T_star * (dzdt_F - dzdt_I); } // 선형 완화
else {                                         dzdt_star = dzdt_F; }      // 성숙 쇄파 → 낮은 임계
```

즉 막 시작한 쇄파는 개시 임계 `dzdt_I`(큰 값)를 써야 발동하고, 이미 쇄파 중(`T_star` 이내)이면 임계가 `dzdt_F`까지 점진 하강해 더 쉽게 유지된다 — Kennedy 모델의 hysteresis 핵심.

### 1.3 쇄파 강도 B와 점성

`detadt`를 `dzdt_star`와 비교해 강도 `B_Breaking ∈ [0,1]` 결정(`:114-123`):

| 조건 | B_Breaking | t_here 갱신 |
|---|---|---|
| `detadt < dzdt_star` | 0 (쇄파 아님) | `t_here = 0` (리셋, `:116`) |
| `dzdt_star ≤ detadt ≤ 2·dzdt_star` | `detadt/dzdt_star - 1` (선형 램프) | 새 셀이면 `t_here = total_time` (`:122`) |
| `detadt > 2·dzdt_star` | 1 (완전 쇄파) | 새 셀이면 `t_here = total_time` (`:119`) |

eddy 점성(`:125`):

```wgsl
let nu_breaking = min(1.0 * dx*dy/dt,  B_Breaking * delta_breaking * h_here * detadt);
```

`B·δ_b·h·(∂η/∂t)` 형태(δ_b = `delta_breaking`)에 수치 안정 상한 `dx·dy/dt`을 건다. 이는 FUNWAVE eddy-viscosity breaker의 ν ∝ δ²·h·(∂η/∂t) 구조와 동형(δ_b가 길이 스케일 역할).

### 1.4 점성 플럭스 출력 → Pass3가 소비

`nu_total = nu_breaking + nu_Smag`을 각 모멘텀 구배(`dPdx,dPdy,dQdx,dQdy`, `:85-89`)에 곱해 `nu_flux` 작성(`:132-140`):

- `txDissipationFlux ← (nu·dPdx, nu·dPdy, nu·dQdx, nu·dQdy)` (`:143`)
- `txtemp_Breaking ← (t_here, nu_breaking, B_Breaking, nu_Smag)` (`:141,144`)

Boussinesq/COULWAVE `Pass3` 변형이 `txDissipationFlux`를 다시 미분해 모멘텀 확산항으로 더한다(docs 명시). `txtemp_Breaking`의 x채널(`t_here`)이 다음 스텝 `txBreaking`로 복사돼 쇄파 나이를 잇는다. 바인딩은 `Handler_PassBreaking.js:91-134` (txBreaking 입력 binding 6, 출력 txtemp_Breaking binding 8).

---

## 2. BoundaryPass — 경계 유형 열거 (가장 두꺼운 섹션)

`main()`은 한 셀에서 **periodic → sponge → solid → incident wave → river stage/discharge → island/negative-depth cleanup** 순으로 `BCState`를 덮어쓴다(`shaders/BoundaryPass.wgsl:184-595`). 네 변(`west/east/south/north`) 각각 `*_boundary_type` 정수로 분기. 타입 코드:

| 코드 | 의미 | 분기 |
|---|---|---|
| ≤1 (0,1) | solid wall (0) / 그 외 (1) | `:307,318,329,340` |
| 1 | sponge layer | `:264,273,282,291` |
| 2 | incident wave injection | `:352,369,386,403` |
| 3 | periodic | `:203,217,231,245` |
| 4 | river stage/discharge | `:448,463,475` |

> 주의: solid 분기는 `*_boundary_type <= 1`이라 type 1은 sponge 블록과 solid 블록 양쪽에 걸린다(sponge가 먼저 적용된 뒤 가장자리 1~2셀이 solid로 덮임).

### 2.1 Solid wall — 미러링된 모멘텀

가장자리 셀을 내부 거울상으로 채우고 **법선 모멘텀 부호 반전**(`:61-83`):

| 함수 | real_idx | 반환 부호 |
|---|---|---|
| `WestBoundarySolid` (`:61`) | `(boundary_shift - x, y)` | `(η, -hu, hv, sed)` |
| `EastBoundarySolid` (`:67`) | `(reflect_x - x, y)` | `(η, -hu, hv, sed)` |
| `SouthBoundarySolid` (`:73`) | `(x, boundary_shift - y)` | `(η, hu, -hv, sed)` |
| `NorthBoundarySolid` (`:79`) | `(x, reflect_y - y)` | `(η, hu, -hv, sed)` |

적용: 가장자리 ≤1셀은 전체 미러(`:309` 등), 한 셀 안쪽(x==2 등)은 법선속도만 0으로(`:311-314`). 모든 solid 셀에서 `BCState_Sed = zero`.

### 2.2 Sponge / damping — 0을 향한 cosine 감쇠

`*BoundarySponge`(`:85-107`)는 cosine 윈도우를 0.005승한 감쇠계수 γ로 state 전체(η,hu,hv,sed)를 곱한다:

```wgsl
let gamma = pow(0.5 * (0.5 + 0.5*cos(PI*(BoundaryWidth - idx.x + 2)/(BoundaryWidth-1))), 0.005);
```

`main`은 네 변 sponge를 **거리 가중 평균**으로 합성(`:259-302`): 변마다 선형 가중 `s`로 `state_sum += s·state`, 마지막에 `BCState = state_sum/weight_sum`(`:300-301`). 코너에서 두 sponge가 겹쳐도 부드럽게 섞임. 모든 sponge 셀에서 `BCState_Sed = zero`(`:269` 등). γ<1이라 매 스텝 진폭이 줄어 흡수 경계 역할.

### 2.3 Periodic — 2셀 overlap 교환

`periodic_overlap = 2`(`:201`). 한쪽 끝 2셀을 반대편 내부에서 통째로 복사(state·sed·breaking 모두), overlap 경계 셀 1개는 법선 플럭스를 양끝 평균으로 봉합:

| 변 | 끝 셀 복사 | 봉합 셀 |
|---|---|---|
| west (`:203`) | `x ≤ 1` ← east 내부 (`:204-209`) | `x==2`: `BCState.y = 0.5(.y+동측.y)` (`:210-213`) |
| east (`:217`) | `x ≥ W-2` ← west 내부 (`:218-223`) | `x==W-3`: 동일 (`:224-227`) |
| south (`:231`) | `y ≤ 1` ← north 내부 (`:232-237`) | `y==2`: `BCState.z` 평균 (`:238-241`) |
| north (`:245`) | `y ≥ H-2` ← south 내부 (`:246-251`) | `y==H-3`: 동일 (`:252-255`) |

periodic에서는 breaking state도 함께 복사(`:208,222,236,250`)돼 쇄파가 경계를 넘어 이어진다.

### 2.4 Incident wave injection — sine / transient / solitary

type==2 변, 가장자리 ≤2(또는 ≥W-3 등)셀에 주입(`:352-417`). `incident_wave_type`으로 파형 선택:

- **type ≤ 2 → sine (또는 transient pulse)**: `BoundarySineWave`(`:168`)가 `txWaves`의 `numberOfWaves`개 성분을 합산(`:176-179`). 각 성분 `sineWave`(`:135-166`):
  - `omega=2π/T`, `k`는 `calc_wavenumber_approx`(천수 분산 근사, `:109-112`)로 추정.
  - `eta = amplitude·sin(ωt - kx - ky + phase)·min(1, t/T)` — ramp-up(`:154`).
  - **type==2면 transient**: `num_waves=4`로 4파 후 cos-taper로 꺼짐(`:156-161`) → 유한 wave train.
  - 모멘텀 `hu = g·eta/(c·k)·tanh(kd)·cosθ` (선형 천수 관계, `:162-164`).
  - Hs "finger" 줄이려 origin을 시간에 따라 천천히 이동(`yshift/xshift`, `:142-150`).
- **type == 3 → solitary**: `SolitaryWave`(`:114-133`). sech² 프로파일:
  - `eta = a/cosh²(k(x'cosθ + y'sinθ - c·t))`, `a=0.5`(하드코딩, `:121`), `k=sqrt(0.75·a/d³)`, `c=sqrt(g(a+d))`.
  - 각 변마다 origin `(x0,y0)`와 입사각 θ 지정(west θ=0, east θ=-π, south θ=π/2, north θ=-π/2; `:360-414`).

depth는 `base_depth`(균일 가정, `:116,169`)에서 가져옴 — 실제 bathy 미사용(주석 처리). 모든 incident 셀에서 `BCState_Sed = zero`.

### 2.5 River stage/discharge — 상수 stage·유량 (type 4)

홍수 재현빈도 선택(`incident_wave_type 10~14 → 10/50/100/200/500-yr`, `:419-442`)으로 `(stage_c, Q_c)` 결정. 채널 단면 사다리꼴 가정으로 유속 산출(`:444-446`):

```wgsl
stage_elevation = mean_upstream_channel_elevation + stage_c;
stage_speed = Q_c / stage_c / (channel_bottom_width·cos(angle) + stage_c/channel_side_slope);
```

| 변 | 역할 | 셀 조건 | 주입 |
|---|---|---|---|
| west (type 4) | upstream 유입 | `x≤1` & 채널 폭 내 (`:451`) | `(stage_elev, +hu, +hv, conc)` (`:457`) |
| east (type 4) | downstream 유출 | `x≥W-2` & 채널 폭 내 (`:464`) | `(stage_elev-5, -hu, -hv, 0)` (`:469`) |
| north (type 4) | upstream(LARIVER) | `y≥H-2` & 폭 내 (`:477`) | `(stage_elev, -hu, -hv, conc)` (`:483`) |

`flow_depth = max(stage_elevation - B_here, 0)`로 수심 한정. `conc`는 30초 주기로 0/1 토글되는 tracer 펄스(`:456,482`). river 셀은 `BCState_Sed`와 `BCState_Breaking` 모두 0 리셋(`:458-459` 등).

### 2.6 Sediment reset

위 모든 분기(sponge·solid·incident·river)에서 `BCState_Sed = zero`(또는 `max(.,zero)`로 음수 농도 방지, `:196`). 즉 경계는 퇴적물 농도 source가 아니며, river만 tracer `conc`를 state의 4번째 채널로 별도 주입.

### 2.7 Breaking propagation

`BCState_Breaking`은 기본적으로 `txBreaking`을 그대로 통과(`:189`)시키되 periodic에서 이웃 복사(`:208` 등), river에서 0 리셋(`:459,471,485`). 마지막에 `txtemp_Breaking ← BCState_Breaking`(`:594`)로 다음 스텝에 전달.

### 2.8 Wet/dry · 음수 수심 · 단일셀 island 억제 (cleanup)

경계 강제 이후 셰이더 끝에서 shoreline 안정화(`:490-590`). `delta`(최소 수심)와 이웃 bathy 차로 `h_cut` 계산(`:527-531`), 각 방향 dry 플래그(`:533-543`), `sum_dry` 집계(`:545`).

| 케이스 | 조건 | 처리 |
|---|---|---|
| 고립 wet 셀(island) | `dry_here==1 & sum_dry==0` & 내부 (`:562-563`) | 정지: `(max(η,B) 또는 B, 0,0,0)` (`:564-571`) |
| 단일격자 channel 끝 | `sum_dry==1` & (`algochanges==0` 또는 nearshore≤delta) (`:573`) | 인접 wet η 평균으로 freeze, 속도 0 (`:574-576`) |
| 음수/얕은 수심 | `h_here = BCState.x - B_here ≤ delta` (`:581-582`) | `η=max(η,B)`(수중) 또는 `η=B`(육상), 속도 0 (`:583-589`) |

`boundary_boolean`(`:556-559`)으로 진짜 경계 셀은 island 제거에서 제외. 음수 수심 clamp는 무조건 마지막에 적용해 dry 셀 속도를 0으로 강제 → 수치 폭주 방지.

### 2.9 출력 → JS 복사

`main` 끝에서 임시 텍스처에 기록(`:592-594`): `txNewState ← BCState`, `txNewState_Sed ← BCState_Sed`, `txtemp_Breaking ← BCState_Breaking`. canonical state로의 복사는 JS(`Handler_BoundaryPass.js`는 바인딩만 정의, binding 5/6/8이 write-only storage)가 담당. 입력 state는 binding 1 `current_stateUVstar`(`Handler_BoundaryPass.js:100-147`). ping-pong 세부는 인프라 노트 참조.

---

## 3. Wave generation — waves.txt → txWaves

`Wave_Generator.js`(Codex 추가, `:1-2`)가 incident wave 성분 배열을 만들어 `txWaves`에 올린다. 각 성분 행 = `[amplitude, period, direction(rad), phase]` (BoundaryPass `sineWave`의 인자 순서 `wave.r/g/b/a`와 일치, `BoundaryPass.wgsl:177-178`).

- **단일 sine**(`buildSineWaveData`, `Wave_Generator.js:44-50`): `[0.5·H, T, dir(rad), 0]` — 진폭은 파고의 절반. `incident_wave_H/T/direction`(config)에서.
- **TMA/JONSWAP 스펙트럼**(`buildTmaWaveData`, `:52-131`): JONSWAP 에너지(`calculateJonswapEnergy`, `:179-190`, γ=3.3)에 cos-power 방향 분포(`:192-213`)를 곱해 다방향 성분 생성. 주파수 100개(`fp/3 ~ 3·fp`, `:133-147`), 방향 ±20°/5°(`:149-160`). 입력 파고로 재정규화(`scaleDirectionalSpectraToInputHeight`, Hs=4.004·√E0, `:215-231`), 에너지 1% 미만 절단(`:233-241`). 위상은 random(`:125`).
- **주기경계 보정**(`fitDirectionToPeriodicBoundary`, `:243-275`): 각 성분의 along-boundary 파장이 경계 길이에 정수배로 맞도록 방향을 미세 조정 → periodic 경계에서 위상 불연속 방지. 경계 기하(길이·각도·수심)는 `getIncidentBoundaryGeometry`(`:277-301`)가 활성 type==2 변에서 도출.

BoundaryPass는 매 스텝 `txWaves`의 `numberOfWaves` 행을 합산(`BoundaryPass.wgsl:176-179`)하므로, JS는 파라미터 변경 시에만 텍스처를 재생성(TMA 결과 캐시, `:22-23,59-72`). transient(type 2)는 JS가 아닌 셰이더 `sineWave`의 4파 taper(`:156-161`)로 처리.

---

## 4. Wet/dry treatment — near-dry 플래그

`Update_neardry.wgsl`(`:1-56`)은 `txBottom`의 **4번째 채널(.w)**에 near-dry 플래그를 유지한다. bathy 변경(예: 침식·dhdt) 후 호출.

- **near-dry 판정**(`:18-35`): 셀 주변 ±3칸(`lengthCheck=3`) 윈도우 안에 `bathy(.z) ≥ 0`(육상)인 점이 하나라도 있으면 `B_here.w = -99`, 없으면 `+99`. 즉 .w<0 = "물가 근처(near-dry)", .w>0 = "깊은 물(safe)".
- **단일점 island 제거**(`:37-52`): `.z>0`(육상)인데 4방향 이웃이 모두 `.z<0`(수중)이면 그 점을 물로 바꿈(`.z=0`), 경사 .x/.y는 이웃 절반으로 채워 격리 봉우리 제거.
- 출력은 임시 `txtemp_bottom`(`:54`); JS(`Handler_Updateneardry.js:34-53`, binding 1 입력 txBottom → binding 2 출력 txtemp_bottom)가 canonical `txBottom`으로 복사.

이 .w 플래그는 flux 패스(Pass1)가 near-dry 셀에서 보수적 Riemann/재구성을 쓰도록 gate하는 데 쓰인다(flux 노트 영역). BoundaryPass의 cleanup(§2.8)은 .w와 독립적으로 `delta`·이웃 bathy로 매 스텝 wet/dry를 재판정한다 — 두 메커니즘이 별개임에 유의.

> **공통 패턴**: 세 패스 모두 "임시 텍스처에 write → JS가 canonical로 copy"를 따른다. WebGPU storage 텍스처는 같은 패스에서 read+write 불가하므로 ping-pong이 강제된다(인프라 노트 [celeris-webgpu-infrastructure.md](celeris-webgpu-infrastructure.md) 참조).
