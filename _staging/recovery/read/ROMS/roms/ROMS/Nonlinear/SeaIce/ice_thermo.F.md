---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/SeaIce/ice_thermo.F
lines: 24
sha256: a6be883f0f03343164918e91d2368ba7784ea71d2e1c61245a02701c42259a5f
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ice_thermo.F — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `cppdefs.h`를 끼워 넣는다(1). C 형식 블록 주석은 저작권·MIT/X 라이선스·해빙 열역학(ice thermodynamics) 성장/감소 항과 현재 Mellor-Kantha (1989)만 선택 가능하다는 설명을 포함한다(2–15). 원문 조건·대입식·전처리 지시: `#include "cppdefs.h"` (1). |
| 16–24 | `ICE_MODEL && ICE_THERMO` 참 분기(16)의 `ICE_MK` 조건(17)은 `ice_mk.h`를 끼워 넣는다(18). 포함 파일 이름은 ice_mk.h이다. 바깥 조건의 `#else`는 내용 없는 `ice_thermo_mod`를 정의한다(20–22). 전처리 조건 종료와 마지막 빈 줄을 포함한다(23–24). 원문 조건·대입식·전처리 지시: `#if defined ICE_MODEL && defined ICE_THERMO` (16) `# ifdef ICE_MK` (17) `#  include <ice_mk.h>` (18) `# endif` (19) `#else` (20) `#endif` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–23: ICE_MODEL 및 ICE_THERMO가 정의되고 ICE_MK가 정의되지 않은 조합에는 포함 파일이나 빈 모듈 본문을 내보내는 분기가 없다. 빈 모듈은 바깥 조건의 ELSE에만 있다.
