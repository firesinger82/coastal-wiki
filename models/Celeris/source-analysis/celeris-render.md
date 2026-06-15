---
title: "Celeris-WebGPU 렌더링·시각화 — Copytxf32_txf16 + fragment/vertex3D + skybox"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/shaders/{Copytxf32_txf16,fragment,vertex,vertex3D,model.*,skybox.*}.wgsl + js/Handler_Render.js 직접 read. 라인 인용 소스 기준. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> 모델 정체·라이선스·canonical 선언은 [../README.md](../README.md). 본 노트는 **시각화 파이프라인** — 수치 적분(Pass0~3·TriDiag·Breaking·Boundary)을 **전혀 전진시키지 않는다**. solver가 생산한 텍스처를 GPU 위에서 그대로 읽어 화면으로 합성하는 렌더 경로만 다룬다. 수치 메커닉은 별도 source-analysis 노트 참조.

## 0. 왜 렌더가 Celeris 정체성인가

- README: "Real-Time Coastal Wave Simulation in the Browser" — solver와 visualization이 **동일 GPU·동일 브라우저**에 co-resident. 서버 없음, 추가 설치 없음 (`README.md:3,7`).
- "interactive frame rates", "Real-Time Visualization" + **Explorer 3D view** (`README.md:15,18`).
- 핵심: 렌더 fragment/vertex는 **시뮬레이션 텍스처를 직접 sample** — CPU 라운드트립 없음. `Handler_Render.js`의 `createRenderBindGroup`이 `txState·txBottom·txMeans·txWaveHeight·txBreaking·txRenderVarsf16` 등 **solver가 쓰는 그 텍스처들**을 바인딩한다 (`js/Handler_Render.js:179`).
- faster-than-real-time 비율은 UI에 노출 — `total_time / elapsedTime_update` (`js/display_parameters.js:63,103`).

## 1. 렌더 캐시 패킹 — Copytxf32_txf16

매 렌더 직전 1회 compute 패스. full-precision `rgba32float` 시뮬 텍스처 여러 장을 자주 샘플되는 변수만 골라 **단일 `rgba16float` 2D-array 텍스처**(`txRenderVarsf16`, 3 layer)로 packing. 목적: fragment/vertex3D가 적은 수의 텍스처만, 또 절반 대역폭(f16)으로 sample하게 해 렌더 압력 감소 (`docs/architecture/DATA_AND_TEXTURES.md:97-103`).

WGSL 본체 (`shaders/Copytxf32_txf16.wgsl`):

- 입력 바인딩: `txNewState`(1), `txBottom`(2), `txMeans_Speed`(3), `txMeans_Momflux`(5), `txModelVelocities`(6), `txMeans`(7), `txHardBottom`(8); 출력 storage `txRenderVarsf16`(4) (`:10-17`).
- dry-cell 처리: `eta - bottom < delta`이면 `eta = -10*base_depth`(placeholder), `foam=0` (`:27-31`).
- 패킹 레이아웃 (`:42-48`):
  - **layer 0** = `(eta, max_eta, bottom, foam)` — 자유수면·최대수면·해저·foam/tracer.
  - **layer 1** = `(u, v, 0, vort_mean)` — 유속 u·v·평균 vorticity.
  - **layer 2** = `(bottom, hard_bottom, available_depth, 0)` — `available_depth = bottom - hard_bottom`(세굴 가용심도).
- workgroup 16×16 (`:19`). JS 바인딩 매칭: `Handler_Copytxf32_txf16.js:90` (`txRenderVarsf16`는 `write-only rgba16float 2d-array`, `:43-47`).

fragment·vertex3D는 이후 `txRenderVarsf16`를 layer index로 sample (예: 유속은 layer 1, 세굴심도는 layer 2).

## 2. 2D 경로 — fragment.wgsl (928줄, 본체)

vertex는 fullscreen quad. `vertex.wgsl`은 4-vertex triangle-strip `[-1,1]²`를 만들고 `uv = pos*0.5+0.5` 전달 (`shaders/vertex.wgsl:9-17`). 모든 그림은 fragment에서.

### 2.1 Globals + 바인딩
`Globals` uniform에 colormap·scale·colorbar·boundary type·10종 design-component 마찰계수·`viewProj` 카메라행렬·arrow·linear-structure preview가 전부 들어감 (`shaders/fragment.wgsl:5-68`). 텍스처 바인딩 1~18: `etaTexture·bottomTexture·txMeans·txWaveHeight·txBaseline_WaveHeight·txBottomFriction·sed 3종·txDesignComponents·txOverlayMap·txDraw·sampler·txTimeSeries_Locations·txBreaking·txSamplePNGs(array)·linear sampler·txRenderVarsf16` (`:70-89`).

