---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Handler_UpdateTrid.js
lines: 81
sha256: d5a83925aac6a2ade0910de395e43aa0faa97032b77da5fb190d0a8d28f1df0b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_UpdateTrid.js — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 바인드 그룹(bind group) 레이아웃을 생성한다(2–3). 계산 셰이더(compute shader)에 노출되는 uniform 버퍼와 두 입력 텍스처(texture)를 선언한다. 입력은 unfilterable-float·rgba32float이다(7–26). 원문: `// Handler_Tridiag.js` (1); `export function create_UpdateTrid_BindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `{` (5); `// 0th binding: A uniform buffer (for parameters like time, etc.)` (6); `binding: 0,` (7); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `{` (11); `// 1st binding: A texture that the fragment shader will sample from.` (12); `binding: 1,` (13); `visibility: GPUShaderStage.COMPUTE,` (14); `texture: {` (15); `sampleType: 'unfilterable-float',` (16); `format: 'rgba32float'` (17); `}` (18); `},` (19); `{` (20); `// 2nd binding: A texture that the fragment shader will sample from.` (21); `binding: 2,` (22); `visibility: GPUShaderStage.COMPUTE,` (23); `texture: {` (24); `sampleType: 'unfilterable-float',` (25); `format: 'rgba32float'` (26); `}` (27); `},` (28) |
| 29–52 | 시작 시 2행 create_UpdateTrid_BindGroupLayout 함수·3행 레이아웃 객체·4행 entries 배열 안. 쓰기 전용 rgba32float·2d 저장 텍스처를 binding 3·4에 선언한 뒤 레이아웃을 반환한다(31–50). 원문: `{` (29); `// 4th binding: A storage texture. The compute shader will write results into this texture.` (30); `binding: 3,` (31); `visibility: GPUShaderStage.COMPUTE,` (32); `storageTexture: {` (33); `access: 'write-only',      // This texture is only for writing data` (34); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (35); `viewDimension: '2d'       // The texture is a 2D texture` (36); `}` (37); `},` (38); `{` (39); `// 5th binding: A storage texture. The compute shader will write results into this texture.` (40); `binding: 4,` (41); `visibility: GPUShaderStage.COMPUTE,` (42); `storageTexture: {` (43); `access: 'write-only',      // This texture is only for writing data` (44); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (45); `viewDimension: '2d'       // The texture is a 2D texture` (46); `}` (47); `}` (48); `]` (49); `});` (50); `}` (51) |
| 53–81 | create_UpdateTrid_BindGroup은 레이아웃을 새로 만들고 uniformBuffer, txBottom, txNewState, coefMatx, coefMaty를 binding 0–4 순서로 연결한다(53–80). 원문: `export function create_UpdateTrid_BindGroup(device, uniformBuffer, txBottom, txNewState, coefMatx, coefMaty) {` (53); `return device.createBindGroup({` (54); `layout: create_UpdateTrid_BindGroupLayout(device),` (55); `entries: [` (56); `{` (57); `binding: 0,` (58); `resource: {` (59); `buffer: uniformBuffer` (60); `}` (61); `},` (62); `{` (63); `binding: 1,` (64); `resource: txBottom.createView()` (65); `},` (66); `{` (67); `binding: 2,` (68); `resource: txNewState.createView()` (69); `},` (70); `{` (71); `binding: 3,` (72); `resource: coefMatx.createView()` (73); `},` (74); `{` (75); `binding: 4,` (76); `resource: coefMaty.createView()` (77); `},` (78); `]` (79); `});` (80); `}` (81) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: 머리말 파일명은 Handler_Tridiag.js이며 실제 대상 파일명은 Handler_UpdateTrid.js이다.
- 12·21: 입력 텍스처 주석은 fragment shader를 언급하지만 visibility 값은 GPUShaderStage.COMPUTE이다(14·23).
