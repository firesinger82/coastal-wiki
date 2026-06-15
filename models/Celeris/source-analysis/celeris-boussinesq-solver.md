---
title: "Celeris-WebGPU Boussinesq 분산 solver — Pass3_Bous + PCR tridiagonal 음해"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/{Pass3_Bous,Pass3_NLSW,Update_TriDiag_coef,TriDiag_PCRx,TriDiag_PCRy}.wgsl + js/Run_Tridiag_Solver.js 직접 read. 라인·수식 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 상위: [../README.md](../README.md) · 파이프라인 전체: [celeris-pipeline-graph.md](celeris-pipeline-graph.md) · FV 재구성/플럭스: [celeris-fv-reconstruction.md](celeris-fv-reconstruction.md) · COULWAVE 변형: [celeris-coulwave.md](celeris-coulwave.md)
> FUNWAVE 대응(같은 물리 클래스, 다른 solver 구현): [../../FUNWAVE/source-analysis/funwave-dispersion-solver.md](../../FUNWAVE/source-analysis/funwave-dispersion-solver.md)

## 0. 위치

phase-resolving Boussinesq를 NLSW와 구분짓는 **음해(implicit) 분산 solver**가 이 노트의 대상. Celeris 한 timestep의 코어:

```
Pass1 (flux)  →  Pass2 (explicit)  →  Pass3_Bous (source+AB 적분, 명시 RHS 생성)
              →  Update_TriDiag_coef (계수 텍스처)  →  TriDiag_PCRx/y (PCR 음해)
```

FUNWAVE의 tridiagonal solve(Thomas/cusparse)에 정확히 대응하는 GPU 텍스처 기반 **Parallel Cyclic Reduction(PCR)** 구현이다. NLSW(`NLSW_or_Bous == 0`)는 이 음해를 **우회**하고 직접 복사한다.

---

## 1. Pass3가 조립하는 것 (`Pass3_Bous.wgsl`)

Pass3는 운동량/연속 방정식의 RHS를 한 셀에서 조립하고 Adams-Bashforth로 시간 적분한다. 구성요소:

**(a) 플럭스 발산** — Pass1/Pass2가 만든 셀면 플럭스 텍스처(`txXFlux`/`txYFlux`)의 차분:
```wgsl
let d_by_dt = (xflux_west - xflux_here) * globals.one_over_dx
            + (yflux_south - yflux_here) * globals.one_over_dy
            + source_term + vorticity_dissipation;
```
`shaders/Pass3_Bous.wgsl:394`.

**(b) source_term 벡터** — `Pass3_Bous.wgsl:392`:
```wgsl
let source_term = vec4<f32>(
  dhdt + overflow_dry,
  -globals.g * h_here * detadx - in_state_here.y * friction_ + breaking_x + (Psi1x + Psi2x) + press_x,
  -globals.g * h_here * detady - in_state_here.z * friction_ + breaking_y + (Psi1y + Psi2y) + press_y,
  hc_by_dx_dx + hc_by_dy_dy + 2.0 * hc_by_dx_dy + c_dissipation);
```
4성분 = [질량(dhdt/침투), x운동량, y운동량, scalar transport]. x운동량 항만 보면:
- `-g·h·detadx` : eta 경사 압력 구동 (`detadx`는 분산 켜질 때 4차 차분, `:241`)
- `-Hu·friction_` : 바닥 마찰 (`FrictionCalc`, `:67-93`; Manning 옵션 `:82-83`)
- `breaking_x` : 파괴 와점성 유발 운동량 확산 (`:361`, `useBreakingModel`일 때 `txDissipationFlux` 차분)
- `(Psi1x + Psi2x)` : **Boussinesq 분산 source** (§2)
- `press_x` : 외부 압력 경사 `-0.5·h·(g/dx)·(P_right-P_left)` (`:314`)

**(c) 시간 적분** — `:399-410` (§4).

