---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/gmtxte2_s.f
lines: 35
sha256: 97cd0d659dfb2e2fb61db69d20f230e97b6ead94068372f2c1392735e515dea0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxte2_s.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | GMTXTE2_S의 암시적 형·배열 선언. DATA로 다섯 적분 점과 가중치를 정의한다. 마지막 가중치는 음수다. 두 행렬을 0으로 초기화한다. 원문: `      SUBROUTINE GMTXTE2_S(EKPP,ECPP,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 연속문(4–5): `      DIMENSION WG(5),RLG(4,5),EKPP(55),ECPP(55),RN(10),X(3,10)` <br> `     &         ,DNDX(3,10),RKPP(55),CPP(55)`; `      DATA WG  / 4*0.075D0, -0.133333333333333D0 /` (6); 연속문(7–16): `      DATA RLG /` <br> `     &    0.500000000000000D0, 0.166666666666667D0, 0.166666666666667D0` <br> `     &  , 0.166666666666667D0` <br> `     &  , 0.166666666666667D0, 0.500000000000000D0, 0.166666666666667D0` <br> `     &  , 0.166666666666667D0` <br> `     &  , 0.166666666666667D0, 0.166666666666667D0, 0.500000000000000D0` <br> `     &  , 0.166666666666667D0` <br> `     &  , 0.166666666666667D0, 0.166666666666667D0, 0.166666666666667D0` <br> `     &  , 0.500000000000000D0` <br> `     &  , 4*0.25D0 /`; `      EKPP(:) = 0.` (18); `      ECPP(:) = 0.` (19). |
| 21–35 | GMTXTE2_S 루틴 안. 다섯 점에서 SFNTE2·DERXTE2를 호출한다. MATML에 DNDX·RN을 전달하여 RKPP·CPP를 얻는다. RKPP·CPP에 WG(I)*DET를 곱해 EKPP·ECPP에 각각 누적한다. 해석: RN은 형상 함수 값이고 DNDX는 공간 도함수로 읽힌다. 원문: `      DO I = 1, 5` (21); `        CALL SFNTE2(RLG(1,I),RN)` (23); `        CALL DERXTE2(DNDX,DET,RLG(1,I),X,ITO)` (25); `        CALL MATML(RKPP,1,DNDX,3,DNDX,2,10,10,3)` (27); `        CALL MATML(CPP,1,RN,3,RN,2,10,10,1)` (28); `        EKPP(:) = EKPP(:) + RKPP(:)*WG(I)*DET` (30); `        ECPP(:) = ECPP(:) + CPP(:)*WG(I)*DET` (31); `      ENDDO` (33); `      END` (35). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6: DATA WG의 다섯 번째 가중치는 -0.133333333333333D0이다.
