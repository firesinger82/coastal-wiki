---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_CalcWaveHeight.js
lines: 93
sha256: 283d88ae38a302c1fbd6906366644f1d85e69c1f91bccd0ae23f4e3598b1328a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_CalcWaveHeight.js — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 머리말과 `create_CalcWaveHeight_BindGroupLayout` 시작(1–4). 계산 셰이더(compute shader)용 바인드 그룹(bind group)에서 0은 유니폼 버퍼(uniform buffer), 1·2·3은 unfilterable-float·rgba32float 입력 텍스처(texture)이다(7–35). 원문: `export function create_CalcWaveHeight_BindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `{` (5); `binding: 0,` (7); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `{` (11); `binding: 1,` (13); `visibility: GPUShaderStage.COMPUTE,` (14); `texture: {` (15); `sampleType: 'unfilterable-float',` (16); `format: 'rgba32float'` (17); `}` (18); `},` (19); `{` (20); `binding: 2,` (22); `visibility: GPUShaderStage.COMPUTE,` (23); `texture: {` (24); `sampleType: 'unfilterable-float',` (25); `format: 'rgba32float'` (26); `}` (27); `},` (28); `{` (29); `binding: 3,` (31); `visibility: GPUShaderStage.COMPUTE,` (32); `texture: {` (33); `sampleType: 'unfilterable-float',` (34); `format: 'rgba32float'` (35); `}` (36); `},` (37); `{` (38) 6행 주석은 uniform을 시간 등의 매개변수용으로 설명한다. [11-04 전수 검증 보완] |
| 39–60 | 시작 시 2행 레이아웃 함수·3행 생성 객체·4행 entries 배열 안. 4는 같은 입력 형식이고 5는 write-only·rgba32float·2d 저장 텍스처이다(40–54). 레이아웃을 닫는다(57–59). 원문: `binding: 4,` (40); `visibility: GPUShaderStage.COMPUTE,` (41); `texture: {` (42); `sampleType: 'unfilterable-float',` (43); `format: 'rgba32float'` (44); `}` (45); `},` (46); `{` (47); `binding: 5,` (49); `visibility: GPUShaderStage.COMPUTE,` (50); `storageTexture: {` (51); `access: 'write-only',      // This texture is only for writing data` (52); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (53); `viewDimension: '2d'       // The texture is a 2D texture` (54); `}` (55); `}` (56); `]` (57); `});` (58); `}` (59) 구간 시작은 38행에서 열린 binding 4 객체 안이며 이 객체는 46행에서 닫힌다. [11-04 전수 검증 보완] |
| 61–93 | `create_CalcWaveHeight_BindGroup`는 0에 uniformBuffer, 1..5에 txState·txNewState·txMeans·txWaveHeight·txtemp_WaveHeight 뷰를 이 순서로 연결한다(61–93). 생성 호출·모든 자원 연결을 인용한다. 원문: `export function create_CalcWaveHeight_BindGroup(device, uniformBuffer, txState, txNewState, txMeans, txWaveHeight, txtemp_WaveHeight) {` (61); `return device.createBindGroup({` (62); `layout: create_CalcWaveHeight_BindGroupLayout(device),` (63); `entries: [` (64); `{` (65); `binding: 0,` (66); `resource: {` (67); `buffer: uniformBuffer` (68); `}` (69); `},` (70); `{` (71); `binding: 1,` (72); `resource: txState.createView()` (73); `},` (74); `{` (75); `binding: 2,` (76); `resource: txNewState.createView()` (77); `},` (78); `{` (79); `binding: 3,` (80); `resource: txMeans.createView()` (81); `},` (82); `{` (83); `binding: 4,` (84); `resource: txWaveHeight.createView()` (85); `},` (86); `{` (87); `binding: 5,` (88); `resource: txtemp_WaveHeight.createView()` (89); `},` (90); `]` (91); `});` (92); `}` (93) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: 머리말은 Handler_Tridiag.js라고 적혀 있다.
- 12·21·30·39: 입력 텍스처 설명은 fragment shader를 언급하지만 해당 visibility는 COMPUTE이다.
