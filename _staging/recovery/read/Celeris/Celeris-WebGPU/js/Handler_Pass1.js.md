---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_Pass1.js
lines: 111
sha256: 936984115a0a214d7612f3dd3d1b4ef52a56b39bd7a19b421266da01c839e78d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass1.js — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 머리말과 `create_Pass1_BindGroupLayout` 시작(1–5). 계산 셰이더(compute shader)용 바인드 그룹(bind group)에서 0은 유니폼 버퍼(uniform buffer), 1·2는 unfilterable-float rgba32float 입력 텍스처(texture), 3은 write-only rgba32float 2d 출력이다(8–38). 원문: `export function create_Pass1_BindGroupLayout(device) {` (3); `return device.createBindGroupLayout({` (4); `entries: [` (5); `{` (6); `binding: 0,` (8); `visibility: GPUShaderStage.COMPUTE, // This buffer is only visible to the compute stage` (9); `buffer: { type: 'uniform' }  // It's a uniform buffer` (10); `},` (11); `{` (12); `binding: 1,` (14); `visibility: GPUShaderStage.COMPUTE,` (15); `texture: {` (16); `sampleType: 'unfilterable-float',` (17); `format: 'rgba32float'` (18); `}` (19); `},` (20); `{` (21); `binding: 2,` (23); `visibility: GPUShaderStage.COMPUTE,` (24); `texture: {` (25); `sampleType: 'unfilterable-float',` (26); `format: 'rgba32float'` (27); `}` (28); `},` (29); `{` (30); `binding: 3,` (32); `visibility: GPUShaderStage.COMPUTE,` (33); `storageTexture: {` (34); `access: 'write-only',      // This texture is only for writing data` (35); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (36); `viewDimension: '2d'       // The texture is a 2D texture` (37); `}` (38); `},` (39); `{` (40) 7행 주석은 uniform을 시간 등의 매개변수용으로 설명한다. 13·22행 주석은 입력을 fragment shader 표본화용이라고 적지만 실제 visibility는 COMPUTE이다. [11-04 전수 검증 보완] |
| 41–74 | 시작 시 3행 레이아웃 함수·4행 생성 객체·5행 entries 배열 안. 4·5·6은 모두 write-only rgba32float 2d 저장 텍스처이다(42–68). 레이아웃 종료·빈 줄을 포함한다(70–74). 원문: `binding: 4,` (42); `visibility: GPUShaderStage.COMPUTE,` (43); `storageTexture: {` (44); `access: 'write-only',      // This texture is only for writing data` (45); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (46); `viewDimension: '2d'       // The texture is a 2D texture` (47); `}` (48); `},` (49); `{` (50); `binding: 5,` (52); `visibility: GPUShaderStage.COMPUTE,` (53); `storageTexture: {` (54); `access: 'write-only',      // This texture is only for writing data` (55); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (56); `viewDimension: '2d'       // The texture is a 2D texture` (57); `}` (58); `},` (59); `{` (60); `binding: 6,` (62); `visibility: GPUShaderStage.COMPUTE,` (63); `storageTexture: {` (64); `access: 'write-only',      // This texture is only for writing data` (65); `format: 'rgba32float',    // Data format: 32-bit floating point values for red, green, blue, and alpha channels` (66); `viewDimension: '2d'       // The texture is a 2D texture` (67); `}` (68); `}` (69); `]` (70); `});` (71); `}` (72) 구간 시작은 40행에서 열린 binding 4 객체 안이며 이 객체는 49행에서 닫힌다. [11-04 전수 검증 보완] |
| 75–111 | `create_Pass1_BindGroup`는 0에 uniformBuffer, 1..6에 txState·txBottom·txH·txU·txV·txC 뷰를 연결한다(75–111). 원문: `export function create_Pass1_BindGroup(device, uniformBuffer, txState, txBottom, txH, txU, txV, txC) {` (75); `return device.createBindGroup({` (76); `layout: create_Pass1_BindGroupLayout(device),` (77); `entries: [` (78); `{` (79); `binding: 0,` (80); `resource: {` (81); `buffer: uniformBuffer` (82); `}` (83); `},` (84); `{` (85); `binding: 1,` (86); `resource: txState.createView()` (87); `},` (88); `{` (89); `binding: 2,` (90); `resource: txBottom.createView()` (91); `},` (92); `{` (93); `binding: 3,` (94); `resource: txH.createView()` (95); `},` (96); `{` (97); `binding: 4,` (98); `resource: txU.createView()` (99); `},` (100); `{` (101); `binding: 5,` (102); `resource: txV.createView()` (103); `},` (104); `{` (105); `binding: 6,` (106); `resource: txC.createView()` (107); `},` (108); `]` (109); `});` (110); `}` (111) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41·51: binding 4·5의 주석은 fragment shader 표본화를 설명하지만 실행 선언은 COMPUTE·write-only storageTexture이다(42–58).
