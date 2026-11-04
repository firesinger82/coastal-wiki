---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Handler_Model.js
lines: 58
sha256: 8e674edab93a74cabea39c100d738120866392e20616a2006aa48b34d344a47e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Model.js — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 모델 표시용 바인드 그룹(bind group) 레이아웃을 만든다(2–31). 유니폼 버퍼(uniform buffer) 0번은 정점(vertex)·프래그먼트(fragment) 단계에 공개한다. 1번은 프래그먼트용 `float`·`bgra8unorm`·`2d` 텍스처(texture)이고 2번은 두 단계용 filtering 샘플러(sampler)이다. 원문: `export function createModelBindGroupLayout(device) {` (2)<br>`return device.createBindGroupLayout({` (3)<br>`entries: [` (4)<br>`{` (5)<br>`binding: 0,` (7)<br>`visibility: GPUShaderStage.VERTEX \| GPUShaderStage.FRAGMENT,` (8)<br>`buffer: { type: 'uniform' }  // It's a uniform buffer` (9)<br>`},` (10)<br>`{` (11)<br>`binding: 1,` (13)<br>`visibility: GPUShaderStage.FRAGMENT,` (14)<br>`texture: {` (15)<br>`sampleType: 'float',` (16)<br>`format: 'bgra8unorm',  // imagedata for the google maps image` (17)<br>`viewDimension: '2d'` (18)<br>`}` (19)<br>`},` (20)<br>`{` (21)<br>`binding: 2,` (23)<br>`visibility: GPUShaderStage.VERTEX \| GPUShaderStage.FRAGMENT,` (24)<br>`sampler: {` (25)<br>`type: 'filtering'  // Nearest-neighbor sampling (no interpolation)` (26)<br>`}` (27)<br>`},` (28)<br>`]` (29)<br>`});` (30)<br>`}` (31) 유니폼 매개변수 예시의 주석: `// 0th binding: A uniform buffer (for parameters like time, etc.)` (6) [11-04 전수 검증 보완] |
| 34–58 | 바인드 그룹 생성에서 `uniformBuffer`·`txModelPNG_view`·`textureSampler_linear` 인수를 0–2번에 연결한다(35–55). 마지막 빈 줄을 포함한다. 원문: `export function createModelBindGroup(device, uniformBuffer, txModelPNG_view, textureSampler_linear) {` (35)<br>`return device.createBindGroup({` (36)<br>`layout: createModelBindGroupLayout(device),` (37)<br>`entries: [` (38)<br>`{` (39)<br>`binding: 0,` (40)<br>`resource: {` (41)<br>`buffer: uniformBuffer` (42)<br>`}` (43)<br>`},` (44)<br>`{` (45)<br>`binding: 1,` (46)<br>`resource: txModelPNG_view` (47)<br>`},` (48)<br>`{` (49)<br>`binding: 2,` (50)<br>`resource: textureSampler_linear` (51)<br>`},` (52)<br>`]` (53)<br>`});` (54)<br>`}` (55) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–26: 샘플러 설명에는 linear와 nearest-neighbor가 함께 적혀 있다. 실제 sampler type은 `filtering`이다.
- 17·35–47: 이미지 형식 주석은 Google Maps 이미지라고 적는다. 바인드 그룹 생성 함수의 해당 인수 이름은 `txModelPNG_view`이다.
