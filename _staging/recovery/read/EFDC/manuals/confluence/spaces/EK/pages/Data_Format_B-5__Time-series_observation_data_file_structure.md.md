---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Format_B-5__Time-series_observation_data_file_structure.md
lines: 13
sha256: 15bf2dfc88a229a8e8f1ac00fffca99dff1d749f79f4cecb518568eeabcd2ea7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-5__Time-series_observation_data_file_structure.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 페이지 제목은 `"Data Format B-5  Time-series observation data file structure."` (3)이다. `id: 1588723821` (2), `space: EK` (4), `version: 1` (6), `updated: 2021-11-10T04:11:02.961Z` (7)를 기록한다. 원문 URL (5)과 문서 경로 (8)가 있다. 1·9행은 frontmatter 구분선이다. |
| 10–13 | Time-series observation data file structure — 표의 머리말과 구분선 (10–11)을 포함한다. 관측 시계열(time-series observation) 파일 확장자는 `*Data file containing observation data (.wq,.dat)*` (12)이다. 첫 입력 행은 데이터 점 개수 `N`과 라벨(label)용 제목이며, 제목은 라벨에만 사용한다고 적는다 (13). 관측 날짜·시각·매개변수 값이 뒤따른다 (13). 그레고리력 날짜(Gregorian date)와 율리우스 날짜(Julian date)를 허용한다 (13). Windows가 날짜로 인식하는 그레고리력 형식을 허용한다 (13). EE는 각 행의 마지막 매개변수를 데이터 값으로 사용한다 (13). 데이터 행은 N개 관측점 모두에 대해 반복한다 (13). 원문 예시 셀 전체: `10993 USGS\_Speedy, Salinity, PPT 01-Jul-1999 00:00 27.7 01-Jul-1999 01:00 27.6 01-Jul-1999 02:00 27.8 01-Jul-1999 03:00 27.8 01-Jul-1999 04:00 27.7 01-Jul-1999 05:00 27.6 01-Jul-1999 06:00 27.6 01-Jul-1999 07:00 27.5 01-Jul-1999 08:00 27.5 01-Jul-1999 09:00 27.5 01-Jul-1999 10:00 27.6 01-Jul-1999 11:00 27.8 01-Jul-1999 12:00 27.9 01-Jul-1999 13:00 28 01-Jul-1999 14:00 27.9 01-Jul-1999 15:00 28 01-Jul-1999 16:00 28.1 01-Jul-1999 17:00 28.1 .......................` (13). 입력 필드·수량·날짜 형식·사용 조건을 설명한 셀 전체: `***First line:***10993: number (**N**) of data points; USGS\_Speedy, Name, Units: title for some meaning (here: station name, water temperature in Celsius degree). This text is only used for labeling.  ***Second line to N lines:***Date (Gregorian) (Julian date is also OK, for example, the 370th day counting from 01-Jan-1999), time and parameter's value. The Gregorian date format can be in any format that Windows recognizes as a date. EE uses the last parameter in the line as the data value.  The data lines are repeated for all N data points.` (13). 원문은 예시를 한 Markdown 물리 행에 두므로 입력 파일의 줄바꿈을 임의로 복원하지 않았다. |

수식 전사: 0개. 매개변수·입력 필드 이름 전사: 5개 (`N`, `title`, `Date (Gregorian)`, `time`, `parameter's value`).
이 집계는 전사한 이름의 종류 수이다. 예시 값은 기본값으로 간주하지 않았다.
참조 그림 0개를 로컬 파일로 직접 열어 확인했다.

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13: 예시 제목은 `USGS\_Speedy, Salinity, PPT`이다. 설명 셀은 같은 제목의 의미를 관측소 이름과 섭씨 수온으로 적는다.
- 13: 설명 셀은 `Second line to N lines`라고 적는다. 같은 셀은 `The data lines are repeated for all N data points.`라고도 적는다.
- 13: 원문 Markdown의 단일 표 행에 예시 제목과 모든 가시 시각·값이 이어져 있다. 설명이 구분하는 입력 파일 행의 줄바꿈은 예시 셀에 남아 있지 않다.
