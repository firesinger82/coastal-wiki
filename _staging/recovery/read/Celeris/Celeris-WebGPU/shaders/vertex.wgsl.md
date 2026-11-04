---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/vertex.wgsl
lines: 19
sha256: 90a9d0ab4829f562a7ae1c063f2f7adb9ce4cf536198979fe798d4ddcad665f7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vertex.wgsl — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | 정점 출력은 내장 clip_position vec4와 location 1의 uv vec2이다. 원문: `struct VertexOutput {` (1); `@builtin(position) clip_position: vec4<f32>,` (2); `@location(1) uv: vec2<f32>,` (3) |
| 6–19 | 정점 셰이더(vertex shader)의 vs_main은 네 모서리 배열을 vertex_index로 읽는다. 좌표를 절반 배율·절반 이동으로 uv에 대응시킨다. z=0,w=1의 클립 위치를 반환한다. 원문: `@vertex` (6); `fn vs_main(@builtin(vertex_index) in_vertex_index: u32) -> VertexOutput {` (7); `var out: VertexOutput;` (8); `let positions: array<vec2<f32>, 4> = array<vec2<f32>, 4>(` (9); `vec2<f32>(-1.0, -1.0),  // bottom-left` (10); `vec2<f32>(-1.0, 1.0),   // top-left` (11); `vec2<f32>(1.0, -1.0),   // bottom-right` (12); `vec2<f32>(1.0, 1.0)     // top-right` (13); `);` (14); `let position = positions[in_vertex_index];` (15); `out.uv = position * 0.5 + 0.5;` (16); `out.clip_position = vec4<f32>(position, 0.0, 1.0);` (17); `return out;` (18) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–15: positions 크기는 4이고 in_vertex_index를 직접 인덱스로 쓴다. 이 함수에 범위 검사 조건은 없다.
