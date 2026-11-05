---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_PBAR.f
lines: 26
sha256: 29553798df949fb47ec5733ba604b3a8730b08babaacb10aa58048685fa7d214
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_PBAR.f — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | RD_PBAR의 IMPLICIT와 J_PBAR(3)·R_PBAR(6)을 선언한다(1–6). 최초 카드(card)에서 정수 두 성분과 실수 네 성분을 읽는다(8). 다음 두 레코드(record)에 대해 각각 12·19행 조건을 검사한다. 앞 8자가 공백이 아니면 BACKSPACE 후 반환한다(13–14·20–21). 두 레코드가 모두 공백 표식이면 두 번째 레코드에서 R_PBAR(5:6)를 읽는다(24). 원문: `      SUBROUTINE RD_PBAR( J_PBAR, R_PBAR, CHAR, ITI )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      CHARACTER*8 BLK /'        '/` (5); `      DIMENSION J_PBAR(3), R_PBAR(6)` (6); `      READ(CHAR,'(BN,8X,2I8,4F8.0)') J_PBAR(1:2), R_PBAR(1:4)` (8); `      READ(ITI,'(A80)') CHAR` (10); `      IF( CHAR(1:8) /= BLK ) THEN` (12); `        BACKSPACE( ITI )` (13); `        RETURN` (14); `      ENDIF` (15); `      READ(ITI,'(A80)') CHAR` (17); `      IF( CHAR(1:8) /= BLK ) THEN` (19); `        BACKSPACE( ITI )` (20); `        RETURN` (21); `      ENDIF` (22); `      READ(CHAR,'(BN,8X,2F8.0)') R_PBAR(5:6)` (24); `      END` (26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–24: 첫 번째 공백 연속행은 읽은 뒤 필드 판독 없이 건너뛴다.
- 6·8·24: J_PBAR(3)은 이 루틴에서 대입하지 않는다.
