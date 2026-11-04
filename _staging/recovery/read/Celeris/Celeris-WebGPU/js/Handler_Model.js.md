---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_Model.js
lines: 58
sha256: 8e674edab93a74cabea39c100d738120866392e20616a2006aa48b34d344a47e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Model.js — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 머리말과 `createModelBindGroupLayout`는 바인드 그룹(bind group) 레이아웃을 만든다(1–4). 0 유니폼 버퍼(uniform buffer)는 VERTEX·FRAGMENT, 1 float·bgra8unorm·2d 입력 텍스처(texture)는 FRAGMENT, 2 filtering 샘플러(sampler)는 VERTEX·FRAGMENT에 보인다(7–27). 원문: `export function createModelBindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `{` (5); `binding: 0,` (7); `visibility: GPUShaderStage.VERTEX \| GPUShaderStage.FRAGMENT,` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `{` (11); `binding: 1,` (13); `visibility: GPUShaderStage.FRAGMENT,` (14); `texture: {` (15); `sampleType: 'float',` (16); `format: 'bgra8unorm',  // imagedata for the google maps image` (17); `viewDimension: '2d'` (18); `}` (19); `},` (20); `{` (21); `binding: 2,` (23); `visibility: GPUShaderStage.VERTEX \| GPUShaderStage.FRAGMENT,` (24); `sampler: {` (25); `type: 'filtering'  // Nearest-neighbor sampling (no interpolation)` (26); `}` (27); `},` (28); `]` (29); `});` (30); `}` (31) 6행 주석은 uniform을 시간 등의 매개변수용으로 설명한다. 22행 주석은 binding 2를 텍스처 표본화 방법을 지정하는 linear sampler라고 적는다. [11-04 전수 검증 보완] |
| 34–58 | `createModelBindGroup`는 생성한 레이아웃의 0에 uniformBuffer, 1에 이미 생성된 txModelPNG_view, 2에 textureSampler_linear를 연결한다(35–54). 이 함수는 텍스처 뷰를 새로 만들지 않는다. 끝 빈 줄을 포함한다(56–58). 원문: `export function createModelBindGroup(device, uniformBuffer, txModelPNG_view, textureSampler_linear) {` (35); `return device.createBindGroup({` (36); `layout: createModelBindGroupLayout(device),` (37); `entries: [` (38); `{` (39); `binding: 0,` (40); `resource: {` (41); `buffer: uniformBuffer` (42); `}` (43); `},` (44); `{` (45); `binding: 1,` (46); `resource: txModelPNG_view` (47); `},` (48); `{` (49); `binding: 2,` (50); `resource: textureSampler_linear` (51); `},` (52); `]` (53); `});` (54); `}` (55) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26: sampler type은 'filtering'이지만 같은 행 주석은 Nearest-neighbor sampling (no interpolation)이라고 적는다.
