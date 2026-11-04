---
title: "Celeris-WebGPU 인프라·데이터 규약 — 텍스처 상태·바인드그룹·config·진단"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/js/{Create_Textures,Config_Pipelines,Run_Compute_Shader,constants_load_calc,main,Handler_Calc*,Handler_ExtractTimeSeries}.js 직접 read + docs/architecture 대조. 라인 인용 소스 기준. 2026-06-15. 2026-11-04 Celeris recovery 대조 보고서 반영"
last_source_check: "2026-11-04 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
source_scope: Celeris-WebGPU/js, Celeris-WebGPU/shaders
---

> 관련: [../README.md](../README.md) · [celeris-source-map.md](celeris-source-map.md) (파일 지도) · [celeris-pipeline-graph.md](celeris-pipeline-graph.md) (패스 순서 그래프).
> 이 노트는 **GPU 위에 시뮬레이션이 어떻게 배선되는가** — 텍스처 상태 규약, 바인드그룹 패턴, 시작 흐름, config 파생 상수, 진단 — 를 다룬다. 패스별 물리는 `celeris-fv-reconstruction`·`celeris-boussinesq-solver`·`celeris-breaking-boundary`·`celeris-coulwave`·`celeris-sediment`, 렌더는 `celeris-render` 참조.

## 0. 기본 골격

Celeris-WebGPU는 빌드 단계 없이 JavaScript 모듈과 WGSL 컴퓨트 셰이더를 브라우저에서 로드한다(`ARCHITECTURE.md:3`). 모델 선택값은 NLSW·Boussinesq·COULWAVE 경로를 구분한다(`ARCHITECTURE.md:63–67`). 유체 상태의 시간적분은 GPU 텍스처를 갱신한다(`shaders/Pass3_Bous.wgsl:399–429`). 입력 지형은 CPU의 `bathy2D` 2차원 배열에도 저장한다(`js/File_Loader.js:36–54`). [11-04 전수 검증 정정]
주요 2D 유체 상태는 `WIDTH × HEIGHT`의 `rgba32float`이다 (`js/Create_Textures.js:2–13`). [11-04 대조 정정]
COULWAVE 그룹은 3D이다 (`js/Create_Textures.js:54–65`; `js/main.js:515`). [11-04 대조 정정]
파 성분·시계열·더미 텍스처는 별도 크기이다 (`js/Create_Textures.js:68–71`; `js/main.js:529–536,563–576`). [11-04 대조 정정] [11-04 전수 검증 정정]
렌더 캐시는 `rgba16float`이다 (`js/Create_Textures.js:15–18`). [11-04 대조 정정]
위의 `rgba32float` 유체 상태 텍스처는 네 채널 `(r/x, g/y, b/z, a/w)`을 사용한다(`js/Create_Textures.js:2–6`; `shaders/Pass3_Bous.wgsl:392–429`). [11-04 전수 검증 정정]

핵심 헬퍼 (`js/Create_Textures.js`):

| 헬퍼 | 포맷·차원 | 용도 |
|---|---|---|
| `create_2D_Texture` | rgba32float 2D | 모든 시뮬 상태 텍스처 (라인 2) |
| `create_2D_F16Texture` | rgba16float 2D-array | 렌더 캐시 `txRenderVarsf16` (라인 15) |
| `create_2D_Image_Texture` | bgra8unorm 2D | 스크린/오버레이 (라인 28) |
| `create_3D_Image_Texture` | bgra8unorm 2D 배열 | skybox는 6층 배열에 cube view를 만든다 (`js/Create_Textures.js:41–58`; `js/main.js:556,782`). [11-04 대조 정정] |
| `create_3D_Data_Texture` | rgba32float 3D | COULWAVE `txCW_groupings` (라인 54) |
| `create_1D_Texture` | rgba32float 1×W | 파동 입력·시계열 위치/데이터 (라인 68) |
| `createUniformBuffer` | 기본 256 B | 패스별 uniform (라인 81) |
| `create_Depth_Texture` | depth24plus | 3D 렌더 깊이 (라인 88) |

