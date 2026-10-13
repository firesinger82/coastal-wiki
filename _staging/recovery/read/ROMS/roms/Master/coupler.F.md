---
file: models/ROMS/raw/source_code/roms/Master/coupler.F
lines: 25
sha256: 5d2f39bf34a094211bad44aaf54bda31059fca173c93f8dade62298f14edd710
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# coupler.F — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#include "cppdefs.h"` (1)로 cpp 설정 파일 cppdefs.h를 끼워 넣는다. 저작권·MIT/X 라이선스·License_ROMS.md 안내(2–8)와 ROMS를 ESMF/NUOPC 또는 MCT 라이브러리로 다른 모델에 결합(coupling)한다는 모듈 설명(9–14), 빈 줄(15). |
| 16–21 | `#if defined MODEL_COUPLING && !defined CMEPS` (16)에서 모델 결합을 켜고 CMEPS를 정의하지 않을 때 내부 선택을 수행한다. `# if defined MCT_LIB` (17)이면 `#  include "mct_coupler.h"` (18)로 mct_coupler.h를 끼워 넣는다. 같은 내부 선택의 `# elif defined ESMF_LIB` (19)이면 `#  include "esmf_coupler.h"` (20)로 esmf_coupler.h를 끼워 넣는다. `# endif` (21)로 내부 전처리 선택을 닫는다. |
| 22–25 | 시작 시 16행 `#if defined MODEL_COUPLING && !defined CMEPS` (16) 선택 안. `#else` (22)는 16행 조건의 불성립 분기이다. 빈 coupler_mod 모듈을 선언·종료한다(23–24). `#endif` (25)로 바깥 선택을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–21: MODEL_COUPLING을 정의하고 CMEPS를 정의하지 않은 분기에는 MCT_LIB와 ESMF_LIB 선택만 있다. 두 라이브러리 매크로가 모두 정의되면 먼저 위치한 MCT_LIB 분기를 선택한다. 두 매크로가 모두 없으면 이 분기에는 모듈 선언이 없다.
