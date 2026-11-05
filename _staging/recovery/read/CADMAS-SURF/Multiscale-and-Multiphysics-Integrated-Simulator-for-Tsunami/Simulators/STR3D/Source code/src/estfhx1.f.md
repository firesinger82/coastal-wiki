---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estfhx1.f
lines: 63
sha256: b0cf3d3e240e1f94e182c58c32e7defc080f9a9299f12ad530ab95481f3a053a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfhx1.f — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 8절점 요소의 강성 배열과 일본어 인수 설명·선언·적분표 포함 구간이다. LCCHX1을 호출하고 ESTF를 0으로 한다. 원문: `      SUBROUTINE ESTFHX1(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (1)； `!     ESTF : OUT : 要素剛性行列(上三角,1次元配列)` (3) (요소 강성행렬(stiffness matrix)을 상삼각 1차원 배열로 출력한다.)； `!                  配列要素の並びは3×3の行列を例にとると以下の通り` (4) (3×3 행렬을 예로 든 배열 원소의 배치이다.)； `!                    1 2 3` (6)； `!                      4 5` (7)； `!                        6` (8)； `!     GRID : IN  : 節点座標` (10) (절점 좌표 입력이다.)； `!     UG   : IN  : 節点変位` (11) (절점 변위 입력이다.)； `!     NP   : IN  : 要素の構成節点番号` (12) (요소 구성 절점 번호 입력이다.)； `!     D    : IN  : 構成則マトリックス` (13) (구성법칙 행렬 입력이다.)； `!     S    : IN  : 応力` (14) (응력 입력이다.)； `!     IGNL : IN  : =0:微小変形, =1:大変形` (15) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (17)； 연속문(19–22): `      DIMENSION TE(3,3),X0(3,8),U(3,8),GRID(3,*),UG(6,*),NP(8)` (19)； `     &         ,D(21,2,2,2),DNDX(3,8,4),DUDX(3,3,4),BL(6,24),BLTD(24,6)` (20)； `     &         ,BLTDBL(300),E(300,6),SE(300),S(6,2,2,2),ESTF(300)` (21)； `     &         ,WK(576)` (22)； `      INCLUDE 'gauss_ln_3.h'` (24)； `      CALL LCCHX1(TE,X0,U,GRID,UG,NP)` (26)； `      ESTF(:) = 0.` (28)。 |
| 30–63 | 시작 시 1행 ESTFHX1 루틴 안이다. 각 방향 2점 적분에서 DERXHX1을 호출한다. L=1..4에 대해 MATML을 호출한다. BLMHX1·MATML을 차례로 호출한다. 해석: DUDX는 변위 기울기이고 BLTDBL은 재료 항이다. IGNL > 0일 때 ETAHX1과 응력으로 SE를 계산한다. ESTF를 누적한 뒤 STFGL을 호출한다. 원문: `      DO I = 1, 2` (30)； `      DO J = 1, 2` (31)； `      DO K = 1, 2` (32)； `        XG1 = XG(I,2)` (34)； `        XG2 = XG(J,2)` (35)； `        XG3 = XG(K,2)` (36)； `        WGT = WG(I,2)*WG(J,2)*WG(K,2)` (37)； `        CALL DERXHX1(DNDX,DET,XG1,XG2,XG3,X0,ITO)` (39)； `        DO L = 1, 4` (40)； `          CALL MATML(DUDX(1,1,L),2,DNDX(1,1,L),2,U,3,3,3,8)` (41)； `        ENDDO` (42)； `        CALL BLMHX1(BL,DNDX,DUDX,IGNL)` (44)； `        CALL MATML(BLTD,2,BL,3,D(1,I,J,K),1,24,6,6)` (45)； `        CALL MATML(BLTDBL,1,BLTD,2,BL,2,24,24,6)` (46)； `        IF( IGNL > 0 ) THEN` (48)； `          CALL ETAHX1(E,DNDX)` (49)； `          CALL MATML(SE,2,E,2,S(1,I,J,K),2,300,1,6)` (50)； `        ELSE` (51)； `          SE(:) = 0.` (52)； `        ENDIF` (53)； `        ESTF(:) = ESTF(:) + ( BLTDBL(:) + SE(:) ) * DET * WGT` (55)； `      ENDDO` (57)； `      ENDDO` (58)； `      ENDDO` (59)； `      CALL STFGL(ESTF,WK,TE,24,3)` (61)； `      END` (63)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–22·30–32: NP는 8개 절점, ESTF는 300개 성분, 적분은 2×2×2점으로 고정된다.
