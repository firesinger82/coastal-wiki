---
title: "ROMS Tangent Linear Model (TLM) — tl_* perturbation 전파 커널"
model: ROMS
component: ROMS/Tangent
canonical_source: self
citation_status: verified
verification_method: "ROMS 소스 직접 read (roms/ROMS/Tangent/). tl_main3d.F·tl_main2d.F·tl_step3d_t.F·tl_pre_step3d.F·tl_step2d.F·tl_omega.F·tl_rho_eos.F·tl_initial.F·tl_get_data.F·tl_prsgrd.F 의 헤더 주석·CALL 시퀀스·선형화 라인을 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/ROMS/source-analysis/roms_main_driver_dispatch.md
  - models/ROMS/source-analysis/roms_baroclinic_3d.md
  - models/ROMS/source-analysis/roms_adjoint_framework.md
  - models/ROMS/source-analysis/roms_4dvar.md
  - models/ROMS/README.md
---

# ROMS Tangent Linear Model (TLM) — tl_* perturbation 전파 커널

> 비선형(NLM) 원시방정식을 BASIC STATE 주위에서 선형화한 접선선형 모델. perturbation $\delta\mathbf{x}$ 를 forward 전파하며, 4D-Var incremental minimization 의 핵심 엔진. (경로: `roms/ROMS/Tangent/`)

## 1. 개요 — TLM 이란

ROMS 4D-Var 데이터동화는 비선형 trajectory(BASIC STATE) 주위의 perturbation 동역학을 다룬다. 비선형 모델 $\mathbf{x}_{n+1}=\mathcal{M}(\mathbf{x}_n)$ 에 대해, perturbation 은 야코비안으로 전파된다:

$$\delta\mathbf{x}_{n+1} = \mathbf{M}\,\delta\mathbf{x}_n, \qquad \mathbf{M} = \frac{\partial\mathcal{M}}{\partial\mathbf{x}}\Big|_{\text{BASIC STATE}}$$

`Tangent/` 의 `tl_*` 루틴은 NLM 코드([[roms_baroclinic_3d]]의 `main3d.F` 등)의 **줄단위 선형화 버전**으로, 동일한 CALL 시퀀스를 유지하되 각 비선형 연산을 그 directional derivative 로 치환한다. `Tangent/` 디렉토리는 54개 `.F`/`.h` 파일로, NLM 의 거의 모든 커널에 1:1 대응한다.

ROMS 모델 ID `iTLM` 으로 식별된다 (`tl_main3d.F` 전반에서 `iTLM` 인자 사용, 예 `tl_main3d.F:179` `CALL ntimesteps (iTLM, ...)`).

## 2. 진입과 컴파일 가드

전체 디렉토리가 `TANGENT` CPP 매크로로 가드된다:

- `tl_main3d.F:2` — `#if defined TANGENT && defined SOLVE3D` (3D baroclinic TLM)
- `tl_main2d.F:2` — `#if defined TANGENT && !defined SOLVE3D` (2D barotropic-only TLM)
- `tl_step3d_t.F:5` — `#if !defined TS_FIXED && (defined TANGENT && defined SOLVE3D)` (tracer step, `TS_FIXED` 시 비활성)

헤더 주석이 정체성을 명시:

- `tl_main3d.F:12-15`: `"This routine is the main driver for tangent linear ROMS when configurated as a full 3D baroclinic ocean model. It advances forward the tangent linear model equations for all nested grids ... by the specified time interval (seconds), RunInterval."`
- `tl_main2d.F:12-15`: `"... configurated as shallow water (barotropic) ocean model only."`

진입점은 [[roms_main_driver_dispatch]] 의 드라이버가 `tl_main3d`/`tl_main2d` 를 dispatch.

## 3. 3D TLM 시간적분 루프 (`tl_main3d.F`)

