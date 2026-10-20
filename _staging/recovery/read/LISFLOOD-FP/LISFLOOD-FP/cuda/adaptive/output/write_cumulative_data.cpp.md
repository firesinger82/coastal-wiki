---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_cumulative_data.cpp
lines: 53
sha256: 44fceb61f6ab9b7715969750254b46fa9e2306c1880c44f0f52c59dd21ec963c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_cumulative_data.cpp — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#include "write_cumulative_data.h"` (1), 빈 줄(2), `write_cumulative_data` 정의와 본문 시작(3–15). 시작 시계 `start`와 첫 단계 여부는 값으로 받는다(5·13). 현재 시간, 두 실행 시간, 시간 간격, 셀 수, 두 설정 객체는 상수 참조로 받는다(6–12). 이 파일에는 조건부 전처리 분기가 없다. |
| 16–29 | 시작 시 3–15행 `write_cumulative_data` 본문 안. 길이 255의 `fullpath`를 널 문자로 초기화한다(16). `sprintf(fullpath, "%s%c%s%s", plot_params.dirroot, '/', plot_params.resroot, ".cumu");` (18)로 경로를 만든다. 삼항 연산자를 포함한 원문은 `FILE* cumulative_input = fopen(fullpath, (first_t_step) ? "w" : "a");` (20)다. `if (NULL == cumulative_input)` (22)이면 표준 오류 출력 뒤 `exit(-1)`을 호출한다(24–25). `if (first_t_step) fprintf(cumulative_input, "simtime,runtime_mra,runtime_solver,runtime_total,dt,reduction\n");` (28)로 첫 단계에만 열 이름을 쓴다. 29행은 빈 줄이다. |
| 30–53 | 시작 시 3–15행 `write_cumulative_data` 본문 안이며 22행 오류 분기 밖. `const clock_t end = clock();` (30)을 실행한다. 축소 비율 식은 `const real compression = ( C(100.0) - C(100.0) * num_cells / (sim_params.xsz * sim_params.ysz) ) / C(100.0);` (32)다. `fprintf` (34–50)는 `NUM_FRMT`를 여섯 열에 사용한다(37–42). 출력 순서는 `current_time`, `time_mra`, `time_solver`, `time_mra + time_solver` (47), `dt`, `compression`이다(44–49). `fclose(cumulative_input)`을 호출하고 루틴을 닫는다(52–53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·30·34–50: 인수 `start`는 본문에서 참조되지 않는다. `end`는 `clock()` 결과를 받지만 이후 참조되지 않는다. `runtime_total` 열에는 `time_mra + time_solver`가 기록된다(28·47).
- 16·18: 경로 버퍼 크기는 255로 고정되어 있다. 경로 작성에는 `sprintf`를 사용한다. 이 함수에는 출력 경로 길이 검사문이 없다.
- 32: `compression`의 분모는 `sim_params.xsz * sim_params.ysz`다. 이 함수에는 두 크기가 0인지 검사하는 조건이 없다.
