---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/bdfpn2.f
lines: 38
sha256: e5430d4a978cb1662e57050e56311955808e5b81c0806c6a8f07d5c9a944ce12
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bdfpn2.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | BDFPN2의 암시적 형·15절점 배열 선언. DATA로 삼각형 네 점·축방향 세 점과 가중치를 정의한다. 삼각형 마지막 가중치는 -0.28125D0이다. 원문: `      SUBROUTINE BDFPN2(FC,X,GRAV,R0,IGR,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 연속문(4–5): `      DIMENSION P(3,15),RG(4),SG(4),TG(3),X(3,15),XJI(3,3),H(15),VEC(3)` <br> `     &         ,GRAV(3),R0(3),FC(3,15),WGI(4),WGJ(3)`; `      DATA RG / 0.2D0, 0.6D0, 0.2D0, 0.333333333333333D0 /` (7); `      DATA SG / 0.2D0, 0.2D0, 0.6D0, 0.333333333333333D0 /` (8); `      DATA TG / -.774596669241483D0, 0.0D0, .774596669241483D0 /` (9); `      DATA WGI / 3*0.260416666666667D0, -0.28125D0 /` (11); 연속문(12–13): `      DATA WGJ / 0.55555555555555556D0, 0.88888888888888889D0` <br> `     &         , 0.55555555555555556D0 /`; `C-----------------------------------------------------------------------` (14). |
| 15–38 | BDFPN2 루틴 안. 3개 축방향·4개 삼각형 적분 점에서 DERPN2·JACOB3·SFNPN2를 15절점으로 호출한다. 각 절점에서 IGR=1이면 GRAV, 그 밖에는 X-R0를 택한다. H·벡터·행렬식·두 가중치의 곱을 FC에 누적한다. 원문: `      DO JG = 1, 3` (15); `        DO IG = 1, 4` (16); `          CALL DERPN2(P,15,RG(IG),SG(IG),TG(JG))` (18); `          CALL JACOB3(15,P,X,XJI,DET,ITO)` (19); `          CALL SFNPN2(H,15,RG(IG),SG(IG),TG(JG))` (21); `          DO I = 1, 15` (23); `            IF( IGR == 1 ) THEN` (25); `              VEC(:) = GRAV(:)` (26); `            ELSE` (27); `              VEC(:) = X(:,I) - R0(:)` (28); `            ENDIF` (29); `            FC(:,I) = FC(:,I) + H(I) * VEC(:) * DET * WGI(IG) * WGJ(JG)` (31); `          ENDDO` (33); `        ENDDO` (35); `      ENDDO` (36); `      END` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: DATA WGI의 네 번째 가중치는 -0.28125D0이다.
- 31: FC에 기존 값을 더해 누적한다. 이 파일에는 FC 전체 초기화문이 없다.
