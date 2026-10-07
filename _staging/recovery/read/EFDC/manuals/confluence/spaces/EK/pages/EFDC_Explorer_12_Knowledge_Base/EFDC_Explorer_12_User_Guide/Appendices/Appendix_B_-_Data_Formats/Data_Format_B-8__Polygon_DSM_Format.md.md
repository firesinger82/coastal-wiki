---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-8__Polygon_DSM_Format.md
lines: 14
sha256: 1053ee1fe60838f75a185bee0af6f8ca9a7ee1596076d941f41ca3fcc3de0ac4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-8__Polygon_DSM_Format.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–11 | Polygon DSM Format — 디지털 퇴적물 모델(Digital Sediment Model, DSM) 파일은 임의 개수의 영역 다각형과 퇴적물 데이터 블록을 담는다(11). 다각형 ID와 데이터 블록 ID는 일치해야 한다(11). 데이터가 있는 각 깊이의 줄에 깊이·두께·공극률(porosity)·입도(grain size)를 두고 label 줄에서 입도 등급과 경계를 결정한다(11). 파일 내 모든 블록의 입도 등급 수와 크기는 같아야 하지만 파일 또는 프로젝트 간에는 달라도 된다(11). 단위와 조건을 원문 그대로 옮긴다. 원문: `**Data Format B-8**  **Polygon DSM Format**   ` (10); `The "Polygon" Digital Sediment Model (DSM) format is a file that contains any number of polygons that define an area followed by a data block that contains the sediment data. The polygon ID and the data block ID's must match. The data block consists of a line for each depth (beginning at the surface or 0.0 depth) for which data exists. On each line, the user must include the depth (m), thickness (m), porosity, and then the grain size. The number of grain size classes and the associated size breaks are determined by the space-delimited data of the label line (see example). The number of grain size classes and their sizes must be the same for every sediment data block in the file. However, the size classes can vary from file to file or project to project to meet the project needs.   ` (11). |
| 12–14 | Example / 참조 그림 — 로컬 `models/EFDC/raw/manuals/confluence/spaces/EK/attachments/2094956664/12-7-2020_10-13-11_AM.png`를 직접 열었다(14). 그림은 POLY 좌표 블록과 DATA 표의 입력 예시를 보여 준다(14). 주황색 X·Y·Z 표시는 각각 좌표 열을 가리킨다(14). `Max grainsize, unit ( um or mm as user defined).` 표시는 입경 헤더를 가리키며 `% Finer` 표시는 분포 값 줄을 가리킨다(14). 표의 헤더·입경·각 데이터 줄은 다음과 같다. 그림에 보이는 줄: `POLY Coarse Gravel` (14행 그림 내부 1행); `-0.017 1.019 0.000` (14행 그림 내부 2행); `1.396 1.016 0.000` (14행 그림 내부 3행); `1.393 -0.046 0.000` (14행 그림 내부 4행); `-0.017 -0.035 0.000` (14행 그림 내부 5행); `-0.017 0.993 0.000` (14행 그림 내부 6행); `-0.017 0.993 0.000` (14행 그림 내부 7행); `END Coarse Gravel` (14행 그림 내부 8행); `DATA` (14행 그림 내부 9행); `depth thick density porosity 1940um 2967um 3994um 4644um 5021um 6048um 6615um 8587um 10558um 12530um` (14행 그림 내부 10행); `0.00 0.000 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 11행); `0.00 0.000 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 12행); `0.00 0.000 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 13행); `0.00 0.000 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 14행); `0.00 0.000 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 15행); `0.00 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 16행); `0.10 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 17행); `0.20 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 18행); `0.30 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 19행); `0.40 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 20행); `0.50 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 21행); `0.60 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 22행); `0.70 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 23행); `0.80 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 24행); `0.90 0.010 1643 0.38 0.0 0.0 0.0 0.2 0.0 0.0 0.4 0.6 0.8 1.0` (14행 그림 내부 25행); `END` (14행 그림 내부 26행). 원문: `Example` (12); `![](https://eemodelingsystem.atlassian.net/wiki/download/attachments/2094956664/12-7-2020%2010-13-11%20AM.png?version=1&modificationDate=1636516144975&cacheVersion=1&api=v2)` (14). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11·14(그림): 본문은 깊이·두께·공극률·입도 순서를 설명하지만 그림의 DATA 헤더에는 `depth thick density porosity`가 있다. 그림의 `density` 열은 본문에서 설명하지 않는다.
