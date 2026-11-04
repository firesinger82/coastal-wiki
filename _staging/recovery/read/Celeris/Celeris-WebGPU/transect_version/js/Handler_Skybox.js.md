---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Handler_Skybox.js
lines: 57
sha256: 916df1c4e21f8962e61e9294ca1bde7f061540916ffe24e13b5a295b3b7fb735
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Skybox.js — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 머리말·빈 줄과 스카이박스(skybox) 바인드 그룹(bind group) 레이아웃을 정의한다(2–31). 유니폼 버퍼(uniform buffer) 0번은 정점(vertex) 단계에만 공개한다. 텍스처(texture) 1번은 프래그먼트(fragment)용 `float`·`bgra8unorm`·`cube`이다. 2번은 프래그먼트용 filtering 샘플러(sampler)이다. 원문: `export function createSkyboxBindGroupLayout(device) {` (2)<br>`return device.createBindGroupLayout({` (3)<br>`entries: [` (4)<br>`{` (5)<br>`binding: 0,` (7)<br>`visibility: GPUShaderStage.VERTEX,` (8)<br>`buffer: { type: 'uniform' }  // It's a uniform buffer` (9)<br>`},` (10)<br>`{` (11)<br>`binding: 1,` (13)<br>`visibility: GPUShaderStage.FRAGMENT,` (14)<br>`texture: {` (15)<br>`sampleType: 'float',` (16)<br>`format: 'bgra8unorm',  // imagedata for the skybox cube images` (17)<br>`viewDimension: 'cube',  // Cube map view` (18)<br>`}` (19)<br>`},` (20)<br>`{` (21)<br>`binding: 2,` (23)<br>`visibility: GPUShaderStage.FRAGMENT,` (24)<br>`sampler: {` (25)<br>`type: 'filtering'  // Nearest-neighbor sampling (no interpolation)` (26)<br>`}` (27)<br>`},` (28)<br>`]` (29)<br>`});` (30)<br>`}` (31) 유니폼 매개변수 예시의 주석: `// 0th binding: A uniform buffer (for parameters like time, etc.)` (6) [11-04 전수 검증 보완] |
| 34–57 | 바인드 그룹 생성은 uniformBuffer·cubeView·cubeSampler를 0–2번에 연결한다(35–55). 텍스처 뷰(view)는 인수로 받아 그대로 사용한다. 마지막 빈 줄을 포함한다. 원문: `export function createSkyboxBindGroup(device, uniformBuffer, cubeView, cubeSampler) {` (35)<br>`return device.createBindGroup({` (36)<br>`layout: createSkyboxBindGroupLayout(device),` (37)<br>`entries: [` (38)<br>`{` (39)<br>`binding: 0,` (40)<br>`resource: {` (41)<br>`buffer: uniformBuffer` (42)<br>`}` (43)<br>`},` (44)<br>`{` (45)<br>`binding: 1,` (46)<br>`resource: cubeView` (47)<br>`},` (48)<br>`{` (49)<br>`binding: 2,` (50)<br>`resource: cubeSampler` (51)<br>`},` (52)<br>`]` (53)<br>`});` (54)<br>`}` (55) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–26: 샘플러 주석은 linear와 nearest-neighbor를 함께 적는다. 실제 type은 `filtering`이다.
