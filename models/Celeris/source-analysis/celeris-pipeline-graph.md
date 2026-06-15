---
title: "Celeris-WebGPU 파이프라인 그래프 — 타임스텝 패스 순서·모드 분기·predictor-corrector"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/js/main.js + Handler_*.js + Run_*.js 직접 read, docs/architecture/SIMULATION_PIPELINE.md 대조. 라인 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> Canonical: [`../README.md`](../README.md) (모델 정체) · 소스 맵 [`celeris-source-map.md`](celeris-source-map.md).
> 본 노트 = **per-timestep 파이프라인 + 제어흐름 그래프**. 인용 경로는 `Celeris-WebGPU/` 루트 상대 (`js/main.js:NNN`).

Celeris-WebGPU는 단일 모놀리식 오케스트레이터 `js/main.js`(~6800 lines)가 WebGPU compute 패스를 고정 순서로 디스패치한다. JS는 스케줄링·텍스처 복사만, 수치 커널은 WGSL. 이 노트는 그 디스패치 시퀀스를 소스 라인 기준으로 재구성한다.

---

## 1. 프레임 루프 → 프레임당 타임스텝 (동적 조정)

`frame()`은 `requestAnimationFrame(frame)`로 재호출되는 클로저 (`js/main.js:1540`, 재귀 호출 `js/main.js:2933`). 프레임 내부에서 compute 루프는 `render_step`회 반복:

```
for (frame_c = 0; frame_c < render_step; frame_c++)   // js/main.js:1874
    { … 1 timestep (predictor [+corrector]) … }
```

- compute 루프는 `simPause < 0`일 때만 실행 (`js/main.js:1873`).
- **`render_step` 동적 조정** (`js/main.js:1565–1595`): `adapt_render_step==1 && setRenderStep==0`이면 1초마다 step당 clock time를 측정해 GPU가 빠르면 `render_step += 1`, 응답성이 나빠지면 `Math.max(1, render_step-1)`로 back-off (`:1578`,`:1583`). 즉 **렌더 1회당 시뮬 스텝 수**를 런타임에 조율 — 화면 갱신은 줄이고 GPU 점유를 최대화.
- 사용자가 render_step를 수동 설정하면(`setRenderStep`) 자동 탐색 비활성 (`js/main.js:4013`).
- `total_time = frame_count * dt` (`js/main.js:1881`) — `dt`는 고정 (Courant 기반, `constants_load_calc.js`에서 산출). 프레임 시작 시 `await device.queue.onSubmittedWorkDone()`로 큐 플러시 (`js/main.js:1546`).

---

## 2. 활성 수력 패스 순서 (predictor 1스텝)

아래는 `NLSW_or_Bous>0`(Boussinesq) + `useBreakingModel==1` 기준 실제 디스패치 순서. 각 라인은 `runComputeShader_EncStack`(`Run_Compute_Shader.js:55`, encoder에 적재) 또는 `runComputeShader`(`:3`, 즉시 submit). encoder는 중간중간 `device.queue.submit(...finish())`로 끊어 제출.

```text
[predictor — pred_or_corrector=1 (js/main.js:1927)]
 Pass0                       js/main.js:1893   이웃 수심 (dry/wet 헬퍼)
 Pass1 (or Pass1_HighOrder)  js/main.js:1896   face 재구성 (수심·유속·스칼라)
 SedTrans_Pass1   [if Sed]   js/main.js:1900   sed 농도 face 재구성
 Pass2 (or HighOrder_HLLC)   js/main.js:1904   face 수치 flux (HLLC/HLLEM)
 Pass_Breaking    [if brk]   js/main.js:1908   breaking age/intensity, eddy visc
   └ copy txtemp_Breaking→txBreaking            js/main.js:1909
 ── submit encoder stack ──  js/main.js:1913
 [COULWAVE only] Pass3A_COULWAVE, Pass3B_COULWAVE  js/main.js:1917–1918
   └ copy2DDataTo3DTexture ×6 → txCW_groupings    js/main.js:1919–1924
 Pass3_{Bous|NLSW}           js/main.js:1934 / :1937   flux divergence·friction·
                                              pressure·breaking·dispersion·predictor update
   └ copy dU_by_dt→predictedGradients           js/main.js:1940
 SedTrans_Pass3   [if Sed]   js/main.js:1944
 BoundaryPass                js/main.js:1949   BC + wet/dry cleanup (explicit state)
   └ copy txtemp_boundary→current_stateUVstar   js/main.js:1951
 [COULWAVE] Update_TriDiag_coef (UpdateTrid)    js/main.js:1959   비선형 계수 갱신
 ── submit encoder stack ──  js/main.js:1963
 runTridiagSolver:           js/main.js:1972    (NLSW: copy만, Bous: PCR)
   TriDiag_PCRx ×Px loop  →  Run_Tridiag_Solver.js:48–63
   TriDiag_PCRy ×Py loop  →  Run_Tridiag_Solver.js:73–88
 BoundaryPass (NewState)     js/main.js:1984   tridiag 후 eta,P,Q BC 재적용 (Bous만)
   └ copy txtemp_boundary→txNewState            js/main.js:1987
 [Bous] F_G_star history shift                  js/main.js:1990–1991
 [disturbanceType==5] AddDisturbance+Updateneardry+UpdateTrid  js/main.js:1996–2000
 ── submit encoder stack ──  js/main.js:2010
```

