---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort39.rst
lines: 35
sha256: bc3c513ebb4e2f64b8c28d5977c0b2c798f76763fef11e82581706490208dd20
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort39.rst — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.39: Salinity and Temperature River Boundary Values Input File — 하천 경계의 염분(salinity)과 수온(temperature) 입력 파일이다(3–6). 격자 파일에 경압성 하천 경계(baroclinic river boundary)가 있고 IDEN이 양수일 때 사용한다(6). 원문: ```The Salinity and Temperature River Boundary Values Input File (``fort.39``) is used when the mesh file (``fort.14``) contains a baroclinic river boundary (IBTYPE=122) and :ref:`IDEN <IDEN>` is positive.``` (6). |
| 8–26 | File Structure — 자료 집합(data set)과 하천 경계 절점(river boundary node)의 순서로 수직 층별 경계값을 읽는 형식을 제시한다(15–21). RIVBCTIMINC는 자료 집합 사이의 초 단위 간격이다(24). RIVBCSTATIM은 초기 시작(cold start) 시각을 기준으로 한 자료 시작 시각이며 단위는 초이다(25). 원문: `The file format is as follows:` (11); `.. parsed-literal::` (13); `    RIVBCTIMINC, RIVBCSTATIM` (15); `    for i=1 to numberOfDataSets` (17); `        for j=1 to number_of_river_boundary_nodes` (18); ``            (bc(j,k), k=1, :ref:`NFEN <NFEN>`)`` (19); `        end j loop` (20); `    end i loop` (21); `where:` (23); `- RIVBCTIMINC is the time increment (in seconds) between the boundary condition datasets` (24); `- RIVBCSTATIM is the time (in seconds) when the boundary condition data start, relative to the cold start time` (25). |
| 27–35 | Notes — 파일의 필요 조건을 다시 제시한다(30). IDEN=2는 염분 경계값을 뜻한다(32). IDEN=3은 수온 경계값을 뜻한다(33). IDEN=4에서는 bc(j,k)를 salbc(j,k),tempbc(j,k)로 대체해야 한다(34). NFEN은 수직 층수이다(35). 원문: ``- This file is only required when using baroclinic river boundaries (IBTYPE=122) with positive :ref:`IDEN <IDEN>` values`` (30); ``- The bc(j,k) values depend on the value of :ref:`IDEN <IDEN>`:`` (31); `  - If IDEN=2: bc(j,k) represents salinity boundary condition values` (32); `  - If IDEN=3: bc(j,k) represents temperature boundary condition values` (33); `  - If IDEN=4: bc(j,k) should be replaced with salbc(j,k),tempbc(j,k)` (34); `- NFEN is the number of vertical levels in the model ` (35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
