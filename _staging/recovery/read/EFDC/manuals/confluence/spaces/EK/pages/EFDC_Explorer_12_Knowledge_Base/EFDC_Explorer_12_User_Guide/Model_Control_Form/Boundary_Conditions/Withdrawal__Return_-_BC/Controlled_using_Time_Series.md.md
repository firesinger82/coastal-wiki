---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Boundary_Conditions/Withdrawal__Return_-_BC/Controlled_using_Time_Series.md
lines: 26
sha256: a4062a92288eac40a7d5e93697e45dcf960e9f4976f0971b7eabe3823e07239c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Controlled_using_Time_Series.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Controlled using Time Series / 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각과 문서 계층을 담은 frontmatter 및 구분선이다(1–9). |
| 10–17 | Time Series / 경계와 시계열 선택 — Current Boundary Group의 Time Control에서 시계열 제어를 선택하고 Current Boundary Cell에서 취수 셀(withdrawal cell)과 환류 셀(return cell)을 정의한다(10–12). W/R Flow and Concentration Rise/Fall Settings의 Time Variable Series에서 시계열(time series)을 선택한다(14). 원문: ``Select *Controlled using Time-Series* from the drop-down box for *Time Control* in the *Current Boundary Group* frame.`` (10); ``Define the withdrawal cell and the return cell in the *Current Boundary Cell* frame.`` (12); ``In the *W/R Flow and Concentration Rise/Fall Settings* frame, select a time series from the drop-down box for *Time Variable Series*as shown in [Controlled using Time Series#Figure 1](https://eemodelingsystem.atlassian.net/wiki/spaces/EK/pages/2133852161#ControlledusingTimeSeries-Figure1).`` (14). 16행 `6-15-2022_2-10-15_PM.png`의 로컬 사본을 열었다. 그림은 `Controlled using Time-Series`와 `Time Variable Series: WR_1`을 빨간 테두리로 강조한다(16). |
| 18–26 | Time Series / 편집과 자료 열 — Edit로 기존 시계열을 편집하거나 Boundary Data Series의 Add New로 새 시계열을 생성한다(18). 시간과 유량 정의는 원문 그대로 옮긴다: ``Time (days) is Julian time in days`` (20); ``Flow (m3/s) is the actual flow rate from the withdrawal cells to return cells`` (22). 다른 열은 취수 셀에서 환류 셀까지의 염분(salinity), 수온(temperature), 염료(dye), 수질(water quality), 화학물질 거동·수송(chemical fate & transport)의 농도 차다(24). 양의 차이는 환류 셀 농도가 취수 셀보다 크다는 뜻이며 반대도 같다고 적는다(24). 부호의 원문: ``Other columns for salinity, temperature, dye, water quality, and chemical fate & transport, are different concentration values of the withdrawal cells to return cells. The positive delta values represent concentration in the return cells greater than the concentration of withdrawal cells and vice versa.`` (24). 26행 `6-15-2022_2-29-45_PM.png`의 로컬 사본을 열었다. WR_1 자료 표의 보이는 열 머리글은 `Time (days)`, `Flow (m³/s)`, `Salinity (ppt)`, `Temp (°C)`, `Dye01 (mg/L)`, `SFL (#/L)`, `RPOC (mg/L)`이다(26행 그림). 완전히 보이는 자료 행을 `행 번호: Time, Flow, Salinity, Temp, Dye01, SFL, RPOC` 순서로 옮긴다: ``1: 182, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``2: 183, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``3: 184, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``4: 185, 3.000, 0.000, 1.50, 0.000000E+000, 0.000, 0.310``; ``5: 186, 3.000, 0.000, 1.50, 0.000000E+000, 0.000, 0.300``; ``6: 187, 3.000, 0.000, 1.50, 0.000000E+000, 0.000, 0.400``; ``7: 188, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``8: 189, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``9: 190, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``10: 191, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000``; ``11: 192, 0.000, 0.000, 0.00, 0.000000E+000, 0.000, 0.000`` (26행 그림). 화면은 `# of Points: 181`이라고 표시한다. 다음 자료 행은 하단에서 일부 잘려 있고 오른쪽 추가 열은 화면 밖에 있으므로 그 값은 옮기지 않았다(26행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·18: Figure 1·2 링크는 원문 페이지의 `#ControlledusingTimeSeries-Figure1` 등 이름을 사용한다. 이 Markdown 파일에는 해당 ID의 앵커나 그림 캡션이 없다.
- 20: Time은 Julian time in days라고만 정의한다. 이 파일에는 그 시간의 기준일이나 달력 규약이 없다.
- 26행 그림: 표에는 `SFL`과 `RPOC` 열이 있다. 이 파일 본문은 그 약어를 정의하지 않는다. 전체 181개 점 중 완전한 자료 행은 처음 11개만 화면에 보인다.
