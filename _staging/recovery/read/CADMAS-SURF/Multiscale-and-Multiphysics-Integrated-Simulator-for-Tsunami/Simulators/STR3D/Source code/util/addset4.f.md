---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/addset4.f
lines: 13
sha256: 3562220a04299c13643af04276a85762b16fe0772d7f427533d2c084c2a5ba1f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# addset4.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | ADDSET4의 인수와 INDEX(*)를 선언한다(1–3). 첫 항목의 시작 IS는 1이다(5–6). 그 외 시작은 이전 INDEX에 1을 더한다(7–9). IE는 INDEX(I)로 복사한다(11). 빈 줄과 END까지 포함한다. 원문: `      SUBROUTINE ADDSET4(IS,IE,INDEX,I)` (1); `      DIMENSION INDEX(*)` (3); `      IF( I == 1 ) THEN` (5); `        IS = 1` (6); `      ELSE` (7); `        IS = INDEX(I-1) + 1` (8); `      ENDIF` (9); `      IE = INDEX(I)` (11); `      END` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
