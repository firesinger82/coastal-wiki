---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/nolifa.rst
lines: 52
sha256: a0b66bdf72bd81176e184675cedc1e872282ad539c8b8d1189134009e0b5fda6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# nolifa.rst — 판독 구간 기록

구간은 1행부터 52행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | NOLIFA / Parameter Summary — 메타데이터·앵커를 포함한다(1–8). 유한 진폭항(finite amplitude term)과 습윤·건조(wetting-drying) 선택, H0 의미와 추가 입력의 관련성을 옮긴다(10–14). 표의 필수·권고 입력 안내를 포함한다(19–20). 원문: `` **NOLIFA** is a parameter in the :ref:`fort.15 file <fort15>` controlling `` (10); ` controlling the finite amplitude terms and wetting-drying in ADCIRC. The value ` (11); `` of NOLIFA effects the meaning of the minimum water depth parameter (:ref:`H0`) `` (12); ` and requires the specification of additional parameters together with ` (13); `` :ref:`H0`. `` (14). |
| 22–44 | Parameter Summary / 표 — NOLIFA=0·1·2의 유한 진폭항·습윤건조 사용 여부, 초기 수심 가정, H0·NOLICA 조건을 행마다 옮긴다(27–42). NOLIFA=0에서 연속식 시간 변화항 외 모든 항에 지형 수심(bathymetric depth)을 쓴다는 예외를 유지한다(33). 원문: ` .. list-table:: ` (22); `    :header-rows: 1 ` (23); `    :widths: 10 20 40 30 ` (24); `    :class: wrap-table ` (25); `    * - NOLIFA Value ` (27); `      - Description ` (28); `      - Details ` (29); `      - Required/Recommended Inputs ` (30); `    * - 0 ` (31); `      - No finite amplitude terms and no wetting-drying ` (32); ``      - The depth is linearized by using the bathymetric depth, rather than the total depth, in all terms except the transient term in the continuity equation. Wetting and drying of elements is disabled. Initial water depths are assumed equal to the bathymetric water depth specified in the `fort.14 file <fort.14_file>`__. `` (33); ``      - :ref:`H0 <H0>`, :ref:`NOLICA <NOLICA>` = 0 `` (34); `    * - 1 ` (35); `      - Finite amplitude terms without wetting-drying ` (36); ``      - Finite amplitude terms are included in the model run and wetting and drying of elements is disabled. Initial water depths are assumed equal to the bathymetric water depth specified in the :ref:`fort.14 file <fort14>`. `` (37); ``      - :ref:`H0 <H0>`, :ref:`NOLICA <NOLICA>` = 1 `` (38); `    * - 2 ` (39); `      - Finite amplitude terms with wetting-drying ` (40); ``      - Finite amplitude terms are included in the model run and wetting and drying of elements is enabled. Initial water depths are assumed equal to the bathymetric water depth specified in the :ref:`fort.14 file <fort14>`. `` (41); ``      - :ref:`H0 <H0>`, :ref:`NOLICA <NOLICA>` = 1 `` (42). |
| 45–52 | Usage Notes — 질량 보존(mass conservation)과 일관성을 위해 유한 진폭항을 켜면 이류항 시간 미분(time derivative)을 켜야 한다는 권고를 옮긴다(48–50). NOLIFA>0이면 NOLICA=1이라는 조건과 끝의 빈 줄을 포함한다. 원문: ` When the finite amplitude terms are turned on, the time derivative portion of ` (48); ` the advective terms should also be turned on for proper mass conservation and ` (49); `` consistency (i.e., when NOLIFA > 0, then `NOLICA <NOLICA>`__ = 1). `` (50). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10–11: controlling이 두 번 연속 적혀 있다.
