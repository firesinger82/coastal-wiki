---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cg3fwb.f
lines: 30
sha256: 668cb4dd6573b9c6dca798e61cf7c9f6714a04086c7745e9ba497bced39cebe6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cg3fwb.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | CG3FWB의 암시적 형(implicit typing)과 벡터·희소 인덱스(sparse index) 배열 크기를 선언한다. 원문: `      SUBROUTINE CG3FWB(D,RLOW,X,WK,NEQ,IDSK,IDCG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION D(NEQ),RLOW(*),X(NEQ),WK(NEQ),IDSK(NEQ+1),IDCG(*)` (4). |
| 6–16 | 시작 시 1행 CG3FWB 루틴 안. I를 증가시키는 전진대입(forward substitution)에서 IDSK로 행 범위를 구한다. `IF(IS.LE.IE) THEN`인 경우에만 RLOW 항을 뺀다. `X(I)=X(I)*D(I)`는 이 IF 밖에서 매 I 반복마다 실행한다. 원문: `      DO 1000 I=1,NEQ` (6); `        IS=IDSK(I)+1` (7); `        IE=IDSK(I+1)-1` (8); `        IF(IS.LE.IE) THEN` (9); `          DO 1100 J=IS,IE` (10); `            X(I)=X(I)-RLOW(J)*X(IDCG(J))` (11); ` 1100     CONTINUE` (12); `        ENDIF` (13); `        X(I)=X(I)*D(I)` (14); ` 1000 CONTINUE` (15). [11-04 전수 검증 정정] |
| 17–30 | 시작 시 1행 CG3FWB 루틴 안. CLEAR1으로 WK를 초기화한다. J를 역순으로 돌며 WK에 연결 항을 누적한 후 X(J-1)을 갱신하는 후진대입(backward substitution)을 수행한다. 반환문과 루틴 끝을 포함한다. 원문: `      CALL CLEAR1(WK,NEQ)` (17); `      DO 2000 J=NEQ,2,-1` (18); `        IS=IDSK(J)+1` (19); `        IE=IDSK(J+1)-1` (20); `        IF(IS.LE.IE) THEN` (21); `          DO 2100 I=IS,IE` (22); `            WK(IDCG(I))=WK(IDCG(I))+RLOW(I)*X(J)` (23); ` 2100     CONTINUE` (24); `        ENDIF` (25); `        X(J-1)=X(J-1)-D(J-1)*WK(J-1)` (26); ` 2000 CONTINUE` (27); `      RETURN` (29); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
