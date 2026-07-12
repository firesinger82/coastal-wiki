---
title: "시간적분(time integration) cross-model 대조 — 12개 모델 (스킴 계열·mode splitting·adaptive dt·implicit 성분)"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "전 행이 각 모델 verified source-analysis 노트로 소급(셀에 노트 링크+file:line). 대표 anchor 직접 재확인(2026-07-10): ADCIRC read_input.F:2996(READ A00,B00,C00)·gwce.F:182(CPRECOR)+IS2TIM 전역 rg 0건 / EFDC aaefdc.f90:3187-3188(IS2TIM==0→HDMT, ≥1→HDMT2T) / SWASH SwashComputFlow.ftn90:42-47(Method verbatim 'unconditionally stable…leap-frog') / FUNWAVE mod_global.F:122-123(alpha=(0,3/4,1/3)·beta=(1,1/4,2/3))·main.F:414(ESTIMATE_HUV)·etauv_solver.F:268-270 / SFINCS sfincs_input.f90:70(alfa 기본 0.50) / LISFLOOD SolverParams.h(HWFV1 CFL=0.5·MWDG2 CFL=0.3) / Delft3D adi.f90:282,439(stage1/stage2) / Celeris shaders/Pass3_Bous.wgsl:398-409(Euler/AB3/AM4 분기). 미커버 셀은 §5 disclosed."
note_author: "Claude Fable 5"
note_date: 2026-07-10
related:
  - models/ROMS/source-analysis/roms_barotropic_2d.md
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md
  - models/Delft3D/source-analysis/delft3d_adi_solver.md
  - models/SWASH/source-analysis/swash-timestepping-update-driver.md
---

# 시간적분 cross-model 대조 (12모델)

> **Canonical source 규칙**: 각 모델 상세는 해당 source-analysis 노트가 진실의 원천 — 본 노트는 **대조 축**만 제공. cross-model 시리즈 7탄: EOS·스칼라 transport·[[bottom-friction-cross-model]]·[[vertical-mixing-cross-model]]·[[wetting-drying-cross-model]]·[[wave-breaking-cross-model]] 에 이음.

## 0. 대분류 — 세 가지 설계 축

같은 "시간적분"이라도 모델 계열별로 지배 설계 축이 다르다:

| 축 | 질문 | 분기 |
|---|---|---|
| **A. 스킴 계열** | 시간레벨 몇 개, 어떤 조합? | leapfrog 3TL / predictor-corrector / SSP-RK / AB-AM multistep / ADI 교번 / θ semi-implicit / projection(SMAC) |
| **B. mode splitting** | 빠른 중력파를 어떻게 격리? | barotropic-baroclinic time-split(ROMS) / external-internal(EFDC) / semi-implicit 로 CFL 자체 완화(ADCIRC·Delft3D·FM·SWASH) / 분리 없음(explicit 천수·위상해상) |
| **C. dt 전략** | 고정 vs 적응? | implicit 계열=고정 dt(무조건 안정) vs explicit 계열=CFL adaptive dt(매 스텝 재산정) |

## 1. 모델별 스킴 대조

### 1.1 3D/2D 해양 모델 (mode splitting 계열)

