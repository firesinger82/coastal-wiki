---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/inundationtime63.rst
lines: 37
sha256: b2ab9007c7a20bb312c0034c235a4754b71313d23b1e54abbf880b6522d90225
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# inundationtime63.rst — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | Inundationtime.63: Inundation Time File — 문서는 처음에 건조했던 영역이 침수 기준 수심(inundation threshold depth)을 초과해 침수된 총시간을 저장한다고 적는다(4). 문서는 출력 활성화 설정을 명시한다(6). 자료 집합(data sets)은 둘이다(8). 첫째 자료는 기준 수심을 초과한 침수 기간의 누적 시간이다(9). 연속하지 않은 침수 기간도 누적 시간에 포함한다(9). 둘째 자료는 기준 수심을 초과한 침수의 시작 시각이다(10). 시작 시각의 기준은 초기 시작(cold start)이다(10). 원문은 두 자료의 시간 단위를 명시한다(9–10). 제목과 빈 줄을 포함한다(1–11). 원문: `` The inundationtime.63 file records the total time that an initially dry area is inundated beyond a certain inundation threshold depth specified in the :doc:`fort.15 <../input_files/fort15>` file in the inundationOutputControl namelist by the parameter :ref:`inunThresh <inunThresh>`. `` (4); `` The writing of the inundationtime.63 output file is activated when the :ref:`inundationOutput <inundationOutput>` parameter is set to .true. in the optional inundationOutputContol namelist at the bottom of the :doc:`fort.15 <../input_files/fort15>` file. `` (6); ` The file contains two data sets: ` (8); ` 1. Total accumulated time in seconds that a node was inundated beyond the threshold (periods of inundation are counted toward the total time, even if they are not contiguous) ` (9); ` 2. Time of onset of inundation beyond the threshold in seconds since cold start (useful in the context of real time model guidance for decision making) ` (10). |
| 12–30 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(15). 반복문은 여러 출력 행을 나타낸다(15). 헤더의 자료 집합 수는 2이다(20). 첫째 절점(node)별 블록은 침수 누적 시간을 저장한다(21–24). 둘째 절점별 블록은 침수 시작 시각을 저장한다(26–29). 지시문과 중간 빈 줄을 포함한다(12–30). 원문: ` .. parsed-literal:: ` (17); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (19); ``    2, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (20); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (21); ``    for k=1, :ref:`NP <NP>` `` (22); ``       k, :ref:`inundationtime(k) <inundationtime>` `` (23); `    end k loop ` (24); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (26); ``    for k=1, :ref:`NP <NP>` `` (27); ``       k, :ref:`inundationtime_onset(k) <inundationtime_onset>` `` (28); `    end k loop ` (29). |
| 31–37 | Notes — 문서는 출력 설정에 따라 ASCII 또는 netCDF 형식을 쓸 수 있다고 적는다(34). 파일은 시간 단계 계산을 마친 뒤 모의 종료에 쓴다(35). 값은 재시작(hotstarted)했더라도 현재 실행만 반영한다(36). 마지막 주석은 처음에 건조했던 영역의 최대 침수 수심(maximum inundation depth)을 기록한다고 적는다(37). 원문: `` * Output may be in ascii or netCDF format depending on how :ref:`NOUTGE <NOUTGE>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (34); ` * The inundationtime.63 file is written at the very end of the simulation, after timestepping is complete ` (35); ` * The values only reflect the current run, even if the run was hotstarted ` (36); `` * The data only record maximum inundation depth in areas that are initially dry, according to the :doc:`initiallydry.63 <initiallydry63>` file  `` (37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 4·8–10·23·28·37: 본문은 누적 침수 시간과 침수 시작 시각을 설명한다(4·8–10). 구조의 출력 변수는 `inundationtime(k)`와 `inundationtime_onset(k)`이다(23·28). 37행은 자료가 `maximum inundation depth`를 기록한다고 적는다.
- 4·6: namelist 이름은 4행에서 `inundationOutputControl`이고 6행에서 `inundationOutputContol`이다.
