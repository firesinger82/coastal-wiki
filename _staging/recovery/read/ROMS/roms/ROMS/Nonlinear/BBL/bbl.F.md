---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/BBL/bbl.F
lines: 29
sha256: b776ba5dce76cb55ecf8e9255c2ed53ac1ac715187f4a957df540ab0c678b4cb
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# bbl.F — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)로 `cppdefs.h`를 끼워 넣는다. `#if defined NONLINEAR && defined BBL_MODEL` (2)가 활성 구현 선택부를 감싼다. 저작권·MIT/X 라이선스 주석(4–9). 저층 경계층(bottom boundary layer) 공식으로 바닥 운동량 응력(bottom momentum stress)을 계산한다는 주석이다(11–12). 닫는 주석행까지 포함한다(13–15). |
| 16–25 | 시작 시 2행 `#if defined NONLINEAR && defined BBL_MODEL` 안. `# if defined SSW_BBL` (16)에서는 `#  include "ssw_bbl.h"` (17)로 `ssw_bbl.h`를 끼워 넣는다. `# elif defined MB_BBL` (18)에서는 `#  include "mb_bbl.h"` (19)로 `mb_bbl.h`를 끼워 넣는다. `# elif defined SG_BBL` (20)에서는 `#  include "sg_bbl.h"` (21)로 `sg_bbl.h`를 끼워 넣는다. 같은 조건 사슬의 `# else` (22)에서는 빈 `bbl_mod` 모듈을 정의한다(23–24). `# endif` (25)로 내부 선택을 닫는다. 포함 파일 내부의 루틴·계산식은 이 대상 파일에서 판독하지 않았다. |
| 26–29 | 시작 시 2행 `#if defined NONLINEAR && defined BBL_MODEL`의 참 분기 안이며 16행 내부 조건은 닫힌 상태. 바깥 `#else` (26)에서는 빈 `bbl_mod` 모듈을 정의한다(27–28). `#endif` (29)로 2행 조건을 닫는다. 이 파일에 직접 적힌 계산식·기본값 대입·실행 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
