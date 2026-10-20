---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/rev_z_order_assem_sol.cu
lines: 98
sha256: 3841b67b07001267329b0958cd0f76322f13a7d3bb1753261e40ea586e1a7959
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rev_z_order_assem_sol.cu — 판독 구간 기록

구간은 1행부터 98행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 대응 헤더 포함(1), `rev_z_order_assem_sol`의 Morton 코드(Morton code) 키·출력 인덱스·두 조립 해·배열 길이 인수 선언(3–10). 임시 저장소 포인터 NULL 및 바이트 수 0 초기화(12–13). 기수 정렬(radix sort) `CHECK_CUDA_ERROR( cub::DeviceRadixSort::SortPairs` 호출(18–27)은 d_rev_z_order/d_indices와 z0 입출력으로 필요한 저장소 크기를 조회한다. `d_temp_storage = malloc_device(temp_storage);` (29)로 할당한다. 이 파일에는 전처리 조건 분기가 없다. |
| 30–74 | 시작 시 3–11행 `rev_z_order_assem_sol` 루틴 안. 같은 임시 저장소와 d_rev_z_order/d_indices를 쓰는 `cub::DeviceRadixSort::SortPairs`를 h0(31–40), qx0(42–51), qy0(53–62), z0(64–73)에 각각 호출한다. 각 값 입력은 d_buf_assem_sol이고 출력은 d_assem_sol이며 정렬 개수는 array_length다. 모든 호출을 CHECK_CUDA_ERROR로 감싼다. |
| 75–98 | 시작 시 3–11행 루틴 안. `cub::DeviceRadixSort::SortPairs`로 levels(75–84)와 act_idcs(86–95)를 같은 키·길이로 정렬한다. `free_device(d_temp_storage);` (97) 후 루틴 종료(98). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–95: 정렬 대상은 h0·qx0·qy0·z0·levels·act_idcs이다. 이 루틴에는 h1x·h1y 등 1차 계수의 정렬 호출이 없다.
