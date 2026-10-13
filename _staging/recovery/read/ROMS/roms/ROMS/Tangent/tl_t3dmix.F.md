---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_t3dmix.F
lines: 44
sha256: 002ce5574943661ea5af929196d25bae69ac2e41050ee6ce3a725bf664ac4348
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_t3dmix.F — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 포함한다(1). TANGENT이고 TS_FIXED가 없으며 SOLVE3D이고 TS_DIF2 또는 TS_DIF4이면 접선형(tangent linear) 추적자(tracer) 수평 혼합(horizontal mixing) 구현을 선택한다(3–5). 4–5행은 역슬래시로 이어지는 하나의 전처리 조건이다. 머리말은 저작권·MIT/X 라이선스·루틴 목적을 적는다(7–16). 원문: `#include "cppdefs.h"` (1); `#ifdef TANGENT` (3); `# if !defined TS_FIXED && defined SOLVE3D &&  \` (4); `     (defined TS_DIF2  \|\| defined TS_DIF4)` (5). |
| 18–27 | 시작 시 3행 `#ifdef TANGENT`·4행 `# if !defined TS_FIXED && defined SOLVE3D &&  \`·5행 `(defined TS_DIF2  \|\| defined TS_DIF4)` 안. TS_DIF2이면 MIX_S_TS·MIX_GEO_TS·MIX_ISO_TS를 IF·ELIF 순서로 검사한다(18–25). 각각 `tl_t3dmix2_s.h`·`tl_t3dmix2_geo.h`·`tl_t3dmix2_iso.h`를 끼워 넣는다(20·22·24). 선택 분기와 TS_DIF2 조건을 닫는다(25–26). 원문: `#  ifdef TS_DIF2` (18); `#   if defined MIX_S_TS` (19); `#    include "tl_t3dmix2_s.h"` (20); `#   elif defined MIX_GEO_TS` (21); `#    include "tl_t3dmix2_geo.h"` (22); `#   elif defined MIX_ISO_TS` (23); `#    include "tl_t3dmix2_iso.h"` (24); `#   endif` (25); `#  endif` (26). |
| 28–37 | 시작 시 3행 `#ifdef TANGENT`·4행 `# if !defined TS_FIXED && defined SOLVE3D &&  \`·5행 `(defined TS_DIF2  \|\| defined TS_DIF4)` 안. TS_DIF4이면 MIX_S_TS·MIX_GEO_TS·MIX_ISO_TS를 같은 IF·ELIF 순서로 검사한다(28–35). 각각 `tl_t3dmix4_s.h`·`tl_t3dmix4_geo.h`·`tl_t3dmix4_iso.h`를 끼워 넣는다(30·32·34). 이 파일에서는 포함 파일 내부를 읽지 않는다. 선택 조건·TS_DIF4·4–5행 조건을 닫는다(35–37). 원문: `#  ifdef TS_DIF4` (28); `#   if defined MIX_S_TS` (29); `#    include "tl_t3dmix4_s.h"` (30); `#   elif defined MIX_GEO_TS` (31); `#    include "tl_t3dmix4_geo.h"` (32); `#   elif defined MIX_ISO_TS` (33); `#    include "tl_t3dmix4_iso.h"` (34); `#   endif` (35); `#  endif` (36); `# endif` (37). |
| 38–44 | 시작 시 3행 `#ifdef TANGENT` 안. 시작 시 3행 TANGENT 조건 안. TANGENT가 없는 ELSE 경로는 본문 없는 `tl_t3dmix2_mod`·`tl_t3dmix4_mod`를 정의한다(38–43). 44행은 TANGENT 조건을 닫는다. 원문: `#else` (38); `#endif` (44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–36: TS_DIF2와 TS_DIF4는 서로 독립된 IFDEF이다. 각 내부의 좌표 선택은 MIX_S_TS, MIX_GEO_TS, MIX_ISO_TS 순서의 IF/ELIF이며 마지막 ELSE가 없다.
- 3–5·37–44: 빈 모듈 대체 분기는 TANGENT가 없는 경우에만 있다. TANGENT가 있지만 4–5행 조건이 거짓인 경우의 빈 모듈 대체 분기는 없다.
