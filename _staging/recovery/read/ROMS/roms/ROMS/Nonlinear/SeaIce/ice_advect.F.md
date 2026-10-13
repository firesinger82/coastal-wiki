---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/ice_advect.F
lines: 21
sha256: e45e067ae21d24b75f0b7f76daa8275bb1cd0f6b1ef05be82b8974906980b897
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ice_advect.F — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 전처리 조건 밖. `#include "cppdefs.h"` (1)는 cppdefs.h를 끼워 넣는다. C 형식 머리말은 얼음 추적자(ice tracer) 이류(advection)를 계산하는 모듈이라고 설명한다(2–13). 원문: `#include "cppdefs.h"` (1). |
| 14–21 | 전처리 조건 밖에서 시작한다. ICE_MODEL과 ICE_ADVECT가 모두 정의되면 ICE_SMOLAR 조건에서 `ice_smolar.h`를 끼워 넣는다(14–17). 바깥 else는 빈 `ice_advect_mod`만 선언·종료한다(18–21). 포함 파일 내부는 이 파일 판독에 포함하지 않았다. 원문: `#if defined ICE_MODEL && defined ICE_ADVECT` (14); `# if defined ICE_SMOLAR` (15); `#  include <ice_smolar.h>` (16); `# endif` (17); `#else` (18); `#endif` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–21: ICE_MODEL·ICE_ADVECT가 정의된 경로에서 ICE_SMOLAR가 없으면 이 파일은 모듈 선언이나 다른 구현 include를 출력하지 않는다.
