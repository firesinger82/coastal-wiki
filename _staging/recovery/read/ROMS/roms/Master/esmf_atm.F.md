---
file: models/ROMS/raw/source_code/roms/Master/esmf_atm.F
lines: 40
sha256: 78e4602653595cf4af5bfb0e51b0ea8c40e5f1077d5f0a86eb182dab9fbd15e5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# esmf_atm.F — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#include "cppdefs.h"` (1)로 cppdefs.h를 끼워 넣는다. `#if defined MODEL_COUPLING && defined ESMF_LIB` (2)는 MODEL_COUPLING과 ESMF_LIB를 모두 요구한다. 저작권·라이선스 안내(3–9), ESMF/NUOPC를 사용하는 대기 격자 구성요소(gridded component) 설명(10–13), ESMF 버전 7 이상과 ESMF/NUOPC 이름·주소를 적은 주석(14–21), 빈 줄(22). |
| 23–32 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB` (2) 안. `# if defined ATM_COUPLING` (23) 안에서 `#  if defined COAMPS_COUPLING` (24)이면 `#   include "esmf_atm_coamps.h"` (25)로 esmf_atm_coamps.h를 끼워 넣는다. 같은 선택의 `#  elif defined REGCM_COUPLING` (26)이면 `#   include "esmf_atm_regcm.h"` (27)로 esmf_atm_regcm.h를 끼워 넣고, `#  elif defined WRF_COUPLING` (28)이면 `#   include "esmf_atm_wrf.h"` (29)로 esmf_atm_wrf.h를 끼워 넣는다. `#  else` (30)이면 `#   include "esmf_atm_void.h"` (31)로 esmf_atm_void.h를 끼워 넣는다. `#  endif` (32)로 모델별 선택을 닫는다. |
| 33–40 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB` (2)·23행 `# if defined ATM_COUPLING` (23) 선택 안. `# else` (33)에서 빈 esmf_atm_mod 모듈을 선언·종료한다(34–35). `# endif` (36)로 ATM_COUPLING 선택을 닫는다. `#else` (37)은 2행 조건 불성립 분기이며 같은 빈 esmf_atm_mod 모듈을 선언·종료한다(38–39). `#endif` (40)으로 바깥 선택을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–31: 모델별 선택 순서는 COAMPS_COUPLING, REGCM_COUPLING, WRF_COUPLING이다. 이 중 여러 매크로를 동시에 정의해도 앞에서 성립한 한 분기의 파일만 포함한다.
