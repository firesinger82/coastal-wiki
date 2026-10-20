---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_simulate.cuh
lines: 28
sha256: 66c9814a588d7ad42e9b8cd7191c964277f2989dfbb6106bafdd5bd9c3e15ad6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_simulate.cuh — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 중복 포함 방지·lisflood·CUDA Simulation 헤더와 lis::cuda::acc 이름공간(namespace) 선언(1–11). 조건부 전처리 블록이 없다. 헤더 전체는 포함 번역 단위(translation unit)의 매크로 조합을 따르며 자체 #if 제한이 없다. CMakeLists.txt:73·77은 CUDA 구성의 CUDA·THRUST_IGNORE_CUB_VERSION_CHECK 정의이고 config.default.cmake:2는 _NUMERIC_MODE=1 정의이다. 원문(조건·식·호출·선언): `#pragma once` (1); `#include "../../lisflood.h"` (2); `#include "../cuda_simulate.cuh"` (3); `namespace lis` (6); `namespace cuda` (8); `namespace acc` (10). |
| 13–28 | 시작 시 6·8·10행 이름공간 안. ACC Simulation은 cuda::Simulation을 public 상속(inheritance)한다(13). run은 Fnames·States·Pars·전역 ::Solver 참조와 int verbose를 받는 void 메서드로 선언한다(15–23). 클래스·이름공간을 닫는다(24–28). 실행 조건·기본값·수치식·직접 CUDA 커널 지시는 없다. 원문(조건·식·호출·선언): `class Simulation : public cuda::Simulation` (13); `public:` (15); `void run` (16); `(` (17); `Fnames& filenames,` (18); `States& states,` (19); `Pars& pars,` (20); `::Solver& solver,` (21); `int verbose` (22); `);` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
