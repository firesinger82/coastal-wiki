---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort19.rst
lines: 51
sha256: e94fc49dc958c47d1a303984b250d21718fc096cbda5c321da256cbab39354dc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort19.rst — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.19: Non-periodic Elevation Boundary Condition File — 수위 지정 경계의 비주기·시변(non-periodic, time varying) 수위 입력이며 NOPE와 NBFR의 읽기 조건을 제시한다(6). 원문: ``The fort.19 file contains non-periodic, time varying elevation boundary conditions for "elevation specified" boundary nodes. This file is only read when an "elevation specified" boundary condition has been specified in the :doc:`Grid and Boundary Information File <fort14>` (NOPE>0) and NBFR=0 in the :doc:`Model Parameter and Periodic Boundary Condition File <fort15>`.`` (6). |
| 8–21 | File Structure — ETIMINC와 경계 절점별 ESBIN 반복의 기본 형식이다(11–18). 위 블록을 모의 끝까지 각 시간 단계에 반복하라고 적는다(20). 원문: `.. parsed-literal::` (13); ``    :ref:`ETIMINC <ETIMINC>` `` (15); ``    for k=1 to :ref:`NETA <NETA>` `` (16); ``       :ref:`ESBIN(k) <ESBIN>` `` (17); `   end k loop` (18); `   Repeat the block above for each time step until the end of the simulation.` (20). |
| 22–28 | Notes — 처음 자료의 시각과 뒤 자료 간격 및 전체 실행을 덮는 자료 제공 의무를 명시한다(25–26). 경계 절점 순서는 fort.14 수위 지정 경계 순서와 같아야 한다(27). 원문: `* The first set of elevation values are provided at TIME=STATIM (as specified in fort.15). Additional sets of elevation values are provided every ETIMINC.` (25); `* Enough sets of elevation values must be provided to extend for the entire model run, otherwise the run will crash!` (26); `* The node order in this file must match the order specified in the elevation specified boundary condition part of the Grid and Boundary Information File.` (27). |
| 29–51 | Example — 수위 절점 세 개의 예시이며 간격 900초와 세 시간 단계의 수위 값을 제시한다(32–45). 예시의 단위와 절점 수 및 수위 증가량을 원문으로 적는다(49–51). 원문: `.. code-block:: none` (34); `   900.0` (36); `   0.5` (37); `   0.5` (38); `   0.5` (39); `   0.6` (40); `   0.6` (41); `   0.6` (42); `   0.7` (43); `   0.7` (44); `   0.7` (45); `* A time increment (ETIMINC) of 900.0 seconds (15 minutes)` (49); `* Three elevation specified boundary nodes (NETA=3)` (50); `* Three time steps of data, with values starting at 0.5 meters and increasing by 0.1 meters for each time step` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15–20·36–45행: 형식의 `Repeat the block above` 대상에는 ETIMINC가 포함되어 있으나 예시는 간격 값 `900.0`을 처음에 한 번만 쓰고 수위 자료 세 집합을 이어서 제시한다.
