---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/estfpn1.f
lines: 67
sha256: eed73764752bcb3b74a0de6a761b170702f81afce71cc956f5785dda9b65859d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# estfpn1.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 6절점 요소의 강성 배열과 인수 설명·선언·적분표 포함 구간이다. LCCPN1·TRPN1S를 호출한다. I 루프에서 DERXPN2의 일곱 번째 인수에 `0.D0`을 전달한다. MATML 호출 뒤 BLMPN1S를 호출한다. 해석: 이 루프는 중앙면의 변위 기울기를 계산한다. IGNL > 0일 때만 ETAPN1S를 호출한다. ESTF를 0으로 한다. 원문: `      SUBROUTINE ESTFPN1(ESTF,GRID,UG,NP,D,S,IGNL,ITO)` (1)； `!     ESTF : OUT : 要素剛性行列(上三角,1次元配列)` (3) (요소 강성행렬(stiffness matrix)을 상삼각 1차원 배열로 출력한다.)； `!                  配列要素の並びは3×3の行列を例にとると以下の通り` (4) (3×3 행렬을 예로 든 배열 원소의 배치이다.)； `!                    1 2 3` (6)； `!                      4 5` (7)； `!                        6` (8)； `!     GRID : IN  : 節点座標` (10) (절점 좌표 입력이다.)； `!     UG   : IN  : 節点変位` (11) (절점 변위 입력이다.)； `!     NP   : IN  : 要素の構成節点番号` (12) (요소 구성 절점 번호 입력이다.)； `!     D    : IN  : 構成則マトリックス` (13) (구성법칙 행렬 입력이다.)； `!     S    : IN  : 応力` (14) (응력 입력이다.)； `!     IGNL : IN  : =0:微小変形, =1:大変形` (15) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (17)； 연속문(19–22): `      DIMENSION TE(3,3),X0(3,6),U(3,6),GRID(3,*),UG(6,*),NP(6),TR(6,6)` (19)； `     &         ,DNDX(3,6,3),DUDX(3,3,3),BLS(2,18,3),ES(171,2,3),BL(6,18)` (20)； `     &         ,D(21,3,2),BLTD(18,6),BLTDBL(171),E(171,6),SE(171)` (21)； `     &         ,S(6,3,2),ESTF(171),WK(324)` (22)； `      INCLUDE 'gauss_pn_32.h'` (24)； `      CALL LCCPN1(TE,X0,U,GRID,UG,NP)` (26)； `      CALL TRPN1S(TR,X0,ITO)` (28)； `      DO I = 1, 3` (30)； `        CALL DERXPN2(DNDX(1,1,I),DET,6,X0,RG(I),SG(I),0.D0,ITO)` (31)； `        CALL MATML(DUDX(1,1,I),2,DNDX(1,1,I),2,U,3,3,3,6)` (32)； `      ENDDO` (33)； `      CALL BLMPN1S(BLS,DNDX,DUDX,TR,IGNL)` (35)； `      IF( IGNL > 0 ) CALL ETAPN1S(ES,DNDX,TR)` (37)； `      ESTF(:) = 0.` (39)。 [11-04 전수 검증 정정] [11-04 전수 검증 정정] |
| 41–67 | 시작 시 1행 ESTFPN1 루틴 안이다. J=1..2와 I=1..3에서 DERXPN2·MATML·BLMPN1을 호출하고 BL의 5:6 성분을 BLS로 바꾼다. IGNL > 0일 때 ETAPN1 호출 뒤 E의 5:6열을 ES로 바꾸어 SE를 구한다. DET/6을 곱해 강성을 누적하고 STFGL을 호출한다. 원문: `      DO J = 1, 2` (41)； `        DO I = 1, 3` (42)； `          CALL DERXPN2(DNDX,DET,6,X0,RG(I),SG(I),TG(J),ITO)` (44)； `          CALL MATML(DUDX,2,DNDX,2,U,3,3,3,6)` (45)； `          CALL BLMPN1(BL,DNDX,DUDX,IGNL)` (47)； `          BL(5:6,:) = BLS(:,:,I)` (48)； `          CALL MATML(BLTD,2,BL,3,D(1,I,J),1,18,6,6)` (49)； `          CALL MATML(BLTDBL,1,BLTD,2,BL,2,18,18,6)` (50)； `          IF( IGNL > 0 ) THEN` (52)； `            CALL ETAPN1(E,DNDX)` (53)； `            E(:,5:6) = ES(:,:,I)` (54)； `            CALL MATML(SE,2,E,2,S(1,I,J),2,171,1,6)` (55)； `          ELSE` (56)； `            SE(:) = 0.` (57)； `          ENDIF` (58)； `          ESTF(:) = ESTF(:) + ( BLTDBL(:) + SE(:) ) * DET / 6.D0` (60)； `        ENDDO` (62)； `      ENDDO` (63)； `      CALL STFGL(ESTF,WK,TE,18,3)` (65)； `      END` (67)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60: ESTF 누적식은 `( BLTDBL(:) + SE(:) ) * DET / 6.D0`을 더한다. [11-04 전수 검증 정정]
