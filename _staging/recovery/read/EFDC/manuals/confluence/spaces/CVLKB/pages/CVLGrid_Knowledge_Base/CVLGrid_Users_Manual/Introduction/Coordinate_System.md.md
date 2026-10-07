---
file: models/EFDC/raw/manuals/confluence/spaces/CVLKB/pages/CVLGrid_Knowledge_Base/CVLGrid_Users_Manual/Introduction/Coordinate_System.md
lines: 12
sha256: ff1b7629b8dacd17e64fde46ff8b3c4ea14219dd03399fe16aa93a9a67b2a2c1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Coordinate_System.md — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Coordinate System / 문서 메타데이터 — 페이지 ID `2818256`, 제목, space, 원문 URL, 버전 `2`, 갱신 시각, 문서 계층을 포함한다(1–9). |
| 10–11 | Coordinate System / Cartesian과 I·J — 셀 위치는 직교좌표계(Cartesian coordinate system)로 지정한다고 적는다(10). 서로 수직인 방향선을 기준으로 평면상의 점을 지정하고 셀을 네 사분면(quadrants)으로 나눈다고 설명한다(10). `I`는 X축 방향 셀 인덱스(cell index), `J`는 Y축 방향 셀 인덱스라고 적는다(10). 같은 문장은 X·Y가 일반적으로 곡선이라고 적는다(10). 기본 단위는 미터(meters)다(10). 좌표 기호·단위 원문: `CVLGrid uses the Cartesian coordinate system to specify cell locations. The Cartesian coordinate system specifies a point on a plane relative to two perpendicular directed lines that split the cell into four quadrants. In CVLGrid "I" represents the index of cell along the X-axis and "J" represents the one along the Y-axis, in which X, Y is the curves in general. The base unit for this coordinate system is meters.` (10). |
| 12–12 | Coordinate System / Shape file 좌표계 — 모형 영역의 형상 파일(shape file)을 올릴 수 있다(12). 이 파일의 기본 좌표계는 UTM(Universal Transverse Mercator)이며 기본 단위도 미터다(12). 적용 파일·좌표계·단위 원문: `CVLGrid also allows the user to upload a shape file of the model domain. The base coordinate system used for these files is the Universal Transverse Mercator (UTM) with base units in meters as well.` (12). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10행: 같은 문단은 좌표 기준선을 `two perpendicular directed lines`로 설명하고 이어 X·Y에 대해 `the curves in general`이라고 적는다. 두 설명의 관계는 이 파일에서 정의하지 않는다.
