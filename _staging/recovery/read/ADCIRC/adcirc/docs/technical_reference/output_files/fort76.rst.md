---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort76.rst
lines: 26
sha256: 31c546e89969442f5b314a905b26ab23ebc3fb07627dd3d16bf24b48190d1cc7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort76.rst — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.76: Bathymetry Time Series at All Nodes — 제목과 빈 줄을 포함한다(1–5). 문서는 시간 변화 수심 지형(time varying bathymetry) 기능이 활성화될 때 격자 전체 절점(node)의 수심 지형 시계열을 저장한다고 적는다(4). 전체 영역 수위(water surface elevation) 시계열 출력 설정이 출력을 제어한다(4). 원문: `` This file contains bathymetry time series data at all nodes in the model grid when ADCIRC's time varying bathymetry feature is activated. The output is controlled by the full domain time varying water surface elevation output parameters (:ref:`NOUTGE <NOUTGE>`, etc.) specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. `` (4). |
| 6–19 | File Structure — 문서는 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 쓸 수 있다고 적는다(9). 헤더 뒤에 시각과 반복 단계, 절점별 수심 지형 자료를 배치한다(13–18). 지시문과 빈 줄을 포함한다(6–19). 원문: `` The file can be written in either ASCII or binary format, depending on how :ref:`NOUTGE <NOUTGE>` is set in the Model Parameter and Periodic Boundary Condition File. The basic structure is shown below: `` (9); ` .. parsed-literal:: ` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NDSETSE <NDSETSE>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (14); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (15); ``     for k=1, :ref:`NP <NP>` `` (16); ``         k, :ref:`dp(k) <dp>` `` (17); `     end k loop ` (18). |
| 20–26 | Notes — 문서는 출력 형식과 출력 빈도를 제어하는 설정을 명시한다(23·26). 이진 출력은 절점 번호를 포함하지 않는다(24). 수심 지형 시계열은 격자의 모든 절점에서 저장한다(25). 원문: `` * Output format (ASCII/binary) is determined by :ref:`NOUTGE <NOUTGE>` in the fort.15 file `` (23); ` * For binary output, the node number (k) is not included in the output ` (24); ` * Time series data is recorded for every node in the model grid ` (25); `` * The output frequency is controlled by :ref:`NSPOOLGE <NSPOOLGE>` parameter  `` (26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
