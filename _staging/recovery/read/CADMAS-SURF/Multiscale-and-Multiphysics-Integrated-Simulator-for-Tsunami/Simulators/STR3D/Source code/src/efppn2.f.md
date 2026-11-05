---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/efppn2.f
lines: 52
sha256: af2fbc8da3209cf75ef88fd297493920e4d2d228b444dfadf59f0eb86d2bfe4f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# efppn2.f — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | EFPPN2의 배열과 암시적 형(implicit typing)을 선언한다. DATA RG·SG·TG·WGI·WGJ는 두 열의 값을 저장한다. 해석: RG·SG·WGI는 평면 3·7점 적분의 좌표와 가중치에 해당한다. 해석: TG·WGJ는 축 방향 2·3점 적분의 좌표와 가중치에 해당한다. 원문: `      SUBROUTINE EFPPN2(FP,ND,NI,NJ,X,PB,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RG(7,2),SG(7,2),TG(3,2),WGI(7,2),WGJ(3,2),RN(ND),X(3,ND)`<br>`     &         ,DNDX(3,ND),PB(ND),FP(3,ND)` (4–5); `      DATA RG / .5D0, .5D0, 0.D0, 4*0.D0,`<br>`     &  0.101286507323456D0, 0.797426985353087D0, 0.101286507323456D0,`<br>`     &  0.470142064105115D0, 0.470142064105115D0, 0.059715871789770D0,`<br>`     &  0.333333333333333D0 /` (7–10); `      DATA SG / 0.D0, .5D0, .5D0, 4*0.D0,`<br>`     &  0.101286507323456D0, 0.101286507323456D0, 0.797426985353087D0,`<br>`     &  0.059715871789770D0, 0.470142064105115D0, 0.470142064105115D0,`<br>`     &  0.333333333333333D0 /` (11–14); `      DATA TG / -.577350269189626D0, .577350269189626D0, 0.D0,`<br>`     &  -.774596669241483D0, 0.0D0, .774596669241483D0 /` (15–16); `      DATA WGI / 3*0.166666666666667D0, 4*0.D0,`<br>`     &  3*0.062969590272414D0, 3*0.066197076394253D0, 0.1125D0 /` (18–19); `      DATA WGJ / 2*1.D0, 0.D0,`<br>`     &  0.55555555555555556D0, 0.88888888888888889D0,`<br>`     &  0.55555555555555556D0 /` (20–22). [11-04 전수 검증 정정] |
| 24–31 | 시작 시 1행 EFPPN2 루틴 안. ND가 6이면 표 열 ID=1을 사용하고 나머지는 ID=2를 사용한다. FP를 0으로 초기화한다. 원문: `      IF( ND == 6 ) THEN` (24); `        ID = 1` (25); `      ELSE` (26); `        ID = 2` (27); `      ENDIF` (28); `      FP(:,:) = 0.` (30). |
| 32–52 | 시작 시 1행 EFPPN2 루틴 안. J·I 루프에서 적분 좌표와 가중치 곱을 구한다. SFNPN2·DERXPN2·VECML1을 차례로 호출한다. DNDX*PG*DET*WGT를 FP에 더한다. 루프와 루틴 끝을 포함한다. 원문: `      DO J = 1, NJ` (32); `        DO I = 1, NI` (33); `          R = RG(I,ID)` (35); `          S = SG(I,ID)` (36); `          T = TG(J,ID)` (37); `          WGT = WGI(I,ID)*WGJ(J,ID)` (39); `          CALL SFNPN2(RN,ND,R,S,T)` (41); `          CALL DERXPN2(DNDX,DET,ND,X,R,S,T,ITO)` (43); `          CALL VECML1(PG,RN,PB,ND)` (45); `          FP(:,:) = FP(:,:) + DNDX(:,:) * PG * DET * WGT` (47); `        ENDDO` (49); `      ENDDO` (50); `      END` (52). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·32–39: 평면 표의 첫 번째 크기는 7이고 축 방향 표의 첫 번째 크기는 3이다. NI·NJ의 범위 검사는 없다.
