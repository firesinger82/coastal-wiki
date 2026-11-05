---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/iccg.f
lines: 78
sha256: 3213560c2ce8e1ea34fd47f1a23e1c44007019600971ca6e1a6e69901b0e9da6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# iccg.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | ICCG 인수와 MPI_PARAM 사용, 배열 선언 구간이다. 반복 상한이 0이면 CG_MPI_ALLREDUCE_I를 호출하고 결과를 5로 나눈 뒤 최소 50으로 한다. `A(IDSK(I)) .LE. 0.D0`이면 ITO에 `'PIVOT .LE. 0. , PROGRAM STOPPED !'`를 쓴다. 이어서 `CALL ERRSTP(90,ITO)`를 실행한다. SCALSY와 DTPRDCT를 호출한다. BNRM이 0이면 X를 초기화하고 반환하며 그 외에는 수렴 허용치(tolerance)를 계산한다. 원문: 연속문(1–2): `      SUBROUTINE ICCG(A,RLOW,B,X,WK,NEQ,NEQEXT,NCGSPC,IDSK,IDCG,INDOF` (1)； `     *               ,NDF,MXITCG,CGTOL,ITO,IDCOMP,IMPC)` (2)； `      USE MPI_PARAM` (4)； `      IMPLICIT REAL*8(A-H,O-Z)` (6)； 연속문(8–9): `      DIMENSION A(NCGSPC),B(NEQEXT),X(NEQEXT),WK(NEQEXT,6)` (8)； `     *         ,IDSK(NEQEXT+1),IDCG(NCGSPC),RLOW(NCGSPC),INDOF(NDF,*)` (9)； `      MAXITR=MXITCG` (11)； `      IF(MAXITR.EQ.0) THEN` (12)； `        CALL CG_MPI_ALLREDUCE_I(NEQ,MAXITR,1,0)` (13)； `        MAXITR=MAXITR/5` (14)； `        IF(MAXITR.LT.50) MAXITR=50` (15)； `      ENDIF` (16)； `      DO 300 I=1,NEQ` (18)； `        IF( A(IDSK(I)) .LE. 0.D0 ) THEN` (19)； `          WRITE(ITO,*) 'PIVOT .LE. 0. , PROGRAM STOPPED !'` (20)； `          CALL ERRSTP(90,ITO)` (21)； `        ENDIF` (22)； `  300 CONTINUE` (23)； `      CALL SCALSY(NEQ,NEQEXT,WK(1,4),A,B,IDSK,IDCG,INDOF,NDF,IMPC)` (25)； `      CALL DTPRDCT(BNRM,B,B,NEQ)` (26)； `      IF(BNRM.EQ.0.D0) THEN` (27)； `        CALL CLEAR1(X,NEQ)` (28)； `        RETURN` (29)； `      ENDIF` (30)； `      TOL=CGTOL*CGTOL*BNRM` (31)。 [11-04 전수 검증 정정] |
| 33–45 | 시작 시 1행 ICCG 루틴 안이다. IDCOMP == 0이면 CG3ILU와 SHIFT1을 호출하고 ELSE에서는 ICHSKY를 호출한다. SHIFT1·CG3FWB·DTPRDCT·CLEAR1을 차례로 호출한다. 해석: 작업 벡터와 전처리(preconditioning) 결과·내적을 준비하고 X를 0으로 한다. 원문: `      IF(IDCOMP.EQ.0) THEN` (33)； `        CALL CG3ILU(WK(1,3),A,NEQ,IDSK,IDCG,NCGSPC,ITO)` (34)； `        CALL SHIFT1(RLOW,A,NCGSPC)` (35)； `      ELSE` (36)； `        CALL ICHSKY(WK(1,3),A,RLOW,NEQ,IDSK,IDCG,ITO)` (37)； `      ENDIF` (38)； `      CALL SHIFT1(WK(1,1),B,NEQ)` (40)； `      CALL SHIFT1(WK(1,2),WK(1,1),NEQ)` (41)； `      CALL CG3FWB(WK(1,3),RLOW,WK(1,2),WK(1,6),NEQ,IDSK,IDCG)` (42)； `      CALL DTPRDCT(BETA1,WK(1,2),WK(1,1),NEQ)` (43)； `      CALL CLEAR1(X,NEQ)` (44)。 [11-04 전수 검증 정정] |
| 46–78 | 시작 시 1행 ICCG 루틴 안이다. 반복 중 CG3ML2·DTPRDCT·RMULT4를 호출한다. 해석: 이 호출들은 해와 잔차(residual)를 갱신한다. `RES < TOL` 또는 `ITER == MAXITR .AND. RES < TOL*1.D3`이면 71행 레이블 200으로 이동한다. 해석: 그 외에는 전처리와 탐색 방향을 갱신한다. 반복이 소진되면 ITO에 `'NOT CONVERGED BY CG METHOD.'`를 쓴다. 이어서 `CALL ERRSTP(21,ITO)`를 실행한다. 71행 레이블 200에서 VECML3를 호출한다. NPROCS > 1이면 COMM_CG를 호출한다. 같은 블록 안에서 IMPC > 0이면 COMM_CGX도 호출한다. 원문: `      DO 100 ITER=1,MAXITR` (46)； `        ALP1=BETA1` (47)； 연속문(48–49): `        CALL CG3ML2(WK(1,5),A,WK(1,2),NEQEXT,IDSK,IDCG,NCGSPC,INDOF,NDF` (48)； `     &             ,IMPC,ITO)` (49)； `        CALL DTPRDCT(ALP2,WK(1,2),WK(1,5),NEQ)` (50)； `        ALP=ALP1/ALP2` (51)； `        CALL RMULT4(X,X,ALP,WK(1,2),NEQ)` (52)； `        CALL RMULT4(WK(1,1),WK(1,1),-ALP,WK(1,5),NEQ)` (53)； `        CALL DTPRDCT(RES,WK(1,1),WK(1,1),NEQ)` (55)； 연속문(57–58): `        IF( RES < TOL .OR. ( ITER == MAXITR .AND. RES < TOL*1.D3 ) )` (57)； `     &    GOTO 200` (58)； `        BETA2=BETA1` (60)； `        CALL SHIFT1(WK(1,5),WK(1,1),NEQ)` (61)； `        CALL CG3FWB(WK(1,3),RLOW,WK(1,5),WK(1,6),NEQ,IDSK,IDCG)` (62)； `        CALL DTPRDCT(BETA1,WK(1,5),WK(1,1),NEQ)` (63)； `        BETA=BETA1/BETA2` (64)； `        CALL RMULT4(WK(1,2),WK(1,5),BETA,WK(1,2),NEQ)` (65)； `  100 CONTINUE` (66)； `      WRITE(ITO,*) 'NOT CONVERGED BY CG METHOD.'` (68)； `      CALL ERRSTP(21,ITO)` (69)； `  200 CALL VECML3(X,WK(1,4),X,NEQ)` (71)； `      IF( NPROCS > 1 ) THEN` (73)； `        CALL COMM_CG(X,INDOF,NDF)` (74)； `        IF( IMPC > 0 ) CALL COMM_CGX(X,INDOF,NDF)` (75)； `      ENDIF` (76)； `      END        ` (78)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–58: 마지막 반복에서는 RES < TOL*1.D3인 경우에도 200으로 이동한다.
- 51·64: ALP2와 BETA2로 나누기 전의 0 여부 검사는 이 파일에 없다.
- 27–29: BNRM == 0일 때의 RETURN은 71–76행의 VECML3·통신 호출보다 앞에 있다.