구조가 NLM `main3d.F` 와 동일: `KERNEL_LOOP → NEST_LAYER → STEP_LOOP` 3중 루프 (`tl_main3d.F:158`, `:170`, `:185`). 각 그리드·타일에 대해 `tl_*` 커널을 호출한다.

### 3.1 시간 인덱스 (NLM 과 동일 leapfrog)

`tl_main3d.F:191-193`:
```
nstp(ng)=1+MOD(iic(ng)-ntstart(ng),2)
nnew(ng)=3-nstp(ng)
nrhs(ng)=nstp(ng)
```

### 3.2 STEP_LOOP 내 CALL 시퀀스 (대표)

| 단계 | TL 루틴 | file:line | 역할 |
|---|---|---|---|
| 입력 데이터 | `tl_get_data` | `tl_main3d.F:210` | 강제력·기후값 + **BASIC STATE forward 읽기** |
| 데이터 처리 | `tl_set_data` | `tl_main3d.F:227` | 시간보간; `set_depth(iTLM)` BASIC STATE 깊이 `:230` |
| BASIC STATE 질량플럭스 | `set_massflux(iTLM)` | `tl_main3d.F:246` | `FORWARD_READ` 시 (`:237`) |
| weak-constraint 강제 | `tl_forcing` | `tl_main3d.F:275, :285` | `WEAK_CONSTRAINT`/`FORCING_SV` 시 adjoint 임펄스 주입 |
| 초기화 (첫 스텝) | `tl_post_initial` | `tl_main3d.F:305` | `iic==ntstart` 시 |
| 질량플럭스·밀도 | `tl_set_massflux`, `tl_rho_eos` | `tl_main3d.F:319, :321` | TL 질량플럭스/상태방정식 |
| 진단 | `tl_diag` | `tl_main3d.F:326` | TL 진단량 |
| BASIC STATE omega | `omega(iTLM)` | `tl_main3d.F:328` | `FORWARD_READ` 시 비선형 omega |
| 수직경계조건 | `tl_set_vbc` | `tl_main3d.F:390` | TL surface/bottom flux |
| 경계증분 조정 | `tl_obc_adjust` 등 | `tl_main3d.F:422-424` | `ADJUST_BOUNDARY` (4D-Var 제어변수) |
| 표면강제 조정 | `tl_frc_adjust` | `tl_main3d.F:442` | `ADJUST_STFLUX`/`ADJUST_WSTRESS` |
| TL 수직속도 | `tl_omega` | `tl_main3d.F:465` | S좌표 수직속도 |
| 자유표면 평균 | `tl_set_zeta` | `tl_main3d.F:480` | 시간평균 zeta |
| 출력 | `tl_output` | `tl_main3d.F:513` | TL NetCDF 출력 |
| 3D RHS | `tl_rhs3d` | `tl_main3d.F:554` | TL 우변항 |
| 2D 적분 (LOOP_2D) | `tl_step2d` | `tl_main3d.F:612, :659` | barotropic predictor/corrector |
| 깊이 재계산 | `tl_set_depth` | `tl_main3d.F:723` | 새 zeta 로 |
| 3D 모멘텀 step | `tl_step3d_uv` | `tl_main3d.F:749` | TL 모멘텀 |
| 수직혼합/source-sink | `tl_omega`, `tl_biology` | `tl_main3d.F:776, :783` | corrector |
| tracer step | `tl_step3d_t` | `tl_main3d.F:801` | `#ifndef TS_FIXED` (`:792`) |

이 순서가 [[roms_baroclinic_3d]] 의 NLM `main3d.F` CALL 시퀀스와 일치 — TLM 은 NLM 의 줄단위 거울.

### 3.3 barotropic split-explicit LOOP_2D

`tl_main3d.F:583` `LOOP_2D : DO my_iif=1,MAXVAL(nfast)+1`. NLM 과 동일하게 predictor (`PREDICTOR_2D_STEP=.TRUE.`, `:593`)/corrector (`:646`) 의 fast-time 2D 적분. `tl_step2d` 가 양쪽에서 호출 (`:612` predictor, `:659` corrector). `nfast+1` 보조 스텝은 fast-time 평균 마무리용으로 실제 적분 안 함 (주석 `tl_main3d.F:605-608`).

