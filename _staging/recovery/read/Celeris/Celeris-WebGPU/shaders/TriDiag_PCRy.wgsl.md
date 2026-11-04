---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/TriDiag_PCRy.wgsl
lines: 110
sha256: ac5ebf4cfec1d35a556f0858997faf39a8781a114b7c0d74a315a2bcc6dac02f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# TriDiag_PCRy.wgsl — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | y 방향 계수 coefMaty 및 상태·UVstar·두 저장 텍스처(texture)를 선언한다. Globals는 x 본판과 같은 P 필드를 쓴다. 원문: `struct Globals {` (1); `width: i32,` (2); `height: i32,` (3); `p: i32,` (4); `s: i32,` (5); `P: i32,` (7); `@group(0) @binding(0) var<uniform> globals: Globals;` (10); `@group(0) @binding(1) var coefMaty: texture_2d<f32>;` (12); `@group(0) @binding(2) var current_state: texture_2d<f32>;` (13); `@group(0) @binding(3) var current_stateUVstar: texture_2d<f32>;` (14); `@group(0) @binding(4) var txtemp: texture_storage_2d<rgba32float, write>;` (16); `@group(0) @binding(5) var txtemp2: texture_storage_2d<rgba32float, write>;` (17) 6행 주석은 JS가 `s` 뒤에 총 PCR 반복 수 uniform을 이미 쓴다고 설명한다. 이는 주석의 설명이다. 원문: `// CODEX: Total PCR iteration count; JS already writes this uniform after s.` (6). [11-04 전수 검증 보완] |
| 19–55 | 계산 셰이더(compute shader)의 main은 y 방향 ±s 좌표를 height 나머지로 만든다. x 본판과 같은 초기화이며 가장자리 검사는 주석이다. 원문: `@compute @workgroup_size(16, 16)` (19); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (20); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (21); `// let CurrentState = textureLoad(current_state, idx, 0);` (23); `let s = (globals.s);` (25); `let width = (globals.width);` (26); `let height = (globals.height);` (27); `//    let zero = vec4<f32>(0.0, 1.0, 0.0, CurrentState.b);` (29); `//    if (idx.x >= width - 2 \|\| idx.y >= height - 2 \|\| idx.x <= 1 \|\| idx.y <= 1) {` (34); `let idx_left =  vec2<i32>(idx.x, (idx.y - s + height) % height);` (38); `let idx_right = vec2<i32>(idx.x, (idx.y + s + height) % height);` (39); `var aIn = 0.0;` (41); `var bIn = 0.0;` (42); `var cIn = 0.0;` (43); `var dIn = 0.0;` (44); `var aInLeft = 0.0;` (46); `var bInLeft = 0.0;` (47); `var cInLeft = 0.0;` (48); `var dInLeft = 0.0;` (49); `var aInRight = 0.0;` (51); `var bInRight = 0.0;` (52); `var cInRight = 0.0;` (53); `var dInRight = 0.0;` (54) |
| 56–88 | 시작 시 20행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 첫 반복 정규화의 우변은 UVstar.b이다. x 본판과 달리 coefMaty를 읽는다. 후속 반복은 같은 r·b·a 성분 방식이다. 원문: `if (globals.p == 0) {` (56); `bIn = textureLoad(coefMaty, idx, 0).g;` (58); `bInLeft = textureLoad(coefMaty, idx_left, 0).g;` (59); `bInRight = textureLoad(coefMaty, idx_right, 0).g;` (60); `aIn = textureLoad(coefMaty, idx, 0).r / bIn;` (62); `aInLeft = textureLoad(coefMaty, idx_left, 0).r / bInLeft;` (63); `aInRight = textureLoad(coefMaty, idx_right, 0).r / bInRight;` (64); `cIn = textureLoad(coefMaty, idx, 0).b / bIn;` (66); `cInLeft = textureLoad(coefMaty, idx_left, 0).b / bInLeft;` (67); `cInRight =  textureLoad(coefMaty, idx_right, 0).b / bInRight;` (68); `dIn = textureLoad(current_stateUVstar, idx, 0).b / bIn;` (70); `dInLeft = textureLoad(current_stateUVstar, idx_left, 0).b / bInLeft;` (71); `dInRight = textureLoad(current_stateUVstar, idx_right, 0).b / bInRight;` (72); `} else {` (74); `aIn = textureLoad(coefMaty, idx, 0).r;` (76); `aInLeft = textureLoad(coefMaty, idx_left, 0).r;` (77); `aInRight = textureLoad(coefMaty, idx_right, 0).r;` (78); `cIn = textureLoad(coefMaty, idx, 0).b;` (80); `cInLeft = textureLoad(coefMaty, idx_left, 0).b;` (81); `cInRight = textureLoad(coefMaty, idx_right, 0).b;` (82); `dIn = textureLoad(coefMaty, idx, 0).a;` (84); `dInLeft = textureLoad(coefMaty, idx_left, 0).a;` (85); `dInRight = textureLoad(coefMaty, idx_right, 0).a;` (86) |
| 89–110 | 시작 시 20행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. PCR 소거식은 x 본판과 같다. 계수는 매 반복 저장한다. 마지막 반복만 현재 상태의 b 성분을 dOut으로 바꾸고 다른 성분을 보존한다. 끝 빈 줄을 포함한다. 원문: `let r = 1.0 / (1.0 - aIn * cInLeft - cIn * aInRight);` (89); `let aOut = -r * aIn * aInLeft;` (90); `let cOut = -r * cIn * cInRight;` (91); `let dOut = r * (dIn - aIn * dInLeft - cIn * dInRight);` (92); `let txtemp_out = vec4<f32>(aOut, 1.0, cOut, dOut);` (94); `// let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);` (95); `textureStore(txtemp, idx,  txtemp_out);` (97); `if (globals.p == globals.P - 1) {` (101); `let CurrentState = textureLoad(current_state, idx, 0);` (102); `let txtemp2_out = vec4<f32>(CurrentState.r, CurrentState.g, dOut, CurrentState.a);` (103); `textureStore(txtemp2, idx, txtemp2_out);` (104) 기존 상태 저장문은 주석 처리되어 있다. 원문: `// textureStore(txtemp2, idx, txtemp2_out);` (98). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–36: 가장자리 반환은 주석 처리되어 있다.
- 62–72·89: 정규화 및 소거 분모의 0 비교 조건은 없다.
- 101–104: 상태 저장은 마지막 반복 조건 안에만 있다.
