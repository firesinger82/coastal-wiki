---
title: "Celeris-WebGPU 아키텍처·config 매뉴얼 노트 — 상류 docs/architecture + 원논문"
model: Celeris
citation_status: verified
verification_method: "models/Celeris/raw/source_code/Celeris-WebGPU/docs/architecture/*.md + ARCHITECTURE.md + REFERENCE_PAPERS.md 직접 read. 인용은 해당 doc 섹션 기준. PDF 원논문은 서지만. 2026-06-15."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-15
---

> **이 노트의 위치.** Celeris-WebGPU는 별도 PDF 사용자 매뉴얼이 없다. 대신 상류 저장소가 `docs/architecture/*.md`(아키텍처 docs)와 루트 `ARCHITECTURE.md`/`CLAUDE.md`를 사실상의(de-facto) 매뉴얼로 제공한다. 본 노트는 그 docs를 매뉴얼 스타일로 압축한 것이며, 모든 단언에 해당 doc 섹션을 인용한다. PDF 원논문(Tavakkol·Lynett, Lynett et al.)은 §4에 서지로만 정리한다(PDF 본문 미독).
> 관련: 모델 정체성·라이선스·공식 링크 → [../README.md](../README.md) · 공식 자료/논문 landing → [../web-refs/celeris-official-resources.md](../web-refs/celeris-official-resources.md) · 코드/텍스처 심화 → [../source-analysis/](../source-analysis/).

---

## 0. 개요 — config가 매뉴얼인 이유

Celeris-WebGPU에는 스키마 검증기·빌드 스텝·패키지 매니저가 없다(`ARCHITECTURE.md` 도입부; `CLAUDE.md` "No Build System"). 시뮬레이션 동작은 `js/constants_load_calc.js`의 기본 `calc_constants` 객체 + `examples/<Location>/config.json` 오버라이드 + JS에서 계산되는 **파생상수**로 전적으로 결정된다(`docs/architecture/CONFIGURATION.md` §Loading Order). 따라서 **`CONFIGURATION.md`가 사실상의 config-reference 매뉴얼**이며, 본 노트의 §1은 이를 파라미터 표로 정리한다.

---

## 1. Configuration reference (config.json)

### 1.1 로딩 순서 (CONFIGURATION.md §Loading Order)

1. `constants_load_calc.js`의 기본값으로 `calc_constants` 시작.
2. `loadConfig()`가 선택된 example `config.json` fetch.
3. `init_sim_parameters()`가 업로드/example 값을 기본값 위에 병합.
4. **파생값 재계산**: dispatch counts, timestep, Boussinesq 계수, 역(inverse) 격자간격, 경계 reflection 인덱스, canvas/render 치수, 퇴적물 계수, colorbar 레이아웃.
5. uniform 버퍼 갱신.

> **스키마 검증기 없음.** 미지(unknown) 키는 무시될 수 있고, 누락 키는 코드 경로가 읽으면 JS 기본값으로 fallback (CONFIGURATION.md §Loading Order). 루트 `config.json`은 `.gitignore` 처리됨 → 수동 테스트용 루트 config는 배포·커밋 안 됨; 정상 시나리오 정의는 `examples/` 내부 (CONFIGURATION.md §Root Config Note; CLAUDE.md §.gitignore).

### 1.2 직접 로드 필드 (편집 대상) — CONFIGURATION.md §Important Config Families