**(d) vorticity 혼합** — `vort_friction_factor>0`일 때 와도 경사 기반 운동량 확산 (`:290-300`), source와 분리해 더함.

압력/마찰/breaking/scalar 항은 NLSW와 공유. **분산 source(Psi)와 breaking_x/y, F_star/G_star만 Bous 고유**다.

---

## 2. Bous가 NLSW에 추가하는 분산 항 (Pass3_Bous vs Pass3_NLSW)

`Pass3_NLSW.wgsl`의 source_term(`:248`)은 운동량에 `-g·h·detad* - HU·friction_ + press_*`만 갖는다. breaking·Psi가 **없다**. Bous가 추가하는 것:

### 2.1 F_star / G_star — 분산 보정량 (시간미분용 helper)

`near_dry > 0`이고 주기경계 가드가 아닐 때만 계산(`:192`). depth `d_here = -B_here`, 4차 차분 스텐실 사용. `Pass3_Bous.wgsl:269-279`:
```wgsl
F_star = (1.0/6.0)*d_here*(dd_by_dx*(0.5*one_over_dy)*(v_up-v_down)
        + dd_by_dy*(0.5*one_over_dx)*(v_right-v_left))
        + (Bcoef + 1.0/3.0)*d2_here*(one_over_dxdy*0.25)
          *(v_up_right - v_down_right - v_up_left + v_down_left);
G_star = (1.0/6.0)*d_here*(dd_by_dx*(0.5*one_over_dy)*(u_up-u_down)
        + dd_by_dy*(0.5*one_over_dx)*(u_right-u_left))
        + (Bcoef + 1.0/3.0)*d2_here*(one_over_dxdy*0.25)
          *(u_up_right - u_down_right - u_up_left + u_down_left);
```
교차 운동량의 혼합 2차 미분 구조 (`∂(d·∂v)/∂x∂y` 형태). `Bcoef`는 Boussinesq 분산 보정 계수(Nwogu류 α 관련). `F_star`/`G_star`는 `F_G_star` 텍스처로 출력(`:397, 428`)되어 다음 step에서 `F_G_star_oldOldGradients`로 시간미분에 쓰인다.

### 2.2 Psi1 / Psi2 — 운동량에 더해지는 명시 분산 source

`:282-286`:
```wgsl
Psi1x = Bcoef_g * d3_here * ((eta_right_right - 2*eta_right + 2*eta_left - eta_left_left)*(0.5*one_over_d3x)
      + (eta_up_right - eta_up_left - 2*eta_right + 2*eta_left + eta_down_right - eta_down_left)*(0.5*one_over_dx*one_over_d2y));
Psi2x = Bcoef_g * d2_here * (dd_by_dx*(2*eta_by_dx_dx + eta_by_dy_dy) + dd_by_dy*eta_by_dx_dy)
      + (F_star - F_G_star_oldOldies.y) / globals.dt * 0.5;
```
(y는 대칭, `:285-286`).
- `Psi1x` = `Bcoef_g · d³ · (η의 3차 분산 미분)` — depth³ 곱한 자유표면 분산항.
- `Psi2x` = `Bcoef_g · d² · (depth 경사 × η 2차미분)` + **`(F_star - F_G_star_oldOldies.y)/dt · 0.5`** — F_star의 시간미분(현재−oldOld)/dt 항. 즉 분산 보정의 시간변화율이 운동량 RHS로 들어간다.

이 Psi 항이 source_term의 운동량 성분에 더해져(`:392`) **명시(explicit) RHS**를 만든다. 이 RHS가 `current_stateUVstar`로 출력(`:429`)되고, 이것이 **음해 tridiagonal solve의 우변 b**가 된다.

### 2.3 핵심 출력 (음해와의 인터페이스)

