---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/ExtractTimeSeries.wgsl
lines: 65
sha256: ad715033294a4640c0428c7ececdbdbcf7780547ae2f52d1b13d111b479f1091
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ExtractTimeSeries.wgsl — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | Globals의 격자·마우스 위치·시간·하천·교란 필드를 선언한다. 계산 셰이더(compute shader)의 uniform 및 입출력 텍스처(texture)는 group 0 binding 0–8이다. 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `dx: f32,` (4); `dy: f32,` (5); `mouse_current_canvas_indX: i32,` (6); `mouse_current_canvas_indY: i32,` (7); `time: f32,` (8); `river_sim: i32,` (9); `disturbanceType: i32` (10); `@group(0) @binding(0) var<uniform> globals: Globals;` (13); `@group(0) @binding(1) var txBottom: texture_2d<f32>;` (15); `@group(0) @binding(2) var txBottomFriction: texture_2d<f32>;` (16); `@group(0) @binding(3) var txContSource: texture_2d<f32>;` (17); `@group(0) @binding(4) var txState: texture_2d<f32>;` (18); `@group(0) @binding(5) var txWaveHeight: texture_2d<f32>;` (19); `@group(0) @binding(6) var txTimeSeries_Locations: texture_2d<f32>;` (20); `@group(0) @binding(7) var txTimeSeries_Data: texture_storage_2d<rgba32float, write>;` (21); `@group(0) @binding(8) var txMeans_Speed: texture_2d<f32>;` (22) |
| 25–44 | 작업군은 1×1이다. idx.x=0이면 마우스 위치의 툴팁(tooltip)을 만든다. 하천 모드에서는 수심 하한 0.01을 사용하여 두 유량으로 속력을 계산한다. 원문: `@compute @workgroup_size(1, 1)` (25); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (26); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (27); `var current_location = vec2<i32>(0, 0);` (29); `var output = vec4<f32>(0.0, 0.0, 0.0, 0.0);` (30); `if (idx.x == 0) { // for the first index in the texture, store the tooltip` (31); `current_location = vec2<i32>(globals.mouse_current_canvas_indX, globals.mouse_current_canvas_indY);` (32); `let bottom = textureLoad(txBottom, current_location, 0).z;` (33); `let friction = textureLoad(txBottomFriction, current_location, 0).x;   // friction factor, always between [0 and 1], no normalization needed` (34); `if (globals.river_sim == 1) {` (36); `let state = textureLoad(txState, current_location, 0).xyz;  // Free surface elevation, P, Q  LARIVER mod` (37); `let waves = state.x;` (38); `let H = max(waves - bottom, 0.01);` (39); `let u = state.y / H;` (40); `let v = state.z / H;` (41); `let speed = sqrt(u * u + v * v);` (42); `output = vec4<f32>(bottom, waves, speed, friction);` (43) |
| 45–65 | 시작 시 26행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록, 31행 `if (idx.x == 0) { // for the first index in the texture, store the tooltip` 블록 안. 하천 모드 이외에서는 disturbanceType>1일 때 최대 수면고, 그 외에는 유의파고를 툴팁에 넣는다. idx.x!=0이면 위치 텍스처의 좌표에서 시간·수면고·두 유량을 읽고 현재 출력 좌표에 저장한다. 원문: `let waves = textureLoad(txState, current_location, 0).x;  // Free surface elevation` (46); `var hsig = 0.0;` (47); `if (globals.disturbanceType > 1) {` (48); `hsig = textureLoad(txMeans_Speed, current_location, 0).w;  // Max free surface elevation` (49); `} else {` (50); `hsig = textureLoad(txWaveHeight, current_location, 0).z;  // Significant wave height` (51); `output = vec4<f32>(bottom, waves, hsig, friction);` (53); `} else {  // for all other indices, store the time series data` (55); `current_location = vec2<i32>(textureLoad(txTimeSeries_Locations, idx, 0).xy);` (56); `let waves = textureLoad(txState, current_location, 0).x;  // Free surface elevation` (57); `let P = textureLoad(txState, current_location, 0).y;  // x-flux` (58); `let Q = textureLoad(txState, current_location, 0).z;   // y-flux` (59); `output = vec4<f32>(globals.time, waves, P, Q);` (60); `textureStore(txTimeSeries_Data, idx, output);` (63) 45행 `else {`는 36행 `if (globals.river_sim == 1) {`의 반대 가지이다. 이 가지는 54행에서 닫힌다. 50행 `} else {`는 48행 `if (globals.disturbanceType > 1) {`의 반대 가지이다. 55행은 31행 조건의 반대 가지를 연다. 그 가지는 61행에서 닫힌다. `main`은 64행에서 닫힌다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17: txContSource는 선언하지만 실행 경로에서 읽지 않는다.
- 32–34·56–59: 마우스 위치와 저장된 표본 위치에 대한 clamp 또는 범위 검사 조건은 없다.
