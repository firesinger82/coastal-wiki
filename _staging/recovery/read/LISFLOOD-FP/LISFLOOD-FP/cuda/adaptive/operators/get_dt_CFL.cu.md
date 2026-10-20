---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_dt_CFL.cu
lines: 50
sha256: 6b6fd326e4e6481d6c1e8f4eacc4fe531ae863e9e8a8cbace809aabff51d674d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_dt_CFL.cu — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–24 | 헤더를 포함하고 CUDA 호스트 함수(host function) `get_dt_CFL`을 정의한다(1–9). 장치 CFL(Courant–Friedrichs–Lewy) 배열 포인터 참조와 해 길이 참조를 받는다(6–7). 호스트·장치의 실수 출력 저장소를 할당하고 임시 저장소 포인터를 NULL, 바이트 수를 0으로 초기화한다(10–14). 첫 `cub::DeviceReduce::Min` 호출을 `CHECK_CUDA_ERROR`로 감싸 필요한 저장소 크기를 질의한다(16–23). 전처리 조건 분기는 없다. 오류 검사 매크로의 정의는 이 파일에 없다. 원문: `__host__` (3); `real* d_min_out = (real*)malloc_device(sizeof(real));` (11); `CHECK_CUDA_ERROR( cub::DeviceReduce::Min`<br>`(`<br>`d_temp_storage,`<br>`temp_storage,`<br>`d_dt_CFL,`<br>`d_min_out,`<br>`sol_len`<br>`) );` (16–23). |
| 25–50 | 시작 시 3–9행 `get_dt_CFL` 안. `malloc_device(temp_storage)`로 임시 저장소를 할당한다(25). 두 번째 `cub::DeviceReduce::Min`을 호출하여 최솟값을 구한다(27–34). `copy_cuda`로 실수 하나를 호스트로 복사하고 dt_min에 보관한다(36–43). 두 장치 저장소와 호스트 객체를 해제한 뒤 최솟값을 반환한다(45–50). 원문: `CHECK_CUDA_ERROR( cub::DeviceReduce::Min`<br>`(`<br>`d_temp_storage,`<br>`temp_storage,`<br>`d_dt_CFL,`<br>`d_min_out,`<br>`sol_len`<br>`) );` (27–34); `copy_cuda`<br>`(`<br>`h_min_out,`<br>`d_min_out,`<br>`sizeof(real)`<br>`);` (36–41); `real dt_min = *h_min_out;` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–7·16–34: 입력 길이 `sol_len`을 두 축약(reduction) 호출에 그대로 전달한다. 이 함수에는 빈 배열이나 음수 길이를 별도로 검사하는 조건문이 없다.