`Pass3_Bous.wgsl:426-429`:
```wgsl
textureStore(txNewState, idx, newState);            // AB 적분 결과 (분산 미보정)
textureStore(dU_by_dt, idx, d_by_dt);               // history
textureStore(F_G_star, idx, F_G_here);              // 분산 helper history
textureStore(current_stateUVstar, idx, newState);   // ★ 음해 RHS (U*, V*)
```
`current_stateUVstar`의 `.g`(=U*)·`.b`(=V*)가 PCR의 우변이다. NLSW에서는 `F_G_star`에 `(0,0,0,1)`을 쓰고(`Pass3_NLSW.wgsl:280, 284`) 분산 정보가 없다.

---

## 3. 음해 solve — Update_TriDiag_coef + PCR

분산 Boussinesq의 운동량 방정식은 `(I + L)·U = U*` 꼴의 tridiagonal 시스템 (L = 분산 연산자). 방향분리(ADI류): x행마다 한 tridiagonal, y열마다 한 tridiagonal.

### 3.1 계수 텍스처 빌드 (`Update_TriDiag_coef.wgsl`)

각 셀에서 tridiagonal 3-대각 `(a,b,c)`를 계산해 `coefMatx`(x방향), `coefMaty`(y방향)에 저장. 표준 Boussinesq(`NLSW_or_Bous != 2`) x계수, `Update_TriDiag_coef.wgsl:67-69`:
```wgsl
a =  d_here*d_dx/(6.0*dx) - (Bcoef + 1.0/3.0)*d_here*d_here/(dx*dx);
b = 1.0 + 2.0*(Bcoef + 1.0/3.0)*d_here*d_here/(dx*dx);
c = -d_here*d_dx/(6.0*dx) - (Bcoef + 1.0/3.0)*d_here*d_here/(dx*dx);
```
대각 `b = 1 + 2(Bcoef+1/3)d²/dx²`(대각우세), 비대각은 depth² 분산 강도. `d_dx`는 depth 1차미분(`:64`). 경계행(`idx.x<=2 || idx.x>=width-3`)과 `near_dry<0` 셀은 `a=0,b=1,c=0` → **항등행**(`:42-46`)이라 solve가 그 셀을 통과시킨다(분산 미적용). `coefMat*`의 채널: `.r=a, .g=b, .b=c, .a` (PCR이 RHS·해를 쓰는 자리). COULWAVE(`==2`) 변형은 `:52-61`의 다른 계수식 — [celeris-coulwave.md](celeris-coulwave.md) 참조.

### 3.2 왜 PCR인가 (Thomas가 아니라)

Thomas 알고리즘은 forward sweep → back substitution이 **본질적으로 순차적**(셀 i가 i-1에 의존). GPU에서 한 행에 수천 셀이 있어도 직렬화돼 병렬성을 못 살린다. **Parallel Cyclic Reduction(PCR)**은 매 패스마다 모든 미지수를 stride `s`만큼 떨어진 이웃 2개와 결합해 동시에 줄인다. `log2(N)` 패스로 시스템을 항등(대각만 남김)으로 환원 → 각 셀이 독립적으로 해를 읽는다. WGSL compute(셀=스레드) 모델에 자연스럽다.

JS가 패스 수를 `Px = ceil(log2(WIDTH))`, `Py = ceil(log2(HEIGHT))`로 계산(`js/constants_load_calc.js:427-428`). 우라일 `Px`는 PCR uniform `P`로 byte offset 16에 기록(`main.js:1034`).

### 3.3 PCR 한 패스 (`TriDiag_PCRx.wgsl`)

stride 이웃을 **modulo wrap**으로 잡는다(`:38-39`):
```wgsl
let idx_left  = vec2<i32>((idx.x - s + width) % width, idx.y);
let idx_right = vec2<i32>((idx.x + s + width) % width, idx.y);
```
패스 0(`p==0`)은 대각으로 정규화하고 RHS를 `current_stateUVstar.g`(U*)에서 로드(`:56-72`). 이후 패스는 직전 패스가 쓴 reduced 계수·RHS를 읽는다(`:74-87`, `.a` 채널이 RHS).