`Create_Textures.js`의 텍스처 헬퍼로 생성한 텍스처는(`js/Create_Textures.js:2-99`) `allTextures` Set에 추적 등록 → 재시작 시 일괄 `destroy()` (`js/main.js:225-228`). `Model_Loaders.js`의 glTF 텍스처는 이 Set에 등록하지 않는다(`js/Model_Loaders.js:95-116`).

---

## 1. 텍스처 상태 규약 (centerpiece)

채널 의미는 `docs/architecture/DATA_AND_TEXTURES.md`와 대조했고, 진단 셰이더(CalcMeans/CalcWaveHeight/ExtractTimeSeries) 실제 `.x/.y/.z/.w` 접근으로 교차 검증했다. 할당은 모두 `js/main.js:449-576`.

### 1a. 주 상태 (primary state)

| 텍스처 | r/x | g/y | b/z | a/w | 쓰는 패스 → 읽는 패스 | line |
|---|---|---|---|---|---|---|
| `txState` | η (자유수면) | P = hu (x-운동량) | Q = hv (y-운동량) | scalar/tracer | Pass1이 면 재구성에 읽는다. Pass2는 면 텍스처에서 플럭스를 계산한다. 스텝 끝에 `txNewState`를 `txState`로 복사한다. | `js/main.js:970,1015,2900` [11-04 대조 정정] |
| `txNewState` | η (n+1) | P | Q | scalar | Pass3 출력 → 다음 스텝 입력. CalcMeans/CalcWaveHeight가 η 읽음 | 344 |
| `txstateUVstar` | η | U* | V* | c | UVstar는 분산 중간 상태의 시간 이력이다. PCR 최종 해와 구분한다. | `shaders/Pass3_Bous.wgsl:426–429`; `js/main.js:2900–2901` [11-04 대조 정정] |
| `current_stateUVstar` | η | U* | V* | c | bous-그룹 상태 (n+1) → 스텝 끝 `txstateUVstar`로 복사 | 348 |
| `txState_Sed` / `txNewState_Sed` | sed 농도 상태 (class별) | — | — | — | 퇴적물 전송 (옵션) | 345-346 |

> NLSW는 `current_stateUVstar`를 `txNewState`에 복사한다 (`js/Run_Tridiag_Solver.js:37–38`). [11-04 대조 정정]
> Boussinesq 경로는 `current_stateUVstar`에서 PCR의 초기 우변을 읽는다 (`shaders/TriDiag_PCRx.wgsl:70–72,101–104`; `shaders/TriDiag_PCRy.wgsl:70–72,101–104`). [11-04 대조 정정]
> COULWAVE 경로는 중간 상태에서 만든 계수 텍스처의 a 채널에서 PCR의 초기 우변을 읽는다 (`shaders/Update_TriDiag_coef_COULWAVE.wgsl:51–52,84–85,114–115`; `shaders/TriDiag_PCRx_COULWAVE.wgsl:72–74,101–107`). [11-04 대조 정정]
> 각 방향의 PCR 해는 `txtemp2_PCRx` 또는 `txtemp2_PCRy`에 기록한다 (`shaders/TriDiag_PCRx.wgsl:101–104`; `shaders/TriDiag_PCRy.wgsl:101–104`). [11-04 대조 정정]
> 호스트는 그 해를 `txNewState`로 복사한다 (`js/Run_Tridiag_Solver.js:66,91`). [11-04 대조 정정]
>
> 첫 경계의 상태 입력은 `current_stateUVstar`이다 (`js/main.js:1157`). [11-04 대조 정정]
> 풀이 뒤 경계의 상태 입력은 `txNewState`이다 (`js/main.js:1160`). [11-04 대조 정정]

### 1b. 지형·마찰·소스

| 텍스처 | r/x | g/y | b/z | a/w | 비고 | line |
|---|---|---|---|---|---|---|
| `txBottom` | 북면 bed 표고 BN | 동면 bed 표고 BE | 셀중심 bed 표고 | near-dry 플래그 (+far, −near) | `copyBathyDataToTexture`가 BN/BE/center/flag 채움 | 341 |
| `txBottomInitial` | (txBottom 사본) | | | | 이동 bed·누적 sed 변화 기준 | 342 |
| `txHardBottom` | hard bed 하한 | | | | 비침식 하한 | 361 |
| `txBottomFriction` | 마찰계수 [0,1] | | | | ExtractTimeSeries가 .x 읽음 | 362 |
| `txContSource` | passive tracer 소스맵 | | | | | 364 |
| `txDesignComponents` | 추가 컴포넌트 맵 | | | | GUI 설계요소 | 363 |