`Update_TriDiag_coef`(코드상 `UpdateTrid`)는 **Celeris-Bous(=1)에서는 predictor에서 매 스텝 재호출하지 않는다** — 초기화 시 1회, 그리고 깊이가 변할 때(disturbance·sediment)만 갱신 (`js/main.js:2000`,`:2141`). COULWAVE(=2)는 비선형 계수라 tridiag 직전 매 스텝 갱신 (`js/main.js:1959`,`:2089`).

타임스텝 말미 공통 후처리 (corrector 유무 무관, `js/main.js:2122–2178`):

```text
 [if Sed] SedTrans_UpdateBottom → txBottom 갱신, Updateneardry,
          [Bous=1] UpdateTrid (깊이 변화 반영)        js/main.js:2134–2142
 gradient history shift: oldGradients→oldOldGradients,
                         predictedGradients→oldGradients   js/main.js:2146–2147
 state swap: txNewState→txState,
             current_stateUVstar→txstateUVstar            js/main.js:2150–2151
 [if Sed] Sed history shift + state swap                  js/main.js:2155–2157
 ── 진단(diagnostics) ──
 Pass1 (cell-side 텍스처 재계산, 유속 출력용)              js/main.js:2163
 CalcMeans → txMeans/txMeans_Speed/txMeans_Momflux        js/main.js:2165–2170
 CalcWaveHeight → txWaveHeight                            js/main.js:2174–2175
 ── submit encoder stack ──                               js/main.js:2178
```

이후 프레임 단위(루프 밖): `Copytxf32_txf16`(f16 렌더 텍스처, `:2184`) → render pass(2D quad / 3D vertexgrid, `:2240`/`:2197`) → `ExtractTimeSeries`(툴팁·시계열, `:2652`).

---

## 3. 모드 분기 — `NLSW_or_Bous` (0/1/2) · `Accuracy_mode`

셰이더 **선택은 초기화 1회**(fetch+pipeline 생성), 디스패치 시점엔 미리 만든 파이프라인 변수를 분기 선택.

| config | 값 | 효과 | 인용 |
|---|---|---|---|
| `Accuracy_mode` | 1 | Pass1 → `Pass1_HighOrder.wgsl` (4th-order MUSCL-TVD), Pass2 → `Pass2_HighOrder_HLLC.wgsl` | `js/main.js:1322–1334` |
| | 0 | `Pass1.wgsl`, `Pass2.wgsl` (저차) | 동일 |
| `NLSW_or_Bous` | 0 | NLSW. Pass3 = `Pass3_Pipeline_NLSW`; **tridiag 생략**(copy만) | `js/main.js:1937`, `Run_Tridiag_Solver.js:37–39` |
| | 1 | Celeris Boussinesq. Pass3 = `Pass3_Bous.wgsl`, `Update_TriDiag_coef.wgsl`, `TriDiag_PCRx/y.wgsl` | `js/main.js:1340`,`:1357`,`:1368` |
| | 2 | COULWAVE. Pass3 = `Pass3_COULWAVE.wgsl`(+Pass3A/B), `Update_TriDiag_coef_COULWAVE.wgsl`, `TriDiag_PCRx/y_COULWAVE.wgsl` | `js/main.js:1345`,`:1354`,`:1366` |

