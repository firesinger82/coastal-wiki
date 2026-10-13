---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_t3dmix.F
lines: 44
sha256: 56c6cd6204c19936bbc18c84366aeb30663b8ad31224bee8ae04d839a087afcb
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_t3dmix.F — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시작 시 열린 전처리 조건 없음. cppdefs.h를 끼워 넣는다(1). ADJOINT 아래에서 TS_FIXED가 정의되지 않고 SOLVE3D가 정의되며 TS_DIF2 또는 TS_DIF4가 정의된 경우 혼합 구현을 포함한다(3–5). 머리말은 보조변수(adjoint) 추적자(tracer)의 수평 혼합(horizontal mixing) 루틴이라고 설명한다(6–17). 원문 조건·식·호출·전처리(행 순서): `#include "cppdefs.h"` (1); `#ifdef ADJOINT` (3); `# if !defined TS_FIXED && defined SOLVE3D &&  \` (4). |
| 18–27 | 시작 시 전처리 조건: `#ifdef ADJOINT` (3) 안; `# if !defined TS_FIXED && defined SOLVE3D &&  \` (4) 안. TS_DIF4 분기는 쌍조화 혼합(biharmonic mixing) 구현 파일을 선택한다(18–26). MIX_S_TS이면 ad_t3dmix4_s.h를, 대체 MIX_GEO_TS이면 ad_t3dmix4_geo.h를, 대체 MIX_ISO_TS이면 ad_t3dmix4_iso.h를 끼워 넣는다(19–24). 이 파일의 include 선택만 판독한 구간이다. 원문 조건·식·호출·전처리(행 순서): `#  ifdef TS_DIF4` (18); `#   if defined MIX_S_TS` (19); `#    include "ad_t3dmix4_s.h"` (20); `#   elif defined MIX_GEO_TS` (21); `#    include "ad_t3dmix4_geo.h"` (22); `#   elif defined MIX_ISO_TS` (23); `#    include "ad_t3dmix4_iso.h"` (24); `#   endif` (25); `#  endif` (26). |
| 28–37 | 시작 시 전처리 조건: `#ifdef ADJOINT` (3) 안; `# if !defined TS_FIXED && defined SOLVE3D &&  \` (4) 안. TS_DIF2 분기는 조화 혼합(harmonic mixing) 구현 파일을 선택한다(28–36). MIX_S_TS이면 ad_t3dmix2_s.h를, 대체 MIX_GEO_TS이면 ad_t3dmix2_geo.h를, 대체 MIX_ISO_TS이면 ad_t3dmix2_iso.h를 끼워 넣는다(29–34). TS_FIXED·SOLVE3D·확산 옵션의 결합 조건을 닫는다(37). 원문 조건·식·호출·전처리(행 순서): `#  ifdef TS_DIF2` (28); `#   if defined MIX_S_TS` (29); `#    include "ad_t3dmix2_s.h"` (30); `#   elif defined MIX_GEO_TS` (31); `#    include "ad_t3dmix2_geo.h"` (32); `#   elif defined MIX_ISO_TS` (33); `#    include "ad_t3dmix2_iso.h"` (34); `#   endif` (35); `#  endif` (36); `# endif` (37). |
| 38–44 | 시작 시 전처리 조건: `#ifdef ADJOINT` (3) 안. ADJOINT가 정의되지 않은 대체 분기는 빈 ad_t3dmix2_mod와 ad_t3dmix4_mod 모듈을 선언한다(38–43). ADJOINT 조건을 닫는다(44). 원문 조건·식·호출·전처리(행 순서): `#else` (38); `      MODULE ad_t3dmix2_mod` (39); `      END MODULE ad_t3dmix2_mod` (40); `      MODULE ad_t3dmix4_mod` (42); `      END MODULE ad_t3dmix4_mod` (43); `#endif` (44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–36: TS_DIF4와 TS_DIF2는 독립된 전처리 블록이다. 두 블록 안에서 MIX_S_TS·MIX_GEO_TS·MIX_ISO_TS는 if·elif 순서로 선택된다.
- 3–5·37–44: ADJOINT가 정의되지 않으면 빈 모듈을 선언한다. ADJOINT가 정의되지만 내부의 TS_FIXED·SOLVE3D·TS_DIF2·TS_DIF4 결합 조건이 거짓이면 이 파일에는 대체 모듈 선언이 없다.
