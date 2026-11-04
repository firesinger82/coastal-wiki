---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/vertex3D.wgsl
lines: 86
sha256: 0216f7ce8ec962505f26837bf4bf2f4d1d015083873d03252615d3a4b8dcd0b9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vertex3D.wgsl — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 입력 location 0의 pos와 출력 클립 위치·location 1의 uv 자료형을 선언한다. 원문: `struct VertexIn {` (1); `@location(0) pos : vec2<f32>,   // the vec2 from the buffer` (2); `struct VertexOut {` (5); `@builtin(position) clip_position: vec4<f32>,` (6); `@location(1) uv: vec2<f32>,` (7) |
| 10–61 | Globals에 색·지도·격자·카메라·설계 마찰·수직 배율·viewProj 필드를 순서대로 선언한다. viewProj 바이트 범위는 원문 주석이다. 원문: `struct Globals {` (10); `colorVal_max: f32,` (11); `colorVal_min: f32,` (12); `colorMap_choice: i32,` (13); `surfaceToPlot: i32,` (14); `showBreaking: i32,` (15); `GoogleMapOverlay: i32,` (16); `scaleX: f32,` (17); `scaleY: f32,` (18); `offsetX: f32,` (19); `offsetY: f32,` (20); `dx: f32,` (21); `dy: f32,` (22); `WIDTH: i32,` (23); `HEIGHT: i32,` (24); `rotationAngle_xy: f32,` (25); `shift_x: f32,` (26); `shift_y: f32,` (27); `forward: f32,` (28); `canvas_width_ratio: f32,` (29); `canvas_height_ratio: f32,` (30); `delta: f32,` (31); `CB_show: i32,` (32); `CB_xbuffer_uv: f32,` (33); `CB_xstart_uv: f32,` (34); `CB_width_uv: f32,` (35); `CB_ystart: i32,` (36); `CB_label_height: i32,` (37); `base_depth: f32,` (38); `NumberOfTimeSeries: i32,` (39); `time: f32,` (40); `west_boundary_type: i32,` (41); `east_boundary_type: i32,` (42); `south_boundary_type: i32,` (43); `north_boundary_type: i32,` (44); `designcomponent_Fric_Coral: f32,` (45); `designcomponent_Fric_Oyser: f32,` (46); `designcomponent_Fric_Mangrove: f32,` (47); `designcomponent_Fric_Kelp: f32,` (48); `designcomponent_Fric_Grass: f32,` (49); `designcomponent_Fric_Scrub: f32,` (50); `designcomponent_Fric_RubbleMound: f32,` (51); `designcomponent_Fric_Dune: f32,` (52); `designcomponent_Fric_Berm: f32,` (53); `designcomponent_Fric_Seawall: f32,` (54); `bathy_cmap_zero: f32,` (55); `renderZScale: f32,` (56); `temp1: f32,` (57); `temp2: f32,` (58); `viewProj: mat4x4<f32>, // bytes 192–255: your camera matrix` (59) |
| 62–69 | uniform과 수위·바닥 텍스처(texture), 두 sampler와 렌더 배열을 바인딩한다. 원문: `@group(0) @binding(0) var<uniform> globals: Globals;` (62); `@group(0) @binding(1) var etaTexture: texture_2d<f32>;` (64); `@group(0) @binding(2) var bottomTexture: texture_2d<f32>;` (65); `@group(0) @binding(13) var textureSampler: sampler;` (66); `@group(0) @binding(17) var textureSampler_linear: sampler;` (67); `@group(0) @binding(18) var txRenderVarsf16: texture_2d_array<f32>;` (68) |
| 70–86 | 정점 셰이더(vertex shader)는 pos를 uv로 변환한다. 수위 텍스처를 정수 격자 위치에서 직접 읽고 물리 x·y와 배율 적용 z를 만든다. viewProj 행렬을 곱해 클립 위치를 반환한다. 대체 textureSampleLevel은 주석이다. 원문: `@vertex` (70); `fn vs_main(v : VertexIn) -> VertexOut {` (71); `var out: VertexOut;` (72); `out.uv = v.pos * 0.5 + 0.5;` (75); `//let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;` (77); `var elev = textureLoad(etaTexture, vec2<i32>(i32(out.uv.x * f32(globals.WIDTH - 1)), i32(out.uv.y * f32(globals.HEIGHT - 1))), 0).r;` (78); `let worldX = out.uv.x * f32(globals.WIDTH - 1)  * globals.dx;` (80); `let worldY = out.uv.y * f32(globals.HEIGHT - 1) * globals.dy;` (81); `let worldZ = elev * globals.renderZScale;` (82); `out.clip_position = globals.viewProj * vec4<f32>(worldX, worldY, worldZ, 1.0);` (84); `return out;` (85) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65–68·77–78: 실행되는 수위 읽기는 etaTexture의 textureLoad이다. bottomTexture·두 sampler·txRenderVarsf16은 이 함수의 실행식에서 사용되지 않는다.
- 78: uv로 만든 정수 좌표를 textureLoad에 바로 사용한다. 좌표를 clamp하는 문장은 없다.
