---
file: models/ROMS/raw/source_code/roms/ROMS/Adjoint/ad_step2d.F
lines: 24
sha256: 282100154d1887665b955d2a4b5891e6c5e19d810773322843b9420d14c166ef
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ad_step2d.F — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#include "cppdefs.h"` (1)로 cppdefs.h를 포함한다. `#ifdef ADJOINT` (2) 안에서 저작권·MIT/X 라이선스 주석(4–9)을 적는다. 자유수면과 2차원 운동량의 수반(adjoint) 방정식에 빠른 예측자(predictor) 또는 보정자(corrector) 시간 단계를 수행한다는 주석(11–12). |
| 13–20 | 시작 시 2행 `#ifdef ADJOINT` 안. `# ifdef SOLVE3D` (13)·`# endif` (16) 사이에 3차원 적용에서 고주파 신호를 감쇠하기 위해 모든 빠른 시간 단계의 시간 필터링(time filtering) 변수를 계산한다는 주석(14–15)을 둔다. 구분 주석(17–19), `# include "ad_step2d_LF_AM3.h"` (20)로 ad_step2d_LF_AM3.h를 포함한다. 이 파일에는 포함 파일의 루틴 본문이 직접 적혀 있지 않다. |
| 21–24 | 시작 시 2행 `#ifdef ADJOINT`의 참 분기 끝. `#else` (21)는 ADJOINT가 정의되지 않은 분기이다. 빈 ad_step2d_mod 모듈을 선언·종료한다(22–23). `#endif` (24)로 2행 조건을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20: 포함 파일 이름은 ad_step2d_LF_AM3.h이다. 지정된 다른 판독 대상 ad_step2d_FB.h를 포함하는 행은 이 파일에 없다.
