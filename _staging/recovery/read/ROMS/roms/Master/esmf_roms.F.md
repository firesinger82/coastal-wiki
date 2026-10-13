---
file: models/ROMS/raw/source_code/roms/Master/esmf_roms.F
lines: 37
sha256: 49db396f81645447a7dc9cb348765d525b0193036daea49280fb8ad528d84493
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# esmf_roms.F — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 전처리 포함문 `#include "cppdefs.h"` (1)은 cppdefs.h를 끼워 넣는다. 전처리 조건 `#if defined MODEL_COUPLING && defined ESMF_LIB` (2)은 모델 결합과 지구 시스템 모델링 프레임워크(Earth System Modeling Framework, ESMF)를 함께 사용할 때 본문을 포함한다. git 표식·저작권·MIT/X 허가·License_ROMS.md 안내 주석(3–9). 주석은 ROMS 격자 구성요소(gridded component)의 ESMF/국가 통합 운영 예측 기능(National Unified Operational Prediction Capability, NUOPC) 계층이 자체 결합 또는 외부 결합 프레임워크에 쓰인다고 설명한다(11–12). CDEPS·CMEPS의 풀 이름·URL과 ESMF 7 이상·NUOPC의 풀 이름·URL 주석(14–24), 주석 끝·빈 줄(25–28). |
| 29–37 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB` 안. 내부 조건 `# if defined CMEPS` (29)이 참이면 `#  include "cmeps_roms.h"` (30)로 cmeps_roms.h를 끼워 넣는다. 같은 조건의 `# else` (31)는 `#  include "esmf_roms.h"` (32)로 esmf_roms.h를 끼워 넣는다. 내부 조건 끝 `# endif` (33). 2행 조건의 `#else` (34)에서는 내용이 없는 esmf_roms_mod 모듈만 선언·종료한다(35–36). 바깥 조건 끝 `#endif` (37). 포함 파일 내부는 이 대상 파일에 들어 있지 않다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
