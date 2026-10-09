---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort91.rst
lines: 27
sha256: f90b0551be101e59736becca4649a23515f607a654a37dad4455eb3f95e8a960
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort91.rst — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.91: Ice Coverage Fields at Recording Stations — 제목과 빈 줄을 포함한다(1–5). 문서는 얼음 피복(ice coverage) 입력 기능이 활성화될 때 지정 기상 기록 지점(meteorological recording stations)의 얼음 피복 자료를 저장한다고 적는다(4). fort.15의 기상 기록 지점 설정이 출력을 제어한다(4). 원문: `` This file contains ice coverage field data at specified meteorological recording stations when ADCIRC's ice coverage input feature is activated. The output is controlled by the meteorological recording station parameters (:ref:`NOUTM <NOUTM>`, etc.) specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. `` (4). |
| 6–19 | File Structure — 문서는 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 쓸 수 있다고 적는다(9). 헤더 뒤에 시각과 반복 단계, 지점별 얼음 피복 자료를 배치한다(13–18). 지시문과 빈 줄을 포함한다(6–19). 원문: `` The file can be written in either ASCII or binary format, depending on how :ref:`NOUTM <NOUTM>` is set in the Model Parameter and Periodic Boundary Condition File. The basic structure is shown below: `` (9); ` .. parsed-literal:: ` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NTRSPM <NTRSPM>`, :ref:`NSTAM <NSTAM>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLM <NSPOOLM>`, :ref:`NSPOOLM <NSPOOLM>`, :ref:`IRTYPE <IRTYPE>` `` (14); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (15); ``     for k=1, :ref:`NSTAM <NSTAM>` `` (16); `         k, RMICE00(k) ` (17); `     end k loop ` (18). |
| 20–27 | Notes — 문서는 출력 형식과 출력 빈도 설정을 적는다(23·26). 이진 출력은 지점 번호를 포함하지 않는다(24). 기상 기록 지점에서 시계열을 저장한다(25). 문서는 출력 변수를 지점별 얼음 피복장 값으로 설명한다(27). 원문: `` * Output format (ASCII/binary) is determined by :ref:`NOUTM <NOUTM>` in the fort.15 file `` (23); ` * For binary output, the station number (k) is not included in the output ` (24); ` * Time series data is recorded at stations specified for meteorological recording ` (25); `` * The output frequency is controlled by :ref:`NSPOOLM <NSPOOLM>` parameter `` (26); ` * The variable RMICE00 represents the ice coverage field value at each recording station  ` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 17·27: `RMICE00(k)`를 출력 변수로 제시한다(17). 변수 설명은 `ice coverage field value`이다(27). 이 파일에는 값의 단위와 수치 범위가 없다.
