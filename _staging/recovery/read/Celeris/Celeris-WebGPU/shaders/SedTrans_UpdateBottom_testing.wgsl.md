---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/SedTrans_UpdateBottom_testing.wgsl
lines: 90
sha256: 0e0d6b28c45dc374ba79b50b4e432bd22ce2f820792f5bd81b384748ca20a313
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SedTrans_UpdateBottom_testing.wgsl — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | Globals에 n_sim·sedUpdateInt를 추가하고 초기 바닥·누적 변화·최근 변화용 텍스처(texture) 바인딩을 선언한다. 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `dt: f32,` (4); `dx: f32,` (5); `dy: f32,` (6); `base_depth: f32,` (7); `timeScheme: i32,` (8); `pred_or_corrector: i32,` (9); `sedC1_n: f32,` (10); `west_boundary_type: i32,` (11); `east_boundary_type: i32,` (12); `south_boundary_type: i32,` (13); `north_boundary_type: i32,` (14); `n_sim: i32,` (15); `sedUpdateInt: i32,` (16); `@group(0) @binding(0) var<uniform> globals: Globals;` (19); `@group(0) @binding(1) var txBottomInitial: texture_2d<f32>;` (21); `@group(0) @binding(2) var txBotChange_Sed: texture_2d<f32>;` (22); `@group(0) @binding(3) var txBotChangeRecent_Sed: texture_2d<f32>;` (23); `@group(0) @binding(4) var erosion_Sed: texture_2d<f32>;` (24); `@group(0) @binding(5) var depostion_Sed: texture_2d<f32>;` (25); `@group(0) @binding(6) var txtemp_SedTrans_Botttom: texture_storage_2d<rgba32float, write>;` (26); `@group(0) @binding(7) var txtemp_SedTrans_Change: texture_storage_2d<rgba32float, write>;` (27); `@group(0) @binding(8) var txtemp_txBotChangeRecent_Sed: texture_storage_2d<rgba32float, write>;` (28) |
| 31–52 | 계산 셰이더(compute shader)는 현재·우측·상측 침식·퇴적을 읽는다. 본판과 달리 dB 계산에 dt가 없고 이웃 평균은 각 셀의 침식·퇴적 차로 만든다. 원문: `@compute @workgroup_size(16, 16)` (31); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (32); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (33); `let rightIdx = idx + vec2<i32>(1, 0);` (35); `let upIdx = idx + vec2<i32>(0, 1);` (36); `let min_val = -globals.base_depth;` (38); `let e_here =  textureLoad(erosion_Sed, idx, 0).x;` (40); `let d_here =  textureLoad(depostion_Sed, idx, 0).x;` (41); `let e_right =  textureLoad(erosion_Sed, rightIdx, 0).x;` (42); `let d_right =  textureLoad(depostion_Sed, rightIdx, 0).x;` (43); `let e_up =  textureLoad(erosion_Sed, upIdx, 0).x;` (44); `let d_up =  textureLoad(depostion_Sed, upIdx, 0).x;` (45); `let dB_here = (e_here - d_here) / (1.0 - globals.sedC1_n); // this is positive when eroding - when increasing depth, or decreasing elevation` (47); `let dB_right = 0.5 * ( dB_here +  (e_right - d_right) / (1.0 - globals.sedC1_n));` (48); `let dB_up =    0.5 * ( dB_here +  (e_up - d_up) / (1.0 - globals.sedC1_n));` (49); `var dB = vec4<f32>(dB_up, dB_right, dB_here, 0.0);` (51) |
| 53–69 | 시작 시 32행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 본판과 같은 네 경계 조건과 선형 ramp를 적용한다. 원문: `if (globals.west_boundary_type == 2 && idx.x < 10) {` (53); `let ramp = max(0.0, (f32(idx.x)-5.0) / 5.0);  // Linear ramp from 0 to 1 over the first 10 columns` (54); `dB = ramp * dB;  // No sediment transport in the first 20 columns` (55); `if (globals.east_boundary_type == 2 && idx.x > globals.width - 11) {` (57); `let ramp = max(0.0, (f32(globals.width - idx.x) - 5.0) / 5.0);  // Linear ramp from 0 to 1 over the last 10 columns` (58); `dB = ramp * dB;  // No sediment transport in the last 20 columns` (59); `if (globals.south_boundary_type == 2 && idx.y < 10) {` (61); `let ramp = max(0.0, (f32(idx.y)-5.0) / 5.0);  // Linear ramp from 0 to 1 over the first 10 rows` (62); `dB = ramp * dB;  // No sediment transport in the first 20 rows` (63); `if (globals.north_boundary_type == 2 && idx.y > globals.height - 11) {` (65); `let ramp = max(0.0, (f32(globals.height - idx.y) - 5.0) / 5.0);  // Linear ramp from 0 to 1 over the last 10 rows` (66); `dB = ramp * dB;  // No sediment transport in the last 20 rows` (67) |
| 70–90 | 시작 시 32행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 누적 변화에서 dt*dB를 뺀다. 출력 바닥은 초기 바닥 그대로이다. 최근 변화 누적과 sedUpdateInt 간격 바닥 갱신은 주석 처리되어 있다. 바닥·누적 변화 두 출력만 저장한다. 원문: `var dB_cumulative = textureLoad(txBotChange_Sed, idx, 0);` (70); `dB_cumulative = dB_cumulative - globals.dt * dB;` (71); `//  var dB_UpdateSum = textureLoad(txBotChangeRecent_Sed, idx, 0);` (73); `//  dB_UpdateSum = dB_UpdateSum + dB;` (74); `let B_initial = textureLoad(txBottomInitial, idx, 0);` (76); `let B_here = B_initial; // + dB_cumulative;` (77); `//   if (globals.n_sim % globals.sedUpdateInt == 0) {` (79); `//      B_here = B_here - globals.dt * dB_UpdateSum;` (81); `//      dB_UpdateSum = vec4<f32>(0.0, 0.0, 0.0, 0.0);` (83); `textureStore(txtemp_SedTrans_Botttom, idx, B_here);` (86); `textureStore(txtemp_SedTrans_Change, idx, dB_cumulative);` (87) 최근 변화 출력도 주석 처리되어 있다. 원문: `//  textureStore(txtemp_txBotChangeRecent_Sed, idx, dB_UpdateSum);` (88). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–45: main 안에 격자 범위 검사나 가장자리 반환이 없다. 우측·상측 읽기를 수행한다.
- 38: min_val은 선언 뒤 사용되지 않는다.
- 73–84: 최근 변화 누적과 주기 조건 및 바닥 갱신식이 주석 처리되어 있다.
- 76–87: B_here는 B_initial 그대로이며 누적 변화는 별도 출력에만 저장한다.
- 23·28·73·88: 최근 변화 텍스처는 선언되어 있으나 관련 읽기·쓰기는 주석 처리되어 있다.