디스패치 분기 패턴 (predictor·corrector 동일):
- Pass3: `if (NLSW_or_Bous > 0) Pass3_Pipeline_Bous else Pass3_Pipeline_NLSW` (`js/main.js:1933–1938`). `Pass3_Pipeline_Bous`는 셰이더 코드만 NLSW=1→Celeris / =2→COULWAVE로 미리 분기됨 (`js/main.js:1339–1346`, 동일 bind-group layout `Pass3_BindGroupLayout` 재사용 `:1399–1400`).
- COULWAVE 전용 grouping 패스(Pass3A/B + `copy2DDataTo3DTexture` ×6)는 `if (NLSW_or_Bous == 2)`로 가드 (`js/main.js:1916–1925`).
- PCR 솔버 진입 자체가 `NLSW_or_Bous==0`이면 copy로 단락 (`Run_Tridiag_Solver.js:37`).

> 즉 **mode = "어떤 .wgsl을 컴파일했나"(초기화 분기) + "어떤 Pipeline 변수를 디스패치하나"(루프 분기)** 이중 구조. 한 세션에서 mode 변경 = 셰이더 재fetch·재컴파일 필요.

---

## 4. `timeScheme==2` predictor/corrector + history 텍스처 시프트

`timeScheme` (Pass3 uniform `js/main.js:1634`): `0`=단일 explicit, `≠0`=Adams-Bashforth (current/old/older 도함수). `pred_or_corrector` (uniform `:1928`): `1`=predictor, `2`=corrector.

predictor는 항상 실행(§2). **corrector substep은 `if (timeScheme==2)`에서만** (`js/main.js:2012`). corrector는 predictor 결과를 시드로 동일 패스 시퀀스를 한 번 더:

```text
[corrector — js/main.js:2012, pred_or_corrector=2 (:2061)]
 copy txNewState→txState   (예측값을 gradient 기준으로)   js/main.js:2021
 Pass0, Pass1, [SedTrans_Pass1], Pass2, [Pass_Breaking]  js/main.js:2027–2044
 [COULWAVE] Pass3A/B + grouping copies                   js/main.js:2050–2058
 Pass3_{Bous|NLSW} (corrector update)                    js/main.js:2067 / :2070
 [SedTrans_Pass3]                                        js/main.js:2075
 BoundaryPass → current_stateUVstar                      js/main.js:2079–2081
 [COULWAVE] UpdateTrid                                   js/main.js:2089
 runTridiagSolver                                        js/main.js:2102
 BoundaryPass(NewState) → txNewState  [Bous]             js/main.js:2113–2116
```

corrector는 더 큰 dt(≈2배)와 정확도를 위해 계산량 2배를 추가 (`js/main.js:2012` 주석).

**history 텍스처 시프트** (3차 AB의 도함수 이력):

| 시프트 | 시점 | 인용 |
|---|---|---|
| `dU_by_dt → predictedGradients` | predictor Pass3 직후 | `js/main.js:1940` |
| `F_G_star_oldGradients → F_G_star_oldOldGradients`, `predictedF_G_star → F_G_star_oldGradients` | predictor·tridiag 후 (Bous 전용 dispersive 헬퍼) | `js/main.js:1990–1991` |
| `oldGradients → oldOldGradients`, `predictedGradients → oldGradients` | 타임스텝 말미 (corrector 후) | `js/main.js:2146–2147` |
| `txNewState → txState`, `current_stateUVstar → txstateUVstar` | 상태 스왑 (말미) | `js/main.js:2150–2151` |
| Sed: `oldGradients_Sed→oldOldGradients_Sed`, `predictedGradients_Sed→oldGradients_Sed`, `txNewState_Sed→txState_Sed` | 말미 (Sed 전용) | `js/main.js:2155–2157` |

즉 도함수 ring buffer를 GPU 텍스처 copy로 한 칸씩 밀어 다음 스텝의 `oldGradients`/`oldOldGradients`를 채운다 (별도 ALU 없이 `copyTextureToTexture`).

---

## 5. JS 핸들러 호출 그래프

Handler_*.js는 **루프에서 매번 호출되지 않는다**. 각 핸들러는 `create_<Pass>_BindGroupLayout` + `create_<Pass>_BindGroup`(텍스처/버퍼 바인딩)를 export, **초기화 시 1회** 호출되어 BindGroup·uniform 객체를 만든다 (예: `Handler_Pass3.js:create_Pass3_BindGroup(...)` 21개 텍스처 바인딩). 루프는 그 결과를 `Run_Compute_Shader.js`/`Run_Tridiag_Solver.js`로 디스패치할 뿐.

