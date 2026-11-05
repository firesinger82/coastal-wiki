---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/gmtxhx2_s.f
lines: 47
sha256: 5968621f8a5a9ce2d0e938a248f25b5a246323c341a1faf09e445151cc7f7d36
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gmtxhx2_s.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | GMTXHX2_S의 암시적 형·배열 선언과 DATA 가우스 점(Gauss point)·가중치 표. ND=8이면 NG=2, 그 밖에는 NG=3이다. 두 행렬을 0으로 초기화한다. 원문: `      SUBROUTINE GMTXHX2_S(EKPP,ECPP,ND,NN,X,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 연속문(4–5): `      DIMENSION WG(3,3),XG(3,3),EKPP(NN),ECPP(NN),RN(ND),X(3,ND)` <br> `     &         ,DNDX(3,ND),RKPP(NN),CPP(NN)`; 연속문(6–8): `      DATA XG / 3*0.0D0` <br> `     &        , -.577350269189626D0, .577350269189626D0, 0.0D0` <br> `     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /`; 연속문(9–12): `      DATA WG / 2.0D0, 2*0.0D0` <br> `     &        , 2*1.0D0, 0.0D0` <br> `     &        , 0.55555555555555556D0, 0.88888888888888889D0` <br> `     &        , 0.55555555555555556D0 /`; `      IF( ND == 8 ) THEN` (14); `        NG = 2` (15); `      ELSE` (16); `        NG = 3` (17); `      ENDIF` (18); `      EKPP(:) = 0.` (20); `      ECPP(:) = 0.` (21). |
| 23–47 | GMTXHX2_S 루틴 안. I·J·K의 세 적분 루프에서 가중치 곱을 계산한다. SFNHX2·DERXHX2에 RN·DNDX·DET를 전달한다. MATML에 DNDX·RN을 전달하여 RKPP·CPP를 얻는다. RKPP·CPP에 WGT*DET를 곱해 EKPP·ECPP에 각각 누적한다. 해석: RN은 형상 함수 값이고 DNDX는 공간 도함수로 읽힌다. 원문: `      DO I = 1, NG` (23); `      DO J = 1, NG` (24); `      DO K = 1, NG` (25); `        XG1 = XG(I,NG)` (27); `        XG2 = XG(J,NG)` (28); `        XG3 = XG(K,NG)` (29); `        WGT = WG(I,NG)*WG(J,NG)*WG(K,NG)` (31); `        CALL SFNHX2(XG1,XG2,XG3,ND,RN)` (33); `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X,ND,ITO)` (35); `        CALL MATML(RKPP,1,DNDX,3,DNDX,2,ND,ND,3)` (37); `        CALL MATML(CPP,1,RN,3,RN,2,ND,ND,1)` (38); `        EKPP(:) = EKPP(:) + RKPP(:)*WGT*DET` (40); `        ECPP(:) = ECPP(:) + CPP(:)*WGT*DET` (41); `      ENDDO` (43); `      ENDDO` (44); `      ENDDO` (45); `      END` (47). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
