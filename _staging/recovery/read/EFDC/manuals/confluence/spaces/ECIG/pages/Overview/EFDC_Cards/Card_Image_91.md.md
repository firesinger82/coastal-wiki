---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_91.md
lines: 46
sha256: 891c67338cfd2f2d05b7d3db9f00f09440fc0ecb7f6d0062f19e841573590520
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_91.md — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Card Image 91이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–42 | C91 OPTIONS FOR GENERATION OF NETCDF FILE(S) — NetCDF 파일 생성 여부, 압축 수준과 2차원 유속장의 실제 동쪽(true east)·실제 북쪽(true north) 방향 회전(rotation)을 설명한다(14–24). 정수형 결측값(missing value), UTM 구역의 반구별 부호, 시작 후 재시작 출력까지의 시간, 공백 없는 기준 날짜·시간, 공백 없이 최대 길이 20인 프로젝트 이름을 설명한다(26–40). 각 옵션·범위·단위를 그대로 옮긴다. 원문: `\* NCDFOUT:      OPTION FOR NETCDF EXPORT` (14); `\*                   =1 GENERATE NETCDF FILE NC` (16); `\*                   =0 NO GENERATION` (18); `\* DEFLEV:         LEVEL OF COMPRESSION OF NETCDF FILE FROM 0 TO 9` (20); `\* ROTA:       =1 ROTATING 2D VELOCITY FIELD TO THE TRUE EAST AND TRUE NORTH` (22); `\*                  =0 NO ROTATION TO TRUE EAST AND TRUE NORTH` (24); `\* BLK:               MISSING VALUE: INTEGER KIND` (26); `\* UTMZ:            UTM ZONE` (28); `\*                       >0 FOR NORTHERN HEMISPHERE; <0 FOR SOUTHERN HEMISPHERE` (30); `\* HREST:          NUMBER OF HOURS AFTER BEGIN TIME FOR RESTART OUTPUT` (32); `\* BASEDATE:   YYYY-MM-DD (NO BLANK)` (34); `\* BASETIME:   HH:MM:SS (NO BLANK)` (36); `\* PROJ:           PROJECT NAME IS A STRING OF MAXIMUM LENGTH 20` (38); `\*                      WITHOUT ANY BLANKS` (40). |
| 43–46 | C91 / 입력 예시 — 카드 헤더와 한 데이터 행을 그대로 옮긴다(44–46). 출력 생성값 0, 압축값 2, 회전값 1, 결측값 -999, UTM 구역 12, 재시작 시간 24시간, 날짜·시간과 프로젝트 이름은 이 행의 예시값이다. 이 파일은 이 값을 기본값으로 정의하지 않는다. 원문: `C91 NCDFOUT  DEFLEV  ROTA  BLK  UTMZ  HREST  BASEDATE BASETIME     PROJ` (44); `              0               2            1     -999     12         24       1990-01-01 00:00:00   AESRDOldmanRiver` (46). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
