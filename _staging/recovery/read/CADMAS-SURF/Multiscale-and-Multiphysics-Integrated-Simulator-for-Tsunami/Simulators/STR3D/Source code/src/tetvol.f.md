---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/tetvol.f
lines: 24
sha256: deb152070c6a4677f14351b5df9d873a994e018a416089522410b6d87298a28c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tetvol.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | TETVOL 입구와 IMPLICIT·배열 선언이다(1–4). XYZ의 네 열을 X1·Y1·Z1부터 X4·Y4·Z4까지 복사한다(6–17). 해석: 이 네 열을 사면체 꼭짓점 좌표로 볼 수 있다. 네 번째 꼭짓점을 기준으로 좌표차의 삼중곱(triple product)을 전개하고 음의 6분의 1을 곱해 V를 계산한다(19–21). 원문: `      SUBROUTINE TETVOL(XYZ,V)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XYZ(3,4)` (4); 주석: `C----&------------------------------------------------------------------` (5); `      X1 = XYZ(1,1)` (6); `      Y1 = XYZ(2,1)` (7); `      Z1 = XYZ(3,1)` (8); `      X2 = XYZ(1,2)` (9); `      Y2 = XYZ(2,2)` (10); `      Z2 = XYZ(3,2)` (11); `      X3 = XYZ(1,3)` (12); `      Y3 = XYZ(2,3)` (13); `      Z3 = XYZ(3,3)` (14); `      X4 = XYZ(1,4)` (15); `      Y4 = XYZ(2,4)` (16); `      Z4 = XYZ(3,4)` (17); `      V = -(   (X1-X4)*(Y2-Y4)*(Z3-Z4) + (X3-X4)*(Z2-Z4)*(Y1-Y4)`<br>`     &       + (X2-X4)*(Y3-Y4)*(Z1-Z4) - (Z1-Z4)*(Y2-Y4)*(X3-X4)`<br>`     &       - (X1-X4)*(Y3-Y4)*(Z2-Z4) - (Y1-Y4)*(X2-X4)*(Z3-Z4)  )/6.D0` (19–21); `      RETURN` (23); `      END` (24) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–21: V 계산식은 절댓값을 취하지 않는다.