| 모델 | 스킴 | stage 구조 | 핵심 anchor | 근거 |
|---|---|---|---|---|
| **ROMS** | **split-explicit LF-AM3 predictor-corrector** (compile-time 대안 FB LF-AM3/FB AB3-AM4, main3d.F:665,716,810) | pre_step3d(predictor half, AB 기여 pre_step3d.F:16-19) → 2D fast substep `my_iif=1..nfast+1`(step2d_LF_AM3.h:924-2693, AM3 weight 5/12·8/12·−1/12) → step3d_uv/step3d_t(corrector) | weight 설계 set_weights.F:12-182(`nfast≠NDTFAST` — 필터 support 가 NDTFAST 초과 확장), `dtfast=dt/NDTFAST`(read_phypar.F:608) | [[roms_barotropic_2d]]·[[roms_tracer_timestep_step3d_t]]·[[roms_nonlinear_core_remaining]] |
| **EFDC+** | **3TL leapfrog + trapezoidal corrector** (기본) / **2TL** 토글 | dispatch `IS2TIM==0→HDMT / ≥1→HDMT2T`(aaefdc.f90:3187-3188, 직접 재확인). 3TL: `ISTL=3` full leapfrog(DELT=DT2, hdmt.f90:1344-1349) + `ISTL=2` trapezoidal corrector 를 **NTSTBC 주기**로(computational mode 감쇠, ROLD=0.5) | external 연속 CALPUV9C=PCG semi-implicit(calpuv9c.f90:693-707) / 2TL 은 dynamic dt(DTDYN) 가능 | [[efdc_hydro_core]]·[[efdc_external_mode_solver]]·[[efdc_transport_scheme]] |
| **ADCIRC** | **GWCE semi-implicit 3-time-level**: ETA0/1/2 상태 + fort.15 **A00,B00,C00 시간가중**(read_input.F:2996 직접 재확인; RHS 가중 gwce.F:1540-1543) — 별도 θ 파라미터 없음 | ζ(GWCE JCG solve 또는 ILump=1 lumped 대각역산 gwce.F:2001-2017) → U,V(Coriolis+마찰 2×2 implicit momentum.F:751-772) → 옵션 `CPRECOR` predictor-corrector(gwce.F:182 직접 재확인) | time-split 아님 — 순차 semi-implicit 결합. friction 3레벨 TK0/TK/TK2(gwce.F:2477-2482) | [[adcirc-gwce-implementation]]·[[adcirc-timestep-orchestration]]·[[adcirc-momentum-implementation]] |
| **Delft3D-FLOW** | **ADI 2-stage 교번**(Leendertse) | stage1(adi.f90:282, 직접 재확인): ξ방향 SUD(운동량+연속 동시 implicit, double-sweep/CG) + η방향 UZD(implicit advection·연직 diffusion) → stage2(:439) 방향 swap. transport 짝 difu 도 반스텝 `timest` 교번([[delft3d_difu_transport]] — 단 수평은 red-black Jacobi 반복) | ADI 무조건 안정 → 큰 dt | [[delft3d_adi_solver]] |
| **D-Flow FM** | **semi-implicit staggered FV**(Stelling-Duinmeijer 2003·Kernkamp 2011) + **Nested Newton**(Casulli-Zanolli) | `furu`(fu/ru 계수) → `s1nod`(SPD 연속행렬) → Guus solver → back-substitute u1, wetting-drying 비선형은 Newton 반복으로 양정치 보장 | 수위·barotropic implicit(θ), advection explicit | [[delft3d_dflowfm_kernel_scheme]] |

### 1.2 위상해상·비정수압 모델

| 모델 | 스킴 | stage 구조 | 핵심 anchor | 근거 |
|---|---|---|---|---|
| **SWASH** | **mtimei 이분기**: ①semi-implicit θ("unconditionally stable w.r.t. gravity waves, bottom shear, vertical eddy viscosity" — SwashComputFlow.ftn90:42-47 verbatim 직접 재확인) ②explicit **staggered leap-frog(Hansen)** | Imp: θ-연속·수위경사 + MacCormack advection + Euler-implicit 마찰 + Keller-box w + **2차 pressure correction**(Poisson→SIP/BiCGSTAB→projection). Exp: MacCormack 예측-수정, 압력만 implicit | Coriolis 는 modified AB2(첫 스텝 Euler 부트스트랩) | [[swash-timestepping-update-driver]]·[[swash-nonhydrostatic-pressure-solver]]·[[swash-explicit-depthavg-flow]] |
| **FUNWAVE** | **3단 SSP-RK3**(Gottlieb-Shu convex combination) — **계수 직접 재확인**: `alpha=(0, 3/4, 1/3)`·`beta=(1, 1/4, 2/3)`(mod_global.F:122-123; GPU constant 동일 mod_cuda.F:41-42) | 매 스텝 ESTIMATE_DT → RK 3단(main.F:414 ESTIMATE_HUV) — 각 단: MUSCL-TVD/HLL flux → `Eta=α·Eta0+β(Eta+DT·R1)`(etauv_solver.F:268-270) → **분산 tridiagonal 풀이**(매 서브단계, Thomas/MPI 파이프라인/GPU cuSPARSE) | RK 서브단계마다 implicit 분산 solve 가 비용 지배 | [[funwave-dispersion-solver]]·[[funwave-infrastructure]] |
| **Celeris** | **timeScheme 3분기**(Pass3_Bous.wgsl:398-409 직접 재확인): ⓪Euler `U+dt·d/dt` ①**AB3 predictor** `dt/12·(23dⁿ−16dⁿ⁻¹+5dⁿ⁻²)` ②**AM4 corrector** `dt/24·(9dⁿ⁺¹+19dⁿ−5dⁿ⁻¹+dⁿ⁻²)` | predictor 패스 → (timeScheme==2 시) corrector 재실행, history 텍스처 rotation. 분산 좌변은 PCR tridiagonal | 계수 위치는 shader 측(§5 — JS 는 uniform 세팅만) | [[celeris-boussinesq-solver]]·[[celeris-pipeline-graph]] |
| **XBeach** | **explicit Euler 1차**(flow_timestep.F90:559-593) + 옵션 MacCormack 2차(flow_secondorder.F90); **nonh 모드**: predictor-corrector + 동압 5-diagonal Poisson(SIP) 스텝당 2회 | surf-beat(파군평균) 기본 — 흐름은 explicit, nonh 켜면 projection 추가 | wave action 은 별도 방정식 | [[xbeach_flow_solver]]·[[xbeach_timestep_control]]·[[xbeach_nonh]] |

