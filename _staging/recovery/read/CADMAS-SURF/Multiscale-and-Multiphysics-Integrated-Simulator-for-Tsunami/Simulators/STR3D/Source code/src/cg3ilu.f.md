---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cg3ilu.f
lines: 49
sha256: 2690022a74a5302200175dd8e1b8249f0171607467cdbbece2f41385cd41a898
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg3ilu.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | CG3ILU의 배열과 암시적 형(implicit typing)을 선언한다. 불완전 분해(incomplete decomposition) 계수 DFAC의 DATA 값은 1.5D0이다. NEQ가 0이면 반환한다. 첫 대각 역수를 D(1)에 둔다. 14행은 주석 처리된 코드다. 원문: `      SUBROUTINE CG3ILU( D,A,NEQ  ,IDSK,IDCG`<br>`     1                 ,ISTOH ,ITO)` (1–2); 주석 원문 `C              SUB FOR INCOMPLETE DECOMPOSITION ` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION  A(ISTOH),IDSK(NEQ+1),IDCG(*)` (8); `      DIMENSION  D(NEQ)` (9); `      DATA DFAC /1.5D0/` (10); `      IF(NEQ.EQ.0) RETURN` (12); 주석 원문 `C     DFACO=DFAC` (14); `      D(1)=1.0D0/A(1)` (15). |
| 17–29 | 시작 시 1행 CG3ILU 루틴 안. I 루프에서 대각값에 DFAC를 곱한 C를 만들고 저장된 하위 항의 제곱과 D의 곱을 뺀다. 원문: `   40 DO 20 I=2,NEQ` (17); `        IP=IDSK(I)` (18); `        IS=IP+1` (19); `        IE=IDSK(I+1)-1` (20); `        C=DFAC*A(IP)` (21); `        IF(IS.LE.IE) THEN` (23); `          DO 10 J=IS,IE` (24); `            JP=IDCG(J)` (25); `            C=C-A(J)*A(J)*D(JP)` (26); `   10     CONTINUE` (27); `        END IF` (28). |
| 30–49 | 시작 시 17행 `   40 DO 20 I=2,NEQ` 안이다. 이 루프는 42행 `   20 CONTINUE`에서 닫힌다. 39행 `GO TO 40`의 대상은 17행이다. C가 1.0D-37보다 작으면 DFAC를 0.1씩 늘린다. DFAC가 5를 넘으면 실패 메시지를 출력하고 ERRSTP(22,ITO)를 호출한다. 40번 표지로 돌아가 I 루프를 다시 시작한다. 정상 경로에서는 D(I)에 C의 역수를 둔다. 31–32·35·44–47행은 주석 처리된 코드다. 반환문과 루틴 끝을 포함한다. 원문: `   30   IF(C.LT.1.0D-37) THEN` (30); 주석 원문 `C         WRITE(ITO,'(/6X,A,I8,E15.7)') 'NEGATIVE IN CG3ILU --- I,D='` (31); 주석 원문 `C    &                                  ,I,1.0D0/C` (32); `          DFAC=DFAC+1.0D-1` (33); `          IF(DFAC.GT.5.0D0) THEN` (34); 주석 원문 `C           WRITE(ITO,*) 'DFAC TOO LARGE, PROGRAM STOPPED!'` (35); `            WRITE(ITO,*) 'CG METHOD FAILED.'` (36); `            CALL ERRSTP(22,ITO)` (37); `          END IF` (38); `          GO TO 40` (39); `        END IF             ` (40); `        D(I)=1.0D0/C` (41); `   20 CONTINUE` (42); 주석 원문 `C     IF(DFAC .NE. DFACO) THEN` (44); 주석 원문 `C       WRITE(ITO,100) DFACO,DFAC` (45); 주석 원문 `C 100   FORMAT(/6X,'DFAC CHANGED : ',F7.3,'  ---> ',F7.3/)` (46); 주석 원문 `C     END IF` (47); `      RETURN` (48); `      END` (49). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10·33·39: DATA로 초기화한 DFAC를 증가시키는 문장이 있다. 40번으로 재시작할 때 DFAC를 1.5D0으로 되돌리는 문장은 없다.
- 15·17·39: D(1)의 역수 계산은 재시작 표지 40보다 앞에 있다.
