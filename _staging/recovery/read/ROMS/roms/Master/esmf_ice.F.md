---
file: models/ROMS/raw/source_code/roms/Master/esmf_ice.F
lines: 36
sha256: 1ce6dbea6fe4e2804dc965fcdf41b3a4a1ac3d6f39a6c940307ab77a50fed31a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# esmf_ice.F — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#if defined MODEL_COUPLING && defined ESMF_LIB` (2)가 해빙 모델(sea ice model) 결합 구현 선택을 감싼다. C 형식 블록 주석의 저작권·MIT/X 라이선스·ROMS에 ESMF(Earth System Modeling Framework)·NUOPC(National Unified Operational Prediction Capability)로 결합한다는 설명(3–21). 주석은 ESMF 7 이상과 두 프로젝트 주소를 적는다(14–18). 빈 줄(22). |
| 23–28 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB` 안. `# if defined ICE_COUPLING` (23)의 `#  if defined CICE_COUPLING_NOT_YET` (24)은 `#   include "esmf_ice_cice.h"` (25)로 esmf_ice_cice.h를 포함한다. `#  else` (26)는 `#   include "esmf_ice_void.h"` (27)로 esmf_ice_void.h를 포함한다. `#  endif` (28)가 CICE_COUPLING_NOT_YET 분기를 닫는다. 두 포함 파일 내부는 이 대상 파일 판독에 포함하지 않았다. |
| 29–36 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB`·23행 `# if defined ICE_COUPLING` 안이며 24행 분기 밖. `# else` (29)는 ICE_COUPLING이 정의되지 않은 분기이며 빈 esmf_ice_mod 모듈을 선언·종료한다(30–31). `# endif` (32)가 23행 조건을 닫는다. `#else` (33)는 2행 조건의 불성립 분기이며 같은 빈 모듈을 선언·종료한다(34–35). `#endif` (36)가 2행 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–28: esmf_ice_cice.h 포함 여부를 결정하는 매크로 이름은 CICE_COUPLING_NOT_YET이다. 해당 매크로가 정의되지 않으면 esmf_ice_void.h를 포함한다.
- 30–31·34–35: 두 비활성 결합 분기의 esmf_ice_mod에는 선언·루틴·실행문이 없다. 활성 결합 루틴은 이 파일 본문에 직접 작성되어 있지 않다.
