---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cg3ml3.f
lines: 19
sha256: 5f147f967a05d8573837b4f25f57d5ab2390d86e525f93a73a8da81de407400d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg3ml3.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | CG3ML3의 MPI_PARAM 사용, 암시적 형(implicit typing), 벡터·희소 인덱스(sparse index) 배열을 선언한다. INDOF의 첫 번째 크기는 6이다. 원문: `      SUBROUTINE CG3ML3(Y,A,X,NEQ,IDSK,IDCG,INDOF,INDOP,IMPC,ITO)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION Y(NEQ),A(*),X(*),IDSK(NEQ+1),IDCG(*),INDOF(6,*),INDOP(*)` (6). |
| 8–12 | 시작 시 1행 CG3ML3 루틴 안. NPROCS가 1보다 크면 COMM_CG2를 호출한다. 같은 분기에서 IMPC가 양수이면 COMM_CG2X도 호출한다. 원문: `      IF( NPROCS > 1 ) THEN` (8); `        CALL COMM_CG2(X,INDOF,INDOP)` (9); `        IF( IMPC > 0 ) CALL COMM_CG2X(X,INDOF,INDOP)` (10); `      ENDIF` (11). |
| 13–19 | 시작 시 1행 CG3ML3 루틴 안. NEQ개 행의 시작 위치와 길이를 계산하여 VECMID3에 Y(I)와 관련 배열을 전달한다. 루틴 끝을 포함한다. 원문: `      DO 100 I=1,NEQ` (13); `        IS=IDSK(I)` (14); `        NN=IDSK(I+1)-IDSK(I)` (15); `        CALL VECMID3(Y(I),A(IS),X,IDCG(IS),NN)` (16); `  100 CONTINUE` (17); `      END` (19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·3–19: ITO는 인수에 있지만 본문에서 참조하지 않는다.
