---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/vertex3D.wgsl
lines: 85
sha256: 547083b47e50f1d3313793f0e31b90564bd187b4cf5efa691a28906c9e31bebf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vertex3D.wgsl — 판독 구간 기록

구간은 1행부터 85행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 정점 셰이더(vertex shader)의 입력·출력 구조체를 선언한다. 입력 pos는 버퍼에서 오는 위치 0의 vec2<f32>라는 주석을 둔다(1–3). 출력은 내장 클립 좌표(clip coordinates)와 위치 1의 텍스처(texture) 좌표 uv이다(5–8). 속성·자료형 원문: `struct VertexIn {` (1). `@location(0) pos : vec2<f32>,   // the vec2 from the buffer` (2). `};` (3). `struct VertexOut {` (5). `@builtin(position) clip_position: vec4<f32>,` (6). `@location(1) uv: vec2<f32>,` (7). `};` (8). |
| 10–61 | uniform 구조체(uniform structure) Globals를 선언한다(10–60). 색상 범위·표시 변수, 지도 변환, 격자 크기, 화면 변환, 색상 막대, 수심·시계열·시간, 경계 유형, 설계 요소 마찰, 지형 기준, 수직 배율, 임시 필드, 카메라 행렬이 순서대로 있다. 필드 자료형 전체 원문은 다음과 같다. 선언에는 필드 기본값이 없다. viewProj 주석은 bytes 192–255를 적는다(59). 이 파일에서는 지도 필드명이 GoogleMapOverlay이다(16). `struct Globals {` (10). `colorVal_max: f32,` (11). `colorVal_min: f32,` (12). `colorMap_choice: i32,` (13). `surfaceToPlot: i32,` (14). `showBreaking: i32,` (15). `GoogleMapOverlay: i32,` (16). `scaleX: f32,` (17). `scaleY: f32,` (18). `offsetX: f32,` (19). `offsetY: f32,` (20). `dx: f32,` (21). `dy: f32,` (22). `WIDTH: i32,` (23). `HEIGHT: i32,` (24). `rotationAngle_xy: f32,` (25). `shift_x: f32,` (26). `shift_y: f32,` (27). `forward: f32,` (28). `canvas_width_ratio: f32,` (29). `canvas_height_ratio: f32,` (30). `delta: f32,` (31). `CB_show: i32,` (32). `CB_xbuffer_uv: f32,` (33). `CB_xstart_uv: f32,` (34). `CB_width_uv: f32,` (35). `CB_ystart: i32,` (36). `CB_label_height: i32,` (37). `base_depth: f32,` (38). `NumberOfTimeSeries: i32,` (39). `time: f32,` (40). `west_boundary_type: i32,` (41). `east_boundary_type: i32,` (42). `south_boundary_type: i32,` (43). `north_boundary_type: i32,` (44). `designcomponent_Fric_Coral: f32,` (45). `designcomponent_Fric_Oyser: f32,` (46). `designcomponent_Fric_Mangrove: f32,` (47). `designcomponent_Fric_Kelp: f32,` (48). `designcomponent_Fric_Grass: f32,` (49). `designcomponent_Fric_Scrub: f32,` (50). `designcomponent_Fric_RubbleMound: f32,` (51). `designcomponent_Fric_Dune: f32,` (52). `designcomponent_Fric_Berm: f32,` (53). `designcomponent_Fric_Seawall: f32,` (54). `bathy_cmap_zero: f32,` (55). `renderZScale: f32,` (56). `temp1: f32,` (57). `temp2: f32,` (58). `viewProj: mat4x4<f32>, // bytes 192–255: your camera matrix` (59). `};` (60). |
| 62–69 | 바인드 그룹(bind group) 0의 바인딩을 선언한다. binding 0은 Globals uniform, 1·2는 texture_2d<f32>, 13·17은 sampler, 18은 texture_2d_array<f32>이다(62–68). 번호·변수명·자료형 원문: `@group(0) @binding(0) var<uniform> globals: Globals;` (62). `@group(0) @binding(1) var etaTexture: texture_2d<f32>;` (64). `@group(0) @binding(2) var bottomTexture: texture_2d<f32>;` (65). `@group(0) @binding(13) var textureSampler: sampler;` (66). `@group(0) @binding(17) var textureSampler_linear: sampler;` (67). `@group(0) @binding(18) var txRenderVarsf16: texture_2d_array<f32>;` (68). |
| 70–85 | @vertex 진입점 vs_main은 VertexIn을 받고 VertexOut을 반환한다(70–72). 위치를 uv로 변환하는 식은 vertex.wgsl 16행과 같은 0.5배·0.5 이동이며 여기서는 v.pos를 사용한다(75). textureSampleLevel은 out.uv·배열 층 0·명시적 밉 수준(mip level) 0.0의 r를 높이로 읽는다(77). uv에 격자 수와 간격을 곱해 세계 좌표(world coordinates) x·y를 만들고 높이에는 renderZScale을 곱한다(79–81). viewProj 행렬을 곱해 클립 좌표를 만들고 반환한다(83–85). 함수·좌표·샘플링·변환식 전체 원문: `@vertex` (70). `fn vs_main(v : VertexIn) -> VertexOut {` (71). `var out: VertexOut;` (72). `out.uv = v.pos * 0.5 + 0.5;` (75). `let elev = textureSampleLevel(txRenderVarsf16, textureSampler_linear, out.uv, 0, 0.0).r;` (77). `let worldX = out.uv.x * f32(globals.WIDTH)  * globals.dx;` (79). `let worldY = out.uv.y * f32(globals.HEIGHT) * globals.dy;` (80). `let worldZ = elev * globals.renderZScale;` (81). `out.clip_position = globals.viewProj * vec4<f32>(worldX, worldY, worldZ, 1.0);` (83). `return out;` (84). `}` (85). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 64–68·75–83: etaTexture·bottomTexture·textureSampler는 바인딩으로 선언되지만 이 파일의 vs_main에서는 참조하지 않는다. 높이 샘플링은 txRenderVarsf16과 textureSampler_linear를 사용한다.
- 77–83: 높이는 txRenderVarsf16의 층 0·r에서 읽는다. 이 진입점에는 surfaceToPlot에 따른 높이 선택 분기가 없다.
- 10–60: Globals는 viewProj 필드에서 끝난다. 함께 판독한 fragment.wgsl의 Globals는 IsOverlayMapLoaded 필드(11)를 쓰며 viewProj 뒤에 showArrows·arrow_scale·arrow_density 필드(55–57)를 더 선언한다. 이 파일의 대응 지도 필드명은 GoogleMapOverlay이다(16).
