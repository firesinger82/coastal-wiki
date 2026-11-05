---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/etapn1s.f
lines: 44
sha256: 36f15a78d8b235f1f190fec465addb69b0df8384c0d24f87aa86cc3d26f70b20
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# etapn1s.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | ETAPN1S의 적분점별 E23·E31 설명과 배열 선언이다. 세 적분점에서 F를 구성하고 MATML의 두 순서 곱을 더하여 E의 IG·IG+3 열을 구한다. 원문: `      SUBROUTINE ETAPN1S(ES,DNDX,GQD)` (1)； `!     ES   : OUT : ES(:,1,ig) = [E23] (積分点ig)` (3) (적분점 ig의 E23 출력이다.)； `!                  ES(:,2,ig) = [E31] (積分点ig)` (4) (적분점 ig의 E31 출력이다.)； `!     DNDX : IN  : DNDX(i,j,ig) = ∂Nj/∂xi (積分点ig)` (5) (적분점 ig에서 형상함수 공간 미분 입력이다.)； `!     GQD  : IN  : [E] (γyz,γzxの変換行列)` (6) (γyz·γzx 변환행렬(transformation matrix) 입력이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (8)； 연속문(9–10): `      DIMENSION F(3,18,3),DNDX(3,6,3),FTF(171,3,3),E(171,6),EB(171,6)` (9)； `     &         ,GQD(6,6),ES(171,2,3)` (10)； `      DO IG = 1, 3` (12)； `        F(:,:,:) = 0.` (14)； `        DO I = 1, 3` (16)； `          DO J = 1, 6` (17)； `            J0 = 3 * ( J - 1 )` (18)； `            DO K = 1, 3` (19)； `              F(K,J0+K,I) = DNDX(I,J,IG)` (20)； `            ENDDO` (21)； `          ENDDO` (22)； `        ENDDO` (23)； `        CALL MATML(FTF(1,2,3),1,F(1,1,2),3,F(1,1,3),2,18,18,3)` (25)； `        CALL MATML(FTF(1,3,2),1,F(1,1,3),3,F(1,1,2),2,18,18,3)` (26)； `        E(:,IG) = FTF(:,2,3) + FTF(:,3,2)` (28)； `        CALL MATML(FTF(1,3,1),1,F(1,1,3),3,F(1,1,1),2,18,18,3)` (30)； `        CALL MATML(FTF(1,1,3),1,F(1,1,1),3,F(1,1,3),2,18,18,3)` (31)； `        E(:,IG+3) = FTF(:,3,1) + FTF(:,1,3)` (33)； `      ENDDO` (35)。 |
| 36–44 | 시작 시 1행 ETAPN1S 루틴 안이며 12행 IG 루프 밖이다. GQD와 MATML을 사용하여 EB를 계산한 뒤 세 적분점의 두 전단 성분을 ES에 복사한다. 원문: `      CALL MATML(EB,2,E,2,GQD,3,171,6,6)` (37)； `      DO IG = 1, 3` (39)； `        ES(:,1,IG) = EB(:,IG)` (40)； `        ES(:,2,IG) = EB(:,IG+3)` (41)； `      ENDDO` (42)； `      END` (44)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–10·12–41: 세 적분점과 여섯 구성 절점을 배열과 반복 범위에 고정한다.
