---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/Copytxf32_txf16.wgsl
lines: 50
sha256: dbf601f87d288374e55d5d68bee375a938e619c96f3defe606a4957b2394d720
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Copytxf32_txf16.wgsl — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | Globals의 격자·건조 임계치·기준 수심 필드를 선언한다. 계산 셰이더(compute shader)의 입력 텍스처(texture)와 rgba16float 배열 쓰기 텍스처는 group 0 binding 0–8에 있다. 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `delta: f32,` (4); `base_depth: f32,` (5); `@group(0) @binding(0) var<uniform> globals: Globals;` (8); `@group(0) @binding(1) var txNewState: texture_2d<f32>;` (10); `@group(0) @binding(2) var txBottom: texture_2d<f32>;` (11); `@group(0) @binding(3) var txMeans_Speed: texture_2d<f32>;` (12); `@group(0) @binding(4) var txRenderVarsf16: texture_storage_2d_array<rgba16float, write>;` (13); `@group(0) @binding(5) var txMeans_Momflux: texture_2d<f32>;` (14); `@group(0) @binding(6) var txModelVelocities: texture_2d<f32>;` (15); `@group(0) @binding(7) var txMeans: texture_2d<f32>;` (16); `@group(0) @binding(8) var txHardBottom: texture_2d<f32>;` (17) |
| 19–40 | 작업군 16×16에서 상태·바닥·최대 수면고·속도·평균 와도·고정 바닥을 읽는다. 건조 위치의 eta는 -10*base_depth로, foam은 0으로 바꾼다. 가용 깊이를 bottom-hard_bottom으로 계산한다. 원문: `@compute @workgroup_size(16, 16)` (19); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (20); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (21); `var eta = textureLoad(txNewState, idx, 0).r;` (23); `var foam = textureLoad(txNewState, idx, 0).a;` (24); `let bottom = textureLoad(txBottom, idx, 0).b;` (25); `let max_eta = textureLoad(txMeans_Speed, idx, 0).a;` (26); `if (eta - bottom < globals.delta) {` (27); `eta = -10.0 * globals.base_depth; // This is a placeholder for dry cells` (29); `foam = 0.0; // Reset foam for dry cells` (30); `let u = textureLoad(txModelVelocities, idx, 0).r;` (34); `let v = textureLoad(txModelVelocities, idx, 0).g;` (35); `let vort_mean = textureLoad(txMeans_Momflux, idx, 0).a;` (36); `let hard_bottom = textureLoad(txHardBottom, idx, 0).r;` (38); `let avaliable_depth = bottom - hard_bottom;` (39) 28행 주석의 설명과 달리 건조 분기는 `eta`와 `foam`만 바꾼다. 누락된 주석 원문: `// If the water depth is below the base depth, set velocities to zero` (28). [11-04 전수 검증 보완] |
| 41–50 | 시작 시 20행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 배열 텍스처 0층은 수면고·최대 수면고·바닥·거품, 1층은 속도·0·평균 와도, 2층은 바닥·고정 바닥·가용 깊이·0을 저장한다. 원문: `let output_layer0 = vec4<f32>(eta, max_eta, bottom, foam);` (42); `let output_layer1 = vec4<f32>(u, v, 0.0, vort_mean);` (43); `let output_layer2 = vec4<f32>(bottom, hard_bottom, avaliable_depth, 0.0);` (44); `textureStore(txRenderVarsf16, idx, 0, output_layer0);` (46); `textureStore(txRenderVarsf16, idx, 1, output_layer1);` (47); `textureStore(txRenderVarsf16, idx, 2, output_layer2);` (48) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16: txMeans는 바인딩에 선언하지만 main에서 읽지 않는다.
- 27–35: 건조 분기는 eta와 foam을 바꾸며 이후 읽는 u·v를 0으로 바꾸는 문장은 없다.
