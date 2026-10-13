---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/Biology/ad_biology.F
lines: 28
sha256: 5f002a052b455ac499f6d3be10cc93500d9a71824fd092ea6ca652e057c3dbeb
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_biology.F — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#include "cppdefs.h"` (1)로 cppdefs.h를 끼워 넣는다. `#if defined ADJOINT && defined BIOLOGY` (2) 안의 빈 줄과 C 형식 주석은 선택된 생물 모델의 수반 생성항(source)·소멸항(sink)을 계산한다는 설명이다(3–13). |
| 14–24 | 시작 시 2행 `#if defined ADJOINT && defined BIOLOGY` 안. `# if defined BIO_FENNEL` (14), 주석 `!!#  include <ad_fennel.h>` (15), `# elif defined NEMURO` (16), 주석 `!!#  include <ad_nemuro.h>` (17). `# elif defined NPZD_FRANKS` (18), `#  include <ad_npzd_Franks.h>` (19), `# elif defined NPZD_IRON` (20), `#  include <ad_npzd_iron.h>` (21), `# elif defined NPZD_POWELL` (22), `#  include <ad_npzd_Powell.h>` (23), `# endif` (24). 실행되는 include는 각각 ad_npzd_Franks.h·ad_npzd_iron.h·ad_npzd_Powell.h를 끼워 넣는다. |
| 25–28 | 시작 시 2행 `#if defined ADJOINT && defined BIOLOGY` 안. `#else` (25)는 바깥 조건 불성립 분기이다. 내용이 없는 ad_biology_mod 모듈을 선언하고 종료한다(26–27). `#endif` (28)로 바깥 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–17: BIO_FENNEL과 NEMURO 선택 조건은 있지만 대응하는 include 줄은 `!!`로 시작하는 주석이다.
- 14–24: 생물 모델 선택 사슬에는 마지막 대체 `#else`가 없다. 포함 파일 내부는 이번 판독 범위에 없다.
