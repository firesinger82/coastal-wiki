---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/noff100.rst
lines: 33
sha256: 136b0c8ee67c754bf7b8da79d19e0c6a1fe428c17abe6bc528878818a505a2e7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# noff100.rst — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Noff.100: Wet/Dry Elemental State File — 문서는 자료 집합이 기록된 시각의 격자 요소(element) 습윤·건조 상태(wet/dry state)를 저장한다고 적는다(4). 요소 배열(elemental array) 이름과 상태 값을 명시한다(4). 자료는 주로 실험적인 습윤·건조 알고리즘을 다루는 ADCIRC 개발자에게 유용하다고 설명한다(4). 문서는 출력 활성화 설정과 namelist를 명시한다(6). 출력 일정은 fort.63 수위(water surface elevation) 파일과 같다(6). 문서는 일정에 사용하는 설정 이름을 명시한다(6). 제목과 빈 줄을 포함한다(1–7). 원문: `` This file records the wet/dry state of elements in the model grid, where a value of 1 indicates a wet element and 0 indicates a dry element at the time the dataset was written. The data comes from the elemental wet/dry array :ref:`NOFF <NOFF>` in ADCIRC. These data are primarily useful for ADCIRC developers working on experimental wet/dry algorithms. `` (4); `` The file is generated when the `outputNOFF` parameter is set to `.true.` in the optional `wetDryControl` namelist at the bottom of the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. Output timing follows the same schedule as the :doc:`Water Surface Elevation <fort63>` file, using the parameters :ref:`TOUTSGE <TOUTSGE>`, :ref:`TOUTFGE <TOUTFGE>`, and :ref:`NSPOOLGE <NSPOOLGE>`. `` (6). |
| 8–24 | File Structure — 문서는 출력이 ASCII 형식으로만 제공된다고 적는다(11). 예제는 헤더에서 요소 수를 사용한다(17). 헤더 뒤에 시각과 반복 단계, 요소별 상태를 배치한다(19–23). 지시문과 중간 빈 줄을 포함한다(8–24). 원문: ` The file is only available in ASCII format. The basic structure is shown below: ` (11); ` .. parsed-literal:: ` (13); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (15); ``     :ref:`NDSETSE <NDSETSE>`, :ref:`NE <NE>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (17); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (19); ``     for i=1, :ref:`NE <NE>` `` (21); ``         i, :ref:`NOFF(i) <NOFF>` `` (22); `     end i loop ` (23). |
| 25–33 | Notes — 문서는 이 파일을 절점 자료가 아닌 요소 자료를 생성하는 유일한 ADCIRC 출력 파일이라고 설명한다(28). 출력은 ASCII 형식만 제공한다(29). 문서는 정수 상태 값과 출력 빈도 설정을 다시 명시한다(30–31). 생성 제어 설정은 namelist에 둔다(32). 자료는 주로 습윤·건조 알고리즘 개발과 시험을 위한 것이다(33). 원문: ` * This is the only ADCIRC output file that produces elemental (rather than nodal) data ` (28); ` * Output is available only in ASCII format ` (29); ` * Values are integers: 1 for wet elements, 0 for dry elements ` (30); `` * Output timing matches fort.63 file using :ref:`NSPOOLGE <NSPOOLGE>` parameter `` (31); `` * File generation is controlled by `outputNOFF` in the `wetDryControl` namelist `` (32); ` * Data is primarily intended for wet/dry algorithm development and testing  ` (33). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
