---
title: "저면마찰(bottom friction) cross-model 대조 — 10개 모델 (법칙·조도 knob·implicit 처리·wave-current BBL)"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "전 행이 각 모델 verified source-analysis 노트로 소급(각 셀에 노트 링크+file:line). 대표 anchor 직접 재확인(2026-07-07): Delft3D taubot.f90:381-427(Manning/Chezy/W-C/z0)·ROMS set_vbc.F:597-615(LOGDRAG+clamp)·LISFLOOD-FP cuda/adaptive/operators/apply_friction.cuh:41-52(반음해 Jacobian). 미커버 셀은 §5에 disclosed."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - models/EFDC/source-analysis/efdc_bottom_friction.md
  - models/SWASH/source-analysis/swash-bottom-friction-wind.md
  - models/XBeach/source-analysis/xbeach_bed_friction.md
  - models/ROMS/source-analysis/roms_bottom_boundary_layer.md
---

# 저면마찰 cross-model 대조 (10모델)

> **Canonical source 규칙**: 각 모델 상세는 해당 source-analysis 노트가 진실의 원천 — 본 노트는 **대조 축**만 제공. cross-model 시리즈: EOS([[roms_equation_of_state]] §대조)·스칼라 transport(4모델, [[roms_tracer_timestep_step3d_t]] 계열)에 이은 3번째.

## 0. 물리 구분 — 같은 "bottom friction"이라도 세 가지 물리

| 부류 | 대상 | 모델 |
|---|---|---|
| **A. 흐름 bed shear** τ_b (운동량 sink) | 평균류/천수 유속 | EFDC·Delft3D·ROMS·ADCIRC·SWASH·SFINCS·LISFLOOD-FP·FUNWAVE·Celeris·XBeach(flow) |
| **B. 파랑 스펙트럼 저면소산** S_ds,b (에너지 sink) | 파 궤도속도 | SWAN (흐름은 안 풂 — [[swan-tech-ch2-dissipation-detailed]]) |
| **C. 파 궤도속도 마찰 소산** D_f=c·ρ·f_w·u_orb³ | wave action sink | XBeach(fw, [[xbeach_bed_friction]]) — A와 별도 계수 |

## 1. 흐름 마찰 법칙·knob 대조 (부류 A)

