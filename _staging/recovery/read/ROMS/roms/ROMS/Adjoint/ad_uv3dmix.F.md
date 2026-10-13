---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_uv3dmix.F
lines: 38
sha256: e4dbfb457e7c30b7c4c6aac380ca69c67b7ca7615f8473af3860289e9ccb4d4b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_uv3dmix.F — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 시작 시 열린 전처리 조건·루틴·조건·루프 없음. cppdefs.h를 끼워 넣는다(1). ADJOINT·SOLVE3D와 UV_VIS2 또는 UV_VIS4의 결합 조건에서 구현 헤더를 선택한다(3–4). 수반(adjoint) 수평 운동량 점성(horizontal viscosity of momentum)을 계산한다는 주석이다(13). 저작권·라이선스·빈 줄을 포함한다(2·5–16). 4행은 3행 #if의 연속행이다. 전처리 `#include "cppdefs.h"` (1); 전처리 `#if defined ADJOINT && defined SOLVE3D && \` (3); 전처리 연속행 `(defined UV_VIS2 \|\| defined UV_VIS4)` (4). |
| 17–19 | 시작 시 3행 `#if defined ADJOINT && defined SOLVE3D && \` (3) · `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. UV_VIS2 조건 안에서 MIX_S_UV가 정의되어 있으면 ad_uv3dmix2_s.h를 끼워 넣는다(17–19). 이 구간에는 별도의 실행 루틴 본문이 없다. 전처리 `# ifdef UV_VIS2` (17); 전처리 `#  if defined MIX_S_UV` (18); 전처리 `#   include "ad_uv3dmix2_s.h"` (19). |
| 20–24 | 시작 시 3행 `#if defined ADJOINT && defined SOLVE3D && \` (3) · `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) / 17행 `# ifdef UV_VIS2` (17) / 18행 `#  if defined MIX_S_UV` (18) 안. 18행 MIX_S_UV 조건의 #elif defined MIX_GEO_UV 분기는 ad_uv3dmix2_geo.h를 끼워 넣는다(20–21). 혼합 좌표 선택 조건과 UV_VIS2 조건을 닫고 빈 줄을 포함한다(22–24). 전처리 `#  elif defined MIX_GEO_UV` (20); 전처리 `#   include "ad_uv3dmix2_geo.h"` (21); 전처리 `#  endif` (22); 전처리 `# endif` (23). |
| 25–27 | 시작 시 3행 `#if defined ADJOINT && defined SOLVE3D && \` (3) · `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. 별도 UV_VIS4 조건 안에서 MIX_S_UV가 정의되어 있으면 ad_uv3dmix4_s.h를 끼워 넣는다(25–27). 전처리 `# ifdef UV_VIS4` (25); 전처리 `#  if defined MIX_S_UV` (26); 전처리 `#   include "ad_uv3dmix4_s.h"` (27). |
| 28–31 | 시작 시 3행 `#if defined ADJOINT && defined SOLVE3D && \` (3) · `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) / 25행 `# ifdef UV_VIS4` (25) / 26행 `#  if defined MIX_S_UV` (26) 안. 26행 MIX_S_UV 조건의 #elif defined MIX_GEO_UV 분기는 ad_uv3dmix4_geo.h를 끼워 넣는다(28–29). 혼합 좌표 선택 조건과 UV_VIS4 조건을 닫는다(30–31). 전처리 `#  elif defined MIX_GEO_UV` (28); 전처리 `#   include "ad_uv3dmix4_geo.h"` (29); 전처리 `#  endif` (30); 전처리 `# endif` (31). |
| 32–38 | 시작 시 3행 `#if defined ADJOINT && defined SOLVE3D && \` (3) · `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. 3–4행 외부 조건의 #else 분기이다(32). 실행 루틴 없이 ad_uv3dmix2_mod와 ad_uv3dmix4_mod의 빈 모듈을 선언하고 종료한다(33–37). 외부 전처리 조건을 닫는다(38). 전처리 `#else` (32); `END MODULE ad_uv3dmix2_mod` (34); `END MODULE ad_uv3dmix4_mod` (37); 전처리 `#endif` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17–31: 두 점성 차수 선택 블록은 독립된 #ifdef이다. 각 블록의 혼합 좌표 선택은 MIX_S_UV를 먼저 검사하고 MIX_GEO_UV를 #elif로 검사한다. 두 혼합 좌표 조건이 모두 불성립일 때의 #else는 없다.
