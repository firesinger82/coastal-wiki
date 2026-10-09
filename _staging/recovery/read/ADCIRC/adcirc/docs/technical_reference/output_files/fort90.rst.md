---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort90.rst
lines: 32
sha256: 41c168b6182ba0cde44e8f552c8f246d3168c6ae8b2a24bfb99b32f35515589f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort90.rst — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.90: Primitive Weighting in Continuity Equation — 앵커와 제목을 포함한다(1–4). 문서는 격자 전체 절점(node)의 연속방정식(continuity equation) primitive 가중치(primitive weighting) 시계열을 설명한다(6). 출력 형식과 빈도 설정은 fort.63 수위(elevation) 시계열과 같은 설정을 사용한다(6). 원문: `` This file contains primitive weighting in continuity equation time series data at all nodes in the model grid as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. The output format and frequency settings are controlled by the same parameters used for the :doc:`Elevation Time Series <fort63>` file. `` (6). |
| 8–24 | File Structure — 문서는 출력 설정에 따라 ASCII 또는 NetCDF 형식을 쓸 수 있다고 적는다(11). 헤더 뒤에 시각과 반복 단계, 절점별 가중치 자료를 배치한다(15–23). 지시문과 중간 빈 줄을 포함한다(8–24). 원문: `` The file can be written in either ASCII or NetCDF format, depending on how :ref:`NOUTGE <NOUTGE>` is set in the Model Parameter and Periodic Boundary Condition File. The basic structure is shown below: `` (11); ` .. parsed-literal:: ` (13); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``     :ref:`NDSETSE <NDSETSE>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (17); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (19); ``     for k=1, :ref:`NP <NP>` `` (21); ``         k, :ref:`tau0var(k) <tau0var>` `` (22); `     end k loop ` (23). |
| 25–32 | Notes — 문서는 출력 형식을 ASCII/NetCDF로 적는다(28). 절점 번호 생략 조건은 binary/NetCDF 출력으로 적혀 있다(29). 모든 격자 절점에서 자료를 저장한다(30). 출력 빈도 설정은 fort.63과 일치한다(31). 문서는 출력 변수의 뜻을 적는다(32). 원문: `` * Output format (ASCII/NetCDF) is determined by :ref:`NOUTGE <NOUTGE>` in the fort.15 file `` (28); ` * For binary/NetCDF output, the node number (k) is not included in the output ` (29); ` * Time series data is recorded for every node in the model grid ` (30); `` * The output frequency is controlled by :ref:`NSPOOLGE <NSPOOLGE>` parameter, matching fort.63 settings `` (31); ` * The variable tau0var represents the primitive weighting value in the continuity equation at each node  ` (32). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 11·28·29: 출력 형식 설명은 `ASCII or NetCDF`(11)와 `ASCII/NetCDF`(28)를 사용한다. 절점 번호 생략 조건은 `binary/NetCDF output`(29)으로 적혀 있다. 이 파일은 이진 형식 선택을 별도로 설명하지 않는다.