| 패밀리 | 필드 | 의미 / 비고 |
|---|---|---|
| 격자·시간 | `WIDTH`, `HEIGHT` | 격자 셀 수 |
| | `dx`, `dy` | 격자 간격 |
| | `Courant` | CFL 안정 한계 계수 (dt 산출 입력) |
| | `dt` | 시간 스텝 (보통 파생; §1.4) |
| | `ThreadX`, `ThreadY` | workgroup 크기 (보통 16×16) |
| | `DispatchX`, `DispatchY` | 디스패치 카운트 (파생; §1.4) |
| 물리·수치 | `NLSW_or_Bous` | 지배방정식 모드 플래그 (§1.3) |
| | `Accuracy_mode` | 표준 vs 고차(high-order) 재구성 경로 선택 (§1.3) |
| | `timeScheme` | 시간적분 스킴 (§1.3, §1.5) |
| | `TWO_THETA` | minmod limiter 파라미터 (2θ) |
| | `Bcoef`, `Bcoef_g`, `Bous_alpha` | Boussinesq 분산(dispersion) 계수 |
| | `gravity` | 중력 가속도 g |
| | `friction`, `isManning` | 바닥 마찰계수 / Manning 식 사용 여부 |
| | `useBreakingModel` | 쇄파 모델 on/off |
| | `delta`, `epsilon`, `base_depth` | wet/dry δ, ε, 기준 수심 |
| 경계·forcing | `west/east/south/north_boundary_type` | 사방 경계 타입 |
| | `BoundaryWidth` | 스펀지/경계 폭 |
| | `incident_wave_type` | 입사파 모드: `0`=단일 sine, `1`=TMA 방향 스펙트럼 |
| | `incident_wave_H`, `incident_wave_T`, `incident_wave_direction` | 파고 H·주기 T·방향(deg) |
| | `numberOfWaves` | 파 성분 수 (type=0이면 1, type=1이면 생성 성분 수) |
| | river stage/discharge | 홍수 시나리오용 하천 stage/유량 |
| 퇴적물 | `useSedTransModel` | 퇴적물 수송 모델 on/off |
| | `sedC1_shields`, `sedC1_criticalshields`, `sedC1_erosion` | Shields·임계Shields·침식 |
| | `sedC1_fallvel`, `sedC1_n`, `sedC1_bedloadMPM` | 침강속도·공극률·MPM bedload |
| | `sedTurbDispersion`, `sedBreakingDispersionCoef` | 난류·쇄파 분산 계수 |
| 렌더·상호작용 | `surfaceToPlot` | 표시할 표면 변수 |
| | `colorMap_choice`, `colorVal_min`, `colorVal_max` | 컬러맵·범위 |
| | `GoogleMapOverlay`, `IsOverlayMapLoaded` | 지도 오버레이 |
| | `renderZScale` | 수직 과장(z scale) |
| | `showArrows`, `arrow_scale`, `arrow_density` | 속도 화살표 |
| | design-component friction 상수 | 방재 구조물 마찰 |

> 입사파 처리 (CONFIGURATION.md §Important Config Families 끝): `incident_wave_type==0`이면 `main.js`가 UI 값을 단일 sine 성분으로 취급 — 파고→진폭 `H/2`, 방향 deg→rad, `numberOfWaves=1`, `txWaves` 재업로드. `==1`이면 `Wave_Generator.js`가 동일 H·T·방향 컨트롤로 캐시된 **TMA 방향 스펙트럼** 생성, `numberOfWaves`=생성 성분 수, `txWaves` 재업로드.

### 1.3 모드 플래그 (분기 결정) — SIMULATION_PIPELINE.md §Active Shader Selection

`main.js`는 config에 따라 다른 WGSL 파일을 fetch·컴파일한다:

| 플래그 | 값 | 활성 셰이더 / 경로 |
|---|---|---|
| `Accuracy_mode` (표준) | — | `Pass1.wgsl`, `Pass2.wgsl` |
| `Accuracy_mode` (고차) | — | `Pass1_HighOrder.wgsl`, `Pass2_HighOrder_HLLC.wgsl` (현 고차 경로는 HLLC 선택) |
| `NLSW_or_Bous` = NLSW | — | `Pass3_NLSW.wgsl`, **PCR 솔브 생략** (중간상태를 `txNewState`로 복사) |
| `NLSW_or_Bous` = Boussinesq | — | `Pass3_Bous.wgsl` + `Update_TriDiag_coef.wgsl` + `TriDiag_PCRx.wgsl` + `TriDiag_PCRy.wgsl` |
| `NLSW_or_Bous` = COULWAVE | — | `Pass3A/3B/3_COULWAVE.wgsl` + `Update_TriDiag_coef_COULWAVE.wgsl` + `TriDiag_PCRx/y_COULWAVE.wgsl` |

(SIMULATION_PIPELINE.md §Active Shader Selection — 플래그의 정확한 정수값은 doc에 미기재; 분기 효과만 명시. 일부 셰이더 파일은 실험·구버전이므로 수정 전 현 `main.js` 경로 검증 필요.)

### 1.4 파생상수 (직접 편집 금지) — CONFIGURATION.md §Derived Values

`init_sim_parameters()`가 로딩 후 계산하며, UI 변경이 재계산을 트리거하면 매번 덮어쓸 수 있음.

| 파생값 | 산출 입력 |
|---|---|
| `dt` | 격자 간격, `gravity`, `base_depth`, Courant 계열 설정 |
| `DispatchX`/`DispatchY` | 격자 크기 ÷ workgroup 크기 |
| `Px`/`Py` | PCR 반복 횟수 |
| `one_over_d2x`, `one_over_d3x`, `one_over_dxdy` | 역 격자간격 및 그 거듭제곱 |
| 경계 reflection/shift 인덱스 | 경계 타입·폭 |
| render/canvas 비율, colorbar 좌표 | 격자·캔버스 치수 |
| 퇴적물 settling/erosion 계수 | 설정된 물성치 |

