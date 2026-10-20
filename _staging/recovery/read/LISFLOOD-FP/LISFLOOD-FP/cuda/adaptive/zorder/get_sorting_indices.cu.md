---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/get_sorting_indices.cu
lines: 62
sha256: d7c3b55864491b557de336d36605bd99ef48ebca14f490d80650b67784d49fca
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_sorting_indices.cu — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `get_sorting_indices.cuh`를 포함한다(1). 빈 줄(2) 뒤 `__host__` (3) 함수 `get_sorting_indices`를 정의한다(4–15). 인수는 원본·정렬된 모턴 코드(Morton code) 배열, 해와 임시 해의 참조(reference), 인덱스 배열, 역 Z 순서(reverse Z-order) 배열, 역 행 우선 순서(reverse row-major order) 배열, 해법 매개변수 참조이다(6–13). 구분 주석은 Z 순서를 되돌릴 배열을 만든다고 적는다(16–18). 빈 줄(19) 뒤 임시 저장소 포인터는 `NULL`, 저장소 바이트 수는 0으로 초기화한다(20–21). 마지막은 빈 줄(22)이다. 전처리 조건 분기는 없다. |
| 23–36 | 시작 시 4행 함수 본문 안이다. 주석은 첫 호출이 임시 저장소 크기만 결정한다고 설명한다(23). 오류 검사 매크로를 감싼 키·값 쌍 기수 정렬(radix sort) 호출 원문은 `CHECK_CUDA_ERROR( cub::DeviceRadixSort::SortPairs`<br>`(`<br>`d_temp_storage,`<br>`temp_storage,`<br>`d_morton_codes,`<br>`d_sorted_morton_codes,`<br>`d_indices,`<br>`d_rev_z_order,`<br>`d_assem_sol.length`<br>`) );` (24–33)이다. 키(key)는 `d_morton_codes`, 키 출력은 `d_sorted_morton_codes`, 값(value)은 `d_indices`, 값 출력은 `d_rev_z_order`, 원소 수는 `d_assem_sol.length`이다. 빈 줄(34) 뒤 `d_temp_storage = malloc_device(temp_storage);` (35)로 장치 메모리(device memory)를 할당한다. 마지막은 빈 줄(36)이다. |
| 37–47 | 시작 시 4행 함수 본문 안이며 35행 할당 뒤이다. 원문 호출은 `CHECK_CUDA_ERROR( cub::DeviceRadixSort::SortPairs`<br>`(`<br>`d_temp_storage,`<br>`temp_storage,`<br>`d_morton_codes,`<br>`d_sorted_morton_codes,`<br>`d_indices,`<br>`d_rev_z_order,`<br>`d_assem_sol.length`<br>`) );` (37–46)이다. 할당된 임시 저장소로 모턴 코드 키와 원래 인덱스 값의 정렬을 수행하여 `d_sorted_morton_codes`와 `d_rev_z_order`에 출력한다. `CHECK_CUDA_ERROR`가 반환 상태를 검사한다. 마지막은 빈 줄(47)이다. |
| 48–62 | 시작 시 4행 함수 본문 안이다. 두 번째 정렬의 원문은 `CHECK_CUDA_ERROR( cub::DeviceRadixSort::SortPairs`<br>`(`<br>`d_temp_storage,`<br>`temp_storage,`<br>`d_rev_z_order,`<br>`d_sorted_morton_codes,`<br>`d_indices,`<br>`d_rev_row_major,`<br>`d_assem_sol.length`<br>`) );` (48–57)이다. 이 호출은 `d_rev_z_order`를 키 입력으로, `d_sorted_morton_codes`를 키 출력으로, `d_indices`를 값 입력으로, `d_rev_row_major`를 값 출력으로 사용한다. 원소 수는 다시 `d_assem_sol.length`이다. `CHECK_CUDA_ERROR`가 반환 상태를 검사한다. 빈 줄(58) 뒤 `free_device(d_temp_storage);` (59)로 저장소를 해제한다. 빈 줄·구분 주석·함수 종료가 이어진다(60–62). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·13·15–62: 인수 `d_buf_assem_sol`과 `solver_params`는 함수 본문에서 참조하지 않는다.
- 29·42·53: 첫 정렬 결과를 받는 `d_sorted_morton_codes`는 마지막 정렬에서도 키 출력 배열이다. 마지막 호출의 키 입력은 원래 모턴 코드 배열이 아니라 `d_rev_z_order`이다.
- 59: `free_device(d_temp_storage)`의 반환값은 저장하거나 `CHECK_CUDA_ERROR`에 넘기지 않는다.
