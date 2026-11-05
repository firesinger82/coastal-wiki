---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/scalus.f
lines: 32
sha256: 5760fcef3c785a531d3d2c18e81a21f4c946cbe32c8f09652b04c69b7158fc38
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# scalus.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | SCALUS 입구와 모듈·배열 선언이다(1–6). `IS=IDSK(I)`(9)가 가리키는 A(IS)의 역제곱근으로 P(I)를 만든다(10). 해석: A(IS)를 대각 성분으로 보면 대각 스케일링 인수이다. 다중 프로세스 조건에서 COMM_CG2·조건부 COMM_CG2X를 호출한다(13–16). A(J)에는 P(I)*P(K)를 곱한다(23). B(I)에는 P(I)를 곱한다(28). 해석: A를 희소행렬, B를 우변으로 보는 설명은 저장 구조에 따른 해석이다. 원문: `      SUBROUTINE SCALUS(NEQ,P,A,B,IDSK,IDCG,INDOF,INDOP,IMPC)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION IDSK(NEQ+1),P(*),A(*),IDCG(*),B(NEQ),INDOF(6,*),INDOP(*)` (6); `      DO 200 I=1,NEQ` (8); `        IS=IDSK(I)` (9); `        P(I)=1.D0/DSQRT(A(IS))` (10); `  200 CONTINUE` (11); `      IF( NPROCS > 1 ) THEN` (13); `        CALL COMM_CG2(P,INDOF,INDOP)` (14); `        IF( IMPC > 0 ) CALL COMM_CG2X(P,INDOF,INDOP)` (15); `      ENDIF` (16); `      DO 100 I=1,NEQ` (18); `        IS=IDSK(I)` (19); `        IE=IDSK(I+1)-1` (20); `        DO 120 J=IS,IE` (21); `          K=IDCG(J)` (22); `          A(J)=A(J)*P(I)*P(K)` (23); `  120   CONTINUE` (24); `  100 CONTINUE` (25); `      DO 300 I=1,NEQ` (27); `        B(I)=B(I)*P(I)` (28); `  300 CONTINUE` (29); `      RETURN` (31); `      END` (32) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–10: P는 A(IS)의 제곱근으로 나누어 계산한다. 이 루프에는 A(IS)의 양수 여부를 검사하는 문장이 없다.
