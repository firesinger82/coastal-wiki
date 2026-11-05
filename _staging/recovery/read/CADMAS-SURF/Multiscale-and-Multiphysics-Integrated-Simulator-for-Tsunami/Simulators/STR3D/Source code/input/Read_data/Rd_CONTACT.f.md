---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_CONTACT.f
lines: 11
sha256: e8a33890b6b14bc987647e66cf413397ee0fb109f358fdaa6cfecf20b88ff599
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_CONTACT.f — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | RD_CONTACT 선언과 IMPLICIT·RR(*)·문자열 선언을 포함한다(1–5). 7행 TOLA 조건이 참일 때만 CHAR(14:)를 자유 형식(list-directed format)으로 읽어 RR(13)에 저장한다(8). 조건 종료·주석·END를 포함한다(9–11). 원문: `      SUBROUTINE RD_CONTACT( RR, CHAR )` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      CHARACTER*80 CHAR` (4); `      DIMENSION RR(*)` (5); `      IF( CHAR(9:12) == 'TOLA' ) THEN` (7); `        READ(CHAR(14:),*) RR(13)` (8); `      ENDIF` (9); `      END` (11). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
