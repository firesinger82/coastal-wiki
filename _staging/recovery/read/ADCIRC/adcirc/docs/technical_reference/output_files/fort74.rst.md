---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort74.rst
lines: 28
sha256: 19ff35f93322bbb617ffa92c551ca4d41de6b89a0b331f4c94c59e7ef1586c2e
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort74.rst — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.74: Wind Stress or VelocityTime Series at All Nodes in the Model Grid — 앵커와 제목을 포함한다(1–4). fort.15에서 지정한 모델 격자 전체 절점(node)의 풍속(wind velocity) 또는 풍응력(wind stress) 시계열 출력을 설명한다(6). 원문: `` Wind velocity or stress time series output at all nodes in the model grid as specified in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. `` (6). |
| 8–23 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(11). 반복문은 여러 출력 행을 나타낸다(11). 헤더 뒤에 시각과 반복 단계, 절점별 출력 성분을 배치한다(15–20). 예제는 시각별 블록을 모의 종료까지 반복하도록 적는다(22). 지시문과 빈 줄을 포함한다(8–23). 원문: ` .. parsed-literal:: ` (13); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``    :ref:`NDSETSW <NDSETSW>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGW <NSPOOLGW>`, :ref:`NSPOOLGW <NSPOOLGW>`, :ref:`IRTYPE <IRTYPE>` `` (16); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (17); ``    for k=1, :ref:`NP <NP>` `` (18); ``       k, :ref:`WVNXOUT(k) <WVNXOUT>`, :ref:`WVNYOUT(k) <WVNYOUT>` `` (19); `    end k loop ` (20); `    Repeat the block above for each time step until the end of the simulation. ` (22). |
| 24–28 | Note — 문서는 fort.15의 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 사용할 수 있다고 적는다(27). 이진 출력은 절점 번호를 포함하지 않는다(28). 원문: `` * Output may be in ascii or binary format depending on how :ref:`NOUTGW <NOUTGW>` is set in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>` `` (27); ` * If binary output is specified, the node number (k) is not included in the output  ` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 6·19: 문서는 풍속 또는 풍응력을 출력한다고 적는다(6). 예제는 `WVNXOUT(k)`와 `WVNYOUT(k)`를 제시한다(19). 이 파일은 두 물리량의 선택 조건과 출력 단위를 명시하지 않는다.
