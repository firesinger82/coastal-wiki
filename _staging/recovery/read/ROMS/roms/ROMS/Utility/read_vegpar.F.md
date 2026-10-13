---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/read_vegpar.F
lines: 19
sha256: 27493bbf54a76649878a23253232dbefbc086c9386f881605832f4f57aa26b1a
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# read_vegpar.F — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#ifdef VEGETATION` (2) 안에 저작권·MIT/X 라이선스·식생(vegetation) 모델 입력 매개변수를 읽고 보고한다는 주석이 있다(3–14). `# include <vegetation_inp.h>` (15)로 vegetation_inp.h를 포함한다. 포함 파일 내부는 이 대상 파일의 판독 범위에 없다. |
| 16–19 | 시작 시 2행 `#ifdef VEGETATION` 안. `#else` (16)는 VEGETATION 조건 불성립 경로다. `SUBROUTINE read_vegpar` (17)와 `END SUBROUTINE read_vegpar` (18) 사이에는 실행문이 없다. `#endif` (19)로 전처리 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·15–19: VEGETATION이 정의되면 구현은 vegetation_inp.h에서 삽입된다. VEGETATION이 정의되지 않으면 인수와 실행문이 없는 read_vegpar만 남는다.
