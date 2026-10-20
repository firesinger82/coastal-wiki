---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/rev_z_order_reals.cu
lines: 41
sha256: 3b92a3df8ed36750e85419aa8eecfd76e970731d2248418882a85bb8d9d55024
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rev_z_order_reals.cu — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 대응 헤더 포함(1). `__host__` (3) 루틴 rev_z_order_reals는 두 Morton 코드(Morton code) 포인터·실수 입출력 포인터·길이를 받는다(4–11). 임시 포인터 NULL·크기 0(13–14). `CHECK_CUDA_ERROR( cub::DeviceRadixSort::SortPairs` (16–25)는 d_rev_z_order/d_indices 키와 d_array/d_array_sorted 값의 기수 정렬(radix sort) 저장소 크기를 조회한다. `d_temp_storage = malloc_device(temp_storage);` (27)로 할당한다. 전처리 조건 분기는 없다. |
| 28–41 | 시작 시 4–12행 rev_z_order_reals 루틴 안. 같은 인수로 `cub::DeviceRadixSort::SortPairs`를 재호출하여 array_length개 값을 정렬한다(29–38). CHECK_CUDA_ERROR로 오류를 검사하며 `free_device(d_temp_storage);` (40)로 해제하고 끝난다(41). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
