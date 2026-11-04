---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/Update_neardry.wgsl
lines: 56
sha256: cf2496dc52c14edccf1a83ca6f1f2d7a706c3660a0d1bbc3532ce8343591d2fa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Update_neardry.wgsl — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 격자 크기 Globals와 바닥 읽기·저장 텍스처(texture)를 선언한다. 계산 셰이더(compute shader)는 바닥 네 성분을 읽는다. 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `@group(0) @binding(0) var<uniform> globals: Globals;` (6); `@group(0) @binding(1) var txBottom: texture_2d<f32>;` (8); `@group(0) @binding(2) var txtemp_bottom: texture_storage_2d<rgba32float, write>;` (9); `@compute @workgroup_size(16, 16)` (12); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (13); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (14); `var B_here = textureLoad(txBottom, idx, 0);` (16) |
| 18–36 | 시작 시 13행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 검사 반경 lengthCheck=3, w=99로 시작한다. y·x의 양 끝을 포함하는 이중 루프에서 좌표를 격자 범위로 제한한다. 반경 안 바닥이 0 이상이면 w=-99로 표시한다. 원문: `let lengthCheck = 3;    // check within three points` (19); `B_here.w = 99.;` (20); `for (var yy = idx.y - lengthCheck; yy <= idx.y + lengthCheck; yy += 1)` (21); `for (var xx = idx.x - lengthCheck; xx <= idx.x + lengthCheck; xx += 1) {` (23); `let xC = min(globals.width - 1, max(0, xx));` (24); `let yC = min(globals.height - 1, max(0, yy));` (25); `let idx_C = vec2<i32>(xC, yC);` (27); `let bathy_C = textureLoad(txBottom, idx_C, 0).z;` (28); `if (bathy_C >= 0.)` (29); `B_here.w = -99.;` (31) |
| 37–56 | 시작 시 13행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 현재 바닥이 양수이고 네 직교 이웃이 모두 음수이면 중심 z를 0으로 바꾼다. 위·오른쪽 면 성분은 북·동 바닥의 절반으로 바꾼다. 수정한 바닥을 저장한다. 원문: `let leftIdx = idx + vec2<i32>(-1, 0);` (38); `let rightIdx = idx + vec2<i32>(1, 0);` (39); `let downIdx = idx + vec2<i32>(0, -1);` (40); `let upIdx = idx + vec2<i32>(0, 1);` (41); `let B_south = textureLoad(txBottom, downIdx, 0).z;` (42); `let B_north = textureLoad(txBottom, upIdx, 0).z;` (43); `let B_west = textureLoad(txBottom, leftIdx, 0).z;` (44); `let B_east = textureLoad(txBottom, rightIdx, 0).z;` (45); `if(B_here.z > 0.){` (46); `if(B_south < 0.0 && B_north < 0.0 && B_west < 0.0 && B_east < 0.0) {` (47); `B_here.z = 0.0;` (48); `B_here.x = B_north / 2.0;` (49); `B_here.y = B_east / 2.0;` (50); `textureStore(txtemp_bottom, idx, B_here);` (54) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–35: near_dry 검사는 수위 텍스처 없이 바닥 높이의 부호만 사용한다. 반경 3은 상수이다.
- 24–25·38–45: 이중 루프의 좌표는 제한하지만 단일점 섬 검사의 네 이웃 좌표에는 별도 min/max가 없다.
- 20–35·46–50: w 검사는 섬의 z 수정 전에 수행한다. z 수정 뒤 w를 다시 계산하는 루프는 없다.
