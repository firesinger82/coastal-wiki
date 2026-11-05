---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/thru.f
lines: 14
sha256: 9e441d7e4d548bc242f24ad05a2c47cba0afb559c335fe36ff41e2548f27e255
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# thru.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 논리 함수 THRU는 8자 CHAR를 선언한다(1–3). 기본 반환값은 .FALSE.이다(5). 7행 루프(loop)는 길이 4의 부분문자열을 검사한다(8). THRU와 일치하면 .TRUE.로 반환한다(9–10). 루프 종료·주석·END를 포함한다(11–14). 원문: `      LOGICAL FUNCTION THRU(CHAR)` (1); `      CHARACTER*8 CHAR` (3); `      THRU = .FALSE.` (5); `      DO I = 1, 5` (7); `        IF( CHAR(I:I+3) == 'THRU' ) THEN` (8); `          THRU = .TRUE.` (9); `          RETURN` (10); `        ENDIF` (11); `      ENDDO` (12); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