`txBottom` 채널은 `copyBathyDataToTexture`에서 직접 확인: `paddedFlatData[+0]=BN(red)`, `[+1]=BE(green)`, `[+2]=center(blue)`, `[+3]=near-dry flag ±99(alpha)` (`js/Copy_Data_to_Textures.js:44-47, 56`). CalcMeans는 bed로 `txBottom...z`(중심)를 사용 (`shaders/CalcMeans.wgsl:41`).

### 1c. 면 재구성 (Pass1 출력) — 채널 = 면 순서

| 텍스처 | x | y | z | w | line |
|---|---|---|---|---|---|
| `txH` | 북면 H | 동면 H | 남면 H | 서면 H | 349 |
| `txU` | 북면 u | 동면 u | 남면 u | 서면 u | 350 |
| `txV` | 북면 v | 동면 v | 남면 v | 서면 v | 351 |
| `txC` | 북면 c | 동면 c | 남면 c | 서면 c | 353 |
| `txHnear` | 이웃 북측 수심 | 이웃 동측 수심 | 이웃 남측 수심 | 이웃 서측 수심 | Pass0가 쓰고 Pass2가 읽는다 (`js/main.js:957,1015`; `shaders/Pass0.wgsl:52–57`; `shaders/Pass2.wgsl:70,105`). [11-04 대조 정정] |

> ⚠ x=북면, y=동면. CalcMeans는 셀 평균을 `(x+y+z+w)/4`로 복원 (`shaders/CalcMeans.wgsl:43-46`) — 이 4-면 규약을 그대로 가정한다.

### 1d. 플럭스 (Pass2 출력)

| 텍스처 | x | y | z | w | line |
|---|---|---|---|---|---|
| `txXFlux` | 질량/수면 플럭스 | x-운동량 플럭스 | y-운동량 플럭스 | scalar 플럭스 | 365 |
| `txYFlux` | (동일 규약, y방향) | | | | 366 |
| `txXFlux_Sed`/`txYFlux_Sed` | sed class별 플럭스 | | | | 367-368 |

### 1e. 시간적분 그래디언트 (Adams-Bashforth)

| 텍스처 | 의미 | line |
|---|---|---|
| `dU_by_dt` | Pass3 출력 d(state)/dt | 397 |
| `predictedGradients` | predictor 단계 d/dt | 371 |
| `oldGradients` | 이전 스텝 d/dt | 372 |
| `oldOldGradients` | 두 스텝 전 d/dt | 373 |
| `predictedF_G_star` / `F_G_star_oldGradients` / `F_G_star_oldOldGradients` | Bous 전용 F*,G* (현/이전/두스텝전) | 377-379 |
| `*_Sed` 변종 | 퇴적물 적분용 | 374-376 |

스텝 끝 시프트: `oldGradients→oldOldGradients`, `predictedGradients→oldGradients` (`js/main.js:2896-2897`).

예측 쇄파·COULWAVE B는 직전 시간 단계의 마지막 Pass3가 남긴 도함수를 읽는다 (`shaders/Pass_Breaking.wgsl:55`; `shaders/Pass3B_COULWAVE.wgsl:191`; `js/main.js:2649–2679`). [11-04 대조 정정]
첫 시간 단계에는 이전 Pass3 결과가 없다 (`js/main.js:2649–2679,2895–2901`). [11-04 대조 정정]
보정 호출은 이번 예측 Pass3의 도함수를 읽는다 (`js/main.js:2678–2685,2783–2812`). [11-04 대조 정정]
Pass2도 이번 쇄파 갱신보다 먼저 `txBreaking`을 읽는다 (`js/main.js:2649–2679`). [11-04 대조 정정]

### 1f. PCR 삼중대각 솔버 (Bous/COULWAVE)

