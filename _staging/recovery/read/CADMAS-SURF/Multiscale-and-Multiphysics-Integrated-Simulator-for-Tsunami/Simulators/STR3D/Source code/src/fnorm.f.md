---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/fnorm.f
lines: 30
sha256: a8bfb2c63938740cc6d4a3a333e6cbbcc641390f02c54cbae8e1174603b4ddfa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fnorm.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | FNORM의 인수와 배열을 선언한다. KK(26)에서 NNOD를 받고 CLEAR1로 FNRM을 초기화한다. INDOF의 양수 첨자에 대해 앞의 세 성분과 뒤의 세 성분 FT 제곱합을 따로 누적한다. 원문: `      SUBROUTINE FNORM(FNRM,KK,INDOF,INDOP,FT,ISLV)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION FNRM(3),KK(*),INDOF(6,*),INDOP(*),FT(*)` (4)； `      NNOD=KK(26)` (6)； `      CALL CLEAR1(FNRM,3)` (7)； `      DO 300 I=1,NNOD` (8)； `        DO 310 J=1,3` (9)； `          IFR=INDOF(J,I)` (10)； `          IF(IFR .GT. 0) FNRM(1)=FNRM(1)+FT(IFR)*FT(IFR)` (11)； `  310   CONTINUE` (12)； `        DO 320 J=4,6` (13)； `          IFR=INDOF(J,I)` (14)； `          IF(IFR .GT. 0) FNRM(2)=FNRM(2)+FT(IFR)*FT(IFR)` (15)； `  320   CONTINUE` (16)； `  300 CONTINUE` (17)。 |
| 18–30 | 시작 시 1행 FNORM 루틴 안이다. ISLV > 10이면 INDOP 양수 첨자의 제곱합을 세 번째 값에 누적한다. 각 값이 양수일 때 제곱근을 취하여 노름(norm)을 반환한다. 원문: `      IF( ISLV > 10 ) THEN` (18)； `        DO 400 I=1,NNOD` (19)； `          IFR=INDOP(I)` (20)； `          IF(IFR .GT. 0) FNRM(3)=FNRM(3)+FT(IFR)*FT(IFR)` (21)； `  400   CONTINUE` (22)； `      ENDIF` (23)； `      IF(FNRM(1) .GT. 0.) FNRM(1)=DSQRT( FNRM(1) )` (25)； `      IF(FNRM(2) .GT. 0.) FNRM(2)=DSQRT( FNRM(2) )` (26)； `      IF(FNRM(3) .GT. 0.) FNRM(3)=DSQRT( FNRM(3) )` (27)； `      RETURN` (29)； `      END` (30)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–23: INDOP를 사용하는 세 번째 노름 누적은 ISLV > 10일 때만 실행한다.
