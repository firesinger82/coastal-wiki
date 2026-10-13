---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/read_biopar.F
lines: 38
sha256: c7f627b42b0df7bdfb49913c0a70c9beba0a79a1b6e3ffe57f00409cca4acbb6
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# read_biopar.F — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 포함하고 BIOLOGY 조건을 연다(1–2). 저작권·라이선스와 선택된 생물 모델(biological model) 매개변수의 판독·보고 목적을 적은 주석이다(3–15). 이 구간에는 실행문이나 매개변수 기본값 대입이 없다. 전처리 원문: `#include "cppdefs.h"` (1); `#ifdef BIOLOGY` (2). |
| 16–25 | 시작 시 전처리 바깥 블록 `#ifdef BIOLOGY` (2) 안. BIOLOGY 안의 생물 모델 헤더 선택을 시작한다(16–25). BIO_FENNEL은 fennel_inp.h(16–17), ECB는 ecb_inp.h(18–19), ECOSIM은 ecosim_inp.h(20–21), HYPOXIA_SRM은 hypoxia_srm_inp.h(22–23), NEMURO는 nemuro_inp.h(24–25)를 끼워 넣는다. #if/#elif 순서에서 먼저 성립하는 분기를 선택한다. 포함 파일 내부는 이 대상 원문에 들어 있지 않다. 전처리 원문: `# if defined BIO_FENNEL` (16); `#  include <fennel_inp.h>` (17); `# elif defined ECB` (18); `#  include <ecb_inp.h>` (19); `# elif defined ECOSIM` (20); `#  include <ecosim_inp.h>` (21); `# elif defined HYPOXIA_SRM` (22); `#  include <hypoxia_srm_inp.h>` (23); `# elif defined NEMURO` (24); `#  include <nemuro_inp.h>` (25). |
| 26–34 | 시작 시 전처리 바깥 블록 `#ifdef BIOLOGY` (2); `# if defined BIO_FENNEL` (16); `# elif defined NEMURO` (24) 안. 생물 모델 선택의 #elif가 이어진다(26–34). NPZD_FRANKS는 npzd_Franks_inp.h(26–27), NPZD_IRON은 npzd_iron_inp.h(28–29), NPZD_POWELL은 npzd_Powell_inp.h(30–31), RED_TIDE는 red_tide_inp.h(32–33)를 끼워 넣는다. 16행 선택 조건을 닫는다(34). 이 선택 체인에는 #else가 없다. 전처리 원문: `# elif defined NPZD_FRANKS` (26); `#  include <npzd_Franks_inp.h>` (27); `# elif defined NPZD_IRON` (28); `#  include <npzd_iron_inp.h>` (29); `# elif defined NPZD_POWELL` (30); `#  include <npzd_Powell_inp.h>` (31); `# elif defined RED_TIDE` (32); `#  include <red_tide_inp.h>` (33); `# endif` (34). |
| 35–38 | 시작 시 전처리 바깥 블록 `#ifdef BIOLOGY` (2) 안. BIOLOGY의 else로 전환한다(35). BIOLOGY가 정의되지 않으면 인수와 실행문이 없는 `read_BioPar` 스텁(stub) 루틴을 정의한다(36–37). BIOLOGY 조건을 닫는다(38). 전처리 원문: `#else` (35); `#endif` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–34: BIOLOGY 안의 9개 생물 모델 선택은 #if/#elif 체인이며 #else 기본 분기가 없다. 이 파일에 직접 적힌 read_BioPar 스텁은 BIOLOGY가 없는 바깥 #else에만 있다(35–37).