| 텍스처 | r/x=a(하) | g/y=b(대각) | b/z=c(상) | a/w=RHS | line |
|---|---|---|---|---|---|
| `coefMatx`/`coefMaty` | 초기 삼중대각 계수 (x/y dir) | | | | 393-394 |
| `newcoef_x`/`newcoef_y` | PCR 계수 ping-pong A면 | | | | 395-396 |
| `txtemp_PCRx`/`txtemp_PCRy` | PCR 계수 ping-pong B면 | | | | 386-387 |
| `txtemp2_PCRx`/`txtemp2_PCRy` | 마지막 PCR 반복의 해(solution)만 기록 | | | | 388-389 |

> 활성 솔버는 매 반복마다 `coefMat*→newcoef_*` 복사를 하지 않는다 — JS가 "현재 계수 텍스처 읽고 다음 계수 텍스처 쓰는" 바인드그룹을 선택해 ping-pong 한다 (DATA_AND_TEXTURES.md). PCR 메커닉은 `celeris-boussinesq-solver` 참조.

### 1g. 임시·경계·breaking·기타

| 텍스처 | 용도 | line |
|---|---|---|
| `txBreaking` | x=breaking age, y=eddy visc, z=front/intensity, w=Smagorinsky placeholder | 369 |
| `txDissipationFlux` | breaking 운동량 확산용 점성-가중 그래디언트 | 370 |
| `txtemp_Breaking` | breaking 임시 → `txBreaking` 복사 | 380 |
| `txtemp_bottom`/`txtemp_boundary`/`txtemp_boundary_Sed` | Boundary 패스 임시 | 381-383 |
| `txtemp_AddDisturbance`/`txtemp_MouseClick`/`txtemp_MouseClick2` | 교란·마우스 편집 임시 | 390-392 |
| `txModelVelocities` | 셀 평균 u,v (플럭스 스킴이 쓰는 실 u,v). CalcMeans가 `(u,v,eta,h)` 기록 | 400 / `CalcMeans.wgsl:102` |
| `txBoundaryForcing` | ship pressure (WebGPU 미사용) | 399 |
| `txzeros` | 0 리셋용 | 438 |
| `txCW_groupings` (3D) + `txCW_uvhuhv`/`zalpha`/`STval`/`STgrad`/`Eterms`/`FGterms` | COULWAVE 중간장 (6 layer). 자세히는 `celeris-coulwave` | 405-426 |

### 1h. 진단·렌더·시계열

| 텍스처 | 내용 | line |
|---|---|---|
| `txMeans` | 러닝 평균 (eta,u,v,c) | 429 |
| `txMeans_Speed` | max: x=u_max, y=v_max, z=speed_max, w=eta_max(=Hs용) | 431 |
| `txMeans_Momflux` | x=hu²_max, y=hv²_max, z=momflux_max, w=평균 |vorticity| | 433 |
| `txtemp_Means*` | 위 셋의 write 타겟 임시 (read+write 동일 텍스처 불가 회피) | 430/432/434 |
| `txWaveHeight` | x=Σeta², y=상대변화, z=H_sig, w=H_mean(RMS) | 435 |
| `txtemp_WaveHeight` / `txBaseline_WaveHeight` | write 임시 / baseline | 436-437 |
| `txRenderVarsf16` (f16, 3 layer) | 렌더 캐시. `shaders/Copytxf32_txf16.wgsl`가 f32→f16 패킹 (자세히는 `celeris-render`) | 449 |
| `txWaves` (1D) | 스펙트럼/경계 파동 입력 [amp, period, dir, phase] | 453 |
| `txTimeSeries_Locations` (1D) | 시계열 격자좌표 (element 0=tooltip) | 455 |
| `txTimeSeries_Data` (1D) | ExtractTimeSeries write 타겟 | 456 |

---

## 2. 바인드그룹 패턴 — handler ⇄ bind group ⇄ WGSL @binding

**바인딩 번호가 인터페이스**다. 각 패스는 `Handler_<Pass>.js`에서 (a) `create_*_BindGroupLayout(device)` (b) `create_*_BindGroup(...)` 두 함수를 정의하고, JS 인자 순서를 numbered `@group(0) @binding(N)`에 매핑한다. handler는 디스패치를 하지 않는다 — 디스패치는 `Run_Compute_Shader.js`가 담당 (WEBGPU_BINDING_PATTERN.md:9-15).

