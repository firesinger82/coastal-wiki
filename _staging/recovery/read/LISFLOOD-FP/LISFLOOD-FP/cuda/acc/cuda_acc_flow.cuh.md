---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_flow.cuh
lines: 63
sha256: 33a9bc7fae8db52e02a307c784b5d14f05be4cbeb9f11c8badc6b5ec335a9092
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_flow.cuh — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 중복 포함 방지와 geometry·cuda_flow 헤더 포함(1–3), lis::cuda::acc 이름공간(namespace) 시작(5–10). 이 파일에는 조건부 전처리 블록이 없다. 헤더 전체는 포함된 번역 단위(translation unit)의 매크로 조합을 따르며 자체 #if 제한은 없다. CMakeLists.txt:73·77의 CUDA 구성 정의와 config.default.cmake:2의 _NUMERIC_MODE=1이 관련 빌드 정의이며 실제 빌드는 실행하지 않았다. 원문(조건·식·호출·선언): `#pragma once` (1); `#include "../geometry.h"` (2); `#include "cuda_flow.cuh"` (3); `namespace lis` (5); `namespace cuda` (7); `namespace acc` (9). |
| 12–30 | 시작 시 5·7·9행 lis::cuda::acc 이름공간 안. Flow 구조체의 __restrict__ NUMERIC_TYPE 포인터를 선언한다(12–29). 셀 수심 H·최대수심 maxH·총 침수시간 totalHtm·최대수심 시각 maxHtm·최초 침수시각 initHtm, 현재 및 과거 Qx/Qy·Vx/Vy를 보유한다. ChanMask 선언은 주석이다(15). 멤버 기본값 대입은 없다. 원문(조건·식·호출·선언): `struct Flow` (12); `NUMERIC_TYPE* __restrict__ H;` (14); `NUMERIC_TYPE* __restrict__ maxH;` (17); `NUMERIC_TYPE* __restrict__ totalHtm;` (18); `NUMERIC_TYPE* __restrict__ maxHtm;` (19); `NUMERIC_TYPE* __restrict__ initHtm;` (20); `NUMERIC_TYPE* __restrict__ Qx;` (23); `NUMERIC_TYPE* __restrict__ Qy;` (24); `NUMERIC_TYPE* __restrict__ Qxold;` (25); `NUMERIC_TYPE* __restrict__ Qyold;` (26); `NUMERIC_TYPE* __restrict__ Vx;` (28); `NUMERIC_TYPE* __restrict__ Vy;` (29). |
| 31–49 | 시작 시 5·7·9행 이름공간·12행 Flow 구조체 안. static allocate_pinned와 allocate_device는 Flow·Geometry 참조를 받는다(31–41). static copy는 목적·원본 Flow 및 Geometry 참조를 받는다(43–48). 구현과 실행 조건은 이 선언 파일에 없다. 원문(조건·식·호출·선언): `static void allocate_pinned` (31); `(` (32); `Flow& flow,` (33); `Geometry& geometry` (34); `);` (35); `static void allocate_device` (37); `(` (38); `Flow& flow,` (39); `Geometry& geometry` (40); `);` (41); `static void copy` (43); `(` (44); `Flow& dst,` (45); `Flow& src,` (46); `Geometry& geometry` (47); `);` (48). |
| 50–63 | 시작 시 5·7·9행 이름공간·12행 Flow 구조체 안. static free_pinned·free_device가 Flow 참조를 받도록 선언한다(50–58). 구조체 및 세 이름공간을 닫는다(59–63). CUDA 실행 위치 한정자나 커널 호출은 없다. 원문(조건·식·호출·선언): `static void free_pinned` (50); `(` (51); `Flow& flow` (52); `);` (53); `static void free_device` (55); `(` (56); `Flow& flow` (57); `);` (58). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–29: Flow의 포인터 멤버에는 선언 초기값이 없으며 이 구조체에 별도 생성자 선언이 없다.
- 15: ChanMask 포인터 선언은 주석 처리되어 있다.
