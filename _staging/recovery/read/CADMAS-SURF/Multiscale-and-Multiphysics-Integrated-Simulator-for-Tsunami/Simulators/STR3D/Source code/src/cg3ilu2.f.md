---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cg3ilu2.f
lines: 71
sha256: 4f2f0555fe23b4246873d68a312fc936f81cfd9324ceef12c2ac2e0b7d259dfb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg3ilu2.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | CG3ILU2의 배열과 암시적 형(implicit typing)을 선언하고 DFAC를 DATA 값 1.5D0으로 초기화한다. 불완전 분해(incomplete decomposition) 전처리에서 음수 대각을 가진 행은 B와 해당 A 행 전체의 부호를 바꾼다. 이후 첫 대각 역수를 구한다. 24행은 주석 처리된 코드다. 원문: `      SUBROUTINE CG3ILU2( D,A,B ,NEQ  ,IDSK,IDCG`<br>`     1                 ,ITO)` (1–2); 주석 원문 `C              SUB FOR INCOMPLETE DECOMPOSITION ` (4); 주석 원문 `C                 ( BLOCKED NONSYMETRIC-SKYLINE MATRIX)` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION  A(*),IDSK(NEQ+1),IDCG(*)` (9); `      DIMENSION  D(NEQ),B(NEQ)` (10); `      DATA DFAC /1.5D0/` (11); `      DO 60 I=1,NEQ` (13); `        IS=IDSK(I)` (14); `        IF(A(IS).LT.0.D0) THEN` (15); `          B(I)=-B(I)` (16); `          IE=IDSK(I+1)-1` (17); `          DO 70 J=IS,IE` (18); `            A(J)=-A(J)` (19); `   70     CONTINUE` (20); `        ENDIF` (21); `   60 CONTINUE` (22); 주석 원문 `C      DFACO=DFAC` (24); `      D(1)=1.0D0/A(1)` (25). |
| 27–50 | 시작 시 1행 CG3ILU2 루틴 안. I 루프에서 DFAC를 곱한 대각 C를 만들고, JP 행에서 현재 I열을 찾아 대응하는 A 두 값과 D의 곱을 뺀다. `IF(JP.GT.I) GO TO 30`은 51행 레이블 30으로 이동한다. 41·44행의 `GOTO 10`은 48행 `   10     CONTINUE`로 이동한다. I 루프는 64행 레이블 20에서 닫힌다. 원문: `   40 DO 20 I=2,NEQ` (27); `        IP=IDSK(I)` (28); `        IS=IP+1` (29); `        IE=IDSK(I+1)-1` (30); `        C=DFAC*A(IP)` (31); `        IF(IS.LE.IE) THEN` (33); `          DO 10 J=IS,IE` (34); `            JP=IDCG(J)` (35); `            IF(JP.GT.I) GO TO 30` (36); `            IS2=IDSK(JP)+1` (37); `            IE2=IDSK(JP+1)-1` (38); `            IF(IS2.LE.IE2) THEN` (39); `              DO 50 K=IS2,IE2` (40); `                IF(IDCG(K).GT.I) GOTO 10` (41); `                IF(IDCG(K).EQ.I) THEN` (42); `                  C=C-A(J)*A(K)*D(JP)` (43); `                  GOTO 10` (44); `                ENDIF` (45); `   50         CONTINUE` (46); `            ENDIF` (47); `   10     CONTINUE` (48); `        END IF` (49). [11-04 전수 검증 보완] |
| 51–71 | 시작 시 27행 `   40 DO 20 I=2,NEQ` 안이다. 이 루프는 64행 `   20 CONTINUE`에서 닫힌다. 61행 `GO TO 40`의 대상은 27행이다. 작은 C를 만나면 DFAC를 0.1씩 늘리고, 5를 넘으면 실패 메시지와 ERRSTP 호출을 수행한다. 40번으로 분해 루프를 재시작한다. 정상 경로에서는 C의 역수를 D에 둔다. 52–53·56–57·66–69행은 주석 처리된 코드다. 반환문과 루틴 끝을 포함한다. 원문: `   30   IF(C.LT.1.0D-37) THEN` (51); 주석 원문 `C          WRITE(ITO,'(/6X,A,I8,E15.7)') 'NEGATIVE IN CG3ILU --- I,D='` (52); 주석 원문 `C     &                                  ,I,1.0D0/C` (53); `          DFAC=DFAC+1.0D-1` (54); `          IF(DFAC.GT.5.0D0) THEN` (55); 주석 원문 `C            WRITE(ITO,*) 'DFAC TOO LARGE! PROGRAM STOP'` (56); 주석 원문 `C            STOP` (57); `            WRITE(ITO,*) 'CG METHOD FAILED.'` (58); `            CALL ERRSTP(22,ITO)` (59); `          END IF` (60); `          GO TO 40` (61); `        END IF             ` (62); `        D(I)=1.0D0/C` (63); `   20 CONTINUE` (64); 주석 원문 `C      IF(DFAC .NE. DFACO) THEN` (66); 주석 원문 `C        WRITE(ITO,100) DFACO,DFAC` (67); 주석 원문 `C  100   FORMAT(/6X,'DFAC CHANGED : ',F7.3,'  ---> ',F7.3/)` (68); 주석 원문 `C      END IF` (69); `      RETURN` (70); `      END` (71). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–25: NEQ가 0인 경우를 검사하는 실행문 없이 D(1)=1.0D0/A(1)을 실행한다.
- 11·54·61: DATA로 초기화한 DFAC를 증가시키며 재시작 시 초기값 복원문은 없다.
- 25·27·61: D(1)의 역수 계산은 재시작 표지 40보다 앞에 있다.
