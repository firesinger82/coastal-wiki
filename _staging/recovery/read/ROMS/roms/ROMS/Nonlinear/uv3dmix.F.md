---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/uv3dmix.F
lines: 43
sha256: 2cc5b4e39b990b5af1062edded754788205080f587a66712e7ddf36721917545
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# uv3dmix.F — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `cppdefs.h`를 포함한다(1). SOLVE3D·NONLINEAR와 UV_VIS2 또는 UV_VIS4의 조건을 연다(3–4). 저작권·MIT/X 라이선스와 운동량(momentum)의 수평 점성(horizontal viscosity) 계산 주석을 포함한다(6–17). 이 구간에는 계산 대입식이나 루틴 호출이 없다. 원문 조건·식·호출·전처리: `#include "cppdefs.h"` (1); `#if defined SOLVE3D && defined NONLINEAR && \` (3); `(defined UV_VIS2 \|\| defined UV_VIS4)` (4). |
| 18–27 | 시작 시 3행 `#if defined SOLVE3D && defined NONLINEAR && \` · 4행 `(defined UV_VIS2 \|\| defined UV_VIS4)` 안. UV_VIS2 조건에서 MIX_S_UV이면 `uv3dmix2_s.h`를 포함한다(18–20). 병렬 `#  elif defined MIX_GEO_UV` (21)는 `uv3dmix2_geo.h`를 포함한다(22). ELSE는 `UV3DMIX: must define one of MIX_S_UV, MIX_GEO_UV` (24)를 원문 본문에 둔다. 방향 조건·UV_VIS2를 닫고 빈 줄을 포함한다(25–27). 원문 조건·식·호출·전처리: `# ifdef UV_VIS2` (18); `#  if defined MIX_S_UV` (19); `#   include "uv3dmix2_s.h"` (20); `#  elif defined MIX_GEO_UV` (21); `#   include "uv3dmix2_geo.h"` (22); `#  else` (23); `#  endif` (25); `# endif` (26). |
| 28–36 | 시작 시 3행 `#if defined SOLVE3D && defined NONLINEAR && \` · 4행 `(defined UV_VIS2 \|\| defined UV_VIS4)` 안. UV_VIS4 조건에서 MIX_S_UV이면 `uv3dmix4_s.h`를 포함한다(28–30). 병렬 `#  elif defined MIX_GEO_UV` (31)는 `uv3dmix4_geo.h`를 포함한다(32). ELSE는 `UV3DMIX: must define one of MIX_S_UV, MIX_GEO_UV` (34)를 원문 본문에 둔다. 방향 조건과 UV_VIS4를 닫는다(35–36). 원문 조건·식·호출·전처리: `# ifdef UV_VIS4` (28); `#  if defined MIX_S_UV` (29); `#   include "uv3dmix4_s.h"` (30); `#  elif defined MIX_GEO_UV` (31); `#   include "uv3dmix4_geo.h"` (32); `#  else` (33); `#  endif` (35); `# endif` (36). |
| 37–43 | 시작 시 3행 `#if defined SOLVE3D && defined NONLINEAR && \` · 4행 `(defined UV_VIS2 \|\| defined UV_VIS4)` 안. 3–4행 최상위 조건의 ELSE 분기를 연다(37). 구현 없는 uv3dmix2_mod와 uv3dmix4_mod 모듈을 각각 선언하고 끝낸다(38–42). 최상위 전처리 조건을 닫는다(43). 원문 조건·식·호출·전처리: `#else` (37); `#endif` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–24·33–34: 혼합면 선택의 ELSE 분기는 `UV3DMIX: must define one of MIX_S_UV, MIX_GEO_UV`라는 본문 행을 포함한다(24·34). 이 두 행은 전처리기의 #error 지시문으로 쓰지 않는다.
