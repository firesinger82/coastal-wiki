---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/koji3e.f
lines: 41
sha256: 6515dd5e737a5f3b6b3dc0cd17d2a7b76f53f3d40d6d5290ca535cf04cc9551b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# koji3e.f — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | KOJI3E의 주변형률(principal strain)·방향 코사인(direction cosine) 영어 설명과 배열 선언이다. STRAIN의 여섯 성분 제곱합을 계산한다. 임계값을 넘지 않으면 PSTRAIN은 0, CMX는 단위행렬로 만들고 9000으로 이동한다. 원문: `      SUBROUTINE KOJI3E(STRAIN,PSTRAIN,CMX,ITO)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `C     PRINCIPAL STRAIN AND ITS DIRECTION COSINE` (5)； `C       STRAIN(1)=EPSILON_X` (7)； `C       STRAIN(2)=EPSILON_Y` (8)； `C       STRAIN(3)=EPSILON_Z` (9)； `C       STRAIN(4)=GAMMA_XY = 2*EPSILON_XY` (10)； `C       STRAIN(5)=GAMMA_YZ = 2*EPSILON_YZ` (11)； `C       STRAIN(6)=GAMMA_ZX = 2*EPSILON_ZX` (12)； `      DIMENSION STRAIN(6),PSTRAIN(3),CMX(3,3),STRMTX(3,3)` (14)； `      SS=0.0D0` (16)； `      DO 2000 I=1,6` (17)； ` 2000 SS=SS+STRAIN(I)*STRAIN(I)` (18)； `      IF(SS.GT.1.0D-20)GO TO 4000` (19)； `      DO 3100 I=1,3` (20)； `      DO 3050 J=1,3` (21)； ` 3050 CMX(I,J)=0.0D0` (22)； `      PSTRAIN(I)=0.0D0` (23)； ` 3100 CMX(I,I)=1.0D0` (24)； `      GO TO 9000` (25)。 |
| 27–41 | 시작 시 1행 KOJI3E 루틴 안이며 19행 `IF(SS.GT.1.0D-20)GO TO 4000`에서 27행 레이블 4000으로 이동한 경로이다. 레이블 9000은 40행 RETURN이다. 전단 성분에 0.5를 곱하여 3×3 대칭 변형률 행렬을 구성한다. FACT를 설정하고 JACOBI를 호출한 뒤 반환한다. 원문: ` 4000 STRMTX(1,1)=STRAIN(1)` (27)； `      STRMTX(1,2)=STRAIN(4)*0.5D0` (28)； `      STRMTX(1,3)=STRAIN(6)*0.5D0` (29)； `      STRMTX(2,1)=STRMTX(1,2)` (30)； `      STRMTX(2,2)=STRAIN(2)` (31)； `      STRMTX(2,3)=STRAIN(5)*0.5D0` (32)； `      STRMTX(3,1)=STRMTX(1,3)` (33)； `      STRMTX(3,2)=STRMTX(2,3)` (34)； `      STRMTX(3,3)=STRAIN(3)` (35)； `      FACT=1.0D-6` (37)； `      CALL JACOBI(STRMTX,PSTRAIN,CMX,3,15,FACT ,0,3,K,ITO)` (38)； ` 9000 RETURN` (40)； `      END` (41)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–25: `SS.GT.1.0D-20`이 참이면 행렬 구성으로 이동한다. 이 조건이 거짓이면 PSTRAIN을 0으로 설정한다. 37–38행의 FACT는 1.0D-6이다. 반복 상한 15의 근거는 같은 원문 디렉터리의 `jacobi.f:1,12,22`이다. [11-04 전수 검증 정정]
