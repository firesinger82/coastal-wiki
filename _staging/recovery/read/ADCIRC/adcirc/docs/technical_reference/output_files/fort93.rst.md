---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort93.rst
lines: 29
sha256: 716060dbf5567a3c260653c4ac88cdfc8545e987eaa9d7ffeaee8217a15103e4
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort93.rst — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.93: Ice Coverage Fields at All Nodes — 제목과 빈 줄을 포함한다(1–5). 문서는 전체 격자 절점(node)의 얼음 피복(ice coverage) 자료를 설명한다(4). 형식은 fort.73과 fort.63을 따른다(4). 얼음 피복장 기능이 활성화되고 전역 기상 출력(global meteorology output)이 활성화될 때만 파일을 생성한다(4). 문서는 생성 조건의 설정 이름을 명시한다(4). 원문: `` This file contains ice coverage field data at all nodes in the model grid. The file follows the same format as the :doc:`Pressure <fort73>` and :doc:`Elevation <fort63>` files. It is generated only when ice fields are activated and global meteorology output is enabled through the parameters (:ref:`NOUTGW <NOUTGW>`, :ref:`TOUTSGW <TOUTSGW>`, :ref:`TOUTFGW <TOUTFGW>`, :ref:`NSPOOLGW <NSPOOLGW>`) in the :doc:`Model Parameter and Periodic Boundary Condition File <../input_files/fort15>`. `` (4). |
| 6–19 | File Structure — 문서는 출력 설정에 따라 ASCII 또는 이진(binary) 형식을 쓸 수 있다고 적는다(9). 헤더 뒤에 시각과 반복 단계, 절점별 얼음 피복률을 배치한다(13–18). 지시문과 빈 줄을 포함한다(6–19). 원문: `` The file can be written in either ASCII or binary format, depending on how :ref:`NOUTGW <NOUTGW>` is set in the Model Parameter and Periodic Boundary Condition File. The basic structure is shown below: `` (9); ` .. parsed-literal:: ` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NDSETSW <NDSETSW>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGW <NSPOOLGW>`, :ref:`NSPOOLGW <NSPOOLGW>`, :ref:`IRTYPE <IRTYPE>` `` (14); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (15); ``     for k=1, :ref:`NP <NP>` `` (16); `         k, iceCoveragePercent(k) ` (17); `     end k loop ` (18). |
| 20–29 | Notes — 문서는 출력 형식과 출력 빈도 설정을 적는다(23·26). 이진 출력은 절점 번호를 포함하지 않는다(24). 모든 격자 절점에서 시계열을 저장한다(25). 시작 시각과 종료 시각 설정으로 출력 시기를 추가 제어할 수 있다(27). 출력 변수는 절점별 얼음 피복의 백분율이다(28). 문서는 fort.73·fort.63과 같은 구조라고 다시 적는다(29). 원문: `` * Output format (ASCII/binary) is determined by :ref:`NOUTGW <NOUTGW>` in the fort.15 file `` (23); ` * For binary output, the node number (k) is not included in the output ` (24); ` * Time series data is recorded for every node in the model grid ` (25); `` * The output frequency is controlled by :ref:`NSPOOLGW <NSPOOLGW>` parameter `` (26); `` * Output timing can be further controlled using :ref:`TOUTSGW <TOUTSGW>` (start time) and :ref:`TOUTFGW <TOUTFGW>` (end time) `` (27); ` * The variable iceCoveragePercent represents the percentage of ice coverage at each node ` (28); ` * File structure matches the format used in fort.73 (pressure) and fort.63 (elevation) files  ` (29). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
