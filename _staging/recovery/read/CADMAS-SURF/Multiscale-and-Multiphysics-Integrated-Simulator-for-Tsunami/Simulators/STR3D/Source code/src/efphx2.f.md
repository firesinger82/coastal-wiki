---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/efphx2.f
lines: 39
sha256: 365c81567613c11a95231e1bc0633c2c462c976d2a83d28abf9c04da137dec15
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# efphx2.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | EFPHX2의 배열과 암시적 형(implicit typing)을 선언한다. 해석: DATA XG·WG는 1·2·3점 가우스 적분의 좌표와 가중치 표에 해당한다. 원문: `      SUBROUTINE EFPHX2(FP,ND,NG,X,PB,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XG(3,3),WG(3,3),RN(ND),DNDX(3,ND),X(3,ND),PB(ND)`<br>`     &         ,FP(3,ND)` (4–5); `      DATA XG / 3*0.0D0`<br>`     &        , -.577350269189626D0, .577350269189626D0, 0.0D0`<br>`     &        , -.774596669241483D0, 0.0D0, .774596669241483D0 /` (7–9); `      DATA WG / 2.0D0, 2*0.0D0`<br>`     &        , 2*1.0D0, 0.0D0`<br>`     &        , 0.55555555555555556D0, 0.88888888888888889D0`<br>`     &        , 0.55555555555555556D0 /` (10–13). [11-04 전수 검증 정정] |
| 15–26 | 시작 시 1행 EFPHX2 루틴 안. FP를 0으로 초기화한다. 각 방향 NG개 적분점을 순회하는 I·J·K 루프에서 좌표와 세 가중치의 곱을 계산한다. 원문: `      FP(:,:) = 0.` (15); `      DO I = 1, NG` (17); `      DO J = 1, NG` (18); `      DO K = 1, NG` (19); `        XG1 = XG(I,NG)` (21); `        XG2 = XG(J,NG)` (22); `        XG3 = XG(K,NG)` (23); `        WGT=WG(I,NG)*WG(J,NG)*WG(K,NG)` (25). |
| 27–39 | 시작 시 17행 `      DO I = 1, NG`, 18행 `      DO J = 1, NG`, 19행 `      DO K = 1, NG` 안이다. K·J·I 루프는 각각 35·36·37행 ENDDO에서 닫힌다. SFNHX2와 DERXHX2를 차례로 호출한다. 해석: SFNHX2는 형상함수를 계산한다. DERXHX2의 출력 DNDX·DET 설명은 `derxhx2.f:3–4`에 있다. VECML1에 RN·PB를 전달하여 PG를 받고 DNDX*PG*DET*WGT를 FP에 누적한다. 루프와 루틴 끝을 포함한다. 원문: `        CALL SFNHX2(XG1,XG2,XG3,ND,RN)` (27); `        CALL DERXHX2(DNDX,DET,XG1,XG2,XG3,X,ND,ITO)` (29); `        CALL VECML1(PG,RN,PB,ND)` (31); `        FP(:,:) = FP(:,:) + DNDX(:,:) * PG * DET * WGT` (33); `      ENDDO` (35); `      ENDDO` (36); `      ENDDO` (37); `      END` (39). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·17–25: XG·WG의 크기는 3×3이다. 이 파일에는 NG 범위 검사가 없다.
