---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gmtxte2.f
lines: 42
sha256: 1801605ffb2f97d9028da2482cfad0497e62dbd03e6b76b6f2d5812bf839005c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxte2.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | GMTXTE2는 결합 행렬을 구성한다. 해석: 루틴 이름과 배열 크기는 10절점 사면체(tetrahedron) 요소를 가리키는 것으로 보인다. 실수 IMPLICIT와 배열 범위를 아래에 인용한다. WG(5)와 RLG(4,5)를 DATA 연속문으로 설정한다. 해석: RLG는 사면체의 네 성분 체적좌표로 보인다. 원문: `      SUBROUTINE GMTXTE2(EKUP,EKPP,ECPU,ECPP,EMPU,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION WG(5),RLG(4,5),EKUP(30,10),EKPP(10,10),ECPU(10,30)` (4); `     &         ,ECPP(10,10),EMPU(10,30),RN(10),X(3,10),DNDX(3,10)` (5); `     &         ,RKUP(30,10),RKPP(10,10),CPU(10,30),CPP(10,10)` (6); `     &         ,RMPU(10,30)` (7); `      DATA WG  / 4*0.075D0, -0.133333333333333D0 /` (8); `      DATA RLG /` (9); `     &    0.500000000000000D0, 0.166666666666667D0, 0.166666666666667D0` (10); `     &  , 0.166666666666667D0` (11); `     &  , 0.166666666666667D0, 0.500000000000000D0, 0.166666666666667D0` (12); `     &  , 0.166666666666667D0` (13); `     &  , 0.166666666666667D0, 0.166666666666667D0, 0.500000000000000D0` (14); `     &  , 0.166666666666667D0` (15); `     &  , 0.166666666666667D0, 0.166666666666667D0, 0.166666666666667D0` (16); `     &  , 0.500000000000000D0` (17); `     &  , 4*0.25D0 /` (18) [11-04 전수 검증 정정] |
| 20–42 | 결과 행렬 다섯 개를 0으로 초기화한다. I=1,5에서 SFNTE2·DERXTE2·GMTX를 호출한다. 각 결과에 WG(I)*DET를 곱하여 누적하고 루틴을 끝낸다. 원문: `      EKUP(:,:) = 0.` (20); `      EKPP(:,:) = 0.` (21); `      ECPU(:,:) = 0.` (22); `      ECPP(:,:) = 0.` (23); `      EMPU(:,:) = 0.` (24); `      DO I = 1, 5` (26); `        CALL SFNTE2(RLG(1,I),RN)` (28); `        CALL DERXTE2(DNDX,DET,RLG(1,I),X,ITO)` (30); `        CALL GMTX(RKUP,RKPP,CPU,CPP,RMPU,RN,DNDX,10,30)` (32); `        EKUP(:,:) = EKUP(:,:) + RKUP(:,:)*WG(I)*DET` (34); `        EKPP(:,:) = EKPP(:,:) + RKPP(:,:)*WG(I)*DET` (35); `        ECPU(:,:) = ECPU(:,:) + CPU(:,:)*WG(I)*DET` (36); `        ECPP(:,:) = ECPP(:,:) + CPP(:,:)*WG(I)*DET` (37); `        EMPU(:,:) = EMPU(:,:) + RMPU(:,:)*WG(I)*DET` (38); `      ENDDO` (40); `      END` (42) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8: 다섯 번째 적분 가중치는 -0.133333333333333D0이다.
