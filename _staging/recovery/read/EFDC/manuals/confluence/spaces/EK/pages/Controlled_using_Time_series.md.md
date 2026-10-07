---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Controlled_using_Time_series.md
lines: 22
sha256: 016e4e4ffd2ce1607d272f1f40ad3cc09114ea42e33e750acdc0a5aadd14483b
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Controlled_using_Time_series.md — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 정보 — Controlled using Time series의 페이지 메타데이터와 frontmatter 구분선을 포함한다(1–9). |
| 10–15 | Controlled using Time-Series / W/R 설정 — 이 옵션을 선택하면 수질 성분의 상승·하강(rise/fall)을 지정할 수 있다(10). 취수·방류(withdrawal/return, W/R) 셀 간 유량·농도 차를 시간에 대해 상수 또는 변화 값으로 지정하고 Time Variable Series에서 자료를 선택한다(10). 적용 조건을 원문으로 옮기며 Figure 1 참조와 캡션을 포함한다(12–14). 원문: `If *Controlled using Time-Series* is selected from the drop-box, the rise/fall for each water quality constituent can be defined. In *W/R Flow and Concentration Rise/Fall Settings* frame user can set Flow and difference concentration between W/R cells as constant all the times or vary base on time. The user should select the time series data in the *Time Variable Series* box of *W/R Flow and Concentration Rise/Fall Settings* frame ([Figure 1](#Figure1)).` (10). 그림 확인: `attachments/2131132540/Withdrawal2.png?version=1&modificationDate=1617787857810&cacheVersion=1&api=v2&width=850` — Figure 1(12): 그림 파일 없음. URL을 디코딩하고 공백·콜론을 처리한 경로에 파일이 없다. 페이지 첨부 폴더를 ls로 확인했으며 Figure 2의 PNG 한 파일만 있었다. |
| 16–22 | Time Variable Series / Boundary Data Series — External Forcing Data의 기존 시계열을 선택하거나 Edit로 수정·생성한다(16). Add New·Copy & New·Delete를 제공한다(18). Time과 Flow는 실제 값이고 다른 성분은 W/R 셀 간 차이라고 구분한다(18). Julian 시간과 유량 단위·나머지 변수의 해석을 원문으로 옮긴다(18). 시계열 표 그림과 마지막 캡션을 포함한다(20–22). 원문: `User can *Add New, Copy & New* or *Delete* the series. In *Data Series* tab, *Time (days)* and *Flow (m3/s)* columns are real value. Time in Julian and Flow is the amount of water W/R. Other columns, inculde Temp, Sal, and other WQ, Toxic parameters are represented by difference value between W/R cells` (18). 그림 직접 확인: `attachments/2131132540/2022-06-07_10-40-59_AM.png` — Figure 2(20): Boundary Data Series에서 `Select Series: Pump`, `Series Name: Pump`, `# of Points: 181`을 표시한다. 표의 열은 `Time (days)`, `Flow (m³/s)`, `Salinity (ppt)`, `Temp. (°C)`, `Dye01 (mg/L)`, `SFL. (#/L)`, `RPOC (mg/L)`, `LPOC (mg/L)`, `DOC (mg/L)`이다. 이 열 순서로 완전히 보이는 1–10행을 옮긴다: `182 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`; `183 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`; `184 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`; `185 3.000 0.000 1.50 0.000000E+... 0.000 0.310 0.540 0.850`; `186 3.000 0.000 1.50 0.000000E+... 0.000 0.300 0.526 0.830`; `187 3.000 0.000 1.50 0.000000E+... 0.000 0.400 0.700 1.100`; `188 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`; `189 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`; `190 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`; `191 0.000 0.000 0.00 0.000000E+... 0.000 0.000 0.000 0.000`. Dye01의 값은 그림의 셀 자체에서 끝을 생략한다. 11행 이하의 내용은 화면 하단에서 잘려 있다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: 그림 파일 없음. URL의 인코딩된 파일명 부분까지 변환한 경로에 파일이 없으며 `attachments/2131132540/`의 ls 결과에는 Figure 2 파일만 있다.
- 10·16: 그림 링크는 `#Figure1`, `#Figure2`를 사용하지만 이 Markdown 파일에는 해당 ID를 정의하는 마크업이 없다.
- 20: Figure 2의 Dye01 열은 화면 셀 자체에서 값을 `0.000000E+...`로 생략한다. 11행 이하의 내용은 화면 하단에서 잘려 있다.