> **디버깅 팁** (CONFIGURATION.md §Derived Values 끝): 시나리오가 이상하면 해당 값이 JSON 직접 로드인지 로딩 후 파생인지 확인. 후자는 UI 변경마다 덮어쓰일 수 있음.

### 1.5 Adams-Bashforth 시간적분 — SIMULATION_PIPELINE.md §Time Integration

| `timeScheme` / `pred_or_corrector` | 동작 |
|---|---|
| `timeScheme == 0` | 단일 스텝 explicit 업데이트 |
| `timeScheme != 0`, `pred_or_corrector == 1` | Adams-Bashforth 스타일 **predictor** — 현재·old·older 도함수 사용 |
| `pred_or_corrector == 2` | **corrector** — 새 도함수 + predictor + history 도함수 결합 |

물·퇴적물 경로 모두 gradient-history 텍스처 유지. Boussinesq/COULWAVE 모드는 추가로 `F_G_star` history 텍스처가 `Pass3`용 분산 helper 항을 보존 (SIMULATION_PIPELINE.md §Time Integration).

### 1.6 Uniform 커플링 (편집 시 주의) — CONFIGURATION.md §Uniform Coupling

각 WGSL은 자신이 필요한 값만 담은 `Globals` struct를 선언; JS의 uniform-buffer 패킹 로직(`main.js`)이 채운다. 커플링은 **positional·byte-layout 민감** — 셰이더 `Globals`에 필드 추가 시 대응 JS 버퍼 writer도 갱신 필요. 같은 config 값(`delta`, `base_depth`, 격자 치수, 역 격자간격 등)이 hydrodynamic·sediment·boundary·render·tridiagonal 여러 셰이더 struct에 중복 등장.

---

## 2. 텍스처·데이터 계약 요약 (DATA_AND_TEXTURES.md)

> 심화(채널 의미·PCR ping-pong·COULWAVE grouping 레이어)는 [../source-analysis/](../source-analysis/) 인프라 노트 참조. 여기서는 요약만.

시뮬레이션은 **텍스처 중심**: 전통 모델의 CPU 행렬이 여기선 WebGPU 텍스처 (DATA_AND_TEXTURES.md 도입부). 핵심 텍스처:

| 텍스처 | 역할 (채널) |
|---|---|
| `txState` / `txNewState` | 주 수면상태 — `r`=수면고, `g`=x운동량(P/hu), `b`=y운동량(Q/hv), `a`=스칼라(foam/tracer) (§State Textures) |
| `txstateUVstar` / `current_stateUVstar` | 암시적 분산 솔브용 중간상태. NLSW는 통과 복사, Bous/COULWAVE는 PCR RHS/해 (§State Textures) |
| `txBottom` | 지형·wet/dry — `r`=북면, `g`=동면, `b`=셀중심 bed고, `a`=near-dry 플래그 (§Bathymetry) |
| `txBottomInitial` / `txHardBottom` | 시작 bed 보존(이동바닥·누적 bed-change용) / 비침식 하한 (§Bathymetry) |
| `txH`/`txU`/`txV`/`txC` | `Pass1` 면(face) 재구성 — 깊이/x속도/y속도/스칼라. 채널 `x/y/z/w`=북/동/남/서 면 (§Face Reconstruction; **x=북, y=동 주의**) |
| `txXFlux`/`txYFlux` | `Pass2` 수치 플럭스 — `x`=질량, `y`=x운동량, `z`=y운동량, `w`=스칼라 (§Flux) |
| `txXFlux_Sed`/`txYFlux_Sed` | 퇴적물 플럭스(클래스당 1채널; 현재 주로 class 1, 레이아웃은 4클래스 여유) (§Flux) |
| `txBreaking` | 쇄파 — `x`=시작/age, `y`=eddy viscosity, `z`=front/intensity, `w`=Smagorinsky placeholder (§Breaking) |
| `txDissipationFlux` | viscosity-가중 운동량 gradient (`Pass3_Bous`/`Pass3_COULWAVE` 쇄파 확산) (§Breaking) |
| `coefMatx/y`, `newcoef_x/y`, `txtemp_PCRx/y`, `txtemp2_PCRx/y` | PCR 삼중대각 계수·해 텍스처(채널 `r/g/b/a`=하/대각/상/RHS) (§Tridiagonal) |
| `txCW_groupings` | COULWAVE 3D `rgba32float`, 6 레이어로 중간장 패킹 (§COULWAVE Grouping) |
| `txRenderVarsf16` | `rgba16float` 2D-array 렌더 캐시(3 레이어) — 풀 `rgba32float` 샘플 압박 완화 (§Render) |
| `txScreen`/`txDraw`/`txOverlayMap`/`txSamplePNGs`/`txCube_Skybox` | 화면·캔버스 오버레이·지도·자산·skybox (§Render) |
| `txTimeSeries_Locations` / `txTimeSeries_Data` | 프로브 좌표 / 샘플값(elem 0=tooltip, 1..N=시계열) (§Time Series) |

