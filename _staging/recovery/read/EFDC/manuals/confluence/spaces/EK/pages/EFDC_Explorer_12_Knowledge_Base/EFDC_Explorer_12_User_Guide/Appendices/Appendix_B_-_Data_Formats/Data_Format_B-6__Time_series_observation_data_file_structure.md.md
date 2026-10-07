---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-6__Time_series_observation_data_file_structure.md
lines: 15
sha256: 6c8b215f4c5f6aa1a81715a4051425cc1f5a70ec578ea1b9986b37581f19844f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-6__Time_series_observation_data_file_structure.md — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–15 | Time series observation data file structure — 관측 시계열(observation time series) 파일 예시와 Description을 같은 표에 둔다(12–15). 첫 줄의 데이터 점 수와 제목의 용도를 설명한다(15). 날짜·시각·값의 데이터 줄은 모든 N개 데이터 점에 대해 반복하고 EE는 줄의 마지막 매개변수를 데이터 값으로 사용한다(15). Gregorian 날짜는 Windows가 날짜로 인식하는 형식을 쓸 수 있고 Julian 날짜도 허용한다(15). 예시 값·단위·조건과 반복 설명을 표 행 전체로 옮긴다. 원문: `**Data Format B-6  Time series observation data file structure**` (10); `\|  \|  \|` (12); `\| --- \| --- \|` (13); `\| *Data file containing observation data (.wq,.dat)* \| *Description* \|` (14); `\| 10993 USGS\_Speedy, Salinity, PPT  01-Jul-1999 00:00 27.7  01-Jul-1999 01:00 27.6  01-Jul-1999 02:00 27.8  01-Jul-1999 03:00 27.8  01-Jul-1999 04:00 27.7  01-Jul-1999 05:00 27.6  01-Jul-1999 06:00 27.6  01-Jul-1999 07:00 27.5  01-Jul-1999 08:00 27.5  01-Jul-1999 09:00 27.5  01-Jul-1999 10:00 27.6  01-Jul-1999 11:00 27.8  01-Jul-1999 12:00 27.9  01-Jul-1999 13:00 28  01-Jul-1999 14:00 27.9  01-Jul-1999 15:00 28  01-Jul-1999 16:00 28.1  01-Jul-1999 17:00 28.1  ....................... \| ***First line:*** 10993: number (**N**) of data points; USGS\_Speedy, Name, Units: title for some meaning (here: station name, water temperature in Celsius degree). This text is only used for labeling.   ***Second line to N lines:*** Date (Gregorian) (Julian date is also OK, for example, the 370th day counting from 01-Jan-1999), time, and parameter's value. The Gregorian date format can be in any format that Windows recognizes as a date. EE uses the last parameter in the line as the data value.   The data lines are repeated for all N data points. \|` (15). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15: 예시의 제목은 `Salinity, PPT`이고 Description의 예시 설명은 `water temperature in Celsius degree`이다.
- 15: Description은 `Second line to N lines`라고 적으며 데이터 줄을 모든 `N data points`에 반복한다고도 적는다. 첫 줄에는 데이터 점 수가 있다.
