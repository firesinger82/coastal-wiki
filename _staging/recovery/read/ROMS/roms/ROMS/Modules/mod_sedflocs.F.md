---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_sedflocs.F
lines: 28
sha256: ef5d219333dfa8f925a7540a8ee21c73031a5fb64feade2559ba6f248cb425cb
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_sedflocs.F — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣고, `MODULE mod_sedflocs` (2)가 모듈을 연다. 빈 줄과 git 식별자·2002–2026 ROMS Group 저작권·MIT/X 형식 라이선스·License_ROMS.md 안내를 포함한다(3–11). 주석은 응집(flocculation) 상호작용 속성의 구조를 선언한다고 설명한다(12–14). 주석은 ROMS/Nonlinear/Sediment의 헤더를 프로젝트 디렉터리에서 변경할 수 있도록 꺾쇠 포함문으로 읽는다고 설명한다(16–19). 주석 종료와 빈 줄을 포함한다(20–23). |
| 24–28 | 시작 시 2행 mod_sedflocs 모듈 안이며 열린 전처리 조건 없음. `#if defined SEDIMENT` (24)의 참 분기에서 `# include <sedflocs_mod.h>` (25)로 sedflocs_mod.h를 끼워 넣는다. `#endif` (26)가 조건을 닫는다. 빈 줄(27)과 모듈 종료(28)를 포함한다. 이 파일에는 계산식과 루틴 호출이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
