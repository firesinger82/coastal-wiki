---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/gmtxpn2_s.f
lines: 59
sha256: bd3d26508e7d9ce0cdbda976acda5364c766001fa51256f9a59192a443a27e54
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxpn2_s.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | GMTXPN2_S의 암시적 형·배열 선언과 DATA 적분 점·가중치 표. ND=6이면 ID=1, 그 밖에는 ID=2를 설정한다. 해석: NI·NJ는 각각 삼각형·축방향 적분 점 수로 읽힌다. 두 행렬을 0으로 초기화한다. 원문: `      SUBROUTINE GMTXPN2_S(EKPP,ECPP,ND,NN,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 연속문(4–6): `      DIMENSION NI(2),NJ(2),RG(7,2),SG(7,2),TG(3,2),WGI(7,2),WGJ(3,2)` <br> `     &         ,EKPP(NN),ECPP(NN),RN(ND),X(3,ND),DNDX(3,ND),RKPP(NN)` <br> `     &         ,CPP(NN)`; `      DATA NI / 3, 7 /` (8); `      DATA NJ / 2, 3 /` (9); 연속문(11–14): `      DATA RG / .5D0, .5D0, 0.D0, 4*0.D0,` <br> `     &  0.101286507323456D0, 0.797426985353087D0, 0.101286507323456D0,` <br> `     &  0.470142064105115D0, 0.470142064105115D0, 0.059715871789770D0,` <br> `     &  0.333333333333333D0 /`; 연속문(15–18): `      DATA SG / 0.D0, .5D0, .5D0, 4*0.D0,` <br> `     &  0.101286507323456D0, 0.101286507323456D0, 0.797426985353087D0,` <br> `     &  0.059715871789770D0, 0.470142064105115D0, 0.470142064105115D0,` <br> `     &  0.333333333333333D0 /`; 연속문(19–20): `      DATA TG / -.577350269189626D0, .577350269189626D0, 0.D0,` <br> `     &  -.774596669241483D0, 0.0D0, .774596669241483D0 /`; 연속문(22–23): `      DATA WGI / 3*0.166666666666667D0, 4*0.D0,` <br> `     &  3*0.062969590272414D0, 3*0.066197076394253D0, 0.1125D0 /`; 연속문(24–26): `      DATA WGJ / 2*1.D0, 0.D0,` <br> `     &  0.55555555555555556D0, 0.88888888888888889D0,` <br> `     &  0.55555555555555556D0 /`; `      IF( ND == 6 ) THEN` (28); `        ID = 1` (29); `      ELSE` (30); `        ID = 2` (31); `      ENDIF` (32); `      EKPP(:) = 0.` (34); `      ECPP(:) = 0.` (35). [11-04 전수 검증 정정] |
| 37–59 | GMTXPN2_S 루틴 안. NJ(ID)·NI(ID)의 두 루프에서 좌표와 곱 가중치를 취한다. SFNPN2·DERXPN2를 호출한다. MATML에 DNDX·RN을 전달하여 RKPP·CPP를 얻는다. RKPP·CPP에 WGT*DET를 곱해 EKPP·ECPP에 각각 누적한다. 해석: RN은 형상 함수 값이고 DNDX는 공간 도함수이며 DET는 야코비안 행렬식으로 읽힌다. 원문: `      DO J = 1, NJ(ID)` (37); `        DO I = 1, NI(ID)` (38); `          R = RG(I,ID)` (40); `          S = SG(I,ID)` (41); `          T = TG(J,ID)` (42); `          WGT = WGI(I,ID)*WGJ(J,ID)` (44); `          CALL SFNPN2(RN,ND,R,S,T)` (46); `          CALL DERXPN2(DNDX,DET,ND,X,R,S,T,ITO)` (48); `          CALL MATML(RKPP,1,DNDX,3,DNDX,2,ND,ND,3)` (50); `          CALL MATML(CPP,1,RN,3,RN,2,ND,ND,1)` (51); `          EKPP(:) = EKPP(:) + RKPP(:)*WGT*DET` (53); `          ECPP(:) = ECPP(:) + CPP(:)*WGT*DET` (54); `        ENDDO` (56); `      ENDDO` (57); `      END` (59). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
