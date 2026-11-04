---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Handler_CalcWaveHeight.js
lines: 93
sha256: 7d824de15dcf92caf1b943ef080ca8fb4c2fbe61f90c0dad16ac5dc4aaecdf8f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_CalcWaveHeight.js — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–60 | 머리말과 파고(wave height) 계산 바인드 그룹(bind group) 레이아웃이다. 계산 셰이더(compute shader)용 유니폼 버퍼(uniform buffer) 0번, 읽기 `rgba32float` 텍스처(texture) 1–4번, 쓰기 전용 2차원 저장 텍스처 5번을 선언한다(2–59). 원문: `export function create_CalcWaveHeight_BindGroupLayout(device) {` (2)<br>`return device.createBindGroupLayout({` (3)<br>`entries: [` (4)<br>`{` (5)<br>`binding: 0,` (7)<br>`visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (8)<br>`buffer: { type: 'uniform' }  // It's a uniform buffer` (9)<br>`},` (10)<br>`{` (11)<br>`binding: 1,` (13)<br>`visibility: GPUShaderStage.COMPUTE,` (14)<br>`texture: {` (15)<br>`sampleType: 'unfilterable-float',` (16)<br>`format: 'rgba32float'` (17)<br>`}` (18)<br>`},` (19)<br>`{` (20)<br>`binding: 2,` (22)<br>`visibility: GPUShaderStage.COMPUTE,` (23)<br>`texture: {` (24)<br>`sampleType: 'unfilterable-float',` (25)<br>`format: 'rgba32float'` (26)<br>`}` (27)<br>`},` (28)<br>`{` (29)<br>`binding: 3,` (31)<br>`visibility: GPUShaderStage.COMPUTE,` (32)<br>`texture: {` (33)<br>`sampleType: 'unfilterable-float',` (34)<br>`format: 'rgba32float'` (35)<br>`}` (36)<br>`},` (37)<br>`{` (38)<br>`binding: 4,` (40)<br>`visibility: GPUShaderStage.COMPUTE,` (41)<br>`texture: {` (42)<br>`sampleType: 'unfilterable-float',` (43)<br>`format: 'rgba32float'` (44)<br>`}` (45)<br>`},` (46)<br>`{` (47)<br>`binding: 5,` (49)<br>`visibility: GPUShaderStage.COMPUTE,` (50)<br>`storageTexture: {` (51)<br>`access: 'write-only',      // This texture is only for writing data` (52)<br>`format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (53)<br>`viewDimension: '2d'       // The texture is a 2D texture` (54)<br>`}` (55)<br>`}` (56)<br>`]` (57)<br>`});` (58)<br>`}` (59) 유니폼 매개변수 예시의 주석: `// 0th binding: A uniform buffer (for parameters like time, etc.)` (6) [11-04 전수 검증 보완] |
| 61–93 | 바인드 그룹을 생성한다. 0번은 uniformBuffer이고 1–5번은 txState·txNewState·txMeans·txWaveHeight·txtemp_WaveHeight 뷰(view)이다(61–93). 원문: `export function create_CalcWaveHeight_BindGroup(device, uniformBuffer, txState, txNewState, txMeans, txWaveHeight, txtemp_WaveHeight) {` (61)<br>`return device.createBindGroup({` (62)<br>`layout: create_CalcWaveHeight_BindGroupLayout(device),` (63)<br>`entries: [` (64)<br>`{` (65)<br>`binding: 0,` (66)<br>`resource: {` (67)<br>`buffer: uniformBuffer` (68)<br>`}` (69)<br>`},` (70)<br>`{` (71)<br>`binding: 1,` (72)<br>`resource: txState.createView()` (73)<br>`},` (74)<br>`{` (75)<br>`binding: 2,` (76)<br>`resource: txNewState.createView()` (77)<br>`},` (78)<br>`{` (79)<br>`binding: 3,` (80)<br>`resource: txMeans.createView()` (81)<br>`},` (82)<br>`{` (83)<br>`binding: 4,` (84)<br>`resource: txWaveHeight.createView()` (85)<br>`},` (86)<br>`{` (87)<br>`binding: 5,` (88)<br>`resource: txtemp_WaveHeight.createView()` (89)<br>`},` (90)<br>`]` (91)<br>`});` (92)<br>`}` (93) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·2·61: 머리말은 `Handler_Tridiag.js`이고 공개 함수는 CalcWaveHeight용이다.
- 12–44: 읽기 텍스처 주석은 fragment shader를 적지만 visibility는 COMPUTE이다.
