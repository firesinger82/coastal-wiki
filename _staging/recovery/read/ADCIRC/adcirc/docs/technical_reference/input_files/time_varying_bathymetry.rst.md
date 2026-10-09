---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/time_varying_bathymetry.rst
lines: 51
sha256: c7eab6c6d584092362b6f9b50353627ae23c414f69072a0c5950cfaa41abb241
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# time_varying_bathymetry.rst — 판독 구간 기록

구간은 1행부터 51행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.141: Time Varying Bathymetry Input File — fort.14의 NDDT가 0이 아니면 시간 가변 수심(time varying bathymetry) 파일을 사용한다(6). NDDT 값에 따른 두 변형을 소개한다(6). 원문: ```The ADCIRC Time Varying Bathymetry Input File (``fort.141``) is used by ADCIRC whenever the :ref:`NDDT <NDDT>` value in the ``fort.14`` is nonzero. There are two variations of this file, depending on the value of :ref:`NDDT <NDDT>`.``` (6). |
| 8–25 | Full Domain Bathymetry Change — NDDT가 +/-1이면 각 자료 집합(data set)이 전체 영역을 덮는다(11). 자료 집합·전체 절점 순회의 파일 형식을 제시한다(15–19). NP는 수평 격자 절점 수이고 j는 절점 번호이다(22–23). depth(j)의 의미는 fort.14의 DP와 같다(24). 원문: ``If :ref:`NDDT <NDDT>` is +/-1, then each bathymetry dataset in the file covers the full domain, and the file format is as follows:`` (11); `.. parsed-literal::` (13); `    for i=1 to numDataSets` (15); ``         for j=1 to :ref:`NP <NP>` `` (16); `            j, depth(j)` (17); `        end j loop` (18); `    end i loop` (19); `where:` (21); ``- :ref:`NP <NP>` is the number of nodes in the horizontal mesh`` (22); `- j is the node number` (23); ```- depth(j) has the same meaning as DP in the mesh file (``fort.14``)``` (24). |
| 26–39 | Limited Area Bathymetry Change — NDDT가 +/-2이면 각 자료 집합은 영역 일부만 덮는다(29). 자료 집합 시작의 해시 표지(hash mark)와 해당 절점별 수심 기록 형식을 제시한다(31–38). 원문: ```If :ref:`NDDT <NDDT>` is +/-2, then each dataset in the ``fort.141`` file covers only part of the domain, and the file format is as follows:``` (29); `.. parsed-literal::` (31); `    for i=1 to numDataSets` (33); `        "#"` (34); `        for j=1 to areaNodes` (35); `            j, depth(j)` (36); `        end j loop` (37); `    end i loop` (38). |
| 40–51 | Notes — NDDT의 사용 조건을 반복한다(43). +/-1에서는 모든 절점과 NP개의 고정 기록 수가 필요하다(44–46). +/-2에서는 자료 집합마다 절점 부분집합이 달라도 된다(47–48). 자료 집합을 구분하는 #는 줄의 두 번째 열에 둔다(49). 시간에 따라 수심이 변하는 절점 수가 달라질 수 있다(50). depth의 의미를 다시 제시한다(51). 원문: ``- This file is only required when :ref:`NDDT <NDDT>` is nonzero`` (43); `- For NDDT=+/-1:` (44); `  - Each dataset must cover all nodes in the domain` (45); `  - The number of records per dataset is fixed (equal to NP)` (46); `- For NDDT=+/-2:` (47); `  - Each dataset can cover a different subset of nodes` (48); `  - The separation between datasets is achieved by placing a hash mark ("#") in the second column of a line` (49); `  - This allows for simulations where the number of nodes that change their bathymetry varies over time` (50); ```- The depth values have the same meaning as the DP values in the mesh file (``fort.14``) ``` (51). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 15·33·35행: `numDataSets`와 `areaNodes`가 파일 형식의 반복 상한에 쓰인다. 이 파일은 두 이름을 별도로 정의하지 않는다.
