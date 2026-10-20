---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/NonUniformNeighbours.h
lines: 109
sha256: c59fd6b3dc24b0416923526ea7272cdfdbef71a7be72ae3afb3a23304f614d3f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# NonUniformNeighbours.h — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | `#pragma once` (1), cuda_utils·lisflood·index_1D 포함(3–5), `lis::cuda::acc_nugrid` 이름공간(namespace)(7–12). 비균일 격자 이웃(non-uniform neighbour) 구조체(struct) NonUniformNeighbours(14–15)는 실수 포인터 h_owner·h_nghbr·z_owner·z_nghbr·n_owner·n_nghbr·q·z·v(16–24), 이웃·소유 요소의 인덱스(index)·플래그(flag)·개수 포인터(25–31), 실수 dx·dx_sum 포인터(32–33), int* dirs·itrface_counts·cumu_itrface_counts·sum_flags(34–37), length·is_copy(38–39)를 선언한다. act_idcs 두 포인터의 원소 형식은 index_1D다(26·29). 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 41–73 | 시작 시 14행 구조체 안. 생성자(constructor)는 num_nghbrs·non_uniform_n을 받는다(41–42). `size_t bytes_real = num_nghbrs * sizeof(NUMERIC_TYPE);` (43), `size_t bytes_int  = num_nghbrs * sizeof(index_1D); // MKS: or int???` (44). h_owner·h_nghbr·z_owner·z_nghbr·q·z·v에 `(NUMERIC_TYPE*)malloc_device(bytes_real)`를 할당한다(46–52). `n_owner = (non_uniform_n) ? (NUMERIC_TYPE*)malloc_device(bytes_real) : nullptr;` (54), `n_nghbr = (non_uniform_n) ? (NUMERIC_TYPE*)malloc_device(bytes_real) : nullptr;` (55). nghbr_elem_idcs·nghbr_flags·owner_elem_idcs·owner_counts·owner_flags는 `(int*)malloc_device(bytes_int)` (57·59–60·62–63), nghbr_act_idcs·owner_act_idcs는 `(index_1D*)malloc_device(bytes_int)` (58·61). dx·dx_sum은 `(NUMERIC_TYPE*)malloc_device(bytes_real)` (64–65), dirs·itrface_counts·cumu_itrface_counts·sum_flags는 `(int*)malloc_device(bytes_int)` (66–69). length=num_nghbrs·is_copy=false(70–71). 생성자 종료와 빈 줄(72–73). |
| 74–109 | 시작 시 14행 구조체 안. 복사 생성자(copy constructor) `NonUniformNeighbours(const NonUniformNeighbours& original) { *this = original; is_copy = true; }` (74). 소멸자(destructor)(76–77)의 `if (!is_copy)` (78)에서 h_owner·h_nghbr·z_owner·z_nghbr·n_owner·n_nghbr·q·z·v(80–88), nghbr_elem_idcs·nghbr_act_idcs·nghbr_flags·owner_elem_idcs·owner_act_idcs(89–93), dx·dx_sum·dirs·owner_counts·owner_flags·itrface_counts·cumu_itrface_counts·sum_flags(94–101)에 free_device를 호출한다. 블록·구조체·이름공간 종료와 빈 줄(102–109). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44·57–69: int* 배열의 할당 크기도 sizeof(index_1D)로 계산한다. 44행 주석은 `MKS: or int???`라고 적는다. index_1D의 실제 정의는 이 파일에 없다.
- 41–72: 생성자는 배열을 할당하지만 배열 원소를 채우는 문장을 포함하지 않는다.
- 54–55·78–85: non_uniform_n이 거짓이면 n_owner·n_nghbr는 nullptr다. 원본 소멸자는 별도 포인터 조건 없이 두 포인터에 free_device를 호출한다.
