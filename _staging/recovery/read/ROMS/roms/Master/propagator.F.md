---
file: models/ROMS/raw/source_code/roms/Master/propagator.F
lines: 64
sha256: 5e77eb70d81cf714ff6828ffba98d8ba4786ea13e489e0c1d68ddd0e6a99d5c5
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator.F — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | `#include "cppdefs.h"` (1)로 cppdefs.h를 끼워 넣는다. `#ifdef PROPAGATOR` (2) 안에 저작권·MIT/X 라이선스와 일반화 안정성 이론(Generalized Stability Theory, GST) 드라이버 설명이 있다(3–29). Moore 등 2004 참조 주석과 빈 주석을 포함한다(30–37). |
| 38–49 | 시작 시 2행 `#ifdef PROPAGATOR` 안. `# if defined AFT_EIGENMODES` (38), `#  include "propagator_afte.h"` (39), `# elif defined FT_EIGENMODES` (40), `#  include "propagator_fte.h"` (41), `# elif defined FORCING_SV` (42), `#  include "propagator_fsv.h"` (43), `# elif defined HESSIAN_FSV` (44). 45행 `!!#  include "propagator_hfsv.h"`는 주석이다. 이어 `# elif defined OPT_PERTURBATION` (46), `#  include "propagator_op.h"` (47), `# elif defined HESSIAN_SV` (48), `#  include "propagator_hop.h"` (49). 선택된 조건의 해당 이름 파일을 끼워 넣는다. |
| 50–60 | 시작 시 2행 `#ifdef PROPAGATOR` 및 38행에서 시작한 전처리 선택 사슬 안. `# elif defined STOCHASTIC_OPT` (50) 안에서 `#  ifdef HESSIAN_SO` (51)이면 `#    include "propagator_hso.h"` (52), `#  else` (53)이면 `#    include "propagator_so.h"` (54), `#  endif` (55). 다음 병렬 조건은 `# elif defined SO_SEMI` (56), `#  include "propagator_so_semi.h"` (57), `# elif defined SO_TRACE` (58)이다. 59행 `!!#  include "propagator_so_trace.h"`는 주석이다. `# endif` (60)로 선택 사슬을 닫는다. include는 각각 표시된 이름 파일을 끼워 넣는다. |
| 61–64 | 시작 시 2행 `#ifdef PROPAGATOR` 안. `#else` (61)는 PROPAGATOR가 정의되지 않은 분기이다. 내용이 없는 `MODULE propagator_mod`와 `END MODULE propagator_mod`를 둔다(62–63). `#endif` (64)로 바깥 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·38–39: 설명 주석의 드라이버 이름은 propagator_adte이다. 실제 AFT_EIGENMODES 분기의 포함 파일 이름은 propagator_afte.h이다.
- 44–45·58–59: HESSIAN_FSV와 SO_TRACE 조건은 있지만 두 include 줄은 `!!`로 시작하는 주석이다.
- 38–60: PROPAGATOR 참 분기의 전처리 선택 사슬에는 마지막 대체 `#else`가 없다. 각 포함 파일 내부는 이번 판독 범위에 없다.
