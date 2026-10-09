---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort83.rst
lines: 33
sha256: cf039e3237d18ec4e861e6c24456dceeec292e5a050ef71b6d9f954267abec01
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort83.rst — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Fort.83: Scalar Concentration Time Series at All Nodes — 제목과 빈 줄을 포함한다(1–8). 문서는 격자 전체 절점(node)의 스칼라 농도(scalar concentration) 시계열을 설명한다(4). note 지시문은 해당 기능을 현재 ADCIRC에서 지원하지 않는다고 명시한다(6–7). 원문: `` This file contains scalar concentration time series data at all nodes in the model grid as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`.  `` (4); ` .. note:: ` (6); `    This feature is currently not supported in ADCIRC. ` (7). |
| 9–25 | File Structure — 문서는 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 쓸 수 있다고 적는다(12). 제시된 구조는 헤더 뒤에 시각과 반복 단계, 절점별 농도 자료를 배치한다(16–24). 지시문과 중간 빈 줄을 포함한다(9–25). 기능의 현재 지원 상태는 7행에 명시되어 있다. 원문: `` The file can be written in either ASCII or binary format, depending on how :ref:`NOUTGC <NOUTGC>` is set in the Model Parameter and Periodic Boundary Condition File. The basic structure is shown below: `` (12); ` .. parsed-literal:: ` (14); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (16); ``     :ref:`NDSETSC <NDSETSC>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGC <NSPOOLGC>`, :ref:`NSPOOLGC <NSPOOLGC>`, :ref:`IRTYPE <IRTYPE>` `` (18); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (20); ``     for k=1, :ref:`NP <NP>` `` (22); ``         k, :ref:`C1(k) <C1>` `` (23); `     end k loop ` (24). |
| 26–33 | Notes — 문서는 출력 형식과 출력 빈도 설정을 적는다(29·32). 이진 출력은 절점 번호를 포함하지 않는다(30). 모든 격자 절점에서 시계열을 저장하는 구조를 설명한다(31). 문서는 해당 기능이 개발 중이며 아직 지원되지 않는다고 다시 명시한다(33). 원문: `` * Output format (ASCII/binary) is determined by :ref:`NOUTGC <NOUTGC>` in the fort.15 file `` (29); ` * For binary output, the node number (k) is not included in the output ` (30); ` * Time series data is recorded for every node in the model grid ` (31); `` * The output frequency is controlled by :ref:`NSPOOLGC <NSPOOLGC>` parameter `` (32); ` * This feature is currently under development and not yet supported in ADCIRC  ` (33). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
