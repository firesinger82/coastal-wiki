---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/nodecode63.rst
lines: 27
sha256: 6f1ff2c848328cbb31c8aa9bafaf2dedbbf985de62549163638e89c8f92873f3
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# nodecode63.rst — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | Nodecode.63: Wet/Dry State of Nodes — 문서는 자료 집합이 기록된 시간 단계에서 절점(node)이 습윤 또는 건조로 분류되었는지를 저장한다고 적는다(4). 습윤·건조 상태(wet/dry state)의 정수 값을 명시한다(4). 자료는 일반적으로 실험적인 습윤·건조 알고리즘을 다루는 ADCIRC 개발자에게만 가치가 있다고 설명한다(4). 문서는 출력 활성화 설정과 namelist를 명시한다(6). 출력은 ASCII 형식으로만 제공한다(8). 출력 일정은 전체 영역 수위(water surface elevation) 파일 fort.63과 같다(8). 문서는 일정에 사용하는 설정 이름을 명시한다(8). 제목과 빈 줄을 포함한다(1–9). 원문: ` The nodecode.63 file records the wet/dry state of nodes where 1 indicates a node is categorized as wet on the timestep that the dataset was written while a value of 0 indicates that a node is categorized as dry. These data are generally only valuable to ADCIRC developers who are working on experimental wet/dry algorithms. ` (4); `` The writing of the nodecode.63 output file is activated when the :ref:`outputNodeCode <outputNodeCode>` parameter is set to .true. in the optional wetDryContol namelist at the bottom of the :doc:`fort.15 <../input_files/fort15>` file. `` (6); `` Output is only available in the ascii format. The data are produced on the same schedule as the full domain water surface elevation (:doc:`fort.63 <fort63>`) file, i.e., the values of :ref:`TOUTSGE <TOUTSGE>`, :ref:`TOUTFGE <TOUTFGE>`, and :ref:`NSPOOLGE <NSPOOLGE>` are used. `` (8). |
| 10–23 | File Structure — 문서는 예제의 각 행이 출력 한 행에 대응한다고 적는다(13). 반복문은 여러 출력 행을 나타낸다(13). 헤더 뒤에 시각과 반복 단계, 전체 절점의 습윤·건조 상태를 배치한다(17–22). 지시문과 빈 줄을 포함한다(10–23). 원문: ` .. parsed-literal:: ` (15); ``    :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (17); ``    :ref:`NDSETSE <NDSETSE>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>`\*:ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (18); ``    :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (19); ``    for k=1, :ref:`NP <NP>` `` (20); ``       k, :ref:`nodecode(k) <nodecode>` `` (21); `    end k loop ` (22). |
| 24–27 | Note — 문서는 nodecode.63이 정수 값을 포함한다고 적는다(27). 절 제목과 빈 줄을 포함한다(24–26). 원문: ` * The nodecode.63 file contains integer values  ` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