### 1.3 reduced-complexity 천수·VOF 모델

| 모델 | 스킴 | 핵심 anchor | 근거 |
|---|---|---|---|
| **SFINCS** | **explicit staggered local-inertial**: momentum(explicit, advection 은 직전값 q0/uv0) → **Bates(2010) semi-implicit 마찰 분모** → continuity | 마찰 갱신 sfincs_momentum.f90:677 | [[sfincs_flow_solver]] |
| **LISFLOOD-FP** | **솔버별 4계열**: ACC=Bates local-inertial(q-centred θ=1 semi-implicit 마찰, fp_acc.cpp:88) / diffusive=explicit Manning / Roe=1차 Godunov / **DG2·MWDG2=2단 SSP-RK2**(dg2_update.cu:681 stage1→:326-334 평균) | GPU adaptive 는 RK 단간 MRA 재인코딩(cuda_adaptive_simulate.cu:710-725) | [[lisflood-fp-classic-acc-flow]]·[[lisflood-fp-swe-fv1-dg2]]·[[lisflood-fp-mwdg2-adaptive-mra]] |
| **CADMAS-SURF/3D** | **SMAC projection + VOF**: Euler 예측자(VF_VEULER) → 압력 Poisson 7-diagonal 조립(vf_vpcoef.f:152-348) → **(M)ILU-BiCGSTAB**(vf_m1bcgs.f:178-227) → 속도·압력 보정(vf_vmodif.f:201,206) | outer 반복 `DO 600 ILOOP=1,LOOPS`(vf_a1main.f:1058) | [[cadmas-surf3d-smac-velocity-pressure-solver]]·[[cadmas-surf3d-architecture-source-map]] |

## 2. 계보 — 네 흐름

1. **split-explicit 해양모델(ROMS 단독)**: 빠른 barotropic 을 **작은 dtfast explicit substep + 시간필터**로 처리. NDTFAST 가 핵심 knob — 나머지 전부 implicit/semi-implicit 로 격리하는 다른 모델과 정반대 설계. leapfrog computational mode 는 LF-AM3 weight 자체가 억제(Asselin 필터 불사용).
2. **semi-implicit 중력파 격리(EFDC·ADCIRC·Delft3D-FLOW·FM·SWASH-Imp)**: 자유표면/연속을 행렬로 풀어 표면중력파 CFL 제거. 행렬 형태가 갈림 — EFDC CALPUV PCG / ADCIRC GWCE JCG(consistent) 또는 lumped / Delft3D ADI double-sweep(방향분리로 tridiagonal 화) / FM Guus SPD+Nested Newton / SWASH SIP·BiCGSTAB. leapfrog mode 제어도 갈림: EFDC=주기적 trapezoidal corrector(NTSTBC), ADCIRC=GWCE wave-continuity 정식화 자체.
3. **explicit CFL-adaptive 천수(SFINCS·LISFLOOD·XBeach)**: 행렬 없음 — 매 스텝 CFL 로 dt 재산정(§3), 마찰만 semi-implicit(Bates 분모, [[bottom-friction-cross-model]] §3). 유일한 무조건 안정 성분이 마찰이라는 점이 특징.
4. **고차 multistep/multistage 위상해상(FUNWAVE·Celeris·LISFLOOD DG2)**: 파형 위상 전파의 시간 정확도가 목적 — FUNWAVE SSP-RK3(3단×flux 재계산, TVD 안정성 보존), Celeris AB3-AM4(1회 flux + history 재활용 = GPU 효율 지향), LISFLOOD DG2 SSP-RK2(공간 2차와 짝). multistep(Celeris)은 시작 3스텝 부트스트랩·불연속 취약, multistage(FUNWAVE)는 스텝당 3배 비용이 트레이드오프.

