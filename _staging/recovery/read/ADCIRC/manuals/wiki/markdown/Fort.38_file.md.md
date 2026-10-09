---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.38_file.md
lines: 54
sha256: 0185a6ea16fa2d8723ccc4a71411b591ad7564883d36b8c4dfdf19edcd0ebd0d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.38_file.md — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.38 file / 표면 온도 경계조건(surface temperature boundary condition) — 제목(1)과 판본 표기 `_revid=1112_` (3)를 포함한다. fort.38은 fort.15의 RES_BC_FLAG가 -3, 3, -4 또는 4일 때 읽는다(5). 원문은 이 조건을 측면 온도 경계조건(lateral temperature boundary condition)을 사용하는 경우라고 설명한다(5). 파일 형식은 표면 열 플럭스(surface heat flux) 매개화를 제어하는 BCFLAG_TEMP에 따라 달라진다(5). 원문: `The surface temperature boundary condition input file (fort.38) is read in when the [RES_BC_FLAG](/index.php?title=RES_BC_FLAG&action=edit&redlink=1) is set to -3, 3, -4, or 4 in the [fort.15 file](/Fort.15_file) (i.e., when a lateral temperature boundary condition is being used) and its format depends on the [BCFLAG_TEMP](/index.php?title=BCFLAG_TEMP&action=edit&redlink=1) parameter in the [fort.15 file](/Fort.15_file), which controls the surface heat flux parameterization in ADCIRC.` (5). |
| 7–18 | Contents — File Format, BCFLAG_TEMP의 세 값과 Note로 이동하는 목차를 나열한다(7–17). 조건 표기는 `[1.1 BCFLAG_TEMP=1](#BCFLAG_TEMP=1)` (11); `- [1.2 BCFLAG_TEMP=2](#BCFLAG_TEMP=2)` (13); `- [1.3 BCFLAG_TEMP=3](#BCFLAG_TEMP=3)` (15)이다. 목차 주변 빈 줄(8·10·12·14·16·18)을 포함한다. |
| 19–22 | File Format — 절 제목과 편집 링크(19)를 포함한다. 원문은 입력 줄을 굵은 변수명 줄로 나타낸다고 설명한다(21). 빈 줄은 가독성을 위한 것이라고 설명한다(21). 반복문은 여러 입력 줄을 뜻한다고 설명한다(21). 원문: `The basic file structure is shown below. Each line of input is represented by a line containing the input variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of input.` (21). |
| 23–31 | BCFLAG_TEMP=1 — 이 조건의 절 제목(23) 뒤에 자료 묶음(data set)과 NP 절점 반복을 둔다(25–30). 절점별 줄은 k와 q_heat(k)를 나열한다(28). 원문: ``### `BCFLAG_TEMP=1`[[edit](/index.php?title=Fort.38_file&action=edit&section=2)]`` (23); `for i=1 to [numberOfDataSets](/index.php?title=NumberOfDataSets&action=edit&redlink=1)` (25); `for k=1 to [NP](/index.php?title=NP&action=edit&redlink=1)` (27); `` `k`, `[q_heat(k)](/index.php?title=Q_heat(k)&action=edit&redlink=1)` `` (28); `end k loop` (29); `end i loop` (30). |
| 32–41 | BCFLAG_TEMP=2 — 이 조건의 절 제목(32) 뒤에 자료 묶음 반복과 TMP(K,J)의 J=1,6, K=1,NP 형식을 둔다(34–38). TMP(K,J)는 K번째 수평 격자 절점(horizontal mesh node)의 J번째 표면 열 플럭스 성분이라고 설명한다(40). 원문은 괄호를 암시적 Fortran 입출력 반복문(implicit Fortran i/o loop)의 표기로 설명한다(40). 원문: ``### `BCFLAG_TEMP=2`[[edit](/index.php?title=Fort.38_file&action=edit&section=3)]`` (32); `for i=1 to [numberOfDataSets](/index.php?title=NumberOfDataSets&action=edit&redlink=1)` (34); ``(`K`, (`TMP(K,J)`, J=1,6),K=1,[NP](/index.php?title=NP&action=edit&redlink=1))`` (36); `end i loop` (38); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (40). |
| 42–51 | BCFLAG_TEMP=3 — 이 조건의 절 제목(42) 뒤에 자료 묶음 반복과 TMP(K,J)의 J=1,4, K=1,NP 형식을 둔다(44–48). TMP(K,J)의 의미와 암시적 Fortran 입출력 반복문 설명을 다시 적는다(50). 원문: ``### `BCFLAG_TEMP=3`[[edit](/index.php?title=Fort.38_file&action=edit&section=4)]`` (42); `for i=1 to [numberOfDataSets](/index.php?title=NumberOfDataSets&action=edit&redlink=1)` (44); ``(`K`, (`TMP(K,J)`, J=1,4),K=1,[NP](/index.php?title=NP&action=edit&redlink=1))`` (46); `end i loop` (48); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (50). |
| 52–54 | Note — NP는 위 모든 경우에 수평 격자의 절점 수이며 2차원 전체 영역(2D fulldomain)의 절점 수라고 정의한다(54). 3차원 경압(baroclinic) 물리와 BCFLAG_TEMP 값의 상세 설명은 fort.15 문서로 연결한다(54). 원문: `In all the above cases, NP is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes). See the [fort.15 file](/Fort.15_file) documentation on 3D baroclinic physics (particularly the explanation of various [BCFLAG_TEMP](/index.php?title=BCFLAG_TEMP&action=edit&redlink=1) values) for more details.` (54). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·25·27–28·34·36·44·46·54: `RES_BC_FLAG`, `BCFLAG_TEMP`, `numberOfDataSets`, `NP`, `q_heat(k)` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 21·25–30·34–38·44–48: 21행은 변수명이 `bold face type`이라고 설명한다. 형식 줄의 변수에는 굵게 표시하는 Markdown 표기가 없다.
- 25·28·36·40·46·50: `numberOfDataSets`와 `q_heat(k)`의 정의는 이 파일에 없다. `TMP(K,J)`의 각 성분 이름과 단위도 이 파일에 없다.
