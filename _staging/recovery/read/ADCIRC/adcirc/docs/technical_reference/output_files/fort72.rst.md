---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort72.rst
lines: 30
sha256: aaf218508859b368ac054559e03934c4f165d1106c7e3e15ea5c37ce4af8ed1a
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort72.rst — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.72: Wind Velocity Time Series at Specified Meteorological Recording Stations — 앵커와 제목을 포함한다(1–4). fort.15에서 정한 기상 기록 지점(meteorological recording stations)의 풍속(wind velocity) 시계열을 설명한다(6). 문서는 기상 출력이 활성화될 때 이 파일을 생성한다고 적는다(6). 원문: `` The fort.72 file contains wind velocity time series data at specified meteorological recording stations as defined in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. This file is generated when meteorological output is enabled. `` (6). |
| 8–23 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(11). 반복문은 여러 출력 행을 나타낸다(11). 헤더 뒤에 시각과 반복 단계, 지점별 풍속의 두 성분을 배치한다(15–20). 예제는 시각별 블록을 모의 종료까지 반복하도록 적는다(22). 지시문과 빈 줄을 포함한다(8–23). 원문: ` .. parsed-literal:: ` (13); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``    :ref:`NTRSPM <NTRSPM>`, :ref:`NSTAM <NSTAM>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLM <NSPOOLM>`, :ref:`NSPOOLM <NSPOOLM>`, :ref:`IRTYPE <IRTYPE>` `` (16); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (17); ``    for k=1, :ref:`NSTAM <NSTAM>` `` (18); ``       k, :ref:`WVNX(k) <WVNX>`, :ref:`WVNY(k) <WVNY>` `` (19); `    end k loop ` (20); `    Repeat the block above for each time step until the end of the simulation. ` (22). |
| 24–30 | Notes — 문서는 fort.15의 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 사용할 수 있다고 적는다(27). 이진 출력은 지점 번호를 포함하지 않는다(28). 기상 기록 지점 위치는 fort.15에 지정한다(29). 문서는 풍속 성분의 단위를 명시한다(30). 원문: `` * Output may be in ascii or binary format depending on how :ref:`NOUTM <NOUTM>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (27); ` * If binary output is specified, the station number (k) is not included in the output ` (28); ` * The meteorological recording station locations are specified in the fort.15 file ` (29); ` * Wind velocity components (WVNX, WVNY) are given in meters per second  ` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
