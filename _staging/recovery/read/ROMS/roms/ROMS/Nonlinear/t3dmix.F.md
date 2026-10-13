---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/t3dmix.F
lines: 47
sha256: 789ac961f833e650ea390e641f08494e1ecd13c6d933426ef4ac53aa7269eb94
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# t3dmix.F — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시작 시 열린 전처리 조건 없음. cppdefs.h를 끼워 넣는다(1). TS_FIXED가 없고 SOLVE3D·NONLINEAR가 있으며 TS_DIF2 또는 TS_DIF4이면 혼합 구현을 포함하는 바깥 조건이다(3–4). 라이선스와 추적자(tracer)의 수평 혼합(horizontal mixing)을 계산한다는 주석을 포함한다(6–17). 원문(행 순서): `#include "cppdefs.h"` (1) `#if !defined TS_FIXED && defined SOLVE3D && defined NONLINEAR && \` (3) `    (defined TS_DIF2  \|\| defined TS_DIF4)` (4). |
| 18–29 | 시작 시 3행 `#if !defined TS_FIXED && defined SOLVE3D && defined NONLINEAR && \` 및 4행 `    (defined TS_DIF2  \|\| defined TS_DIF4)` 안. TS_DIF2이면 MIX_S_TS에 t3dmix2_s.h, MIX_GEO_TS에 t3dmix2_geo.h, MIX_ISO_TS에 t3dmix2_iso.h를 끼워 넣는다(18–24). else는 `      T3DMIX: must define one of MIX_S_TS, MIX_GEO_TS, MIX_ISO_TS` (26)를 둔다. 두 조건을 닫는다(27–28). 원문(행 순서): `# ifdef TS_DIF2` (18) `#  if defined MIX_S_TS` (19) `#   include "t3dmix2_s.h"` (20) `#  elif defined MIX_GEO_TS` (21) `#   include "t3dmix2_geo.h"` (22) `#  elif defined MIX_ISO_TS` (23) `#   include "t3dmix2_iso.h"` (24) `#  else` (25) `#  endif` (27) `# endif` (28). |
| 30–40 | 시작 시 3행 `#if !defined TS_FIXED && defined SOLVE3D && defined NONLINEAR && \` 및 4행 `    (defined TS_DIF2  \|\| defined TS_DIF4)` 안. TS_DIF4이면 MIX_S_TS에 t3dmix4_s.h, MIX_GEO_TS에 t3dmix4_geo.h, MIX_ISO_TS에 t3dmix4_iso.h를 끼워 넣는다(30–36). else는 `      T3DMIX: must define one of MIX_S_TS, MIX_GEO_TS, MIX_ISO_TS` (38)를 둔다. 두 조건을 닫는다(39–40). 원문(행 순서): `# ifdef TS_DIF4` (30) `#  if defined MIX_S_TS` (31) `#   include "t3dmix4_s.h"` (32) `#  elif defined MIX_GEO_TS` (33) `#   include "t3dmix4_geo.h"` (34) `#  elif defined MIX_ISO_TS` (35) `#   include "t3dmix4_iso.h"` (36) `#  else` (37) `#  endif` (39) `# endif` (40). |
| 41–47 | 시작 시 3행 `#if !defined TS_FIXED && defined SOLVE3D && defined NONLINEAR && \` 및 4행 `    (defined TS_DIF2  \|\| defined TS_DIF4)` 안. 3–4행의 바깥 조건이 거짓인 else는 내용 없는 t3dmix2_mod와 t3dmix4_mod 모듈을 정의한다(41–46). 바깥 조건을 닫는다(47). 원문(행 순서): `#else` (41) `#endif` (47). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–28·30–40: TS_DIF2와 TS_DIF4 선택은 서로 독립된 두 전처리 조건이다.
- 19–24·31–36: 혼합면 선택 순서는 MIX_S_TS, MIX_GEO_TS, MIX_ISO_TS의 #if/#elif 사슬이다. 여러 정의가 동시에 참인 경우에도 앞에서 선택한 분기 이후의 #elif 파일은 끼워 넣지 않는다.
