---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_prsgrd.F
lines: 30
sha256: deeebe025701ffc638251242d853d7809dc15d901da0f495885362d3237e7f2b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_prsgrd.F — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건·루틴·반복·분기 없음. `cppdefs.h`를 포함한다(1). `ADJOINT`·`SOLVE3D` 조합은 경압(baroclinic) 정수압 압력경도(hydrostatic pressure gradient)의 수반(adjoint) 항을 계산한다는 주석을 둔다(2·11–12). 저작권·라이선스·구분 주석을 포함한다(3–15).<br>원문 조건·반복·대입·호출·전처리 행:<br>`#include "cppdefs.h"` (1)<br>`#if defined ADJOINT && defined SOLVE3D` (2) |
| 16–17 | 시작 시 전처리 2행 `#if defined ADJOINT && defined SOLVE3D` 안. 압력경도 방법의 전처리 선택을 시작한다(16). `PJ_GRADPQ4`의 원문은 `!!#  include "ad_prsgrd44.h"` (17)이다. 이 포함 지시 형태는 `!!`로 주석 처리되어 있다.<br>원문 조건·반복·대입·호출·전처리 행:<br>`# if defined PJ_GRADPQ4` (16) |
| 18–19 | 시작 시 전처리 2행 `#if defined ADJOINT && defined SOLVE3D`·16행 `# if defined PJ_GRADPQ4`의 18행 `# elif defined PJ_GRADPQ2` 분기 안. 같은 선택 사슬의 `PJ_GRADPQ2` 분기이다(18). 원문은 `!!#  include "ad_prsgrd42.h"` (19)이다. 이 포함 지시 형태도 `!!`로 주석 처리되어 있다.<br>원문 조건·반복·대입·호출·전처리 행:<br>`# elif defined PJ_GRADPQ2` (18) |
| 20–21 | 시작 시 전처리 2행 `#if defined ADJOINT && defined SOLVE3D`·16행 `# if defined PJ_GRADPQ4`의 20행 `# elif defined PJ_GRADP` 분기 안. 같은 선택 사슬의 `PJ_GRADP` 분기는 `ad_prsgrd40.h`를 포함한다(20–21). 포함 파일의 내부는 지정된 판독 대상에 없다.<br>원문 조건·반복·대입·호출·전처리 행:<br>`# elif defined PJ_GRADP` (20)<br>`#  include "ad_prsgrd40.h"` (21) |
| 22–23 | 시작 시 전처리 2행 `#if defined ADJOINT && defined SOLVE3D`·16행 `# if defined PJ_GRADPQ4`의 22행 `# elif defined DJ_GRADPS` 분기 안. 같은 선택 사슬의 `DJ_GRADPS` 분기는 `ad_prsgrd32.h`를 포함한다(22–23). 포함 파일의 내부는 지정된 판독 대상에 없다.<br>원문 조건·반복·대입·호출·전처리 행:<br>`# elif defined DJ_GRADPS` (22)<br>`#  include "ad_prsgrd32.h"` (23) |
| 24–26 | 시작 시 전처리 2행 `#if defined ADJOINT && defined SOLVE3D`·16행 `# if defined PJ_GRADPQ4`의 24행 `# else` 분기 안. 같은 선택 사슬의 대체 분기는 `ad_prsgrd31.h`를 포함하고 방법 선택 조건을 닫는다(24–26). 포함 파일의 내부는 지정된 판독 대상에 없다.<br>원문 조건·반복·대입·호출·전처리 행:<br>`# else` (24)<br>`#  include "ad_prsgrd31.h"` (25)<br>`# endif` (26) |
| 27–30 | 시작 시 전처리 2행 `#if defined ADJOINT && defined SOLVE3D`의 27행 `#else` 분기 안. `ADJOINT`·`SOLVE3D` 조합의 대체 분기는 실행 루틴 없는 `ad_prsgrd_mod`를 선언·종료한다(27–29). 전체 전처리 조건을 닫는다(30).<br>원문 조건·반복·대입·호출·전처리 행:<br>`#else` (27)<br>`#endif` (30) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–19: `PJ_GRADPQ4`·`PJ_GRADPQ2` 분기의 포함 지시는 각각 `!!#  include "ad_prsgrd44.h"` (17)·`!!#  include "ad_prsgrd42.h"` (19)로 주석 처리되어 있다. 두 분기는 활성 `#include` 행을 갖지 않는다. 뒤의 세 선택 분기는 활성 포함 지시를 갖는다(21·23·25).
