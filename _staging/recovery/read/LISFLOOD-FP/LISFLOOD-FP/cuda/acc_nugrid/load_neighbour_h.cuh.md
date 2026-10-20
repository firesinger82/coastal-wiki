---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/load_neighbour_h.cuh
lines: 32
sha256: d04976448d674b9bbbf29bab73407f286d397f95b29a9734fbbd087bc74a462f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_neighbour_h.cuh — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#pragma once` (1)로 중복 포함을 제한한다. CUDA 런타임(runtime), 장치 실행 매개변수, 표준 입출력과 조립 해(assembled solution)·방향·Morton 코드·계층 인덱스·비균일 이웃·유령 셀·압축·경계 형식의 헤더를 포함한다(3–14). 빈 줄도 포함한다. 이 파일 전체에는 조건부 전처리 분기와 매크로 값 정의가 없다. |
| 16–32 | lis::cuda::acc_nugrid 이름공간(namespace)을 연다(16–21). `__global__ void load_neighbour_h` (23); `(` (24); `AssembledSolution d_assem_sol,` (25); `NonUniformNeighbours d_non_uniform_nghbrs,` (26); `bool non_uniform_n` (27); `);` (28)로 CUDA 커널(kernel)을 선언한다. 조립 해와 비균일 이웃을 값 인수로 받고 non_uniform_n 불리언을 받는다. 함수 본문과 커널 실행은 이 파일에 없다. 빈 줄과 이름공간 닫기를 포함한다(29–32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
