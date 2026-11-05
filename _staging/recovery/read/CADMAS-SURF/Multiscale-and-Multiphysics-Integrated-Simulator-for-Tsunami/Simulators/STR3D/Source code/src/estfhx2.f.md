---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estfhx2.f
lines: 59
sha256: c1d49632020a48c404931632eff9142907404fb461f74502d3ff3dfecd72b99b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfhx2.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 20절점 요소의 강성 배열과 일본어 인수 설명·선언·적분표 포함 구간이다. 좌표와 변위를 수집하고 ESTF를 0으로 한다. 원문: `      SUBROUTINE ESTFHX2(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (1)； `!     ESTF : OUT : 要素剛性行列(上三角,1次元配列)` (3) (요소 강성행렬(stiffness matrix)을 상삼각 1차원 배열로 출력한다.)； `!                  配列要素の並びは3×3の行列を例にとると以下の通り` (4) (3×3 행렬을 예로 든 배열 원소의 배치이다.)； `!                    1 2 3` (6)； `!                      4 5` (7)； `!                        6` (8)； `!     GRID : IN  : 節点座標` (10) (절점 좌표 입력이다.)； `!     UG   : IN  : 節点変位` (11) (절점 변위 입력이다.)； `!     NP   : IN  : 要素の構成節点番号` (12) (요소 구성 절점 번호 입력이다.)； `!     D    : IN  : 構成則マトリックス` (13) (구성법칙 행렬 입력이다.)； `!     S    : IN  : 応力` (14) (응력 입력이다.)； `!     IGNL : IN  : =0:微小変形, =1:大変形` (15) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (17)； 연속문(19–21): `      DIMENSION X0(3,20),U(3,20),GRID(3,*),UG(6,*),NP(20),D(21,3,3,3)` (19)； `     &         ,DNDX(3,20),DUDX(3,3),BL(6,60),BLTD(60,6),BLTDBL(1830)` (20)； `     &         ,E(1830,6),SE(1830),S(6,3,3,3),ESTF(1830)` (21)； `      INCLUDE 'gauss_ln_3.h'` (23)； `      X0(:,:) = GRID(:,NP(:))` (25)； `      U(:,:) = UG(1:3,NP(:))` (26)； `      ESTF(:) = 0.` (28)。 |
| 30–59 | 시작 시 1행 ESTFHX2 루틴 안이다. 각 방향 3점 적분에서 DERXHX2·MATML·BLMTX를 호출한다. IGNL > 0이면 ETAMTX와 응력으로 SE를 계산한다. `DET * WGT`를 곱해 ESTF를 누적한다. 해석: DET는 행렬식이고 WGT는 적분 가중치이다. 원문: `      DO I = 1, 3` (30)； `      DO J = 1, 3` (31)； `      DO K = 1, 3` (32)； `        XG1 = XG(I,3)` (34)； `        XG2 = XG(J,3)` (35)； `        XG3 = XG(K,3)` (36)； `        WGT = WG(I,3)*WG(J,3)*WG(K,3)` (37)； `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X0,20,ITO)` (39)； `        CALL MATML(DUDX,2,DNDX,2,U,3,3,3,20)` (40)； `        CALL BLMTX(BL,DNDX,DUDX,20,IGNL)` (42)； `        CALL MATML(BLTD,2,BL,3,D(1,I,J,K),1,60,6,6)` (43)； `        CALL MATML(BLTDBL,1,BLTD,2,BL,2,60,60,6)` (44)； `        IF( IGNL > 0 ) THEN` (46)； `          CALL ETAMTX(E,DNDX,20,60,1830)` (47)； `          CALL MATML(SE,2,E,2,S(1,I,J,K),2,1830,1,6)` (48)； `        ELSE` (49)； `          SE(:) = 0.` (50)； `        ENDIF` (51)； `        ESTF(:) = ESTF(:) + ( BLTDBL(:) + SE(:) ) * DET * WGT` (53)； `      ENDDO` (55)； `      ENDDO` (56)； `      ENDDO` (57)； `      END` (59)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–21·30–32: NP는 20개 절점, ESTF는 1830개 성분, 적분은 3×3×3점으로 고정된다.
