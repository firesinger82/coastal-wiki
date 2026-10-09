---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort36.rst
lines: 29
sha256: 0d5dce510eb2bba1e05a0fe5b54afff2a461adeeaa4c8ca572344a484dcb46dc
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort36.rst — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.36: Salinity Boundary Condition Input File — 서로 다른 수직 층(vertical levels)의 해양 경계 절점 염분(salinity) 입력이며 RES_BC_FLAG 적용 조건을 제시한다(6). 원문: ```The Salinity Boundary Condition Input File (``fort.36``) is used when the :ref:`RES_BC_FLAG <RES_BC_FLAG>` parameter is set to -2, 2, -4, or 4 in the ``fort.15`` file. This file specifies salinity values for ocean boundary nodes at different vertical levels.``` (6). |
| 8–21 | File Structure — 자료 집합별 날짜 주석과 해양 경계 절점별 번호·수직 층 염분의 반복 형식이다(11–20). 원문: `.. parsed-literal::` (13); `    for i=1 to numberOfDataSets` (15); `        comment line (date)` (16); `        for k=1 to number_of_ocean_boundary_nodes` (17); ``            k, (SALBC(k,m), m=1, :ref:`NFEN <NFEN>`)`` (18); `        end k loop` (19); `    end i loop` (20). |
| 22–29 | Notes — 적용 조건, 모든 해양 경계 절점 값과 날짜 주석 줄을 제시한다(25–27). SALBC의 절점·층 첨자와 NFEN의 수직 층 수 정의를 적는다(28–29). 원문: ``- This file is only required when running simulations with :ref:`RES_BC_FLAG <RES_BC_FLAG>` = -2, 2, -4, or 4`` (25); `- The salinity values should be specified for all ocean boundary nodes` (26); `- Each dataset should include a comment line with the date` (27); `- SALBC(k,m) represents the salinity value at node k and vertical level m` (28); `- NFEN is the number of vertical levels in the model ` (29). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
