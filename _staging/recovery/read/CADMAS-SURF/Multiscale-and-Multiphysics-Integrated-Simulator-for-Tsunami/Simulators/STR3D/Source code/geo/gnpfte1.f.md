---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gnpfte1.f
lines: 35
sha256: 4df7227a0496fd261d2f9e8e7fa1f7a3a1b855829e7d1199542e46e95236534c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpfte1.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | GNPFTE1은 VELG와 FI를 계산한다. 실수 IMPLICIT·배열 선언을 아래에 적었다. RN은 모두 .25D0이다. DERXTE1·AXB를 호출한다. VELG는 `-GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:)`에 RK를 곱한 값이다. 해석: 루틴 이름과 배열 크기는 4절점 사면체(tetrahedron)를 가리키는 것으로 보인다. 해석: RN·DNDX·GRP·UDDG·GRAV는 각각 형상함수·공간 미분·압력 경사·보간 가속도·중력으로 보인다. 해석: VELG는 유량(flux)으로 보인다. ATXB 결과에 -DET/6을 곱하여 FI를 얻는다. 원문: `      SUBROUTINE GNPFTE1(FI,FO,FP,VELG,VELE,X,UD,UDD,P,PB,PD,POR,RKF,RK` (1); `     &                  ,RHOF,GRAV,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION RN(4),DNDX(3,4),X(3,4),GRP(3),P(4),UDDG(3),UDD(3,4)` (5); `     &         ,GRAV(3),FI(4),UD(3,4),PD(4),FO(4),PB(4),FP(3,4),VELE(3)` (6); `     &         ,VELG(3)` (7); `      RN(:) = .25D0` (9); `      CALL DERXTE1(DNDX,DET,X,ITO)` (11); `      CALL AXB(GRP,DNDX,P,3,4,1)` (13); `      CALL AXB(UDDG,UDD,RN,3,4,1)` (14); `      VELG(:) = RK * ( -GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:) )` (16); `      CALL ATXB(FI,DNDX,VELG,3,4,1)` (18); `      FI(:) = -FI(:) * DET / 6.D0` (20) [11-04 전수 검증 정정] |
| 21–35 | VECML1에 DUD·PDG를 각각 전달한다. FO는 RN*(DUD+POR/RKF*PDG)*DET/6.D0의 음수이다. PG·RN·PB를 VECML1에 전달한다. FP는 DNDX*PG*DET/6.D0이다. 해석: POR는 공극률(porosity)로 보인다. 해석: PG는 PB의 보간값으로 보인다. 중심점 값 VELE는 VELG를 복사한다. 원문: `      CALL VECML1(DUD,DNDX,UD,12)` (22); `      CALL VECML1(PDG,RN,PD,4)` (23); `      FO(:) = -RN(:) * ( DUD + POR / RKF * PDG ) * DET / 6.D0` (25); `      CALL VECML1(PG,RN,PB,4)` (27); `      FP(:,:) = DNDX(:,:) * PG * DET / 6.D0` (29); `!     ----- VELOCITY OF CENTER POINT -----` (31); `      VELE(:) = VELG(:)` (33); `      END` (35) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25: FO 계산식은 RKF로 나눈다. 이 파일에는 RKF=0 검사문이 없다.
