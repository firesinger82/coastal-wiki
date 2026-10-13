---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/tl_uv3dmix.F
lines: 39
sha256: f51659778d7425f7f652b37add534864343ca737654091c8c0997c8469f03f86
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_uv3dmix.F — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시작 시 열린 전처리 조건 없음. cppdefs.h를 끼워 넣는다(1). 바깥 전처리 조건은 TANGENT와 SOLVE3D가 있으며 UV_VIS2 또는 UV_VIS4가 있는 경우이다(3–4). 저작권·MIT/X 사용권·접선 선형(tangent linear) 수평 운동량 점성(momentum viscosity) 목적의 주석을 포함한다(5–17). 원문: `#include "cppdefs.h"` (1); `#if defined TANGENT && defined SOLVE3D && \` (3); `(defined UV_VIS2 \|\| defined UV_VIS4)` (4). |
| 18–25 | 시작 시 전처리 블록: `#if defined TANGENT && defined SOLVE3D && \` (3); `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. UV_VIS2 안에서 MIX_S_UV이면 tl_uv3dmix2_s.h를 끼워 넣는다(18–20). #elif의 MIX_GEO_UV이면 tl_uv3dmix2_geo.h를 끼워 넣는다(21–22). 두 조건 종료와 빈 줄(23–25). 포함 파일 이름과 전처리 선택만 이 구간의 판독 대상이다. 원문: `# ifdef UV_VIS2` (18); `#  if defined MIX_S_UV` (19); `#   include "tl_uv3dmix2_s.h"` (20); `#  elif defined MIX_GEO_UV` (21); `#   include "tl_uv3dmix2_geo.h"` (22); `#  endif` (23); `# endif` (24). |
| 26–32 | 시작 시 전처리 블록: `#if defined TANGENT && defined SOLVE3D && \` (3); `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. UV_VIS4 안에서 MIX_S_UV이면 tl_uv3dmix4_s.h를 끼워 넣는다(26–28). #elif의 MIX_GEO_UV이면 tl_uv3dmix4_geo.h를 끼워 넣는다(29–30). 두 조건 종료(31–32). 원문: `# ifdef UV_VIS4` (26); `#  if defined MIX_S_UV` (27); `#   include "tl_uv3dmix4_s.h"` (28); `#  elif defined MIX_GEO_UV` (29); `#   include "tl_uv3dmix4_geo.h"` (30); `#  endif` (31); `# endif` (32). |
| 33–39 | 시작 시 전처리 블록: `#if defined TANGENT && defined SOLVE3D && \` (3); `(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. 바깥 3–4행 조건의 #else에서 빈 tl_uv3dmix2_mod와 tl_uv3dmix4_mod를 선언하고 바로 끝낸다(33–38). 39행은 바깥 조건을 닫는다. 원문: `#else` (33); `MODULE tl_uv3dmix2_mod` (34); `END MODULE tl_uv3dmix2_mod` (35); `MODULE tl_uv3dmix4_mod` (37); `END MODULE tl_uv3dmix4_mod` (38); `#endif` (39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–32: UV_VIS2와 UV_VIS4는 서로 독립된 #ifdef 블록이다. 두 블록 모두 MIX_S_UV가 #if이며 MIX_GEO_UV는 그 #elif이다.
- 19–23·27–31·33–38: MIX_S_UV/MIX_GEO_UV 선택에는 #else가 없다. 빈 모듈 두 개의 선언은 바깥 TANGENT/SOLVE3D/점성 조건의 #else에만 있다.
