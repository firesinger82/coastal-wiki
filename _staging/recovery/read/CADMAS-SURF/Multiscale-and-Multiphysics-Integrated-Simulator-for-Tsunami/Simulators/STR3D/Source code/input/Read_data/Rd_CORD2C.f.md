---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_CORD2C.f
lines: 14
sha256: fdd69506c7d49021b05f48098b26da83d21485c463b8336728a8184431bc16a2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_CORD2C.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | RD_CORD2C의 IMPLICIT 선언과 CORD(9)·ICRDR(*) 배열을 포함한다(1–5). 해석: ICRD는 좌표계 구분값으로 보인다. 코드에서 ICRD는 1이다(7). 현재 CHAR에서 ID와 CORD(1:6)을 읽는다(9). ITI의 다음 레코드(record)에서 CORD(7:9)를 읽는다(10). ICRDR(ID)에 I_CORD를 등록한다(12). 원문: `      SUBROUTINE RD_CORD2C( ICRD, CORD, ICRDR, I_CORD, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION CORD(9), ICRDR(*)` (5); `      ICRD = 1` (7); `      READ(CHAR,'(BN,8X,I8,8X,6F8.0)') ID, CORD(1:6)` (9); `      READ(ITI,'(BN,8X,3F8.0)') CORD(7:9)` (10); `      ICRDR(ID) = I_CORD` (12); `      END` (14). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–10: 첫 카드(card)에서 ID 다음 8열은 8X로 건너뛴다. 다음 카드의 연속행 표식 검사 없이 CORD(7:9)를 읽는다.
