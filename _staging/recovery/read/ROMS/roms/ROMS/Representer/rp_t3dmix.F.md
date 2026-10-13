---
file: models/ROMS/raw/source_code/roms/ROMS/Representer/rp_t3dmix.F
lines: 45
sha256: b3336b10f9957307d5f47c8b33c1dd7445edfd77aa30478835b283148c3d34d1
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_t3dmix.F — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 포함한다(1). TL_IOMS와 TS_FIXED 미정의·SOLVE3D 정의 및 TS_DIF2 또는 TS_DIF4 정의 조건으로 본체를 선택한다(3–5). 저작권·라이선스·추적자(tracer)의 표현자 접선 선형(representer tangent linear) 수평 혼합 설명 주석과 빈 줄을 포함한다(6–18).<br>원문 조건·반복·계산·호출·전처리 행: `#include "cppdefs.h"` (1); `#ifdef TL_IOMS` (3); `# if !defined TS_FIXED && defined SOLVE3D &&  \` (4); `     (defined TS_DIF2  \|\| defined TS_DIF4)` (5). |
| 19–28 | 시작 시 전처리 조건 `#ifdef TL_IOMS` (3)·`# if !defined TS_FIXED && defined SOLVE3D &&  \` (4); `     (defined TS_DIF2  \|\| defined TS_DIF4)` (5) 안. TS_DIF2의 2차 조화 혼합(harmonic mixing) 포함 파일을 선택한다(19–27). MIX_S_TS이면 `rp_t3dmix2_s.h`, 그 ELSE IF MIX_GEO_TS이면 `rp_t3dmix2_geo.h`, 그 ELSE IF MIX_ISO_TS이면 `rp_t3dmix2_iso.h`를 포함한다(20–25). 각 전처리 종료와 빈 줄을 포함한다(26–28).<br>원문 조건·반복·계산·호출·전처리 행: `#  ifdef TS_DIF2` (19); `#   if defined MIX_S_TS` (20); `#    include "rp_t3dmix2_s.h"` (21); `#   elif defined MIX_GEO_TS` (22); `#    include "rp_t3dmix2_geo.h"` (23); `#   elif defined MIX_ISO_TS` (24); `#    include "rp_t3dmix2_iso.h"` (25); `#   endif` (26); `#  endif` (27). |
| 29–38 | 시작 시 전처리 조건 `#ifdef TL_IOMS` (3)·`# if !defined TS_FIXED && defined SOLVE3D &&  \` (4); `     (defined TS_DIF2  \|\| defined TS_DIF4)` (5) 안. TS_DIF4의 4차 이중 조화 혼합(biharmonic mixing) 포함 파일을 선택한다(29–37). MIX_S_TS이면 `rp_t3dmix4_s.h`, MIX_GEO_TS이면 `rp_t3dmix4_geo.h`, MIX_ISO_TS이면 `rp_t3dmix4_iso.h`를 같은 if·elif 순서로 포함한다(30–35). 이 세 포함 파일 내부는 이번 판독 대상이 아니다. 내부 및 외부 전처리 조건 종료를 포함한다(36–38).<br>원문 조건·반복·계산·호출·전처리 행: `#  ifdef TS_DIF4` (29); `#   if defined MIX_S_TS` (30); `#    include "rp_t3dmix4_s.h"` (31); `#   elif defined MIX_GEO_TS` (32); `#    include "rp_t3dmix4_geo.h"` (33); `#   elif defined MIX_ISO_TS` (34); `#    include "rp_t3dmix4_iso.h"` (35); `#   endif` (36); `#  endif` (37); `# endif` (38). |
| 39–45 | 시작 시 전처리 조건 `#ifdef TL_IOMS` (3) 안. TL_IOMS 조건의 else에서 빈 rp_t3dmix2_mod·rp_t3dmix4_mod 모듈을 선언하고 바로 닫는다(39–44). 최상위 TL_IOMS 조건을 닫는다(45).<br>원문 조건·반복·계산·호출·전처리 행: `#else` (39); `#endif` (45). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–27·29–37: TS_DIF2와 TS_DIF4는 서로 독립된 전처리 if 블록이다. 각 블록의 좌표 선택은 MIX_S_TS·MIX_GEO_TS·MIX_ISO_TS의 if·elif 순서이며 마지막 else는 없다.
- 3–5·38–45: 빈 두 모듈은 TL_IOMS의 else에서만 선언한다. TL_IOMS가 정의되고 4–5행 조건이 거짓이면 이 파일의 본체에는 해당 빈 모듈 선언도 포함되지 않는다.
