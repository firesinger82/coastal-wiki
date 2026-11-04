---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Handler_Updateneardry.js
lines: 54
sha256: 603c8c3590d823477591972b852aa95a77d9db2499df06720cea8c4380289bb1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Updateneardry.js — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | create_Updateneardry_BindGroupLayout은 바인드 그룹(bind group) 레이아웃을 만든다. 계산 셰이더(compute shader)용 uniform 버퍼, unfilterable-float 입력 텍스처(texture), 쓰기 전용 rgba32float·2d 저장 텍스처를 binding 0–2에 선언한다(2–32). 원문: `// Handler_Updateneardry.js` (1); `export function create_Updateneardry_BindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `{` (5); `// 0th binding: A uniform buffer (for parameters like time, etc.)` (6); `binding: 0,` (7); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `{` (11); `// 1st binding: A texture that the fragment shader will sample from.` (12); `binding: 1,` (13); `visibility: GPUShaderStage.COMPUTE,` (14); `texture: {` (15); `sampleType: 'unfilterable-float',` (16); `format: 'rgba32float'` (17); `}` (18); `},` (19); `{` (20); `// 2ns binding: A storage texture. The compute shader will write results into this texture.` (21); `binding: 2,` (22); `visibility: GPUShaderStage.COMPUTE,` (23); `storageTexture: {` (24); `access: 'write-only',      // This texture is only for writing data` (25); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (26); `viewDimension: '2d'       // The texture is a 2D texture` (27); `}` (28); `}` (29); `]` (30); `});` (31); `}` (32) |
| 34–54 | create_Updateneardry_BindGroup은 레이아웃을 생성한다(36). binding 0의 버퍼는 `uniformBuffer`이다(39–41). binding 1·2의 텍스처 뷰는 각각 `txBottom.createView()`·`txtemp_bottom.createView()`이다(45–50). 원문: `export function create_Updateneardry_BindGroup(device, uniformBuffer, txBottom, txtemp_bottom) {` (34); `return device.createBindGroup({` (35); `layout: create_Updateneardry_BindGroupLayout(device),` (36); `entries: [` (37); `{` (38); `binding: 0,` (39); `resource: {` (40); `buffer: uniformBuffer` (41); `}` (42); `},` (43); `{` (44); `binding: 1,` (45); `resource: txBottom.createView()` (46); `},` (47); `{` (48); `binding: 2,` (49); `resource: txtemp_bottom.createView()` (50); `},` (51); `]` (52); `});` (53); `}` (54) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–14: 입력 텍스처 주석은 fragment shader를 언급하지만 visibility 값은 GPUShaderStage.COMPUTE이다.
