---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/Ct_TABLEM1.f
lines: 12
sha256: 41c1e41a8d78f518b94b556858d6aabc679aa115e8621151b99cfc57b90d04b0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Ct_TABLEM1.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 80자 CHAR를 선언한다(3). 무한 DO에서 다음 레코드를 읽어 TB_END가 반환한 항목 수 N을 N2에 누적한다(5–8). N<4이면 루프를 끝내고 반환한다(9–12). 원문: `      SUBROUTINE CT_TABLEM1( N2, ITI )` (1); `      CHARACTER*80 CHAR` (3); `      DO` (5); `        READ(ITI,'(A80)') CHAR` (6); `        CALL TB_END( N, CHAR )` (7); `        N2 = N2 + N` (8); `        IF( N < 4 ) EXIT` (9); `      ENDDO` (10); `      END` (12). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–9: 종료 판단은 TB_END의 반환값 N<4이다. TB_END 내부는 이번 대상에 포함하지 않았다.
