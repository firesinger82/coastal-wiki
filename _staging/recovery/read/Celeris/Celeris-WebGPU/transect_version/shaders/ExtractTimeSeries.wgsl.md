---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/ExtractTimeSeries.wgsl
lines: 58
sha256: 1ce20e716308a9fe0f0340cc627db03ad565acc96ffc3d4bdaf2bdd94e873056
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ExtractTimeSeries.wgsl — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | Globals는 격자·마우스 위치·시간·하천 모드를 선언한다(1–10). 바인드 그룹(bind group) 0은 바닥·마찰·상태·파고·시계열 위치 입력 텍스처(texture)와 rgba32float 출력을 연결한다(12–20). 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `dx: f32,` (4); `dy: f32,` (5); `mouse_current_canvas_indX: i32,` (6); `mouse_current_canvas_indY: i32,` (7); `time: f32,` (8); `river_sim: i32,` (9); `@group(0) @binding(0) var<uniform> globals: Globals;` (12); `@group(0) @binding(1) var txBottom: texture_2d<f32>;` (14); `@group(0) @binding(2) var txBottomFriction: texture_2d<f32>;` (15); `@group(0) @binding(3) var txContSource: texture_2d<f32>;` (16); `@group(0) @binding(4) var txState: texture_2d<f32>;` (17); `@group(0) @binding(5) var txWaveHeight: texture_2d<f32>;` (18); `@group(0) @binding(6) var txTimeSeries_Locations: texture_2d<f32>;` (19); `@group(0) @binding(7) var txTimeSeries_Data: texture_storage_2d<rgba32float, write>;` (20) |
| 23–47 | 계산 셰이더(compute shader)는 작업 그룹 1×1이다(23). x 인덱스가 0이면 마우스 위치의 툴팁 값을 만든다(29–47). 하천 모드는 수심을 0.01 이상으로 제한해 속력을 계산하고, 나머지는 유의파고를 읽는다. 원문: `@compute @workgroup_size(1, 1)` (23); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (24); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (25); `var current_location = vec2<i32>(0, 0);` (27); `var output = vec4<f32>(0.0, 0.0, 0.0, 0.0);` (28); `if (idx.x == 0) { // for the first index in the texture, store the tooltip` (29); `current_location = vec2<i32>(globals.mouse_current_canvas_indX, globals.mouse_current_canvas_indY);` (30); `let bottom = textureLoad(txBottom, current_location, 0).z;` (31); `let friction = textureLoad(txBottomFriction, current_location, 0).x;   // friction factor, always between [0 and 1], no normalization needed` (32); `if (globals.river_sim == 1) {` (34); `let state = textureLoad(txState, current_location, 0).xyz;  // Free surface elevation, P, Q  LARIVER mod` (35); `let waves = state.x;` (36); `let H = max(waves - bottom, 0.01);` (37); `let u = state.y / H;` (38); `let v = state.z / H;` (39); `let speed = sqrt(u * u + v * v);` (40); `output = vec4<f32>(bottom, waves, speed, friction);` (41); `else {` (43); `let waves = textureLoad(txState, current_location, 0).x;  // Free surface elevation` (44); `let hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height` (45); `output = vec4<f32>(bottom, waves, hsig, friction);` (46) |
| 48–58 | 시작 시 24행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 48행의 `}`는 29행 `if (idx.x == 0) {` 가지를 닫는다. 같은 행의 else는 그 조건이 거짓인 가지를 연다. else 가지는 54행 `}`에서 닫힌다. main의 29행 조건 불성립 else에서 위치 텍스처로부터 좌표를 읽어 시간·수위·x/y 유량을 출력한다(48–54). 툴팁과 시계열은 같은 출력 텍스처의 idx에 저장한다(56). 원문: `} else {  // for all other indices, store the time series data` (48); `current_location = vec2<i32>(textureLoad(txTimeSeries_Locations, idx, 0).xy);` (49); `let waves = textureLoad(txState, current_location, 0).x;  // Free surface elevation` (50); `let P = textureLoad(txState, current_location, 0).y;  // x-flux` (51); `let Q = textureLoad(txState, current_location, 0).z;   // y-flux` (52); `output = vec4<f32>(globals.time, waves, P, Q);` (53); `textureStore(txTimeSeries_Data, idx, output);` (56) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16: txContSource는 선언 이후 참조되지 않는다.
- 29·48–56: 툴팁 선택 조건은 idx.x == 0이다. idx.y에 대한 툴팁 선택 조건은 없다.
