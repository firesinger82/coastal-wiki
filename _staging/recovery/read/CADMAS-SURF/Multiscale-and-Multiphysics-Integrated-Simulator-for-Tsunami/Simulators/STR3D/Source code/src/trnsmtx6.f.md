---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/trnsmtx6.f
lines: 32
sha256: d52711cb95f6a877d98084fe64538379ac6952254d601fbbc73b904eb27f91ef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# trnsmtx6.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | TRNSMTX6 입구와 배열 선언이다(1–4). ICRD==1이면 E의 아홉 성분을 EG로 복사한다(6–8). ICRD==2이면 기준점에 대한 P의 평면 성분 OP1·OP2를 구한다(10–16). R이 1.D-20 미만이면 ITO에 FORMAT 500의 오류 메시지와 P를 쓴다(17–20). 이어서 ERRSTP(13,ITO)를 호출한다(21). 메시지는 하중점이 원통 좌표계의 Z축 위에 있음을 뜻한다(19–20). RMULT5·DIRCOS·CROSS·SHIFT1으로 원통 좌표계(cylindrical coordinate system)의 기저를 만든다(24–27). 원문: `      SUBROUTINE TRNSMTX6(EG,ICRD,P,E,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION OP(3),P(3),E(3,4),EG(3,3)` (4); 주석: `C----&------------------------------------------------------------------` (5); `      IF( ICRD .EQ. 1 ) THEN` (6); `        CALL SHIFT1(EG,E,9)` (8); `      ELSEIF( ICRD .EQ. 2 ) THEN` (10); `        CALL SUBVEC(OP,P,E(1,4),3)` (12); `        CALL VECML1(OP1,OP,E(1,1),3)` (13); `        CALL VECML1(OP2,OP,E(1,2),3)` (14); `        R=OP1*OP1+OP2*OP2` (16); `        IF( R .LT. 1.D-20 ) THEN` (17); `          WRITE(ITO,500) P` (18); `  500     FORMAT('LOAD POINT IS ON Z-AXIS OF CYLINDRICAL COODINATE'`<br>`     &          ,' SYSTEM.'/'X =',1PE12.4,3X,'Y =',E12.4,3X,'Z =',E12.4)` (19–20); `          CALL ERRSTP(13,ITO)` (21); `        ENDIF` (22); `        CALL RMULT5(EG(1,1),OP1,E(1,1),OP2,E(1,2),3)` (24); `        CALL DIRCOS(EG(1,1),EG(1,1),3)` (25); `        CALL CROSS(E(1,3),EG(1,1),EG(1,2))` (26); `        CALL SHIFT1(EG(1,3),E(1,3),3)` (27); `      ENDIF` (29); `      RETURN` (31); `      END` (32) 해석: R을 제곱 반경으로 보는 설명은 OP1·OP2의 제곱합과 오류 메시지에 따른 해석이다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–29: ICRD가 1 또는 2인 경우만 처리한다. 그 밖의 값에서는 EG를 설정하는 ELSE가 없다.
