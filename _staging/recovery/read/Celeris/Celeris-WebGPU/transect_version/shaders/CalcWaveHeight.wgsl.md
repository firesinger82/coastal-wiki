---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/CalcWaveHeight.wgsl
lines: 77
sha256: 4695c7736fe73db71eb81c015c33fbb119682df71e68e40bf0d9c7537758adf3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# CalcWaveHeight.wgsl — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 단계 수 uniform과 상태·새 상태·평균·파고 입력 텍스처(texture), rgba32float 출력의 바인드 그룹(bind group) 0을 선언한다(1–11). 계산 셰이더(compute shader)는 작업 그룹 16×16으로 수위와 이전 누적값을 읽는다(14–23). 원문: `struct Globals {` (1); `n_time_steps_waveheight: i32` (2); `@group(0) @binding(0) var<uniform> globals: Globals;` (5); `@group(0) @binding(1) var txState: texture_2d<f32>;` (7); `@group(0) @binding(2) var txNewState: texture_2d<f32>;` (8); `@group(0) @binding(3) var txMeans: texture_2d<f32>;` (9); `@group(0) @binding(4) var txWaveHeight: texture_2d<f32>;` (10); `@group(0) @binding(5) var txtemp_WaveHeight: texture_storage_2d<rgba32float, write>;` (11); `@compute @workgroup_size(16, 16)` (14); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (15); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (16); `let eta_Old = textureLoad(txState, idx, 0).r;` (18); `let eta_New = textureLoad(txNewState, idx, 0).r;` (19); `let eta_mean = textureLoad(txMeans, idx, 0).r;` (21); `let old_vals = textureLoad(txWaveHeight, idx, 0);` (23) |
| 25–44 | 시작 시 15행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. Rayleigh 방식은 `globals.n_time_steps_waveheight <= 1`일 때 누적 제곱합을 0으로 설정하고 평균을 뺀 수위 제곱을 누적한다(26–35). 표준편차에 2.829·4.000을 곱하여 RMS 파고와 유의파고(significant wave height)를 계산한다(37–42). 원문: `// rayleigh` (25); `var sum_eta2 = old_vals.r;` (26); `if(globals.n_time_steps_waveheight <= 1) {` (27); `sum_eta2 = 0.0;` (28); `let eta = eta_New-eta_mean;` (31); `sum_eta2 = sum_eta2 + eta * eta;` (33); `var variance = sum_eta2 / f32(globals.n_time_steps_waveheight);` (35); `let sigma = sqrt(variance);` (37); `let H_mean = sigma * 2.829;  // RMS wave height` (39); `let H_sig = sigma * 4.000;   // sig wave height` (40); `let new_vals = vec4<f32>(sum_eta2, (H_sig-old_vals.b)/old_vals.b, H_sig, H_mean);` (42) [11-04 전수 검증 정정] |
| 45–77 | 시작 시 15행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. main의 영점 통과(zero-crossing) 파고 계산은 주석 처리되어 있다(45–73). 활성 경로는 제곱합·유의파고 상대변화·유의파고·RMS 파고를 출력한다(42·75). 원문: `// zero-crossing` (45); `//    var max_eta = old_vals.r;` (46); `//    var min_eta = old_vals.g;` (47); `//    var N_waves = old_vals.b;` (48); `//    var H_mean  = old_vals.a;` (49); `//  if(globals.n_time_steps_waveheight <= 1) {` (50); `//      N_waves = 0.0;` (51); `//      H_mean = 0.0;` (52); `//       max_eta = -999999.;` (53); `//       min_eta =  999999.;` (54); `//` (55); `//    } else if(eta_New>=0. && eta_Old<0.) {  // zero-up crossing` (56); `//       N_waves = N_waves + 1.0;` (57); `//` (58); `//       let H = max_eta - min_eta;` (59); `//` (60); `//        let update_frac = 1. / N_waves;` (61); `//        let old_frac = 1.0 - update_frac;` (62); `//` (63); `//        H_mean = old_frac * H_mean + update_frac * H;` (64); `//` (65); `//        max_eta = -999999.;` (66); `//        min_eta =  999999.;` (67); `//` (68); `//    } else {` (69); `//        max_eta = max(max_eta,eta_New);` (70); `//        min_eta = min(min_eta,eta_New);` (71); `//    let new_vals = vec4<f32>(max_eta, min_eta, N_waves, H_mean);` (73); `textureStore(txtemp_WaveHeight, idx, new_vals);` (75) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·45–73: eta_Old를 읽지만 이를 참조하는 영점 통과 분기는 주석이다.
- 35·42: 단계 수와 old_vals.b를 분모에 사용한다. 해당 분모가 0인 경우를 피하는 실행 조건은 없다.
