---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/init_neighbours.cu
lines: 80
sha256: a9be71cd841ec504184b804dba9a249cd714ce1ce0057bb408d8968e48230aaf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# init_neighbours.cu — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | 관련 헤더와 `helper_cuda.h`·`cub/cub.cuh`를 포함한다(1–3). 호스트 함수 지정은 `__host__ lis::cuda::acc_nugrid::NonUniformNeighbours lis::cuda::acc_nugrid::init_neighbours` (5)이다. 인수는 값으로 전달되는 `AssembledSolution d_assem_sol`과 `bool non_uniform_n`이다(7–8). 호스트 이웃(neighbour) 수 저장소 한 개를 new로 할당한다(11). 장치 할당식은 `NUMERIC_TYPE* d_num_neighbours = (NUMERIC_TYPE*)malloc_device(sizeof(NUMERIC_TYPE));` (12)이다. 임시 저장소 포인터는 NULL, 크기는 0으로 초기화한다(14–15). `CHECK_CUDA_ERROR(cub::DeviceReduce::Sum` (17)에 `d_temp_storage`, `temp_storage`, `d_assem_sol.nghbr_counts`, `d_num_neighbours`, `d_assem_sol.length`를 전달한다(18–24). `d_temp_storage = malloc_device(temp_storage);` (26)로 조회한 크기만큼 할당한다. 이 파일에는 전처리 조건 분기가 없다. |
| 27–49 | 시작 시 5–10행의 `init_neighbours` 함수 안. `CHECK_CUDA_ERROR(cub::DeviceReduce::Sum` (28)을 같은 임시 저장소·크기·이웃 수 입력·출력·길이 인수로 호출한다(29–35). `copy_cuda`로 `sizeof(NUMERIC_TYPE)`만큼 장치 출력에서 호스트 출력으로 복사한다(37–42). `int num_neighbours = *h_num_neighbours;` (44)로 합계를 int에 저장한다. `free_device`로 장치 출력과 임시 저장소를 해제하고 호스트 출력을 delete한다(46–48). |
| 50–80 | 시작 시 5–10행의 `init_neighbours` 함수 안. 누적 이웃 수(cumulative neighbour counts) 계산 주석 뒤 임시 저장소 포인터와 크기를 NULL·0으로 다시 초기화한다(50–53). `CHECK_CUDA_ERROR(cub::DeviceScan::ExclusiveSum` (55)에 `d_temp_storage`, `temp_storage`, `d_assem_sol.nghbr_counts`, `d_assem_sol.cumu_nghbr_counts`, `d_assem_sol.length`를 전달한다(56–62). `d_temp_storage = malloc_device(temp_storage);` (64)로 할당한다. `CHECK_CUDA_ERROR(cub::DeviceScan::ExclusiveSum` (66)을 같은 인수로 다시 호출하여 누적 합의 출력 배열을 지정한다(67–73). 임시 저장소를 해제한다(75). `return NonUniformNeighbours(num_neighbours, non_uniform_n);` (79)로 생성자를 호출해 반환하고 함수를 닫는다(80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–12·37–44: 이웃 수 합계의 호스트·장치 저장소는 NUMERIC_TYPE이다. 호스트로 복사한 값은 int 변수 `num_neighbours`에 대입한다.
- 8·17–73·79: `non_uniform_n`은 반환 객체의 생성자 인수로 전달된다. 두 합산 호출의 선택에는 이 인수를 검사하는 조건문이 없다.
- 7·17–35·55–73: 두 합산 작업의 길이는 `d_assem_sol.length`를 그대로 사용한다. 이 함수에는 입력 길이를 검사하는 조건문이 없다.
