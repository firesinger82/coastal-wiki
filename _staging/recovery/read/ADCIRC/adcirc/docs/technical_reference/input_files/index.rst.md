---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/index.rst
lines: 124
sha256: d145e4c936496193631593694b652ab41220b0d42294440f12c321f200bc2f84
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# index.rst — 판독 구간 기록

구간은 1행부터 124행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Input Files — 입력 파일이 영역·경계조건(boundary conditions)·매개변수를 정의한다고 소개한다(4). fort14와 fort15는 필수이고 다른 파일은 조건부이다(6–8). 원문: `ADCIRC requires several input files that define the model domain, boundary conditions, and various parameters. This section describes the structure and contents of these files.` (4); `.. note::` (6); ``   :doc:`fort14` and :doc:`fort15` are required. Other files are conditional.`` (8). |
| 10–17 | Grid and Boundaries — 격자·경계 목록은 fort14와 fortrotm을 연결한다(10–16). toctree 지시문의 표시 깊이는 1이다(12–13). 원문: `.. toctree::` (12); `   :maxdepth: 1` (13); `   fort14` (15); `   fortrotm` (16). |
| 18–24 | Model Parameters and Periodic BCs — 모델 매개변수와 주기 경계조건(periodic boundary conditions)의 목록은 fort15를 연결한다(18–23). 원문: `.. toctree::` (20); `   :maxdepth: 1` (21); `   fort15` (23). |
| 25–31 | Nodal Attributes — 절점 속성(nodal attributes)의 목록은 fort13을 연결한다(25–30). 원문: `.. toctree::` (27); `   :maxdepth: 1` (28); `   fort13` (30). |
| 32–38 | Hot Start — 재시작(hot start)의 목록은 fort6768을 연결한다(32–37). 원문: `.. toctree::` (34); `   :maxdepth: 1` (35); `   fort6768` (37). |
| 39–47 | Boundary Conditions — 경계조건의 목록은 fort19와 fort20을 연결한다(39–45). 뒤의 빈 줄도 포함한다(46–47). 원문: `.. toctree::` (41); `   :maxdepth: 1` (42); `   fort19` (44); `   fort20` (45). |
| 48–57 | Meteorological Forcing — 기상 외력(meteorological forcing)의 목록은 개요와 fort22, fort22x_grb2, fort200을 연결한다(48–56). 원문: `.. toctree::` (50); `   :maxdepth: 1` (51); `   meteorological_forcing_overview` (53); `   fort22` (54); `   fort22x_grb2` (55); `   fort200` (56). |
| 58–65 | Wave Forcing — 파랑 외력(wave forcing)의 목록은 fort23과 fort26을 연결한다(58–64). 원문: `.. toctree::` (60); `   :maxdepth: 1` (61); `   fort23` (63); `   fort26` (64). |
| 66–72 | Self Attraction/Earth Load Tide Forcing — 자체 인력·지구 하중 조석 외력(self attraction/earth load tide forcing)의 목록은 fort24를 연결한다(66–71). 원문: `.. toctree::` (68); `   :maxdepth: 1` (69); `   fort24` (71). |
| 73–79 | Ice Coverage — 해빙 피복(ice coverage)의 목록은 fort25를 연결한다(73–78). 원문: `.. toctree::` (75); `   :maxdepth: 1` (76); `   fort25` (78). |
| 80–91 | 3D Baroclinic Simulation — 3차원 경압성 모의(3D baroclinic simulation)의 목록은 fort11과 fort35부터 fort39까지를 연결한다(80–90). 원문: `.. toctree::` (82); `   :maxdepth: 1` (83); `   fort11` (85); `   fort35` (86); `   fort36` (87); `   fort37` (88); `   fort38` (89); `   fort39` (90). |
| 92–101 | Station Locations — 관측점 위치(station locations)의 목록은 elev_stat151, vel_stat151, met_stat151, conc_stat151을 연결한다(92–100). 원문: `.. toctree::` (94); `   :maxdepth: 1` (95); `   elev_stat151` (97); `   vel_stat151` (98); `   met_stat151` (99); `   conc_stat151` (100). |
| 102–109 | Time-varying Topography/Bathymetry — 시간 가변 지형·수심(time-varying topography/bathymetry)의 목록은 time_varying_bathymetry와 time_varying_weirs를 연결한다(102–108). 원문: `.. toctree::` (104); `   :maxdepth: 1` (105); `   time_varying_bathymetry` (107); `   time_varying_weirs` (108). |
| 110–116 | Passive Scalar Transport — 수동 스칼라 수송(passive scalar transport)의 목록은 fort10을 연결한다(110–115). 원문: `.. toctree::` (112); `   :maxdepth: 1` (113); `   fort10` (115). |
| 117–124 | Parallel Execution — 병렬 실행(parallel execution)의 목록은 fort18을 연결한다(117–122). 마지막 빈 줄도 포함한다(123–124). 원문: `.. toctree::` (119); `   :maxdepth: 1` (120); `   fort18` (122). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
