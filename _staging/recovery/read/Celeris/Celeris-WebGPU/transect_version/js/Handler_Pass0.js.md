---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Handler_Pass0.js
lines: 69
sha256: 75d9bef7f8e4fe090fb153e33b3c34feff0816aa9f722102081625408bcad111
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass0.js — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–44 | 머리말·빈 줄과 Pass0 바인드 그룹(bind group) 레이아웃을 정의한다(3–42). 계산 셰이더(compute shader)용 유니폼 버퍼(uniform buffer) 0번, 비필터 `rgba32float` 읽기 텍스처(texture) 1–2번, 쓰기 전용 2차원 저장 텍스처 3번을 선언한다. 원문: `export function create_Pass0_BindGroupLayout(device) {` (3)<br>`return device.createBindGroupLayout({` (4)<br>`entries: [` (5)<br>`{` (6)<br>`binding: 0,` (8)<br>`visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (9)<br>`buffer: { type: 'uniform' }  // It's a uniform buffer` (10)<br>`},` (11)<br>`{` (12)<br>`binding: 1,` (14)<br>`visibility: GPUShaderStage.COMPUTE,` (15)<br>`texture: {` (16)<br>`sampleType: 'unfilterable-float',` (17)<br>`format: 'rgba32float'` (18)<br>`}` (19)<br>`},` (20)<br>`{` (21)<br>`binding: 2,` (23)<br>`visibility: GPUShaderStage.COMPUTE,` (24)<br>`texture: {` (25)<br>`sampleType: 'unfilterable-float',` (26)<br>`format: 'rgba32float'` (27)<br>`}` (28)<br>`},` (29)<br>`{` (30)<br>`binding: 3,` (32)<br>`visibility: GPUShaderStage.COMPUTE,` (33)<br>`storageTexture: {` (34)<br>`access: 'write-only',      // This texture is only for writing data` (35)<br>`format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (36)<br>`viewDimension: '2d'       // The texture is a 2D texture` (37)<br>`}` (38)<br>`}` (39)<br>`]` (40)<br>`});` (41)<br>`}` (42) 유니폼 매개변수 예시의 주석: `// 0th binding: A uniform buffer (for parameters like time, etc.)` (7) [11-04 전수 검증 보완] |
| 45–69 | 바인드 그룹을 생성하여 0번에는 `uniformBuffer`를 연결한다. 1–3번에는 txState·txBottom·txHnear 뷰(view)를 연결한다(45–69). 원문: `export function create_Pass0_BindGroup(device, uniformBuffer, txState, txBottom, txHnear) {` (45)<br>`return device.createBindGroup({` (46)<br>`layout: create_Pass0_BindGroupLayout(device),` (47)<br>`entries: [` (48)<br>`{` (49)<br>`binding: 0,` (50)<br>`resource: {` (51)<br>`buffer: uniformBuffer` (52)<br>`}` (53)<br>`},` (54)<br>`{` (55)<br>`binding: 1,` (56)<br>`resource: txState.createView()` (57)<br>`},` (58)<br>`{` (59)<br>`binding: 2,` (60)<br>`resource: txBottom.createView()` (61)<br>`},` (62)<br>`{` (63)<br>`binding: 3,` (64)<br>`resource: txHnear.createView()` (65)<br>`},` (66)<br>`]` (67)<br>`});` (68)<br>`}` (69) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·3·45: 머리말은 `Handler_Pass1.js`이고 공개 함수는 Pass0용이다.
- 13·22·15·24: 입력 텍스처 주석은 fragment shader를 적지만 visibility는 COMPUTE이다.
