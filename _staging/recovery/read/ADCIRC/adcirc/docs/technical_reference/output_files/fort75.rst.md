---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort75.rst
lines: 26
sha256: eaca49529300f5b41c58b28257bd676b382c05d075d3feda8d395f51a4e36cad
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort75.rst — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.75: Bathymetry Time Series at Recording Stations — 제목과 빈 줄을 포함한다(1–5). 문서는 시간 변화 수심 지형(time varying bathymetry) 기능이 활성화될 때 지정 기록 지점의 수심 지형 시계열을 저장한다고 적는다(4). 수위(water surface elevation) 기록 지점 설정이 출력을 제어한다(4). 원문: `` This file contains bathymetry time series data at specified recording stations when ADCIRC's time varying bathymetry feature is activated. The output is controlled by the water surface elevation recording station parameters (:ref:`NOUTE <NOUTE>`, etc.) specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. `` (4). |
| 6–19 | File Structure — 문서는 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 쓸 수 있다고 적는다(9). 헤더 뒤에 시각과 반복 단계, 지점별 수심 지형 자료를 배치한다(13–18). 지시문과 빈 줄을 포함한다(6–19). 원문: `` The file can be written in either ASCII or binary format, depending on how :ref:`NOUTE <NOUTE>` is set in the Model Parameter and Periodic Boundary Condition File. The basic structure is shown below: `` (9); ` .. parsed-literal:: ` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NTRSPE <NTRSPE>`, :ref:`NSTAE <NSTAE>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLE <NSPOOLE>`, :ref:`NSPOOLE <NSPOOLE>`, :ref:`IRTYPE <IRTYPE>` `` (14); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (15); ``     for k=1, :ref:`NSTAE <NSTAE>` `` (16); ``         k, :ref:`DP00(k) <DP>` `` (17); `     end k loop ` (18). |
| 20–26 | Notes — 문서는 출력 형식과 출력 빈도를 제어하는 설정을 명시한다(23·26). 이진 출력은 지점 번호를 포함하지 않는다(24). 수심 지형 시계열은 수위 기록 지점에서 저장한다(25). 원문: `` * Output format (ASCII/binary) is determined by :ref:`NOUTE <NOUTE>` in the fort.15 file `` (23); ` * For binary output, the station number (k) is not included in the output ` (24); ` * Time series data is recorded at stations specified for water surface elevation recording ` (25); `` * The output frequency is controlled by :ref:`NSPOOLE <NSPOOLE>` parameter  `` (26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
