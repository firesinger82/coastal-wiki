---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/mod_julian.f90
lines: 112
sha256: c86bb9905058555c621b36803860fecb014184f5395d1f08ab63af56184bb592
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_julian.f90 — 판독 구간 기록

구간은 1행부터 112행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | EFDC+·GPLv2 머리말(1–8). JULIANMOD·작성자·날짜·GLOBAL 사용과 implicit none(9–14). 기준 일·월·연·시·분·초의 private 정수 DA0/MN0/YR0/HH0/MM0/SS0와 real(8) HR0를 선언한다(15–22). contains와 빈 줄(23–25). |
| 26–47 | JULIDAY는 달력 날짜를 율리우스 일(Julian day)로 바꾸는 함수이다(26–28). 전환 기준 원문은 `parameter (IGREG = 15+31*(10+12*1582))` (29). JY에 IYYY 복사(31). 단일행 조건은 `if( JY == 0) STOP 'JULDAY: THERE IS NO YEAR ZERO'` (32), `if( JY < 0) JY = JY+1` (33). `if( MM > 2 )then` (34)은 `JM = MM+1` (35), `else` (36)는 `JY = JY-1` (37), `JM = MM+13` (38). 조건 밖에서 `JULDAY = 365*JY+INT(0.25D0*JY+2000D0)+INT(30.6001D0*JM)+ID+1718995` (40). `if( ID+31*(MM+12*IYYY).GE.IGREG )then` (41)은 `JA = INT(0.01D0*JY)` (42), `JULDAY = JULDAY+2-JA+INT(0.25D0*JA)` (43). return·종료·빈 줄(44–47). |
| 48–74 | CALDAT 입구·정수 선언·`parameter (IGREG = 2299161)` (48–52). `if( JULIAN.GE.IGREG )then` (53)은 `JALPHA = INT(((JULIAN-1867216)-0.25D0)/36524.25D0)` (54), `JA = JULIAN+1+JALPHA-INT(0.25D0*JALPHA)` (55). `elseif( JULIAN < 0 )then` (56)은 `JA = JULIAN+36525*(1-JULIAN/36525)` (57). `else` (58)는 JA에 JULIAN 복사(59). 이후 `JB = JA+1524` (61), `JC = INT(6680.0D0+((JB-2439870)-122.1D0)/365.25D0)` (62), `JD = 365*JC+INT(0.25D0*JC)` (63), `JE = INT((JB-JD)/30.6001D0)` (64), `ID = JB-JD-INT(30.6001D0*JE)` (65), `MM = JE-1` (66). 원문은 `if( MM > 12 )MM = MM-12` (67), `IYYY = JC-4715` (68), `if( MM > 2 )IYYY = IYYY-1` (69), `if( IYYY <= 0)IYYY = IYYY-1` (70), `if( JULIAN < 0 ) IYYY = IYYY-100*(1-JULIAN/36525)` (71). return·종료·빈 줄(72–74). |
| 75–92 | DATEPRO 입구, 입력 문자열 STR·LEN_TRIM(STR) 길이 SS·출력 DD/MN/YR·정수 M/NL 선언(75–80). SS에 STR 복사(82), `NL = LEN_TRIM(SS)` (83). `do M = 1,NL` (84)의 `if( SS(M:M) == '-' .or. SS(M:M) == ':' .or. SS(M:M) == '/' )then` (85)은 해당 문자에 ''을 대입한다(86). 조건·루프 종료 뒤 `read(SS,*) YR,MN,DD` (89). 루틴 종료·빈 줄(90–92). |
| 93–112 | TOGREGOR는 입력 DAYTIME과 출력 SDATETIME·지역 정수를 선언한다(93–97). `call DATEPRO(BASETIME,HH0,MM0,SS0)` (99), `call DATEPRO(BASEDATE,YR0,MN0,DA0)` (100). `HR0 = HH0+MM0/60._8+SS0/3600._8` (102), `JD0 = JULIDAY(MN0,DA0,YR0)` (103), `JULIAN = IDINT(DAYTIME+JD0)` (105), `call CALDAT(JULIAN,MN,DD,YR)` (106). SDATETIME에 `(I4,I2.2,I2.2)` 형식으로 연·월·일을 쓴다(108). 빈 줄·루틴·모듈 종료(109–112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·99–105: HR0는 기준 시·분·초로 계산되지만 이후 JULIAN 대입식과 다른 실행식에서 사용되지 않는다.
- 85–89: DATEPRO는 '-', ':', '/' 문자를 ''으로 대체한 뒤 세 정수를 내부 read로 읽는다. 이 read에는 iostat·err·end 인수가 없다.
