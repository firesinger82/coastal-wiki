---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.38_file_format.md
lines: 48
sha256: df34aa3009af5b4e144c7535b4bf06c3fe1d31510be45157a0352ad33f567945
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.38_file_format.md — 판독 구간 기록

구간은 1행부터 48행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | Fort.38 file format / 파일 구조 안내 — 제목(1)과 판본 표기 `_revid=674_` (3)를 포함한다. 원문은 입력 줄을 굵은 변수명 줄로 나타낸다고 설명한다(5). 빈 줄은 가독성을 위한 것이라고 설명한다(5). 반복문은 여러 입력 줄을 뜻한다고 설명한다(5). 원문: `The basic file structure is shown below. Each line of input is represented by a line containing the input variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of input.` (5). |
| 7–16 | Contents — BCFLAG_TEMP의 세 값과 Note로 이동하는 목차를 나열한다(7–15). 조건 표기는 `- [1 BCFLAG_TEMP=1](#BCFLAG_TEMP=1)` (9); `- [2 BCFLAG_TEMP=2](#BCFLAG_TEMP=2)` (11); `- [3 BCFLAG_TEMP=3](#BCFLAG_TEMP=3)` (13)이다. 목차 주변 빈 줄(8·10·12·14·16)을 포함한다. |
| 17–25 | BCFLAG_TEMP=1 — 이 조건의 절 제목(17) 뒤에 자료 묶음(data set)과 NP 절점 반복을 둔다(19–24). 절점별 줄은 k와 q_heat(k)를 나열한다(22). 원문: `## BCFLAG_TEMP=1[[edit](/index.php?title=Fort.38_file_format&action=edit&section=1)]` (17); `for i=1 to [numberOfDataSets](/index.php?title=NumberOfDataSets&action=edit&redlink=1)` (19); `for k=1 to [NP](/index.php?title=NP&action=edit&redlink=1)` (21); `k, [q_heat(k)](/index.php?title=Q_heat(k)&action=edit&redlink=1)` (22); `end k loop` (23); `end i loop` (24). |
| 26–35 | BCFLAG_TEMP=2 — 이 조건의 절 제목(26) 뒤에 자료 묶음 반복과 TMP(K,J)의 J=1,6, K=1,NP 형식을 둔다(28–32). TMP(K,J)는 K번째 수평 격자 절점(horizontal mesh node)의 J번째 표면 열 플럭스(surface heat flux) 성분이라고 설명한다(34). 원문은 괄호를 암시적 Fortran 입출력 반복문(implicit Fortran i/o loop)의 표기로 설명한다(34). 원문: `## BCFLAG_TEMP=2[[edit](/index.php?title=Fort.38_file_format&action=edit&section=2)]` (26); `for i=1 to numberOfDataSets` (28); `(K, (TMP(K,J), J=1,6),K=1,NP)` (30); `end i loop` (32); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (34). |
| 36–45 | BCFLAG_TEMP=3 — 이 조건의 절 제목(36) 뒤에 자료 묶음 반복과 TMP(K,J)의 J=1,4, K=1,NP 형식을 둔다(38–42). TMP(K,J)의 의미와 암시적 Fortran 입출력 반복문 설명을 다시 적는다(44). 원문: `## BCFLAG_TEMP=3[[edit](/index.php?title=Fort.38_file_format&action=edit&section=3)]` (36); `for i=1 to numberOfDataSets` (38); `(K, (TMP(K,J), J=1,4),K=1,NP)` (40); `end i loop` (42); `where TMP(K,J) is the surface heat flux parameter Jth heat flux component for the Kth horizontal mesh node. The data are read using an implicit Fortran i/o loop, thus the parentheses around the statement.` (44). |
| 46–48 | Note — NP는 위 모든 경우에 수평 격자의 절점 수이며 2차원 전체 영역(2D fulldomain)의 절점 수라고 정의한다(48). 3차원 경압(baroclinic) 물리와 BCFLAG_TEMP 값의 상세 설명은 fort.15 문서로 연결한다(48). 원문: `In all the above cases, NP is the number of nodes in the horizontal mesh (i.e., the 2D fulldomain number of nodes). See the [fort.15 file](/Fort.15_file) documentation on 3D baroclinic physics (particularly the explanation of various [BCFLAG_TEMP](/index.php?title=BCFLAG_TEMP&action=edit&redlink=1) values) for more details.` (48). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·19–24·28–32·38–42: 5행은 변수명이 `bold face type`이라고 설명한다. 형식 줄의 변수에는 굵게 표시하는 Markdown 표기가 없다.
- 19·21–22·48: `numberOfDataSets`, `NP`, `q_heat(k)`, `BCFLAG_TEMP` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 19·22·28·30·34·38·40·44: `numberOfDataSets`와 `q_heat(k)`의 정의는 이 파일에 없다. `TMP(K,J)`의 각 성분 이름과 단위도 이 파일에 없다.
