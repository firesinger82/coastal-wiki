---
file: models/ADCIRC/raw/manuals/wiki/markdown/Initiallydry.63_file.md
lines: 13
sha256: 1bd5e04911eba7324d3661f3e73a9a40ce416ecaf76551fbebe6c95cf298422f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Initiallydry.63_file.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | Initiallydry.63 file — 콜드스타트(cold start) 시점의 건조(dry)·습윤(wet) 영역을 기록하여 처음 건조한 영역이 이후 습윤해지면 침수(inundation) 영역으로 볼 수 있게 한다(5). 출력 활성화 조건과 1·0 의미를 적는다(7). 핫스타트 실행도 콜드스타트의 건조 상태를 기록한다(7). 절점 속성 세 개, 격자 수심과 건조 절점으로 완전히 둘러싸인 습윤 절점을 건조시키는 landlocking 알고리즘을 반영한다(9). 조석·기상·하천 등 강제력(forcing)의 효과는 포함하지 않는다(9). 제목·판본·빈 줄을 포함한다(1–10). 원문: `When the [inundationOutput](/index.php?title=InundationOutput&action=edit&redlink=1) parameter is set to .true. in the optional [inundationOutputContol namelist](/index.php?title=InundationOutputContol_namelist&action=edit&redlink=1) at the bottom of the [fort.15 file](/Fort.15_file), the initiallydry.63 file will be written at the beginning of the simulation whether the run is a cold start or hot start. The nodal values in the initiallydry.63 file are 1 if a node is dry at cold start, and 0 if the node is wet at coldstart. The data in the initiallydry.63 file represent areas that are dry at cold start, even if the run that produced the initiallydry.63 file was hotstarted.` (7); `The wet/dry state in the initiallydry.63 file takes into account the [initial_river_elevation](/Initial_river_elevation) nodal attribute, the [surface_submergence_state](/index.php?title=Surface_submergence_state&action=edit&redlink=1) nodal attribute, and the [sea_surface_height_above_geoid](/Sea_surface_height_above_geoid) nodal attribute from the [nodal attributes (fort.13) file](/Fort.13_file), as well as the bathymetric depth from the [mesh (fort.14) file](/Fort.14_file). It also includes the results of the landlocking algorithm, which dries any wet nodes that are completely surrounded by dry nodes. It does not include the effect of any tidal, meteorological, river, or other forcing.` (9). |
| 11–13 | File Format — `initiallydry.63 file format` 문서로 연결한다(11–13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9행: inundationOutput, inundationOutputContol namelist, surface_submergence_state 링크에 `action=edit&redlink=1`이 있다. 7행의 네임리스트 이름은 `inundationOutputContol`이다.
