---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Main_Menu/Time_Series/Series_Options.md
lines: 89
sha256: 7c06393fcee4f9a176e278a062c02716a7be7151e1045c421447e603dcdf2350
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Series_Options.md — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 버전, 갱신 시각, 문서 계층 경로와 frontmatter 구분선을 포함한다(1–9). |
| 10–15 | Series Options / Data Series form — 범례를 오른쪽 마우스 클릭하거나 도구 모음의 Format Data Series를 선택하여 표시할 매개변수를 고른다(10). 그림 `TS.JPG`는 자료 서식 창과 Pearl Lake Model 온도(temperature) 그래프다(12). 가로축은 `Time (days)`, 눈금은 150–200이며 간격은 5이다. 세로축은 `Temperature (°C)`, 눈금은 −5–35이며 간격은 4이다. 범례는 셀 642(I:22, J:24)의 Layer 1 빨간선, Layer 5 파란선, Layer 5에서 Layer 1을 뺀 초록선이다. 굵은 빨간 화살표는 범례에서 서식 창 Title 쪽으로 향한다(12, 그림). Figure 1 캡션·빈 줄·그림 마크업을 포함한다(11–15). |
| 16–27 | Data Series — 왼쪽 상자에 표시할 자료 선들이 있다(18). Save·Load로 선과 축의 서식을 저장·불러오고 Delete로 선택한 시계열을 삭제한다(20). Up·Dn은 범례 순서를 바꾼다(22). 그림 `Data1.png`는 셀 780(I:72,J:22), 871(I:78,J:23), 959(I:81,J:24)의 수심 평균 염분(salinity) 목록과 선택 상자를 보여 준다(24). Figure 2 캡션·절 제목·빈 줄을 포함한다(16–27). |
| 28–37 | Series Information — 선택 시계열의 최댓값·최솟값·자료점 수와 범례 문자를 보여 준다(30). 서식 이름은 `*Line Formatting*` (30)이며 `thickness, color, and style` (30)을 설정한다. 왼쪽 클릭으로 선택하고 Control을 누르면 여러 시계열을 선택할 수 있다(32). 그림 `Data2.png`는 셀 871 시계열을 선택한 Data Series 창과 선·기호 서식 및 General Options 탭을 보여 준다(34). Figure 3 캡션·빈 줄·그림 마크업을 포함한다(33–37). |
| 38–45 | General Options — 표시 여부, 오른쪽 Y축, 막대 그래프 설정은 `[Figure 4](#SeriesOptions-Figure4) show the *General Options* frame, that the user can toggle the display of each line by checking *Visible* for the series selected.  An extra Y-axes can be added to the right of the graph by setting the *Right* tab in the “Y-Axis” subframe. Other features include changing lines to bar graphs with the “Show as Bars” check box.` (40). 그림 `Data2.png`를 42행 참조로도 열었다. 그림은 Visible, X-Axis Top·Bottom, Y-Axis Left·Right, Show as Bars와 기타 표시 체크 항목을 보여 준다(42). Figure 4 캡션·빈 줄·그림 마크업을 포함한다(38–45). |
| 46–53 | Transform/Series Editing — X·Y 성분의 가산·승산 조정 계수(additive and multiplicative adjustment factors)를 그래프 용도로 적용하고 시계열 간 더하기·빼기를 지원한다(48). 조건과 EFDC 자료 갱신 여부를 그대로 옮긴다: `The *Transform/Series Editing* tab in [Figure 5](#SeriesOptions-Figure5) provides options for the user to adjust the data with additive and multiplicative adjustment factors for both the X and Y component for plotting purposes. The form also provides a means to add or subtract one series from another and place the resultant series into a specified series with the *Add/Subtract Series* button. The edited data does not update the EFDC data directly.  If desired, an edited series can be exported from the time-series plot and used to update the model input data.` (48). 그림 `TS2.png`는 X Value·Y Value 산술 연산과 Add/Subtract Series 입력 창을 보여 준다(50). Figure 5 캡션·빈 줄을 포함한다(46–53). |
| 54–66 | High and Low Pass Filter / 방법·수식 — 고역 통과 필터(high-pass filter)와 저역 통과 필터(low-pass filter)는 모든 시계열 그래프에 적용할 수 있고 Time series Comparison 및 Model Analysis의 Statistics tools에도 추가되었다고 적는다(56). 순간 유속(instantaneous current velocity)을 시간 평균과 고·저주파 변동의 합으로 나타낸다(58). 그림 `image2016-7-8_112747.png`의 식 (1)은 `v_i = \bar{v} + \widetilde{V}_h + \widetilde{V}_l`이다(60, 그림에서 LaTeX로 전사). 본문 정의는 `vi`가 순간 유속, `v`가 시간 평균 유속이며, 그림 `image2016-7-8_11297.png`의 `\widetilde{V}_h, \widetilde{V}_l`이 각각 고·저주파 변동이라는 것이다(61). 고속 푸리에 변환(Fast Fourier Transform, FFT)과 역변환 적용 및 차단 주파수(cut-off frequency) 예시의 단위는 `Based on the Fast Fourier Transform (FFT) method for energy spectra in the frequency domain, these fluctuations are dependent on the defined cut-off frequency i.e. at 1, 3, and 5 filtering hours. After that, the inverse FFT was used to plot the high or low frequencies results.` (63). 그림 `image2016-7-8_112944.png`의 `High-Pass option:` 식 (2)은 `v_i = \bar{v} + \widetilde{V}_h`이고 `Low-Pass option:` 식 (3)은 `v_i = \bar{v} + \widetilde{V}_l`이다(65, 그림에서 LaTeX로 전사). 절 제목·빈 줄·마크업·공백을 포함한다(54–66). |
| 67–74 | High and Low Pass Filter / 적용 화면·결과 — 원문 탭 표기는 `*Filer lines*` (67)이며 Apply Filter를 선택하면 필터 결과 시계열을 새로 표시한다(67). 그림 `23-09-2021_2-13-58_PM.png`는 Filter lines 탭과 `Hours: 2`, Low Pass Filter·High Pass Filter 선택을 보여 준다(69). 그림 `image2016-7-8_113040.png`의 제목은 `EFDC Testing, Hydrodynamic Example`이다(72). 가로축은 `Time (days)`이며 날짜 눈금은 2002-08-04·11·18·25이다. 세로축은 `WS Elevation (m)`이며 눈금은 −1.2–1.2, 간격은 0.4이다. 빨간 원자료는 `i=6,j=7`, 파란 결과는 `i=6,j=7, Lo-filter 12(hrs)`이다(72, 그림). Figure 6·7 캡션·빈 줄을 포함한다(67–74). |
| 75–89 | Interval — 누락 자료(missing data)의 공백(gap)을 잇는 직선을 제거하는 설정이다(77). 비교 조건·단위·조작 순서는 `When plotting data time series which has gaps (missing data), the plot will have a straight line, as shown in [Figure 9](#SeriesOptions-Figure9). To remove that straight line, the *Gap*tab in the *Data Series*form as shown in [Figure 8](#SeriesOptions-Figure8) can be used. Select the *Gap*, EE will calculate the data gap and number of data points in the underneath table; the gap is presented in hours. Based on the data gap, the user can enter a value that should be greater than the gap in the box *Maximum Gap (hours)*, click *Use*  checkbox, next click *Apply* button. Then click the *OK* button, the plot without the straight line is shown as [Figure 10](#SeriesOptions-Figure10).` (77). 그림 `2022-10-03_3-00-36_PM.png`는 Gaps 탭, `Use` 체크, `Maximum Gap (hours): 1`을 보여 준다(79). Data Gap Summary 표의 `Data Gap (hours)`와 `Number of Data Gaps` 두 열에서 행은 `1 / 2098`, `44 / 1`이다(79, 그림). 그림 `interval11.png`는 공백을 잇는 선을 빨간 타원으로 강조하고 `interval12.png`는 그 선을 제거한 결과다(83·87). 두 그래프의 가로축은 `Time (days)` 332–340이고 세로축은 `Velocity Magnitude (m/s)` 0.00–0.08, 간격은 0.01이다. 범례 `Velocity (m/s)`는 파란선이다(83·87, 그림). Figure 8–10 캡션과 빈 줄·그림 마크업을 포함한다(75–89). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·18·30·40·48·67·77: `#SeriesOptions-Figure1`부터 `#SeriesOptions-Figure10` 링크가 있다. 이 파일에는 대응 앵커 정의가 없다.
- 34·42: 동일한 `Data2.png`가 Figure 3 Series information과 Figure 4 General Options에 사용된다.
- 58·61·63: 그림 식은 평균 유속을 `\bar{v}`로 쓰고 본문 정의는 `v`로 쓴다. 본문은 `cut-off frequency`를 말하며 예시를 `1, 3, and 5 filtering hours`로 적는다.
- 67·69(그림): 본문 탭 이름은 `Filer lines`이다. 그림 탭 이름은 `Filter lines`이다.
- 77·79(그림): 본문은 Maximum Gap 값을 자료 공백보다 크게 입력하라고 적는다. 그림에는 공백 44시간과 Maximum Gap 1시간이 함께 표시된다.

