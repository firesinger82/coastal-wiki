---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/fprobdep.f90
lines: 55
sha256: f8d5c71b6651a6de6bcb5a1e5606f511061b652a1edf6c0ccd4de0cc61373bb8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# fprobdep.f90 — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | EFDC+·저작권·GPLv2 머리말(1–8). FPROBDEP(TAUDDD,TAUBBB) 입구(9). 확률적분(probability integral)으로 퇴적(deposition) 확률을 계산한다는 주석(13–14). EFDC-FULL 1.0a 및 2001년 Hamrick 수정 이력을 적는다(16–18). implicit none·부호 플래그 INEG·실수 작업변수를 선언한다(30–34). TAUDDD·TAUBBB는 intent(IN)이다(34). 빈 줄을 포함한다(35–36). |
| 37–50 | 시작 시 9행 FPROBDEP 안. 주석은 TAUBBB>TAUDDD를 가정한다고 적는다(37). 응력비·EXP·LOG로 YVAL을 계산한다(38). INEG=0에서 시작하고 YVAL<0이면 INEG=1·ABS(YVAL)을 설정한다(39–43). XVAL 유리식(rational expression), POLYX 다항식(polynomial), EXPY·FUNY·TMPVAL을 순서대로 계산한다(44–48). INEG=1이면 확률의 보수를 취하고 반환값에도 1.-TMPVAL을 적용한다(49–50). 조건·계산·호출 원문: `YVAL = 2.04*LOG(0.25*((TAUBBB/TAUDDD)-1.)*EXP(1.27*TAUDDD))` (38); `if( YVAL < 0.0 )then` (40); `INEG = 1` (41); `YVAL = ABS(YVAL)` (42); `XVAL = 1.0/(1.0+0.3327*YVAL)` (44); `POLYX = XVAL*(0.4632-0.1202*XVAL+0.9373*XVAL*XVAL)` (45); `EXPY = -0.5*YVAL*YVAL` (46); `FUNY = 0.3989*EXP(EXPY)` (47); `TMPVAL = 1.0-FUNY*POLYX` (48); `if( INEG == 1 ) TMPVAL = 1.0-TMPVAL` (49); `FPROBDEP = 1.0-TMPVAL` (50). |
| 51–55 | 시작 시 9행 FPROBDEP 안. 빈 줄과 계수 주석을 포함한다(51–54). 주석은 0.3989=1/SQRT(2*PI)라고 적는다(53). END FUNCTION으로 끝난다(55). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 37–38: TAUBBB>TAUDDD 가정은 주석에만 있다. 실행문에는 이 조건이나 TAUDDD=0 검사가 없다.
- 44–50: 반환값에는 별도의 0..1 범위 제한문이 없다. 0.3327·0.4632·0.1202·0.9373·0.3989는 실행식의 고정 계수이다.
