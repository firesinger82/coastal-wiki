---
file: models/ROMS/raw/source_code/roms/ROMS/Representer/rp_prsgrd.F
lines: 30
sha256: 2e9d7c9d164f9ce78d42f308ad2fc6a3c76fd472846fbc785e589a17cfb43372
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_prsgrd.F — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | cppdefs.h를 포함하고 TL_IOMS·SOLVE3D 조건을 연다(1–2). 저작권·설명 주석은 대표자(representer) 접선 선형(tangent linear) 경압(baroclinic) 정수압 압력 경사(hydrostatic pressure gradient)를 계산한다고 적는다(3–15). 원문: `#include "cppdefs.h"` (1); `#if defined TL_IOMS && defined SOLVE3D` (2). |
| 16–26 | 시작 시 전처리 조건 2행 `#if defined TL_IOMS && defined SOLVE3D` 안. PJ_GRADPQ4·PJ_GRADPQ2·PJ_GRADP·DJ_GRADPS와 대체 분기로 구현 포함 파일을 선택한다(16–26). PJ_GRADPQ4의 `!!#  include "rp_prsgrd44.h"` (17)와 PJ_GRADPQ2의 `!!#  include "rp_prsgrd42.h"` (19)는 주석이다. PJ_GRADP는 rp_prsgrd40.h, DJ_GRADPS는 rp_prsgrd32.h, 대체 분기는 rp_prsgrd31.h를 끼워 넣는다(21·23·25). 여기서는 이 선택 파일의 행만 판독하며 다른 포함 파일 내부는 이 기록에 넣지 않는다. 원문: `# if defined PJ_GRADPQ4` (16); `# elif defined PJ_GRADPQ2` (18); `# elif defined PJ_GRADP` (20); `#  include "rp_prsgrd40.h"` (21); `# elif defined DJ_GRADPS` (22); `#  include "rp_prsgrd32.h"` (23); `# else` (24); `#  include "rp_prsgrd31.h"` (25); `# endif` (26). |
| 27–30 | 시작 시 전처리 조건 2행 `#if defined TL_IOMS && defined SOLVE3D` 안. 2행 전처리 조건의 대체 분기를 연다(27). 이 분기는 내용 없는 rp_prsgrd_mod 모듈의 시작과 끝만 정의한다(28–29). 전처리 조건을 닫는다(30). 원문: `#else` (27); `#endif` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–19: PJ_GRADPQ4·PJ_GRADPQ2 분기의 include 행은 각각 !!로 주석 처리되어 있다. 뒤의 PJ_GRADP·DJ_GRADPS·대체 분기 include는 실행 전처리 지시문이다(21·23·25).