> **PCR 솔버 변경점** (DATA_AND_TEXTURES.md §Tridiagonal): 현 솔버는 매 솔브 전 `coefMat*`→`newcoef_*` 복사나 반복 후 `txtemp_PCR*`→`newcoef_*` 복사를 **더 이상 하지 않음**. JS가 현재 계수 텍스처를 읽고 다음 것을 쓰는 bind group을 선택(ping-pong).

---

## 3. WebGPU 바인딩 패턴 계약 (WEBGPU_BINDING_PATTERN.md)

> **핵심 규칙: binding 번호가 곧 인터페이스.** 핸들러의 순서가 WGSL `@group(0) @binding(N)` 선언과 일치해야 하고, `main.js`가 넘기는 리소스가 핸들러 기대와 일치해야 함 (§도입부).

**3계층 커플링**(handler ↔ bind group ↔ shader):

1. **핸들러**(`Handler_*.js`): `create_*_BindGroupLayout(device)` + `create_*_BindGroup(...)` 정의 + JS 텍스처/버퍼 인자를 번호 바인딩에 매핑. 디스패치는 보통 안 함 — `Run_Compute_Shader.js`/`Run_Tridiag_Solver.js`/`main.js` 렌더가 담당 (§Handler Responsibilities).
2. **셰이더**(WGSL): 매칭 `Globals` struct + 매칭 텍스처/스토리지 바인딩 선언. 모든 텍스처는 config 함의 치수; 스토리지 출력은 샘플 입력과 분리(임시 텍스처 후 복사 예외); workgroup 보통 16×16 (§Shader Responsibilities).
3. **임시 텍스처 패턴**: WebGPU는 한 패스에서 같은 텍스처 read+write 불가 → `txtemp_boundary`, `txtemp_Breaking`, `txtemp_bottom`, `txtemp_PCRx`, `txtemp_WaveHeight` 등에 쓴 뒤 canonical 텍스처로 복사. `BoundaryPass`, `Pass_Breaking`, `CalcMeans`/`CalcWaveHeight`, PCR 솔버에서 특히 두드러짐 (§Why Temporary Textures).

**공유 레이아웃** (§Shared Layouts): `Handler_Pass1`(표준+고차), `Handler_Pass2`(표준/HLLC/HLLEM), `Handler_Pass3`(NLSW/Bous/COULWAVE — 셋 다 동일 broad 레이아웃), `Handler_Tridiag`(표준+COULWAVE; 표준 WGSL은 일부 바인딩 미사용), `Handler_UpdateTrid`(표준+COULWAVE). → **미사용 리소스도 호환성 계약의 일부로 취급**.

> **함정** (§Stale Comments): 여러 핸들러 주석이 compute인데 "fragment shader"라 표기; 헤더가 다른 핸들러에서 복붙된 경우 있음. **주석 말고 바인딩 선언 + 현 `main.js` 호출 경로를 신뢰.** 초기 렌더 bind group은 현 19-binding 시그니처; 일부 overlay-refresh 코드는 구버전 인자셋 사용.

**안전 변경 체크리스트** (§Safe Change Checklist) — 셰이더 변경: ① 셰이더 `@binding` 목록 → ② 매칭 `Handler_*.js` 레이아웃 → ③ `main.js`의 모든 `create_*_BindGroup()` 호출 → ④ `Create_Textures.js` 포맷 → ⑤ 디스패치 후 copy → ⑥ 채널 의미 docs. 신규 config/uniform: ① `constants_load_calc.js` 기본값 → ② 파생계산 → ③ JS uniform writer → ④ WGSL `Globals` 올바른 byte 위치 → ⑤ 영향받는 파이프라인/bind group 재생성.

---

## 4. 참조 논문 (REFERENCE_PAPERS.md + docs/ PDF 서지)

PDF 본문은 미독; 아래 서지·연결은 REFERENCE_PAPERS.md(코드 lineage 가이드) 및 PDF 파일명 기준.

### 4.1 서지

