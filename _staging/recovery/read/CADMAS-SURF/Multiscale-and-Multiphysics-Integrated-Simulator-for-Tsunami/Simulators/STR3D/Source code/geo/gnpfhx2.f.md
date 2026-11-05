---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gnpfhx2.f
lines: 80
sha256: 67b0756667dee10eb7754884f55733165d320c61e958071a541c24183e97a572
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpfhx2.f — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | GNPFHX2는 VELG·VELE와 FI·FO·FP를 계산한다. 해석: 루틴 이름은 육면체(hexahedron) 요소를 가리키는 것으로 보인다. 해석: VELG·VELE는 유량 값으로 보인다. 실수 IMPLICIT 및 배열 범위는 아래와 같다. VELG는 (3,NG,NG,NG), VELE는 (3)이다. 적분점·가중치 DATA를 연속행 전체로 인용한다. FI·FO·FP를 0으로 초기화한다. 원문: `      SUBROUTINE GNPFHX2(FI,FO,FP,VELG,VELE,ND,NG,X,UD,UDD,P,PB,PD,POR` (1); `     &                  ,RKF,RK,RHOF,GRAV,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION XG(3,3),WG(3,3),RN(ND),DNDX(3,ND),X(3,ND),GRP(3),P(ND)` (5); `     &         ,UDDG(3),UDD(3,ND),VELG(3,NG,NG,NG),GRAV(3),FIG(ND)` (6); `     &         ,FI(ND),UD(3,ND),PD(ND),FO(ND),PB(ND),FP(3,ND),VELE(3)` (7); `      DATA XG / 3*0.0D0` (9); `     &        , -.577350269189626D0, .577350269189626D0, 0.0D0` (10); `     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (11); `      DATA WG / 2.0D0, 2*0.0D0` (12); `     &        , 2*1.0D0, 0.0D0` (13); `     &        , 0.55555555555555556D0, 0.88888888888888889D0` (14); `     &        , 0.55555555555555556D0 /` (15); `      FI(:) = 0.` (17); `      FO(:) = 0.` (18); `      FP(:,:) = 0.` (19) [11-04 전수 검증 정정] |
| 21–56 | I·J·K의 1–NG 루프에서 적분 좌표와 가중치 곱을 구한다. SFNHX2·DERXHX2 호출 뒤 AXB에 GRP와 UDDG를 각각 전달한다. VELG는 `-GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:)`에 RK를 곱한 값이다. FI에서 FIG*DET*WGT를 뺀다. VECML1에 DUD·PDG·PG를 각각 전달한다. FO에서 RN*(DUD+POR/RKF*PDG)*DET*WGT를 뺀다. FP에는 DNDX*PG*DET*WGT를 더한다. 해석: GRP·UDDG·GRAV·PG·POR는 각각 압력 경사·보간 가속도·중력·압력·공극률로 보인다. 식과 모든 호출 인수는 아래 원문과 같다. 원문: `      DO I = 1, NG` (21); `      DO J = 1, NG` (22); `      DO K = 1, NG` (23); `        XG1 = XG(I,NG)` (25); `        XG2 = XG(J,NG)` (26); `        XG3 = XG(K,NG)` (27); `        WGT=WG(I,NG)*WG(J,NG)*WG(K,NG)` (29); `        CALL SFNHX2(XG1,XG2,XG3,ND,RN)` (31); `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X,ND,ITO)` (33); `        CALL AXB(GRP,DNDX,P,3,ND,1)` (35); `        CALL AXB(UDDG,UDD,RN,3,ND,1)` (36); `        VELG(:,I,J,K) = RK * ( -GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:) )` (38); `        CALL ATXB(FIG,DNDX,VELG(1,I,J,K),3,ND,1)` (40); `        FI(:) = FI(:) - FIG(:) * DET * WGT` (42); `        CALL VECML1(DUD,DNDX,UD,ND*3)` (44); `        CALL VECML1(PDG,RN,PD,ND)` (45); `        FO(:) = FO(:) - RN(:) * ( DUD + POR / RKF * PDG ) * DET * WGT` (47); `        CALL VECML1(PG,RN,PB,ND)` (49); `        FP(:,:) = FP(:,:) + DNDX(:,:) * PG * DET * WGT` (51); `      ENDDO` (53); `      ENDDO` (54); `      ENDDO` (55) [11-04 전수 검증 정정] |
| 57–80 | 중심점 속도(velocity) 계산 주석 뒤 ND=8 분기에서 좌표를 모두 0으로 두고 SFNHX2·DERXHX2·AXB를 다시 호출한다. 같은 유량식으로 VELE를 계산한다. ELSE는 VELG(:,2,2,2)를 VELE에 복사한다. 원문: `!     ----- VELOCITY OF CENTER POINT -----` (57); `      IF( ND == 8 ) THEN` (59); `        XG1 = 0.` (61); `        XG2 = 0.` (62); `        XG3 = 0.` (63); `        CALL SFNHX2(XG1,XG2,XG3,ND,RN)` (65); `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X,ND,ITO)` (67); `        CALL AXB(GRP,DNDX,P,3,ND,1)` (69); `        CALL AXB(UDDG,UDD,RN,3,ND,1)` (70); `        VELE(:) = RK * ( -GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:) )` (72); `      ELSE` (74); `        VELE(:) = VELG(:,2,2,2)` (76); `      ENDIF` (78); `      END` (80) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47: FO 계산식은 RKF로 나눈다. 이 루틴에는 RKF=0 검사문이 없다.
- 5–15·21–29: 적분 표의 각 차원 크기는 3이며 루프 상한은 인수 NG이다. 이 파일에는 NG의 범위 검사문이 없다.
- 74–76: ND=8 이외의 분기는 VELG(:,2,2,2)를 중심점 값으로 사용한다.
