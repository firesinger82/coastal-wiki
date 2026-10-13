---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/read_sedpar.F
lines: 19
sha256: 778e0dd454400147e76d29a4114a6f9ec390981caf0eda00c2f703740e88bf28
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# read_sedpar.F — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#ifdef SEDIMENT` (2) 안에 저작권·MIT/X 라이선스·퇴적물(sediment) 모델 입력 매개변수를 읽고 보고한다는 주석이 있다(3–14). `# include <sediment_inp.h>` (15)로 sediment_inp.h를 포함한다. 포함 파일 내부는 이 대상 파일의 판독 범위에 없다. |
| 16–19 | 시작 시 2행 `#ifdef SEDIMENT` 안. `#else` (16)는 SEDIMENT 조건 불성립 경로다. `SUBROUTINE read_SedPar` (17)와 `END SUBROUTINE read_SedPar` (18) 사이에는 실행문이 없다. `#endif` (19)로 전처리 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·15–19: SEDIMENT가 정의되면 구현은 sediment_inp.h에서 삽입된다. SEDIMENT가 정의되지 않으면 인수와 실행문이 없는 read_SedPar만 남는다.