## 3. dt 전략 대조

| 모델 | dt | CFL 식·계수 (anchor) |
|---|---|---|
| ROMS | 고정 dt + `dtfast=dt/NDTFAST` | 실무식 `NDTFAST=ceil(dt·√(g·Hmax)/(0.4·dx_min))`, Courant 진단 diag.F:243-258 |
| EFDC | 3TL 고정 / 2TL dynamic(DTDYN) | external semi-implicit 로 중력파 CFL 완화 |
| ADCIRC·Delft3D·FM | 고정 dt | semi-implicit/ADI 무조건 안정 (advection explicit 성분의 정량 CFL 은 §5 미커버) |
| SWASH | **mtimei=2 고정** / mtimei=1 만 적응 | explicit 경로: `cflmax>pnums(3)`→dt 반감, `<pnums(2)`+20스텝 안정→배증(SwashMain.ftn90:275-297). CFL 식 3변종(1DH `(dt/dx)(√gh+|u|)` 등) |
| FUNWAVE | **매 스텝 적응** | `DT=CFL·min(DX/|U+c|,DY/|V+c|)`+MPI_ALLREDUCE(misc.F:216) |
| Celeris | **정적**(초기 1회) | `dt=Courant·min(dx,dy)/√(g·base_depth)`, Courant 0.15(P-C ~0.25) — per-step 재산정 아님(§5) |
| XBeach | 매 스텝 적응 | `dt=CFL·min(dsu,dnv)/√(g·max h)`(timestep.F90:416), CFL≈0.7, output-time snapping |
| SFINCS | 매 스텝 적응 | wet점별 후보 min-reduce → `dt=alfa·min_dt`, **alfa 기본 0.50**(sfincs_input.f90:70 직접 재확인), `dt<dtmin` 시 중단 |
| LISFLOOD-FP | 매 스텝 적응(솔버별 식 상이) | ACC `cfl·dx/√(gH)`(유속항 없음, fp_acc.cpp:271, cfl=0.7) / Roe·FV1·DG2 `cfl·dx/(|u|+√gH)` / GPU **CFL 하드코딩 HWFV1=0.5·MWDG2=0.3**(SolverParams.h 직접 재확인), 첫 Δt=0.001s 하드코딩 |
| CADMAS | 적응(IDTTYP≠0) 또는 고정 | VF_CDTCAL = **이류 CFL(porous Courant)+확산한계만 — 표면파 celerity √(gH) 항 없음**([[cadmas-surf3d-timestep-nesting-stoc-coupling]] disclosed) |

## 4. implicit 성분 대조 — "무엇이 행렬로 풀리는가"

