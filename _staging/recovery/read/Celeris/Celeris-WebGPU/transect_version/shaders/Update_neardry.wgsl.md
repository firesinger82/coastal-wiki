---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/Update_neardry.wgsl
lines: 58
sha256: 48117923c0c934126ac45157146bbbf4485d8f63de5e98b1b7cb42d694ba5b50
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Update_neardry.wgsl — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | Globals는 격자 크기를 선언한다(1–4). 바인드 그룹(bind group) 0은 바닥 입력 텍스처(texture)와 rgba32float 바닥 출력을 연결한다(6–9). 계산 셰이더(compute shader)는 작업 그룹 16×16으로 현재 바닥을 읽는다(12–16). 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `@group(0) @binding(0) var<uniform> globals: Globals;` (6); `@group(0) @binding(1) var txBottom: texture_2d<f32>;` (8); `@group(0) @binding(2) var txtemp_bottom: texture_storage_2d<rgba32float, write>;` (9); `@compute @workgroup_size(16, 16)` (12); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (13); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (14); `var B_here = textureLoad(txBottom, idx, 0);` (16) |
| 18–37 | 시작 시 13행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. main은 lengthCheck=3·B_here.w=99로 설정한다(19–20). x 방향 ±3 범위를 순회하고 x 좌표를 경계로 제한한다(23–29). 바닥이 0 이상인 이웃이 있으면 w=-99로 설정한다(30–33). y 순회는 주석이다(21–22·25–27·36). 원문: `// update neardry` (18); `let lengthCheck = 3;    // check within three points` (19); `B_here.w = 99.;` (20); `// for (var yy = idx.y - lengthCheck; yy <= idx.y + lengthCheck; yy += 1)` (21); `// {` (22); `for (var xx = idx.x - lengthCheck; xx <= idx.x + lengthCheck; xx += 1) {` (23); `let xC = min(globals.width - 1, max(0, xx));` (24); `// let yC = min(globals.height - 1, max(0, yy));` (25); `// let idx_C = vec2<i32>(xC, yC);` (27); `let idx_C = vec2<i32>(xC, idx.y);` (28); `let bathy_C = textureLoad(txBottom, idx_C, 0).z;` (29); `if (bathy_C >= 0.)` (30); `B_here.w = -99.;` (32); `// }` (36) |
| 38–58 | 시작 시 13행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. main은 ±1 x 이웃 바닥을 읽는다(39–46). 현재 바닥이 양수이고 양옆 바닥이 음수이면 중심 높이를 0, 동쪽 면 높이를 B_east/2로 설정한다(47–53). 갱신한 바닥을 저장한다(56). 원문: `// check for single point islands` (38); `let leftIdx = idx + vec2<i32>(-1, 0);` (39); `let rightIdx = idx + vec2<i32>(1, 0);` (40); `// let downIdx = idx + vec2<i32>(0, -1);` (41); `// let upIdx = idx + vec2<i32>(0, 1);` (42); `// let B_south = textureLoad(txBottom, downIdx, 0).z;` (43); `// let B_north = textureLoad(txBottom, upIdx, 0).z;` (44); `let B_west = textureLoad(txBottom, leftIdx, 0).z;` (45); `let B_east = textureLoad(txBottom, rightIdx, 0).z;` (46); `if(B_here.z > 0.){` (47); `// if(B_south < 0.0 && B_north < 0.0 && B_west < 0.0 && B_east < 0.0) {` (48); `if(B_west < 0.0 && B_east < 0.0) {` (49); `B_here.z = 0.0;` (50); `// B_here.x = B_north / 2.0;` (51); `B_here.y = B_east / 2.0;` (52); `textureStore(txtemp_bottom, idx, B_here);` (56) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–35: 검사 반경은 x 방향 3격자이며 표지는 99와 -99이다. y 방향 루프는 주석이다.
- 20–35·47–52: 건조 근접 표지는 고립 양수 바닥의 높이를 0으로 바꾸기 전에 계산한다. 높이 변경 뒤 w를 다시 계산하는 루프는 없다.
- 39–46: 고립점 검사에서 동·서 이웃은 경계 제한 없이 읽는다. 앞선 반경 순회의 x 좌표는 0부터 width-1까지 제한한다(24).