## 4. BASIC STATE 의존성 — TLM 의 핵심 개념

TLM 은 **비선형 trajectory(BASIC STATE) 위에서 선형화**되므로, 각 TL 커널은 NLM 변수(야코비안 평가점)를 입력으로 받는다.

- `tl_pre_step3d.F:29-32` 가 의존하는 BASIC STATE 를 명시 주석:
  `"BASIC STATE variables needed: AKt, AKv, Huon, Hvom, Hz, Tsrc, W, bustr, bvstr, ghats, srflx, sustr, svstr, t, z_r, z_w"`
- BASIC STATE 는 `FORWARD_READ` 시 디스크에서 읽음 (`tl_get_data.F:24, :33` `#ifdef FORWARD_READ`; `tl_main3d.F:237` `#if defined FORWARD_READ`). 읽은 후 비선형 `set_depth`/`set_massflux`/`omega` 로 보조량 재계산 (`tl_main3d.F:230, :246, :328`).
- `FORWARD_MIXING` 시 혼합계수도 forward 로 (`tl_get_data.F:59`).

`tl_rho_eos.F:355-356` 주석: `"Compute BASIC STATE and tangent linear density (kg/m3) at standard one atmosphere pressure."` — 한 루틴 안에서 BASIC STATE 값과 그 TL perturbation 을 함께 계산.

## 5. 선형화 패턴 — 줄단위 directional derivative

TL 코드의 본질은 각 비선형 연산 옆에 그 미분을 둔 것이다. 변수명 규약: BASIC STATE 변수 `x`, perturbation `tl_x`.

### 5.1 곱셈의 곱규칙 (`tl_omega.F`)

질량플럭스 발산 적분에서 (`tl_omega.F:176-179`, sediment 분기):
```
W(i,j,0)   =-cff1*(bed_thick(i,j,nstp)-bed_thick(i,j,nnew))*omn(i,j)
tl_W(i,j,0)=-cff1*(tl_bed_thick(i,j,nstp)-tl_bed_thick(i,j,nnew))*omn(i,j)
```
`omn`(상수 grid metric)은 계수로 그대로, perturbation 만 `tl_bed_thick` 로. 기본 분기는 $W(i,j,0)=0$, $\delta W(i,j,0)=0$ (`tl_omega.F:181-182`).

### 5.2 상태방정식 다항식의 미분 (`tl_rho_eos.F`)

다항식 계수 $C(0),C(1),C(2)$ 는 온도 $T_t$ 다항식. 그 TL 은 $T$-미분 계수 `dCdT` 와 $\delta T_t$ 의 곱:

`tl_rho_eos.F:369-371`:
```
tl_C(0)=tl_Tt*dCdT(0)
tl_C(1)=tl_Tt*dCdT(1)
tl_C(2)=tl_Tt*dCdT(2)
```
즉 $\delta C_k = \frac{\partial C_k}{\partial T_t}\,\delta T_t$. 밀도 `den1` 의 곱규칙 전개 (`tl_rho_eos.F:373-377`):
```
den1(i,k)   =C(0)+Ts*(C(1)+sqrtTs*C(2)+Ts*W00)
tl_den1(i,k)=tl_C(0)+
&            tl_Ts*(C(1)+sqrtTs*C(2)+Ts*W00)+
&            Ts*(tl_C(1)+tl_sqrtTs*C(2)+sqrtTs*tl_C(2)+tl_Ts*W00)
```
$\delta(\rho)=\delta C_0 + \delta T_s(\cdots) + T_s\,\delta(\cdots)$ — 정확히 $d(uv)=v\,du+u\,dv$.

