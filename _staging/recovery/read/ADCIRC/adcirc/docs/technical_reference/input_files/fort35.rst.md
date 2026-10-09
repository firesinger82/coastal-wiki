---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort35.rst
lines: 27
sha256: 595cb3f3eecd9eb30ec48413e10285af4555413c764a803b0aa4e2e3de9669f9
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort35.rst — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.35: Level of No Motion Boundary Condition Input File — 3차원 경압 모의(baroclinic simulations)의 무운동면(level of no motion) 경계를 위한 해양 경계 절점 수위 변화 입력이다(6). BCFLAG_LNM 적용 조건을 제시한다(6). 원문: ```The Level of No Motion Boundary Condition Input File (``fort.35``) is used in 3D baroclinic simulations when the :ref:`BCFLAG_LNM <BCFLAG_LNM>` parameter is set to 1 in the ``fort.15`` file. This file specifies elevation changes for ocean boundary nodes.``` (6). |
| 8–21 | File Structure — 자료 집합마다 날짜 주석 줄과 해양 경계 절점 번호·수위 변화의 반복을 입력한다(11–20). 원문: `.. parsed-literal::` (13); `    for i=1 to numberOfDataSets` (15); `        comment line (date)` (16); `        for k=1 to number_of_ocean_boundary_nodes` (17); `            k, elevation_change` (18); `        end k loop` (19); `    end i loop` (20). |
| 22–27 | Notes — 모든 해양 경계 절점의 수위 변화와 집합별 날짜 주석 줄을 제공하도록 안내한다(25–26). 수위 변화는 무운동면 경계조건을 조정한다(27). 원문: `- The elevation changes should be specified for all ocean boundary nodes` (25); `- Each dataset should include a comment line with the date` (26); `- The elevation changes are used to adjust the level of no motion boundary condition ` (27). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
