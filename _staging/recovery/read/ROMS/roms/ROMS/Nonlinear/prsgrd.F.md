---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/prsgrd.F
lines: 30
sha256: 74de1f7131c93dcc95ccf28bbae873dd95ca19ff38cbd8968880305133264405
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# prsgrd.F — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 바깥 블록 없음. `cppdefs.h`를 포함한다(1). NONLINEAR와 SOLVE3D를 모두 만족할 때 경압 정수압 압력 경도(baroclinic hydrostatic pressure gradient) 구현을 선택한다(2·11–12). 저작권·라이선스 머리말과 빈 주석도 이 구간에 포함한다(3–15). 원문: `#include "cppdefs.h"` (1); `#if defined NONLINEAR && defined SOLVE3D` (2). |
| 16–26 | 시작 시 2행 `#if defined NONLINEAR && defined SOLVE3D` 안. 전처리 선택 순서는 PJ_GRADPQ4의 `prsgrd44.h`, PJ_GRADPQ2의 `prsgrd42.h`, PJ_GRADP의 `prsgrd40.h`, DJ_GRADPS의 `prsgrd32.h`, else의 `prsgrd31.h`이다(16–26). 앞 조건이 성립하면 뒤의 elif·else는 선택되지 않는다. 이 파일 자체에는 수치 대입식이나 루틴 호출이 없다. 원문: `# if defined PJ_GRADPQ4` (16); `#  include "prsgrd44.h"` (17); `# elif defined PJ_GRADPQ2` (18); `#  include "prsgrd42.h"` (19); `# elif defined PJ_GRADP` (20); `#  include "prsgrd40.h"` (21); `# elif defined DJ_GRADPS` (22); `#  include "prsgrd32.h"` (23); `# else` (24); `#  include "prsgrd31.h"` (25); `# endif` (26). |
| 27–30 | 시작 시 2행 `#if defined NONLINEAR && defined SOLVE3D` 안. NONLINEAR와 SOLVE3D 조건의 else는 빈 prsgrd_mod 모듈을 선언하고 닫는다(27–30). 원문: `#else` (27); `#endif` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–25: prsgrd31.h는 최종 else에서 포함한다. 이 파일에는 prsgrd31.h 선택을 위해 별도 매크로를 검사하는 조건이 없다.
