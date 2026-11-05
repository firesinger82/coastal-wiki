---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/blmtx.f
lines: 44
sha256: 7b02221a9c56057806c2bae30577ecbe38b5c1b888f1d078ef50a9a785fc1828
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# blmtx.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | BLMTX의 인수와 배열을 선언한다. `節点数`는 절점 수(number of nodes)이고 ND가 이를 받는다. IGNL의 `微小変形`은 미소변형(small deformation), `大変形`은 대변형(large deformation)이다. 해석: 4–5행의 N과 u를 각각 형상함수와 변위로 보면 DNDX와 DUDX는 그 공간 미분이다. 원문: `      SUBROUTINE BLMTX(BL,DNDX,DUDX,ND,IGNL)` (1); 주석 원문 `C     BL   : OUT : [BL]` (3); 주석 원문 `C     DNDX : IN  : DNDX(i,j) = ∂Nj/∂xi` (4); 주석 원문 `C     DUDX : IN  : DUDX(i,j) = ∂uj/∂xi` (5); 주석 원문 `C     ND   : IN  : 節点数` (6); 주석 원문 `C     IGNL : IN  : =0:微小変形, =1:大変形` (7); `      IMPLICIT REAL*8(A-H,O-Z)` (9); `      DIMENSION BL(6,3*ND),DNDX(3,ND),DUDX(3,3)` (10). [11-04 전수 검증 정정] |
| 12–29 | 시작 시 1행 BLMTX 루틴 안. CLEAR1으로 BL을 초기화한다. ND개 절점에 대해 BL의 6개 행에 DNDX 성분을 배치한다. 해석: 이 대입은 변형률 계산에 쓰이는 선형 성분 배치에 해당한다. IGNL이 0이면 반환한다. 원문: `      CALL CLEAR1(BL,6*3*ND)` (12); `      DO 100 J=1,ND` (14); `        J0=3*(J-1)` (16); `        BL(1,J0+1)=DNDX(1,J)` (17); `        BL(2,J0+2)=DNDX(2,J)` (18); `        BL(3,J0+3)=DNDX(3,J)` (19); `        BL(4,J0+1)=DNDX(2,J)` (20); `        BL(4,J0+2)=DNDX(1,J)` (21); `        BL(5,J0+2)=DNDX(3,J)` (22); `        BL(5,J0+3)=DNDX(2,J)` (23); `        BL(6,J0+1)=DNDX(3,J)` (24); `        BL(6,J0+3)=DNDX(1,J)` (25); `  100 CONTINUE` (27); `      IF(IGNL .EQ. 0) RETURN` (29). [11-04 전수 검증 정정] |
| 30–44 | 시작 시 1행 BLMTX 루틴 안. 29행에서 반환하지 않은 경우 J·K·I 루프에서 BL의 1–3행을 보정한다. 37–39행은 BL의 4–6행을 보정한다. 해석: BL의 4–6행은 전단 성분에 해당한다. 반환문과 루틴 끝을 포함한다. 원문: `      DO 200 J=1,ND` (31); `        J0=3*(J-1)` (32); `        DO 210 K=1,3` (33); `          DO 220 I=1,3` (34); `            BL(I,J0+K)=BL(I,J0+K)+DUDX(I,K)*DNDX(I,J)` (35); `  220     CONTINUE` (36); `          BL(4,J0+K)=BL(4,J0+K)+DUDX(1,K)*DNDX(2,J)+DUDX(2,K)*DNDX(1,J)` (37); `          BL(5,J0+K)=BL(5,J0+K)+DUDX(2,K)*DNDX(3,J)+DUDX(3,K)*DNDX(2,J)` (38); `          BL(6,J0+K)=BL(6,J0+K)+DUDX(3,K)*DNDX(1,J)+DUDX(1,K)*DNDX(3,J)` (39); `  210   CONTINUE` (40); `  200 CONTINUE` (41); `      RETURN` (43); `      END` (44). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
