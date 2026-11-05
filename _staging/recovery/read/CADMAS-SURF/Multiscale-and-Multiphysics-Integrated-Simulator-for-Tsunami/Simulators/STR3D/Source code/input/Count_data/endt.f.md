---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Count_data/endt.f
lines: 14
sha256: ccb331765973c934383baaebd673d3ffff433dfd971704e8489f79766f7de374
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# endt.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 논리 함수(logical function) ENDT의 입력 길이는 8이다(1–3). 기본 반환값은 .FALSE.(5)이다. 7행 루프(loop)에서 길이 4의 부분문자열을 검사한다(8). 일치하면 .TRUE.를 반환한다(9–10). 끝 주석과 함수 종료를 포함한다(11–14). 원문: `      LOGICAL FUNCTION ENDT(CHAR)` (1); `      CHARACTER*8 CHAR` (3); `      ENDT = .FALSE.` (5); `      DO I = 1, 5` (7); `        IF( CHAR(I:I+3) == 'ENDT' ) THEN` (8); `          ENDT = .TRUE.` (9); `          RETURN` (10); `        ENDIF` (11); `      ENDDO` (12); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
