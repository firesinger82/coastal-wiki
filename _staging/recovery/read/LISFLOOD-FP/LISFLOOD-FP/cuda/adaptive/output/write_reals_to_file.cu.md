---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_reals_to_file.cu
lines: 48
sha256: 8db5f7ada55f7d1c1e50ed3d5cad5b2f0b75d83a54c88bb4c0e23e86f1a4bb15
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_reals_to_file.cu — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | `#include "write_reals_to_file.cuh"` (1), CUDA 호스트(host) 지시 `__host__` (3), `write_reals_to_file` 정의와 본문 시작(4–11). 파일명, 디렉터리, 장치(device) 실수 배열, 상수 참조 배열 길이를 받는다(6–9). 호스트 배열 `new real[array_length]`를 할당한다(12–13). 복사 크기는 `size_t bytes = array_length * sizeof(real);` (15)다. `copy_cuda`에 `h_results`, `d_results`, `bytes`를 전달한다(17–22). 빈 줄도 포함된다. 이 파일에는 조건부 전처리 분기가 없다. |
| 24–37 | 시작 시 4–11행 `write_reals_to_file` 본문 안. 파일 포인터를 선언하고 길이 255의 경로 버퍼를 널 문자로 초기화한다(24–26). `sprintf(fullpath, "%s%s%s", dirroot, filename, ".csv");` (28)로 경로를 만들고 `fopen(fullpath, "w")`로 연다(30). `if (NULL == fp)` (32)이면 파일명을 표준 오류에 출력하고 `exit(-1)`을 호출한다(34–35). 분기 뒤 빈 줄까지 포함된다(36–37). |
| 38–48 | 시작 시 4–11행 `write_reals_to_file` 본문 안이며 32행 오류 분기 밖. 열 이름 `results`를 쓴다(38). 원문 반복 조건은 `for (int i = 0; i < array_length; i++)` (40)다. 각 원소를 `fprintf(fp, "%" NUM_FRMT "\n", h_results[i]);` (42)로 한 줄씩 출력한다. `fclose(fp)`와 `delete[] h_results`를 실행하고 루틴을 닫는다(45–48). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·28: 경로 버퍼 크기는 255로 고정되어 있다. `sprintf` 호출 앞에 경로 길이 검사문이 없다.
- 28: 경로 형식은 `"%s%s%s"`다. 이 함수는 `dirroot`와 `filename` 사이에 경로 구분 문자를 추가하지 않는다.
