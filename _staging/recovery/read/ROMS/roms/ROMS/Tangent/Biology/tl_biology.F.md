---
file: models/ROMS/raw/source_code/roms/ROMS/Tangent/Biology/tl_biology.F
lines: 28
sha256: 8c7969fb25167787880253d4fe8729743cf8df62158134deebaa214a26edad60
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# tl_biology.F — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 시작 시 바깥 루틴·조건·루프 없음. 열린 전처리 조건 없음. cppdefs.h를 포함한다(1). TANGENT·BIOLOGY가 모두 정의되면 선택된 생물학 모형(biology model)의 접선선형(tangent linear) 생성항과 소멸항(source and sink terms)을 계산한다는 C형 주석을 포함한다(2–12). BIO_FENNEL의 `!!#  include <tl_fennel.h>` (15), NEMURO의 `!!#  include <tl_nemuro.h>` (17)는 주석 처리되어 있다. 하나의 #if/#elif 체인에서 NPZD_FRANKS이면 tl_npzd_Franks.h(18–19), NPZD_IRON이면 tl_npzd_iron.h(20–21), NPZD_POWELL이면 tl_npzd_Powell.h(22–23)를 포함한다. 내부 선택 체인을 닫는다(24). 2행 조건의 else에서는 빈 tl_biology_mod를 선언하고 종료한다(25–27). 바깥 조건을 닫는다(28). 포함 파일 내부는 이 대상 파일의 판독 범위에 포함하지 않았다. 원문: `#include "cppdefs.h"` (1); `#if defined TANGENT && defined BIOLOGY` (2); `# if defined BIO_FENNEL` (14); `# elif defined NEMURO` (16); `# elif defined NPZD_FRANKS` (18); `#  include <tl_npzd_Franks.h>` (19); `# elif defined NPZD_IRON` (20); `#  include <tl_npzd_iron.h>` (21); `# elif defined NPZD_POWELL` (22); `#  include <tl_npzd_Powell.h>` (23); `# endif` (24); `#else` (25); `#endif` (28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–24: 생물학 모형 선택은 하나의 #if/#elif 체인이다. BIO_FENNEL·NEMURO의 include는 !!로 주석 처리되어 있다(15·17). NPZD_FRANKS·NPZD_IRON·NPZD_POWELL의 include는 활성 전처리 지시문이다(19·21·23). 이 선택 체인에는 #else가 없다.
