---
file: models/Celeris/raw/source_code/Celeris-WebGPU/shaders/CalcWaveHeight.wgsl
lines: 77
sha256: 554596bd0fc5d8b2895ec83a93137a8b0e77c5da615140f138076eb7091cd49d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# CalcWaveHeight.wgsl — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | Globals에 파고 누적 횟수를 선언한다. 계산 셰이더(compute shader)는 16×16 작업군을 사용한다. group 0 binding 0–5에 uniform, 입력 텍스처(texture) 네 개와 rgba32float 출력을 둔다. 이전·현재·평균 수면고와 누적값을 읽는다. 원문: `struct Globals {` (1); `n_time_steps_waveheight: i32` (2); `@group(0) @binding(0) var<uniform> globals: Globals;` (5); `@group(0) @binding(1) var txState: texture_2d<f32>;` (7); `@group(0) @binding(2) var txNewState: texture_2d<f32>;` (8); `@group(0) @binding(3) var txMeans: texture_2d<f32>;` (9); `@group(0) @binding(4) var txWaveHeight: texture_2d<f32>;` (10); `@group(0) @binding(5) var txtemp_WaveHeight: texture_storage_2d<rgba32float, write>;` (11); `@compute @workgroup_size(16, 16)` (14); `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` (15); `let idx = vec2<i32>(i32(id.x), i32(id.y));` (16); `let eta_Old = textureLoad(txState, idx, 0).r;` (18); `let eta_New = textureLoad(txNewState, idx, 0).r;` (19); `let eta_mean = textureLoad(txMeans, idx, 0).r;` (21); `let old_vals = textureLoad(txWaveHeight, idx, 0);` (23) |
| 25–43 | 시작 시 15행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 횟수<=1이면 제곱합을 초기화한다. 평균을 뺀 수면고의 제곱을 누적한다. 표준편차에 2.829와 4.000을 곱한다. 제곱합·유의파고 상대 변화·유의파고·RMS 파고를 출력 벡터로 만든다. 원문: `var sum_eta2 = old_vals.r;` (26); `if(globals.n_time_steps_waveheight <= 1) {` (27); `sum_eta2 = 0.0;` (28); `let eta = eta_New-eta_mean;` (31); `sum_eta2 = sum_eta2 + eta * eta;` (33); `var variance = sum_eta2 / f32(globals.n_time_steps_waveheight);` (35); `let sigma = sqrt(variance);` (37); `let H_mean = sigma * 2.829;  // RMS wave height` (39); `let H_sig = sigma * 4.000;   // sig wave height` (40); `let new_vals = vec4<f32>(sum_eta2, (H_sig-old_vals.b)/old_vals.b, H_sig, H_mean);` (42) |
| 44–77 | 시작 시 15행 `fn main(@builtin(global_invocation_id) id: vec3<u32>) {` 블록 안. 영점 통과(zero-crossing) 방식은 전체 주석 처리되어 있다. 현재 실행 경로는 new_vals를 저장하고 종료한다. 원문: `textureStore(txtemp_WaveHeight, idx, new_vals);` (75)  누락된 주석 원문: `//    var max_eta = old_vals.r;` (46);`//    var min_eta = old_vals.g;` (47);`//    var N_waves = old_vals.b;` (48);`//    var H_mean  = old_vals.a;` (49);`//  if(globals.n_time_steps_waveheight <= 1) {` (50);`//      N_waves = 0.0;` (51);`//      H_mean = 0.0;` (52);`//       max_eta = -999999.;` (53);`//       min_eta =  999999.;` (54);`//    } else if(eta_New>=0. && eta_Old<0.) {  // zero-up crossing` (56);`//       N_waves = N_waves + 1.0;` (57);`//       let H = max_eta - min_eta;` (59);`//        let update_frac = 1. / N_waves;` (61);`//        let old_frac = 1.0 - update_frac;` (62);`//        H_mean = old_frac * H_mean + update_frac * H;` (64);`//        max_eta = -999999.;` (66);`//        min_eta =  999999.;` (67);`//    } else {` (69);`//        max_eta = max(max_eta,eta_New);` (70);`//        min_eta = min(min_eta,eta_New);` (71);`//    }` (72);`//    let new_vals = vec4<f32>(max_eta, min_eta, N_waves, H_mean);` (73). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·45–73: eta_Old는 읽지만 실행 계산에는 사용하지 않으며 영점 통과 경로는 주석이다.
- 35·42: 누적 횟수와 old_vals.b를 분모로 쓰며 이 분모가 0인지 검사하는 실행 조건은 없다.