| 패스 | Handler (bind-group 정의) | 루프 디스패치 경유 | 가드 |
|---|---|---|---|
| Pass0 | `Handler_Pass0.js` | `runComputeShader_EncStack` :1893 | 항상 |
| Pass1 | `Handler_Pass1.js` | EncStack :1896,:2030,:2163 | 항상 (말미 1회는 진단) |
| Pass2 | `Handler_Pass2.js` | EncStack :1904 | 항상 |
| Pass_Breaking | `Handler_PassBreaking.js` | EncStack :1908 | `useBreakingModel==1` |
| Pass3 / Pass3A·B | `Handler_Pass3.js` | EncStack :1934/:1937; A·B는 즉시 `runComputeShader` :1917 | mode 분기 |
| BoundaryPass | `Handler_BoundaryPass.js` | EncStack :1949,:1984 | 항상 / Bous |
| UpdateTrid | `Handler_UpdateTrid.js` | EncStack :1959,:2000,:2141 | COULWAVE / 깊이변화 |
| TriDiag PCRx/y | `Handler_Tridiag.js` | **`Run_Tridiag_Solver.js`** (Px/Py 루프) :1972 | `NLSW_or_Bous>0` |
| Updateneardry | `Handler_Updateneardry.js` | EncStack :1998,:2137 | disturbance / Sed |
| AddDisturbance | `Handler_AddDisturbance.js` | EncStack :1996 | `disturbanceType==5` |
| SedTrans_Pass1/3/UpdateBottom | `Handler_SedTrans_*.js` | EncStack :1900,:1944,:2134 | `useSedTransModel==1` |
| CalcMeans | `Handler_CalcMeans.js` | EncStack :2165 | 항상 (진단) |
| CalcWaveHeight | `Handler_CalcWaveHeight.js` | EncStack :2174 | 항상 (진단) |
| Copytxf32_txf16 | `Handler_Copytxf32_txf16.js` | `runComputeShader` :2184 | 프레임당 1 |
| ExtractTimeSeries | `Handler_ExtractTimeSeries.js` | `runComputeShader` :2652 | 프레임당 1 |
| Render / Skybox / Model | `Handler_Render.js`,`Handler_Skybox.js` | RenderPass :2237+ | viewType 분기 |

**디스패치 실행 모델** (`Run_Compute_Shader.js`):
- `runComputeShader_EncStack(:55)` = 공유 `commandEncoder`에 compute pass 적재(submit 안 함) → main.js가 `device.queue.submit([enc.finish()])`로 묶어 제출 (배칭으로 드라이버 왕복 감소).
- `runComputeShader(:3)` = 자체 encoder 생성+즉시 submit (COULWAVE Pass3A/B, Copytxf32, ExtractTimeSeries 등 단발).
- `runCopyTextures(_EncStack)(:38/:78)` = `copyTextureToTexture` (history 시프트·state swap·temp→canonical 환원).
- **PCR 솔버**(`Run_Tridiag_Solver.js`): X-solve `p=0..Px-1`, Y-solve `p=0..Py-1` (`Px=ceil(log2(WIDTH))`, `Py=ceil(log2(HEIGHT))`, `constants_load_calc.js:427–428`), step `s=1<<p`. ping-pong bind group을 `p`에 따라 선택(`BaseToA`/`BToA`/기본, `:57`,`:82`)해 계수 copy-back 없이 핸드오프, 마지막에 `txtemp2_PCR{x,y}→txNewState` 환원(`:66`,`:91`).

---

## 6. 운용적 의의

solver와 렌더가 **동일 GPU에 co-resident** — compute 패스가 쓴 텍스처를 CPU 왕복 없이 그대로 렌더 패스가 읽어, README가 명시하듯 "interactive frame rates"에서 NLSW/Boussinesq 파랑(breaking·run-up·inundation)을 "in real time" 브라우저에서 시뮬·시각화한다 (`README.md:3`,`:7`,`:15`). 이는 FUNWAVE(Fortran/MPI 배치 → 사후 가시화)와 대비되는 **faster-than-real-time interactive** 운용 철학으로, `render_step` 동적 조정(§1)이 그 대화성을 유지하는 핵심 기제다.
