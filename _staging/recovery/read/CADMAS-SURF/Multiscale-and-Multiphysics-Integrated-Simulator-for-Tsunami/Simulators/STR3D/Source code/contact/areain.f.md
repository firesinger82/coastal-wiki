---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/areain.f
lines: 15
sha256: 3ca4ba365d25d84965906e59da3cdf73bda0d9b7ee27ee35a945e483a2e3c38d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# areain.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 논리 함수 AREAIN의 RL(3)을 선언한다(1–4). 세 좌표 각각이 열린 구간 -TOL < RL(i) < 1.+TOL에 있으면 .TRUE., 아니면 .FALSE.를 반환한다(6–12). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      LOGICAL FUNCTION AREAIN(RL,TOL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RL(3)` (4); `C----&------------------------------------------------------------------` (5); `      IF( RL(1) .GT. -TOL .AND. RL(1) .LT. 1.+TOL .AND.` (6); `     &    RL(2) .GT. -TOL .AND. RL(2) .LT. 1.+TOL .AND.` (7); `     &    RL(3) .GT. -TOL .AND. RL(3) .LT. 1.+TOL ) THEN` (8); `        AREAIN=.TRUE.` (9); `      ELSE` (10); `        AREAIN=.FALSE.` (11); `      ENDIF` (12); `      RETURN` (14); `      END` (15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–8: 경계 비교는 모두 엄격 부등호이다. RL 합이 1인지 검사하는 문장은 이 함수에 없다.
