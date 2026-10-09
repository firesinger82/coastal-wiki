---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort62.rst
lines: 27
sha256: 9dc9fba4872d85774e99506f33329f55aaeeec90fef94179326e7229def7e201
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort62.rst — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.62: Depth-averaged Velocity Time Series at Specified Velocity Recording Stations — fort.15에 지정한 속도 관측점(velocity recording station)의 수심 평균 속도(depth-averaged velocity) 시계열(time series) 출력이다(1–4). 속도 관측점의 시계열 출력을 활성화했을 때 생성한다(4). 원문: ``The fort.62 file contains depth-averaged velocity time series data at specified velocity recording stations as defined in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. This file is generated when time series output is enabled for velocity stations.`` (4). |
| 6–21 | File Structure — 실행 식별 정보와 NTRSPV·NSTAV 등의 머리말(header)을 기록한다(13–14). TIME·IT 뒤에 관측점 번호 k와 UU2(k), VV2(k)를 NSTAV개 기록한다(15–18). 이 블록을 모의 종료까지 각 시간 단계마다 반복하도록 적는다(20). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (9); `.. parsed-literal::` (11); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``    :ref:`NTRSPV <NTRSPV>`, :ref:`NSTAV <NSTAV>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLV <NSPOOLV>`, :ref:`NSPOOLV <NSPOOLV>`, :ref:`IRTYPE <IRTYPE>` `` (14); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (15); ``    for k=1, :ref:`NSTAV <NSTAV>` `` (16); ``       k, :ref:`UU2(k) <UU>`, :ref:`VV2(k) <VV>` `` (17); `   end k loop` (18); `   Repeat the block above for each time step until the end of the simulation.` (20). |
| 22–27 | Notes — NOUTV 설정에 따라 ASCII 또는 이진 형식(binary format)일 수 있다(25). 이진 출력을 지정하면 관측점 번호 k를 포함하지 않는다(26). 관측점 위치는 fort.15에 직접 지정하거나 NSTAV가 음수일 때 별도 vel_stat.151 파일로 지정할 수 있다(27). 원문: `` * Output may be in ascii or binary format depending on how :ref:`NOUTV <NOUTV>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (25); `* If binary output is specified, the station number (k) is not included in the output` (26); ``* The velocity recording station locations can be specified either directly in the fort.15 file or through a separate vel_stat.151 file when :ref:`NSTAV <NSTAV>` is set to a negative value `` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
