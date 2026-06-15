---
title: "Celeris-WebGPU 소스 맵 — JS↔WGSL 대응·모듈 구조·텍스처 규약"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/{js,shaders}/* 직접 read + docs/architecture 대조. 라인 인용은 해당 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 본 노트는 Celeris-WebGPU 소스 트리의 **파일 인벤토리·구조 맵**이다. 모델 정체성은 [`../README.md`](../README.md), 패스 실행 순서·데이터 흐름은 [`celeris-pipeline-graph.md`](celeris-pipeline-graph.md), 텍스처/바인딩 계약 심화는 [`celeris-webgpu-infrastructure.md`](celeris-webgpu-infrastructure.md)를 참조. 배치형 HPC 대응물로는 FUNWAVE [`../../FUNWAVE/source-analysis/funwave-source-map.md`](../../FUNWAVE/source-analysis/funwave-source-map.md) 참조 (CPU/MPI ↔ 브라우저/WebGPU 대비).

경로는 모두 Celeris-WebGPU 리포 루트(`models/Celeris/raw/source_code/Celeris-WebGPU/`) 기준 상대. 라인 수는 `wc -l`.

---

## 1. 지배방정식·수치기법 요약

Celeris는 동일 FV(유한체적) 골격 위에서 **3개 방정식 계열**을 config로 전환한다 (`NLSW_or_Bous`). 셰이더 fetch 분기는 `js/main.js:1320-1368`, 패스 시퀀스 설명은 `docs/architecture/SIMULATION_PIPELINE.md`.

| 계열 | 활성 Pass3 셰이더 | 분산항(dispersive) | 암시적 PCR solve |
|---|---|---|---|
| **NLSW** (비선형 천수) | `Pass3_NLSW.wgsl` (285) | 없음 | skip — 중간상태를 `txNewState`로 copy (`Run_Tridiag_Solver.js:37-39`) |
| **Boussinesq** | `Pass3_Bous.wgsl` (430) | `Bcoef`·3차 미분항 (`Pass3_Bous.wgsl:282-286`) | x·y 양방향 PCR |
| **COULWAVE** | `Pass3A/B_COULWAVE.wgsl` + `Pass3_COULWAVE.wgsl` | 다층 z-α 그룹핑 텍스처 | x·y 양방향 PCR (COULWAVE 변형) |

수치 골격 (각 timestep, `SIMULATION_PIPELINE.md` §Timestep + `main.js:1893-2174`):

```
Pass0   neighbor 수심 (dry/wet helper, txHnear)        Pass0.wgsl
Pass1   면(face) 재구성: H,U,V,C @ N/E/S/W            Pass1.wgsl | Pass1_HighOrder.wgsl
Pass2   면 수치플럭스 (HLL류 Riemann) → txXFlux/txYFlux Pass2.wgsl | Pass2_HighOrder_HLLC/HLLEM
[Break] breaking age/eddy-viscosity                    Pass_Breaking.wgsl
[CW]    COULWAVE 보조항 패킹 → txCW_groupings          Pass3A/B_COULWAVE.wgsl
Pass3   플럭스발산+마찰+압력+분산+breaking+pred/corr    Pass3_NLSW|Bous|COULWAVE
Bndry   경계조건·wet/dry cleanup (1차)                  BoundaryPass.wgsl
[Bous]  PCR 계수 갱신 → x-solve → y-solve              Update_TriDiag_coef* + TriDiag_PCRx/y*
Bndry   경계조건 재적용 (2차)                           BoundaryPass.wgsl
```

- **Riemann 수치플럭스**: `Pass2.wgsl:34-40` `NumericalFlux()` = HLL 형태 `(a⁺F⁻−a⁻F⁺+a⁺a⁻ΔU)/(a⁺−a⁻)`. High-order 경로는 HLLC를 선택(`main.js:1331`).
- **시간적분 (3rd-order Adams-Bashforth predictor-corrector)** — `Pass3_Bous.wgsl:400-409`:
  - `timeScheme==0`: 단일 explicit `U + dt·d_by_dt` (l.400)
  - predictor (`pred_or_corrector==1`): `U + dt/12·(23·dⁿ − 16·dⁿ⁻¹ + 5·dⁿ⁻²)` (l.404) — AB3
  - corrector (`pred_or_corrector==2`): `U + dt/24·(9·dⁿ⁺¹ + 19·dⁿ − 5·dⁿ⁻¹ + dⁿ⁻²)` (l.409) — AM4 (AB-Moulton)
  - 미분 이력(`oldGradients`/`oldOldGradients`/`predictedGradients`)·분산 이력(`F_G_star_old*`)을 텍스처로 유지 (`SIMULATION_PIPELINE.md` §Time Integration).
- **PCR(Parallel Cyclic Reduction) 삼중대각 암시 solve**: `Run_Tridiag_Solver.js:48-91`. x-방향 `Px`회, y-방향 `Py`회 log-스텝 reduction (`s = 1<<p`, l.50). 계수 copy 없이 ping-pong 바인드그룹(`BaseToA`/`BToA`)으로 핸드오프 (l.57, l.82 — CODEX 주석). 마지막 패스만 해 텍스처 `txtemp2_PCR*` 작성 → `txNewState` copy (l.66, l.91).

---

## 2. JS 모듈 맵 (35 파일, `js/`)

| 파일 | 줄 | 역할군 |
|---|---:|---|
| `main.js` | 4368 | **오케스트레이션**: init, 셰이더 fetch/컴파일, 파이프라인·바인드그룹 생성, `frame()` 루프, UI/이벤트, 패스 dispatch 시퀀스 |
| `site.js` | 4 | 엔트리 모듈 로더 |
| `constants_load_calc.js` | 556 | 파이프라인 설정·기본 config·파생 상수 계산 (Courant·dt·Bcoef 등) |
| `Config_Pipelines.js` | 283 | **파이프라인 팩토리**: `createComputePipeline`/`createRenderPipeline`/skybox/model (l.6,22,111,150) — 셰이더 코드 인자로 받는 범용 함수 |
| `Create_Textures.js` | 100 | **텍스처 할당** 팩토리: 2D rgba32f / 3D rgba16f / bgra8 / 1D (l.3,16,29,55,69) |
| `Copy_Data_to_Textures.js` | 527 | CPU→GPU 데이터 전송 (bathy·waves·이미지) |
| `Run_Compute_Shader.js` | 89 | 컴퓨트 dispatch 헬퍼 (`runComputeShader`) |
| `Run_Tridiag_Solver.js` | 93 | **PCR 솔버 드라이버** (§1 참조) |
| `Handler_Pass0.js` | 68 | per-pass 핸들러 (바인드그룹 레이아웃·바인드그룹) |
| `Handler_Pass1.js` | 110 | Pass1 핸들러 |
| `Handler_Pass2.js` | 227 | Pass2 핸들러 |
| `Handler_Pass3.js` | 572 | Pass3 + Pass3A/B_COULWAVE 핸들러 (3개 레이아웃) |
| `Handler_PassBreaking.js` | 134 | breaking 패스 핸들러 |
| `Handler_BoundaryPass.js` | 147 | 경계 패스 핸들러 (NewState 변형 포함) |
| `Handler_Tridiag.js` | 108 | PCR x/y 바인드그룹 (ping-pong 변형) |
| `Handler_UpdateTrid.js` | 80 | 삼중대각 계수 갱신 핸들러 |
| `Handler_Updateneardry.js` | 53 | near-dry 플래그 갱신 핸들러 |
| `Handler_SedTrans_Pass1.js` | 123 | 퇴적물 면 재구성 핸들러 |
| `Handler_SedTrans_Pass3.js` | 253 | 퇴적물 적분 핸들러 |
| `Handler_SedTrans_UpdateBottom.js` | 134 | 퇴적물 bed 갱신 핸들러 |
| `Handler_CalcMeans.js` | 199 | 진단: 시간평균 통계 |
| `Handler_CalcWaveHeight.js` | 92 | 진단: 파고(wave height) |
| `Handler_ExtractTimeSeries.js` | 132 | 진단: 시계열/툴팁 추출 |
| `Time_Series.js` | 171 | 시계열 좌표·CPU측 관리 |
| `Handler_AddDisturbance.js` | 120 | 교란(disturbance) 주입 |
| `Handler_MouseClickChange.js` | 119 | 마우스 편집 (bathy/state) |
| `Wave_Generator.js` | 334 | 경계 파랑 생성 (forcing) |
| `Handler_Copytxf32_txf16.js` | 133 | f32→f16 렌더 데이터 패킹 |
| `Handler_Model.js` | 57 | 3D 모델(glTF) 렌더 핸들러 |
| `Handler_Skybox.js` | 56 | 스카이박스 렌더 핸들러 |
| `Handler_Render.js` | 391 | **2D/3D 렌더** 바인드그룹·파이프라인 (vertex/fragment, l.3~) |
| `Model_Loaders.js` | 235 | 3D 모델 로딩 |
| `display_parameters.js` | 232 | UI 패널 로직 |
| `File_Loader.js` | 608 | 입력 파싱 (JSON·bathy·waves·이미지) |
| `File_Writer.js` | 641 | 출력 (JPEG·GIF·binary·JSON) |

> 핸들러 규약: `Handler_*.js`는 **바인드그룹 레이아웃·바인드그룹만** 정의한다 (`grep`상 셰이더 코드·`createShaderModule` 미포함). 셰이더 fetch·컴파일·파이프라인 생성은 모두 `main.js`에서 수행 (`fetchShader` l.1320~, `createComputePipeline` l.1392~).

---

## 3. WGSL 셰이더 맵 (42 파일, `shaders/`)

| 파일 | 줄 | 그룹 |
|---|---:|---|
| `Pass0.wgsl` | 60 | Hydro Pass0 (near-dry helper) |
| `Pass1.wgsl` | 172 | Hydro Pass1 (면 재구성, 표준) |
| `Pass1_HighOrder.wgsl` | 368 | Pass1 고차 변형 |
| `Pass2.wgsl` | 206 | Hydro Pass2 (HLL 플럭스, 표준) |
| `Pass2_HighOrder_HLLC.wgsl` | 291 | Pass2 고차 HLLC (활성 고차 경로) |
| `Pass2_HighOrder_HLLEM.wgsl` | 274 | Pass2 고차 HLLEM |
| `Pass3_NLSW.wgsl` | 285 | Pass3 NLSW (분산 없음) |
| `Pass3_Bous.wgsl` | 430 | Pass3 Boussinesq |
| `Pass3_COULWAVE.wgsl` | 524 | Pass3 COULWAVE |
| `Pass3A_COULWAVE.wgsl` | 85 | COULWAVE 보조항 A (u,v,du,dv·z-α) |
| `Pass3B_COULWAVE.wgsl` | 206 | COULWAVE 보조항 B (S,T·E terms·F,G) |
| `Pass_Breaking.wgsl` | 144 | 파괴 age/eddy-viscosity |
| `BoundaryPass.wgsl` | 595 | 경계조건·wet/dry cleanup |
| `Update_TriDiag_coef.wgsl` | 111 | PCR 계수 초기화 (Bous) |
| `Update_TriDiag_coef_COULWAVE.wgsl` | 117 | PCR 계수 초기화 (COULWAVE) |
| `TriDiag_PCRx.wgsl` | 107 | PCR x-solve (Bous) |
| `TriDiag_PCRy.wgsl` | 110 | PCR y-solve (Bous) |
| `TriDiag_PCRx_COULWAVE.wgsl` | 116 | PCR x-solve (COULWAVE) |
| `TriDiag_PCRy_COULWAVE.wgsl` | 119 | PCR y-solve (COULWAVE) |
| `SedTrans_Pass1.wgsl` | 135 | 퇴적물 면 재구성 |
| `SedTrans_Pass3.wgsl` | 240 | 퇴적물 적분 (활성) |
| `SedTrans_Pass3_old.wgsl` | 180 | 퇴적물 적분 (구버전) |
| `SedTrans_Pass3_wBedUpdate.wgsl` | 254 | 퇴적물 적분 + bed update 변형 |
| `SedTrans_UpdateBottom.wgsl` | 122 | 퇴적물 bed 갱신 (활성) |
| `SedTrans_UpdateBottom_testing.wgsl` | 90 | bed 갱신 실험본 |
| `Update_neardry.wgsl` | 56 | near-dry 플래그 재계산 |
| `CalcMeans.wgsl` | 104 | 진단: 시간평균 |
| `CalcWaveHeight.wgsl` | 77 | 진단: 파고 |
| `ExtractTimeSeries.wgsl` | 65 | 진단: 시계열/툴팁 (1D 출력) |
| `AddDisturbance.wgsl` | 241 | 교란 주입 |
| `MouseClickChange.wgsl` | 246 | 마우스 편집 |
| `Copytxf32_txf16.wgsl` | 50 | f32→f16 렌더 패킹 |
| `vertex.wgsl` | 19 | 2D 렌더 vertex |
| `vertex3D.wgsl` | 85 | 3D 렌더 vertex |
| `fragment.wgsl` | 928 | 2D/3D 메인 fragment (활성) |
| `fragment_testing.wgsl` | 867 | fragment 실험본 |
| `model.vertex.wgsl` / `model.fragment.wgsl` | 23 / 31 | 3D 모델 렌더 |
| `skybox.vertex.wgsl` / `skybox.fragment.wgsl` | 30 / 11 | 스카이박스 |
| `duck.vertex.wgsl` / `duck.fragment.wgsl` | 45 / 33 | duck 모델 (main.js l.1379-80 주석처리 — 비활성) |

> 비활성/실험 변형: `*_old`, `*_testing`, `duck.*`. 활성 경로는 `main.js`의 `fetchShader` 분기로만 판정 (`SIMULATION_PIPELINE.md` §Active Shader Selection 경고 일치).

---

## 4. JS 핸들러 ↔ WGSL 셰이더 ↔ dispatch 대응

핸들러는 바인드그룹 레이아웃을 정의하고, `main.js`가 동명 셰이더 코드와 짝지어 파이프라인을 만든 뒤(`main.js:1392-1422`) frame 루프에서 dispatch(`main.js:1893-2174`)한다. config 분기로 셰이더 파일이 바뀌어도 핸들러(레이아웃)는 동일.

| 핸들러 (`js/`) | 파이프라인 생성 (main.js) | WGSL 셰이더 | dispatch (frame loop) |
|---|---|---|---|
| `Handler_Pass0` | `1392` | `Pass0.wgsl` | `1893` |
| `Handler_Pass1` | `1393` | `Pass1.wgsl` / `Pass1_HighOrder.wgsl` (`1324-1326`) | `1896`, `2163` (진단 재실행) |
| `Handler_SedTrans_Pass1` | `1394` | `SedTrans_Pass1.wgsl` | `1900` |
| `Handler_Pass2` | `1395` | `Pass2.wgsl` / `Pass2_HighOrder_HLLC.wgsl` (`1331-1333`) | `1904` |
| `Handler_PassBreaking` | `1396` | `Pass_Breaking.wgsl` | `1908` |
| `Handler_Pass3` (3A) | `1397` | `Pass3A_COULWAVE.wgsl` | `1917` |
| `Handler_Pass3` (3B) | `1398` | `Pass3B_COULWAVE.wgsl` | `1918` |
| `Handler_Pass3` (NLSW) | `1399` | `Pass3_NLSW.wgsl` | `1921~` (계열 분기) |
| `Handler_Pass3` (Bous/CW) | `1400` | `Pass3_Bous.wgsl` / `Pass3_COULWAVE.wgsl` (`1339-1345`) | `1921~` |
| `Handler_SedTrans_Pass3` | `1401` | `SedTrans_Pass3.wgsl` | `1944` |
| `Handler_BoundaryPass` | `1402` | `BoundaryPass.wgsl` | `1949` (1차), `1984` (2차, NewState) |
| `Handler_Tridiag` (X) | `1403` | `TriDiag_PCRx.wgsl` / `_COULWAVE` (`1354-1357`) | `Run_Tridiag_Solver.js:59` |
| `Handler_Tridiag` (Y) | `1404` | `TriDiag_PCRy.wgsl` / `_COULWAVE` (`1355-1358`) | `Run_Tridiag_Solver.js:84` |
| `Handler_SedTrans_UpdateBottom` | `1405` | `SedTrans_UpdateBottom.wgsl` | `2134` |
| `Handler_Updateneardry` | `1406` | `Update_neardry.wgsl` | `1801`, `1998`, `2137` |
| `Handler_UpdateTrid` | `1407` | `Update_TriDiag_coef.wgsl` / `_COULWAVE` (`1366-1368`) | `1805`, `1959`, `2089` |
| `Handler_CalcMeans` | `1408` | `CalcMeans.wgsl` | `2165` |
| `Handler_CalcWaveHeight` | `1409` | `CalcWaveHeight.wgsl` | `2174` |
| `Handler_AddDisturbance` | `1410` | `AddDisturbance.wgsl` | (UI 트리거) |
| `Handler_MouseClickChange` | `1411` | `MouseClickChange.wgsl` | (UI 트리거) |
| `Handler_ExtractTimeSeries` | `1412` | `ExtractTimeSeries.wgsl` | `2652` (1D dispatch) |
| `Handler_Copytxf32_txf16` | `1422` | `Copytxf32_txf16.wgsl` | (렌더 전 패킹) |
| `Handler_Render`/`Skybox`/`Model` | (render 파이프라인) | `vertex.wgsl`+`fragment.wgsl` / `skybox.*` / `model.*` | (렌더 단계) |

바인드그룹 인자 순서로 확인된 dataflow 예: `Pass1` ← `txState,txBottom` → `txH,txU,txV,txC` (`Handler_Pass1.js:75`); `Pass2` ← `txH,txU,txV,txBottom,txC,txHnear`(+Sed) → `txXFlux,txYFlux`(+Sed) (`Handler_Pass2.js:156`); `Pass3` ← state·flux·gradient 이력·`txCW_groupings(3d)` → `txNewState,dU_by_dt,F_G_star,current_stateUVstar` (`Handler_Pass3.js:202`).

---

## 5. 텍스처 상태 규약 요약 (브리프)

심화 계약은 인프라 노트 + `docs/architecture/DATA_AND_TEXTURES.md`. 텍스처 생성·라벨은 `js/main.js:341-426`에서 검증.

| 텍스처 | 채널 (r,g,b,a) | 출처 |
|---|---|---|
| `txState` / `txNewState` | η, P(=hu), Q(=hv), scalar c | `main.js:343-344`; `DATA_AND_TEXTURES.md` §State |
| `txstateUVstar` / `current_stateUVstar` | bous-grouped 중간상태 (η,U,V,c); PCR RHS/해 | `main.js:347-348` |
| `txBottom` | bed N면, bed E면, bed 셀중심, near-dry 플래그 | `main.js:341`; `DATA_AND_TEXTURES.md` §Bathy |
| `txBottomInitial` / `txHardBottom` | 초기 bed / 비침식 하한 bed | `main.js:342`, `361` |
| `txH` / `txU` / `txV` / `txC` | 면(N,E,S,W = x,y,z,w) 수심 / u / v / scalar | `main.js:349-353`; `DATA_AND_TEXTURES.md` §Face (x=N면, y=E면 주의) |
| `txHnear` | dry/wet helper (Pass0 산출) | `main.js:352`; `Pass0.wgsl:18` |
| `txXFlux` / `txYFlux` | mass, x-mom, y-mom, scalar 플럭스 | `main.js:365-366`; `DATA_AND_TEXTURES.md` §Flux |
| `txBreaking` | breaking age, eddy-visc, intensity, subgrid | `main.js:369`; `DATA_AND_TEXTURES.md` §Breaking |
| `coefMatx` / `coefMaty` | 삼중대각: a(sub), b(diag), c(super), 0/rhs | `main.js:393-394`; `Update_TriDiag_coef.wgsl:72,108` `vec4(a,b,c,0)` |
| `newcoef_x/y`, `txtemp_PCR*`, `txtemp2_PCR*` | PCR ping-pong 계수 / 최종 해 | `main.js:395-396`; `DATA_AND_TEXTURES.md` §Tridiag |
| `txCW_groupings` | COULWAVE 6-layer rgba32f 3D (u/v/du/dv, z-α, S/T, grad, E, …) | `main.js:405`; `Handler_Pass3.js:222` (3d view); `DATA_AND_TEXTURES.md` §COULWAVE |

---

## 부록 — 검증 메모

- AB3 predictor / AM4 corrector 계수는 `Pass3_Bous.wgsl:400-409`에서 직접 확인 (NLSW/COULWAVE Pass3도 동일 골격 Globals 공유 — `Pass3_NLSW.wgsl:1-12`).
- PCR copy-free ping-pong은 `Run_Tridiag_Solver.js`의 CODEX 주석(l.21,46,57,82)과 `TriDiag_PCRx.wgsl:1-8`(`P` uniform 추가)에서 교차확인.
- `Config_Pipelines.js`·`Create_Textures.js`는 **범용 팩토리** — 패스별 셰이더/텍스처 바인딩은 전부 `main.js`가 결정.
