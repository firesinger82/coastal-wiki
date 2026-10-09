---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/maxinundepth63.rst
lines: 37
sha256: 18c5768651636c845fabcf5a5e220e4716996b78ec78b6619cf7c1759336f287
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# maxinundepth63.rst — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Maxinundepth.63: Maximum Inundation Depth File — 문서는 모의 중 발생한 지표 위의 최대 침수 수심(peak inundation depth above ground)을 저장한다고 적는다(4). 원문은 단위를 명시한다(4). 자료는 initiallydry.63에서 처음에 건조한 것으로 정한 영역에서만 저장한다(4). 모의 중 한 번도 습윤하지 않은 영역의 값도 명시한다(4). 문서는 출력 활성화 설정을 명시한다(6). 자료 집합(data sets)은 둘이다(8). 첫째 자료는 최대 침수 수심이다(9). 둘째 자료는 그 최댓값이 발생한 시각이다(10). 발생 시각은 초기 시작(cold start) 이후의 초 단위 시각이다(10). 제목과 빈 줄을 포함한다(1–11). 원문: `` The maximum inundation depth (maxinundepth.63) file records the peak inundation depth (in meters) above ground that occurred during the simulation. The data are only recorded in areas that are initially dry according to the :doc:`initiallydry.63 <initiallydry63>` file. The values are -99999.0 if the area was never wet during the simulation. `` (4); `` The writing of the maxinundepth.63 output file is activated when the :ref:`inundationOutput <inundationOutput>` parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the :doc:`fort.15 <../input_files/fort15>` file. `` (6); ` The file contains two data sets: ` (8); ` 1. Peak inundation value ` (9); ` 2. Time of occurrence of the peak inundation value in seconds since cold start ` (10). |
| 12–30 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(15). 반복문은 여러 출력 행을 나타낸다(15). 헤더의 자료 집합 수는 2이다(20). 첫째 절점(node)별 블록은 최대 침수 수심을 저장한다(21–24). 둘째 절점별 블록은 최대 침수 수심의 발생 시각을 저장한다(26–29). 지시문과 중간 빈 줄을 포함한다(12–30). 원문: ` .. parsed-literal:: ` (17); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (19); ``    2, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (20); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (21); ``    for k=1, :ref:`NP <NP>` `` (22); ``       k, :ref:`maxinundepth(k) <maxinundepth>` `` (23); `    end k loop ` (24); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (26); ``    for k=1, :ref:`NP <NP>` `` (27); ``       k, :ref:`maxinundepth_time(k) <maxinundepth_time>` `` (28); `    end k loop ` (29). |
| 31–37 | Notes — 문서는 출력 설정에 따라 ASCII 또는 netCDF 형식을 쓸 수 있다고 적는다(34). 파일은 시간 단계 계산을 마친 뒤 모의 종료에 쓴다(35). 값은 재시작(hotstarted)했더라도 현재 실행만 반영한다(36). 자료는 initiallydry.63에서 처음에 건조한 것으로 정한 영역의 최대 침수 수심만 기록한다(37). 원문: `` * Output may be in ascii or netCDF format depending on how :ref:`NOUTGE <NOUTGE>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (34); ` * The maxinundepth.63 file is written at the very end of the simulation, after timestepping is complete ` (35); ` * The values only reflect the current run, even if the run was hotstarted ` (36); `` * The data only record maximum inundation depth in areas that are initially dry, according to the :doc:`initiallydry.63 <initiallydry63>` file  `` (37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
