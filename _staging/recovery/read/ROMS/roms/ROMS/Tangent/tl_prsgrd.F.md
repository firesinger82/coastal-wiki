---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_prsgrd.F
lines: 30
sha256: 8f2218cb419a3dfd422d56c65ee5f9e4155102b2dd884349413db147386efcdd
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_prsgrd.F — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `cppdefs.h`를 포함한다(1). TANGENT와 SOLVE3D 결합 조건(2). 저작권·라이선스·Id 및 구분 주석(3–9). 접선형(tangent linear) 경압(baroclinic) 정수압(hydrostatic) 압력 경사(pressure gradient)를 계산한다는 주석(10–15). 이 구간에는 계산 실행문이 없다. 원문 조건·계산식·호출·전처리: `#include "cppdefs.h"` (1); `#if defined TANGENT && defined SOLVE3D` (2). |
| 16–30 | 시작 시 2행 `#if defined TANGENT && defined SOLVE3D` 안. 시작 시 2행 TANGENT/SOLVE3D 조건 안. PJ_GRADPQ4와 PJ_GRADPQ2 우선 분기(16·18)에 적힌 `!!#  include "tl_prsgrd44.h"` (17), `!!#  include "tl_prsgrd42.h"` (19)는 주석이다. PJ_GRADP 분기는 `tl_prsgrd40.h`를 포함한다(20–21). DJ_GRADPS 분기는 `tl_prsgrd32.h`를 포함한다(22–23). cpp else는 `tl_prsgrd31.h`를 포함한다(24–25). 선택 조건 종료(26). 외부 조건의 #else(27)는 비어 있는 tl_prsgrd_mod 모듈만 정의한다(28–29). 최종 #endif(30). 원문 조건·계산식·호출·전처리: `# if defined PJ_GRADPQ4` (16); `# elif defined PJ_GRADPQ2` (18); `# elif defined PJ_GRADP` (20); `#  include "tl_prsgrd40.h"` (21); `# elif defined DJ_GRADPS` (22); `#  include "tl_prsgrd32.h"` (23); `# else` (24); `#  include "tl_prsgrd31.h"` (25); `# endif` (26); `#else` (27); `#endif` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–19: PJ_GRADPQ4와 PJ_GRADPQ2 분기의 include 줄은 !!로 시작하는 주석이다. 이 두 분기에 활성 #include는 없다. 활성 include는 PJ_GRADP, DJ_GRADPS 및 마지막 #else 분기에 있다(20–25).
