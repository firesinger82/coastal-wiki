---
file: models/ROMS/raw/source_code/roms/ROMS/Representer/rp_uv3dmix.F
lines: 39
sha256: 104408050246ba0cb21e72041a9b23e214a0f59e233c13427adcca675c17d6f7
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_uv3dmix.F — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 시작 시 열린 전처리 조건 없음. 시작 시 열린 실행 블록 없음. `cppdefs.h`를 포함한다(1). 외부 구현 조건은 TL_IOMS·SOLVE3D와 UV_VIS2 또는 UV_VIS4이다(3–4). 6–11행은 저작권·MIT/X 라이선스 주석이며 13–14행은 표현자 접선 선형 수평 운동량 점성을 계산한다고 설명한다. 빈 줄·주석까지 포함한다. 원문 조건·루프·대입식·호출·전처리: `#include "cppdefs.h"` (1); `#if defined TL_IOMS && defined SOLVE3D && \` (3); `(defined UV_VIS2 \|\| defined UV_VIS4)` (4). |
| 18–25 | 시작 시 전처리 `#if defined TL_IOMS && defined SOLVE3D && \` (3)·`(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. 시작 시 열린 실행 블록 없음. UV_VIS2 안에서 MIX_S_UV이면 `rp_uv3dmix2_s.h`를 포함한다(18–20). 같은 조건의 elif MIX_GEO_UV이면 `rp_uv3dmix2_geo.h`를 포함한다(21–22). 안쪽·바깥 전처리 조건을 닫는다(23–24). 원문 조건·루프·대입식·호출·전처리: `# ifdef UV_VIS2` (18); `#  if defined MIX_S_UV` (19); `#   include "rp_uv3dmix2_s.h"` (20); `#  elif defined MIX_GEO_UV` (21); `#   include "rp_uv3dmix2_geo.h"` (22); `#  endif` (23); `# endif` (24). |
| 26–32 | 시작 시 전처리 `#if defined TL_IOMS && defined SOLVE3D && \` (3)·`(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. 시작 시 열린 실행 블록 없음. UV_VIS4 안에서 MIX_S_UV이면 `rp_uv3dmix4_s.h`를 포함한다(26–28). 같은 조건의 elif MIX_GEO_UV이면 `rp_uv3dmix4_geo.h`를 포함한다(29–30). 두 전처리 조건을 닫는다(31–32). 원문 조건·루프·대입식·호출·전처리: `# ifdef UV_VIS4` (26); `#  if defined MIX_S_UV` (27); `#   include "rp_uv3dmix4_s.h"` (28); `#  elif defined MIX_GEO_UV` (29); `#   include "rp_uv3dmix4_geo.h"` (30); `#  endif` (31); `# endif` (32). |
| 33–39 | 시작 시 전처리 `#if defined TL_IOMS && defined SOLVE3D && \` (3)·`(defined UV_VIS2 \|\| defined UV_VIS4)` (4) 안. 시작 시 열린 실행 블록 없음. 외부 구현 조건이 거짓인 ELSE에서는 실행 루틴 없이 rp_uv3dmix2_mod와 rp_uv3dmix4_mod 모듈을 각각 선언하고 닫는다(33–38). 외부 전처리 조건을 닫는다(39). 원문 조건·루프·대입식·호출·전처리: `#else` (33); `#endif` (39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–32: UV_VIS2와 UV_VIS4는 서로 독립된 ifdef 블록이다. 각 블록에서 MIX_S_UV는 if이고 MIX_GEO_UV는 elif이므로 두 혼합 방향 매크로가 함께 정의되면 MIX_S_UV 포함 갈래를 선택한다.
- 3–4·18–32·33–39: 외부 구현 조건이 참인 갈래에서 MIX_S_UV와 MIX_GEO_UV가 모두 정의되지 않으면 헤더 포함문을 실행하지 않는다. 빈 모듈 선언은 외부 조건이 거짓인 ELSE에만 있다.
