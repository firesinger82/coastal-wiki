---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort23.rst
lines: 45
sha256: a56b1b5ceb804c83e593c1aff2f71b5ec3c3cdd1e749caa7417cf940e05e60c4
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort23.rst — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.23: Wave Radiation Stress Forcing File — 파랑 복사응력(wave radiation stress)의 단독 또는 다른 강제력과 결합한 입력이다(6). ABS(NWS) 조건과 NWS=-4 PBL 재시작 형식과의 유사성을 제시한다(6). 원문: ``The fort.23 file contains wave radiation stress data that can be used to drive ADCIRC either by itself or in combination with other forcing (including winds). This file is read when ABS(:ref:`NWS <NWS>`) >= 100 in the :ref:`Model Parameter and Periodic Boundary Condition File <fort15>`. The format is similar to the meteorological input file used when :ref:`NWS <NWS>` = -4 (i.e. the PBL hurricane model input format following a hot start).`` (6). |
| 8–16 | File Structure — 절점 번호와 두 방향 복사응력 성분의 입력 한 줄을 parsed-literal로 제시한다(11–15). 원문: `.. parsed-literal::` (13); ``    :ref:`JN <JN>`, :ref:`RSX(JN) <RSX>`, :ref:`RSY(JN) <RSY>` `` (15). |
| 17–31 | Notes — 시간 보간(interpolation)에 최소 두 자료 집합을 요구하며 하나뿐이면 EOF 오류로 종료한다(20). 절점 부분집합(subset)·초기 실행(cold start) 및 재시작(hot start)의 자료 시각·간격·줄 형식·구분 기호·미지정 절점의 0·응력 단위 및 전 기간 자료 제공 의무를 제시한다(22–30). 원문: `1. At least two datasets must be present in the file to allow for time interpolation. If only one dataset is present, the run will terminate with an unexpected end-of-file error.` (20); ``2. Radiation stresses are input directly to a subset of nodes in the ADCIRC grid (as specified by the node number :ref:`JN <JN>`).`` (22); ``3. If ADCIRC is cold started, the first set of radiation stress data corresponds to TIME=:ref:`STATIM <STATIM>`. If ADCIRC is hot started, the first set of radiation stress data corresponds to TIME=HOT START TIME. Additional sets of radiation stress data must be provided every :ref:`RSTIMINC <RSTIMINC>`, where :ref:`RSTIMINC <RSTIMINC>` is the radiation stress time interval and is specified in the :ref:`Model Parameter and Periodic Boundary Condition File <fort15>`. Radiation stresses are interpolated in time to the ADCIRC time step.`` (24); `4. Each data line must have the format I8, 2E13.5. Data input lines are repeated for as many nodes as desired. A line containing the # symbol in column 2 indicates radiation stress data at the next time increment begins on the following line. At each new time, any node that is not specified in the input file is assumed to have zero wave radiation stress.` (26); `5. Wave radiation stress must be input in units of velocity squared (consistent with the units of gravity). Stress in these units is obtained by dividing stress in units of force/area by the reference density of water.` (28); `6. Data must be provided for the entire model run, otherwise the run will crash!` (30). |
| 32–45 | Example — 두 자료 집합에 대한 세 절점 복사응력과 구분 기호의 입력 예시를 제시한다(35–45). 입력 지수 표기와 공백을 원문으로 옮긴다(39–45). 원문: `.. code-block:: none` (37); `   1    0.12345E+00  0.23456E+00` (39); `   2    0.34567E+00  0.45678E+00` (40); `   3    0.56789E+00  0.67890E+00` (41); `   # ` (42); `   1    0.12345E+01  0.23456E+01` (43); `   2    0.34567E+01  0.45678E+01` (44); `   3    0.56789E+01  0.67890E+01` (45). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 26·42행: 설명은 `#`를 열 2에 놓도록 지정한다. 예시의 `#` 행은 code-block의 공통 들여쓰기를 제외하면 기호 앞에 추가 공백이 없다.
