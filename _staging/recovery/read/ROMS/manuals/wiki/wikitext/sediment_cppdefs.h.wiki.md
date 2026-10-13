---
file: models/ROMS/raw/manuals/wiki/wikitext/sediment_cppdefs.h.wiki
lines: 1
sha256: 418258c93e2d5f6da80db66c9f8f0df85aa83634b9c1ebdb525d8eae6cce5c9b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sediment_cppdefs.h.wiki — 판독 구간 기록

구간은 1행부터 1행까지 빈틈없이 이어진다. 한국어 문장은 판독 설명이며, 원문 인용은 행 번호와 함께 구분한다.

| 구간 | 내용 |
|---|---|
| 1–1 | sediment CPPDEFS 예제 — SEDIMENT와 SUSPLOAD 정의, 소류사·형태 변화 옵션 해제, 퇴적물 초기화·파랑 입력의 CPP 조건을 제시한다(1). SG_BBL·MB_BBL·SSW_BBL 분기의 저면 거칠기·로그 보간(logarithmic interpolation)·저면 궤도속도(bottom orbital velocity)·형상 항력(form drag)·연흔 관련 define/undef와 주석을 모두 원문대로 옮긴다(1). 원문 전체는 한 물리 행이며 `<br>`로 예제 줄을 구분한다. 원문: `<div class="box">/* sediment CPPDEFS */<br>#define SEDIMENT<br>#ifdef SEDIMENT /* Chose one or all of these processes: */<br># define SUSPLOAD<br># undef  BEDLOAD_SOULSBY /* or BEDLOAD_MPM */<br># undef  SED_MORPH<br>#endif<br>#if defined SEDIMENT \|\| defined SG_BBL \|\| defined MB_BBL \|\| defined SSW_BBL<br># define ANA_SEDIMENT /* sediment initialization from Fortran routine */<br># undef ANA_SEDIMENT  /* will require initialziation file */<br>#endif<br>#if defined MB_BBL \|\| defined SG_BBL \|\| defined SSW_BBL /* will need wave input */<br># define ANA_WWAVE /* or provide SWAN input */<br>#endif<br>#define SSW_BBL /* or SG_BBL or MB_BBL */<br>#ifdef SG_BBL<br># define SG_CALC_ZNOT<br># undef  SG_LOGINT<br>#endif<br>#ifdef MB_BBL<br># define MB_CALC_ZNOT<br># undef  MB_Z0BIO<br># undef  MB_Z0BL<br># undef  MB_Z0RIP<br>#endif<br>#ifdef SSW_BBL<br># define SSW_CALC_ZNOT /* Compute bottom roughness internally */<br># undef SSW_LOGINT     /* Logarithmic interpolation of (Ur,Vr) */<br># define SSW_CALC_UB   /* Computing bottom orbital velocity internally */<br># undef  SSW_FORM_DRAG_COR   /* Activate form drag coefficient */<br># undef  SSW_ZOBIO     /* Biogenic bedform roughness from ripples */<br># undef  SSW_ZOBL      /* Bedload roughness for ripples */<br># undef  SSW_ZORIP     /* Bedform roughness from ripples */<br>#endif</div>` (1). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 1: 같은 SEDIMENT·SG_BBL·MB_BBL·SSW_BBL 조건 블록 안에서 ANA_SEDIMENT를 define한 뒤 바로 undef한다. 두 줄의 주석은 각각 Fortran 초기화와 초기화 파일 요구를 적는다.
