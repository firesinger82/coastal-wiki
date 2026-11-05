---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_RFORCE.f
lines: 11
sha256: d3b1a1a7b424ec555bf4ab7019cbef6549c44414071525445dd157f7c5d80b16
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_RFORCE.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RD_RFORCE의 IMPLICIT·IRFC(2)·RFRC(3) 선언을 포함한다(1–5). 카드(card)에서 정수 두 값·배율 A·벡터(vector) 세 성분을 읽는다(7). 9행 식으로 RFRC 전체에 A를 곱한다. 끝 주석·END를 포함한다(10–11). 원문: `      SUBROUTINE RD_RFORCE( IRFC, RFRC, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION IRFC(2), RFRC(3)` (5); `      READ(CHAR,'(BN,8X,2I8,8X,4F8.0)') IRFC(:), A, RFRC(:)` (7); `      RFRC(:) = A * RFRC(:)` (9); `      END` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
