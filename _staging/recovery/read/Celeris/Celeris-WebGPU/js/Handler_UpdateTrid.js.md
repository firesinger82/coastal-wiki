---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_UpdateTrid.js
lines: 81
sha256: 9af4dcf1f9ec02e276637f4231c9698de2c3b583573cef3fa0fdceebf3574ca9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_UpdateTrid.js — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–52 | 파일명 주석과 계산 셰이더(compute shader)용 바인드 그룹(bind group) 레이아웃을 선언한다. binding 0은 uniform 버퍼이다. 읽기 텍스처(texture) 1–2는 unfilterable-float·rgba32float이다. 출력 3–4는 write-only·rgba32float·2d이다. 원문(행 순서): `export function create_UpdateTrid_BindGroupLayout(device) {` (2); `return device.createBindGroupLayout({` (3); `entries: [` (4); `binding: 0,` (7); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (8); `buffer: { type: 'uniform' }  // It's a uniform buffer` (9); `},` (10); `binding: 1,` (13); `visibility: GPUShaderStage.COMPUTE,` (14); `texture: {` (15); `sampleType: 'unfilterable-float',` (16); `format: 'rgba32float'` (17); `},` (19); `binding: 2,` (22); `visibility: GPUShaderStage.COMPUTE,` (23); `texture: {` (24); `sampleType: 'unfilterable-float',` (25); `format: 'rgba32float'` (26); `},` (28); `binding: 3,` (31); `visibility: GPUShaderStage.COMPUTE,` (32); `storageTexture: {` (33); `access: 'write-only',      // This texture is only for writing data` (34); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (35); `viewDimension: '2d'       // The texture is a 2D texture` (36); `},` (38); `binding: 4,` (41); `visibility: GPUShaderStage.COMPUTE,` (42); `storageTexture: {` (43); `access: 'write-only',      // This texture is only for writing data` (44); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (45); `viewDimension: '2d'       // The texture is a 2D texture` (46). 6행 주석은 uniform 매개변수 예로 time을 든다. 12·21행 주석은 fragment shader의 표본 추출을 설명하지만 visibility는 COMPUTE이다. 30·40행 주석은 계산 셰이더의 결과 쓰기를 설명한다. [11-04 전수 검증 보완] |
| 53–81 | create_UpdateTrid_BindGroup은 레이아웃 생성 루틴을 호출한다. uniformBuffer, txBottom, txNewState, coefMatx, coefMaty를 binding 0–4에 순서대로 연결한다. 원문(행 순서): `export function create_UpdateTrid_BindGroup(device, uniformBuffer, txBottom, txNewState, coefMatx, coefMaty) {` (53); `return device.createBindGroup({` (54); `layout: create_UpdateTrid_BindGroupLayout(device),` (55); `entries: [` (56); `binding: 0,` (58); `resource: {` (59); `buffer: uniformBuffer` (60); `},` (62); `binding: 1,` (64); `resource: txBottom.createView()` (65); `},` (66); `binding: 2,` (68); `resource: txNewState.createView()` (69); `},` (70); `binding: 3,` (72); `resource: coefMatx.createView()` (73); `},` (74); `binding: 4,` (76); `resource: coefMaty.createView()` (77); `},` (78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·2: 파일 머리말은 Handler_Tridiag.js라고 적지만 공개 루틴 이름은 create_UpdateTrid_BindGroupLayout이다.
- 30–31·40–41: 출력 주석은 4th·5th binding이라고 적지만 실제 binding 값은 3·4이다.
