---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/etamtx.f
lines: 42
sha256: e9bfe4bed6678bd24e26c8426a813a748bb694409ccc0eb2188dbbdd31bf4d31
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# etamtx.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | ETAMTX의 E·DNDX·절점 수와 배열 크기 인수 설명이다. F를 초기화한다. `J0 = 3 * ( J - 1 )`로 열 기준값을 계산한다. `F(K,J0+K,I) = DNDX(I,J)`로 성분을 배치한다. 해석: DNDX는 형상함수(shape function) 기울기이고 J0+K는 세 방향 자유도 위치이다. 원문: `      SUBROUTINE ETAMTX(E,DNDX,N,N3,NL)` (1)； `!     E    : OUT : [Eij]` (3) (Eij 행렬 출력이다.)； `!                  E(:,1) = [E11]` (4)； `!                  E(:,2) = [E22]` (5)； `!                  E(:,3) = [E33]` (6)； `!                  E(:,4) = 2*[E12]` (7)； `!                  E(:,5) = 2*[E23]` (8)； `!                  E(:,6) = 2*[E31]` (9)； `!     DNDX : IN  : DNDX(i,j) = ∂Nj/∂xi` (10)； `!     N    : IN  : 節点数` (11) (절점 수 입력이다.)； `!     N3   : IN  : 3*節点数` (12) (절점 수의 3배 입력이다.)； `!     NL   : IN  : 要素剛性行列のサイズ` (13) (요소 강성행렬 크기 입력이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (15)； `      DIMENSION F(3,N3,3),DNDX(3,N),FTF(NL,3,3),E(NL,6)` (16)； `      F(:,:,:) = 0.` (18)； `      DO I = 1, 3` (20)； `        DO J = 1, N` (21)； `          J0 = 3 * ( J - 1 )` (22)； `          DO K = 1, 3` (23)； `            F(K,J0+K,I) = DNDX(I,J)` (24)； `          ENDDO` (25)； `        ENDDO` (26)； `      ENDDO` (27)。 [11-04 전수 검증 정정] |
| 29–42 | 시작 시 1행 ETAMTX 루틴 안이다. I·J의 모든 방향 조합에 대해 MATML을 호출한다. 세 대각 곱과 세 비대각 대칭 합을 E의 여섯 열로 저장한다. 원문: `      DO I = 1, 3` (29)； `        DO J = 1, 3` (30)； `          CALL MATML(FTF(1,I,J),1,F(1,1,I),3,F(1,1,J),2,N3,N3,3)` (31)； `        ENDDO` (32)； `      ENDDO` (33)； `      E(:,1) = FTF(:,1,1)` (35)； `      E(:,2) = FTF(:,2,2)` (36)； `      E(:,3) = FTF(:,3,3)` (37)； `      E(:,4) = FTF(:,1,2) + FTF(:,2,1)` (38)； `      E(:,5) = FTF(:,2,3) + FTF(:,3,2)` (39)； `      E(:,6) = FTF(:,3,1) + FTF(:,1,3)` (40)； `      END` (42)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
