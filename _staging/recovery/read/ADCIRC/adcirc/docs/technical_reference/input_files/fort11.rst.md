---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort11.rst
lines: 119
sha256: c83129265a672cb62d996b58814eeab488401115893480a594dd1817334035fe
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort11.rst — 판독 구간 기록

구간은 1행부터 119행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | Fort.11: Density Initial Condition Input File / File Structure — 경압 계산(baroclinic runs)의 초기 밀도장(density field) 입력이다(6). 2DDI는 아직 지원하지 않는다고 적으며 3차원 경압 실행과 파일 형식의 IDEN 조건을 제시한다(6·11). 원문: ```The ``fort.11`` file is used to specify the initial density field for baroclinic runs. Baroclinic 2DDI runs are not yet supported. Baroclinic 3D runs occur if IDEN is not equal to 0.``` (6); `The file structure varies depending on the value of IDEN in the fort.15 file.` (11). |
| 13–25 | For Baroclinic 2DDI Runs / Density — 밀도(density) 옵션의 두 헤더, 절점 수와 절점별 밀도 입력 형식을 제시한다(13–24). 원문: `For Baroclinic 2DDI Runs:` (13); ``If :ref:`IDEN <IDEN>` = 1 or -1 (Density):`` (15); `.. parsed-literal::` (17); `    Header Line 1` (19); `    Header Line 2` (20); ``     :ref:`NVP <NVP>` `` (21); ``     for k=1 to :ref:`NVP <NVP>` `` (22); ``         :ref:`jki <jki>`, :ref:`DASIGT(jki) <DASIGT>` `` (23); `    end k loop` (24). |
| 26–36 | For Baroclinic 2DDI Runs / Salinity — 염분(salinity) 옵션의 두 헤더, 절점 수와 절점별 염분 입력 형식을 제시한다(26–35). 원문: ``If :ref:`IDEN <IDEN>` = 2 or -2 (Salinity):`` (26); `.. parsed-literal::` (28); `    Header Line 1` (30); `    Header Line 2` (31); ``     :ref:`NVP <NVP>` `` (32); ``     for k=1 to :ref:`NVP <NVP>` `` (33); ``         :ref:`jki <jki>`, :ref:`DASALT(jki) <DASALT>` `` (34); `    end k loop` (35). |
| 37–47 | For Baroclinic 2DDI Runs / Temperature — 수온(temperature) 옵션의 두 헤더, 절점 수와 절점별 수온 입력 형식을 제시한다(37–46). 원문: ``If :ref:`IDEN <IDEN>` = 3 or -3 (Temperature):`` (37); `.. parsed-literal::` (39); `    Header Line 1` (41); `    Header Line 2` (42); ``     :ref:`NVP <NVP>` `` (43); ``     for k=1 to :ref:`NVP <NVP>` `` (44); ``         :ref:`jki <jki>`, :ref:`DATEMP(jki) <DATEMP>` `` (45); `    end k loop` (46). |
| 48–58 | For Baroclinic 2DDI Runs / Temperature and Salinity — 수온·염분 동시 옵션의 두 헤더, 절점 수와 두 값 입력 형식을 제시한다(48–57). 원문: ``If :ref:`IDEN <IDEN>` = 4 or -4 (Temperature and Salinity):`` (48); `.. parsed-literal::` (50); `    Header Line 1` (52); `    Header Line 2` (53); ``     :ref:`NVP <NVP>` `` (54); ``     for k=1 to :ref:`NVP <NVP>` `` (55); ``         :ref:`jki <jki>`, :ref:`DATEMP(jki) <DATEMP>`, :ref:`DASALT(jki) <DASALT>` `` (56); `    end k loop` (57). |
| 59–73 | For Baroclinic 3D Runs / Density — 밀도 옵션의 두 헤더, NVN·NVP 및 중첩 반복의 밀도 입력 형식을 제시한다(59–72). 원문: `For Baroclinic 3D Runs:` (59); ``If :ref:`IDEN <IDEN>` = 1 or -1 (Density):`` (61); `.. parsed-literal::` (63); `    Header Line 1` (65); `    Header Line 2` (66); `    NVN, NVP` (67); `    for k=1 to NVP` (68); `        for j=1 to NVN` (69); `            k, j, SIGT(NHNN,NVNN)` (70); `        end j loop` (71); `    end k loop` (72). |
| 74–86 | For Baroclinic 3D Runs / Salinity — 염분 옵션의 두 헤더, NVN·NVP 및 중첩 반복의 염분 입력 형식을 제시한다(74–85). 원문: ``If :ref:`IDEN <IDEN>` = 2 or -2 (Salinity):`` (74); `.. parsed-literal::` (76); `    Header Line 1` (78); `    Header Line 2` (79); ``     :ref:`NVN <NVN>`, :ref:`NVP <NVP>` `` (80); ``     for k=1 to :ref:`NVP <NVP>` `` (81); ``         for j=1 to :ref:`NVN <NVN>` `` (82); `            k, j, SAL(k,j)` (83); `        end j loop` (84); `    end k loop` (85). |
| 87–99 | For Baroclinic 3D Runs / Temperature — 수온 옵션의 두 헤더, NVN·NVP 및 중첩 반복의 수온 입력 형식을 제시한다(87–98). 원문: ``If :ref:`IDEN <IDEN>` = 3 or -3 (Temperature):`` (87); `.. parsed-literal::` (89); `    Header Line 1` (91); `    Header Line 2` (92); ``     :ref:`NVN <NVN>`, :ref:`NVP <NVP>` `` (93); ``     for k=1 to :ref:`NVP <NVP>` `` (94); ``         for j=1 to :ref:`NVN <NVN>` `` (95); ``             k, j, :ref:`TEMP(k,j) <TEMP>` `` (96); `        end j loop` (97); `    end k loop` (98). |
| 100–112 | For Baroclinic 3D Runs / Temperature and Salinity — 수온·염분 동시 옵션의 두 헤더, NVN·NVP 및 중첩 반복의 두 값 입력 형식을 제시한다(100–111). 원문: ``If :ref:`IDEN <IDEN>` = 4 or -4 (Temperature and Salinity):`` (100); `.. parsed-literal::` (102); `    Header Line 1` (104); `    Header Line 2` (105); ``     :ref:`NVN <NVN>`, :ref:`NVP <NVP>` `` (106); ``     for k=1 to :ref:`NVP <NVP>` `` (107); ``         for j=1 to :ref:`NVN <NVN>` `` (108); `            k, j, TEMP(k,j),SAL(k,j)` (109); `        end j loop` (110); `    end k loop` (111). |
| 113–119 | Notes — 3차원에서 j=1은 저층(bottom layer), j=NVN은 표층(surface layer)이다(116). IDEN에 따른 형식과 2DDI 미지원 및 3차원 경압 적용 조건을 재명시한다(117–119). 원문: `- For 3D runs, j=1 represents the bottom layer and j=NVN represents the surface layer` (116); `- The file structure depends on the value of IDEN specified in the fort.15 file` (117); `- Baroclinic 2DDI runs are not yet supported` (118); `- Baroclinic 3D runs occur when IDEN is not equal to 0 ` (119). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 6·13–57·118행: 2DDI 경압 실행은 아직 지원하지 않는다고 명시하면서 그 실행에 대한 네 가지 파일 형식을 제시한다.
- 68–70행: 밀도 입력의 반복 변수와 입력 앞 두 필드는 `k`, `j`이지만 배열 표기는 `SIGT(NHNN,NVNN)`이다. 이 형식 블록에 `NHNN`과 `NVNN`을 설정하는 행은 없다.
