---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_ice.F
lines: 48
sha256: 3cdbc90107184b4fdf012baf338f32d0d899f26a18ef89e1af230812316d9d98
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_ice.F — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣는다. C 형식 블록 주석(2–40)에 저작권·라이선스(3–8), 해빙(sea ice) 변수·매개변수 선언 및 모델 사용자 확장 목적(10–13)을 적는다. 구성 파일 설명은 내부 선언 ice_mod.h(17–19), 표준 입력 ice.in(21–23), 입력 판독 ice_inp.h(25–27), varinfo.yaml 메타데이터의 변수 인덱스 ice_var.h(29–32). 주석은 .h 파일들이 ROMS/Nonlinear/SeaIce에 있고 꺾쇠 포함을 통해 프로젝트 디렉터리에서 사용자 지정한다고 설명(34–37). 이 구간에는 Fortran 실행문이 없다. 전처리 원문: `#include "cppdefs.h"` (1). |
| 41–48 | SEAICE 분기 안에서 ICE_MODEL이 정의되면 `#  include <ice_mod.h>` (43)로 ice_mod.h를 끼워 넣는다. 포함 파일 내부는 이 판독 범위에 없다. SEAICE 조건의 else(45)에서는 빈 mod_ice 모듈을 정의하고 종료(46–47). 파일 조건 종료(48). 이 파일 자체에는 변수 선언·계산식·루틴 호출이 없다. 전처리 원문: `#ifdef SEAICE` (41); `# if defined ICE_MODEL` (42); `#  include <ice_mod.h>` (43); `# endif` (44); `#else` (45); `#endif` (48). |


## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15·17–32: 주석은 각 해빙 모델이 seven files로 구성된다고 설명한다. 이 주석의 번호 목록은 (1)–(4)까지이며 파일명은 ice_mod.h·ice.in·ice_inp.h·ice_var.h 네 개이다.
