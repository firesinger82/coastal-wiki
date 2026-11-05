---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/ist_beam.f
lines: 15
sha256: c7f8e50786ec8fb7765c5d3de6e821401db4e00f104528a32fe38c6597b274da
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ist_beam.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | IST_BEAM은 아홉 위치의 상태 IST를 선택한다. 상태 0이면 BEAM0를 호출하고 상태 2이면 BEAM2를 호출한다. 호출 인수와 배열 범위는 아래 원문과 같다. 원문: `      SUBROUTINE IST_BEAM(IST,SY,S,D,E,ANU,ST,IYLD,HD)` (1)； `      IMPLICIT REAL*8(A-H,O-Z)` (3)； `      DIMENSION IST(9),SY(9),S(3,9),D(6,9)` (4)； `      DO J = 1, 9` (6)； `        SELECT CASE( IST(J) )` (7)； `        CASE( 0 )` (8)； `          CALL BEAM0(IST(J),SY(J),S(1,J),D(1,J),E,ANU,ST,IYLD,HD)` (9)； `        CASE( 2 )` (10)； `          CALL BEAM2(IST(J),SY(J),S(1,J),D(1,J),E,ANU,ST)` (11)； `        END SELECT` (12)； `      ENDDO` (13)； `      END` (15)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–12: SELECT CASE에는 0·2만 있으며 CASE DEFAULT는 없다.
