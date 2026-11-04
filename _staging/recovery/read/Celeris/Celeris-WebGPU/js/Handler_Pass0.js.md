---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_Pass0.js
lines: 69
sha256: dd057d7b2da69ddef5e69cb239fefbcd6fa2e6696af6605e3010d2804b09e77a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass0.js — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | 머리말・빈 줄과 `create_Pass0_BindGroupLayout`는 계산 셰이더(compute shader)용 바인드 그룹(bind group) 레이아웃을 만든다(1–5). 0은 유니폼 버퍼(uniform buffer), 1·2는 unfilterable-float rgba32float 입력 텍스처(texture), 3은 write-only rgba32float 2d 출력이다(8–38). 원문: `export function create_Pass0_BindGroupLayout(device) {` (3); `return device.createBindGroupLayout({` (4); `entries: [` (5); `{` (6); `binding: 0,` (8); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (9); `buffer: { type: 'uniform' }  // It's a uniform buffer` (10); `},` (11); `{` (12); `binding: 1,` (14); `visibility: GPUShaderStage.COMPUTE,` (15); `texture: {` (16); `sampleType: 'unfilterable-float',` (17); `format: 'rgba32float'` (18); `}` (19); `},` (20); `{` (21); `binding: 2,` (23); `visibility: GPUShaderStage.COMPUTE,` (24); `texture: {` (25); `sampleType: 'unfilterable-float',` (26); `format: 'rgba32float'` (27); `}` (28); `},` (29); `{` (30); `binding: 3,` (32); `visibility: GPUShaderStage.COMPUTE,` (33); `storageTexture: {` (34); `access: 'write-only',      // This texture is only for writing data` (35); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (36); `viewDimension: '2d'       // The texture is a 2D texture` (37); `}` (38); `}` (39); `]` (40); `});` (41); `}` (42) 7행 주석은 uniform을 시간 등의 매개변수용으로 설명한다. 13·22행 주석은 입력을 fragment shader 표본화용이라고 적지만 실제 visibility는 COMPUTE이다. [11-04 전수 검증 보완] |
| 45–69 | `create_Pass0_BindGroup`는 0에 uniformBuffer, 1에 txState, 2에 txBottom, 3에 txHnear 뷰를 연결한다(45–69). 원문: `export function create_Pass0_BindGroup(device, uniformBuffer, txState, txBottom, txHnear) {` (45); `return device.createBindGroup({` (46); `layout: create_Pass0_BindGroupLayout(device),` (47); `entries: [` (48); `{` (49); `binding: 0,` (50); `resource: {` (51); `buffer: uniformBuffer` (52); `}` (53); `},` (54); `{` (55); `binding: 1,` (56); `resource: txState.createView()` (57); `},` (58); `{` (59); `binding: 2,` (60); `resource: txBottom.createView()` (61); `},` (62); `{` (63); `binding: 3,` (64); `resource: txHnear.createView()` (65); `},` (66); `]` (67); `});` (68); `}` (69) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: 머리말은 Handler_Pass1.js라고 적혀 있다.
