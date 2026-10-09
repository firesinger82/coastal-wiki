---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort73.rst
lines: 28
sha256: 8dc83c61f4b59d3811b5e6a0db92e20bb01c5e686a8b3be5d2ffcf8148e8eaa4
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort73.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.73: Atmospheric Pressure Time Series at All Nodes in the Model Grid — 앵커와 제목을 포함한다(1–4). 모델 격자의 모든 절점(node)에 대한 기압(atmospheric pressure) 시계열을 설명한다(6). 문서는 전체 영역의 기상 출력이 활성화될 때 이 파일을 생성한다고 적는다(6). 원문: `` The fort.73 file contains atmospheric pressure time series data at all nodes in the model grid as defined in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. This file is generated when meteorological output is enabled for the entire domain. `` (6). |
| 8–23 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(11). 반복문은 여러 출력 행을 나타낸다(11). 헤더 뒤에 시각과 반복 단계, 절점별 기압 자료를 배치한다(15–20). 예제는 시각별 블록을 모의 종료까지 반복하도록 적는다(22). 지시문과 빈 줄을 포함한다(8–23). 원문: ` .. parsed-literal:: ` (13); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``    :ref:`NDSETSW <NDSETSW>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGW <NSPOOLGW>`, :ref:`NSPOOLGW <NSPOOLGW>`, :ref:`IRTYPE <IRTYPE>` `` (16); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (17); ``    for k=1, :ref:`NP <NP>` `` (18); ``       k, :ref:`PR2(k) <PR2>` `` (19); `    end k loop ` (20); `    Repeat the block above for each time step until the end of the simulation. ` (22). |
| 24–28 | Notes — 문서는 fort.15의 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 사용할 수 있다고 적는다(27). 이진 출력은 절점 번호를 포함하지 않는다(28). 원문: `` * Output may be in ascii or binary format depending on how :ref:`NOUTGW <NOUTGW>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (27); ` * If binary output is specified, the node number (k) is not included in the output  ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
