---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort38.rst
lines: 50
sha256: b788188bbda476fdbf6bd4204f33363a4aa15f57155465b5519261411e368651
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort38.rst — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | Fort.38: Surface Temperature Boundary Values Input File / File Structure — 측면 수온 경계조건(lateral temperature boundary condition)을 쓰는 RES_BC_FLAG 조건의 입력이다(6). 표면 열 플럭스(surface heat flux) 매개변수화(parameterization) 옵션 BCFLAG_TEMP에 따라 형식이 달라진다고 적는다(6·11). 원문: ```The Surface Temperature Boundary Values Input File (``fort.38``) is used when the :ref:`RES_BC_FLAG <RES_BC_FLAG>` parameter is set to -3, 3, -4, or 4 in the ``fort.15`` file (i.e., when a lateral temperature boundary condition is being used). The format of this file depends on the :ref:`BCFLAG_TEMP <BCFLAG_TEMP>` parameter in the ``fort.15``, which controls the surface heat flux parameterization in ADCIRC.``` (6); ``The file format varies depending on the value of :ref:`BCFLAG_TEMP <BCFLAG_TEMP>`:`` (11). |
| 13–22 | BCFLAG_TEMP=1 — 집합별로 수평 절점 수만큼 절점 번호와 열 플럭스를 입력하는 반복이다(13–21). 원문: `1. If BCFLAG_TEMP=1:` (13); `.. parsed-literal::` (15); `    for i=1 to numberOfDataSets` (17); ``         for k=1 to :ref:`NP <NP>` `` (18); `            k, q_heat(k)` (19); `        end k loop` (20); `    end i loop` (21). |
| 23–30 | BCFLAG_TEMP=2 — 집합별로 전체 수평 절점에 여섯 TMP 성분을 입력하는 암시적 Fortran 입출력 반복(implicit Fortran i/o loop) 형식이다(23–29). 원문: `2. If BCFLAG_TEMP=2:` (23); `.. parsed-literal::` (25); `    for i=1 to numberOfDataSets` (27); ``        (K, (TMP(K,J), J=1,6),K=1, :ref:`NP <NP>`)`` (28); `    end i loop` (29). |
| 31–38 | BCFLAG_TEMP=3 — 집합별로 전체 수평 절점에 네 TMP 성분을 입력하는 암시적 Fortran 입출력 반복 형식이다(31–37). 원문: `3. If BCFLAG_TEMP=3:` (31); `.. parsed-literal::` (33); `    for i=1 to numberOfDataSets` (35); ``        (K, (TMP(K,J), J=1,4),K=1, :ref:`NP <NP>`)`` (36); `    end i loop` (37). |
| 39–50 | Notes — 적용 조건과 2차원 전체 영역(2D fulldomain)의 절점 수를 정의한다(42–43). TMP의 절점·성분 첨자, 옵션별 여섯·네 성분과 q_heat의 절점 열 플럭스 정의를 제시한다(44–50). 원문: ``- This file is only required when running simulations with :ref:`RES_BC_FLAG <RES_BC_FLAG>` = -3, 3, -4, or 4`` (42); `- NP is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes)` (43); `- For BCFLAG_TEMP=2 and 3:` (44); `  - TMP(K,J) represents the Jth heat flux component for the Kth horizontal mesh node` (45); `  - The data are read using an implicit Fortran i/o loop, hence the parentheses` (46); `  - BCFLAG_TEMP=2 requires 6 heat flux components` (47); `  - BCFLAG_TEMP=3 requires 4 heat flux components` (48); `- For BCFLAG_TEMP=1:` (49); `  - q_heat(k) represents the heat flux at node k` (50). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