**파이프라인 생성** (`js/Config_Pipelines.js:6-19`): `createComputePipeline(device, code, layout, set)`는 `createPipelineLayout({bindGroupLayouts:[layout]})` + `createShaderModule({code})` + entryPoint `'main'`. 모든 컴퓨트는 단일 bind group(group 0)·entryPoint `main`. 렌더 파이프라인(quad/vertexgrid/skybox/model/duck)은 별도 팩토리 (라인 22-282).

**3-layer 좌표 규약** — 텍스처 rename·바인딩 추가는 세 층을 동시에 바꿔야 한다:
1. WGSL `@group(0) @binding(N)` 선언
2. `Handler_*.js`의 layout entry + bind group `resource:` 매핑
3. `main.js`의 `create_*_BindGroup(...)` 호출 인자 + 포맷(`Create_Textures.js`)

구체 예 — **CalcMeans**:
- WGSL: `@binding(8) var txtemp_Means: texture_storage_2d<rgba32float, write>` (`shaders/CalcMeans.wgsl:20`)
- Layout: binding 8을 `storageTexture{access:'write-only', format:'rgba32float', viewDimension:'2d'}`로 선언 (`js/Handler_CalcMeans.js:74-83`)
- BindGroup: binding 8 → `txtemp_Means.createView()` (`js/Handler_CalcMeans.js:175-177`)
- main.js: `create_CalcMeans_BindGroup(device, CalcMeans_uniformBuffer, txMeans, txMeans_Speed, ..., txtemp_Means, ...)` 인자 순서 (`js/main.js:1297`)

binding 14개 모두 셰이더의 `@binding(0..13)`와 일치해야 하며, 하나라도 어긋나면 검증 오류. **공유 레이아웃** 주의: `Handler_Pass2.js`는 standard/HLLC/HLLEM 변종, `Handler_Pass3.js`는 NLSW/Bous/COULWAVE를 한 레이아웃으로 공유 — 미사용 바인딩도 호환 계약의 일부로 취급해야 한다 (WEBGPU_BINDING_PATTERN.md:36-46). handler 주석에 "fragment shader"라 적힌 컴퓨트 바인딩이 많으니 주석 말고 `@binding` 선언을 신뢰 (라인 48-50).

**임시 텍스처가 흔한 이유**: WebGPU는 한 패스에서 같은 텍스처 read+write를 허용하지 않으므로, `txtemp_*`에 쓴 뒤 `runCopyTextures_EncStack`로 canonical 텍스처에 복사한다 (WEBGPU_BINDING_PATTERN.md:25-34).

---

## 3. 시작 흐름 (startup) — `js/main.js`

진입은 두 경로: URL `?agent_case=...&autostart=1` 자동 시작 (`loadAgentCaseFromUrl`, 라인 132-167) 또는 `DOMContentLoaded` UI 핸들러 (라인 2951). 둘 다 `initializeWebGPUApp()` (라인 186-)을 호출. 시작 반쪽 순서:

1. **이전 실행 정리**: `allTextures` 전부 destroy, `allComputePipelines`/`RenderPipeline` clear, device/adapter/context null화 (라인 191-202).
2. **adapter 요청**: `gpu.requestAdapter({powerPreference:"high-performance"})`, 실패 시 fallback 어댑터 (라인 205-212).
3. **device 요청**: `bb99fee`(2026-07-02)는 장치 요청에 `maxTextureDimension2D`를 추가했다 (`bb99fee:js/main.js:248–261`). [11-04 대조 정정]
   현재 값은 `const requestedMaxTextureDimension2D = adapter.limits?.maxTextureDimension2D || 8192;`로 정한다 (`js/main.js:249`). [11-04 대조 정정]
   `requiredLimits`는 이 값을 전달한다 (`js/main.js:254–261`). [11-04 대조 정정]
