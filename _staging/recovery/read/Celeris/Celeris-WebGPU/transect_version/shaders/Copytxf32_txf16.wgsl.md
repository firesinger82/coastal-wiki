---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/Copytxf32_txf16.wgsl
lines: 35
sha256: d9a2dab3735133aa6b945b7da724e6cd1a75b8909ec608f3348f79f4ae03b67c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Copytxf32_txf16.wgsl — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 격자 크기 uniform과 입력 텍스처(texture) 6개, rgba16float 저장 배열 텍스처의 바인드 그룹(bind group) 0을 선언한다(1–14). 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `@group(0) @binding(0) var<uniform> globals: Globals;` (6); `@group(0) @binding(1) var txNewState: texture_2d<f32>;` (8); `@group(0) @binding(2) var txBottom: texture_2d<f32>;` (9); `@group(0) @binding(3) var txMeans_Speed: texture_2d<f32>;` (10); `@group(0) @binding(4) var txRenderVarsf16: texture_storage_2d_array<rgba16float, write>;` (11); `@group(0) @binding(5) var txMeans_Momflux: texture_2d<f32>;` (12); `@group(0) @binding(6) var txModelVelocities: texture_2d<f32>;` (13); `@group(0) @binding(7) var txMeans: texture_2d<f32>;` (14) |
| 17–35 | 계산 셰이더(compute shader)는 작업 그룹 16×16이다(17). 층 0에 수위·최대 수위·바닥·거품을 묶는다(21–25). 층 1에 u·v·0·평균 와도를 묶어 각각 배열 층 0·1로 저장한다(27–33). 원문: `@compute @workgroup_size(16, 16)` (17); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (18); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (19); `let eta = textureLoad(txNewState, idx, 0).r;` (21); `let foam = textureLoad(txNewState, idx, 0).a;` (22); `let bottom = textureLoad(txBottom, idx, 0).b;` (23); `let max_eta = textureLoad(txMeans_Speed, idx, 0).a;` (24); `let output_layer0 = vec4<f32>(eta, max_eta, bottom, foam);` (25); `let u = textureLoad(txModelVelocities, idx, 0).r;` (27); `let v = textureLoad(txModelVelocities, idx, 0).g;` (28); `let vort_mean = textureLoad(txMeans_Momflux, idx, 0).a;` (29); `let output_layer1 = vec4<f32>(u, v, 0.0, vort_mean);` (30); `textureStore(txRenderVarsf16, idx, 0, output_layer0);` (32); `textureStore(txRenderVarsf16, idx, 1, output_layer1);` (33) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2–3·14·17–34: width·height와 txMeans는 선언되어 있지만 본문의 실행식에서 사용되지 않는다. invocation 범위를 검사하는 조건도 없다.
