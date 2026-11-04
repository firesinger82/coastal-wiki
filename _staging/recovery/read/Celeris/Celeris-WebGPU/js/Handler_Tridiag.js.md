---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_Tridiag.js
lines: 109
sha256: fbf0dbf450021d96324653e83fb13e31c856988171736a9f2727ad6752303fc5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Tridiag.js — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 삼중대각(tridiagonal) 처리의 바인드 그룹(bind group) 레이아웃을 선언한다. 계산 셰이더(compute shader)용 binding 0은 uniform 버퍼이다. 입력 텍스처(texture) 1–3은 unfilterable-float·rgba32float이다. 원문(행 순서): `export function create_Tridiag_BindGroupLayout(device) {` (3); `return device.createBindGroupLayout({` (4); `entries: [` (5); `binding: 0,` (8); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (9); `buffer: { type: 'uniform' }  // It's a uniform buffer` (10); `},` (11); `binding: 1,` (14); `visibility: GPUShaderStage.COMPUTE,` (15); `texture: {` (16); `sampleType: 'unfilterable-float',` (17); `format: 'rgba32float'` (18); `},` (20); `binding: 2,` (23); `visibility: GPUShaderStage.COMPUTE,` (24); `texture: {` (25); `sampleType: 'unfilterable-float',` (26); `format: 'rgba32float'` (27); `},` (29); `binding: 3,` (32); `visibility: GPUShaderStage.COMPUTE,` (33); `texture: {` (34); `sampleType: 'unfilterable-float',` (35); `format: 'rgba32float'` (36); `},` (38). 7행 주석은 uniform 매개변수 예로 time을 든다. [11-04 전수 검증 보완] |
| 39–72 | 시작 시 3행 create_Tridiag_BindGroupLayout 루틴·4행 호출·5행 entries 배열 안. 출력 4–5는 write-only·rgba32float·2d이다. 입력 6은 unfilterable-float·rgba32float이다. 레이아웃 종료와 빈 줄을 포함한다. 원문(행 순서): `binding: 4,` (41); `visibility: GPUShaderStage.COMPUTE,` (42); `storageTexture: {` (43); `access: 'write-only',      // This texture is only for writing data` (44); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (45); `viewDimension: '2d'       // The texture is a 2D texture` (46); `},` (48); `binding: 5,` (51); `visibility: GPUShaderStage.COMPUTE,` (52); `storageTexture: {` (53); `access: 'write-only',      // This texture is only for writing data` (54); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (55); `viewDimension: '2d'       // The texture is a 2D texture` (56); `},` (58); `binding: 6,` (61); `visibility: GPUShaderStage.COMPUTE,` (62); `texture: {` (63); `sampleType: 'unfilterable-float',` (64); `format: 'rgba32float'` (65); `},` (67). 40·50행 주석은 계산 셰이더의 결과 쓰기를 설명한다. 60행 주석은 fragment shader의 표본 추출을 설명한다. entries 배열·호출·함수는 각각 68·69·70행에서 닫힌다. [11-04 전수 검증 보완] |
| 73–109 | create_Tridiag_BindGroup이 uniformBuffer, newcoef, current_state, current_stateUVstar, txtemp, txtemp2, txBottom을 binding 0–6에 연결한다. 원문(행 순서): `export function create_Tridiag_BindGroup(device, uniformBuffer, newcoef, current_state, current_stateUVstar, txtemp, txtemp2, txBottom) {` (73); `return device.createBindGroup({` (74); `layout: create_Tridiag_BindGroupLayout(device),` (75); `entries: [` (76); `binding: 0,` (78); `resource: {` (79); `buffer: uniformBuffer` (80); `},` (82); `binding: 1,` (84); `resource: newcoef.createView()` (85); `},` (86); `binding: 2,` (88); `resource: current_state.createView()` (89); `},` (90); `binding: 3,` (92); `resource: current_stateUVstar.createView()` (93); `},` (94); `binding: 4,` (96); `resource: txtemp.createView()` (97); `},` (98); `binding: 5,` (100); `resource: txtemp2.createView()` (101); `},` (102); `binding: 6,` (104); `resource: txBottom.createView()` (105); `},` (106). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13·22·31·9–34: 입력 텍스처 주석은 fragment shader를 말하지만 visibility는 COMPUTE이다.
