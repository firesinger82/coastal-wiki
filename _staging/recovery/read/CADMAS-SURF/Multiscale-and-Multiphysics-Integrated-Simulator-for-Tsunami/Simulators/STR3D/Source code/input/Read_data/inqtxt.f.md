---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Read_data/inqtxt.f
lines: 15
sha256: 48120e36293c914a5bdbb001529bad7b90720665b861235b3e29ce90c7d06985
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# inqtxt.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 논리 함수(logical function) INQTXT는 CHARACTER*8 CHAR와 CHARACTER TEXT를 선언한다(1–4). 기본 반환값은 .FALSE.이다(6). 8행 루프(loop)가 N자 부분문자열과 TEXT(1:N)을 비교한다(9). 일치하면 .TRUE.로 반환한다(10–11). 루프 종료·주석·END를 포함한다(12–15). 원문: `      LOGICAL FUNCTION INQTXT( CHAR, TEXT, N )` (1); `      CHARACTER*8 CHAR` (3); `      CHARACTER TEXT` (4); `      INQTXT = .FALSE.` (6); `      DO I = 1, 9 - N` (8); `        IF( CHAR(I:I+N-1) == TEXT(1:N) ) THEN` (9); `          INQTXT = .TRUE.` (10); `          RETURN` (11); `        ENDIF` (12); `      ENDDO` (13); `      END` (15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·9: TEXT 선언에는 길이 지정이 없어 길이는 1이다. 비교식에서는 TEXT(1:N)을 사용한다.
- 8–9: N에 대한 1–8 범위 검사는 이 함수에 없다.