| 모델 | 법칙(선택지) | 핵심식 (조도→drag) | knob·기본값 | 근거 |
|---|---|---|---|---|
| **EFDC+** | log-law 유도 2차 drag 3분기(GOTM 반복/DSI/legacy) | DSI `STBX=(κ/(ln(H/ZBR)−0.8))²`(caltbxy.f90:542, Nezu-Nakagawa wake) | `ZBR`(조도길이) — 최다 캘리브 knob, `H/ZBR≥7.5` 하한(:538) | [[efdc_bottom_friction]] |
| **Delft3D-FLOW** | Chezy(기본)/Manning/White-Colebrook + 3D z₀ | Manning `C=h^{1/6}/n`(taubot.f90:381)·W-C `C=18log₁₀(12h/ks)`(:392-393)·3D `C=√g·ln(1+h/(e·ks/30))/κ`(:395-403)·`τ=ρg·U|U|/C²`(:425-427) | Chezy 65 / n 0.04 / ks 10 m(GUI 기본), trachytope 공간변화 | [[delft3d_flow_compute_aux]]·manual §6 |
| **ROMS** | CPP 3택: UV_LOGDRAG/QDRAG/LDRAG (BBL 정의 시 대체) | LOGDRAG `Cd=κ²/ln²((z₁−z_w0)/Zob)`, `Cdb_min=1e-6≤Cd≤Cdb_max=0.5`(set_vbc.F:597-599, mod_scalars.F:783-784) + dt-기반 응력 clamp(:612-615) | `Zob`/`rdrg`/`rdrg2`(roms.in 입력, 코드 하드디폴트 없음) | [[roms_bottom_boundary_layer]] |
| **ADCIRC** | NOLIBF 3택: 선형/quadratic/**hybrid**(심해 Cd↔천해 Manning형) | hybrid `TK=FRIC·(…(1+(HBREAK/H)^Fθ)^{Fγ/Fθ})`(gwce.F:2479)·Manning→`Cd=g n²/H^{1/3}`(nodalattr.F:2316-2365) | fort.13 nodal attribute(`mannings_n_at_sea_floor` 등), `BFCdLLimit` 하한 | [[adcirc-momentum-implementation]]·[[adcirc-nodal-attributes]] |
| **SWASH** | 6택(상수/Chezy/Manning/Colebrook-White/Nikuradse/선형) | Manning `c_f=g n²/h^{1/3}`(SwashBotFrict.ftn90:196)·Nikuradse `c_f=(κ/ln(33h/(e·ks)))²`(:275, 매끈바닥 Newton 반복 :279-314) | `irough`+`pbot`, 구조/비구조판 식·상수 동일 | [[swash-bottom-friction-wind]] |
| **SFINCS** | Manning 단일 (Bates 2010 semi-implicit) | `q^{n+1}=(q_sm+frc·dt)/(1+g n²dt|q_fr|/h_u^{7/3})`(sfincs_momentum.f90:677) | `manning=0.04` 기본, subgrid 시 수위별 대표 n 테이블(`manningfile` 무시) | [[sfincs_flow_solver]]·[[sfincs_subgrid_quadtree]] |
| **LISFLOOD-FP** | Manning — **솔버별 4방식**(§3) | ACC q-centred 분모 `1+gΔt·h·n²|q|/h^{10/3}`(fp_acc.cpp:88)·diffusive `Q=h^{5/3}S_f/n` explicit(fp_flow.cpp:157)·FV1/DG2·GPU adaptive 반음해 Jacobian(fv1.cpp:141-151, cuda/adaptive/operators/apply_friction.cuh:41-52) | Manning n(parfile/공간 파일), `fricSolver2D=ON` 직교합성 | [[lisflood-fp-classic-acc-flow]]·[[lisflood-fp-swe-fv1-dg2]]·[[lisflood-fp-mwdg2-adaptive-mra]] |
| **FUNWAVE** | Cd quadratic(기본)/Manning(`-DMANNING` 컴파일) | source 항 `−Cd·U·|V|`(explicit) | `Cd fixed`+`FRICTION FILE` 공간변화 | [[funwave-physics-sources]] |
| **Celeris** | 고정 Cd/Manning(`isManning` 스위치) | 운동량 source `−HU·friction_`(Pass3 WGSL, FrictionCalc :67-93) | `friction`·`isManning`(config) | [[celeris-boussinesq-solver]] |
| **XBeach**(flow) | 5택(chezy/cf/manning/white-colebrook/±grainsize) | `τ_bx=c_f·ρ·u_E·√((1.16·u_rms)²+v²)`(flow_timestep.F90:532-552 — **wave-averaged 결합 shear**, Ruessink 2001) | `bedfriction=manning` 권장 n=0.022, grainsize `k=3·D90` | [[xbeach_bed_friction]] |

## 2. 계보 — 세 흐름

1. **z₀/log-law 3D 해양모델**: EFDC(`ZBR`)·Delft3D 3D(`z₀`)·ROMS(`Zob`) — 최하층 유속과 대수분포 가정으로 Cd 유도. 조도**길이**[m]가 knob. 같은 계보라 ZBR↔Zob↔ks/30 상호 환산 가능(주의: EFDC wake −0.8 vs legacy −1.0, Delft3D는 ks=30z₀ 관례).
2. **Manning 계열 천수/범람 모델**: ADCIRC(hybrid의 천해 극한)·SWASH·SFINCS·LISFLOOD·FUNWAVE(-D)·Celeris·XBeach — `Cd=g n²/h^{1/3}` 공통. Manning n[s/m^{1/3}]이 knob. 수심 의존이 자동 내장(천해서 마찰↑).
3. **파랑 소산 별도 축**: SWAN S_ds,b(JONSWAP `C=0.038` 기본, 41.01+ swell 통일 / Collins 0.015 / Madsen kn=0.05 — FRICTION command 미지정 시 **off**)와 XBeach `fw`(D_f∝f_w·u_orb³). 흐름 n/Cd 와 **독립 계수** — 혼동 금지.

## 3. implicit 처리 대조 (wet-dry 안정성의 핵심 분기)

| 방식 | 모델 | 형태 |
|---|---|---|
| **Bates(2010) semi-implicit 분모** | SFINCS(`h^{7/3}`)·LISFLOOD ACC(`h^{10/3}`, q-centred θ=1) | 갱신식 분모에 마찰 — 천수·얕은 wet 셀서 무조건 안정 |
| **반음해 Jacobian** | LISFLOOD FV1/DG2·GPU adaptive(HWFV1/MWDG2 공용 `apply_friction`) | `D_x=1+Δt·Cf(2u²+v²)/(h·|u|)` 로 나눔 |
| **행렬 implicit** | ADCIRC(Coriolis+마찰 2×2 node solve, momentum.F:751-772)·Delft3D(ADI 각 stage implicit)·SWAN(대각 IMATDA 기여, implicit-only) | 계 행렬에 흡수 |
| **explicit(+clamp)** | ROMS(LOGDRAG 응력, dt-기반 상한 clamp)·XBeach(τ_b 100gρh 제한)·EFDC(ISITB 로 implicit 분배 조절)·FUNWAVE·Celeris·LISFLOOD diffusive | 계수/응력 상한으로 보완 |

## 4. wave-current BBL (부류 A 안의 파랑 증폭)

- **EFDC**: Grant-Madsen 형 apparent roughness `ZBRE·(1+0.19·u*_wc/u*_c)` + ripple + analytic BBL 적분(caltbxy.f90:276-498).
- **Delft3D**: Swart(1974) f_w + **선택 가능 BBL 9모델**(FR84·GM79·VR04 등, 매뉴얼 Table 9.5).
- **ROMS**: 별도 BBL 모듈 3종(SSW=Sherwood-Signell-Warner/MB/SG) — `bustrcwmax`가 sediment 침식 구동, moveable-bed ripple feedback.
- **XBeach**: BBL 모델 대신 shear 식에 `1.16·u_rms` 합성(위 표) — 계수 1.16은 캘리브값(변경 금지 주의).
- ADCIRC·SWASH·SFINCS·LISFLOOD·FUNWAVE·Celeris: 흐름 마찰에 파랑 증폭 없음(SFINCS 는 SnapWave `fwuv` 별항, 위상해상 모델은 파를 직접 해상).

## 5. ★함정·미커버 (disclosed gaps)

- **EFDC**: 분기간 상수차(−0.8 vs −1.0) — ICALTB 전환 시 동일 ZBR 라도 유효 drag 변동. `H/ZBR≥7.5` 하한이 고조도 천해 셀 drag 을 clamp. CALTBXY 산출은 **계수**(응력은 hdmt 조립) — [[efdc_bottom_friction]].
- **Delft3D**: cohesive 침식은 total 아닌 **skin friction** 구동([[delft3d_sediment_transport_formulae]]) — 마찰 τ 인용 시 어느 τ 인지 확인.
- **SWAN**: FRICTION command 미지정 시 저면마찰 **완전 off**(기본 활성 아님) — 천해역 과대 파고의 단골 원인.
- **XBeach**: `fwcutoff` 기본 1000 m = 사실상 무게이트. 5 m 등으로 낮추면 도메인 대부분 파마찰 비활성(pitfall).
- **미커버(위키 갭)**: ADCIRC NOLIBF 기본값·HBREAK/FTHETA 수치·3D BBL(vsmy.F) 상세. ~~FUNWAVE `Cd` 기본 수치~~ — **해소(2026-07-12)**: ★`Cd_fixed` 기본 **0.0(마찰 완전 off)** — io.F:2777-2783 이 미지정 시 0.0 대입 + 경고 출력('possibly you used FRICTION_MATRIX'), init.F:887 전 격자 배포. SWAN 기본 off 와 같은 함정 계열(§5 첫 항목과 대구). ~~Celeris FrictionCalc 공식 전개~~ — **해소(2026-07-12)**: Pass3_\*.wgsl:67-92 — `isManning==1`이면 `f=g·n²/h^{1/3}`, 아니면 `f=friction`(무차원 Moody), **f 상한 0.5 클램프**('non-physical above 0.5'), 마찰항 `f·√(hu²+hv²)·2h²/(h⁴+max(h⁴,1e-6))/base_depth²` — ★h⁴ 단정밀도 스케일링으로 **수심 <~5% base_depth 에서 마찰 과소**(소스 주석 disclosed). ★기본 friction=**0.000**·isManning=0(constants_load_calc.js:42-43) — Celeris 도 기본 마찰 0. ~~SWASH `irough` 기본값·입력 키워드~~ — **해소(2026-07-12)**: `FRICtion` 카드 키워드 생략 시 **MANNing 기본**(n=0.019); CON 0.002·CHEZ 65·LOG(SMOOTH 기본)·COLE·LIN=11, 카드 생략 시 마찰 off(irough=0, SwashInit.ftn90:313) — SwashReadInput.ftn90:777-806, [[swash-bottom-friction-wind]] 갱신.

## 6. 관련

- [[efdc_bottom_friction]] · [[swash-bottom-friction-wind]] · [[xbeach_bed_friction]] · [[roms_bottom_boundary_layer]] — 전용 노트 4편
- [[delft3d_flow_compute_aux]] · [[adcirc-momentum-implementation]] · [[sfincs_flow_solver]] · [[lisflood-fp-classic-acc-flow]] — 마찰 포함 solver 노트
- [[swan-tech-ch2-dissipation-detailed]] — 파랑 저면소산 이론(부류 B)
- `concepts/currents/06-model-application.md` §저면마찰 — 본 노트 wrapper 링크
