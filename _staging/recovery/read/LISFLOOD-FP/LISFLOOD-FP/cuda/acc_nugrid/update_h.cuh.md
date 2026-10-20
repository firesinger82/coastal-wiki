---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/update_h.cuh
lines: 38
sha256: 2f6dfccdc5807288c5961ab6a9238a5b4779105e7253836d33f60f2b5be7aec4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# update_h.cuh — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `#pragma once` (1). CUDA 실행·커널 실행 매개변수·stdio·조립 해(assembled solution)·방향·MortonCode·레벨 도우미·비균일 이웃·인터페이스·고스트 셀(ghost cell)·compact·경계·점 유입원(point source) 헤더를 포함한다(3–16). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(18–23). 전처리 조건 분기는 없다. |
| 25–38 | `__global__ void update_h` (25)는 CUDA 커널(kernel) 원형이다. AssembledSolution·NonUniformNeighbours·NonUniformInterfaces·Pars·Solver·Boundaries·PointSources를 값 인수로 받는다(26–34). 기본 인수와 실행 본문은 없다. 빈 줄과 이름공간 닫기(35–38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
