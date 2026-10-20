---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_c_prop_data.cu
lines: 87
sha256: 66a303a627b6cef3ff5dafd61dc05b8802f99277dca4b07ff4ed2e67d95e06d6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_c_prop_data.cu — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#include "write_c_prop_data.cuh"` (1), 빈 줄(2), CUDA 호스트(host) 지시 `__host__` (3)와 `write_c_prop_data` 정의·인수·본문 시작(4–18). 출력 설정, 시작 시계, 해석기 설정, 모의 설정, 조립 해(assembled solution), 현재 시간, 두 실행 시간, 시간 간격, 셀 수, 첫 시간 단계 여부를 상수 참조로 받는다(6–16). 이 파일에는 조건부 전처리 분기가 없다. |
| 19–49 | 시작 시 4–18행 `write_c_prop_data` 본문 안. `write_cumulative_data`에 시작 시계·현재 시간·다중해상도 분석(multiresolution analysis) 시간 `time_mra`·해석 시간·시간 간격·셀 수·설정·첫 단계 여부를 전달한다(19–30). `append_reals_to_file`을 두 번 호출한다(32–48). 이름은 `"qx0-c-prop"` (34)와 `"qy0-c-prop"` (43)이며, 각각 `d_assem_sol.qx0` (36)와 `d_assem_sol.qy0` (45)를 `d_assem_sol.length`개씩 같은 `plot_params.dirroot`에 전달한다. 두 호출은 `first_t_step`도 전달한다(38·47). |
| 50–87 | 시작 시 4–18행 `write_c_prop_data` 본문 안. 원문 조건 `if (solver_params.solver_type == MWDG2)` (50)의 참 분기에서만 `append_reals_to_file`을 네 번 호출한다(52–85). 이름과 배열은 `"qx1x-c-prop"`·`d_assem_sol.qx1x` (54·56), `"qx1y-c-prop"`·`d_assem_sol.qx1y` (63·65), `"qy1x-c-prop"`·`d_assem_sol.qy1x` (72·74), `"qy1y-c-prop"`·`d_assem_sol.qy1y` (80·82)다. 각 호출은 같은 출력 디렉터리, `d_assem_sol.length`, `first_t_step`을 사용한다. 별도 else 분기는 없다. 분기와 루틴을 닫는다(86–87). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
