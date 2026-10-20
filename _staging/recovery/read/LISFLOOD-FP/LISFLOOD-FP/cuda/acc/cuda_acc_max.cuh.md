---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_max.cuh
lines: 36
sha256: 1729ccbee306dcc3b6be3a3d0983f85e5395768ca32dcbed872424acae882fc9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_max.cuh — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 중복 포함 방지 지시·lisflood·ACC Flow·CUDA Geometry 헤더와 lis::cuda::acc 이름공간 선언(1–11). 조건부 전처리 블록이 없다. 헤더 전체는 포함 번역 단위의 빌드 매크로를 따르며 자체 #if 제한이 없다. CMakeLists.txt:73·77은 CUDA 구성에서 CUDA·THRUST_IGNORE_CUB_VERSION_CHECK를 정의하며 config.default.cmake:2는 _NUMERIC_MODE=1을 정의한다. 원문(조건·식·호출·선언): `#pragma once` (1); `#include "../../lisflood.h"` (2); `#include "cuda_acc_flow.cuh"` (3); `#include "cuda_geometry.cuh"` (4); `namespace lis` (6); `namespace cuda` (8); `namespace acc` (10). |
| 13–27 | 시작 시 6·8·10행 이름공간 안. MaxH 클래스의 public 생성자는 Geometry 참조, update는 const Flow 참조를 받으며 소멸자를 선언한다(13–26). 함수 구현·조건·수치 대입식은 이 구간에 없다. 원문(조건·식·호출·선언): `class MaxH` (13); `public:` (15); `MaxH` (16); `(` (17); `Geometry& geometry` (18); `);` (19); `void update` (21); `(` (22); `const Flow& flow` (23); `);` (24); `~MaxH();` (26). |
| 28–36 | 시작 시 6·8·10행 이름공간·13행 MaxH 클래스 안. private 멤버는 const int elements·void* temp·size_t bytes이다(28–31). 클래스와 세 이름공간을 닫는다(32–36). 멤버 선언에 기본값 대입은 없다. 원문(조건·식·호출·선언): `private:` (28); `const int elements;` (29); `void* temp;` (30); `size_t bytes;` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–31: elements·temp·bytes는 선언 기본 초기값을 갖지 않는다. bytes를 직접 초기화하는 생성자 선언도 이 헤더에 없다.
