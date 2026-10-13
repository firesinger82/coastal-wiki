---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_sedbed.F
lines: 28
sha256: 4835c9cf07b7e3e7c19073bf886411d08a50d995450d82557814f968622322dc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_sedbed.F — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣는다. 빈 줄과 git 식별자·2002–2026 ROMS Group 저작권·MIT/X 형식 라이선스·License_ROMS.md 안내 주석을 포함한다(2–10). 주석은 퇴적층(bed layers)·층서(stratigraphy)·바닥 속성의 구조를 선언하는 모듈이라고 설명한다(11–13). 주석은 ROMS/Nonlinear/Sediment의 헤더를 프로젝트 디렉터리에서 사용자 변경이 가능하도록 꺾쇠 포함문으로 읽는다고 설명한다(15–18). 주석 종료와 빈 줄까지 포함한다(19–22). |
| 23–28 | 시작 시 열린 전처리 조건 없음. `#if defined SEDIMENT \|\| defined BBL_MODEL` (23)의 참 분기에서 `# include <sedbed_mod.h>` (24)로 sedbed_mod.h를 끼워 넣는다. `#else` (25) 분기는 빈 `MODULE mod_sedbed`·`END MODULE mod_sedbed`만 둔다(26–27). `#endif` (28)가 조건을 닫는다. 이 파일에는 계산식과 루틴 호출이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
