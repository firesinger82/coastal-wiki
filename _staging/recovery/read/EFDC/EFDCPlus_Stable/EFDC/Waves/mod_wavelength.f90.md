---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Waves/mod_wavelength.f90
lines: 95
sha256: c434d151b612606b948c46aed1213b88a431a6ec423cf4e69da693c634633440
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_wavelength.f90 — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | EFDC+·GPLv2 머리말(1–8). WAVELENGTH·작성자·GLOBAL의 RKD·implicit none(9–13). 원문 상수는 `real(RKD),PRIVATE,parameter :: G = 9.81` (15), `real(RKD),PRIVATE,parameter :: PI = 3.14159265358979` (16). contains·빈 줄(18–19). |
| 20–30 | DISRELATION은 분산관계(dispersion relation) 잔차 FWL을 반환한다(20–21). 주석 단위는 RLS 파장 m·TP 주기 s·HD 수심 m·U 수심 평균 속도 m/s·PHI 파랑과 흐름 각도 rad이다(22–26). REAL(RKD) 선언(27). 원문은 `FWL = (RLS/TP-U*COS(PHI))-SQRT(G*RLS/2._8/PI*TANH(2._8*PI*HD/RLS))` (28). 함수 종료·빈 줄(29–30). |
| 31–64 | 재귀(recursive) 이분법 BISEC 인수·외부 FUN·지역 선언(31–36). A/B에 A0/B0 복사·IST=1(37–39), `FA = FUN(A,TP,HD,U,PHI)` (40), `FB = FUN(B,TP,HD,U,PHI)` (41). `if( FA*FB < 0 )then` (42)은 `X = 0.5*(A+B)` (43), `FX = FUN(X,TP,HD,U,PHI)` (44). 내부 `if( FA*FX < 0 )then` (45)은 B=X(46), `else` (47)는 A=X(48). `if( ABS(A-B) <= TOL )then` (50)은 return(51), `else` (52)는 `call BISEC(FUN,A,B,TOL,TP,HD,U,PHI,X)` (53). 바깥 `elseif( FA == 0 )then` (55)은 X=A(56), `elseif( FB == 0 )then` (57)은 X=B(58). `else` (59)는 `IST = -1` (60)과 `call STOPP('DISPERSION RELATION: FA.FB>0')` (60–61). 조건·루틴 종료·빈 줄(62–64). |
| 65–95 | RTBIS 인수·외부 FUNC·정수/실수 선언(65–69), `parameter (JMAX = 40)` (70). `FMID = FUNC(X2,TP,HD,U,PHI)` (72), `F = FUNC(X1,TP,HD,U,PHI)` (73), `if( F*FMID >= 0.) PAUSE 'ROOT MUST BE BRACKETED IN RTBIS'` (74). `if( F<0. )then` (75)은 RTBIS=X1(76), `DX = X2-X1` (77). `else` (78)는 RTBIS=X2(79), `DX = X1-X2` (80). J=1:JMAX 루프(82)에서 `DX = DX*.5` (83), `XMID = RTBIS+DX` (84), `FMID = FUNC(XMID,TP,HD,U,PHI)` (85), `if( FMID <= 0.)RTBIS = XMID` (86), `if( ABS(DX)<XACC .or. FMID == 0. ) return` (87). 루프 후 `PAUSE 'TOO MANY BISECTIONS IN RTBIS'` (89). 함수·모듈 종료와 끝 빈 줄(90–95). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35·39·60: BISEC의 IST는 1·-1을 대입하지만 이후 읽거나 반환하지 않는다.
- 31–63·70·82–89: BISEC에는 재귀 횟수 제한이 없다. RTBIS는 JMAX=40으로 반복 횟수를 고정한다.
- 42·55–58·74: BISEC은 끝점의 함수값 0을 별도 분기로 반환한다. RTBIS의 초기 PAUSE 조건에는 F*FMID==0도 포함한다.
