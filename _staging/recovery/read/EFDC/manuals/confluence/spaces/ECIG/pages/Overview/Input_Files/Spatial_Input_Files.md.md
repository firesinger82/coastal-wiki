---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Spatial_Input_Files.md
lines: 32
sha256: d6320df56bf5176a291802711e654c34762c5e9e781e2ca1030e1a4fa990b5a1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Spatial_Input_Files.md — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Spatial Input Files이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–18 | Hydrodynamics — 셀 유형(cell type), 보조 셀 유형, 수평 셀 치수·수심·저면 표고·거칠기·식생 분류, 셀 중심 좌표·방향, 셀 모서리 노드(nodes) 파일을 나열한다(12–17). 각 행을 그대로 옮긴다. 빈 줄을 포함한다(18). 원문: `\| **Hydrodynamics** \|  \|` (12); `\| cell.inp \| cell type file \|` (13); `\| celllt.inp \| auxiliary cell type file \|` (14); `\| dxdy.inp \| horizontal cell dimensions, depth, bottom elevation, roughness, vegetation class \|` (15); `\| lxly.inp \| horizontal cell center coordinates and cell orientation \|` (16); `\| corners.inp \| cell corners (nodes) \|` (17). |
| 19–27 | 공간 파일 / 장벽·격자·기상 지도 — 얇은 장벽(thin barriers), 남북 방향 격자 또는 격자 단절, dxdy.inp에서 정한 치수 수정, 대기·바람·지하수 지도, 공간별 일사 차폐(solar radiation shading) 파일을 나열한다(21–27). 대기 지도와 바람 지도는 각각 NASER>1, NWSER>1 조건을 적는다(24–25). 조건과 파일 이름을 그대로 옮긴다. 원문: `\| mask.inp \| specifies thin barriers \|` (21); `\| mappgns.inp \| specifies period grids along north-south or breaks in grid in north-south (J) direction \|` (22); `\| moddxdy.inp \| modifies cell dimensions originally specified in dxdy.inp \|` (23); `\| atmmap.inp \| atmospheric map if NASER>1 \|` (24); `\| wndmap.inp \| wind map if NWSER>1 \|` (25); `\| gwmap.inp \| groundwater map \|` (26); `\| pshade.inp \| spatially varying solar radiation shading \|` (27). |
| 28–32 | Water Quality — I,J,K 수질 셀의 수질 구역(water quality zone) 매핑과 I,J 셀의 퇴적물 플럭스 구역(sediment flux zone) 매핑 파일을 나열한다(29–30). 시간·공간별 조류 성장 동역학 인자(algal growth kinetic factors), 조류·입자성 유기물 침강률(settling rates)과 재포기 조정 인자(reaeration adjustment factor) 파일을 나열한다(31–32). 각 행을 그대로 옮긴다. 원문: `\| **Water Quality** \|  \|` (28); `\| wqwcmap.inp \| Maps an I,J,K water quality cell to a water quality zone \|` (29); `\| wqsdmap.inp \| Maps an I,J water quality cell to a sediment flux zone \|` (30); `\| algaegro.inp \| Time and spatially varying algal growth kinetic factors \|` (31); `\| algaeset.inp \| Time and spatially varying algal and particulate organic matter settling rates and reaeration adjustment factor \|` (32). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 24–25행: NASER와 NWSER의 비교 조건은 있으나 두 변수의 정의는 이 파일에 없다.
- 29–30행: 셀 표기에 I,J,K를 사용하지만 각 첨자의 정의는 이 파일에 없다.

