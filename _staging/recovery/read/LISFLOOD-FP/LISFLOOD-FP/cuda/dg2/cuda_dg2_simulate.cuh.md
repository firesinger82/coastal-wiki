---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_simulate.cuh
lines: 57
sha256: c241e7006ea26528d1c0a01f0c0754311510f34a388185ee84148a1f4da5248d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_simulate.cuh — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1·3)를 두 번 적는다. lisflood·geometry·공통 cuda_simulate 헤더를 포함한다(4–6). 전처리 조건 분기는 없다. lis::cuda::dg2 이름공간(namespace)을 연다(8–13). |
| 15–26 | `class Simulation : public cuda::Simulation` (15)은 공통 Simulation을 공개 상속(public inheritance)한다. 공개 run은 Fnames·States·Pars·전역 ::Solver 참조와 verbose를 받는다(18–25). |
| 27–57 | 시작 시 15행 Simulation 클래스 안이다. private initialise_H는 H·H1x·H1y·파일명·상태·DEM·기하·pitch·offset·verbose를 받는다(28–40). initialise_H_slope는 array·파일명·접미사·기하·pitch·offset·verbose를 받는다(42–51). 클래스·이름공간·마지막 빈 줄을 포함한다(52–57). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·3: #pragma once 지시가 중복되어 있다.
