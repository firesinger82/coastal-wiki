---
file: models/ROMS/raw/source_code/roms/Master/master.F
lines: 27
sha256: f94e5ee992fb805e486e3c02f68eee526c15f79a413f9721147d799c3ce7c88b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# master.F — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `cppdefs.h`를 끼워 넣는 전처리 지시문(1)과 저작권·MIT/X 라이선스·모델 결합용 주 프로그램이라는 주석(2–14), 빈 줄(15). 원문 조건·대입식·반복·전처리: `#include "cppdefs.h"` (1). |
| 16–24 | 모델 결합(model coupling)이 활성화되고 CMEPS가 없을 때 MCT_LIB이면 `mct_driver.h`(18), ESMF_LIB이면 `esmf_driver.h`(20)를 끼워 넣는다. 두 라이브러리 조건이 모두 거짓인 분기는 외부 드라이버를 가정하는 내용 없는 `PROGRAM master`와 종료문(22–23)이다. 내부 조건을 24행에서 닫는다. 원문 조건·대입식·반복·전처리: `#if defined MODEL_COUPLING && !defined CMEPS` (16); `# if defined MCT_LIB` (17); `#  include "mct_driver.h"` (18); `# elif defined ESMF_LIB` (19); `#  include "esmf_driver.h"` (20); `# else` (21); `# endif` (24). |
| 25–27 | 시작 시 16행 `#if defined MODEL_COUPLING && !defined CMEPS` 안. 시작 시 16행 외부 전처리 조건 안. 25행은 그 조건의 거짓 분기를 시작한다. 이 분기는 `roms.h`(26)를 끼워 넣고 27행에서 외부 조건을 닫는다. 원문 조건·대입식·반복·전처리: `#else` (25); `# include "roms.h"` (26); `#endif` (27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–24: MCT_LIB와 ESMF_LIB가 모두 정의된 경우 먼저 검사하는 MCT_LIB 분기가 선택된다.
