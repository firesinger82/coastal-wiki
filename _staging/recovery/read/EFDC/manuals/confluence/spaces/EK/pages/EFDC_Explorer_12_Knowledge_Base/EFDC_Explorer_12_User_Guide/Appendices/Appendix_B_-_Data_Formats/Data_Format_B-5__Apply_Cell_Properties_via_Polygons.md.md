---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-5__Apply_Cell_Properties_via_Polygons.md
lines: 24
sha256: f38b85a05e20574bb785c50c87990502f7acb311e000dffac08c2cdd0172ec49
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-5__Apply_Cell_Properties_via_Polygons.md — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–14 | Assign Value Using Vertical Profiles / 용도 — 수층(water column) 매개변수의 초기 조건장(initial condition field)을 수직·수평으로 변화하도록 배정하는 파일이다(11). 임의 개수의 위치에서 수직 프로파일(vertical profile)을 두며 필요한 위치 수만큼 입력을 반복할 수 있다(11). 파일 설명 줄을 제시한다(13). 원문: `**Data Format B-5  Apply Cell Properties via Polygons: Assign Value Using Vertical Profiles**   ` (10); `This file is used to assign a vertical and horizontally variable initial condition field for any of the water column parameters. The data is basically a series of vertical profiles at any number of locations. The following summarizes the input format for one location. This can be repeated for as many locations as needed.` (11); `Line0: Data file description` (13). |
| 15–24 | 수직 프로파일 입력 형식 — 위치마다 ID, 좌표·점 수, 점 수만큼의 깊이, 점 수만큼의 매개변수 값 순서로 읽는다(15–24). 수면 아래 양의 깊이와 단위 및 매개변수별 값 단위를 원문 그대로 옮긴다. 원문: `Loop over the number of vertical profile locations  ` (15); `    Line 1: ID                                 (any user defined ID)  ` (16); `    Line 2: Xc, Yc, nPts                 (nPts in vertical profile)  ` (17); `    Loop over nPts  ` (18); `       Input Depth                           (Positive depths below the water surface, m)  ` (19); `    End Loop  ` (20); `    Loop over nPts  ` (21); `        Input Parameter\_Value         (units dependent on the parameter)  ` (22); `    End Loop  ` (23); ` End Loop` (24). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 17: `Xc`, `Yc`의 좌표 단위는 이 파일에 없다.
