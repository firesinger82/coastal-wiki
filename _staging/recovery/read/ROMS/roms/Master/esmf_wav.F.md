---
file: models/ROMS/raw/source_code/roms/Master/esmf_wav.F
lines: 40
sha256: 0949effb26e44456a1318a0f17f036bfbedb79977a598de8a5659fc709b04c50
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# esmf_wav.F — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)는 cppdefs.h를 끼워 넣는다. `#if defined MODEL_COUPLING && defined ESMF_LIB` (2)에서 모델 결합(model coupling)과 ESMF 라이브러리 사용을 함께 요구한다. 저작권·MIT/X 라이선스·파랑 모델 그리드 컴포넌트(gridded component) 설명 및 ESMF 7 이상과 NUOPC 이름·주소를 적는다(3–21). 빈 줄(22). |
| 23–32 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB` 안. `# if defined WAV_COUPLING` (23)에서 파랑 결합을 선택한다. `#  if defined REFDIF_COUPLING_NOT_YET` (24), `#   include "esmf_wav_refdif.h"` (25), `#  elif defined SWAN_COUPLING_NOT_YET` (26), `#   include "esmf_wav_swan.h"` (27), `#  elif defined WAM_COUPLING` (28), `#   include "esmf_wav_wam.h"` (29), `#  else` (30), `#   include "esmf_wav_void.h"` (31), `#  endif` (32). 조건에 따라 esmf_wav_refdif.h·esmf_wav_swan.h·esmf_wav_wam.h·esmf_wav_void.h 중 하나를 끼워 넣는다. 포함 파일 내부는 이 파일의 판독 범위에 속하지 않는다. |
| 33–40 | 시작 시 2행 `#if defined MODEL_COUPLING && defined ESMF_LIB`·23행 `# if defined WAV_COUPLING` 안이며, 24행 조건은 종료된 상태. `# else` (33)는 23행 조건의 불성립 분기이다. 빈 esmf_wav_mod 모듈을 선언·종료한다(34–35). `# endif` (36)는 23행 조건을 닫는다. `#else` (37)는 2행 조건의 불성립 분기이다. 여기서도 빈 esmf_wav_mod 모듈을 선언·종료한다(38–39). `#endif` (40)는 2행 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–31: REFDIF와 SWAN 선택 매크로 이름에는 `_NOT_YET`가 들어 있다. 이 선택 연쇄에서 어느 조건도 성립하지 않으면 esmf_wav_void.h를 포함한다.
- 33–40: WAV_COUPLING 불성립 분기와 MODEL_COUPLING·ESMF_LIB 결합 조건 불성립 분기는 모두 본체 없는 esmf_wav_mod를 만든다.
