---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/corrface1.f
lines: 10
sha256: a05b7bfd8a40445a75b941368bee9e29b4d0eb388afa60046b7dec02f65305db
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# corrface1.f — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 루틴·암시적 자료형과 XYZ(3,4), RL(3), RN(3), DUG(3)을 선언한다(1–4). AREACD로 RL·RN·H를 구한 뒤 RMULT1에 RN과 -H를 전달하여 DUG를 계산한다(6–7). RETURN·END로 끝낸다(9–10). 원문: `      SUBROUTINE CORRFACE1(DUG,XYZ)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION XYZ(3,4),RL(3),RN(3),DUG(3)` (4); `      CALL AREACD(RL,RN,H,XYZ)` (6); `      CALL RMULT1(DUG,RN,-H,3)` (7). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
