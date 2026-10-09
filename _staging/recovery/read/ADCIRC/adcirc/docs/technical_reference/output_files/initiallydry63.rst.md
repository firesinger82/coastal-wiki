---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/initiallydry63.rst
lines: 28
sha256: 5985397affc240091f045cfb4ddeb32ff4a13c8a9a5a400f266cabe1839c7d7f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# initiallydry63.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Initiallydry.63: Inundation Data Output File — 문서는 초기 시작(cold start)의 습윤·건조 상태(wet/dry state)를 침수(inundation) 출력의 기준으로 사용한다고 적는다(4). 처음에 건조한 영역은 나중에 습윤해질 때 침수 영역으로 간주할 수 있다(4). 지정 설정이 활성화되면 초기 시작 또는 재시작(hot start) 여부와 관계없이 모의 시작에 파일을 쓴다(6). 저장하는 상태는 초기 시작 때의 상태이다(6). 문서는 건조·습윤 상태의 값과 상태 판정에 쓰는 절점 속성(nodal attributes) 및 격자 수심을 명시한다(6·8). landlocking 알고리즘(landlocking algorithm)은 건조 절점으로 완전히 둘러싸인 습윤 절점을 건조시킨다(8). 이 상태는 조석·기상·하천 또는 다른 강제력(forcing)의 효과를 포함하지 않는다(8). 제목과 빈 줄을 포함한다(1–9). 원문: ` The initiallydry.63 file was created as the foundation of inundation output data by specifying the areas that ADCIRC considers wet and dry upon cold start. Those areas that are initially dry can then be considered as inundated areas when they become wet. ` (4); `` When the :ref:`inundationOutput <inundationOutput>` parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the :doc:`fort.15 <../input_files/fort15>` file, the initiallydry.63 file will be written at the beginning of the simulation whether the run is a cold start or hot start. The nodal values in the initiallydry.63 file are 1 if a node is dry at cold start, and 0 if the node is wet at coldstart. The data in the initiallydry.63 file represent areas that are dry at cold start, even if the run that produced the initiallydry.63 file was hotstarted. `` (6); `` The wet/dry state in the initiallydry.63 file takes into account the :ref:`initial_river_elevation <initial_river_elevation>` nodal attribute, the :ref:`surface_submergence_state <surface_submergence_state>` nodal attribute, and the :ref:`sea_surface_height_above_geoid <sea_surface_height_above_geoid>` nodal attribute from the nodal attributes (:doc:`fort.13 <../input_files/fort13>`) file, as well as the bathymetric depth from the mesh (:doc:`fort.14 <../input_files/fort14>`) file. It also includes the results of the landlocking algorithm, which dries any wet nodes that are completely surrounded by dry nodes. It does not include the effect of any tidal, meteorological, river, or other forcing. `` (8). |
| 10–23 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(13). 반복문은 여러 출력 행을 나타낸다(13). 예제는 자료 집합 수를 1로 적는다(18). 헤더 뒤에 시각과 반복 단계, 전체 절점(node)의 초기 건조 상태를 배치한다(17–22). 지시문과 빈 줄을 포함한다(10–23). 원문: ` .. parsed-literal:: ` (15); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (17); ``    1, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (18); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (19); ``    for k=1, :ref:`NP <NP>` `` (20); ``       k, :ref:`initiallydry(k) <initiallydry>` `` (21); `    end k loop ` (22). |
| 24–28 | Notes — 문서는 출력 설정에 따라 ASCII 또는 netCDF 형식을 쓸 수 있다고 적는다(27). 파일은 모의 시작 시 시간 단계 계산 전에 쓴다(28). 원문: `` * Output may be in ascii or netCDF format depending on how :ref:`NOUTGE <NOUTGE>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (27); ` * The initiallydry.63 is written at the very beginning of a simulation run, before timestepping begins  ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
