---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/read_icepar.F
lines: 21
sha256: 47dec58eb83aecc2db495840926f8af775c1b7074256c6716e133d308001c18b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# read_icepar.F — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 시작 시 열린 전처리 조건은 없다. `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#ifdef SEAICE` (2)가 해빙(sea ice) 입력 처리 분기를 연다. 버전 식별 주석·저작권·MIT/X 계열 라이선스·License_ROMS.md 안내(3–9). 목적 주석은 해빙 모델 입력 매개변수를 읽고 보고한다고 적는다(10–13). 빈 주석(14). 이 구간에는 SUBROUTINE 선언이나 실행문이 없다. |
| 15–17 | 시작 시 2행 `#ifdef SEAICE`의 참 분기 안. `# if defined ICE_MODEL` (15)가 ICE_MODEL 정의 여부를 검사한다. `#  include <ice_inp.h>` (16)으로 ice_inp.h를 포함한다. `# endif` (17)이 15행 조건을 닫는다. 이 대상 파일에는 포함 파일의 루틴 본문·조건·대입식이 직접 적혀 있지 않다. |
| 18–21 | 시작 시 2행 `#ifdef SEAICE`의 참 분기 안이며 15행 ICE_MODEL 조건은 17행에서 종료되었다. `#else` (18)가 SEAICE 미정의 분기로 전환한다. `SUBROUTINE read_IcePar` (19)와 `END SUBROUTINE read_IcePar` (20)은 인수와 실행문이 없는 read_IcePar 루틴을 선언한다. `#endif` (21)이 2행 SEAICE 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·15–20: SEAICE가 정의되고 ICE_MODEL이 정의되지 않은 분기에는 ice_inp.h 포함이나 직접 작성된 read_IcePar 선언이 없다. 빈 read_IcePar 선언은 SEAICE 조건의 ELSE 분기에 있다(18–20).
