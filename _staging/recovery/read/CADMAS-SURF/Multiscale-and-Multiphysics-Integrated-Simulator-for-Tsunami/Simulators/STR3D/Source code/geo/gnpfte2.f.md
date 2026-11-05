---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gnpfte2.f
lines: 55
sha256: 4e5af7d0e5c84d08a7603c8db5cfb1055b57b3f11da4c9d0d73a25a32db00da1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpfte2.f — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | GNPFTE2는 VELG·VELE와 FI·FO·FP를 계산한다. 해석: 루틴 이름과 배열 크기는 10절점 사면체(tetrahedron)를 가리키는 것으로 보인다. 해석: VELG·VELE는 유량(flux)으로 보인다. 실수 IMPLICIT·배열 범위를 아래에 인용한다. 적분점 5개의 WG·RLG DATA 문은 연속행 전체로 옮겼다. FI·FO·FP는 0으로 초기화한다. 원문: `      SUBROUTINE GNPFTE2(FI,FO,FP,VELG,VELE,X,UD,UDD,P,PB,PD,POR,RKF,RK` (1); `     &                  ,RHOF,GRAV,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION WG(5),RLG(4,5),RN(10),DNDX(3,10),X(3,10),GRP(3),P(10)` (5); `     &         ,UDDG(3),UDD(3,10),VELG(3,5),GRAV(3),FIG(10),FI(10)` (6); `     &         ,UD(3,10),PD(10),FO(10),PB(10),FP(3,10),VELE(3)` (7); `      DATA WG  / 4*0.075D0, -0.133333333333333D0 /` (9); `      DATA RLG /` (10); `     &    0.500000000000000D0, 0.166666666666667D0, 0.166666666666667D0` (11); `     &  , 0.166666666666667D0` (12); `     &  , 0.166666666666667D0, 0.500000000000000D0, 0.166666666666667D0` (13); `     &  , 0.166666666666667D0` (14); `     &  , 0.166666666666667D0, 0.166666666666667D0, 0.500000000000000D0` (15); `     &  , 0.166666666666667D0` (16); `     &  , 0.166666666666667D0, 0.166666666666667D0, 0.166666666666667D0` (17); `     &  , 0.500000000000000D0` (18); `     &  , 4*0.25D0 /` (19); `      FI(:) = 0.` (21); `      FO(:) = 0.` (22); `      FP(:,:) = 0.` (23) [11-04 전수 검증 정정] |
| 25–55 | I=1,5에서 SFNTE2·DERXTE2·AXB를 호출한다. VELG는 `-GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:)`에 RK를 곱한 값이다. FI에서 FIG*DET*WG(I)를 뺀다. FO에서 RN*(DUD+POR/RKF*PDG)*DET*WG(I)를 뺀다. FP에는 DNDX*PG*DET*WG(I)를 더한다. 해석: RN·DNDX·GRP·UDDG·GRAV·POR는 각각 형상함수·공간 미분·압력 경사·보간 가속도·중력·공극률로 보인다. 루프 뒤 중심점 값 VELE에 VELG(:,5)를 복사한다. 원문: `      DO I = 1, 5` (25); `        CALL SFNTE2(RLG(1,I),RN)` (27); `        CALL DERXTE2(DNDX,DET,RLG(1,I),X,ITO)` (29); `        CALL AXB(GRP,DNDX,P,3,10,1)` (31); `        CALL AXB(UDDG,UDD,RN,3,10,1)` (32); `        VELG(:,I) = RK * ( -GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:) )` (34); `        CALL ATXB(FIG,DNDX,VELG(1,I),3,10,1)` (36); `        FI(:) = FI(:) - FIG(:) * DET * WG(I)` (38); `        CALL VECML1(DUD,DNDX,UD,30)` (40); `        CALL VECML1(PDG,RN,PD,10)` (41); `        FO(:) = FO(:) - RN(:) * ( DUD + POR / RKF * PDG ) * DET * WG(I)` (43); `        CALL VECML1(PG,RN,PB,10)` (45); `        FP(:,:) = FP(:,:) + DNDX(:,:) * PG * DET * WG(I)` (47); `      ENDDO` (49); `!     ----- VELOCITY OF CENTER POINT -----` (51); `      VELE(:) = VELG(:,5)` (53); `      END` (55) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9: 다섯 번째 적분 가중치는 음수 -0.133333333333333D0이다.
- 43: FO 계산식은 RKF로 나눈다. 이 파일에는 RKF=0 검사문이 없다.