### 5.3 비매끄러운 연산의 선형화 — SIGN 트릭

`MAX`/clamp 같은 비매끄러운 함수는 `SIGN` 으로 부분미분의 지시함수를 만든다. `tl_rho_eos.F:330` 온도 하한:
```
tl_Tt=(0.5_r8-SIGN(0.5_r8,-2.0_r8- ...))* ...
```
`(0.5-SIGN(0.5,arg))` = arg>0 일 때 1, 아니면 0 → clamp 의 (서브)미분. 제곱근의 TL 은 $\delta\sqrt{T_s}=\frac12 T_s^{-1/2}\delta T_s$, 음수면 0 (`tl_rho_eos.F:339-341`):
```
tl_sqrtTs=0.5_r8*tl_Ts/SQRT(Ts)   ! Ts>0
tl_sqrtTs=0.0_r8                   ! else
```

## 6. 2D barotropic step (`tl_step2d.F`, `tl_step2d_*.h`)

`tl_step2d.F` 는 얇은 wrapper — 알고리즘별 `.h` include:
- `tl_step2d.F:20` `#include "tl_step2d_LF_AM3.h"` (LF-AM3 시간적분; 디렉토리에 `tl_step2d_FB.h`, `tl_step2d_FB_LF_AM3.h`, `tl_step2d_LF_AM3.h` 세 변종 존재)
- 헤더 주석 `tl_step2d.F:11-12`: `"This subroutine performs a fast (predictor or corrector) time-step for the free-surface and 2D momentum tangent linear equations."`
- `SOLVE3D` 시 fast-time 필터링 주석 `tl_step2d.F:14-15`.

## 7. 압력경도 dispatch (`tl_prsgrd.F` + `.h`)

NLM 과 동일하게 CPP 로 스킴 선택 (`tl_prsgrd.F:16-25`):

| CPP | include | 비고 |
|---|---|---|
| `PJ_GRADP` | `tl_prsgrd40.h` | `:20-21` |
| `DJ_GRADPS` | `tl_prsgrd32.h` | `:22-23` (기본 spline) |
| (else) | `tl_prsgrd31.h` | `:24-25` |

헤더 주석 `tl_prsgrd.F:11-12`: `"This routine computes the tangent linear baroclinic hydrostatic pressure gradient term."` (`tl_rhs3d.F` 에서 호출, `tl_rhs3d.F:84` `"Compute baroclinic pressure gradient."`).

## 8. tracer / momentum step 세부

### 8.1 `tl_step3d_t.F` (tracer corrector)

헤더 `tl_step3d_t.F:14-18`: `"This routine time-steps tangent linear tracer equations. ... It applies the corrector time-step for horizontal and vertical advection, vertical diffusion, nudging if necessary, and lateral boundary conditions."`

- 입력 배열 의미 주석 `tl_step3d_t.F:27-35`: `t(:,:,:,nnew,:)` = 수평/수직 확산+source/sink (n+1), `t(:,:,:,3,:)` = 이류항+수직확산 predictor (n+1/2).
- **미지원 스킴** 명시 (TLM 한계): MPDATA 미지원 `tl_step3d_t.F:25` `"The MPDATA scheme is not supported in the TLM, RPM, and ADM."`; HSIMT 미구현 `tl_step3d_t.F:22-23` (`NghostPoints=3` 필요로 문제적).

### 8.2 `tl_step3d_uv.F` (momentum)

헤더 `tl_step3d_uv.F:12`: `"This routine time-steps the tangent linear horizontal momentum"`. RHS 시간적분 섹션 `:393`, `:872` (`"Time step right-hand-side terms."`).

### 8.3 `tl_pre_step3d.F`

헤더 `tl_pre_step3d.F:13-14`: `"initialize computations for new time step of the tangent linear 3D primitive variables."` Adams/Bashforth n-1·n-2 기여를 `nnew` 의 u,v 에 미리 합산 (`:16-19`), Crank-Nicholson 음해 수직점성을 미리 계산 (`:21-24`).

