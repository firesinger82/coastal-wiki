---
file: models/ROMS/raw/source_code/roms/ROMS/Representer/Biology/rp_biology.F
lines: 28
sha256: 5391e96a9436f13964907196bb4633fffa1820f7a05559062d6040356bc18b2b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# rp_biology.F — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#include "cppdefs.h"` (1)로 cppdefs.h를 끼워 넣는다. `#if defined TL_IOMS && defined BIOLOGY` (2)가 표현자(representer)의 접선 선형(tangent linear) 생물학 소스·싱크 항을 선택한다는 주석(4–12)을 감싼다. 빈 줄도 포함한다(3·13). |
| 14–24 | 시작 시 2행 `#if defined TL_IOMS && defined BIOLOGY` 안. `# if defined BIO_FENNEL` (14)의 다음 행은 `!!#  include <rp_fennel.h>` (15)이다. `# elif defined NEMURO` (16)의 다음 행은 `!!#  include <rp_nemuro.h>` (17)이다. 두 include 모양의 행에는 앞에 `!!`가 붙어 있다. `# elif defined NPZD_FRANKS` (18)는 `#  include <rp_npzd_Franks.h>` (19)로 rp_npzd_Franks.h를 끼워 넣는다. `# elif defined NPZD_IRON` (20)는 `#  include <rp_npzd_iron.h>` (21)로 rp_npzd_iron.h를 끼워 넣는다. `# elif defined NPZD_POWELL` (22)는 `#  include <rp_npzd_Powell.h>` (23)로 rp_npzd_Powell.h를 끼워 넣는다. `# endif` (24)가 생물학 모델 선택 조건을 닫는다. 포함 파일 내부는 이 파일의 판독 대상이 아니다. |
| 25–28 | 시작 시 2행 `#if defined TL_IOMS && defined BIOLOGY`가 열려 있다. `#else` (25)는 그 조건이 성립하지 않을 때 `MODULE rp_biology_mod` (26)와 `END MODULE rp_biology_mod` (27)만 남긴다. `#endif` (28)가 바깥 조건을 닫는다. 이 분기의 모듈 본문에는 선언·실행문·루틴이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–17: BIO_FENNEL과 NEMURO 분기의 include 모양의 행은 `!!#`로 시작한다. 다른 세 모델 분기의 include 행은 `#`로 시작한다(19·21·23).
- 14–24: 생물학 모델 선택 조건에는 다섯 모델 분기만 있다. 이 내부 조건에는 `#else` 분기가 없다.
