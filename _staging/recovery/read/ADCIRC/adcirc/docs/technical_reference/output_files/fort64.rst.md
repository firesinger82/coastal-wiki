---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort64.rst
lines: 28
sha256: 7b8b2d221118644019c0946fcaaa339089663875c99145b6b7bbcee214e9af7f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort64.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.64: Depth-averaged Velocity Time Series at All Nodes in the Model Grid — fort.15에 따른 전체 격자 절점의 수심 평균 속도(depth-averaged velocity) 시계열(time series) 출력이다(3–6). 전체 모델 영역의 시계열 출력을 활성화했을 때 생성한다(6). 원문: ``Depth-averaged velocity time series output at all nodes in the model grid as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. This file is generated when time series output is enabled for the entire model domain.`` (6). |
| 8–23 | File Structure — 실행 식별 정보와 NDSETSV·NP 등의 머리말(header)을 기록한다(15–16). TIME·IT 뒤에 절점 번호 k와 UU2(k), VV2(k)를 NP개 기록한다(17–20). 이 블록을 모의 종료까지 각 시간 단계마다 반복하도록 적는다(22). 원문: `The basic file structure is shown below. Each line of output is represented by a line containing the output variable name(s). Loops indicate multiple lines of output.` (11); `.. parsed-literal::` (13); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``    :ref:`NDSETSV <NDSETSV>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGV <NSPOOLGV>`, :ref:`NSPOOLGV <NSPOOLGV>`, :ref:`IRTYPE <IRTYPE>` `` (16); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (17); ``    for k=1, :ref:`NP <NP>` `` (18); ``       k, :ref:`UU2(k) <UU>`, :ref:`VV2(k) <VV>` `` (19); `   end k loop` (20); `   Repeat the block above for each time step until the end of the simulation.` (22). |
| 24–28 | Notes — NOUTGV 설정에 따라 ASCII 또는 이진 형식(binary format)일 수 있다(27). 이진 출력을 지정하면 절점 번호 k를 포함하지 않는다(28). 원문: `` * Output may be in ascii or binary format depending on how :ref:`NOUTGV <NOUTGV>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (27); `* If binary output is specified, the node number (k) is not included in the output ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