PCR 환원 코어 (`:89-92`):
```wgsl
let r = 1.0 / (1.0 - aIn*cInLeft - cIn*aInRight);
let aOut = -r * aIn * aInLeft;
let cOut = -r * cIn * cInRight;
let dOut =  r * (dIn - aIn*dInLeft - cIn*dInRight);
```
표준 CR 환원식: 현재행에서 좌·우 stride 이웃 행을 소거해 stride를 2배(`s = 1<<p`, `Run_Tridiag_Solver.js:50`)로 넓힌 새 3-대각을 만든다. 출력 `txtemp_out = (aOut, 1.0, cOut, dOut)`(`:94`) — 대각은 항상 1로 정규화. **마지막 패스(`p == P-1`)에서만** 해 `dOut`을 상태 텍스처 채널에 써넣는다(`:101-105`):
```wgsl
if (globals.p == globals.P - 1) {
    let CurrentState = textureLoad(current_state, idx, 0);
    let txtemp2_out = vec4<f32>(CurrentState.r, dOut, CurrentState.b, CurrentState.a);
    textureStore(txtemp2, idx, txtemp2_out);  // .g = 해 U
}
```
`TriDiag_PCRy.wgsl`은 동일 구조이되 이웃을 y축으로 wrap(`:38-39`)하고 RHS를 `current_stateUVstar.b`(V*)에서 로드, 해를 `.b` 채널에 쓴다(`:101-105`).

> 불확실: 이 환원식은 대각정규화 후 표준 PCR이지만, `(1 - aIn·cInLeft - cIn·aInRight)` 형태는 일부 구현이 쓰는 부호 규약이다. 소스가 보여주는 그대로 전사했고 수학적 유도는 코드 밖이다.

### 3.4 JS 오케스트레이션 (`Run_Tridiag_Solver.js`)

`:37-39` — **NLSW 우회**:
```js
if (calc_constants.NLSW_or_Bous == 0) {
    runCopyTextures(device, calc_constants, current_stateUVstar, txNewState)
}
```
즉 NLSW는 U* = U로 직접 복사, PCR 전혀 안 돈다.

Bous면 X-solve 루프(`:48-63`): `for p in 0..Px`, `s = 1<<p`, uniform에 `p`·`s` 기록, 패스마다 **ping-pong 바인드그룹** 선택(`:57`):
```js
const TridiagX_BindGroup_Current =
  (p == 0) ? TridiagX_BindGroup_BaseToA
           : ((p % 2 == 1) ? TridiagX_BindGroup : TridiagX_BindGroup_BToA);
```
- `p==0`: base 계수(`coefMatx`)를 직접 읽어 A로(`BaseToA`).
- 이후 홀/짝 패스가 `newcoef_x`↔`txtemp_PCRx`를 번갈아 읽기/쓰기(copy-free 핸드오프; 예전 `runCopyTextures` 호출은 주석처리됨 `:47,62`).

루프 후 `runCopyTextures(txtemp2_PCRx, txNewState)`(`:66`)로 풀린 U를 새 상태에 반영. Y-solve가 동일하게 이어진다(`:73-91`). x·y 순차 — 방향분리.

`Handler_UpdateTrid.js`는 coefMatx/coefMaty 쓰기 바인드그룹을, `Handler_Tridiag.js`는 PCR 바인드그룹(`coefMat`, `current_state`, `current_stateUVstar`, `txtemp`, `txtemp2`)을 만든다(읽기 텍스처는 `unfilterable-float rgba32float`, 쓰기는 `write-only` storage).

---

## 4. 시간 적분 — Adams-Bashforth predictor/corrector

