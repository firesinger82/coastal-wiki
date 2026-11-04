---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/shaders/Ship_pressure.compute
lines: 81
sha256: d825f765bc97136afed38d16a1059e8fe366595f8bd7b54ef3aa0fc8c0044159
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ship_pressure.compute — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 이 파일은 HLSL 형식의 계산 셰이더(compute shader)이다. 커널 Ship_Pressure와 선박 위치·폭·길이·흘수·방향·격자 간격·형상 계수·시간 float 변수를 선언한다(1–16). 출력 텍스처(texture)는 RWTexture2D<float4>이다(18). 원문: `#pragma kernel Ship_Pressure` (1); `float ship_posx;` (3); `float ship_posy;` (4); `float ship_width;` (5); `float ship_length;` (6); `float ship_draft;` (7); `float ship_heading;` (8); `float dx;` (9); `float dy;` (10); `float ship_c1a;` (11); `float ship_c1b;` (12); `float ship_c2;` (13); `float ship_c3a;` (14); `float ship_c3b;` (15); `float total_time;` (16); `RWTexture2D<float4> ship_pressure; // will store ship_pressure` (18) |
| 20–31 | ComputePressure는 방향 각도의 cos/sin 제곱과 sin(2*heading)으로 형상 계수를 회전한다(21–25). 격자 위치를 선박 중심 좌표로 바꾸고 이차 형식의 제곱에 음의 부호를 붙여 exp에 넣고 ship_draft를 곱하여 압력 수두를 계산한다(27–30). 원문: `float ComputePressure(float2 idx) {` (20); `float cos_heading2 = pow(cos(ship_heading), 2.0);` (21); `float sin_heading2 = pow(sin(ship_heading), 2.0);` (22); `float c1 = cos_heading2 * ship_c1a + sin_heading2 * ship_c1b;` (23); `float c2 = sin(2.0 * ship_heading) * ship_c2;` (24); `float c3 = sin_heading2 * ship_c3a + cos_heading2 * ship_c3b;` (25); `float xc = idx.x * dx - ship_posx;` (27); `float yc = idx.y * dy - ship_posy;` (28); `float Z = ship_draft * exp(-pow(c1 * pow(xc, 2.0) + 2.0 * c2 * xc * yc + c3 * pow(yc, 2.0), 2.0));` (30) [11-04 전수 검증 정정] |
| 32–61 | 시작 시 20행 `float ComputePressure(float2 idx) {` 블록 안. ComputePressure의 이동 압력파·진폭·파장·미터 변환 대안은 주석 처리되어 있다(32–57). 활성 반환은 30행에서 구한 Z이다(59). 원문: `// float speed = 306.0 * tanh((total_time + 300.0) / 4000.0);` (32); `// float front_distance = speed * total_time;` (33); `// float pwave_period = 2300.0 * pow(total_time, -0.1);` (34); `// float pwave_length = max(1.0e2, speed * pwave_period);` (35); `// float A_current = 2.0 * 3.1415 * sqrt(front_distance);` (37); `// float pmax = max(0.0, min(1.0e5, 2.2e6 / A_current * pow(tanh(front_distance / 3.0e5), 2.0)));` (38); `// float speed_t = 295.0 * tanh(total_time / 7000.0);` (40); `// float front_distance_t = speed_t * total_time;` (41); `// float pwave_period_t = 3300.0 * pow(total_time, -0.1);` (42); `// float pwave_length_t = max(1.0e2, speed_t * pwave_period_t);` (43); `// A_current = 2.0 * 3.1415 * pow((front_distance_t + 2.0e5), 0.9);` (45); `// float pmin = min(1.0e5, 8.0e8 / A_current);` (46); `// float x = idx.x * dx;` (48); `// float y = idx.y * dy;` (49); `// float p_loc = sqrt(pow((x - p_xo), 2.0) + pow((y - p_yo), 2.0));` (51); `// float loc_arg_crest = (p_loc - speed * total_time) / (pwave_length / 1.5);` (53); `// float loc_arg_troug = (p_loc - speed_t * total_time) / (pwave_length_t / 1.5);` (54); `// float Z = pmax * exp(-pow(loc_arg_crest, 2.0)) - pmin * exp(-pow(loc_arg_troug, 2.0));` (56); `// Z = Z / 9810; // convert to meters - Pass3 wants pressure head` (57); `return Z;` (59) |
| 62–81 | multi_compile은 8×8·16×16·32×32 스레드 변형을 선언한다(62). 전처리 조건에 따라 THREAD_X/Y를 정의한다(64–73). Ship_Pressure는 ComputePressure를 호출하고 Z를 출력의 x 성분에 저장한다(75–80). 원문: `#pragma multi_compile THREADS_8x8 THREADS_16x16 THREADS_32x32` (62); `#ifdef THREADS_8x8` (64); `#define THREAD_X 8` (65); `#define THREAD_Y 8` (66); `#elif defined(THREADS_16x16)` (67); `#define THREAD_X 16` (68); `#define THREAD_Y 16` (69); `#elif defined(THREADS_32x32)` (70); `#define THREAD_X 32` (71); `#define THREAD_Y 32` (72); `#endif` (73); `[numthreads(THREAD_X, THREAD_Y, 1)]` (75); `void Ship_Pressure(uint3 id : SV_DispatchThreadID) {` (76); `int2 idx = id.xy;` (77); `float Z = ComputePressure(float2(idx.x, idx.y));` (79); `ship_pressure[idx] = float4(Z, 0.0, 0.0, 0.0);` (80) 64–73행 전처리 조건 사슬에는 마지막 #else가 없다. 어느 매크로도 정의되지 않으면 이 사슬은 THREAD_X·THREAD_Y를 정의하지 않는다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–6·16·20–59: ship_width·ship_length는 선언 이후 활성 식에 사용되지 않는다. total_time은 주석 처리된 대안 식에만 등장한다.
- 75–80: 커널에는 출력 텍스처 크기를 검사하는 조건이 없다.
