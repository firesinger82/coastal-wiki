---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/rain/Rainfall_uniform.h
lines: 95
sha256: 0f0e2e295695f266b346bd5b1c4b29cba8d82f7b001e2ac3e884e8ccc6ec4a40
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# Rainfall_uniform.h — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1)로 중복 포함을 막는다. CUDA 실행시간 헤더(cuda_runtime.h), 표준 입출력·메모리·문자열 헤더와 lisflood.h를 포함한다(3–9). 이 파일 자체에는 CUDA 함수 한정자나 커널 호출이 없다. Rainfall_uniform 구조체는 강우 값 value, 32자 timeseries의 널 초기화, `int         row = 0;` (15)를 가진다(11–15). 생성자는 전달받은 NUMERIC_TYPE 값을 value로 복사한다(17–23). |
| 25–46 | update_rainfall은 강우 파일명과 현재 시각을 받는다(25–30). 255자 입력 버퍼와 32자 buf를 준비하고 fopen으로 파일을 매번 연다(31–34). `if (NULL == fp)` (36)이면 오류 메시지를 내고 exit(-1)로 종료한다(38–39). timeseriesptr에 멤버 배열 주소를 넣고 첫 줄을 fgets·sscanf로 읽는다(42–45). |
| 47–69 | 시작 시 25행 update_rainfall 안. 두 강우 값과 두 시각을 C(0.0), 행 수를 0, 시간 배율을 1로 초기화한다(47–54). 둘째 줄의 행 수와 단위 문자열을 읽는다(56–58). 시간 배율은 `time_multiplier = (!strncmp(buf, "seconds", 7)) ? 1 : (!strncmp(buf, "minutes", 7)) ? 60 : 3600;` (60)이다. `for (int i = 0; i < row + 1; i++) fgets(str, sizeof(str), fp);` (62)로 row 위치까지 읽고 value_1·t_1과 다음 줄의 value_2·t_2를 sscanf로 받는다(64–68). |
| 70–83 | 시작 시 25행 update_rainfall 안. `if (time_now > t_2*time_multiplier)` (70)이면 row를 한 번 증가시킨다(72). `t_1 = t_2*time_multiplier;` (74)로 앞 시각을 갱신하고 value_1에 value_2를 복사한다(75). 그 분기 안에서 다음 줄을 fgets·sscanf로 읽는다(77–79). 분기 종료 뒤 fclose를 호출한다(80–82). |
| 84–95 | 시작 시 25행 update_rainfall 안. `if (row + 1 >= num_rows_timeseries)` (84)이면 row를 한 번 줄이고 `value = C(0.0);` (87)로 강우를 0으로 만든다. `else {` (89)에서는 선형 보간(linear interpolation) `value = value_1 + (value_2 - value_1) / ((t_2 - t_1) * time_multiplier) * (time_now - t_1 * time_multiplier);` (90)을 적용하고 `value /= (C(1000.0) * C(3600.0));` (91)로 값을 변환한다. 함수·구조체를 닫는다(92–95). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·42: timeseriesptr는 timeseries 주소를 받은 뒤 이 함수에서 다시 사용되지 않는다.
- 44–79: fgets와 sscanf의 반환값을 검사하는 조건이 없다.
- 70–79: 시간 구간 전진은 while이 아닌 단일 if이며 한 호출에서 row를 한 번만 증가시킨다.
- 74·90: 전진 분기에서 t_1에 t_2*time_multiplier를 넣고, 보간식에서는 t_1에 time_multiplier를 다시 곱한다. 두 식을 그대로 기록했다.
