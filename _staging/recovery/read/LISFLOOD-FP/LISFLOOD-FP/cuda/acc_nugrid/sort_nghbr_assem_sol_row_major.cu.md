---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/sort_nghbr_assem_sol_row_major.cu
lines: 54
sha256: 58873c6c1825aec3e754fca8a591be9cb6ef55bed127cf9b981c3ca9bca39dee
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sort_nghbr_assem_sol_row_major.cu — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 관련 헤더·helper_cuda·CUB 포함(1–3). `__host__ void lis::cuda::acc_nugrid::sort_nghbr_assem_sol_row_major` (5)는 호스트(host) 함수이다. 역 Z 순서·인덱스 MortonCode 배열, 버퍼·이웃 조립 해(assembled solution) 참조와 int array_length를 받는다(6–12). 임시 포인터 NULL·크기 0(14–15). CHECK_CUDA_ERROR로 감싼 cub::DeviceRadixSort::SortPairs에 d_reverse_z_order·d_indices 키와 버퍼·이웃 act_idcs를 전달하여 크기를 조회한다(18–27). malloc_device로 할당한다(29). 전처리 조건 분기와 실행 조건문은 없다. |
| 30–54 | 시작 시 5행 sort_nghbr_assem_sol_row_major 함수 안. 같은 키·길이로 act_idcs를 실제 정렬하고(31–40), levels도 정렬한다(42–51). 두 SortPairs는 CHECK_CUDA_ERROR로 감싼다. free_device로 임시 메모리를 해제하고 함수를 닫는다(53–54). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–51·53: SortPairs 호출은 CHECK_CUDA_ERROR로 감싸지만 free_device 호출은 감싸지 않는다.
