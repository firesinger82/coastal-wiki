---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gmtxhx2.f
lines: 54
sha256: 561df7648d77de47f897689d0f494c8dbe93105e02bc5dc4b099012fd329605c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxhx2.f — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | GMTXHX2는 결합 요소 행렬을 적분한다. 해석: 루틴 이름은 육면체(hexahedron) 요소를 가리키는 것으로 보인다. 실수 IMPLICIT·배열 선언과 적분점 XG·가중치 WG의 DATA 연속문을 아래에 그대로 적었다. ND=8이면 방향별 적분점 수 NG=2, ELSE는 NG=3이다. 원문: `      SUBROUTINE GMTXHX2(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION WG(3,3),XG(3,3),EKUP(ND3,ND),EKPP(ND,ND),ECPU(ND,ND3)` (4); `     &         ,ECPP(ND,ND),EMPU(ND,ND3),RN(ND),X(3,ND),DNDX(3,ND)` (5); `     &         ,RKUP(ND3,ND),RKPP(ND,ND),CPU(ND,ND3),CPP(ND,ND)` (6); `     &         ,RMPU(ND,ND3)` (7); `      DATA XG / 3*0.0D0` (8); `     &        , -.577350269189626D0, .577350269189626D0, 0.0D0` (9); `     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (10); `      DATA WG / 2.0D0, 2*0.0D0` (11); `     &        , 2*1.0D0, 0.0D0` (12); `     &        , 0.55555555555555556D0, 0.88888888888888889D0` (13); `     &        , 0.55555555555555556D0 /` (14); `      IF( ND == 8 ) THEN` (16); `        NG = 2` (17); `      ELSE` (18); `        NG = 3` (19); `      ENDIF` (20) [11-04 전수 검증 정정] |
| 22–54 | 다섯 결과 행렬을 0으로 초기화한다. I·J·K의 1–NG 중첩 루프에서 적분 좌표와 세 방향 가중치 곱을 얻는다. SFNHX2에 RN을 전달한다. DERXHX2에 DNDX·DET를 전달한다. 해석: RN은 형상함수(shape function)로 보인다. 해석: DNDX·DET는 공간 미분·행렬식(determinant)으로 보인다. GMTX의 결과에 WGT*DET를 곱하여 다섯 행렬에 누적한다. 원문: `      EKUP(:,:) = 0.` (22); `      EKPP(:,:) = 0.` (23); `      ECPU(:,:) = 0.` (24); `      ECPP(:,:) = 0.` (25); `      EMPU(:,:) = 0.` (26); `      DO I = 1, NG` (28); `      DO J = 1, NG` (29); `      DO K = 1, NG` (30); `        XG1 = XG(I,NG)` (32); `        XG2 = XG(J,NG)` (33); `        XG3 = XG(K,NG)` (34); `        WGT = WG(I,NG)*WG(J,NG)*WG(K,NG)` (36); `        CALL SFNHX2(XG1,XG2,XG3,ND,RN)` (38); `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X,ND,ITO)` (40); `        CALL GMTX(RKUP,RKPP,CPU,CPP,RMPU,RN,DNDX,ND,ND3)` (42); `        EKUP(:,:) = EKUP(:,:) + RKUP(:,:)*WGT*DET` (44); `        EKPP(:,:) = EKPP(:,:) + RKPP(:,:)*WGT*DET` (45); `        ECPU(:,:) = ECPU(:,:) + CPU(:,:)*WGT*DET` (46); `        ECPP(:,:) = ECPP(:,:) + CPP(:,:)*WGT*DET` (47); `        EMPU(:,:) = EMPU(:,:) + RMPU(:,:)*WGT*DET` (48); `      ENDDO` (50); `      ENDDO` (51); `      ENDDO` (52); `      END` (54) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–20: ND=8 이외의 모든 값은 NG=3으로 처리한다. 별도 ND 유효성 검사문은 없다.
