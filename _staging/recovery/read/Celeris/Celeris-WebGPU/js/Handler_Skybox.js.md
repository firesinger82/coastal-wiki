---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_Skybox.js
lines: 57
sha256: 916df1c4e21f8962e61e9294ca1bde7f061540916ffe24e13b5a295b3b7fb735
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Skybox.js — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | skybox 바인드 그룹(bind group) 레이아웃을 반환한다. binding 0은 VERTEX 전용 uniform 버퍼이다. binding 1은 FRAGMENT 전용 float·bgra8unorm·cube 텍스처(texture)이다. binding 2는 FRAGMENT 전용 filtering 샘플러(sampler)이다. 원문(행 순서): `export function createSkyboxBindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `binding: 0,` (7); `visibility: GPUShaderStage.VERTEX,` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `binding: 1,` (13); `visibility: GPUShaderStage.FRAGMENT,` (14); `texture: {` (15); `sampleType: 'float',` (16); `format: 'bgra8unorm',  // imagedata for the skybox cube images` (17); `viewDimension: 'cube',  // Cube map view` (18); `},` (20); `binding: 2,` (23); `visibility: GPUShaderStage.FRAGMENT,` (24); `sampler: {` (25); `type: 'filtering'  // Nearest-neighbor sampling (no interpolation)` (26); `},` (28). 6행 주석은 uniform 매개변수 예로 time을 든다. [11-04 전수 검증 보완] |
| 34–57 | createSkyboxBindGroup은 레이아웃 생성 루틴을 호출한다. uniformBuffer, cubeView, cubeSampler를 binding 0·1·2에 연결한다. 마지막 빈 줄을 포함한다. 원문(행 순서): `export function createSkyboxBindGroup(device, uniformBuffer, cubeView, cubeSampler) {` (35); `return device.createBindGroup({` (36); `layout: createSkyboxBindGroupLayout(device),` (37); `entries: [` (38); `binding: 0,` (40); `resource: {` (41); `buffer: uniformBuffer` (42); `},` (44); `binding: 1,` (46); `resource: cubeView` (47); `},` (48); `binding: 2,` (50); `resource: cubeSampler` (51); `},` (52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·26: 샘플러 주석에는 linear 및 Nearest-neighbor sampling (no interpolation)이 함께 있다. 선언값은 type: 'filtering'이다.