- **Tavakkol, S. & Lynett, P. (2017).** *Celeris: A GPU-accelerated open source software with a Boussinesq-type wave solver for real-time interactive simulation and visualization.* Computer Physics Communications **217**, 117–127.
  - PDF: `docs/Tavakkol_2017_Celeris_GPU_accelerated_Computer_Physics_Communications.pdf`
- **Tavakkol, S. & Lynett, P. (2020).** *Celeris Base: An interactive and immersive Boussinesq-type nearshore wave simulation software.* Computer Physics Communications.
  - PDF: `docs/Tavakkol_2020_Celeris_Base_interactive_Computer_Physics_Communications.pdf`
- **Tavakkol, S. & Lynett, P. (2019).** *Adaptive third-order Adams-Bashforth time stepping scheme for 2D extended Boussinesq equations.* arXiv:1909.04153.
  - (REFERENCE_PAPERS.md에 별도 절은 없으나 §1.5 Adams-Bashforth predictor/corrector 시간스킴의 학술 근거; 저장소 docs/에 PDF 미포함, arXiv landing은 [../web-refs/celeris-official-resources.md](../web-refs/celeris-official-resources.md) 참조)
- **Lynett, P. et al. (2026).** *An interactive nearshore wave simulator for rapid design prototyping and natural hazard education.*
  - PDF: `docs/lynett-et-al-2026-an-interactive-nearshore-wave-simulator-for-rapid-design-prototyping-and-natural-hazard-education.pdf`

### 4.2 어느 스킴/방정식이 어느 논문에 추적되는가 (REFERENCE_PAPERS.md)

| 논문 | 코드 연결 (REFERENCE_PAPERS.md 해당 절) |
|---|---|
| **Lynett et al. 2026** (WebGPU) | 현 저장소 아키텍처의 근거: 정적 웹앱·서버측 compute 없음·빌드 스텝 없음·WGSL compute. NLSW/Boussinesq/고차(COULWAVE) 지원. **하이브리드 FV/FD 전략**(쌍곡선부=FV 플럭스, 분산항=FD+암시적 솔브). 상호작용성(bathy 편집·disturbance·design components·지도·시계열)이 설계 일부 (§Lynett Et Al. 2026) |
| **Tavakkol & Lynett 2017** | GPU 가속 Boussinesq의 개념적 조상. explicit FV 업데이트 ↔ 분산 Boussinesq 보정 분리, **이동 shoreline/wet-dry 로직 중심**, 암시적 분산 솔브의 삼중대각=**PCR(Parallel Cyclic Reduction)**, 상호작용 시각화·빠른 피드백이 핵심 목표 (§Tavakkol And Lynett 2017) |
| **Tavakkol & Lynett 2020** (Celeris Base) | 상호작용 모델을 접근성 높은 앱 환경으로 이동, 지도 오버레이·게이지·몰입형 시각화 강조. WebGPU 버전이 정적 브라우저앱으로 그 정신 계승; `main.js`·`File_Loader.js`·`File_Writer.js`·렌더 셰이더의 UI/오버레이/시계열/export가 이 워크플로 방향 (§Tavakkol And Lynett 2020) |
| **2019 arXiv 1909.04153** | §1.5의 적응형 3차 Adams-Bashforth predictor/corrector 시간적분의 학술적 출처 |

### 4.3 권장 읽기 순서 (REFERENCE_PAPERS.md §Practical Reading Order)

- **수치 커널 수정 시**: WebGPU 논문(현 아키텍처) → 초기 Celeris 논문(Boussinesq/PCR·wet-dry lineage) → `SIMULATION_PIPELINE.md` → `docs/source/shaders/` 셰이더 docs.
- **UI/시각화/시나리오 로딩 수정 시**: WebGPU 논문(브라우저 모델) → 2020 Celeris Base 논문(워크플로 맥락) → `main.js`·`File_Loader.js`·`File_Writer.js`·`Handler_Render.js`·`fragment.wgsl`·`Copytxf32_txf16.wgsl` docs.

---

## 5. 한 줄 요약

config.json은 `constants_load_calc.js` 기본 + example 오버라이드 + JS 파생상수(dt·dispatch·Bous계수·역격자간격)로 결정되며 스키마 검증 없음; 모드는 `NLSW_or_Bous`/`Accuracy_mode`/`timeScheme`(+`pred_or_corrector`로 AB predictor/corrector) 플래그가 활성 WGSL 경로를 분기한다. 모든 패스는 handler↔bind group(@binding 번호)↔shader 3계층 positional 계약으로 묶이고, 수치 lineage는 Boussinesq/PCR/wet-dry(Tavakkol&Lynett 2017·2020), 3차 AB(2019), WebGPU 정적웹앱 아키텍처(Lynett et al. 2026)로 추적된다.
