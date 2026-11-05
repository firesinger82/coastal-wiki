---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gnpfpn2.f
lines: 94
sha256: ad0301d837e4918f271b2ea23ab5439f2bd664cad7f5a008689a321e5179b178
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpfpn2.f — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | GNPFPN2는 VELG·VELE와 FI·FO·FP를 계산한다. 해석: 루틴 이름은 삼각기둥(prism) 요소를 가리키는 것으로 보인다. 해석: VELG·VELE는 유량 값으로 보인다. 실수 IMPLICIT·배열 선언을 아래에 적었다. VELG는 (3,NI,NJ)이다. RG·SG·TG 좌표와 WGI·WGJ 가중치의 DATA 문을 연속행 전체로 인용한다. 원문: `      SUBROUTINE GNPFPN2(FI,FO,FP,VELG,VELE,ND,NI,NJ,X,UD,UDD,P,PB,PD` (1); `     &                  ,POR,RKF,RK,RHOF,GRAV,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION RG(7,2),SG(7,2),TG(3,2),WGI(7,2),WGJ(3,2),RN(ND),X(3,ND)` (5); `     &         ,DNDX(3,ND),GRP(3),P(ND),UDDG(3),UDD(3,ND),VELG(3,NI,NJ)` (6); `     &         ,GRAV(3),FIG(ND),FI(ND),UD(3,ND),PD(ND),FO(ND),PB(ND)` (7); `     &         ,FP(3,ND),VELE(3)` (8); `      DATA RG / .5D0, .5D0, 0.D0, 4*0.D0,` (10); `     &  0.101286507323456D0, 0.797426985353087D0, 0.101286507323456D0,` (11); `     &  0.470142064105115D0, 0.470142064105115D0, 0.059715871789770D0,` (12); `     &  0.333333333333333D0 /` (13); `      DATA SG / 0.D0, .5D0, .5D0, 4*0.D0,` (14); `     &  0.101286507323456D0, 0.101286507323456D0, 0.797426985353087D0,` (15); `     &  0.059715871789770D0, 0.470142064105115D0, 0.470142064105115D0,` (16); `     &  0.333333333333333D0 /` (17); `      DATA TG / -.577350269189626D0, .577350269189626D0, 0.D0,` (18); `     &  -.774596669241483D0, 0.0D0, .774596669241483D0 /` (19); `      DATA WGI / 3*0.166666666666667D0, 4*0.D0,` (21); `     &  3*0.062969590272414D0, 3*0.066197076394253D0, 0.1125D0 /` (22); `      DATA WGJ / 2*1.D0, 0.D0,` (23); `     &  0.55555555555555556D0, 0.88888888888888889D0,` (24); `     &  0.55555555555555556D0 /` (25) [11-04 전수 검증 정정] |
| 27–69 | ND=6은 적분 표 ID=1, ELSE는 ID=2이다. FI·FO·FP를 0으로 초기화한다. J=1,NJ·I=1,NI에서 좌표·가중치를 읽고 SFNPN2·DERXPN2를 호출한다. AXB에 GRP와 UDDG를 각각 전달한다. VELG는 `-GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:)`에 RK를 곱한 값이다. ATXB에 FIG를 전달한다. FI에서 FIG*DET*WGT를 뺀다. VECML1에 DUD·PDG·PG를 각각 전달한다. FO에서 RN*(DUD+POR/RKF*PDG)*DET*WGT를 뺀다. FP에는 DNDX*PG*DET*WGT를 더한다. 해석: GRP·UDDG·GRAV·PG·POR는 각각 압력 경사·보간 가속도·중력·압력·공극률로 보인다. 식과 모든 호출 인수는 아래 원문과 같다. 원문: `      IF( ND == 6 ) THEN` (27); `        ID = 1` (28); `      ELSE` (29); `        ID = 2` (30); `      ENDIF` (31); `      FI(:) = 0.` (33); `      FO(:) = 0.` (34); `      FP(:,:) = 0.` (35); `      DO J = 1, NJ` (37); `        DO I = 1, NI` (38); `          R = RG(I,ID)` (40); `          S = SG(I,ID)` (41); `          T = TG(J,ID)` (42); `          WGT = WGI(I,ID)*WGJ(J,ID)` (44); `          CALL SFNPN2(RN,ND,R,S,T)` (46); `          CALL DERXPN2(DNDX,DET,ND,X,R,S,T,ITO)` (48); `          CALL AXB(GRP,DNDX,P,3,ND,1)` (50); `          CALL AXB(UDDG,UDD,RN,3,ND,1)` (51); `          VELG(:,I,J) = RK * ( -GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:) )` (53); `          CALL ATXB(FIG,DNDX,VELG(1,I,J),3,ND,1)` (55); `          FI(:) = FI(:) - FIG(:) * DET * WGT` (57); `          CALL VECML1(DUD,DNDX,UD,ND*3)` (59); `          CALL VECML1(PDG,RN,PD,ND)` (60); `          FO(:) = FO(:) - RN(:) * ( DUD + POR / RKF * PDG ) * DET * WGT` (62); `          CALL VECML1(PG,RN,PB,ND)` (64); `          FP(:,:) = FP(:,:) + DNDX(:,:) * PG * DET * WGT` (66); `        ENDDO` (68); `      ENDDO` (69) [11-04 전수 검증 정정] |
| 70–94 | 71행 주석은 중심점 속도(velocity) 계산을 뜻한다. ND=6이면 R=S=1/3·T=0으로 두고 SFNPN2·DERXPN2·AXB를 다시 호출한다. 해석: 이 호출은 형상함수(shape function)·미분·압력 경사·가속도 계산으로 보인다. 같은 식으로 VELE를 얻는다. ELSE는 VELG(:,7,2)를 복사한다. 원문: `!     ----- VELOCITY OF CENTER POINT -----` (71); `      IF( ND == 6 ) THEN` (73); `        R = 1.D0 / 3.D0` (75); `        S = 1.D0 / 3.D0` (76); `        T = 0.D0` (77); `        CALL SFNPN2(RN,ND,R,S,T)` (79); `        CALL DERXPN2(DNDX,DET,ND,X,R,S,T,ITO)` (81); `        CALL AXB(GRP,DNDX,P,3,ND,1)` (83); `        CALL AXB(UDDG,UDD,RN,3,ND,1)` (84); `        VELE(:) = RK * ( -GRP(:) + RHOF*GRAV(:) - RHOF*UDDG(:) )` (86); `      ELSE` (88); `        VELE(:) = VELG(:,7,2)` (90); `      ENDIF` (92); `      END` (94) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–31·37–44: ND가 적분 표를 선택하지만 NI·NJ 루프 상한은 인수로 받는다. 이 파일에는 NI·NJ와 ND의 대응 검사문이 없다.
- 62: FO 계산식은 RKF로 나눈다. 이 파일에는 RKF=0 검사문이 없다.
- 88–90: ND=6 이외의 중심값은 고정된 적분점 위치 (7,2)에서 복사한다.
