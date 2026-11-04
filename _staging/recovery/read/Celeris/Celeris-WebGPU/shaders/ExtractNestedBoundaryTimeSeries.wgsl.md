---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/ExtractNestedBoundaryTimeSeries.wgsl
lines: 53
sha256: 16ad04a725bc266ca79a4a30fea3b95ebdb8e7c0d46eb3af259cf889f6d5f904
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ExtractNestedBoundaryTimeSeries.wgsl — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | Globals는 원 격자 크기·추출 범위·방향별 지점 수·표본 번호를 i32로 선언한다. 계산 셰이더(compute shader)의 group 0 binding 0–6에는 uniform·상태·바닥 입력과 네 경계 출력 텍스처(texture)가 있다. 원문: `struct Globals {` (2); `width: i32,` (3); `height: i32,` (4); `i0: i32,` (5); `j0: i32,` (6); `i1: i32,` (7); `j1: i32,` (8); `nx: i32,` (9); `ny: i32,` (10); `sample_index: i32` (11); `@group(0) @binding(0) var<uniform> globals: Globals;` (14); `@group(0) @binding(1) var txState: texture_2d<f32>;` (15); `@group(0) @binding(2) var txNestedSouth: texture_storage_2d<rgba32float, write>;` (16); `@group(0) @binding(3) var txNestedNorth: texture_storage_2d<rgba32float, write>;` (17); `@group(0) @binding(4) var txNestedWest: texture_storage_2d<rgba32float, write>;` (18); `@group(0) @binding(5) var txNestedEast: texture_storage_2d<rgba32float, write>;` (19); `@group(0) @binding(6) var txBottom: texture_2d<f32>;` (21)  누락된 주석 원문: `// Added by Codex: Bottom elevation is needed so dry cells export zero eta/hu/hv instead of DEM elevation.` (20). [11-04 전수 검증 보완] |
| 23–35 | LoadState는 i·j를 원 격자 범위로 제한한다. 수심<=0이면 영벡터를 반환한다. 그 외에는 수면고와 두 유량 성분 및 0을 반환한다. 원문: `fn LoadState(i: i32, j: i32) -> vec4<f32> {` (23); `let safe_i = clamp(i, 0, globals.width - 1);` (24); `let safe_j = clamp(j, 0, globals.height - 1);` (25); `let state = textureLoad(txState, vec2<i32>(safe_i, safe_j), 0);` (26); `let bottom = textureLoad(txBottom, vec2<i32>(safe_i, safe_j), 0).z;` (28); `if (state.x - bottom <= 0.0) {` (29); `return vec4<f32>(0.0, 0.0, 0.0, 0.0);` (30); `return vec4<f32>(state.x, state.y, state.z, 0.0);` (33) |
| 36–53 | 작업군은 16×1이다. id.x를 지점 번호로 사용한다. nx·ny 조건을 각각 검사하고 남·북·서·동을 sample_index 행에 저장한다. 각 경계 상태는 LoadState로 읽는다. 원문: `@compute @workgroup_size(16, 1)` (36); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (37); `let station_index = i32(id.x);` (38); `let output_row = globals.sample_index;` (39); `if (station_index < globals.nx) {` (41); `let i = globals.i0 + station_index;` (42); `textureStore(txNestedSouth, vec2<i32>(station_index, output_row), LoadState(i, globals.j0));` (43); `textureStore(txNestedNorth, vec2<i32>(station_index, output_row), LoadState(i, globals.j1));` (44); `if (station_index < globals.ny) {` (47); `let j = globals.j0 + station_index;` (48); `textureStore(txNestedWest, vec2<i32>(station_index, output_row), LoadState(globals.i0, j));` (49); `textureStore(txNestedEast, vec2<i32>(station_index, output_row), LoadState(globals.i1, j));` (50) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–33: 건조 상태는 바닥 표고를 출력하지 않고 네 성분 모두 0을 반환한다.
- 39·43–50: 출력 행은 sample_index이며 이 셰이더에는 출력 행 상한 검사 조건이 없다.
