---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/Rd_SHELL.f
lines: 13
sha256: f42fa97fd4896a53c7db4c053c58e3ef659e24fd333ad61e659ac92b2c897afa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Rd_SHELL.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RD_SHELL의 80자 CHAR와 J_SHEL(10)을 선언한다(1–4). 6행 N<=6 조건은 현재 카드(card)에서 J_SHEL(1:2+N)을 읽는다(7). ELSE(8)는 현재 카드에서 J_SHEL(1:8), 다음 레코드(record)에서 J_SHEL(9:10)을 읽는다(9–10). 조건 종료·주석·END를 포함한다(11–13). 원문: `      SUBROUTINE RD_SHELL( J_SHEL, N, CHAR, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      DIMENSION J_SHEL(10)` (4); `      IF( N <= 6 ) THEN` (6); `        READ(CHAR,'(BN,8X,8I8)') J_SHEL(1:2+N)` (7); `      ELSE` (8); `        READ(CHAR,'(BN,8X,8I8)') J_SHEL(1:8)` (9); `        READ(ITI,'(BN,8X,2I8)') J_SHEL(9:10)` (10); `      ENDIF` (11); `      END` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–10: N>6 분기는 N의 값과 무관하게 총 열 개의 정수 성분을 읽는다.
