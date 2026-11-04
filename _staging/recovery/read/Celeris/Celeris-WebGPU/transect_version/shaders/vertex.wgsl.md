---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/vertex.wgsl
lines: 19
sha256: 34a5ab61baf6b048c17e619aea32cd05f3754512c97f9b6689621c544ecf6a74
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vertex.wgsl — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 정점 셰이더(vertex shader)의 출력 구조체 VertexOutput을 선언한다(1–4). 클립 좌표(clip coordinates)는 @builtin(position)의 vec4<f32>이며, 텍스처(texture) 좌표 uv는 @location(1)의 vec2<f32>이다. 5행은 빈 줄이다. 자료형·속성 원문: `struct VertexOutput {` (1). `@builtin(position) clip_position: vec4<f32>,` (2). `@location(1) uv: vec2<f32>,` (3). `};` (4). |
| 6–14 | @vertex 진입점 vs_main은 @builtin(vertex_index)의 u32 인덱스를 받는다(6–7). 출력 변수를 선언하고 네 모서리의 2차원 위치 배열을 만든다(8–14). 순서는 왼쪽 아래·왼쪽 위·오른쪽 아래·오른쪽 위이다(10–13). 함수 선언·배열 크기·좌표 상수 전체 원문: `@vertex` (6). `fn vs_main(@builtin(vertex_index) in_vertex_index: u32) -> VertexOutput {` (7). `var out: VertexOutput;` (8). `let positions: array<vec2<f32>, 4> = array<vec2<f32>, 4>(` (9). `vec2<f32>(-1.0, -1.0),  // bottom-left` (10). `vec2<f32>(-1.0, 1.0),   // top-left` (11). `vec2<f32>(1.0, -1.0),   // bottom-right` (12). `vec2<f32>(1.0, 1.0)     // top-right` (13). `);` (14). |
| 15–19 | 시작 시 7행 vs_main 루틴 안. 인덱스로 위치를 고르고 위치를 0.5배 한 뒤 0.5를 더하여 uv를 만든다(15–16). z=0·w=1의 클립 좌표를 만들고 반환한 뒤 루틴을 끝낸다(17–19). 위치 선택·좌표 변환식 원문: `let position = positions[in_vertex_index];` (15). `out.uv = position * 0.5 + 0.5;` (16). `out.clip_position = vec4<f32>(position, 0.0, 1.0);` (17). `return out;` (18). `}` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–15: positions는 원소 4개 배열이며 in_vertex_index를 직접 배열 인덱스로 사용한다. 이 함수에는 인덱스 범위를 검사하는 조건이 없다. 실제 정점 호출 수는 이 파일에 없다.
