---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort61.rst
lines: 26
sha256: 0c7ecb9085030646e92871fa0d18985e6c6256e404706ade414189cae16367ea
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort61.rst — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.61: Elevation Time Series at Specified Elevation Recording Stations — fort.15에 지정한 수위 관측점(elevation recording station)의 수위 시계열(elevation time series) 출력이다(1–4). 수위 관측점의 시계열 출력을 활성화했을 때 생성한다(4). 원문: ``Elevation time series output at the elevation recording stations as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. This file is generated when time series output is enabled for elevation stations.`` (4). |
| 6–21 | File Structure — 실행 식별 정보와 NTRSPE·NSTAE 등의 머리말(header)을 기록한다(13–14). TIME·IT 뒤에 관측점 번호 k와 ET00(k)를 NSTAE개 기록한다(15–18). 이 블록을 모의 종료까지 각 시간 단계마다 반복하도록 적는다(20). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (9); `.. parsed-literal::` (11); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``    :ref:`NTRSPE <NTRSPE>`, :ref:`NSTAE <NSTAE>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLE <NSPOOLE>`, :ref:`NSPOOLE <NSPOOLE>`, :ref:`IRTYPE <IRTYPE>` `` (14); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (15); ``    for k=1, :ref:`NSTAE <NSTAE>` `` (16); ``       k, :ref:`ET00(k) <ET00>` `` (17); `   end k loop` (18); `   Repeat the block above for each time step until the end of the simulation.` (20). |
| 22–26 | Notes — NOUTE 설정에 따라 ASCII 또는 이진 형식(binary format)일 수 있다(25). 이진 출력을 지정하면 관측점 번호 k를 포함하지 않는다(26). 원문: `` * Output may be in ascii or binary format depending on how :ref:`NOUTE <NOUTE>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (25); `* If binary output is specified, the station number (k) is not included in the output ` (26). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
