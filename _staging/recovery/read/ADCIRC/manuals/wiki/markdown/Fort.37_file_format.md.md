---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.37_file_format.md
lines: 13
sha256: 3336b4c147bc9c148b4e9729b5fc1cbe9c40b016162935fa53e5f86f53d274b6
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.37_file_format.md — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | Fort.37 file format — 문서 제목(1)과 판본 표기 `_revid=672_` (3)를 포함한다. 빈 줄(2·4)을 포함한다. |
| 5–6 | 파일 구조 안내 — 원문은 입력 줄을 굵은 변수명 줄로 나타낸다고 설명한다(5). 빈 줄은 가독성을 위한 것이라고 설명한다(5). 반복문은 여러 입력 줄을 뜻한다고 설명한다(5). 원문: `The basic file structure is shown below. Each line of input is represented by a line containing the input variable name(s) in bold face type. Blank lines are to enhance readability. Loops indicate multiple lines of input.` (5). |
| 7–13 | 파일 형식 — 자료 묶음(data set) 반복 안에 날짜 주석 줄과 해양 경계 절점(ocean boundary node) 반복을 둔다(7–13). 절점별 줄은 k와 m=1,NFEN에 대한 TEMPBC(k,m)을 나열한다(11). 빈 줄(8)을 포함한다. 원문: `for i=1 to [numberOfDataSets](/index.php?title=NumberOfDataSets&action=edit&redlink=1)` (7); `comment line (date)` (9); `for k=1 to [number_of_ocean_boundary_nodes](/index.php?title=Number_of_ocean_boundary_nodes&action=edit&redlink=1)` (10); `k, ([TEMPBC](/index.php?title=TEMPBC&action=edit&redlink=1)(k,m), m=1,[NFEN](/index.php?title=NFEN&action=edit&redlink=1))` (11); `end k loop` (12); `end i loop` (13). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 5·7·10–11: 5행은 변수명이 `bold face type`이라고 설명한다. 7·10–11행의 변수 링크에는 굵게 표시하는 Markdown 표기가 없다.
- 7·10–11: `numberOfDataSets`, `number_of_ocean_boundary_nodes`, `TEMPBC`, `NFEN` 링크 주소에 `action=edit&redlink=1`이 들어 있다.
- 7·10–11: `numberOfDataSets`, `number_of_ocean_boundary_nodes`, `TEMPBC`, `NFEN`의 정의는 이 파일에 없다. `TEMPBC`의 단위도 이 파일에 없다.
