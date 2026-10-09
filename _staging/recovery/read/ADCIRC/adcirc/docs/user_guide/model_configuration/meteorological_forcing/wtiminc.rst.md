---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/meteorological_forcing/wtiminc.rst
lines: 20
sha256: a77580268d7289ce8b849e0a4cf989492682aa7f5d72961813df1fe84ebdd9cc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# wtiminc.rst — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | WTIMINC Supplemental — 메타데이터·앵커·제목을 포함한다(1–8). fort.15의 기상 자료 세트 간 시간 간격과 초 단위를 옮긴다(10–12). 입력 행의 NWS 의존성, ABS(NWS)>1의 필요 조건과 매개 와류(parametric vortex) 예외, NWS=−14의 WTIMINC_12를 원문대로 옮긴다(13–20). 원문: `` **WTIMINC** is a parameter in the :ref:`fort.15 file <fort15>` that is `` (10); ` the time increment between meteorological forcing data sets (in seconds) in ` (11); `` input files like the :ref:`fort.22 <fort22>` file. This parameter and the :ref:`line on `` (12); `` which it appears :ref:<fort15>` depend on the value of `` (13); `` :ref:`NWS <NWS>`. For a detailed breakdown of what goes on this line in the `` (14); `` :ref:`fort.15 file <fort15>`, see the :ref:`supplemental meteorological/wave/ice `` (15); `` parameters <supplemental_meteorological_wave_ice_parameters>` page. Broadly, `` (16); ``` ``WTIMINC`` is required for ``ABS(NWS)>1`` unless you are using one of the ``` (17); ` parametric vortex models for meteorology. Relatedly, note that when ` (18); ``` ``NWS=-14``, a second parameter, WTIMINC_12 ``` (19); ` defines the time increment for meteorological data for the OWI-formatted files. ` (20). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12–13: 참조 역할(role)의 내용이 :ref:`line on which it appears :ref:<fort15>`로 적혀 있어 내부에 :ref:가 한 번 더 들어 있다.
