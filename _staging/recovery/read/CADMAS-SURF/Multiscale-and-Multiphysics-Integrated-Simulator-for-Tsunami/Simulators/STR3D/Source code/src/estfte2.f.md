---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estfte2.f
lines: 50
sha256: 9c3faa91b42fdc2f9eb402eeca021e699a4872bb97ab1adfd5981d35928ec268
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfte2.f — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 10절점 요소의 강성 배열과 인수 설명·선언·적분표 포함 구간이다. 좌표·변위를 수집하고 ESTF를 0으로 한다. 원문: `      SUBROUTINE ESTFTE2(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (1)； `!     ESTF : OUT : 要素剛性行列(上三角,1次元配列)` (3) (요소 강성행렬(stiffness matrix)을 상삼각 1차원 배열로 출력한다.)； `!                  配列要素の並びは3×3の行列を例にとると以下の通り` (4) (3×3 행렬을 예로 든 배열 원소의 배치이다.)； `!                    1 2 3` (6)； `!                      4 5` (7)； `!                        6` (8)； `!     GRID : IN  : 節点座標` (10) (절점 좌표 입력이다.)； `!     UG   : IN  : 節点変位` (11) (절점 변위 입력이다.)； `!     NP   : IN  : 要素の構成節点番号` (12) (요소 구성 절점 번호 입력이다.)； `!     D    : IN  : 構成則マトリックス` (13) (구성법칙 행렬 입력이다.)； `!     S    : IN  : 応力` (14) (응력 입력이다.)； `!     IGNL : IN  : =0:微小変形, =1:大変形` (15) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (17)； 연속문(19–21): `      DIMENSION X0(3,10),U(3,10),GRID(3,*),UG(6,*),NP(10),D(21,5)` (19)； `     &         ,DNDX(3,10),DUDX(3,3),BL(6,30),BLTD(30,6),BLTDBL(465)` (20)； `     &         ,E(465,6),SE(465),S(6,5),ESTF(465)` (21)； `      INCLUDE 'gauss_te_5.h'` (23)； `      X0(:,:) = GRID(:,NP(:))` (25)； `      U(:,:) = UG(1:3,NP(:))` (26)； `      ESTF(:) = 0.` (28)。 |
| 30–50 | 시작 시 1행 ESTFTE2 루틴 안이다. 다섯 적분점에서 DERXTE2·MATML·BLMTX를 호출한다. IGNL > 0이면 ETAMTX와 응력으로 SE를 구한다. DET와 WG를 곱해 ESTF에 누적한다. 원문: `      DO I = 1, 5` (30)； `        CALL DERXTE2(DNDX,DET,RLG(1,I),X0,ITO)` (32)； `        CALL MATML(DUDX,2,DNDX,2,U,3,3,3,10)` (33)； `        CALL BLMTX(BL,DNDX,DUDX,10,IGNL)` (35)； `        CALL MATML(BLTD,2,BL,3,D(1,I),1,30,6,6)` (36)； `        CALL MATML(BLTDBL,1,BLTD,2,BL,2,30,30,6)` (37)； `        IF( IGNL > 0 ) THEN` (39)； `          CALL ETAMTX(E,DNDX,10,30,465)` (40)； `          CALL MATML(SE,2,E,2,S(1,I),2,465,1,6)` (41)； `        ELSE` (42)； `          SE(:) = 0.` (43)； `        ENDIF` (44)； `        ESTF(:) = ESTF(:) + ( BLTDBL(:) + SE(:) ) * DET * WG(I)` (46)； `      ENDDO` (48)； `      END` (50)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–21·30: NP는 10개 절점, ESTF는 465개 성분, 적분점 수는 5로 고정된다.
