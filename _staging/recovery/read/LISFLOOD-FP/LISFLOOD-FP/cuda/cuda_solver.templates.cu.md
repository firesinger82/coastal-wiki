---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_solver.templates.cu
lines: 116
sha256: 8791663c0e94b37fad70894313de43ec1481cdfcba01595d881722ba809c505f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_solver.templates.cu — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | GhostRaster·CUDA geometry/util·helper_cuda·CUB 라이브러리 헤더를 포함한다(1–5). 파일 내부 전처리 조건 분기는 없다. DynamicTimestep<F> 생성자는 `adaptive(adaptive_ts == ON),` (19), `elements(lis::GhostRaster::elements(geometry))` (21)로 초기화한다. `if (adaptive)` (23)이면 임시 포인터를 nullptr로 두고 `checkCudaErrors(cub::DeviceReduce::Min(d_temp, bytes,` (29), `dummy_in, dummy_out, elements));` (30)로 최소값 축약(reduction)의 작업 메모리 크기를 조회한다. malloc_device(bytes)와 cuda::GhostRaster::allocate_device를 호출한다(32–34). `else` (36)는 dt=max_dt이다(38). |
| 42–72 | DynamicTimestepACC<F> 생성자는 `adaptive(adaptive_ts == ON),` (54), `elements(lis::GhostRaster::elements_H(geometry))` (56)로 초기화한다. 분기 없이 임시 포인터를 nullptr로 두고 `checkCudaErrors(cub::DeviceReduce::Min(d_temp, bytes,` (63), `dummy_in, dummy_out, elements));` (64)로 크기를 조회한다. malloc_device(bytes)와 cuda::GhostRaster::allocate_device_H를 호출한다(66–68). |
| 73–86 | DynamicTimestep<F>::update_dt의 `if (adaptive)` (76) 안에서 solver.update_dt_per_element(dt_field)를 호출하고 `checkCudaErrors(cub::DeviceReduce::Min(d_temp, bytes,` (79), `dt_field, &dt, elements));` (80)로 dt를 축약한다. 분기 밖에서 cuda::sync를 호출하고 dt를 반환한다(82–84). |
| 87–98 | DynamicTimestepACC<F>::update_dt_ACC는 분기 없이 solver.update_dt_per_element를 호출한다(90). `checkCudaErrors(cub::DeviceReduce::Min(d_temp, bytes,` (91), `dt_field, &dt, elements));` (92), cuda::sync, dt 반환을 수행한다(94–96). |
| 99–116 | DynamicTimestep 소멸자는 `if (adaptive)` (102) 안에서만 cuda::free_device(dt_field)와 free_device(d_temp)를 호출한다(104–105). DynamicTimestepACC 소멸자는 같은 두 해제를 무조건 호출한다(110–116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 54·59–68·88–96·110–114: ACC 생성자는 adaptive를 저장한다. ACC의 할당·시간 간격 축약·해제에는 adaptive 조건이 없다.
- 18·38·53·74–96: max_dt를 직접 dt에 대입하는 문장은 일반 생성자의 비적응 분기에만 있다. 두 update 함수에는 max_dt 참조가 없다.
