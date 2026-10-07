---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_70.md
lines: 48
sha256: a69cbbe50dfbd398d6a85ea34697f8465127f0e15cec11a6697b8fdecbfe8f2d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_70.md — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–30 | C70 CONTROLS FOR WRITING ASCII OR BINARY DUMP FILES / 형식·시각 — 덤프 파일(dump file)의 활성화 조건과 스케일 변환(scaling)을 적용한 ASCII 정수·16비트 이진 정수, 스케일 변환 없는 ASCII·이진 부동소수점 옵션을 적는다(14–22). 정수 값 범위는 엄격 부등호 그대로 옮긴다(16·18). 기존 파일에 덧붙이기 조건, 덤프 간격과 일(days) 단위의 시작·종료 시각을 정의한다(24–30). 지정 시작 전·종료 후에는 덤프가 없다고 적는다(28·30). 주석 표식과 빈 줄을 포함한다(11–30). 원문: `C70 CONTROLS FOR WRITING ASCII OR BINARY DUMP FILES` (10); `\* ISDUMP: GREATER THAN 0 TO ACTIVATE` (14); `\*                1 SCALED ASCII INTERGER (0<VAL<65535)` (16); `\*                2 SCALED 16BIT BINARY INTEGER (0<VAL<65535) OR (-32768<VAL<32767)` (18); `\*                3 UNSCALED ASCII FLOATING POINT` (20); `\*                4 UNSCALED BINARY FLOATING POINT` (22); `\* ISADMP: GREATER THAN 0 TO APPEND EXISTING DUMP FILES` (24); `\* NSDUMP: NUMBER OF TIME STEPS BETWEEN DUMPS` (26); `\* TSDUMP: STARTING TIME FOR DUMPS - DAYS (NO DUMPS BEFORE THIS TIME)` (28); `\* TEDUMP: ENDING TIME FOR DUMPS - DAYS (NO DUMPS AFTER THIS TIME)` (30). |
| 31–44 | C70 CONTROLS FOR WRITING ASCII OR BINARY DUMP FILES / 변수·정수 범위 — 수면 표고(water surface elevation)·수평 및 수직 속도(horizontal/vertical velocity)·수송 변수(transported variable)의 덤프 조건을 적는다(32–38). 스케일 변환된 이진 정수 범위 조정 값을 제시한다(40–42). 주석 표식과 빈 줄을 포함한다(31–44). 원문: `\* ISDMPP: GREATER THAN 0 FOR WATER SURFACE ELEVATION DUMP` (32); `\* ISDMPU: GREATER THAN 0 FOR HORIZONTAL VELOCITY DUMP` (34); `\* ISDMPW: GREATER THAN 0 FOR VERTICAL VELOCITY DUMP` (36); `\* ISDMPT: GREATER THAN 0 FOR TRANSPORTED VARIABLE DUMPS` (38); `\* IADJDMP: 0 FOR SCALED BINARY INTEGERS (0<VAL<65535)` (40); `\*                 -32768 FOR SCALED BINARY INTEGERS (-32768<VAL<32767)` (42). |
| 45–48 | C70 입력 예시 — 입력 열 제목과 수치 값 행을 제시한다(46·48). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(45·47). 원문: `C70 ISDUMP ISADMP NSDUMP TSDUMP TEDUMP ISDMPP ISDMPU ISDMPW ISDMPT IADJDMP` (46); `             0          0            10080       0            731          0             0            0          1          -32768` (48). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

