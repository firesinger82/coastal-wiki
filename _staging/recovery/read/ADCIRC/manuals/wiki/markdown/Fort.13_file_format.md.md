---
file: models/ADCIRC/raw/manuals/wiki/markdown/Fort.13_file_format.md
lines: 30
sha256: 0a391ee7ac6ce06bccbe5667b4b120907a91a320612ec23aa9e3528d932fb241
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# Fort.13_file_format.md — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | Fort.13 file format / 머리말과 파일 선두 — 제목·판본 표기·빈 줄을 포함한다(1–4). 입력 변수 한 행이 입력 자료 한 행을 나타내며 빈 줄은 가독성을 위한 것이라고 적는다(5). 격자 식별자와 절점 수·속성 수를 순서대로 제시한다(7–11). 원문: `The basic file structure of the [fort.13 file](/Fort.13_file) is shown below. Each line of input data is represented by a line containing the input variable name(s). Blank lines are only to enhance readability. Loops indicate multiple lines of input. ` (5); `[AGRID](/index.php?title=AGRID&action=edit&redlink=1)` (7); `[NumOfNodes](/index.php?title=NumOfNodes&action=edit&redlink=1)` (9); `[NAttr](/index.php?title=NAttr&action=edit&redlink=1)` (11). |
| 13–21 | 속성(attribute) 기본값 블록 — 각 속성의 이름·단위·절점당 값 수·기본값을 쓰는 반복문을 제시한다(13–20). 기본값의 실제 숫자와 단위의 실제 값은 이 구간에 없다. 원문: `for i = 1 to [NAttr](/index.php?title=NAttr&action=edit&redlink=1)` (13); `[AttrName(i)](/index.php?title=AttrName(i)&action=edit&redlink=1)` (15); `[Units(i)](/index.php?title=Units(i)&action=edit&redlink=1)` (16); `[ValuesPerNode(i)](/index.php?title=ValuesPerNode(i)&action=edit&redlink=1)` (17); `[DefaultAttrVal(i,k)](/index.php?title=DefaultAttrVal(i,k)&action=edit&redlink=1), k = 1, [ValuesPerNode(i)](/index.php?title=ValuesPerNode(i)&action=edit&redlink=1)` (18); `end i loop` (20). |
| 22–30 | 기본값이 아닌 절점 블록 — 속성별 이름과 기본값이 아닌 절점 수를 쓴 뒤 절점 번호와 해당 절점의 속성 값을 반복해서 쓰는 구조를 제시한다(22–30). 원문: `for i = 1 to [NAttr](/index.php?title=NAttr&action=edit&redlink=1)` (22); `[AttrName(i)](/index.php?title=AttrName(i)&action=edit&redlink=1)` (24); `[NumNodesNotDefaultVal(i)](/index.php?title=NumNodesNotDefaultVal(i)&action=edit&redlink=1)` (25); `for j = 1 to [NumNodesNotDefaultVal(i)](/index.php?title=NumNodesNotDefaultVal(i)&action=edit&redlink=1)` (26); `n, ([AttrVal(n,k)](/index.php?title=AttrVal(n,k)&action=edit&redlink=1), k = 1, [ValuesPerNode(i)](/index.php?title=ValuesPerNode(i)&action=edit&redlink=1))` (27); `end j loop` (28); `end i loop` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 7·9·11·13·15–18·22·24–27: 변수 참조 URL에 `action=edit&redlink=1`이 들어 있다. 이 파일은 해당 변수 정의를 본문에 제공하지 않는다.