### 2.2 colormap 선택
`colorMap_choice` 0~6 → 16색 LUT: 0=blue-white waves, 1=parula, 2=turbo, 3=HSV, 4=gray, 5=pink, 6=haxby(bathy/topo) (`:147-274`). `colorMap_choice==0`이고 waves 모드일 때만 `photorealistic=1` 활성 (`:295`).

### 2.3 surfaceToPlot 분기 (그릴 변수 선택)
`surfaceToPlot` 0~23 대분기로 `render_surface` 결정 (`:293-382`). 주요:
- 0 waves(자유수면, layer0.r), 1 speed=√(u²+v²) (layer1.r/g), 2/3 u/v, 4 vorticity(중심차분, layer1) (`:298-329`).
- 5 breaking(`txBreaking.g`), 6 bathy(bottom), 7~11 mean η/speed/u/v/breaking(`txMeans`) (`:331-353`).
- 12 RMS Hwave, 13 significant Hs, 14 baseline 편차(`txWaveHeight`/baseline) (`:354-361`).
- 15 friction map, 16 max η(layer0.g), 17~21 sediment(농도·침식·가용세굴심도 layer2.b·심도변화), 22 design components, 23 mean |vort|(layer1.a) (`:362-382`).

label 텍스트 매핑은 JS측 `update_colorbar`의 `textMapping`에 동일 ID로 존재 (`js/Handler_Render.js:297-321`).

### 2.4 colormap 모드 vs photorealistic 모드
- **육지(dry)**: `bottom+delta >= waves` 이고 surfaceToPlot≠6 → slide-mass gray / `txOverlayMap`(GoogleMap) / sand+bathy 음영 중 택1 (`:576-587`).
- **colormap 모드**(`photorealistic==0`): `render_surface`를 `[minWave,maxWave]`로 정규화→16색 LUT 선형보간 (`:589-606`).
- **photorealistic 모드**(`:392-568, 608-731`): 물리기반 음영.
  - 미세 chop을 7방향×5파장 합성 사인파로 추가 (`calculateChangeEta`, `:92-120, 437-440`).
  - 중심차분으로 수면 법선→Phong (ambient 0.1 + diffuse 0.5 + specular 0.5, shininess 32). 광원 위치는 incoming-wave 경계방향에 따라 이동 (`:436-483`).
  - 깊이별 물색: deep(>50m)·shallow·sand 보간 (`:609-628`).
  - vorticity proxy로 sediment plume를 sand색으로 혼합 (`:485-508, 631`).
  - 회전류로 turbulence 텍스처(`txSamplePNGs` layer0)를 coarse+fine 2-scale로 흘려 거품·난류 질감 (`:531-564`).

### 2.5 design-component 텍스처 오버레이
photorealistic 경로에서 `txDesignComponents.r`를 floor→`component_index` 1~10 (coral·oyster·mangrove·kelp·grass·scrub·rubble·dune·berm·seawall). 각자 가시심도·마찰비례 edge mod·수면위/수중 텍스처(`txSamplePNGs` 해당 layer) 선택해 `component_frac`로 합성 (`:566-728`). mangrove(3)·grass~seawall(5~10)은 육상 허용 (`design_component_allowed_on_land`, `:574`).

### 2.6 arrows · breaking/tracer · time-series dots · colorbar (합성 후처리)
순서대로 `color_rgb` 위에 덮어쓴다:
- **velocity arrows** (`showArrows>=1`): 격자를 bin으로 나눠 bin중심 유속 sample→atan2 각도로 화살표 텍스처(`txSamplePNGs` layer9, photorealistic이면 filled layer10) 회전·합성 (`:736-792`).
- **breaking/tracer**: `showBreaking==1`이면 layer0.a × breaking_texture를 흰색 가산, `==2`면 tracer를 적색 가산 (`:795-801`).
- **linear-structure preview**: start/end UV에 검은 점, 선분 거리<0.0035에 검은 선 (`:804-852`).
- **time-series dots**: 최대 15색 팔레트, `txTimeSeries_Locations`의 좌표를 UV거리 비교해 점 찍음 (`:855-884`).
- **colorbar**: `CB_show==1`일 때 LUT 가로 띠 + 회색 배경, `txDraw`(JS canvas로 그린 tick·label·logo) 합성 (`:887-922`). `txDraw`는 `update_colorbar`가 OffscreenCanvas→`copyExternalImageToTexture`로 업로드 (`js/Handler_Render.js:266-381`).

## 3. 3D 경로 — vertex3D + scene props

