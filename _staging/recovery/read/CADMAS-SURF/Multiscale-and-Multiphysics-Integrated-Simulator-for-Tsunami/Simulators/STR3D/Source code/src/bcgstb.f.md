---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/bcgstb.f
lines: 73
sha256: 95aafc00b27d70f518b2bf517a23c9d077a5eff8822a29a0bde6178f6c4f4b68
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bcgstb.f — 판독 구간 기록

구간은 1행부터 73행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | BCGSTB의 연속 인수·MPI 모듈·암시적 형·배열 선언. 최대 반복 수 입력이 0이면 CG_MPI_ALLREDUCE_I 결과의 절반을 쓰며 최소 50으로 제한한다. SCALUS로 스케일링하고 BNRM이 0이면 CLEAR1(X,NEQ)를 호출한 뒤 반환한다. X의 선언 길이는 NEQEXT이지만 이 호출의 개수 인수는 NEQ다. 제곱 허용오차를 계산하고 CG3ILU2와 작업 벡터를 준비한다. 원문: 연속문(1–2): `      SUBROUTINE BCGSTB(A,B,X,WK,NEQ,NEQEXT,IDSK,IDCG,INDOF,INDOP,MXITCG` <br> `     &                 ,CGTOL,IMPC,ITO)`; `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); 연속문(8–9): `      DIMENSION A(*),B(NEQ),X(NEQEXT),WK(NEQEXT,9),IDSK(NEQ+1),IDCG(*)` <br> `     *         ,INDOF(6,*),INDOP(*)`; `      MAXITR=MXITCG` (11); `      IF(MAXITR.EQ.0) THEN` (12); `        CALL CG_MPI_ALLREDUCE_I(NEQ,MAXITR,1,0)` (13); `        MAXITR=MAXITR/2` (14); `        IF(MAXITR.LT.50) MAXITR=50` (15); `      ENDIF` (16); `      CALL SCALUS(NEQ,WK(1,9),A,B,IDSK,IDCG,INDOF,INDOP,IMPC)` (18); `      CALL DTPRDCT(BNRM,B,B,NEQ)` (19); `      IF(BNRM.EQ.0.D0) THEN` (20); `        CALL CLEAR1(X,NEQ)` (21); `        RETURN` (22); `      ENDIF` (23); `      TOL=CGTOL*CGTOL*BNRM` (24); `      CALL CG3ILU2(WK(1,7),A,B,NEQ,IDSK,IDCG,ITO)` (25); `      CALL SHIFT1(WK(1,1),B,NEQ)` (26); `      CALL SHIFT1(WK(1,2),WK(1,1),NEQ)` (27); `      CALL SHIFT1(WK(1,3),WK(1,1),NEQ)` (28); `      CALL DTPRDCT(C1,WK(1,1),WK(1,2),NEQ)` (29); `      CALL CLEAR1(X,NEQ)` (30). [11-04 전수 검증 정정] |
| 32–61 | BCGSTB 루틴 안. ITER=1:MAXITR에서 CG3FWB2·CG3ML3·DTPRDCT와 벡터 연산으로 안정화 쌍대공액기울기법(BiCGSTAB)의 ALP·C3·BETA를 계산하고 해·잔차·탐색 벡터를 갱신한다. RES<TOL이거나 마지막 반복에서 RES<TOL*1.D3이면 200번으로 이동한다. 원문: `      DO 100 ITER=1,MAXITR` (32); `        CALL SHIFT1(WK(1,8),WK(1,3),NEQ)` (33); `        CALL CG3FWB2(WK(1,7),A,WK(1,8),NEQ,IDSK,IDCG,ITO)` (34); 연속문(35–36): `        CALL CG3ML3(WK(1,6),A,WK(1,8),NEQ,IDSK,IDCG,INDOF,INDOP,IMPC` <br> `     &             ,ITO)`; `        CALL DTPRDCT(C2,WK(1,1),WK(1,6),NEQ)` (37); `        ALP=C1/C2` (38); `        CALL RMULT4(WK(1,4),WK(1,2),-ALP,WK(1,6),NEQ)` (39); `        CALL SHIFT1(WK(1,8),WK(1,4),NEQ)` (40); `        CALL CG3FWB2(WK(1,7),A,WK(1,8),NEQ,IDSK,IDCG,ITO)` (41); 연속문(42–43): `        CALL CG3ML3(WK(1,5),A,WK(1,8),NEQ,IDSK,IDCG,INDOF,INDOP,IMPC` <br> `     &             ,ITO)`; `        CALL DTPRDCT(C31,WK(1,4),WK(1,5),NEQ)` (44); `        CALL DTPRDCT(C32,WK(1,5),WK(1,5),NEQ)` (45); `        C3=C31/C32` (46); `        CALL RMULT5(WK(1,8),ALP,WK(1,3),C3,WK(1,4),NEQ)` (47); `        CALL CG3FWB2(WK(1,7),A,WK(1,8),NEQ,IDSK,IDCG,ITO)` (48); `        CALL ADDVEC(X,X,WK(1,8),NEQ)` (49); `        CALL RMULT4(WK(1,2),WK(1,4),-C3,WK(1,5),NEQ)` (50); `        CALL DTPRDCT(RES,WK(1,2),WK(1,2),NEQ)` (52); 연속문(54–55): `        IF( RES < TOL .OR. ( ITER == MAXITR .AND. RES < TOL*1.D3 ) )` <br> `     &    GOTO 200`; `        CALL DTPRDCT(C1,WK(1,1),WK(1,2),NEQ)` (57); `        BETA=C1/(C2*C3)` (58); `        CALL RMULT4(WK(1,8),WK(1,3),-C3,WK(1,6),NEQ)` (59); `        CALL RMULT4(WK(1,3),WK(1,2),BETA,WK(1,8),NEQ)` (60); `  100 CONTINUE` (61). |
| 62–73 | BCGSTB 루틴 안. GOTO 200을 실행하지 않고 반복을 마치면 63행 WRITE가 비수렴 메시지를 출력한다. 그 뒤 ERRSTP(21,ITO)를 호출한다. 200번에서 VECML3으로 스케일을 복원한다. NPROCS>1이면 COMM_CG2, 그 안에서 IMPC>0이면 COMM_CG2X를 호출한다. 원문: `      WRITE(ITO,*) 'NOT CONVERGED BY CG METHOD.'` (63); `      CALL ERRSTP(21,ITO)` (64); `  200 CALL VECML3(X,WK(1,9),X,NEQ)` (66); `      IF( NPROCS > 1 ) THEN` (68); `        CALL COMM_CG2(X,INDOF,INDOP)` (69); `        IF( IMPC > 0 ) CALL COMM_CG2X(X,INDOF,INDOP)` (70); `      ENDIF` (71); `      END        ` (73). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38·46·58: ALP=C1/C2, C3=C31/C32, BETA=C1/(C2*C3)를 계산한다. 해당 나눗셈 직전에 분모 0 검사문은 없다.
- 54–55: 마지막 반복에는 기준을 TOL*1.D3까지 완화하는 분기가 있다.
