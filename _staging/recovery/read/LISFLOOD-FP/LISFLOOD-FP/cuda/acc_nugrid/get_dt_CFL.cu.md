---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_dt_CFL.cu
lines: 49
sha256: 22bc857f6e7c0fa5d69282f83dff1b9a5156025f23a2870aab22c82160451fb3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_dt_CFL.cu — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#include "get_dt_CFL.cuh"` (1) 뒤 호스트(host) 함수 `__host__ NUMERIC_TYPE lis::cuda::acc_nugrid::get_dt_CFL` (3)을 정의한다. 인수는 `NUMERIC_TYPE*& d_dt_CFL`과 `const int& sol_len`이다(5–6). 호스트 최소값 저장소를 `new NUMERIC_TYPE`으로 할당한다(9). 장치(device) 저장소 할당은 `NUMERIC_TYPE* d_min_out = (NUMERIC_TYPE*)malloc_device(sizeof(NUMERIC_TYPE));` (10)이다. 임시 저장소 포인터는 NULL, 크기는 0으로 초기화한다(12–13). 이 파일에는 전처리 조건 분기가 없다. |
| 15–34 | 시작 시 3–8행의 `get_dt_CFL` 함수 안. CUB 최소값 축약(reduction)의 첫 호출을 `CHECK_CUDA_ERROR( cub::DeviceReduce::Min` (15)으로 감싼다. 인수 순서는 `d_temp_storage`, `temp_storage`, `d_dt_CFL`, `d_min_out`, `sol_len`이며 `) );`로 닫는다(16–22). NULL 임시 저장소를 전달한 호출 뒤 `d_temp_storage = malloc_device(temp_storage);` (24)로 임시 저장소를 할당한다. 두 번째 `CHECK_CUDA_ERROR( cub::DeviceReduce::Min` (26) 호출은 같은 순서의 인수로 최소값을 축약하고 `) );`로 닫는다(27–33). 호출 자체의 구현은 이 파일에 없다. |
| 35–49 | 시작 시 3–8행의 `get_dt_CFL` 함수 안. `copy_cuda`에 `h_min_out`, `d_min_out`, `sizeof(NUMERIC_TYPE)`을 넘겨 최소값 한 개를 복사한다(35–40). `NUMERIC_TYPE dt_min = *h_min_out;` (42)로 호스트 값을 보관한다. `free_device(d_min_out)`과 `free_device(d_temp_storage)`를 호출하고 호스트 저장소를 delete한다(44–46). `return dt_min;` (48) 뒤 함수를 닫는다(49). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–6·15–33: `sol_len`과 `d_dt_CFL`은 두 축약 호출에 그대로 전달된다. 이 함수에는 빈 입력 길이나 NULL 입력 포인터를 검사하는 조건문이 없다.
