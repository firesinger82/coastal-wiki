---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cg3ml2.f
lines: 23
sha256: c3fd21cac049d4cd5d397f8bceb11ffcc71d0607bc6f5bc8680fbaceaa6ea7d6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg3ml2.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | CG3ML2의 MPI_PARAM 사용과 암시적 형 및 배열 크기를 선언한다. 해석: IDSK·IDCG는 희소 인덱스이며 INDOF는 자유도 인덱스이다. 원문: `      SUBROUTINE CG3ML2(Y,A,X,NEQ,IDSK,IDCG,NCGSPC,INDOF,NDF,IMPC,ITO)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION Y(NEQ),A(NCGSPC),X(NEQ),IDSK(NEQ+1),IDCG(NCGSPC)`<br>`     *         ,INDOF(NDF,*)` (6–7). [11-04 전수 검증 정정] |
| 9–15 | 시작 시 1행 CG3ML2 루틴 안. NPROCS가 1보다 크면 X·INDOF·NDF를 인수로 COMM_CG를 호출한다. 이 분기에서 IMPC가 양수이면 COMM_CGX도 호출한다. CLEAR1으로 Y를 초기화한다. 원문: `      IF( NPROCS > 1 ) THEN` (9); `        CALL COMM_CG(X,INDOF,NDF)` (10); `        IF( IMPC > 0 ) CALL COMM_CGX(X,INDOF,NDF)` (11); `      ENDIF` (12); `      CALL CLEAR1(Y,NEQ)` (14). [11-04 전수 검증 정정] |
| 16–23 | 시작 시 1행 CG3ML2 루틴 안. 각 행의 시작 위치와 길이를 계산하여 VECMID를 호출한다. NN이 2 이상이면 VECMID2에 A(IS+1)·IDCG(IS+1)과 NN-1을 전달한다. 해석: IS가 대각 저장 위치이면 IS+1은 대각 다음 위치이다. 반환문과 루틴 끝을 포함한다. 원문: `      DO 100 I=1,NEQ` (16); `        IS=IDSK(I)` (17); `        NN=IDSK(I+1)-IDSK(I)` (18); `        CALL VECMID(Y(I),A(IS),X,IDCG(IS),NN)` (19); `        IF(NN.GE.2) CALL VECMID2(Y,A(IS+1),X(I),IDCG(IS+1),NN-1)` (20); `  100 CONTINUE` (21); `      RETURN` (22); `      END` (23). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·3–23: ITO는 인수에 있지만 본문에서 참조하지 않는다.