`Pass3_Bous.wgsl:399-410` (NLSW와 동일 코드, `Pass3_NLSW.wgsl:257-266`):
```wgsl
if (timeScheme == 0) {                       // Euler
    newState = in_state_here_UV + dt * d_by_dt;
} else if (pred_or_corrector == 1) {          // AB predictor (3차)
    newState = in_state_here_UV + dt/12.0 * (23.0*d_by_dt - 16.0*oldies + 5.0*oldOldies);
} else if (pred_or_corrector == 2) {          // AM corrector (4차)
    let predicted = textureLoad(predictedGradients, idx, 0);
    newState = in_state_here_UV + dt/24.0 * (9.0*d_by_dt + 19.0*predicted - 5.0*oldies + oldOldies);
}
```
- `pred_or_corrector==1`: 3차 Adams-Bashforth predictor — 계수 (23, −16, 5)/12. `oldies`=직전 step `dU/dt`(`oldGradients`), `oldOldies`=그 전(`oldOldGradients`).
- `pred_or_corrector==2`: 4차 Adams-Moulton corrector — (9, 19, −5, 1)/24, `predictedGradients`(predictor의 `dU/dt`) 사용.
- 적분 기준은 `in_state_here_UV = txstateUVstar`(이전 step의 분산보정 상태), 결과를 `current_stateUVstar`로 내보내 §3 음해의 RHS가 된다.

**파이프라인 결합**: predictor 단계 → coef build → PCR(x,y) → boundary → (옵션) corrector 단계 → 다시 PCR. F_G_star history(`F_G_star_oldGradients`/`oldOldGradients`)와 gradient history는 매 step rotate된다. 전체 패스 순서·텍스처 rotation은 [celeris-pipeline-graph.md](celeris-pipeline-graph.md) 참조.

---

## 5. FUNWAVE 대조

같은 물리 클래스(phase-resolving Boussinesq), 같은 수치 골격(명시 source + tridiagonal 분산 음해 + 고차 AB/AM 시간적분)이지만 **음해 solver 구현이 다르다**:

| | Celeris-WebGPU | FUNWAVE-TVD |
|---|---|---|
| 분산 음해 | **PCR**, `log2(N)` 패스, GPU 텍스처, modulo-wrap stride | Thomas(직렬) 또는 cusparse(CUDA 빌드) |
| 데이터 구조 | rgba32float 텍스처(`coefMat*`, `txtemp*`) | Fortran 배열, 방향별 tridiag |
| 병렬성 | 셀=스레드, 패스 내 완전 병렬 | MPI 도메인 분할 + 행/열 내 직렬 sweep |
| 방향 처리 | x-solve → y-solve 순차(`Run_Tridiag_Solver.js`) | 마찬가지 방향분리 |
| 계수 부호 | `b = 1+2(Bcoef+1/3)d²/dx²` (`Update_TriDiag_coef.wgsl:68`) | `dispersion.F`/`tridiagnal.F`의 (1/3-B) 계수족 |
| NLSW 격하 | `NLSW_or_Bous==0`→직접 복사(우회) | DISPERSION 플래그로 분산항 off |

PCR은 Thomas보다 연산량은 많지만(O(N log N) vs O(N)) GPU 병렬도 덕에 wall-clock이 짧다 — 실시간 브라우저 시뮬을 가능케 한 핵심 선택. FUNWAVE 측 상세: [../../FUNWAVE/source-analysis/funwave-dispersion-solver.md](../../FUNWAVE/source-analysis/funwave-dispersion-solver.md).

---

## 6. 한 줄 요약 체인

`Pass3_Bous`(명시 RHS = flux발산 + 압력/마찰/breaking/**Psi 분산** + AB적분) → `current_stateUVstar`(U*,V*) → `Update_TriDiag_coef`(coefMatx/y) → `TriDiag_PCRx`(log2 W 패스) → `TriDiag_PCRy`(log2 H 패스) → `txNewState`(분산보정 U,V). NLSW는 이 음해 전체를 직접 복사로 우회.
