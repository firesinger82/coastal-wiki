---
file: models/ShorelineS/raw/source_code/shorelines/functions/select_multi_polygon.m
lines: 99
sha256: 0791ede9e1f086b41c89ccafde53d6126e8981583c4b9d5aacc820aa7b0b668a
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# select_multi_polygon.m — 판독 구간 기록

구간은 1행부터 99행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 함수 시그니처는 `function [xi,yi]=select_multi_polygon(col)` (1). 주석은 수심(bathymetry)에 포함할 다각형(polygon)을 색상 col로 선택하고 m 단위 xi·yi를 반환한다고 설명한다(2–12). S 구조체 인수와 S 필드 기본값은 없다. 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄을 포함한다(13–40). |
| 41–66 | hold on 뒤 xi·yi를 비우고 n을 0으로 초기화한다(41–43). `finished=0;` (45). `while ~finished` (46)에서 nold에 n을 복사하고 `but = 1;` (48). `while but == 1` (49)은 ginput(1)을 호출한다(50). `if but==1` (51)이면 `n = n+1;` (52), xi·yi에 선택 좌표 복사(53–54), 선택 선과 점 표시(55). `if nold==n \|\| but==113 \|\| but==27` (58)이면 `finished=1;` (59). 주석은 113·27을 q·escape로 설명한다. `else` (60)는 `n=n+1;` (61) 뒤 xi·yi에 NaN 구분자를 대입한다(62–63). 내부 조건과 두 루프 종료·빈 줄을 포함한다. |
| 67–92 | `idnan = find(isnan(xi));` (68), xi2·yi2 빈 배열 초기화(69–70). `if length(idnan)>=1` (71) 안에서 `if idnan(1)>1` (72)이면 `idnan=[0;idnan(:)]';` (73). `if ~isnan(xi(n))` (75)이면 `xi=[xi,nan];` (76), `yi=[yi,nan];` (77), `n=n+1;` (78), `idnan=[idnan,n];` (79). `id = diff(idnan)-1;` (81). `for mm=1:length(id)` (82)에서 `if id(mm)>1` (83)이면 `xi2 = [xi2,xi(idnan(mm)+1:idnan(mm+1))];` (84), `yi2 = [yi2,yi(idnan(mm)+1:idnan(mm+1))];` (85)로 두 점 이상인 요소와 뒤 NaN을 남긴다. xi2·yi2를 결과에 복사하고 `n=length(xi);` (90). 내부 조건·루프·바깥 조건 종료와 빈 줄을 포함한다. |
| 93–99 | `if n>0&&isnan(xi(n))` (94)이면 `xi=xi(1:n-1);` (95), `yi=yi(1:n-1);` (96)로 마지막 NaN을 제거한다. 주석·조건 종료·빈 줄·함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 58–64: 새 점이 없거나 q·escape이면 종료한다. 그 외 입력은 NaN을 붙여 다음 요소를 시작한다. 오른쪽 마우스 버튼 값만 따로 검사하는 조건은 없다.
- 67–91: 단일 점 제거 루프는 NaN 구분자가 하나 이상 있을 때만 실행한다.
- 53–54·84–96: 선택 좌표를 저장하고 요소를 정리한다. 첫 점을 마지막 점에 다시 붙여 다각형을 닫는 문장은 없다.
