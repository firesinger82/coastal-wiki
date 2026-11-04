---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/SedTrans_UpdateBottom.wgsl
lines: 52
sha256: 207424425b4c62ef015c947d36471da1fad5517eb9b46ea705174b9424215151
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_UpdateBottom.wgsl — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | Globals는 격자·dt·간격·기준 수심·적분 종류·공극률을 선언한다(1–11). 바인드 그룹(bind group) 0은 바닥·누적 변화·침식·퇴적 입력 텍스처(texture)와 바닥·변화 rgba32float 출력을 연결한다(13–20). 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `dt: f32,` (4); `dx: f32,` (5); `dy: f32,` (6); `base_depth: f32,` (7); `timeScheme: i32,` (8); `pred_or_corrector: i32,` (9); `sedC1_n: f32,` (10); `@group(0) @binding(0) var<uniform> globals: Globals;` (13); `@group(0) @binding(1) var txBottom: texture_2d<f32>;` (15); `@group(0) @binding(2) var txBotChange_Sed: texture_2d<f32>;` (16); `@group(0) @binding(3) var erosion_Sed: texture_2d<f32>;` (17); `@group(0) @binding(4) var depostion_Sed: texture_2d<f32>;` (18); `@group(0) @binding(5) var txtemp_SedTrans_Botttom: texture_storage_2d<rgba32float, write>;` (19); `@group(0) @binding(6) var txtemp_SedTrans_Change: texture_storage_2d<rgba32float, write>;` (20) |
| 23–40 | 계산 셰이더(compute shader)는 작업 그룹 16×16이다(23). 동·북 좌표는 각각 (1,0)·(0,1) 오프셋이다(27–28). 현재·동·북의 침식·퇴적을 읽고 바닥·누적 변화도 읽는다(30–39). 원문: `@compute @workgroup_size(16, 16)` (23); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (24); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (25); `let rightIdx = idx + vec2<i32>(1, 0);` (27); `let upIdx = idx + vec2<i32>(0, 1);` (28); `var dB_cumulative = textureLoad(txBotChange_Sed, idx, 0);` (30); `var B_here = textureLoad(txBottom, idx, 0);` (31); `let min_val = -globals.base_depth;` (32); `let e_here =  textureLoad(erosion_Sed, idx, 0).x;` (34); `let d_here =  textureLoad(depostion_Sed, idx, 0).x;` (35); `let e_right =  textureLoad(erosion_Sed, rightIdx, 0).x;` (36); `let d_right =  textureLoad(depostion_Sed, rightIdx, 0).x;` (37); `let e_up =  textureLoad(erosion_Sed, upIdx, 0).x;` (38); `let d_up =  textureLoad(depostion_Sed, upIdx, 0).x;` (39) |
| 41–52 | 시작 시 24행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. main은 dt와 1-공극률로 중심 바닥 변화를 구하고 동·북 면에는 두 중심값의 평균을 쓴다(41–45). 바닥은 자기 대입으로 유지한다(46). 누적 변화에서 dB를 빼고 바닥·누적 변화를 저장한다(47–50). 원문: `let dB_here = globals.dt * (e_here - d_here) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation` (41); `let dB_right = 0.5 * ( dB_here +  globals.dt * (e_right - d_right) / (1.0 - globals.sedC1_n));` (42); `let dB_up =    0.5 * ( dB_here +  globals.dt * (e_up - d_up) / (1.0 - globals.sedC1_n));` (43); `let dB = vec4<f32>(dB_up, dB_right, dB_here, 0.0);` (45); `B_here = B_here; // - dB;  // B is elevation, so a positive dB (eroding) should decrease the elevation` (46); `dB_cumulative = dB_cumulative - dB;` (47); `textureStore(txtemp_SedTrans_Botttom, idx, B_here);` (49); `textureStore(txtemp_SedTrans_Change, idx, dB_cumulative);` (50) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 46: 활성 문장은 B_here = B_here;이다. 바닥에서 dB를 빼는 부분은 주석이다.
- 32: min_val=-globals.base_depth를 계산하지만 이후 실행식에서 사용하지 않는다.
- 27–28·36–39: 동·북 이웃은 경계 제한 없이 읽는다. 파일에는 경계 반환 조건이 없다.
- 41–43: 공극률 인자 1.0 - globals.sedC1_n을 분모로 사용한다. 0인 경우를 거르는 조건은 없다.
