---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/green_pn1s.f
lines: 36
sha256: 5fdcc9cf7e8f2cff2a4df4681a84e5ad890b77214c00595c91524e5ddfb8ce70
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# green_pn1s.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | GREEN_PN1S의 적분점별 전단 변형률 설명과 선언이다. 세 적분점에서 EPS의 I·I+3 성분을 계산한다. IGNL == 0이면 CYCLE로 이차 항을 건너뛴다. 그 외에는 기울기 곱을 더한다. 원문: `      SUBROUTINE GREEN_PN1S(EPSS,DUDX,GQD,IGNL)` (1)； `C     EPSS : OUT : EPSS(1,ig) = 2*ε23 (積分点ig)` (3) (적분점 ig의 전단 변형률 2*ε23 출력이다.)； `C                  EPSS(2,ig) = 2*ε31 (積分点ig)` (4) (적분점 ig의 전단 변형률 2*ε31 출력이다.)； `C     DUDX : IN  : DUDX(i,j,ig) = ∂uj/∂xi (積分点ig)` (5) (적분점 ig의 변위 기울기 입력이다.)； `C     GQD  : IN  : [E] ` (6)； `C     IGNL : IN  : =0:微小変形, =1:大変形` (7) (0은 미소변형(small deformation), 1은 대변형(large deformation)이다.)； `      IMPLICIT REAL*8(A-H,O-Z)` (9)； `      DIMENSION EPS(6),DUDX(3,3,3),EPSB(6),EPSS(2,3),GQD(6,6)` (10)； `      DO I = 1, 3` (12)； `        EPS(I  )=DUDX(3,2,I)+DUDX(2,3,I)` (14)； `        EPS(I+3)=DUDX(1,3,I)+DUDX(3,1,I)` (15)； `        IF( IGNL == 0 ) CYCLE` (17)； 연속문(19–21): `        EPS(I  )=EPS(I  )+( DUDX(2,1,I)*DUDX(3,1,I)` (19)； `     &                    + DUDX(2,2,I)*DUDX(3,2,I)` (20)； `     &                    + DUDX(2,3,I)*DUDX(3,3,I) )` (21)； 연속문(22–24): `        EPS(I+3)=EPS(I+3)+( DUDX(3,1,I)*DUDX(1,1,I)` (22)； `     &                    + DUDX(3,2,I)*DUDX(1,2,I)` (23)； `     &                    + DUDX(3,3,I)*DUDX(1,3,I) )` (24)； `      ENDDO` (26)。 |
| 28–36 | 시작 시 1행 GREEN_PN1S 루틴 안이며 12행 I 루프 밖이다. AXB에 GQD와 EPS를 전달하여 EPSB를 구한다. 세 적분점의 두 전단 성분을 EPSS로 복사한다. 원문: `      CALL AXB(EPSB,GQD,EPS,6,6,1)` (28)； `      DO I = 1, 3` (30)； `        EPSS(1,I) = EPSB(I)` (31)； `        EPSS(2,I) = EPSB(I+3)` (32)； `      ENDDO` (33)； `      RETURN` (35)； `      END` (36)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
