---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Import_External_Layers.md
lines: 68
sha256: 06eca83f48d41bffcb5f4b7bef5e1ed143582cbe4144b3dc193bda4ee9ccd7d5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Import_External_Layers.md — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–38 | 외부 레이어 가져오기(Import External Layers) — 레이블(label), 지리 참조 지도(geo-referenced map), XYZ 자료, ADCP 자료, 수치 표고 모델(DEM), 퇴적물 코어(sediment core), Google Maps의 `.KML`을 가져올 수 있다(10). 개별 레이블 형식은 자료 파일과 같은 이름의 `.LBF` 파일에 저장한다(12). Layer Control 아래 가져오기 버튼으로 Open External Layer를 열고 형식과 파일을 선택한다(14–18). 파일 형식 원문: `Georeferenced Images`와 `(\*.geo; \*.jgw; ...)` (16); `shoreline ( \*.p2d)` (18). 14행의 아이콘을 직접 열었으며 외부 레이어 가져오기 버튼을 보여 준다. 그림 1은 Layer Control의 가져오기 버튼을 보여 준다(20–22). 그림 2는 파일 형식 목록과 Georeferenced Images 선택을 보여 준다(24–26). 그림 3은 Image01.jgw 파일 선택과 Open 버튼을 보여 준다(28–30). 그림 4는 Image01 배경 영상 위의 모델 격자를 보여 준다(32–34). 그림 5는 Lake Washington Model Outline.p2d 해안선 오버레이(overlay)를 보여 준다(36–38). |
| 39–61 | ADCP 횡단 자료 형식 — 실측 음향 도플러 유속계(ADCP) 횡단 자료를 모델 결과와 비교하며 Tecplot `\*.plt` 형식을 요구한다(40). 처음 두 열은 UTM 좌표의 Easting (X), Northing (Y)이며 단위 원문은 `UTM meter`이다(40). 마지막 두 열은 동서·남북 성분 유속이며 원문 이름은 `V\_E\_W`와 `V\_N\_S`이다(40). 입력 예제 원문: `TITLE = "ADCP 2D Depth Averaged Data"` (42); `VARIABLES = "X", "Y", "V\_E\_W", "V\_N\_S"` (43); `ZONE I=58, J=1, F=POINT, T="2024-12-19 13:17"` (44); `516547 5050427 -0.035 0.014` (45); `516554 5050430 -0.133 0.213` (46); `516561 5050433 -0.073 0.282` (47); `516569 5050437 -0.059 0.233` (48); `516577 5050440 -0.115 0.258` (49); `516586 5050445 -0.159 0.374` (50); `516594 5050449 -0.151 0.370` (51); `516602 5050453 -0.135 0.325` (52); `516610 5050458 -0.168 0.372` (53); `516617 5050463 -0.152 0.413` (54); `516625 5050468 -0.201 0.389` (55); `516633 5050473 -0.153 0.360` (56); `516640 5050477 -0.179 0.388` (57); `516648 5050481 -0.145 0.277` (58); `516656 5050487 -0.191 0.426` (59); `516664 5050494 -0.181 0.439` (60).42–59행 말미의 두 공백은 Markdown 줄바꿈 마크업이다. |
| 62–68 | ADCP와 모델 벡터 표시 — 그림 6에 해당하는 파일 선택 화면을 직접 열었다(62). 화면은 `ADCP Data (*.adcp;*.plt;*.txt)` 필터를 보여 준다. 데이터 레이어의 오른쪽 클릭 Properties로 실측 유속 벡터(velocity vector)의 속성을 변경한다(64). 모델 벡터도 Properties에서 변경하며 같은 시작점에 놓으려면 `Location File`, `Select`, `\*.p2d`를 사용한다(66). 이 p2d는 Tecplot ADCP 파일의 X, Y 열에서 만든다(66). 68행의 두 그림을 모두 직접 열었다. 첫 그림은 ADCP Layer Settings와 빨간 실측 화살표, 두 번째는 Vector2D Layer Properties의 Location File 선택과 같은 시작점의 청록색 모델 화살표·빨간 실측 화살표를 보여 준다. 범례 유속 크기는 양쪽 모두 `1.000`이며 단위는 모델 `m/s`, 실측 `(m/s)`이다(68행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 44–60: `ZONE I=58, J=1` 선언 뒤 이 파일에 수록된 수치 자료는 45–60행의 16행이다. 생략 표시나 나머지 자료 행은 이 예제에 없다.
- 40·68: 본문은 좌표 단위만 명시한다. 벡터 범례에는 유속 단위 `m/s`가 표시되어 있다.