## 9. 초기화 (`tl_initial.F`)

헤더 `tl_initial.F:12`: `"This routine initializes all tangent linear model variables."`

- `FOUR_DVAR` 시 4D-Var 자료구조 USE (`tl_initial.F:21-29`).
- `ana_perturb(iTLM)` 로 해석적 perturbation 주입 (`tl_initial.F:538`).
- **TLM_CHECK** (TL 정확성 검증) 시 `tl_ini_perturb` 로 outer-loop 의 steepest-descent (adjoint gradient) 방향 perturbation (`tl_initial.F:542-552`): 주석 `"Perturb tangent linear state variable according to the outer loop iteration with the steepest descent direction of the gradient (adjoint state)."`
- 깊이/질량플럭스/밀도/omega 의 TL 초기 보조량: `tl_set_depth`, `tl_set_massflux`, `tl_rho_eos`, `tl_omega` USE (`tl_initial.F:86-90`).

`TLM_CHECK` 시 `tl_dotproduct` 로 내적 보존 검증 (`tl_main3d.F:331`, `tl_main2d.F:30`) — TL 코드와 NL 코드의 일관성 회귀 테스트.

## 10. 4D-Var 와의 연결 (고유 영역 경계)

TLM 은 incremental 4D-Var 의 forward perturbation 엔진:
- weak-constraint 강제 임펄스 주입 `tl_forcing` (`tl_main3d.F:275, :285`, `#if WEAK_CONSTRAINT || FORCING_SV`).
- 제어변수 조정: 경계 `tl_obc_adjust` (`ADJUST_BOUNDARY`), 표면강제 `tl_frc_adjust` (`ADJUST_STFLUX`/`ADJUST_WSTRESS`) (`tl_main3d.F:411-447`).
- minimization 루틴 `tl_rpcg_lanczos.F`, `tl_congrad.F`, convolution `tl_convolution.F`/`tl_conv_*.F` 가 디렉토리에 동거 (배경오차 공분산 적용·켤레경사 — 상세는 [[roms_4dvar]]).

수반(adjoint) 역방향 전파 $\mathbf{M}^T$ 는 [[roms_adjoint_framework]] (`Adjoint/ad_*`), representer 모델은 RPM 으로 별도. TLM 은 그 forward 짝.

## 11. 요약

| 측면 | 내용 | 대표 인용 |
|---|---|---|
| 정체성 | NLM 의 줄단위 선형화, perturbation forward 전파 | `tl_main3d.F:12-15` |
| 가드 | `TANGENT` (+`SOLVE3D`/`!SOLVE3D`) | `tl_main3d.F:2`, `tl_main2d.F:2` |
| 루프 | KERNEL/NEST_LAYER/STEP_LOOP + LOOP_2D, NLM 미러 | `tl_main3d.F:158,170,185,583` |
| BASIC STATE | 야코비안 평가점, `FORWARD_READ` 로 디스크 | `tl_pre_step3d.F:29-32`, `tl_main3d.F:237` |
| 선형화 패턴 | 곱규칙·다항식미분·SIGN 서브미분 | `tl_rho_eos.F:369-377`, `tl_omega.F:176-179` |
| 한계 | MPDATA/HSIMT 미지원 | `tl_step3d_t.F:22-25` |
| 4D-Var | forward perturbation 엔진, 제어변수 조정 | `tl_main3d.F:275,422,442` |
| 검증 | TLM_CHECK + tl_dotproduct | `tl_main3d.F:331`, `tl_initial.F:542-552` |

> ⚠ 본 노트는 driver/대표 커널 중심. 개별 `.h` 의 advection/mixing 줄단위 선형화 전수와 `tl_convolution`/`tl_rpcg_lanczos` 의 4D-Var 수학 세부는 source-needed (추후 [[roms_4dvar]] 와 연계 확장).
