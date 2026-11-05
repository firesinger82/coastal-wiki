---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/beam0.f
lines: 23
sha256: 972e45e4deef5526b54fa372d773de346ea881f89422f888123fd55eb8d2ba9b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# beam0.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | BEAM0의 암시적 형과 S(3)·D(6) 배열 선언. ST>0이고 S(1)>=ST이면 IST=1로 설정하고 S·D를 0으로 만든 뒤 반환한다. 원문: `      SUBROUTINE BEAM0(IST,SY,S,D,E,ANU,ST,IYLD,HD)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION S(3),D(6)` (4); `      IF( ST > 0. ) THEN` (6); `        IF( S(1) >= ST ) THEN` (7); `          IST = 1` (8); `          S(:) = 0.` (9); `          D(:) = 0.` (10); `          RETURN` (11); `        ENDIF` (12); `      ENDIF` (13). [11-04 전수 검증 정정] |
| 15–23 | BEAM0 루틴 안. IYLD>0이고 DABS(S(1))>=SY이면 IST=2를 설정한다. SY에 DABS(S(1))을 대입하고 DBEAM2(D,E,ANU,HD)를 호출한다. 원문: `      IF( IYLD > 0 ) THEN` (15); `        IF( DABS(S(1)) >= SY ) THEN` (16); `          IST = 2` (17); `          SY = DABS(S(1))` (18); `          CALL DBEAM2(D,E,ANU,HD)` (19); `        ENDIF` (20); `      ENDIF` (21); `      END` (23). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–21: 해당 조건들을 만족하지 않는 경로에는 IST를 설정하는 문장이 없다.
