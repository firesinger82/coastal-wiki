---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/endrisinginun63.rst
lines: 30
sha256: 1c31edb2544762b498222683bdad614f7c0f5d698b5139bc493e7db26cb9a6a1
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# endrisinginun63.rst — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Endrisinginun.63: Inundation Rising at the End of the Run Flag File — 최종 시간 단계와 직전 시간 단계의 수면 높이(water surface elevation)를 비교해 모의 종료 시 침수 깊이(inundation depth)가 상승하는 절점에 1을 부여한다(6). 나머지 절점에는 0을 부여한다(6). 선택적 namelist의 inundationOutput을 .true.로 설정하면 파일 쓰기를 활성화한다(8). 원문: `The endrisinginun.63 file flags nodes whose inundation depth is rising at the end of the simulation by comparing the water surface elevation on the final time step with the water surface elevation on the previous time step. Nodes with rising inundation levels are flagged with an integer value of 1 and all others are given an integer value of 0.` (6); ``The writing of the endrisinginun.63 output file is activated when the :ref:`inundationOutput <inundationOutput>` parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the :doc:`fort.15 <../input_files/fort15>` file.`` (8). |
| 10–23 | File Structure — 실행 식별 정보와 자료 집합 수 1인 머리말(header)을 제시한다(17–18). TIME·IT 다음에 NP개 절점의 번호와 endrisinginun(k)를 기록하는 형식이다(19–22). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (13); `.. parsed-literal::` (15); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (17); ``    1, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (18); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (19); ``    for k=1, :ref:`NP <NP>` `` (20); ``       k, :ref:`endrisinginun(k) <endrisinginun>` `` (21); `   end k loop` (22). |
| 24–30 | Notes — NOUTGE 설정에 따라 ASCII 또는 netCDF 형식일 수 있다(27). 시간 적분(timestepping)이 끝난 모의 종료 시 파일을 쓴다(28). 재시작(hot start)한 경우에도 현재 실행만 반영한다(29). initiallydry.63에 따른 초기 건조 영역에서 상승하는 수면 높이만 표시한다(30). 원문: `` * Output may be in ascii or netCDF format depending on how :ref:`NOUTGE <NOUTGE>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (27); `* The endrisinginun.63 file is written at the very end of the simulation, after timestepping is complete` (28); `* The values only reflect the current run, even if the run was hotstarted` (29); ``* The data only flag rising water surface elevation in areas that are initially dry, according to the :doc:`initiallydry.63 <initiallydry63>` file `` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
