---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/beam2.f
lines: 23
sha256: 73613173b888696324de569cfd2b5555c0f24265dc57a0d05953ac67c87e2a4a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# beam2.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | BEAM2의 암시적 형과 S(3)·D(6) 배열 선언. ST>0이고 S(1)>=ST이면 IST=1로 설정하고 S·D를 0으로 만든 뒤 반환한다. 원문: `      SUBROUTINE BEAM2(IST,SY,S,D,E,ANU,ST)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION S(3),D(6)` (4); `      IF( ST > 0. ) THEN` (6); `        IF( S(1) >= ST ) THEN` (7); `          IST = 1` (8); `          S(:) = 0.` (9); `          D(:) = 0.` (10); `          RETURN` (11); `        ENDIF` (12); `      ENDIF` (13). [11-04 전수 검증 정정] |
| 15–23 | BEAM2 루틴 안. DABS(S(1))>=SY이면 SY만 갱신한다. 그 밖에는 IST=0으로 설정하고 SY에 DABS(S(1))을 대입한 뒤 DBEAM0(D,E,ANU)를 호출한다. 원문: `      IF( DABS(S(1)) >= SY ) THEN` (15); `        SY = DABS(S(1))` (16); `      ELSE` (17); `        IST = 0` (18); `        SY = DABS(S(1))` (19); `        CALL DBEAM0(D,E,ANU)` (20); `      ENDIF` (21); `      END` (23). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–20: DABS(S(1))>=SY 참 분기에는 IST 대입이나 DBEAM0 호출이 없다. 두 분기 모두 SY에 DABS(S(1))을 대입한다. [11-04 전수 검증 정정]
