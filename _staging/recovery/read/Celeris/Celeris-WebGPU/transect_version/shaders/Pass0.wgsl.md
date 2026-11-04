---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/Pass0.wgsl
lines: 60
sha256: ed65f49e8775f87377efa08fa75b423a0b2cd69e3adf806b129953656dc3e1a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass0.wgsl — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 격자 크기·epsilon·dt·수심·격자 간격 uniform을 선언한다(3–11). 바인드 그룹(bind group) 0은 상태·바닥 입력 텍스처(texture)와 rgba32float 수심 출력을 연결한다(14–18). 원문: `// Define structures and bindings` (1); `struct Globals {` (3); `width: i32,` (4); `height: i32,` (5); `epsilon: f32,` (6); `dt: f32,` (7); `base_depth: f32,` (8); `dx_global: f32,` (9); `dy_global: f32,` (10); `@group(0) @binding(0) var<uniform> globals: Globals;` (14); `@group(0) @binding(1) var txState: texture_2d<f32>;` (16); `@group(0) @binding(2) var txBottom: texture_2d<f32>;` (17); `@group(0) @binding(3) var txHnear: texture_storage_2d<rgba32float, write>;` (18) |
| 21–50 | 계산 셰이더(compute shader)는 작업 그룹 16×16이다(21). 동·서 이웃 좌표는 영역 끝으로 제한한다(27·29). 각 이웃에서 수위와 바닥을 읽어 수심을 계산한다(36–49). 남·북 관련 문장은 주석이다. 원문: `@compute @workgroup_size(16, 16) //` (21); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (22); `// Convert the 3D thread ID to a 2D grid coordinate` (23); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (24); `// Compute the coordinates of the neighbors for each pixel, and enforce boundary conditions` (26); `let rightIdx = min(idx + vec2<i32>(1, 0), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` (27); `//    let upIdx = min(idx + vec2<i32>(0, 1), vec2<i32>(i32(globals.width)-1, i32(globals.height)-1));` (28); `let leftIdx = max(idx + vec2<i32>(-1, 0), vec2<i32>(0, 0));` (29); `//    let downIdx = max(idx + vec2<i32>(0, -1), vec2<i32>(0, 0));` (30); `// Read in the state of the water at this pixel and its neighbors` (32); `//    let in_here = textureLoad(txState, idx, 0).x;` (33); `//    let in_south = textureLoad(txState, downIdx, 0).x;` (34); `//    let in_north = textureLoad(txState, upIdx, 0).x;` (35); `let in_west = textureLoad(txState, leftIdx, 0).x;` (36); `let in_east = textureLoad(txState, rightIdx, 0).x;` (37); `//    let B_here = textureLoad(txBottom, idx, 0).z;` (39); `//    let B_south = textureLoad(txBottom, downIdx, 0).z;` (40); `//    let B_north = textureLoad(txBottom, upIdx, 0).z;` (41); `let B_west = textureLoad(txBottom, leftIdx, 0).z;` (42); `let B_east = textureLoad(txBottom, rightIdx, 0).z;` (43); `//    let h_here = in_here.x - B_here;` (45); `//    let h_south = in_south - B_south;` (46); `//    let h_north = in_north - B_north;` (47); `let h_west = in_west - B_west;` (48); `let h_east = in_east - B_east;` (49) |
| 51–60 | 시작 시 22행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. main은 h_vec의 북·남 성분을 0으로 정하고 동·서 성분에 이웃 수심을 넣는다(51–55). txHnear에 저장하고 종료한다(57–60). 원문: `var h_vec = vec4<f32>(0.0, 0.0, 0.0, 0.0);` (51); `h_vec.x= 0.0; //h_north; //min(h_here, h_north);` (52); `h_vec.y= h_east; //min(h_here, h_east);` (53); `h_vec.z= 0.0; //h_south; //min(h_here, h_south);` (54); `h_vec.w= h_west; //min(h_here, h_west);` (55); `textureStore(txHnear, idx, h_vec);  //move this output texture to BC call, and keep the C calcs here` (57) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–10: epsilon·dt·base_depth·dx_global·dy_global은 선언 이후 실행식에서 사용되지 않는다.
- 28–55: 남·북 이웃 판독과 수심 계산은 주석이다. h_vec.x·h_vec.z에는 0.0을 대입한다.
