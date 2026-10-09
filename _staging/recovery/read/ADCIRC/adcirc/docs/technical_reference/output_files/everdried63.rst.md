---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/everdried63.rst
lines: 38
sha256: c7dee8d2169971fd1d5f07e9505bfc60720367a986b506fc797ceaa9e168888c
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# everdried63.rst — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | Everdried.63: Dry Node Flagging File — 모의 중 한 번이라도 건조해진 절점을 표시해 조화 분석(harmonic analysis)을 지원한다(6). 한 시간 단계라도 건조하면 수면 높이(water surface elevation)의 -99999가 분석 해를 오염시킨다고 적는다(6). inundationOutput = .true.일 때 파일 쓰기를 활성화한다(8). 첫 자료 집합(data set)은 건조 이력에 따른 상태값이다(10–11). 둘째 자료 집합은 건조했던 총 시간을 초 단위로 기록한다(12). 원문: `The everdried.63 file was created to support harmonic analysis by flagging all nodes that had ever become dry during the course of a simulation. These data are useful to harmonic analysis because a node that goes dry for a single time step has a -99999 recorded for its water surface elevation, which contaminates the harmonic analysis solution.` (6); ``The writing of the everdried.63 output file is activated when the :ref:`inundationOutput <inundationOutput>` parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the :doc:`fort.15 <../input_files/fort15>` file.`` (8); `The file contains two data sets:` (10); `1. Wet/dry state information: -99999.0 if a node ever went dry during the simulation, 1.0 if it was wet for the entire simulation` (11); `2. Total time in seconds that a node was dry during the simulation (0.0 if it was always wet)` (12). |
| 14–32 | File Structure — 실행 식별 정보와 자료 집합 수 2인 머리말(header)을 제시한다(21–22). 첫 NP 반복 블록은 everdried(k)를 기록한다(23–26). 다음 TIME·IT와 NP 반복 블록은 driedtime(k)를 기록한다(28–31). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (17); `.. parsed-literal::` (19); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (21); ``    2, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (22); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (23); ``    for k=1, :ref:`NP <NP>` `` (24); ``       k, :ref:`everdried(k) <everdried>` `` (25); `   end k loop` (26); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (28); ``    for k=1, :ref:`NP <NP>` `` (29); ``       k, :ref:`driedtime(k) <driedtime>` `` (30); `   end k loop` (31). |
| 33–38 | Notes — NOUTGE 설정에 따라 ASCII 또는 netCDF 형식일 수 있다(36). 시간 적분(timestepping)이 끝난 모의 종료 시 파일을 쓴다(37). 재시작(hot start)한 경우에도 값은 현재 실행만 반영한다(38). 원문: `` * Output may be in ascii or netCDF format depending on how :ref:`NOUTGE <NOUTGE>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (36); `* The everdried.63 file is written at the very end of the simulation, after timestepping is complete` (37); `* The values only reflect the current run, even if the run was hotstarted ` (38). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
