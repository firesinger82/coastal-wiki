---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gmtxpn2.f
lines: 65
sha256: 1393abeb9c76ca0986370b34d90acd278dd2019caacf6b573985549538c849be
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxpn2.f — 판독 구간 기록

구간은 1행부터 65행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | GMTXPN2는 결합 요소 행렬을 적분한다. 해석: 루틴 이름은 삼각기둥(prism) 요소를 가리키는 것으로 보인다. 실수 IMPLICIT와 배열 범위, NI·NJ·RG·SG·TG·WGI·WGJ의 DATA 문을 연속행 전체와 함께 인용한다. NI는 3·7, NJ는 2·3이다. RG·SG·TG와 WGI·WGJ의 상수는 아래 원문과 같다. 해석: RG·SG는 삼각면 좌표로 보인다. 해석: TG는 두께 방향 좌표로 보인다. 원문: `      SUBROUTINE GMTXPN2(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION NI(2),NJ(2),RG(7,2),SG(7,2),TG(3,2),WGI(7,2),WGJ(3,2)` (4); `     &         ,EKUP(ND3,ND),EKPP(ND,ND),ECPU(ND,ND3),ECPP(ND,ND)` (5); `     &         ,EMPU(ND,ND3),RN(ND),X(3,ND),DNDX(3,ND),RKUP(ND3,ND)` (6); `     &         ,RKPP(ND,ND),CPU(ND,ND3),CPP(ND,ND),RMPU(ND,ND3)` (7); `      DATA NI / 3, 7 /` (9); `      DATA NJ / 2, 3 /` (10); `      DATA RG / .5D0, .5D0, 0.D0, 4*0.D0,` (12); `     &  0.101286507323456D0, 0.797426985353087D0, 0.101286507323456D0,` (13); `     &  0.470142064105115D0, 0.470142064105115D0, 0.059715871789770D0,` (14); `     &  0.333333333333333D0 /` (15); `      DATA SG / 0.D0, .5D0, .5D0, 4*0.D0,` (16); `     &  0.101286507323456D0, 0.101286507323456D0, 0.797426985353087D0,` (17); `     &  0.059715871789770D0, 0.470142064105115D0, 0.470142064105115D0,` (18); `     &  0.333333333333333D0 /` (19); `      DATA TG / -.577350269189626D0, .577350269189626D0, 0.D0,` (20); `     &  -.774596669241483D0, 0.0D0, .774596669241483D0 /` (21); `      DATA WGI / 3*0.166666666666667D0, 4*0.D0,` (23); `     &  3*0.062969590272414D0, 3*0.066197076394253D0, 0.1125D0 /` (24); `      DATA WGJ / 2*1.D0, 0.D0,` (25); `     &  0.55555555555555556D0, 0.88888888888888889D0,` (26); `     &  0.55555555555555556D0 /` (27) [11-04 전수 검증 정정] |
| 29–65 | ND=6이면 적분 표 ID=1, ELSE는 ID=2이다. 다섯 결과 행렬을 0으로 초기화한다. J=1,NJ(ID) 및 I=1,NI(ID)에서 좌표·가중치 곱을 구한다. SFNPN2·DERXPN2·GMTX를 호출하고 WGT*DET를 곱한 다섯 행렬을 누적한다. 원문: `      IF( ND == 6 ) THEN` (29); `        ID = 1` (30); `      ELSE` (31); `        ID = 2` (32); `      ENDIF` (33); `      EKUP(:,:) = 0.` (35); `      EKPP(:,:) = 0.` (36); `      ECPU(:,:) = 0.` (37); `      ECPP(:,:) = 0.` (38); `      EMPU(:,:) = 0.` (39); `      DO J = 1, NJ(ID)` (41); `        DO I = 1, NI(ID)` (42); `          R = RG(I,ID)` (44); `          S = SG(I,ID)` (45); `          T = TG(J,ID)` (46); `          WGT = WGI(I,ID)*WGJ(J,ID)` (48); `          CALL SFNPN2(RN,ND,R,S,T)` (50); `          CALL DERXPN2(DNDX,DET,ND,X,R,S,T,ITO)` (52); `          CALL GMTX(RKUP,RKPP,CPU,CPP,RMPU,RN,DNDX,ND,ND3)` (54); `          EKUP(:,:) = EKUP(:,:) + RKUP(:,:)*WGT*DET` (56); `          EKPP(:,:) = EKPP(:,:) + RKPP(:,:)*WGT*DET` (57); `          ECPU(:,:) = ECPU(:,:) + CPU(:,:)*WGT*DET` (58); `          ECPP(:,:) = ECPP(:,:) + CPP(:,:)*WGT*DET` (59); `          EMPU(:,:) = EMPU(:,:) + RMPU(:,:)*WGT*DET` (60); `        ENDDO` (62); `      ENDDO` (63); `      END` (65) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 29–33: ND=6 이외의 모든 값은 두 번째 적분 표를 사용한다.
