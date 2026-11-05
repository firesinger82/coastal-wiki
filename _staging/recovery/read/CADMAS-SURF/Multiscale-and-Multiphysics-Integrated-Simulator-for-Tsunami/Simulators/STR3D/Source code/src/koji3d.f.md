---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/koji3d.f
lines: 48
sha256: d946158568e185796952459450d813152d9761df994ad395c4b2bebe7fb36a3f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# koji3d.f — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | KOJI3D의 응력·주응력(principal stress)·주축(principal axis) 일본어 설명과 배열 선언이다. 응력 여섯 성분의 제곱합을 구한다. SS가 임계값을 넘지 않으면 주응력을 0, 주축 행렬을 단위행렬로 설정하고 9000으로 이동한다. 원문: `      SUBROUTINE KOJI3D(STRESS,PSTRES,CMX,ITO)` (1)； `C     STRESS : IN  : 応力` (3) (응력 입력이다.)； `C                    STRESS(1) = σx` (4)； `C                    STRESS(2) = σy` (5)； `C                    STRESS(3) = σz` (6)； `C                    STRESS(4) = τxy` (7)； `C                    STRESS(5) = τyz` (8)； `C                    STRESS(6) = τzx` (9)； `C     PSTRES : OUT : 主応力` (10) (주응력 출력이다.)； `C                    PSTRES(1) = σ1` (11)； `C                    PSTRES(2) = σ2` (12)； `C                    PSTRES(3) = σ3` (13)； `C     CMX    : OUT : 主軸` (14) (주축 출력이다.)； `C                    CMX(:,1) = σ1の方向余弦` (15) (σ1의 방향 코사인(direction cosine)이다.)； `C                    CMX(:,2) = σ2の方向余弦` (16) (σ2의 방향 코사인이다.)； `C                    CMX(:,3) = σ3の方向余弦` (17) (σ3의 방향 코사인이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (19)； `      DIMENSION STRESS(6),PSTRES(3),CMX(3,3),STRMTX(3,3)` (21)； `      SS=0.0D0` (23)； `      DO 2000 I=1,6` (24)； ` 2000 SS=SS+STRESS(I)*STRESS(I)` (25)； `      IF(SS.GT.1.0D-10)GO TO 4000` (26)； `      DO 3100 I=1,3` (27)； `      DO 3050 J=1,3` (28)； ` 3050 CMX(I,J)=0.0D0` (29)； `      PSTRES(I)=0.0D0` (30)； ` 3100 CMX(I,I)=1.0D0` (31)； `      GO TO 9000` (32)。 |
| 34–48 | 시작 시 1행 KOJI3D 루틴 안이며 26행 `IF(SS.GT.1.0D-10)GO TO 4000`에서 34행 레이블 4000으로 이동한 경로이다. 레이블 9000은 47행 RETURN이다. 여섯 응력 성분으로 3×3 대칭행렬을 구성한다. FACT를 설정하고 JACOBI에 크기 3·반복 상한 15 등을 전달한 뒤 반환한다. 원문: ` 4000 STRMTX(1,1)=STRESS(1)` (34)； `      STRMTX(1,2)=STRESS(4)` (35)； `      STRMTX(1,3)=STRESS(6)` (36)； `      STRMTX(2,1)=STRMTX(1,2)` (37)； `      STRMTX(2,2)=STRESS(2)` (38)； `      STRMTX(2,3)=STRESS(5)` (39)； `      STRMTX(3,1)=STRMTX(1,3)` (40)； `      STRMTX(3,2)=STRMTX(2,3)` (41)； `      STRMTX(3,3)=STRESS(3)` (42)； `      FACT=0.001` (44)； `      CALL JACOBI(STRMTX,PSTRES,CMX,3,15,FACT ,0,3,K,ITO)` (45)； ` 9000 RETURN` (47)； `      END` (48)。 [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–32: `SS.GT.1.0D-10`이 참이면 행렬 구성으로 이동한다. 이 조건이 거짓이면 PSTRES를 0으로 설정한다. 44–45행의 FACT는 0.001이다. 반복 상한 15의 근거는 같은 원문 디렉터리의 `jacobi.f:1,12,22`이다. [11-04 전수 검증 정정]