| implicit 대상 | 모델 (형태) |
|---|---|
| **자유표면/연속** | EFDC(PCG)·ADCIRC(JCG/lumped)·Delft3D(ADI sweep)·FM(Guus+Newton)·SWASH-Imp(θ) |
| **비정수압/동압 Poisson** | SWASH(SIP/BiCGSTAB, 2차 pressure correction)·XBeach-nonh(5-diag SIP, 스텝당 2회)·CADMAS(7-diag MILU-BiCGSTAB)·SFINCS-nonh(별도 모듈) |
| **Boussinesq 분산 tridiagonal** | FUNWAVE(매 RK 서브단계, Thomas/cuSPARSE)·Celeris(PCR; Bous 는 계수 재활용, COULWAVE 는 매 스텝) |
| **연직 확산/이류** | ROMS(Crank-Nicholson 확산 + implicit 연직 advection, **별개 tridiagonal 2회** step3d_t.F:1556-1655,1730-1764)·Delft3D UZD·EFDC(운동량=**전단 완전 implicit**+Sherman-Morrison [[efdc_internal_shear_caluvw]]·난류 MY2.5 QQ/QQL tridiag)·SWASH(연직 eddy viscosity 포함 무조건 안정)·ADCIRC 3D(θ=Alp3 연직확산+Alp1 Coriolis+Alp2 저면응력 — 복소 tridiag, **연직이류는 explicit**, [[adcirc-3d-vssol-vertical-scheme]]) |
| **마찰** | SFINCS·LISFLOOD ACC(Bates 분모)·SWASH-Imp(Euler implicit)·ADCIRC(2×2 행렬)·LISFLOOD FV1/DG2(Jacobian) — 상세 [[bottom-friction-cross-model]] §3 |

## 5. ★함정·미커버 (disclosed gaps)

- **★ADCIRC 노트 오염 적발·정정(2026-07-10)**: [[adcirc-timestep-orchestration]] §5 가 EFDC 파라미터(IS2TIM/ISTL/DTDYN/ISDYNSTP)를 ADCIRC 에 혼용 서술했었음 — ADCIRC src 전역 rg 0건으로 확정, A00/B00/C00·CPRECOR·ILump 기반으로 §5 재작성 완료. cross-model 작업이 모델 간 서술 누출을 잡은 사례.
- **Celeris 시간적분 위치**: AB3/AM4 분기는 shader 측(`Pass3_Bous.wgsl:398-409` 직접 재확인, [[celeris-source-map]] `:400-409` 인용과 일치; Pass3_NLSW·SedTrans_Pass3* 에 동형 반복) — JS 측 `main.js` 는 uniform(`timeScheme`·`pred_or_corrector`) 세팅만. 검색 시 JS 만 뒤지면 못 찾는 함정.
- **Celeris dt 정적**: 실행 중 dt 재산정 로직이 노트·코드 스코핑에서 확인 안 됨 — `base_depth` 특성수심 기반 초기 추정뿐. 얕은 국소 수심에서 CFL 위반 가능성은 미검증 `[source-needed]`.
- **θ 기본값 미커버**: SWASH `theta/theta3`(pnums) 기본값·FM θ 수치값·Delft3D ADI advection explicit 성분의 정량 CFL — 전부 해당 노트 disclosed TODO.
- **ROMS `nfast≠NDTFAST` 함정**: 필터 support 가 NDTFAST 를 초과 — substep 수를 NDTFAST 로 가정한 후처리/디버깅 오류 주의([[roms_barotropic_2d]]).
- **EFDC NTSTBC 과대 함정**: corrector 주기 >100 시 leapfrog computational mode 성장(checkerboard HP) — [[efdc_hydro_core]] Working Rules.
- ~~**ADCIRC 3D 연직 시간적분**: VSSOL 내부의 implicit θ/tridiagonal 여부 미커버~~ — **해소(2026-07-11)**: [[adcirc-3d-vssol-vertical-scheme]] 신설 — 2TL θ³-가중(Alp1 Coriolis·Alp2 저면응력·Alp3 연직확산, fort.15 독립 3-knob)·복소 q=u+iv tridiagonal(node 별 NFEN 계)·연직 linear FE consistent mass·이류는 전부 explicit·w 는 연속식 적분+adjoint 보정(Wf=0 하드코딩).
- **CADMAS celerity 부재**: VF_CDTCAL 에 √(gH) 항 없음 — 자유수면 안정성은 VOF 이류 CFL 이 사실상 지배. "celerity 안정항" 주장 금지(원노트 명시).
- ~~**EFDC 내부모드 운동량 연직확산의 시간처리**: 전용 노트 미커버~~ — **해소(2026-07-11)**: [[efdc_internal_shear_caluvw]] 신설 — 미지수가 속도 아닌 **층간 전단 DU/DV**, 연직확산 **완전 implicit**(θ knob 없음, CMU=1+CDZMU·DELTI·HU·AVUI)·Thomas 소거+**Sherman-Morrison rank-one**(저면항력↔깊이적분 결합)·★바람 전단 주입 ISTL==2 게이트(3TL full step 미주입).
