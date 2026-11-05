---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_GRAV.f
lines: 11
sha256: 409fa3b1b5bb1fd0c115411d55060bc857bcf15e69f3080697f2ed52893a6e40
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_GRAV.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RD_GRAV 선언과 IMPLICIT·GRAV(3)을 포함한다(1–5). 카드(card)에서 IGRV, 배율 A와 세 벡터(vector) 성분을 읽는다(7). 9행 식으로 각 성분에 A를 곱한다. 끝 주석과 END를 포함한다(10–11). 원문: `      SUBROUTINE RD_GRAV( IGRV, GRAV, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION GRAV(3)` (5); `      READ(CHAR,'(BN,8X,I8,8X,4F8.0)') IGRV, A, GRAV(:)` (7); `      GRAV(:) = A * GRAV(:)` (9); `      END` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