4. **canvas 컨텍스트 config**: `canvas.getContext('webgpu')`, `swapChainFormat='bgra8unorm'`, `context.configure({device, format, usage: RENDER_ATTACHMENT|COPY_SRC})` (라인 233-244).
5. **OrderedFunctions**: 본판은 adapter/device를 얻은 뒤 `OrderedFunctions`를 호출한다 (`js/main.js:240,254,300`). [11-04 대조 정정]
   `bb99fee`(2026-07-02)는 `OrderedFunctions`에 type-5 경계 시계열 로딩을 추가했다 (`bb99fee:js/main.js:201–213`). [11-04 대조 정정]
   현재 함수는 설정·수심·파랑 다음에 선택 경계 시계열을 읽는다 (`js/main.js:201–213`). [11-04 대조 정정]
   반환 객체는 공통 시간벡터를 포함한다 (`js/main.js:213`; `js/File_Loader.js:453,502–510`). [11-04 대조 정정]
6. **uniform 버퍼 생성**: 패스별 `createUniformBuffer(device)` ×수십 개 + readback 버퍼(`bytesPerRow` 256배수 정렬) (라인 286-321).
7. **텍스처 할당**: 1c 섹션의 전 텍스처 (라인 341-456).
8. **CPU→GPU 복사**: `copyBathyDataToTexture`(txBottom) / `refreshBoundaryWaveTexture`(txWaves) / `copyTSlocsToTexture`(시계열 위치) / `copyInitialConditionDataToTexture`(txState·txstateUVstar) (라인 462-475, `js/Copy_Data_to_Textures.js`). 옵션: 초기수면·마찰·hard bottom·overlay 파일 (라인 478-).
9. **bind group 생성**: bind group은 대응 파이프라인 생성보다 먼저 만든다 (`js/main.js:954–960,1619–1627`). [11-04 대조 정정]
10. **셰이더 fetch + 파이프라인**: `fetchShader('/shaders/*.wgsl')` (라인 1371- ) → `createComputePipeline(...)` (라인 1408- ).
11. **루프 진입**: `async function frame()` 정의 (라인 1540) 후 `await frame()` 1회 호출 (라인 2938), 매 프레임 끝 `requestAnimationFrame(frame)` (라인 2933).

`render_step` 자동 튜닝: 1초마다 스텝당 클럭을 재고 GPU 포화에 맞춰 `render_step`을 ±1 조정 (라인 1565-1595). 패스 디스패치 순서 전체는 `celeris-pipeline-graph` 참조.

---

## 4. config + 파생 상수 — `js/constants_load_calc.js`

`calc_constants`는 ~270 키 평면 JSON 기본값 (라인 14-365). `config.json`이 fetch되어 `{...calc_constants, ...loadedConfig}`로 오버라이드 (라인 369-401). 핵심 입력:

| 키 | 기본 | 의미 |
|---|---|---|
| `WIDTH`/`HEIGHT` | 800/600 | 격자 |
| `dx`/`dy` | 1.0 | 셀 크기 |
| `Courant_num` | 0.15 | 목표 Courant (P-C ~0.25, explicit ~0.05) |
| `timeScheme` | 2 | 0=Euler, 1=AB3 예측, 2=AB3 예측과 AM4 한 번 보정 (`shaders/Pass3_Bous.wgsl:399–410`; `js/main.js:2757–2815`). [11-04 대조 정정] |
| `NLSW_or_Bous` | 0 | 0=NLSW, 1=Madsen Bous, 2=COULWAVE |
| `Bcoef` | 1/15 | 분산 파라미터 (최적값) |
| `Bous_alpha` | −0.531 | Nwogu 확장 Bous 파라미터 |
| `g` | 9.80665 | 중력 |
| `base_depth` | 20.0 | dt 추정용 특성 수심 |
| `Theta` | 2.0 | minmod 리미터 (1=upwind~2=centered) |
| `friction`/`isManning` | 0/0 | 마찰계수 또는 Manning n |
| `useBreakingModel` | 1 | breaking 모델 on |