### 3.1 vertex3D.wgsl — 수면 height field
정점 버퍼의 `pos`(vec2)를 `uv=pos*0.5+0.5`로 변환, `etaTexture.r`를 `textureLoad`로 읽어 elevation 취득, world좌표 `(uv.x·(W-1)·dx, uv.y·(H-1)·dy, elev·renderZScale)`를 `viewProj` 카메라행렬로 clip 변환 (`shaders/vertex3D.wgsl:71-85`). 즉 시뮬 수면을 그대로 3D 높이장 메시로 들어올린다. fragment는 2D `fragment.wgsl` 재사용(Explorer 3D view).

### 3.2 공유 bind group caveat
vertex3D의 `Globals`는 fragment와 동일 layout이며 `viewProj`까지 포함 (`vertex3D.wgsl:10-60`). `Handler_Render.js`의 단일 bind group layout이 vertex+fragment 양쪽에 쓰이므로 binding 0/1/2/13/17/18은 `VERTEX | FRAGMENT` 양쪽 visibility로 선언됨 (`js/Handler_Render.js:9,15,123,159,167`). → **2D fragment용처럼 보이는 바인딩(`etaTexture`, sampler, `txRenderVarsf16`)이라도 3D vertex가 height 샘플에 필요**하므로 둘을 같은 그룹에 묶어야 한다 (단일 render bind group 공유). 나머지 sed/overlay 텍스처는 fragment-only.

### 3.3 scene props (별도 파이프라인·별도 bind group)
2D 렌더 그룹과 무관, 자체 uniform 사용:
- **skybox**: `skybox.vertex.wgsl`이 fullscreen triangle을 inverse-VP로 unproject해 방향벡터 생성(Y/Z swap), fragment가 `texture_cube`를 sample (`shaders/skybox.vertex.wgsl:11-29`, `skybox.fragment.wgsl:3-11`). 바인딩: uniform invVP + cube + filtering sampler (`js/Handler_Skybox.js:5-30`).
- **model**(box facecolor): `model.vertex.wgsl`이 `viewProj·model`로 변환, fragment는 면별 gray로 음영 (`shaders/model.vertex.wgsl:16-22`, `model.fragment.wgsl:13-30`).
- **duck**: Y/Z swap으로 직립, world normal 계산 후 Lambert diffuse + albedo 텍스처 (`shaders/duck.vertex.wgsl:26-43`, `duck.fragment.wgsl:21-32`).

## 4. UI 연동 — display_parameters.js / Handler_Render.js

(수치적 비중 최소 — 표시·라벨링만)

- `displayCalcConstants` / `displaySimStatus`: NLSW/Bous, 시간스킴, dx·dy·격자수·Courant·dt·base_depth·경계타입·friction law를 패널에 텍스트 출력. **Faster-than-Realtime Ratio** 표시 (`js/display_parameters.js:24-105`).
- `displayTimeSeriesLocations`·`displaySlideVolume`·`ConsoleLogRedirection`: 프로브 좌표·슬라이드 체적·로그 미러링 (`:108-184`).
- render 파라미터(`surfaceToPlot`, `colorMap_choice`, `colorVal_min/max`, `showArrows`, `arrow_scale/density`, `CB_*`, `renderZScale` 등)는 `calc_constants`에서 uniform buffer로 업로드되어 fragment Globals로 전달 — UI 조작이 즉시 다음 프레임 렌더에 반영(라운드트립 없음). label 매핑은 `update_colorbar`의 `textMapping`이 surfaceToPlot ID와 1:1 (`js/Handler_Render.js:297-324`).
- `update_colorbar`: OffscreenCanvas 2D context에 colorbar 선·tick(5개)·수치 label·logo를 그려 `txDraw`로 업로드 (`:266-381`).

## 5. 요약 — 데이터 흐름

```
solver textures (rgba32float)
  txNewState, txBottom, txMeans*, txModelVelocities, txHardBottom
        │  Copytxf32_txf16 (compute, 1회/프레임)
        ▼
txRenderVarsf16 (rgba16float, 3 layer)  ← 렌더 캐시
        │
  ┌─────┴───────────────────────────┐
  ▼                                  ▼
fragment.wgsl (2D quad)        vertex3D.wgsl (height field)
 colormap/photoreal + design    → 동일 fragment.wgsl 재사용
 + arrows/breaking/dots/colorbar   + skybox/model/duck (별도 그룹)
        ▼
   canvas (no CPU roundtrip)
```

핵심: 모든 단계가 GPU 위에서 시뮬 텍스처를 직접 읽어 interactive·faster-than-real-time을 달성. 수치는 건드리지 않음.
