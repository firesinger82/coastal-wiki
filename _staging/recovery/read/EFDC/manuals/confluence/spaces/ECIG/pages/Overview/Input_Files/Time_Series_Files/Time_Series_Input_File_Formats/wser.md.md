---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Time_Series_Files/Time_Series_Input_File_Formats/wser.md
lines: 70
sha256: 6348b8acf3eb4ca93d3061f4ea4db3b0af29dac703c45ca701afdb0e0db2923e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wser.md — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 wser.inp이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–16 | wser.inp / 파일 용도·적용 버전 — 자유 형식(free format)의 바람 강제력(wind forcing) 파일이며 nw=1,nwser번 반복한다고 적는다(10). EFDC의 1997년 4월 7일 및 이후 버전에 사용하도록 적는다(14). 주석과 빈 줄을 포함한다. 원문: `C wser.inp file, in free format across line, repeats nw=1,nwser times` (10); `C WIND FORCING FILE, USE WITH 7 APRIL 97 AND LATER VERSIONS OF EFDC` (14). |
| 17–43 | 시간·풍속·풍향 매개변수 — MASER는 시간 데이터 수, TCASER는 초 단위 변환, TAASER는 입력 시간과 같은 단위의 가산 조정, WINDSCT는 m/sec 풍속 변환이라고 적는다(18–24). ISWDINT의 0은 향하는 방향(direction to), 1은 불어오는 방향(direction from), 2는 WINDS가 동쪽 속도이고 WINDD가 북쪽 속도인 관례이다(26–32). 시계열 열은 TASER(M), WINDS(M), WINDD(M)이다(40). 이름·값·단위·형식 줄을 그대로 옮긴다. 원문: `C MASER(NW) =NUMBER OF TIME DATA POINTS` (18); `C TCASER(NW) =DATA TIME UNIT CONVERSION TO SECONDS` (20); `C TAASER(NW) =ADDITIVE ADJUSTMENT OF TIME VALUES SAME UNITS AS INPUT TIMES` (22); `C WINDSCT(NW) =WIND SPEED CONVERSION TO M/SEC` (24); `C ISWDINT(NW) =DIRECTION CONVENTION` (26); `C                          0 DIRECTION TO` (28); `C                         1 DIRECTION FROM` (30); `C                         2 WINDS IS EAST VELOCITY, WINDD IS NORTH VELOCITY` (32); `C TASER(M) WINDS(M) WINDD(M)` (40). |
| 44–70 | 바람 시계열 입력 예시 — 헤더와 46–70행의 비어 있지 않은 13개 데이터 행을 순서대로 그대로 옮긴다. 헤더의 시간 데이터 수는 9552이다(44). 빈 줄을 포함한다(45–69). 예시값을 기본값으로 정의하지 않는다. 원문: `9552 86400.0 0.0 1.0 0 10.000 ! WSER\_1` (44); `0.000 10.4370 191.4450` (46); `0.042 10.2040 189.1780` (48); `0.083 10.5230 188.1630` (50); `0.125 10.7250 189.7120` (52); `0.167 10.7180 188.6060` (54); `0.208 10.4630 189.5480` (56); `0.250 10.7180 190.1650` (58); `0.292 10.1390 187.7600` (60); `0.333 9.5870 191.6860` (62); `0.375 8.7080 192.9090` (64); `0.417 7.3990 185.5960` (66); `0.458 6.8500 188.2770` (68); `0.500 6.3800 181.7100` (70). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18–26·44행: 설명은 다섯 헤더 변수를 나열하지만 예시 헤더는 주석 앞에 숫자 여섯 개를 적는다. 마지막 값 `10.000`의 이름과 의미는 이 파일에 없다.
- 26–32·40행: ISWDINT의 방향 관례는 있지만 옵션 0·1에서 WINDD 각도의 단위와 기준 방향은 이 파일에 없다.
- 18·44·46–70행: MASER를 시간 데이터 수로 정의한다. 예시 헤더의 MASER는 9552이다. 이 파일에 실린 뒤쪽 데이터 행은 13개이다.