**파생 상수** (`init_sim_parameters`, 라인 404-428):
- `dt = Courant_num · min(dx,dy) / √(g·base_depth)` (라인 404) — CFL 기반 시간스텝.
- `afc1fe7`(2026-06-19)은 `if (calc_constants.grid_type == 2)`의 구면 시간간격 분기를 추가했다 (`afc1fe7:js/constants_load_calc.js:413–446`). [11-04 대조 정정]
- 이 분기는 셀 중심 위도와 `R_earth`를 사용한 최소 물리 간격으로 `dt`를 계산한다 (`js/constants_load_calc.js:472–484`). [11-04 대조 정정]
- 그 밖의 분기는 기존 직교 시간간격 식을 사용한다 (`js/constants_load_calc.js:485–487`). [11-04 대조 정정]
- 리미터: `TWO_THETA = 2·Theta` (405), `half_g = g/2` (406).
- 분산: `Bcoef_g = Bcoef·g` (407).
- 역격자: `g_over_dx/dy`, `one_over_dx/dy`, `one_over_d2x/d3x`(2·3차), `one_over_d2y/d3y`, `one_over_dxdy` (408-416) — 고차 미분 스텐실용.
- 건습: `delta = min(min_allowable_depth, base_depth/5000)`, `epsilon = delta²` (417-418).
- 경계: `boundary_nx/ny`, `reflect_x = 2·(WIDTH−3)`, `reflect_y`, `boundary_shift=4` (421-425).
- PCR 단계 수: `Px = ⌈log₂ WIDTH⌉`, `Py = ⌈log₂ HEIGHT⌉` (427-428) — 삼중대각 reduction 반복 횟수.
- **디스패치**: `ThreadX=ThreadY=16`, `DispatchX = ⌈WIDTH/16⌉`, `DispatchY = ⌈HEIGHT/16⌉` (493-496).
- 파일쓰기 간격 `n_write_interval`, ship 가우시안 계수 `ship_c1a..c3b` (489-491, 498-502), 퇴적물 fall velocity 등 (508-522).
- canvas 폭은 256바이트/행 정렬 위해 64의 배수로 올림 (`⌈WIDTH/64⌉·64`) — rgba 4채널이라 256/4=64 (라인 530-538).

> AB3·AM4 계수는 셰이더 계산식에 직접 적혀 있다 (`shaders/Pass3_Bous.wgsl:399–409`). [11-04 대조 정정]
> JavaScript는 `dt`와 단계 플래그를 uniform으로 전달한다 ([최종 근거 CD1-1333](../../../_staging/recovery/compare/Celeris-conclusion-verify-CD1h.md); `js/main.js:1083,1095,2672–2673,2806–2807`; `shaders/Pass3_Bous.wgsl:399–409`). [11-04 대조 정정] [11-04 전수 검증 보완]

---

## 5. 진단 (diagnostics)

평균·파고는 매 시간 단계에 갱신한다 (`js/main.js:2865–2872,2915–2925`). [11-04 대조 정정]
점 시계열 추출은 running average가 아니다 (`shaders/ExtractTimeSeries.wgsl:25–63`). [11-04 대조 정정]
f16·점 시계열은 프레임마다 계산한다 (`js/main.js:2980,3515`). [11-04 대조 정정]

### 5a. CalcMeans (`shaders/CalcMeans.wgsl`, `Handler_CalcMeans.js`)
입력 `txMeans/Means_Speed/Means_Momflux`(이전값) + `txH/U/V/C`(면) + `txBottom` + `txNewState`. 셀 평균 `h,u,v,c = (x+y+z+w)/4` 복원 (라인 43-46), `P=hu`, `Q=hv`, `speed`, `momflux=√(hu²²+hv²²)` 계산. 중앙차분으로 vorticity 산출 (라인 61-73).
- running mean: `means_new = means·(1−1/n) + state·(1/n)`, `n = n_time_steps_means` (라인 75-78).
- max 트래킹: u/v/speed/eta_max, hu²/hv²/momflux_max (n>1일 때, 라인 88-97).
- 출력: `txtemp_Means`(means), `txtemp_Means_Speed`(maxes), `txtemp_Means_Momflux`(mom maxes + |vort| 평균), `txModelVelocities=(u,v,eta,h)` (라인 99-102). 건셀은 `eta=−10·base_depth` placeholder (라인 55-57).
- 디스패치 후 `txtemp_Means*`를 `txMeans*`로 복사한다 (`js/main.js:2915–2920`). [11-04 대조 정정]
- `n_time_steps_means`는 매 시간 단계에 증가한다 (`js/main.js:2865–2872`). [11-04 대조 정정]

