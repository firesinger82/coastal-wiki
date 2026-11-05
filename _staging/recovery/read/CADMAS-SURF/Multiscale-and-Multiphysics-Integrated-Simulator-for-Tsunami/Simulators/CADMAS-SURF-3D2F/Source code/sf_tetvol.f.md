---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_tetvol.f
lines: 25
sha256: d46910375e9e440af93f2b145a4b54c609a88f4dedd22eee20e571e0efb89dfa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_tetvol.f — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 암시적 실수·XYZ(3,4)를 선언한다. 해석: 19–21행 식은 부호 있는 사면체 체적을 계산한다. 네 꼭짓점 좌표를 지역 변수로 복사한다(1–17). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE SF_TETVOL(XYZ,V)` (1)<br>`C` (2)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION XYZ(3,4)` (4)<br>`C----&------------------------------------------------------------------` (5)<br>`      X1 = XYZ(1,1)` (6)<br>`      Y1 = XYZ(2,1)` (7)<br>`      Z1 = XYZ(3,1)` (8)<br>`      X2 = XYZ(1,2)` (9)<br>`      Y2 = XYZ(2,2)` (10)<br>`      Z2 = XYZ(3,2)` (11)<br>`      X3 = XYZ(1,3)` (12)<br>`      Y3 = XYZ(2,3)` (13)<br>`      Z3 = XYZ(3,3)` (14)<br>`      X4 = XYZ(1,4)` (15)<br>`      Y4 = XYZ(2,4)` (16)<br>`      Z4 = XYZ(3,4)` (17)<br>`C` (18) [11-04 전수 검증 정정] |
| 19–25 | 시작 시 1행 루틴 안. 여섯 삼중곱 체적 식의 연속행을 적는다(19–21). 23행은 주석 처리된 음의 체적 오류 호출이다. 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      V = -(   (X1-X4)*(Y2-Y4)*(Z3-Z4) + (X3-X4)*(Z2-Z4)*(Y1-Y4)` (19)<br>`     &       + (X2-X4)*(Y3-Y4)*(Z1-Z4) - (Z1-Z4)*(Y2-Y4)*(X3-X4)` (20)<br>`     &       - (X1-X4)*(Y3-Y4)*(Z2-Z4) - (Y1-Y4)*(X2-X4)*(Z3-Z4)  )/6.D0` (21)<br>`C` (22)<br>`C    IF( V < 0.D0 ) CALL VF_A2ERR('SF_TETVOL','P.G ERROR.')` (23)<br>`C` (24)<br>`      END` (25) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23: V<0의 VF_A2ERR 호출은 C로 시작하는 주석이다.
