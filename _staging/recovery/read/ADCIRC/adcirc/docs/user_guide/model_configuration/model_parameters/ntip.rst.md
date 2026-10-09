---
file: models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/ntip.rst
lines: 56
sha256: f544d0c07ab610cc4bcfc9e2334ef1be416d0952c05f0a9f3d14edd9dbd20e91
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# ntip.rst — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | NTIP / Parameter Summary — 메타데이터·앵커·제목을 포함한다(1–8). NTIP가 fort.15의 천문 강제력(astronomical forcing) 형식을 고른다는 정의와 표 안내를 옮긴다(10–17). 원문: `` **NTIP** is an input in the :ref:`fort.15 file <fort15>` that selects the `` (10); ` astronomical forcing input type. ` (11); ` Parameter Summary ` (13); ` ----------------- ` (14); ` The following table is a summary of possible NTIP values, description, details, ` (16); ` and other necessary input parameters and files. ` (17). |
| 19–40 | Parameter Summary / 표 — NTIP=0의 강제력 없음과 NTIF=0, NTIP=1의 해석적 평형 조석 퍼텐셜(equilibrium tidal potential)과 NTIF>0, NTIP=2의 퍼텐셜과 자기 인력·하중 조석(Self-attraction and Loading, SAL) 기여의 합·NTIF>0·fort.24를 행마다 옮긴다(24–39). 원문 summing을 합으로 유지한다. 원문: ` .. list-table:: ` (19); `    :header-rows: 1 ` (20); `    :widths: 10 20 40 30 ` (21); `    :class: wrap-table ` (22); `    * - NTIP Value ` (24); `      - Description ` (25); `      - Details ` (26); `      - Other Required Inputs ` (27); `    * - 0 ` (28); `      - No Astronomical Forcing ` (29); `      - - ` (30); ``      - :ref:`NTIF <ntif_parameter>` = 0 `` (31); `    * - 1 ` (32); `      - Astronomical Tidal Potential ` (33); `      - Reconstructs the tidal elevation using the analytical formulation for the equilibrium tidal potential [1]_ ` (34); ``      - :ref:`NTIF <ntif_parameter>` > 0 `` (35); `    * - 2 ` (36); `      - Astronomical Tidal Potential plus Self-attraction and Loading (SAL) Tide [2]_ ` (37); ``      - Reconstructs the tidal elevation by summing the contribution from the analytical formulation for the equilibrium tidal potential [1]_ with the contribution from the prescribed SAL constituent values found in the `fort.24 file <fort.24_file>`__. `` (38); ``      - :ref:`NTIF <ntif_parameter>` > 0, :ref:`fort.24 file <fort24>` `` (39). |
| 41–56 | References — raw HTML references 태그, Luettich·Westerink 보고서의 식 (27)·17쪽 지정 및 Ray 문헌·DOI를 포함한다(41–56). 이 파일 자체에는 해당 퍼텐셜 수식 본문이 없다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