### 5b. CalcWaveHeight (`shaders/CalcWaveHeight.wgsl`, `Handler_CalcWaveHeight.js`)
입력 `txState`(η_old), `txNewState`(η_new), `txMeans`(η_mean), `txWaveHeight`(이전). η' = η_new − η_mean, `sum_eta2 += η'²` 누적 (n≤1이면 리셋) → `variance = Ση'²/n`, `σ=√variance` (라인 31-37).
- **H_mean = 2.829·σ** (RMS 파고), **H_sig = 4.000·σ** (유의파고) — Rayleigh 가정 (라인 39-41).
- 출력 `txtemp_WaveHeight = (Ση'², (H_sig−old)/old 상대변화, H_sig, H_mean)` (라인 42, 75). zero-crossing 분기는 주석처리됨.
- main.js는 `txstateUVstar`를 binding1(txState)로 넘긴다 (`js/main.js:1310`). [11-04 대조 정정]
- 디스패치 후 `txtemp_WaveHeight`를 `txWaveHeight`로 복사한다 (`js/main.js:2924–2931`). [11-04 대조 정정]
- `n_time_steps_waveheight`는 매 시간 단계에 증가한다 (`js/main.js:2865–2872`). [11-04 대조 정정]

### 5c. ExtractTimeSeries (`shaders/ExtractTimeSeries.wgsl`, `Handler_ExtractTimeSeries.js`)
**workgroup_size(1,1)**, 디스패치 폭 = `NumberOfTimeSeries + 1` (`js/main.js:3515`). 1D 텍스처 `txTimeSeries_Data`에 기록:
- idx 0 = **tooltip**: 마우스 위치의 `(bottom, η, Hs, friction)`. river_sim이면 `(bottom, η, speed, friction)`, disturbanceType>1이면 Hs 대신 `txMeans_Speed.w`(max η) (라인 31-54).
- idx ≥1 = **시계열 프로브**: `txTimeSeries_Locations`에서 격자좌표 읽어 `(time, η, P, Q)` 기록 (라인 55-61).
- readback: `readToolTipTextureData`가 1D 텍스처를 256B/행 버퍼로 `copyTextureToBuffer` → `mapAsync(READ)` → `timeSeriesData[i].{time,eta,P,Q}`에 push (`js/Time_Series.js:60-128`). `downloadTimeSeriesData`가 위치·시계열을 텍스트로 내보냄 (라인 128-171). 차트는 1초 간격 갱신 (`js/main.js:5488`).

본판은 배열을 동기 초기화하고 epoch로 이전 readback을 버린다 (`js/main.js:3467–3518`; `js/Time_Series.js:60–125`). [11-04 대조 정정]
transect 판은 `await buffer.mapAsync(GPUMapMode.READ);` 뒤에 배열을 초기화한다 (`transect_version/js/main.js:2151–2173,3404–3406`; `transect_version/js/Time_Series.js:57–112`). [11-04 대조 정정]
초기화 요청의 반복과 비동기 결과 반영 순서는 E 코드 결함 후보이며 강도는 중간이다 ([최종 근거 CT1-366](../../../_staging/recovery/compare/Celeris-conclusion-verify-CT1c.md)). [11-04 대조 정정]
본판 type5의 절대 시각 지원은 별도 판 차이다 ([최종 근거 CT1-366](../../../_staging/recovery/compare/Celeris-conclusion-verify-CT1c.md)). [11-04 대조 정정]

---

## 부록: 렌더 캐시 패킹
`shaders/Copytxf32_txf16.wgsl`가 매 프레임 f32 시뮬 텍스처 → `txRenderVarsf16`(3 layer, f16)로 패킹해 렌더 시 full rgba32float 샘플링 압력을 줄인다 (`js/main.js:2980`). 레이어 채널 의미·시각화는 `celeris-render` 참조.

문서와 코드 차이 표는 [celeris-webgpu-infrastructure-differences.md](celeris-webgpu-infrastructure-differences.md)에 있다.
