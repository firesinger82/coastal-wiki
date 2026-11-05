---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/module/mavbl.f90
lines: 9
sha256: 5e86ec0f803a50da969b0e4747c76ca9c2d2b37cad2d3f58f2ceddf345576917
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mavbl.f90 — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 종류 매개변수(kind)가 8인 정수 함수 MAVBL을 정의한다(1). `IMPLICIT NONE` (3)과 입력 MUSE 및 함수 MUSED의 kind가 8인 정수 형을 선언한다(5). MUSED()를 호출한 값을 MUSE에서 빼서 반환한다(7). 원문(연속행은 앞 문장에 이어짐): `INTEGER(8) FUNCTION MAVBL( MUSE )` (1); `  IMPLICIT NONE` (3); `  INTEGER(8) :: MUSE, MUSED` (5); `  MAVBL = MUSE - MUSED()` (7); `END` (9) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
