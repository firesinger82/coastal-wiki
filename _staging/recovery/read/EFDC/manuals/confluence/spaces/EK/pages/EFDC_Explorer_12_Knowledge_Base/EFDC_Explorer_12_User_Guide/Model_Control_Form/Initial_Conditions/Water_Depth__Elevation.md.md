---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Initial_Conditions/Water_Depth__Elevation.md
lines: 28
sha256: 68c6a2e5edd35ddfa2489fefeafebd33406347071f69ad6afe93dafa41b1853f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Water_Depth__Elevation.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Water Depth / Elevation — 문서 식별자, 제목, space, URL, 판본, 갱신 시각과 문서 계층의 frontmatter(1–9). |
| 10–15 | Water Depth / Elevation — CSS 선언 뒤 초기 수심(water depth)·수면고(surface elevation) 배정을 설명한다(10). `Assign Elevation`으로 Apply Cell Properties: Water Surface Elevations를 열며 파일 옵션·형식은 Bathymetry를 참조한다(10–12). 빈 줄과 그림을 포함한다(11,13–15). `2019-09-16_5-13-01_PM.png`을 열었다(14). 그림은 초기수면고·수심과 다각형 배정 양식이다. 초기값은 `Average Level (m): 6.675`, `Minimum Depth (m): 0.001`이며 Assign Elevation·Assign Depth·Download를 강조한다. Adjustment (Legacy)는 `Minimum Height (m): 0.001`, `Scaling Factor: 1`, `Vertical Offset (m): 0`이다. 배정 양식은 `Only grid cells inside polygons`, `Scatter (XYZ) data`, `Centroid Interp.`를 선택하며 `All grid cells`, `Constant: 0`, `Avg. Value`, `Max. Value`, `Min. Value`도 표시한다. |
| 16–28 | Download Online Data — HYCOM 자료의 온라인 수면고 다운로드를 설명한다(16–20). 자료 이름·해상도 원문: `HYCOM Global Surface Data (1/12°)` (20) 자료의 시각 범위는 갱신되므로 Get으로 확인하며 단일 시각을 지정한다(22). 시간 조건 원문: `The *Temporal Information* is not fixed and changes regularly as the data set is updated. Click on the *Get* button to get the available time range for downloading. Once the data appears, set the download time (set the same value both boxes as it is one time) in the *Time Range* section and see the corresponding *Time Zone* . ` (22) 공간 범위·다각형 조건 원문: `The spatial data information of the *Data Set* is provided in *Spatial Information* section. The *Data Extraction Limits* is automatically set to the whole model domain, the user can manually download and apply the data for a specific area by checking the *Using Polygon File*and browser to the closed polygon that contains the area inside.` (24) 로그 선택 원문: `The user can also save the extracted data to a file if needed by checking on *Save Log File* checkbox before downloading.` (26) 26행은 선택 자료의 최신 bathymetry를 받아 적용한다고 적는다. 빈 줄과 그림을 포함한다(17,19,21,23,25,27–28). `2019-09-19_3-26-08_PM.png`을 열었다(28). Data Set 이름은 드롭다운 폭에서 잘리며 Data Field는 `surf_el: Water Surface Elevation`이다. Spatial Information의 `Longitude, Latitude`는 `Min.: 0.000, -80.000`; `Max.: 359.840, 80.000`; `Interval: 0.080000, 0.080000`; `#: 4499, 2001`이다. Temporal Information은 `Base Date: 2013-03-05`, `Begin: 2013-03-05 00:00:00`, `End: 2019-09-24 00:00:00`, `Interval (hours): 3`, `#: 16426`이다. 추출 범위의 `Longitude, Latitude`는 `Min.: -82.000229, 26.511147`; `Max.: -81.884956, 26.640270`이다. 두 Time Range 입력값은 모두 `2015-06-01`이며 `Time Zone: 0`이다. `Using Polygon File`과 `Save Log File`은 미체크 상태이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10: Figure 1 링크의 fragment는 `#Figure1`이다. 이 파일에는 해당 anchor 정의가 없다.
- 18: Figure 2 링크는 `resumedraft.action?draftId=240386174#WaterDepth/Elevation-Figure`의 초안 재개 URL이다.
- 18–20·26·28의 그림: 절의 대상과 그림 Data Field는 수면고이다. 26행은 다운로드 대상을 `latest bathymetry data`라고 적는다.
