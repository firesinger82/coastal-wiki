---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/addset3.f
lines: 13
sha256: 97f7750a15f571fdcccf1f60d2d21c3c2464d3e11b1ffdd36afca5eec5b725b5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# addset3.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | ADDSET3의 인수와 INDEX(2,*)를 선언한다(1–3). 첫 항목의 시작 IS는 1이다(5–6). 그 외 시작은 이전 끝에 1을 더한다(7–9). IE는 현재 항목 끝으로 복사한다(11). 빈 줄과 END까지 포함한다. 원문: `      SUBROUTINE ADDSET3(IS,IE,INDEX,I)` (1); `      DIMENSION INDEX(2,*)` (3); `      IF( I == 1 ) THEN` (5); `        IS = 1` (6); `      ELSE` (7); `        IS = INDEX(2,I-1) + 1` (8); `      ENDIF` (9); `      IE = INDEX(2,I)` (11); `      END` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
