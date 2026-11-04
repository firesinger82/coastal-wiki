---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_Updateneardry.js
lines: 54
sha256: b64a8ae81e4347213d850baeed47874874ba6be2ff5d0e648ceb06c01fb15bd1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Updateneardry.js — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 계산 셰이더(compute shader)용 바인드 그룹(bind group) 레이아웃을 선언한다. binding 0은 uniform 버퍼이다. binding 1은 unfilterable-float·rgba32float 읽기 텍스처(texture)이다. binding 2는 write-only·rgba32float·2d 출력이다. 원문(행 순서): `export function create_Updateneardry_BindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `binding: 0,` (7); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `binding: 1,` (13); `visibility: GPUShaderStage.COMPUTE,` (14); `texture: {` (15); `sampleType: 'unfilterable-float',` (16); `format: 'rgba32float'` (17); `},` (19); `binding: 2,` (22); `visibility: GPUShaderStage.COMPUTE,` (23); `storageTexture: {` (24); `access: 'write-only',      // This texture is only for writing data` (25); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (26); `viewDimension: '2d'       // The texture is a 2D texture` (27). 6행 주석은 uniform 매개변수 예로 time을 든다. 21행 주석은 계산 셰이더의 결과 쓰기를 설명한다. [11-04 전수 검증 보완] |
| 34–54 | create_Updateneardry_BindGroup은 uniformBuffer, txBottom, txtemp_bottom을 binding 0–2에 연결한다. 원문(행 순서): `export function create_Updateneardry_BindGroup(device, uniformBuffer, txBottom, txtemp_bottom) {` (34); `return device.createBindGroup({` (35); `layout: create_Updateneardry_BindGroupLayout(device),` (36); `entries: [` (37); `binding: 0,` (39); `resource: {` (40); `buffer: uniformBuffer` (41); `},` (43); `binding: 1,` (45); `resource: txBottom.createView()` (46); `},` (47); `binding: 2,` (49); `resource: txtemp_bottom.createView()` (50); `},` (51). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12·14: 입력 텍스처 주석은 fragment shader를 말하지만 visibility는 COMPUTE이다.
