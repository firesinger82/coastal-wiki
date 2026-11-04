---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Handler_ExtractNestedBoundaryTimeSeries.js
lines: 109
sha256: 0ed70609d5881762c7ff0c158ac36bd6124ed9e2e2f827af6ef4efacbc92e610
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_ExtractNestedBoundaryTimeSeries.js — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | 파일 주석·빈 줄과 `create_ExtractNestedBoundaryTimeSeries_BindGroupLayout` 시작(1–6). 계산 셰이더(compute shader)용 바인드 그룹(bind group)에서 0은 유니폼 버퍼(uniform buffer), 1은 unfilterable-float rgba32float 입력 텍스처(texture)이다(8–18). 2·3은 write-only rgba32float 2d 출력이다(21–36). 원문: `export function create_ExtractNestedBoundaryTimeSeries_BindGroupLayout(device) {` (4); `return device.createBindGroupLayout({` (5); `entries: [` (6); `{` (7); `binding: 0,` (8); `visibility: GPUShaderStage.COMPUTE,` (9); `buffer: { type: 'uniform' }` (10); `},` (11); `{` (12); `binding: 1,` (13); `visibility: GPUShaderStage.COMPUTE,` (14); `texture: {` (15); `sampleType: 'unfilterable-float',` (16); `format: 'rgba32float'` (17); `}` (18); `},` (19); `{` (20); `binding: 2,` (21); `visibility: GPUShaderStage.COMPUTE,` (22); `storageTexture: {` (23); `access: 'write-only',` (24); `format: 'rgba32float',` (25); `viewDimension: '2d'` (26); `}` (27); `},` (28); `{` (29); `binding: 3,` (30); `visibility: GPUShaderStage.COMPUTE,` (31); `storageTexture: {` (32); `access: 'write-only',` (33); `format: 'rgba32float',` (34); `viewDimension: '2d'` (35); `}` (36); `},` (37); `{` (38) |
| 39–68 | 시작 시 4행 레이아웃 함수·5행 생성 객체·6행 entries 배열 안. 4·5는 같은 출력 형식이다(39–54). 6은 마른 경계 정점 마스킹을 위한 바닥 입력이라는 주석과 rgba32float 입력 선언이다(56–64). 레이아웃을 닫는다(65–67). 원문: `binding: 4,` (39); `visibility: GPUShaderStage.COMPUTE,` (40); `storageTexture: {` (41); `access: 'write-only',` (42); `format: 'rgba32float',` (43); `viewDimension: '2d'` (44); `}` (45); `},` (46); `{` (47); `binding: 5,` (48); `visibility: GPUShaderStage.COMPUTE,` (49); `storageTexture: {` (50); `access: 'write-only',` (51); `format: 'rgba32float',` (52); `viewDimension: '2d'` (53); `}` (54); `},` (55); `{` (57); `binding: 6,` (58); `visibility: GPUShaderStage.COMPUTE,` (59); `texture: {` (60); `sampleType: 'unfilterable-float',` (61); `format: 'rgba32float'` (62); `}` (63); `}` (64); `]` (65); `});` (66); `}` (67) 구간 시작은 38행에서 열린 binding 4 객체 안이며 이 객체는 46행에서 닫힌다. 56행 주석은 바닥 높이를 이용해 마른 사각형 경계 표본을 0으로 만든다고 설명한다. [11-04 전수 검증 보완] |
| 69–109 | 이전 함수 원형 주석 뒤 `create_ExtractNestedBoundaryTimeSeries_BindGroup`가 txBottom 인수를 받는다(69–71). 0에 uniformBuffer, 1에 txState, 2..5에 남·북·서·동 출력, 6에 txBottom 뷰를 연결한다(72–107). 끝 함수·주석을 포함한다(108–109). 원문: `export function create_ExtractNestedBoundaryTimeSeries_BindGroup(device, uniformBuffer, txState, txNestedSouth, txNestedNorth, txNestedWest, txNestedEast, txBottom) {` (71); `return device.createBindGroup({` (72); `layout: create_ExtractNestedBoundaryTimeSeries_BindGroupLayout(device),` (73); `entries: [` (74); `{` (75); `binding: 0,` (76); `resource: {` (77); `buffer: uniformBuffer` (78); `}` (79); `},` (80); `{` (81); `binding: 1,` (82); `resource: txState.createView()` (83); `},` (84); `{` (85); `binding: 2,` (86); `resource: txNestedSouth.createView()` (87); `},` (88); `{` (89); `binding: 3,` (90); `resource: txNestedNorth.createView()` (91); `},` (92); `{` (93); `binding: 4,` (94); `resource: txNestedWest.createView()` (95); `},` (96); `{` (97); `binding: 5,` (98); `resource: txNestedEast.createView()` (99); `},` (100); `{` (102); `binding: 6,` (103); `resource: txBottom.createView()` (104); `}` (105); `]` (106); `});` (107); `}` (108) 70행 주석은 마른 셀의 `eta/hu/hv`를 0으로 출력하도록 txBottom을 포함한다고 설명한다. 101행 주석은 바닥 높이 텍스처를 건조 셀 출력 마스킹용으로 설명한다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
