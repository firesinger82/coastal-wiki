---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/Pass0.wgsl
lines: 60
sha256: 21374e4db5643d212e96a8c980ee8fd543d2630b8c17b9ea8b6bb710cb8db160
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass0.wgsl — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | Globals의 필드와 자료형을 선언한다. 계산 셰이더(compute shader)의 group 0 binding 0–3은 uniform·상태·바닥 입력과 rgba32float 이웃 수심 출력 텍스처(texture)이다. 원문: `struct Globals {` (3); `width: i32,` (4); `height: i32,` (5); `epsilon: f32,` (6); `dt: f32,` (7); `base_depth: f32,` (8); `dx_global: f32,` (9); `dy_global: f32,` (10); `@group(0) @binding(0) var<uniform> globals: Globals;` (14); `@group(0) @binding(1) var txState: texture_2d<f32>;` (16); `@group(0) @binding(2) var txBottom: texture_2d<f32>;` (17); `@group(0) @binding(3) var txHnear: texture_storage_2d<rgba32float, write>;` (18) |
| 21–44 | 16×16 작업군에서 ±1 이웃 좌표를 격자 범위로 제한한다. 네 이웃의 수면고·바닥을 읽는다. 중심값을 읽는 문장은 주석 처리되어 있다. 원문: `@compute @workgroup_size(16, 16) //` (21); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (22); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (24); `let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` (27); `let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` (28); `let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));` (29); `let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));` (30); `let in_south = textureLoad(txState, downIdx, 0).x;` (34); `let in_north = textureLoad(txState, upIdx, 0).x;` (35); `let in_west = textureLoad(txState, leftIdx, 0).x;` (36); `let in_east = textureLoad(txState, rightIdx, 0).x;` (37); `let B_south = textureLoad(txBottom, downIdx, 0).z;` (40); `let B_north = textureLoad(txBottom, upIdx, 0).z;` (41); `let B_west = textureLoad(txBottom, leftIdx, 0).z;` (42); `let B_east = textureLoad(txBottom, rightIdx, 0).z;` (43)  누락된 주석 원문: `//    let in_here = textureLoad(txState, idx, 0).x;` (33);`//    let B_here = textureLoad(txBottom, idx, 0).z;` (39). [11-04 전수 검증 보완] |
| 45–60 | 시작 시 22행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 이웃별 수면고에서 바닥을 빼고 북·동·남·서 순서로 벡터에 담아 txHnear에 저장한다. 중심과의 min 대체식은 주석이다. 원문: `let h_south = in_south - B_south;` (46); `let h_north = in_north - B_north;` (47); `let h_west = in_west - B_west;` (48); `let h_east = in_east - B_east;` (49); `var h_vec = vec4<f32>(0.0, 0.0, 0.0, 0.0);` (51); `h_vec.x= h_north; //min(h_here, h_north);` (52); `h_vec.y= h_east; //min(h_here, h_east);` (53); `h_vec.z= h_south; //min(h_here, h_south);` (54); `h_vec.w= h_west; //min(h_here, h_west);` (55); `textureStore(txHnear, idx, h_vec);  //move this output texture to BC call, and keep the C calcs here` (57)  누락된 주석 원문: `//    let h_here = in_here.x - B_here;` (45). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–10: epsilon·dt·base_depth·dx_global·dy_global은 선언되어 있지만 main 계산식에서는 참조하지 않는다.
- 33·39·45·52–55: 중심 수심 계산과 중심 수심을 사용하는 min 식은 주석 처리되어 있다.
